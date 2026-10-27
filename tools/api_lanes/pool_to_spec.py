#!/usr/bin/env python3
"""pool_to_spec.py: turn an owner's plain lane lines into a lanes.py spec, with the pre-check.

Owners write lanes as plain text (METHODOLOGY 4.1, 4.11); this script converts a pool source file
into the JSON spec that `lanes.py build` consumes, and refuses to write a spec that would launch a
broken lane (the PRE-CHECK of 4.7 and the briefs).

Pool source format
  Any non-empty lines BEFORE the first lane line are the HEADER: shared definitions and context,
  written once, carried into every lane's task.
  A lane line is ONE line:
     P#### — <statement to prove, exactly as written> — attach <a>; <b>:<lo>-<hi>; <c>
     P#### — review: <the deciding question> — attach <a>; <b>; <TEXT UNDER REVIEW LAST>
     P#### — read: <what to read and quote, from which pages> — attach <a>:<lo>-<hi>
  Exactly one " — attach " per line (the long dash with spaces). "P####" is a placeholder that is
  renumbered from --first-id; a literal id (P0417) is kept as written and checked for uniqueness.
  Attachments are separated by ";". A token is an absolute path, a path relative to --root, or
  ALIAS/rest where ALIAS is given by --alias ALIAS=/abs/dir (repeatable). One range per token.

Pre-check (any ERROR aborts; WARNINGS are printed):
  ERROR   a continuation line (text after a lane line that is not itself a lane line)
  ERROR   zero or two or more " — attach " parts in a lane line
  ERROR   a MISSING attachment; a reversed range; a range beyond the file's content line count
  ERROR   an attachment over --attachment-cap bytes without a line range
  ERROR   a review lane whose last attachment is not a file (the text under review must be last)
  ERROR   a duplicate id
  WARNING two lanes with identical statements (4.2: distinct methods, never duplicate prompts)
  WARNING a statement that does not end with a full stop, or that contains an ASCII bar
Line counts are by content (a last line without a trailing newline counts), never by `wc -l`.

Usage
  python3 -I -B pool_to_spec.py POOL.txt SPEC.jsonl --out-dir /abs/work/item03 --first-id 101
         [--prefix SEEK] [--root $HARNESS_ROOT] [--alias RECORD=/abs/record ...]
         [--effort max] [--max-tokens 64000] [--model ID] [--attachment-cap 55000]
Then: lanes.py build SPEC.jsonl RUNDIR ; lanes.py run RUNDIR ; lanes.py export RUNDIR.
The spec file is opened with "x": never overwritten. Stdlib only.
"""
import argparse
import json
import os
import re
import sys

LANE_RE = re.compile(r"^(P(?:####|\d{3,5}))\s+—\s+(.*)$")
ATTACH_SEP = " — attach "
RANGE_RE = re.compile(r"^(.*?):(\d+)-(\d+)$")

GRADES = {
    "prove": ("Prove the statement EXACTLY as written. End with one line 'FINAL STATUS: PROVED' or "
              "'PROVED-WEAKER: <the exact weaker statement>' or 'REFUTED: <the counterexample>' or "
              "'NOT PROVED: <the failing step>'. A reduction to an unproved named input is NOT a result."),
    "review": ("Review the LAST attachment (the text under review). First line 'VERDICT: APPROVED' or "
               "'VERDICT: APPROVED_WITH_MINOR' or 'VERDICT: NOT APPROVED'; then numbered findings, each "
               "classed CLERICAL or MATHEMATICAL, with file:line; then 'Required for approval:' as a list."),
    "read": ("Quote the requested lines verbatim with page and line, then state in one paragraph what "
             "they do and do not say. Never paraphrase a quotation stronger than its words."),
}


def content_lines(path):
    with open(path, "rb") as f:
        b = f.read()
    if not b:
        return 0
    return b.count(b"\n") + (0 if b.endswith(b"\n") else 1)


