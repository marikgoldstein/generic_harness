#!/usr/bin/env python3
"""status_post.py: build a status post, enforce the channel's length cap, split at section boundaries.

    status_post.py [--cap N] [--out DIR] [--prefix STATUS] [SOURCE.md]      (SOURCE omitted = stdin)

The source is plain Markdown-ish text. Sections start with lines beginning "## ". The script:
  1. stamps the header line with the clock read AT RUN TIME ("HH:MM UTC" plus the zones in the
     TIMEZONES env, e.g. TIMEZONES="UTC America/New_York"), never from an argument (METHODOLOGY 6.4);
  2. asserts the whole post fits --cap (default: no cap; Discord = 1800) measured in CHARACTERS;
  3. if it does not fit, splits at "## " boundaries into parts each <= cap, numbered "(part i of n)";
     a single section longer than the cap is an error: shorten it (one line per open item, METHODOLOGY 7.12);
  4. writes each part as a NEW file DIR/<PREFIX>_<HHMM>_p<i>.md (never overwrites) and prints the paths.
Pipe each part into your channel's notifier (optional/discord_bridge/discord-notify or your own).
A post file is never edited in place: a new draft is a new file.
"""
import argparse
import datetime
import os
import sys
import zoneinfo


def stamp_line():
    now = datetime.datetime.now(datetime.timezone.utc)
    zones = (os.environ.get("TIMEZONES") or "UTC").replace("/", "/").split()
    parts = []
    for z in zones:
        if z.upper() == "UTC":
            parts.append(now.strftime("%H:%M UTC"))
        else:
            try:
                parts.append(now.astimezone(zoneinfo.ZoneInfo(z)).strftime("%H:%M ") + z.split("/")[-1].replace("_", " "))
            except Exception:  # noqa: BLE001
                parts.append(f"(unknown zone {z})")
    return " / ".join(parts), now


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?")
    ap.add_argument("--cap", type=int, default=int(os.environ.get("POST_CAP_CHARS", "0") or 0))
    ap.add_argument("--out", default=os.environ.get("POSTS_DIR", "posts"))
    ap.add_argument("--prefix", default="STATUS")
    a = ap.parse_args()
    text = open(a.source, encoding="utf-8").read() if a.source else sys.stdin.read()
    when, now = stamp_line()
    lines = text.rstrip("\n").split("\n")
    header = lines[0] if lines else ""
    body = lines[1:] if lines else []
    header = header.replace("{TIME}", when) if "{TIME}" in header else f"{header} ({when})"
    sections, cur = [], []
    for l in body:
        if l.startswith("## ") and cur:
            sections.append("\n".join(cur)); cur = [l]
        else:
            cur.append(l)
    if cur:
        sections.append("\n".join(cur))
    cap = a.cap or 0
    whole = header + "\n" + "\n".join(sections)
    if not cap or len(whole) <= cap:
        parts = [whole]
    else:
        parts, acc = [], ""
        for s in sections:
            if len(s) + len(header) + 24 > cap:
                raise SystemExit(f"a single section is {len(s)} chars; the cap is {cap}. Shorten it (one line per item).")
            cand = (acc + "\n" + s) if acc else s
            if len(header) + 24 + len(cand) > cap:
                parts.append(acc); acc = s
            else:
                acc = cand
        if acc:
            parts.append(acc)
        n = len(parts)
        parts = [f"{header} (part {i} of {n})\n{p}" for i, p in enumerate(parts, 1)]
    os.makedirs(a.out, exist_ok=True)
    hhmm = now.strftime("%H%M")
    for i, p in enumerate(parts, 1):
        if cap:
            assert len(p) <= cap, f"part {i} is {len(p)} > {cap}"
        path = os.path.join(a.out, f"{a.prefix}_{hhmm}_p{i}.md")
        k = 1
        while os.path.exists(path):
            k += 1
            path = os.path.join(a.out, f"{a.prefix}_{hhmm}_p{i}_{k}.md")
        with open(path, "x", encoding="utf-8") as fh:
            fh.write(p + "\n")
        print(f"{path} ({len(p)} chars)")


if __name__ == "__main__":
    main()
