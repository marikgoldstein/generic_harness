---
name: comms-audit-every-status
description: Every status runs a one-shot communication audit: void or truncated lanes, refusals, API errors, lost lanes, unexported outputs, prompt cuts, missing attachments, brief pointers past a file's end; every flag to its owner the same turn (6.10)
metadata:
  type: feedback
---

Run the audit once per status (never in a loop; select runs by name from one directory read). Agent to API: prompt cuts, missing attachments, prompts near the size cap, lanes that wrote no text, lanes cut with text, refusals, API errors, lanes with no output long after launch, outputs never exported. Agent to agent: brief pointers past a file's line count; relays that dropped required items; line ranges in hand-overs checked before sending.

**Why:** once, in a running project, launchers silently cut attachments and the builder cut over-size prompts from the end, which is where the text under review sat; lenses answered "not in the excerpts" and returned NOT. The first audit over four hours and several hundred lanes found eleven lanes with no text and nine cut with text, one of which had fed a verdict. The user said the communication was too important and expensive to lose chunks of context in unexpected ways.

**How to apply:** a void lane is re-cut; a truncated lane is used only for what precedes the cut, with the missing tail named and the owner confirming; a lane missing by exact name while the run log says "no errors" is a lost export. Put the one-line audit result in every status. Related: [[stop-reason-census-before-verdicts]], [[launch-hygiene]].
