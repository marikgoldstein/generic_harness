---
name: edit-lane-lead-decisions-before-reread
description: Read an edit lane's Lead decisions before launching a re-read; "not applied: source not in the excerpts" is a gap in waiting; after every editorial pass one triage agent classifies every such item REQUIRED / OPTIONAL / DONE (5.22)
metadata:
  type: feedback
---

An edit lane returns `STATUS: EDITS n`, byte-exact Old/New blocks, and a `Lead decisions` section. The lead reads that section first. An unapplied ruled item means the next re-read will find exactly that gap.

**Why:** once, in a running project, an edit lane skipped four of eight ruled edits with "source not in the excerpts"; the re-read launched on that version returned a gap for exactly those four. A later triage over sixteen closed texts found forty-two REQUIRED re-read items that wording-only edit lanes had skipped, several at hypothesis level (a clause missing from a theorem, an input enlarged).

**How to apply:** attach every file a ruling cites when building an edit lane (the ruling's words are not enough to write the New text); rebuild with the source rather than re-read; after each editorial pass, one triage agent classifies every Lead-decisions item against its re-read before any item books at the new version; hypothesis-level items become named clauses and the ledger line is amended in the same step. Related: [[named-clauses-not-silent-weakening]], [[output-cap-floors-rebuild-not-retry]].
