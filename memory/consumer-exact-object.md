---
name: consumer-exact-object
description: Quote the consumer's exact line verbatim (file:line) before building any proof chain; the target is neither stronger nor weaker than the consumed form (2.2)
metadata:
  type: feedback
---

Every target file starts with the consumer's verbatim line and states "consumed form = ...". Check the target is not stronger than what is consumed (a stronger clause is struck, not proved) and not weaker (a loss, a sub-class, another domain, another shape).

**Why:** once, in a running project, an item grew for a day into many geometric cases while the proof chain used one form of an object; a max-effort re-audit found the consumer used a different form that met none of the cases and needed no case analysis at all. The user's "maybe something is wrong" was the only alarm.

**How to apply:** when a proof keeps splitting into cases, re-read the consumer first. Write the end-to-end skeleton with a case table before staffing pieces. The full pass checks that the closing statement matches the consumer's line. A reduction claim in a text ("reduces to Lemma X") is a citation of the consumer's actual use and is read before Lemma X is attacked. Read the consumed object from the consumer's own operation, never from a dictionary line's description of it. Related: [[targets-state-scale]], [[outside-prompt-orientation]].
