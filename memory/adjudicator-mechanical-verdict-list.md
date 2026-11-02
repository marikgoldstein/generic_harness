---
name: adjudicator-mechanical-verdict-list
description: Disagreement between lanes is adjudicated, not re-run; the adjudicator writes the verbatim first-line verdict list before any interpretation, and no count is carried without it (5.19)
metadata:
  type: feedback
---

One adjudicator reads every output of a wave. Its file starts with the mechanical list: lane id, stop reason, the first line of the output verbatim. Only then the interpretation, the proposed rulings, the ledger deltas and the next lane list. The lead rules; grade words are never arguments.

**Why:** once, in a running project, an adjudication recorded a line as "PROVED x4" when the four lanes had written REFUTED and PARTIAL on their first lines; the summary had been written from memory of the outputs. Re-running the lanes for every disagreement would have cost twenty to sixty minutes each; the list made the misreading visible in seconds.

**How to apply:** attach the mechanical list to every adjudication block; a lane cut at its cap, refused or without a numbered finding appears in the list as NOT LANDED and gets no verdict; one OK plus one OK-with-clerical-fixes is a confirmation when neither names a false displayed sentence, and the clerical items go to an edit lane. Related: [[stop-reason-census-before-verdicts]], [[clerical-one-not-rule]], [[closure-two-refuters-writer-reread]].
