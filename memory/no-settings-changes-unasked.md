---
name: no-settings-changes-unasked
description: No changes to settings, hooks, permissions or configuration unless the user asks; keep rules prompt-level; propose a guard in one line and wait (10.3)
metadata:
  type: feedback
---

Do not change the harness's settings, hooks, permissions or configuration in the project unless the user asks for it. If a guard seems needed, propose it in one line and wait.

**Why:** once, in a running project, after seven file-rule slips the lead proposed a pre-tool hook to block deletes and in-place edits. The user declined: do not do the hook for now, do not mess with anything, but please back up. Another time the lead applied a session-wide output-cap setting immediately on hearing "next time you spawn"; the user asked for it to be reverted until the next spawn, and the revert itself needed care (removing a line did not unset the live value).

**How to apply:** keep the no-deletes rule at the prompt level in every brief; log every slip; when the user says "backup", run the versioned backup once by hand. Changes to hooks that mirror a chat channel are the same class: stage a fix and let the user install it. Related: [[no-deletes-new-names]], [[channel-stop-hook-posts-human-turns-only]].
