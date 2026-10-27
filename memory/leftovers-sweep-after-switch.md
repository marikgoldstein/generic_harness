---
name: leftovers-sweep-after-switch
description: After any lead switch or restart, sweep for leftovers: orphan loops, open items without a live owner, landed-but-unbooked verdicts, launch logs with cut or missing markers, batch outputs called "partial" without reading their tail (8.11)
metadata:
  type: feedback
---

Every lead switch, model switch or restart is followed by a sweep, repeated cheaply at every status: (1) orphan processes and loops, each with a known owner and purpose, your own stale ones stopped; (2) open items times live owners, an orphan item re-owned the same turn; (3) for every launch older than an hour, the verdict files tested by exact name and any landed-and-unbooked verdict sent to its owner; (4) launch logs with MISSING or CUT markers, judged on the run log, not the dry log; (5) batch outputs without their done line read in their last lines before being called "partial" or "timed out".

**Why:** once, in a running project, a sweep after a lead switch found an eighteen-day watchdog loop over an empty directory on a network file system, an item ownerless for seven hours, a named input at zero effort for forty-five minutes, a false "missing attachment" alarm from a dry log, and a "timeout" that was in fact hundreds of crashed tasks. The user had asked to assume that loops left by the previous lead might have small slips jamming things up.

**How to apply:** two minutes of greps; stop only your own processes (another session's never); re-create crons and backup loops only after checking they are not already running. Related: [[hanging-sweep-every-status]], [[background-shells-outlive-session]], [[no-restart-after-freeze]].
