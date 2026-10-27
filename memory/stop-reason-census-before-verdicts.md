---
name: stop-reason-census-before-verdicts
description: At every landing, count stop reasons BEFORE reading any verdict; a lane cut at its output limit, refused, or without a numbered finding is NOT LANDED whatever its summary says (4.6)
metadata:
  type: feedback
---

Before reading a single verdict, print the stop-reason counts for the landed lanes and compare the exported count with the requested count. A lane that stopped on its output limit, refused, wrote no numbered finding, or was cut by a transport error is NOT LANDED: its summary claims are not of record; a status line written early is a claim about the end, not a result.

**Why:** once, in a running project, a lane's file began with a verdict line and a summary claiming a lemma proved, and stopped before the proof; the lead reported it as a result and a downstream agent built on it. Twice more, truncated texts were relayed as proved-weaker because their first section carried a status written at the start.

**How to apply:** for an output-limit stop, relay "truncated at section k; proved = sections 1..k only" and re-cut into one sub-claim per lane with the write-early clause, never relaunch as is. A refusal is a lost lane: bisect the content, re-issue under a new ID. Read the file's last section, not only its first. Related: [[api-lanes-write-early-and-split]], [[comms-audit-every-status]].