def resolve(token, root, aliases):
    token = token.strip()
    m = RANGE_RE.match(token)
    path, rng = (m.group(1), (int(m.group(2)), int(m.group(3)))) if m else (token, None)
    if not os.path.isabs(path):
        head, _, rest = path.partition("/")
        if head in aliases and rest:
            path = os.path.join(aliases[head], rest)
        else:
            path = os.path.join(root, path)
    return path, rng


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pool")
    ap.add_argument("spec")
    ap.add_argument("--out-dir", required=True, help="where export writes the landings (absolute)")
    ap.add_argument("--first-id", type=int, default=None, help="renumber P#### placeholders from here")
    ap.add_argument("--prefix", default="SEEK", help="landing file prefix: <prefix>_<id>.md")
    ap.add_argument("--root", default=os.environ.get("HARNESS_ROOT", os.getcwd()))
    ap.add_argument("--alias", action="append", default=[], help="ALIAS=/abs/dir (repeatable)")
    ap.add_argument("--effort", default=os.environ.get("LANES_EFFORT", "max"))
    ap.add_argument("--max-tokens", type=int, default=int(os.environ.get("LANES_MAX_TOKENS", "64000")))
    ap.add_argument("--model", default=None)
    ap.add_argument("--attachment-cap", type=int, default=int(os.environ.get("LANES_ATTACHMENT_CAP", "55000")))
    a = ap.parse_args()

    if os.path.exists(a.spec):
        sys.exit(f"ERROR: spec exists, new names only: {a.spec}")
    if not os.path.isabs(a.out_dir):
        sys.exit("ERROR: --out-dir must be absolute")
    aliases = {}
    for s in a.alias:
        k, _, v = s.partition("=")
        if not k or not v:
            sys.exit(f"ERROR: bad --alias {s!r}; use ALIAS=/abs/dir")
        aliases[k] = v

    raw = open(a.pool, encoding="utf-8").read().splitlines()
    header, lanes, errors, warnings = [], [], [], []
    seen_lane = False
    for n, line in enumerate(raw, 1):
        if not line.strip():
            continue
        m = LANE_RE.match(line)
        if m:
            seen_lane = True
            lanes.append((n, m.group(1), m.group(2)))
        elif seen_lane:
            errors.append(f"line {n}: continuation text after a lane line (one statement per line): {line[:80]!r}")
        else:
            header.append(line)
    if not lanes:
        sys.exit("ERROR: no lane lines (expected 'P#### — <statement> — attach ...')")

    next_id = a.first_id
    ids, statements, out = set(), {}, []
    for n, pid, rest in lanes:
        parts = rest.split(ATTACH_SEP)
        if len(parts) != 2:
            errors.append(f"line {n}: expected exactly one '{ATTACH_SEP.strip()}' part, found {len(parts) - 1}")
            continue
        statement, attach = parts[0].strip(), parts[1].strip()
        role = "prove"
        for key in ("review", "read"):
            if statement.lower().startswith(key + ":"):
                role, statement = key, statement[len(key) + 1:].strip()
        if pid == "P####":
            if next_id is None:
                errors.append(f"line {n}: placeholder P#### but no --first-id given")
                continue
            pid, next_id = f"P{next_id:04d}", next_id + 1
        if pid in ids:
            errors.append(f"line {n}: duplicate id {pid}")
            continue
        ids.add(pid)
        if statement in statements:
            warnings.append(f"line {n}: statement identical to {statements[statement]} (4.2: distinct methods)")
        statements.setdefault(statement, pid)
        if not statement.endswith((".", "?", ")")):
            warnings.append(f"line {n} {pid}: statement does not end with a full stop (wrapped line?)")
        if "|" in statement:
            warnings.append(f"line {n} {pid}: ASCII bar inside the statement (write absolute values as ∣x∣)")
        files, attached, missing = [], 0, 0
        for tok in [t for t in attach.split(";") if t.strip()]:
            path, rng = resolve(tok, a.root, aliases)
            if not os.path.isfile(path):
                missing += 1
                errors.append(f"line {n} {pid}: MISSING attachment {path}")
                continue
            nlines = content_lines(path)
            if rng:
                lo, hi = rng
                if lo < 1 or hi < lo:
                    errors.append(f"line {n} {pid}: reversed or empty range {lo}-{hi} on {path}")
                if hi > nlines:
                    errors.append(f"line {n} {pid}: range {lo}-{hi} beyond the file's {nlines} content lines: {path}")
                files.append(f"{path}:{lo}-{hi}")
            else:
                if os.path.getsize(path) > a.attachment_cap:
                    errors.append(f"line {n} {pid}: {path} is {os.path.getsize(path)} bytes > cap "
                                  f"{a.attachment_cap} without a line range (attach by ranges)")
                files.append(path)
            attached += 1
        if role == "review" and not files:
            errors.append(f"line {n} {pid}: a review lane needs the text under review as its LAST attachment")
        task = "\n".join(header + ["", f"TASK: {statement}", "", GRADES[role]]) if header else \
            f"TASK: {statement}\n\n{GRADES[role]}"
        rec = {"id": pid, "role": role, "out": os.path.join(a.out_dir, f"{a.prefix}_{pid}.md"),
               "task": task, "files": files, "effort": a.effort, "max_tokens": a.max_tokens}
        if a.model:
            rec["model"] = a.model
        out.append(rec)
        print(f"  {pid}: role={role} attached={attached} missing={missing}")

    for w in warnings:
        print("WARNING", w)
    if errors:
        for e in errors:
            print("ERROR", e)
        sys.exit(f"pre-check FAILED: {len(errors)} error(s); nothing written")
    with open(a.spec, "x", encoding="utf-8") as f:
        for rec in out:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {a.spec}: {len(out)} lanes; header lines {len(header)}; next free id "
          f"{'P%04d' % next_id if next_id is not None else 'n/a'}")


if __name__ == "__main__":
    main()
