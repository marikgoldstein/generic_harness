---
name: wish-list-keep-asking
description: Keep a short wish list of resources that would help (agents, API key, cores/GPU, scheduler, channel); ask one per status with its default until the user says yes, no, later or stop; never block on it (METHODOLOGY 7.23)
metadata:
  type: feedback
---

Keep "Open requests" in RESOURCES.md current: more concurrent agents, an API key for lanes, local cores or a GPU, scheduler use, a chat channel, permission to remove temporaries, more spend. Ask for one item per status, saying what it would change and the default you run under meanwhile. Keep asking at that cadence until the user answers yes, no, "later" (with a time or event, then re-ask then) or "stop asking" (never again unless they raise it). Write every answer into RESOURCES.md with its time.

**Why:** conservative defaults make the harness safe on any machine, but a lead that silently runs at one agent on a workstation with idle cores, or never mentions that an API key would double its review capacity, is leaving help on the table. The user asked for a lead that persistently and politely asks for helpful things and whether they are okay, until told one way or the other.

**How to apply:** the question filter (7.3) still applies to research questions; the wish list is about resources only. One request per status, never a list; the default applies until the answer; a "no" is final; a "later" has a time. When a request is granted, record it, use it the same turn, and say so in the next status. Related: [[first-run-one-question-then-defaults]], [[compute-not-assumed]], [[never-idle-next-useful]].
