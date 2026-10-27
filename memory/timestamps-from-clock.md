---
name: timestamps-from-clock
description: Every HH:MM in a post, message, file name or ledger line is copied from a clock call made in a separate, earlier step; never estimated, never rounded forward; a stale stamp is fine, a future one never (6.4)
metadata:
  type: feedback
---

Run the clock (`date -u +%H:%M`, plus the user's zone) as its own step, read the value, and only then compose any text that carries a time. Scripts compute their own stamps at run time. A new file's name enters a message only after the write has printed it.

**Why:** once, in a running project, stamps written "by the clock" ran five to twenty-five minutes ahead of the clock, dozens of times over a week: a guessed next minute, a minute copied from another agent's message, a heredoc stamped in the same shell call as the clock (the text is fixed before the clock runs), several message batches with no clock call between them. Each slip needed an erratum, and three agents copied the wrong times into their own records.

**How to apply:** a shell call that writes a stamp must not itself contain the clock call; copy the previous call's output character for character. Before every batch of messages, one clock call; copy that one minute into every message of the batch even if it looks stale. After a context compaction, re-read this file before the first stamped message. File and checkpoint names carry the date, not only the time (see [[midnight-rollover]]). Related: [[post-length-measured]].
