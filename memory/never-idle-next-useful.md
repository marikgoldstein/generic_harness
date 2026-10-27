---
name: never-idle-next-useful
description: Never idle waiting for a user decision; pick the most useful feasible default, start it, tell the user they can redirect (METHODOLOGY 7.1, 7.2)
metadata:
  type: feedback
---

When a resource is free and a choice is pending with the user, choose the most useful feasible option yourself, start it, and report which option you chose and that they can redirect.

**Why:** once, in a running project, an independent prover sat idle for four hours because every status listed its next item as "a decision for the co-author". The user saw waiting on a decision as wasted capacity whenever a sensible default existed, and said so: no reason to idle, go for the next feasible useful thing.

**How to apply:** hold only for the items in HELD_DECISIONS (money or keys; batch submission when the user has reserved it; settings or hook changes; a final theorem's statement or hypotheses). Everything else: decide, start, tell. A status "decisions needed" line lists only genuine held items, never choices you can make. While a decision is pending, draft the recommended route's pieces as drafts (they become of record only after the go). Related: [[question-filter-goal-then-method]], [[decision-posts-three-lines]], [[hanging-sweep-every-status]].
