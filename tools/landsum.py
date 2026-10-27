#!/usr/bin/env python3
"""landsum.py: one-line summaries of landed lane files.

    landsum.py FILE [FILE ...]          exact paths (the normal use)
    landsum.py --glob 'DIR/PREFIX_*.md' a glob, ONLY when you pass it explicitly

For each file prints: the VERDICT or FINAL STATUS line, the "Most serious issue" line, the READ line
if any, and the character count. Exact names are the rule: a glob over a directory with thousands
of entries on a network file system holds the directory lock and can stall every session
(METHODOLOGY 8.7, 10.4). Pass --glob only on a small directory you know.
"""
import glob
import os
import re
import sys


def summarize(path):
    if not os.path.isfile(path):
        print(f"== {path}: MISSING")
        return
    with open(path, encoding="utf-8", errors="replace") as fh:
        t = fh.read()
    head = t[:4000]
    verdict = re.findall(r"^\**\s*VERDICT:?\**\s*[A-Z_ ]+", head, flags=re.M)
    final = [l for l in t.splitlines() if "FINAL STATUS" in l]
    read = re.findall(r"^\**\s*READ:\**\s*[A-Z ]+", head, flags=re.M)
    serious = [l for l in t.splitlines() if l.lower().lstrip("*# ").startswith("most serious")]
    print(f"== {os.path.basename(path)} ({len(t)} chars)")
    if verdict:
        print("   ", verdict[0].strip())
    if final:
        print("   ", final[0][:600])
    if read:
        print("   ", read[0].strip())
    if serious:
        print("   ", serious[0][:500])
    if not (verdict or final or read):
        print("    (no VERDICT / FINAL STATUS / READ line in the first 4000 chars: treat as NOT LANDED until read)")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == "--glob":
        files = []
        for pat in args[1:]:
            files.extend(sorted(glob.glob(pat)))
        if not files:
            print("glob matched nothing")
    else:
        files = args
    for f in files:
        summarize(f)


if __name__ == "__main__":
    main()
