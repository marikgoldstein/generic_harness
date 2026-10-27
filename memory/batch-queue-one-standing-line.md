---
name: batch-queue-one-standing-line
description: When the user submits compute, the agent prepares ONE package and ONE queue line, posts "new in queue", and the user runs the same standing submit line every time; job ids come back through files, never by polling the scheduler
metadata:
  type: reference
---

The agent never hands the user a second script name. It appends one line (tag, folder, batch script, note) to a queue file, posts what the job is for in plain words, and the user runs one unchanging submit line that submits every unmarked queue line and writes the job ids to a submitted folder. The agent reads the ids from that folder.

**Why:** once, in a running project, the user asked for all commands in one script and one line to run, and after two different lines asked "should I run that line again?". One standing line settled it. Later lessons: a reused tag was silently skipped by the done flags, so tags carry a date suffix; a heterogeneous partition killed a job whose per-task thread count exceeded the smallest node; a job that wrote hundreds of thousands of files into one directory was re-cut; a superseding line was submitted alongside the line it superseded and the two collided on shared outputs, so a superseding line is appended together with a cancel line for the old job.

**How to apply:** the package carries the consumed form first, a measured heaviest task, the cost estimate, a resumable task file with a result guard per task, outputs under the scratch tree, and a removal-word check. Read-only scheduler queries are one-shot, never polled; watch outputs by exact file name. `optional/batch_queue/` has the pattern. Related: [[running-computations-are-attempts]], [[python-caps-enforced]].
