---
name: volume-safety-no-root-search
description: Never find, du, ls -R, grep -r or locate from / or across a shared mount as a whole; search only the project's own paths under a timeout and a depth bound; never name a device file as a command argument (10.4)
metadata:
  type: feedback
---

Every agent prompt carries the safety rule: searches start only from the project's own paths, with a timeout and a depth bound; known locations (a library's package dir, a toolchain) are named in the brief instead of searched for; nothing is removed, moved or linked outside the agent's own folder; device files are never named as file arguments, only as redirect targets.

**Why:** once, in a running project, agents ran unbounded `find /` about ten times in a night on a shared volume holding every session's history, and the whole machine froze repeatedly; a clerk copied a file onto the null device and damaged it; a massless-limit agent later removed the null device while cleaning up. Each incident froze other people's sessions too.

**How to apply:** the brief names the exact paths to use. A concurrent sync of a large tree by several agents at once is the same class of incident: serialise with a lock, skip if the last run is recent, stage on local disk. On an HPC gateway or login node, compile and copy only where the brief says. Related: [[never-glob-poll-big-dirs]], [[no-deletes-new-names]].
