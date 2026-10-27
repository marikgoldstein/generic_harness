---
name: targets-state-scale
description: Every target states the scale and the quantifiers in words ("for every scale in the family, constants independent of the index"); fix the consuming scale before launching (2.8)
metadata:
  type: feedback
---

In every target, write the scale and the uniformity out: "for every scale in the family, with constants independent of the index". If the consuming scale is not yet fixed, settle it (ask the coordinator, or decide and record) before launching.

**Why:** once, in a running project, pool targets said "free of the index" next to a fixed small example. Five independent provers proved the fixed-size statement five ways; the consumer needed the uniform one. The user asked whether a piece of knowledge had been missing. It had: the scale was never stated.

**How to apply:** a letter's index set, domain, sup-versus-inf and rounding direction are part of the target (4.17). When a fixed-scale proof comes back, check at once whether the consumer needs more and send the flag the same turn. Related: [[consumer-exact-object]], [[numbers-first-gate]].
