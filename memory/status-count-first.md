---
name: status-count-first
description: Every status and reply opens with the count ("open N of M, now: item (state)"), then one or two plain lines per open item with its resource counts; details only when asked (1.8, 7.12)
metadata:
  type: feedback
---

The first line of every status, and of every reply about progress, is the count and the current focus: "open N of M, dependent D, closed C; algorithmic a / mathematics m; now: <item> (<one-line state>)". Then one or two plain lines per open item with "(local n / lanes m)". Then one line for the public document, one for resources, one for decisions needed (or "none now").

**Why:** once, in a running project, the co-authors followed the work from their phones; a detailed status read as noise, and a flat list of sub-inputs read as scope growth ("have you opened more items?"). They asked for the count and the orientation first, then the high level, with the resources on each item so that an unstaffed item showed at a glance.

**How to apply:** post every STATUS_INTERVAL_MIN minutes while anything is live and at every closure; flag any item at zero effort and fix it the same turn. Public labels only; agents by role, never a bare letter (a one-letter agent name once read as a pronoun). Run SELF_CHECK.md before posting. Related: [[frozen-open-ledger]], [[progress-x-of-y]], [[done-needed-now-format]].
