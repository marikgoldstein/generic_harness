---
name: running-computations-are-attempts
description: A running job is an ATTEMPT until its gate passes: say "an attempt at X is running", name the gate, name the known shortfall modes; never "every remaining computation is running" (7.8)
metadata:
  type: feedback
---

Never write "X runs" or "with your submits every remaining computation is running" as if the submission settled the item. Write "an attempt at X is running", the gate it must pass (a complete manifest, the form check against the consumed line, the certification, the owner's gate word) and the known ways it can fall short (a second cycle, partly certified cells, a tile stop).

**Why:** once, in a running project, a status said every remaining computation was running while one job's pieces were under a form check and another was expected to need a second cycle; the user said "attempt at every remaining computation" was the fact. Separately, a job carried as "running" for hours had completed with exit 0 and no result, because the scheduler lists only live jobs and nobody tested its done file.

**How to apply:** test every "running" job's done file or one scheduler record at every status; a batch's "completed, exit 0" is the batch's word, not the result's; read the output root before the status word moves. A status line about a running computation names its packing (tasks times points, per-task timeout) beside its rate. Related: [[done-needed-now-format]], [[hanging-sweep-every-status]].
