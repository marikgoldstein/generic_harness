---
name: never-glob-poll-big-dirs
description: On a network or shared file system, never poll a large directory with wildcards; test exact names; poll at most every five minutes; bound watchers by wall clock, two at once at most; start new batches in fresh small subdirectories (8.7)
metadata:
  type: feedback
---

To wait for an output, test its exact name (`[ -e "$DIR/NAME" ]`). Never `ls DIR/PREFIX_*` or `for f in DIR/PREFIX_*` in a directory with thousands of entries. Poll at most every five minutes; bound each watcher by wall clock (`timeout 3600 bash -c ...`), not by a loop count; run at most two watchers at once.

**Why:** once, in a running project, six background loops kept re-listing two directories of ten to twenty thousand files with globs. On a network file system every glob read the whole directory and held its lock; every listing took about ten seconds and the lead's main thread blocked on that lock. The session froze twice in a day. A "sixty times sleep sixty" loop ran nine hours because each glob took eight minutes. Killing the loops brought listings back to instant.

**How to apply:** start new batches in fresh subdirectories so no directory grows past a few hundred entries. Never list the lane-output directory or the tools directory unfiltered (one unfiltered listing cost twenty kilobytes of context). If the file system feels slow, look for your own processes in uninterruptible sleep. Related: [[volume-safety-no-root-search]], [[background-shells-outlive-session]].
