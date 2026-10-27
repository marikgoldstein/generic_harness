#!/usr/bin/env python3
"""free_id_blocks.py: print free blocks of lane ids (P0001 ... P9999).

    free_id_blocks.py [--min 30] AGENT_IDS.md [other files ...]

Every lane, file and pair gets a never-reused id (METHODOLOGY 4.11, 6.6). A brief's id block must
come from this script's output, never from a grep for used ids alone: a range assigned in a brief
("ids P9100-P9149") mentions only its endpoints, so a bare grep misses the inside of the range.

Parsing. From EVERY file given: used ids `P####` and ranges `P####-P####` (hyphen or en dash). A range
up to 200 long blocks its whole interior. From the FIRST file (AGENT_IDS.md) also a SEQUENTIAL state
machine, line by line in file order:
  - a line containing the token "RELEASED:" releases every range named AFTER that token on the line;
  - every other line's ranges are ASSIGNED;
  - the last state of an id wins (assigned, released, re-assigned, released again ...).
An id is free iff no file uses it as a lane AND it is either never assigned or last RELEASED.

AGENT_IDS.md line conventions (keep them so the parser stays simple):
  HH:MM:SS <role> SPAWNED ids P1200-P1249 (brief <name>)       assigns the range
  HH:MM:SS <role> ENDED; RELEASED: P1231-P1249                  releases the unspent tail
  - the release token appears ONLY on lines that release and names ONLY the released ranges;
  - every spawn gets its own assignment line the same minute it happens;
  - a successor's block continues after the predecessor's LAST launched id, with a gap if the
    predecessor's chained launches may still spend ids.
Range endpoints named only by assignment or release lines are treated as used (conservative).
"""
import re
import sys

RNG = re.compile(r"P(\d{4})\s*[–\-]\s*P(\d{4})")
ONE = re.compile(r"P(\d{4})(?!\d)")


def main():
    args = sys.argv[1:]
    minlen = 30
    if args and args[0] == "--min":
        minlen = int(args[1]); args = args[2:]
    if not args:
        print(__doc__); sys.exit(1)
    agent_ids = args[0]
    used, ranges = set(), []
    for f in args:
        try:
            t = open(f, encoding="utf-8", errors="ignore").read()
        except OSError as e:
            print("skip", f, e); continue
        if f == agent_ids:
            t_used = "\n".join(l for l in t.splitlines() if "RELEASED:" not in l)
        else:
            t_used = t
        for m in RNG.finditer(t_used):
            a, b = int(m.group(1)), int(m.group(2))
            if 0 < b - a <= 200:
                ranges.append((a, b))
        for m in ONE.finditer(t_used):
            used.add(int(m.group(1)))
    state = {}
    try:
        for line in open(agent_ids, encoding="utf-8", errors="ignore").read().splitlines():
            if "RELEASED:" in line:
                for m in RNG.finditer(line.split("RELEASED:", 1)[1]):
                    a, b = int(m.group(1)), int(m.group(2))
                    if 0 < b - a <= 200:
                        for i in range(a, b + 1): state[i] = "R"
            else:
                for m in RNG.finditer(line):
                    a, b = int(m.group(1)), int(m.group(2))
                    if 0 < b - a <= 200:
                        for i in range(a, b + 1): state[i] = "A"
    except OSError:
        pass
    blocked = set(used)
    for a, b in ranges:
        blocked.update(range(a, b + 1))
    for i, s in state.items():
        if s == "R" and i not in used:
            blocked.discard(i)
    out, start = [], None
    for i in range(1, 10000):
        if i not in blocked:
            if start is None: start = i
        else:
            if start is not None and i - start >= minlen: out.append((start, i - 1))
            start = None
    if start is not None and 10000 - start >= minlen:
        out.append((start, 9999))
    print(f"free blocks (>= {minlen}):", ", ".join(f"P{a:04d}-P{b:04d}" for a, b in out) or "none")
    print("ranges parsed:", len(ranges), "used ids:", len(used),
          "released:", sum(1 for v in state.values() if v == "R"),
          "assigned:", sum(1 for v in state.values() if v == "A"))
    print("cross-check every block against the last lines of", agent_ids, "before handing it out")


if __name__ == "__main__":
    main()
