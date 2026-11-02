---
name: never-edit-running-script
description: Never edit a shell script while an instance of it is running; the shell reads the file lazily and the running instance misparses its tail; patch a copy under a new name or wait (10.13)
metadata:
  type: feedback
---

A shell reads a script as it executes it. Changing the file under a running instance changes what that instance reads next.

**Why:** once, in a running project, a retry sweep was patched in place while it ran; the running sweep read the patched bytes at the wrong offset and failed with "command not found" and "syntax error near done", and the lanes it should have relaunched sat idle until the next check.

**How to apply:** write the fix as a new file under a new name and start it when the old instance has finished; if the old instance must keep running, leave its file untouched. The no-overwrite rule (6.3) already forbids the edit; this is the second reason. Related: [[no-deletes-new-names]], [[background-shells-outlive-session]].
