#!/usr/bin/env python3
"""comms_audit.py: one-shot audit of agent-to-API communication over a lanes directory.

    comms_audit.py LANES_DIR [runs_window_min=240] [landed_window_min=40] [mmdd]

Run ONCE per status (METHODOLOGY 6.10), never in a loop. It does one readdir of LANES_DIR and
selects run dirs by their name stamp "<tag>_<mmdd>_<HHMM>" inside the window; everything else is read
by exact name. Pass mmdd explicitly after midnight UTC when the window spans the previous day.

Prompt side (IN.jsonl): cut markers, MISSING attachments, prompts >= 390 KB (the builder cuts from
the END, where the text under review sits).
Output side (OUT.jsonl): stop_reason census; VOID (max_tokens, no text); TRUNCATED (max_tokens with
text); REFUSAL; partial_* (transport error with partial text); API ERROR.
Delivery: lanes launched > 150 min ago with no output (LOST?); finished lanes whose "out" file is
absent once nothing in the run is in flight (NOT EXPORTED).

Writes LANES_DIR/comms_audit/COMMS_AUDIT_<mmdd>_<HHMM>.txt (a new file; never overwrites) and prints
one summary line plus the flags. Every flag goes to the lane's owner the same turn.
"""
import datetime
import json
import os
import re
import sys

CUTS = ["cut at the attachment cap", "excerpts cut at the prompt cap", "cut at 60 KB", "cut at 400 KB"]


def read_jsonl(path):
    out = []
    if not os.path.isfile(path):
        return out
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                out.append({"_unreadable": True})
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    lanes_dir = sys.argv[1]
    runs_win = float(sys.argv[2]) if len(sys.argv) > 2 else 240.0
    land_win = float(sys.argv[3]) if len(sys.argv) > 3 else 40.0
    now = datetime.datetime.now(datetime.timezone.utc)
    mmdd = sys.argv[4] if len(sys.argv) > 4 else now.strftime("%m%d")
    nowts = now.timestamp()
    pat = re.compile(r"_%s_(\d{2})(\d{2})$" % re.escape(mmdd))
    flags = []
    c = dict(runs=0, lanes=0, landed=0, landed_win=0, end_turn=0, void=0, trunc=0, refusal=0, partial=0,
             error=0, inflight=0, lost=0, notexp=0, cuts=0, missing=0, oversize=0)

    def age_min(hh, mm):
        d = now.hour * 60 + now.minute - (hh * 60 + mm)
        return d if d >= 0 else d + 1440

    for name in sorted(os.listdir(lanes_dir)):
        m = pat.search(name)
        if not m:
            continue
        a = age_min(int(m.group(1)), int(m.group(2)))
        if a > runs_win:
            continue
        d = os.path.join(lanes_dir, name)
        if not os.path.isfile(os.path.join(d, "IN.jsonl")):
            continue
        c["runs"] += 1
        spec = {s.get("id"): s.get("out") for s in read_jsonl(os.path.join(d, "SPEC.jsonl")) if not s.get("_unreadable")}
        ins = []
        for r in read_jsonl(os.path.join(d, "IN.jsonl")):
            if r.get("_unreadable"):
                flags.append(f"{name}: unreadable IN line"); continue
            p = r.get("prompt") or ""; i = r.get("id"); ins.append(i); c["lanes"] += 1
            k = sum(p.count(x) for x in CUTS); ms = p.count("MISSING:"); sz = len(p.encode("utf-8"))
            if k: c["cuts"] += k; flags.append(f"{name} {i}: PROMPT CUT x{k}")
            if ms: c["missing"] += ms; flags.append(f"{name} {i}: MISSING attachment x{ms}")
            if sz >= 390000: c["oversize"] += 1; flags.append(f"{name} {i}: prompt {sz // 1000} KB >= 390 KB (end-cut risk)")
        outs = {}
        op = os.path.join(d, "OUT.jsonl")
        recent = os.path.isfile(op) and (nowts - os.path.getmtime(op)) / 60.0 <= land_win
        for r in read_jsonl(op):
            if r.get("_unreadable"):
                flags.append(f"{name}: unreadable OUT line"); continue
            outs[r.get("id")] = r
        if recent:
            c["landed_win"] += len(outs)
        nfl = sum(1 for i in ins if i not in outs)
        for i in ins:
            o = outs.get(i)
            if o is None:
                if a > 150: c["lost"] += 1; flags.append(f"{name} {i}: NO OUTPUT {a} min after launch (lost?)")
                else: c["inflight"] += 1
                continue
            c["landed"] += 1
            sr = o.get("stop_reason") or ""; tl = len(o.get("text") or ""); err = o.get("error")
            if err: c["error"] += 1; flags.append(f"{name} {i}: API ERROR {str(err)[:120]}")
            if sr == "end_turn": c["end_turn"] += 1
            elif sr == "max_tokens":
                if tl == 0: c["void"] += 1; flags.append(f"{name} {i}: VOID (max_tokens, no text): re-cut (METHODOLOGY 4.5)")
                else: c["trunc"] += 1; flags.append(f"{name} {i}: TRUNCATED at max_tokens ({tl} chars): use only what precedes the cut")
            elif sr == "refusal": c["refusal"] += 1; flags.append(f"{name} {i}: REFUSAL ({tl} chars): bisect and re-issue under a new id")
            elif sr.startswith("partial_"): c["partial"] += 1; flags.append(f"{name} {i}: {sr[:80]} ({tl} chars): partial, not a pass")
            elif sr: flags.append(f"{name} {i}: stop_reason={sr} ({tl} chars)")
            out = spec.get(i)
            if sr == "end_turn" and tl > 0 and out and nfl == 0 and not os.path.exists(out):
                c["notexp"] += 1; flags.append(f"{name} {i}: NOT EXPORTED ({os.path.basename(out)})")

    summary = (f"comms ({c['runs']} runs / {c['lanes']} lanes launched in the last {int(runs_win)} min): landed {c['landed']} "
               f"({c['landed_win']} in the last {int(land_win)} min) = end_turn {c['end_turn']} / void {c['void']} / truncated "
               f"{c['trunc']} / refusal {c['refusal']} / partial {c['partial']} / API errors {c['error']}; in flight {c['inflight']}; "
               f"lost? {c['lost']}; not exported {c['notexp']}; prompt side: cuts {c['cuts']} / missing {c['missing']} / "
               f">=390 KB {c['oversize']}")
    rep_dir = os.path.join(lanes_dir, "comms_audit")
    os.makedirs(rep_dir, exist_ok=True)
    outp = os.path.join(rep_dir, f"COMMS_AUDIT_{mmdd}_{now.strftime('%H%M')}.txt")
    k = 1
    while os.path.exists(outp):
        k += 1
        outp = os.path.join(rep_dir, f"COMMS_AUDIT_{mmdd}_{now.strftime('%H%M')}_{k}.txt")
    with open(outp, "x", encoding="utf-8") as fh:
        fh.write(f"{now.strftime('%H:%M:%S')} UTC\n{summary}\n" + "\n".join(flags) + "\n")
    print(summary)
    for f in flags[:40]:
        print(" -", f)
    if len(flags) > 40:
        print(f" ... {len(flags) - 40} more in {outp}")
    print("report:", outp)


if __name__ == "__main__":
    main()
