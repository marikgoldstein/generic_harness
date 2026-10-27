---
name: launch-registry-pattern
description: With several agents launching API lanes, a shared append-only launch registry prevents same-minute bursts; reserve a minute, launch, record at the launcher's print; keep reservations short and scope to today's entries
metadata:
  type: reference
---

When more than one agent launches lanes, each launcher reads a shared append-only registry immediately before a launch (any launched or planned entry in the current minute means wait into a free minute), appends a "launched" line at the moment the launcher prints its start time, and may reserve a minute ahead with a "planned" line that it later confirms or cancels. Each launcher also waits a few minutes after its own previous launch.

**Why:** once, in a running project, a stagger rule based on "launches visible in one folder" went blind as soon as owners logged their launches elsewhere, and same-minute collisions returned with rising refusals. The registry caught its first collision within twenty minutes. It then needed amendments: read the whole file (planned lines scroll out of a tail), write the launched line at the print (late appends collided), release follow-on reservations at the print (the registry saturated with a dozen launchers holding pairs of minutes), treat stale planned lines as free, and scope the minute comparison to today's lines after the date boundary.

**How to apply:** `optional/launch_registry/` has the rule and a reference waiter. With one launching agent, the rule reduces to "stagger starts by a minute or two and retry failures" (4.16). Related: [[api-lanes-write-early-and-split]], [[midnight-rollover]].
