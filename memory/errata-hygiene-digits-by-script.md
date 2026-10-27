---
name: errata-hygiene-digits-by-script
description: Anchors quoted character-exact, digits by script rounded in the safe direction, citations grep-verified, withdrawals propagated to every occurrence, no sentence beyond the cure (5.12)
metadata:
  type: feedback
---

Every anchor in an erratum is quoted character-exact from the line, never from memory. Every digit comes from a script, rounded in the safe direction (upper bounds up; lower bounds and thresholds down), with the script's output line quoted. Every line citation is grep-verified before the lens. A withdrawal is propagated to every occurrence in the whole text. An erratum adds no sentence beyond the cure and rewrites in full any line whose intermediates it changes.

**Why:** once, in a running project, a text needed four review rounds on one display because retyped digits, a hand-written anchor and a stale appended block each failed a lens in turn; another text's status line was re-worded by hand and failed while the body stood. One un-propagated withdrawal cost a ten-lane round, all NOT.

**How to apply:** build a script that recomputes every displayed number and inequality from its source with the rounding direction, aborts on any mismatch, and prints the table into the text's diff section; no text goes to a second pair without it. Status, grade and scope lines of a text are copied by script from the body's theorem statements. Grep the whole file for every corrected string before submitting. Related: [[clerical-one-not-rule]], [[timestamps-from-clock]].
