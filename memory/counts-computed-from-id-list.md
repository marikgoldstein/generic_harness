---
name: counts-computed-from-id-list
description: Every count line is computed from the id list in the same step (a one-line script), never typed from the previous count (6.17)
metadata:
  type: feedback
---

A count that is copied forward carries its own error forward. Compute it where it is written: a one-line script over the list, or `wc -l` on the id file, in the same command that writes the line.

**Why:** once, in a running project, a list of record had thirteen ids while every count since an earlier version wrote twelve; the slip survived several versions until an audit recounted, and the campaign total moved from thirty to thirty-one.

**How to apply:** the count line shows its computation; hand-offs and statuses carry the open counts with the ledger path; "0 open" on a build is said as "clean build", never as "finished". Related: [[status-count-first]], [[progress-x-of-y]].
