---
name: no-restart-after-freeze
description: After a freeze from memory pressure, resume no subagents without the user's word; spawn fresh from memos rather than resuming huge transcripts; keep tool outputs small (8.5)
metadata:
  type: feedback
---

Many local agents share the lead's process. After a freeze, do not resume or respawn subagents until the user says so; leave the state on disk (which agents were lost and what relays they are owed); when agents are allowed again, spawn fresh from on-disk memos with short briefs and keep far fewer live than before.

**Why:** once, in a running project, the lead froze twice in one evening with a dozen local agents live in one process; the second freeze came two minutes after resuming ten of them, when the process's memory nearly doubled. The user said the context had got too big and not to restart the subagents.

**How to apply:** keep your own tool outputs small (head and cut; never cat large files); list orphan processes before anything else after a restart; grow parallel breadth on the API side where it exists, which costs the lead little memory. Fresh agents' transcripts are small, so resuming those is fine; the caution is about huge transcripts. Related: [[leftovers-sweep-after-switch]], [[background-shells-outlive-session]].
