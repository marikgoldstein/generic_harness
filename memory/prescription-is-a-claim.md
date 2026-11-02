---
name: prescription-is-a-claim
description: A refuter's prescribed replacement statement is applied verbatim but stays PROVED-SINGLE until the next re-read checks it; after two failed repair passes, a fresh prover plus two refuters, not a third patch (5.21)
metadata:
  type: feedback
---

A lens that says "replace the statement by X" has proved nothing about X. Apply X as prescribed, mark it as a single-lane claim, and let the next re-read check it. When repairs chain, stop.

**Why:** once, in a running project, a refuter prescribed a replacement hypothesis that was false for one class of objects; a third lane caught it. On the same text a second prescription was inexact, and a fourth lane found an unproved step. Each prescribing lane's text had been treated as settled, and the defects accumulated through three repair passes.

**How to apply:** never promote a prescription on the strength of the prescribing lane; after two failed repair passes on one text, launch a fresh prover from the corrected hypotheses and two refuters on its output; record the chain of prescriptions as claims in the ledger line. Related: [[closure-two-refuters-writer-reread]], [[named-clauses-not-silent-weakening]].
