---
name: outside-answers-claims-until-two-readers
description: An answer from a model outside the lane system is a claim until two readers confirm it from the record text, not from the answer; it is a third voice beside a refuter pair, never a substitute (4.22)
metadata:
  type: feedback
---

Outside models run in parallel with the lanes on the same packets, as provers and tie-breakers. Their output enters the ledger only through two readers who check it against the record.

**Why:** once, in a running project, outside answers included proofs that failed every reader, an objection the same model retracted a few lines later, and refutations of statements the lead had paraphrased wrongly. Logging each as a claim and confirming through readers was cheap and removed every false lead within a round.

**How to apply:** before reading an outside answer, check its run flag (zero output; partial with reasoning at the cap) and rerun with a larger cap if it is set; never count its agreement as one of the two refuters; carry it to the ledger as "claim (outside), readers pending" until confirmed. Related: [[packets-verbatim-definitions]], [[outside-prompt-orientation]], [[two-blind-image-readers]].
