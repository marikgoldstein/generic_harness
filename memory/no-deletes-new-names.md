---
name: no-deletes-new-names
description: Nothing of record is deleted or overwritten: no rm, mv over a file, in-place sed, rsync --delete, git reset or clean, force push; write every file under a new name; appends to your own logs are fine (6.3, 10.1)
metadata:
  type: feedback
---

Write new files with new names and leave stale files alone. Superseding files carry new names and the ledger says which governs; outputs that failed a format check are flagged "not of record", never removed. If something really must go, ask the user, naming the exact path.

**Why:** once, in a running project, a sync script with a delete flag, run on another session's behalf, wiped live working files that no commit held; transcripts were the only fallback. Later a checker ran a recursive remove in its own scratch folder under a brief that banned only "deletes of files", and another renamed over an existing file under a brief that banned only rm.

**How to apply:** spell it out in every brief: never rm, rmdir or mv, not even on your own scratch files; no cp over an existing file; no in-place sed, even as a no-op; each file under a new name in a new directory. Log every slip. The one relaxation the user may grant (DELETE_POLICY tmp-allowed): a job's own temporary intermediates removed by the job that made them through a result-gated last step named in its memo, never by a glob over a shared directory. When in doubt whether a file is temporary, it is not. Related: [[no-settings-changes-unasked]], [[volume-safety-no-root-search]].
