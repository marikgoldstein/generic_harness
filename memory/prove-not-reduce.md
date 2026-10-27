---
name: prove-not-reduce
description: Provers prove the target exactly as written; a reduction to a new named input is not a result; grades PROVED / PROVED-WEAKER / REFUTED / NOT PROVED (3.3, 1.7)
metadata:
  type: feedback
---

Every prover brief and pool template says: prove the target exactly as written. Grades are PROVED, PROVED-WEAKER (the exact weaker statement), REFUTED (the counterexample), NOT PROVED (the failing step). "Derived given X" is allowed only when X is already of record.

**Why:** once, in a running project, about half of a pool came back "derived given a new named input", the open inputs multiplied instead of closing, and the co-author said the provers were reducing, not proving, which was not the task. At that depth new reductions are rarely acceptable unless they land on statements already proved.

**How to apply:** when a review grades a result "derived given H1..Hn", the next step is to prove each Hi or cite it, numbers first; a new named input is filed only after the proof routes have been tried and each failure stated. Status posts count outright closures separately from reductions. Never present "carry X as a named input" as the default next step. Related: [[closed-means-criteria-hold]], [[frozen-open-ledger]].
