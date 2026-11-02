---
name: output-cap-floors-rebuild-not-retry
description: A lane that returns no text with stop reason "output limit" spent its budget on reasoning; rebuild at a higher cap, never retry at the same; edit and repair lanes get a floor well above a prover's typical need (4.20)
metadata:
  type: feedback
---

Edit and repair lanes read a long text and a long list before they write; a cap sized for a prover leaves them nothing to write with.

**Why:** once, in a running project, an edit lane with a 32k output cap returned an empty file with the stop reason "max tokens"; a retry at the same cap did the same. The project set a floor of 48k for edit lanes and 64k to 96k when the text was over 50 KB or the list long, and the empty landings stopped.

**How to apply:** set the floor in the lane builder, not in the brief; at every landing read the stop reason before the text; an empty landing is rebuilt with a larger cap in the same turn, and the retry at the old cap is never launched. Related: [[stop-reason-census-before-verdicts]], [[api-lanes-write-early-and-split]].
