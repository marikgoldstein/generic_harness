---
name: background-shells-outlive-session
description: Background shells and loops keep running after the session exits or restarts; list orphans at every restart and stop only your own; crons and subagents may or may not survive, so check before re-creating
metadata:
  type: feedback
---

Processes started in the background keep running after the lead's session ends or is restarted. At every restart, and before exiting, list orphaned processes (`ps -u $USER -o pid,ppid,etime,cmd | awk '$2==1'`), identify your own by their working directory, and stop only those. Never touch another session's processes.

**Why:** once, in a running project, a restart lost every subagent and every workflow of the old session (new session id), while the background runners and a numerics job kept going and finished their rounds; the status cron survived, and the re-created one produced a duplicate status two minutes after the real one. An eighteen-day watchdog loop from a retired session was found still polling an empty directory.

**How to apply:** after a restart: list runners and count outputs per run directory; check the cron list before re-creating any cron; re-create the backup loop only if it is not running; respawn persistent agents fresh from their memos only when they have inputs waiting; log it all. Persistent agents therefore always leave their state on disk. Related: [[leftovers-sweep-after-switch]], [[never-glob-poll-big-dirs]].
