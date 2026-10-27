---
name: numbers-first-gate
description: No proof round without numerical evidence that the target holds (a model that keeps the structure and could fail); covers load-bearing intermediate steps and route decisions (2.4, 2.4a, 2.4c)
metadata:
  type: feedback
---

Before staffing any prover on an input, compute it in a model that keeps the inequality's structure, at several sizes and worst-case geometries, with uncertainty, able to fail. Say which numbers are measured, bounded or extrapolated. If the numerics come back against or inconclusive, stop new proof rounds on that input and say so.

**Why:** once, in a running project, an item resisted for two days on inputs a printed source had deferred; the only "evidence" was the source's own "we expect". One estimate turned out false as written and two mechanisms failed on explicit configurations. The co-author asked why strong evidence had not been gathered before spending the effort.

**How to apply:** a printed "we expect" or a deferred proof is not evidence. If no numerics exist, design the cheapest run (CPU first) in the same message. Test load-bearing intermediate steps the same way. Before a certified computation, quote the consumer's threshold with direction and unit (2.4b). A route withdrawal or adoption is tested by a short probe first: a two-minute probe once reversed a "no cure" assessment. Keep per item the list "numbers in hand, proof not yet posed" and its converse "proof posed on proxy numbers" as a deviation to own. Related: [[expect-truth-first]], [[targets-state-scale]].
