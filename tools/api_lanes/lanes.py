#!/usr/bin/env python3
"""lanes.py: generic API lane runner for the harness (build -> run -> export).

One lane = one independent run of a model on one exact task with its attachments (METHODOLOGY
glossary). This script calls the Anthropic API directly with the official `anthropic` SDK. It
requires API_KEYS = yes in RESOURCES.md; without a key the harness runs lanes as fresh subagents or
fresh passes instead (METHODOLOGY 4, preamble).

Subcommands
  build   SPEC.jsonl RUNDIR [--allow-cuts] [--forbidden a,b,c]
  run     RUNDIR [--workers N] [--stagger S] [--model-default ID] [--task-budget N] [--fallbacks]
  export  RUNDIR
  layered SPEC.jsonl RUNPREFIX [--workers N] [--attempts 3]
  census  RUNDIR [RUNDIR ...]

Spec line (one JSON object per line):
  {"id": "P0001",
   "out": "/abs/path/new_file.md",            # written by export; never overwritten (_v2, _v3 ...)
   "task": "Prove exactly: ...",              # the exact task; for review, the deciding question
   "files": ["/abs/f.md", "/abs/g.tex:120-260"],   # one range per entry; the text under review LAST
   "role": "prove" | "review" | "read",       # picks the preamble; default "prove"
   "model": "...", "max_tokens": 64000, "effort": "max"}   # all optional

Defaults: model from --model-default, else env LANES_MODEL, else "claude-opus-5-5" (the current
default model; "claude-fable-5-1" is the most capable and is what a project with top-effort provers
usually sets in RESOURCES.md STRONGEST_MODEL). max_tokens from env LANES_MAX_TOKENS else 64000
(streaming, so a large cap is safe; set OUTPUT_CAP from RESOURCES.md). effort from env LANES_EFFORT
else "max". Thinking is adaptive on every current model; the readable summary is requested so a lane
that wrote no text still leaves a trace of what it was doing.

Caps (env, bytes): LANES_ATTACHMENT_CAP (default 55000 = ATTACHMENT_CAP), LANES_PROMPT_CAP (default
400000). An attachment over its cap is cut and marked; a prompt over its cap is cut from the END,
which is where the text under review sits, so build ABORTS on any cut unless --allow-cuts.

Credentials: ANTHROPIC_API_KEY from the environment, or from the file named by
ANTHROPIC_SECRETS_FILE (mode 600, a line "ANTHROPIC_API_KEY=..."). The key is never printed, never
written to a run dir, never put in a prompt. With no key set, the SDK may still find an `ant auth
login` profile; this script does not interfere with that.

Outputs in RUNDIR: SPEC.jsonl (copy), IN.jsonl (built requests), OUT.jsonl (one line per landed
lane: id, model, text, stop_reason, stop_details, usage, thinking_chars or thinking, error),
journal/<id>.txt (partial text while streaming; survives a crash), EXPORTED.txt (ids written).
A lane whose stop_reason is max_tokens with no text is exported as <out>_VOID.md and is NOT a
result (METHODOLOGY 4.6). Re-running `run` on the same RUNDIR retries only the lanes without a
clean line in OUT.jsonl.

Stdlib + anthropic only. Never run this in a loop; the harness launches each lane batch as one
tracked background job (METHODOLOGY 4.8).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

# ---------------------------------------------------------------- preambles (generic, role-specific)

COMMON_RULES = (
    "You are a mathematical referee and prover working inside a research programme in mathematics or "
    "theoretical physics. You see only the EXCERPTS below (every line is prefixed with its line number) "
    "and you may use printed literature you know precisely, citing it exactly. Work only from these. "
    "When an input is missing say 'not in the excerpts'; never guess, never invent a source. Write "
    "mathematics only: precise statements, complete proofs or precise counterexamples, every constant "
    "tracked with its rounding direction (upper bounds rounded up, lower bounds and thresholds down). "
    "Quote the consumer line you are asked to serve before you begin, and check that what you prove "
    "or review is in exactly that form (direction, sign, norm, set, scale, quantifiers): neither "
    "stronger nor weaker. State the scale and the uniformity in words. "
    "WRITE-EARLY RULE: your thinking and your answer share one output budget, and long proofs have "
    "ended with no text at all. Within the first quarter of your budget write the RESULT section: the "
    "statement, the status word, and either the failing step or the proof skeleton. Then write each "
    "step as it is done. By half of your budget the partial result must be on the page. Unfinished "
    "parts are written out as NAMED inputs (exact statement, where consumed), never left silent. "
    "If you run out, what is written stands; label the rest PARTIAL. Answer in Markdown, about 4000 "
    "words at most unless the task says otherwise."
)

ROLE_RULES = {
    "prove": (
        "ROLE: PROVER. Prove the target EXACTLY as written. Your first line is 'FINAL STATUS: <word>' "
        "with exactly one of PROVED / PROVED-WEAKER / REFUTED / NOT PROVED, followed by one sentence. "
        "PROVED-WEAKER states the exact weaker statement you proved and the loss. REFUTED gives the "
        "counterexample explicitly. NOT PROVED names the exact failing step. 'Derived given X' is "
        "allowed ONLY when X is attached as of record; a reduction to a new unproved statement is NOT "
        "a result and must be reported as NOT PROVED with the new statement named. Do not check or "
        "review; prove."
    ),
    "review": (
        "ROLE: REVIEWER (one lens of an independent pair). Your first line is 'VERDICT: <word>' with "
        "exactly one of APPROVED / APPROVED_WITH_MINOR / NOT APPROVED. Then 'Most serious issue: ...' "
        "in one sentence. Then numbered findings, each with file:line and classed CLERICAL or "
        "MATHEMATICAL. CLERICAL = a citation or line number, a digit or rounding that changes no "
        "conclusion and drops no room below its criterion, wording, a stale label, a build defect, a "
        "missing retraction. MATHEMATICAL (the default) = a false step, a wrong object, a missing or "
        "changed hypothesis or scope, an unproved claim, a change in a quantity's size, a missing "
        "named input, the supply status of a named input, a false displayed constant even when "
        "harmless, a lapsed guard clause. End with 'Required for approval:' as a numbered list, or "
        "'Required for approval: none'. Check that the closing statement matches the consumer line. "
        "You cannot run code: recompute analytically or by hand-checkable arithmetic at a few points."
    ),
    "read": (
        "ROLE: READER. Answer the reading question from the attached pages only. Quote the carrier line "
        "(page:line) first, verbatim, then state the reading, then price the counter-reading if the "
        "page admits one. Your first line is 'READ: <FOUND | NOT IN THE EXCERPTS | AMBIGUOUS>'. A "
        "reading without a quoted carrier is not a reading."
    ),
}

CUT_ATTACH = "[... cut at the attachment cap; ask for the rest by line range ...]"
CUT_PROMPT = "[... excerpts cut at the prompt cap ...]"
MISSING = "MISSING:"


# ---------------------------------------------------------------- helpers

def env_int(name, default):
    try:
        return int(os.environ.get(name, default))
    except ValueError:
        return int(default)


def load_secret():
    """Make ANTHROPIC_API_KEY available to the SDK from ANTHROPIC_SECRETS_FILE if it is not already set.
    The value is never printed. Returns True if a key is now in the environment."""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return True
    f = os.environ.get("ANTHROPIC_SECRETS_FILE")
    if f and os.path.isfile(f):
        with open(f) as fh:
            for line in fh:
                line = line.strip()
                if line.startswith("ANTHROPIC_API_KEY=") and not line.startswith("#"):
                    os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
                    return True
    return False


def parse_file_spec(spec):
    """'/abs/f.md' or '/abs/f.md:120-260' -> (path, (lo, hi) or None). One range per entry."""
    m = re.match(r"^(.*?):(\d+)-(\d+)$", spec)
    if m:
        return m.group(1), (int(m.group(2)), int(m.group(3)))
    m = re.match(r"^(.*?):(\d+)$", spec)
    if m:
        n = int(m.group(2))
        return m.group(1), (n, n)
    return spec, None


def excerpt(spec, forbidden, cap):
    """Return (text, flags). flags: set of 'MISSING', 'CUT', 'FORBIDDEN'."""
    path, rng = parse_file_spec(spec)
    flags = set()
    for f in forbidden:
        if f and f in path:
            flags.add("FORBIDDEN")
            return f"\n===== FILE {path} REFUSED (forbidden source) =====\n", flags
    if not os.path.isfile(path):
        flags.add("MISSING")
        return f"\n===== FILE {path} {MISSING} not found =====\n", flags
    with open(path, errors="replace") as fh:
        lines = fh.read().split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    n = len(lines)
    lo, hi = rng if rng else (1, n)
    if rng and (lo < 1 or hi < lo or lo > n):
        flags.add("MISSING")
        return f"\n===== FILE {path} {MISSING} range {lo}-{hi} outside 1-{n} =====\n", flags
    hi = min(hi, n)
    body = "\n".join(f"{i}: {lines[i - 1]}" for i in range(lo, hi + 1))
    if len(body.encode("utf-8")) > cap:
        body = body.encode("utf-8")[:cap].decode("utf-8", errors="ignore") + "\n" + CUT_ATTACH
        flags.add("CUT")
    head = f"\n===== FILE {path}" + (f" (lines {lo}-{hi})" if rng else f" (lines 1-{n})") + " =====\n"
    return head + body + "\n", flags


def open_new(path, mode="x"):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    return open(path, mode, encoding="utf-8")


def read_jsonl(path):
    if not os.path.isfile(path):
        return []
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out


# ---------------------------------------------------------------- build

def build(spec_path, rundir, allow_cuts=False, forbidden=()):
    attach_cap = env_int("LANES_ATTACHMENT_CAP", 55000)
    prompt_cap = env_int("LANES_PROMPT_CAP", 400000)
    model_default = os.environ.get("LANES_MODEL", "claude-opus-5-5")
    max_tokens_default = env_int("LANES_MAX_TOKENS", 64000)
    effort_default = os.environ.get("LANES_EFFORT", "max")
    os.makedirs(rundir, exist_ok=False)
    reqs, sizes, n_cut, n_missing, n_forbidden = [], [], 0, 0, 0
    with open(spec_path, encoding="utf-8") as fh:
        spec_lines = [l for l in fh.read().splitlines() if l.strip()]
    for l in spec_lines:
        s = json.loads(l)
        role = s.get("role", "prove")
        if role not in ROLE_RULES:
            raise SystemExit(f"{s.get('id')}: unknown role {role!r}; use prove | review | read")
        ctx = ""
        for f in s.get("files", []):
            text, flags = excerpt(f, forbidden, attach_cap)
            n_cut += "CUT" in flags
            n_missing += "MISSING" in flags
            n_forbidden += "FORBIDDEN" in flags
            ctx += text
        if len(ctx.encode("utf-8")) > prompt_cap:
            ctx = ctx.encode("utf-8")[:prompt_cap].decode("utf-8", errors="ignore") + "\n" + CUT_PROMPT
            n_cut += 1
        prompt = f"{COMMON_RULES}\n\n{ROLE_RULES[role]}\n\nTASK ({s['id']}):\n{s['task']}\n\nEXCERPTS:{ctx}"
        reqs.append({
            "id": s["id"],
            "prompt": prompt,
            "model": s.get("model", model_default),
            "max_tokens": int(s.get("max_tokens", max_tokens_default)),
            "effort": s.get("effort", effort_default),
            "role": role,
        })
        sizes.append(len(prompt.encode("utf-8")) // 1024)
    with open_new(os.path.join(rundir, "IN.jsonl")) as f:
        for r in reqs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open_new(os.path.join(rundir, "SPEC.jsonl")) as f:
        f.write("\n".join(spec_lines) + "\n")
    print(f"built {len(reqs)} requests; prompt sizes KB: {sizes}; cut markers {n_cut}; "
          f"MISSING {n_missing}; forbidden refused {n_forbidden}")
    if n_forbidden:
        raise SystemExit("ABORT: a forbidden source was named; fix the spec (nothing was sent).")
    if (n_cut or n_missing) and not allow_cuts:
        raise SystemExit("ABORT: cut markers or MISSING attachments; fix ranges or pass --allow-cuts "
                         "(METHODOLOGY 4.7: a cut text under review is a lost lane).")
    return len(reqs)


# ---------------------------------------------------------------- run

def _one_request(client, r, rundir, task_budget, fallbacks):
    """Run one lane with streaming; journal partial text; keep partial text on error."""
    import anthropic  # local import so build/export work without the SDK installed

    out = {"id": r.get("id"), "model": r.get("model"), "text": None, "stop_reason": None,
           "stop_details": None, "usage": None, "error": None}
    jpath = os.path.join(rundir, "journal", f"{r.get('id')}.txt")
    os.makedirs(os.path.dirname(jpath), exist_ok=True)
    buf, tbuf, last = [], [], 0

    kw = dict(
        model=r.get("model"),
        max_tokens=int(r.get("max_tokens", 64000)),
        messages=[{"role": "user", "content": r["prompt"]}],
        thinking={"type": "adaptive", "display": "summarized"},
        output_config={"effort": r.get("effort", "max")},
    )
    use_beta = False
    betas = []
    if task_budget:
        kw["output_config"]["task_budget"] = {"type": "tokens", "total": int(task_budget)}
        betas.append("task-budgets-2026-03-13")
        use_beta = True
    if fallbacks:
        kw["fallbacks"] = "default"
        betas.append("server-side-fallback-2026-07-01")
        use_beta = True

    def journal():
        with open(jpath, "w", encoding="utf-8") as jf:
            jf.write("".join(buf))

    attempts = 0
    while True:
        attempts += 1
        try:
            streamer = (client.beta.messages.stream(betas=betas, **kw) if use_beta
                        else client.messages.stream(**kw))
            with streamer as st:
                for ev in st:
                    if ev.type == "content_block_delta":
                        if ev.delta.type == "text_delta":
                            buf.append(ev.delta.text)
                            n = sum(len(x) for x in buf)
                            if n - last >= 3000:
                                journal()
                                last = n
                        elif ev.delta.type == "thinking_delta":
                            tbuf.append(ev.delta.thinking or "")
                m = st.get_final_message()
            out["text"] = "".join(b.text for b in m.content if b.type == "text")
            th = "".join((getattr(b, "thinking", "") or "") for b in m.content if b.type == "thinking") \
                or "".join(tbuf)
            if out["text"]:
                out["thinking_chars"] = len(th)
            else:
                out["thinking"] = th  # no text at all: keep the summary so the lane can be re-cut
            out["stop_reason"] = m.stop_reason
            sd = getattr(m, "stop_details", None)
            if m.stop_reason == "refusal" and sd is not None:
                out["stop_details"] = {"category": getattr(sd, "category", None),
                                       "explanation": getattr(sd, "explanation", None)}
            out["usage"] = {"input_tokens": m.usage.input_tokens, "output_tokens": m.usage.output_tokens}
            journal()
            return out
        except anthropic.RateLimitError as e:
            if attempts <= 6:
                time.sleep(min(60 * attempts, 300))
                continue
            out["error"] = f"RateLimitError after {attempts} attempts: {str(e)[:200]}"
        except anthropic.APIStatusError as e:
            if getattr(e, "type", "") == "overloaded_error" or e.status_code >= 500:
                if attempts <= 6:
                    time.sleep(min(60 * attempts, 300))
                    continue
            out["error"] = f"APIStatusError {e.status_code} {getattr(e, 'type', '')}: {str(e)[:200]}"
        except anthropic.APIConnectionError as e:
            if attempts <= 3:
                time.sleep(30 * attempts)
                continue
            out["error"] = f"APIConnectionError: {str(e)[:200]}"
        except Exception as e:  # noqa: BLE001  (anything else: keep what was streamed)
            out["error"] = f"{type(e).__name__}: {str(e)[:300]}"
        if buf:  # a partial text is kept, exported and flagged, never lost
            out["text"] = "".join(buf)
            out["stop_reason"] = f"partial_error: {out['error'][:120]}"
            out["error"] = None
            journal()
        elif tbuf:
            out["thinking"] = "".join(tbuf)
        return out


def run(rundir, workers=4, stagger=5.0, model_default=None, task_budget=None, fallbacks=False):
    have_key = load_secret()
    import anthropic  # noqa: F401  (fail early if the SDK is missing)
    # The key value is never read into a variable this script prints or writes; only the SDK sees it.
    reqs = read_jsonl(os.path.join(rundir, "IN.jsonl"))
    if not reqs:
        raise SystemExit(f"no IN.jsonl in {rundir}; run build first")
    out_path = os.path.join(rundir, "OUT.jsonl")
    done = {d.get("id") for d in read_jsonl(out_path) if d.get("error") is None}
    todo = [r for r in reqs if r.get("id") not in done]
    for r in todo:
        if model_default and not r.get("model"):
            r["model"] = model_default
        r.setdefault("model", model_default or os.environ.get("LANES_MODEL", "claude-opus-5-5"))
    print(f"[lanes] {len(reqs)} requests, {len(done)} already done, {len(todo)} to run"
          + ("" if have_key else " (no ANTHROPIC_API_KEY in env; relying on the SDK's own credential resolution)"),
          flush=True)
    if not todo:
        return 0
    client = anthropic.Anthropic(max_retries=2, timeout=600)
    n_err = 0
    with open(out_path, "a", encoding="utf-8") as f, ThreadPoolExecutor(max_workers=workers) as ex:
        futures = []
        for i, r in enumerate(todo):
            if i:
                time.sleep(stagger)  # each lane reserves its full output budget at start (METHODOLOGY 4.16)
            futures.append(ex.submit(_one_request, client, r, rundir, task_budget, fallbacks))
        for fut in futures:
            o = fut.result()
            n_err += o["error"] is not None
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
            f.flush()
            print(f"[lanes] {o['id']}: stop_reason={o['stop_reason']} "
                  f"out_tokens={(o['usage'] or {}).get('output_tokens')} error={o['error']}", flush=True)
    print(f"[lanes] done; errors: {n_err} (rerun the same command to retry them)", flush=True)
    return 1 if n_err else 0


# ---------------------------------------------------------------- export + census

def _census(outs):
    c = {}
    for o in outs:
        sr = o.get("stop_reason") or ("error" if o.get("error") else "none")
        if isinstance(sr, str) and sr.startswith("partial_"):
            sr = sr.split(":")[0]
        if sr == "max_tokens" and not (o.get("text") or "").strip():
            sr = "max_tokens_VOID"
        c[sr] = c.get(sr, 0) + 1
    return c


def export(rundir):
    spec = {s["id"]: s for s in read_jsonl(os.path.join(rundir, "SPEC.jsonl"))}
    outs = read_jsonl(os.path.join(rundir, "OUT.jsonl"))
    log = os.path.join(rundir, "EXPORTED.txt")
    done = set(open(log).read().split()) if os.path.exists(log) else set()
    n = 0
    for o in outs:
        if o.get("error") or o["id"] in done or o["id"] not in spec:
            continue
        p = spec[o["id"]]["out"]
        text = o.get("text") or ""
        void = (o.get("stop_reason") == "max_tokens" and not text.strip())
        if void:
            base, ext = os.path.splitext(p)
            p = f"{base}_VOID{ext or '.md'}"
            text = ("not a proof, not a verdict: this lane stopped at its output limit with no text. "
                    "Re-cut the target into smaller sub-claims (METHODOLOGY 4.5, 4.6). Thinking summary "
                    "follows for re-cutting only.\n\n" + (o.get("thinking") or ""))
        elif not text.strip():
            continue  # nothing to write (refusal with no text, etc.); the census reports it
        base, ext = os.path.splitext(p)
        k = 1
        while os.path.exists(p):
            k += 1
            p = f"{base}_v{k}{ext}"
        with open_new(p) as f:
            f.write(text)
        with open(log, "a") as f:
            f.write(o["id"] + "\n")
        n += 1
        print(f"{o['id']} -> {p} ({o.get('stop_reason')}, out {(o.get('usage') or {}).get('output_tokens')} tok)")
    print(f"STOP-REASON CENSUS {os.path.basename(rundir)}: {_census(outs)}")
    print(f"exported {n} now; {len(done) + n} of {len(spec)} requested have a file")
    missing = [i for i in spec if i not in {o['id'] for o in outs}]
    if missing:
        print(f"NOT LANDED yet: {missing}")


def census(rundirs):
    for rd in rundirs:
        ins = read_jsonl(os.path.join(rd, "IN.jsonl"))
        outs = read_jsonl(os.path.join(rd, "OUT.jsonl"))
        cuts = sum((r.get("prompt") or "").count(CUT_ATTACH) + (r.get("prompt") or "").count(CUT_PROMPT)
                   + (r.get("prompt") or "").count(MISSING) for r in ins)
        print(f"{os.path.basename(rd)}: requested {len(ins)}, landed {len(outs)}, census {_census(outs)}, "
              f"prompt cut/missing markers {cuts}")


# ---------------------------------------------------------------- layered

def layered(spec_path, prefix, workers=4, attempts=3):
    specs = read_jsonl(spec_path)
    outs = {s["out"]: s["id"] for s in specs}
    strip = lambda f: parse_file_spec(f)[0]  # noqa: E731
    deps = {s["id"]: {outs[strip(f)] for f in s.get("files", []) if strip(f) in outs} for s in specs}
    for s in specs:
        for f in s.get("files", []):
            p = strip(f)
            if p not in outs and not os.path.isfile(p):
                raise SystemExit(f"{s['id']}: input {p} is missing and no lane produces it")
    layers, done = [], set()
    while len(done) < len(specs):
        layer = [s for s in specs if s["id"] not in done and deps[s["id"]] <= done]
        if not layer:
            raise SystemExit("cycle or unresolved dependency among: "
                             + ", ".join(s["id"] for s in specs if s["id"] not in done))
        layers.append(layer)
        done |= {s["id"] for s in layer}
    print(f"{len(layers)} layer(s): {[[s['id'] for s in ly] for ly in layers]}", flush=True)
    me = os.path.abspath(__file__)
    for k, layer in enumerate(layers, 1):
        sp = f"{prefix}_L{k}.spec.jsonl"
        if not os.path.exists(sp):
            with open_new(sp) as f:
                for s in layer:
                    f.write(json.dumps(s, ensure_ascii=False) + "\n")
        rd = f"{prefix}_L{k}"
        if not os.path.exists(os.path.join(rd, "IN.jsonl")):
            r = subprocess.run([sys.executable, "-I", "-B", me, "build", sp, rd], capture_output=True, text=True)
            print(f"layer {k}: {r.stdout.strip()[-300:]} {r.stderr.strip()[-300:]}", flush=True)
            if r.returncode != 0:
                raise SystemExit(f"layer {k}: BUILD FAILED")
        for a in range(1, attempts + 1):
            rc = subprocess.call([sys.executable, "-I", "-B", me, "run", rd, "--workers", str(workers)])
            n = sum(1 for o in read_jsonl(os.path.join(rd, "OUT.jsonl")) if not o.get("error") and o.get("text"))
            print(f"{time.strftime('%H:%M', time.gmtime())} layer {k} attempt {a}: {n}/{len(layer)} (rc {rc})", flush=True)
            if n >= len(layer):
                break
            time.sleep(60)
        subprocess.call([sys.executable, "-I", "-B", me, "export", rd])
    print("layered done", time.strftime("%H:%M", time.gmtime()))


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("spec"); b.add_argument("rundir")
    b.add_argument("--allow-cuts", action="store_true")
    b.add_argument("--forbidden", default=os.environ.get("LANES_FORBIDDEN", ""),
                   help="comma-separated path fragments no lane may read (RESOURCES.md FORBIDDEN_SOURCES)")
    r = sub.add_parser("run"); r.add_argument("rundir")
    r.add_argument("--workers", type=int, default=4)
    r.add_argument("--stagger", type=float, default=5.0, help="seconds between lane starts")
    r.add_argument("--model-default", default=None)
    r.add_argument("--task-budget", type=int, default=None,
                   help="optional visible token budget (beta); minimum 20000; lets the model pace the write-early rule")
    r.add_argument("--fallbacks", action="store_true",
                   help="opt in to server-side refusal fallbacks (beta). Off by default: a lane's model is part of "
                        "its record, and the harness books a refusal as a lost lane rather than a silent model switch")
    e = sub.add_parser("export"); e.add_argument("rundir")
    l = sub.add_parser("layered"); l.add_argument("spec"); l.add_argument("prefix")
    l.add_argument("--workers", type=int, default=4); l.add_argument("--attempts", type=int, default=3)
    c = sub.add_parser("census"); c.add_argument("rundirs", nargs="+")
    a = ap.parse_args()
    if a.cmd == "build":
        forbidden = [x.strip() for x in a.forbidden.split(",") if x.strip()]
        build(a.spec, a.rundir, allow_cuts=a.allow_cuts, forbidden=forbidden)
    elif a.cmd == "run":
        sys.exit(run(a.rundir, a.workers, a.stagger, a.model_default, a.task_budget, a.fallbacks))
    elif a.cmd == "export":
        export(a.rundir)
    elif a.cmd == "layered":
        layered(a.spec, a.prefix, a.workers, a.attempts)
    elif a.cmd == "census":
        census(a.rundirs)


if __name__ == "__main__":
    main()
