---
name: channel-stop-hook-posts-human-turns-only
description: A Stop hook that mirrors the lead's final text to a chat channel fires for turns started by a human or an agent message, not for turns started by a cron or a task notification; answer once, in the right place, never both
metadata:
  type: reference
---

If the channel bridge posts the final text of each turn, the deciding fact is the row that started the turn: a human prompt or an agent message means the final text is posted (so it must be channel-ready: short, plain, times in the user's zones, no internal names); a cron or task-notification start means the final text is terminal-only and anything the user must see goes through the notify command. Mid-turn messages do not change the decision.

**Why:** once, in a running project, the user twice saw no answer to a question asked mid-turn (the turn had started from a notification), and later received two copies of the same answer (the lead posted by hand in a turn that was also mirrored). Internal recaps also went to the channel because those turns had started with an agent message.

**How to apply:** in an agent-started turn the final text is a post; if there is nothing worth posting, make it one short informative line. Status posts and document posts go through the notify command regardless. Posts under the channel's cap, measured by script. `optional/discord_bridge/` has a reference implementation; its hooks are installed only by the user (10.3). Related: [[post-length-measured]], [[no-settings-changes-unasked]].
