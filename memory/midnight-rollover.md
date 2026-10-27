---
name: midnight-rollover
description: Time-only names and comparisons break at the UTC date boundary: waiters hang on a "future" last launch, resume scripts pick yesterday's checkpoint by name order, time-windowed tools select nothing; put the date in names and scope comparisons to today
metadata:
  type: feedback
---

A logged time later than "now" is yesterday; a waiter that computes its own stagger floor from the last logged launch treats a time more than a minute ahead of the clock as the previous day. Checkpoint and log names carry the date, never HHMMSS alone. Any "latest file" logic picks by content or modification time, never by name order. Every time-windowed tool takes an explicit date argument.

**Why:** once, in a running project, three failures came within an hour of the date boundary: every launch waiter derived from one template hung silently to its maximum wait because the last launch "lay in the future"; a resume script re-did half an hour of work from the previous evening's checkpoint because it sorted names; the communication audit selected zero runs for the pre-midnight window. Days later a shared chronological registry without dates matched yesterday's entries at the same minute and blocked a waiter for six minutes.

**How to apply:** before the first launch after the boundary, tell every launching role; check "latest file" logic in resume and merge scripts; scope any minute comparison in a shared chronological file to today's entries (after the last backward time jump). Related: [[timestamps-from-clock]], [[launch-registry-pattern]].
