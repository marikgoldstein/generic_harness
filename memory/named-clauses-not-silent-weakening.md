---
name: named-clauses-not-silent-weakening
description: A fix at statement level is applied as a NAMED CLAUSE ("rel. (H-k)") that the ledger line and the text both carry; a hypothesis-level change costs one more re-read; a wording-only edit lane never gets to decide which it is (5.18, 5.22)
metadata:
  type: feedback
---

When a re-read says the statement needs a condition, the condition gets a name and appears in the theorem, in the ledger line's named inputs and in the "rel." list. Weakening the statement inside a wording pass hides the change from everyone downstream.

**Why:** once, in a running project, an APPROVED_WITH_MINOR closure re-read carried two REQUIRED statement-level items (a convention and a lower bound on a parameter); the wording-only edit lane skipped them, and the next re-read returned a gap. The triage that followed found several hypothesis-level items across other texts that had been treated as wording.

**How to apply:** at closure, read the re-read's REQUIRED list item by item and rule on each statement-level item explicitly; build the edit lane with the ruling and the sources; classify every change as editorial / statement-level / hypothesis-level in the edit list itself; one more re-read for hypothesis-level, none for editorial. Related: [[prescription-is-a-claim]], [[edit-lane-lead-decisions-before-reread]].
