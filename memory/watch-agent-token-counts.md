---
name: watch-agent-token-counts
description: Read the harness's token count for every live subagent at every status sweep; agents misjudge their own context by 0.7x to 3x; ask for the successor onboarding at HANDOVER_ASK_AT and spawn at HANDOVER_SPAWN_AT regardless (9.4)
metadata:
  type: feedback
---

The only reliable context figure for a subagent is the count the harness reports in task notifications (or the last cache-read figure in the agent's output log). Scan it for every live agent at every status sweep. At HANDOVER_ASK_AT send one line: "write your successor's onboarding v1 now and say HAND-OVER READY at about N". At HANDOVER_SPAWN_AT spawn the successor from the onboarding on disk even before the agent says ready.

**Why:** once, in a running project, a prover reached about nine hundred thousand tokens unnoticed because the lead relied on the agents' own "I am at about N" estimates; three other agents were closed by the harness mid-flight, one with a review in flight, each costing a respawn with hundreds of thousands of tokens of reads. The measured ratio of harness count to self-estimate varied from 0.7 to 3.

**How to apply:** put the figure into the lead's status log line and into every hand-over request ("the harness counts you at about N"). Every brief says the lead's count governs. A seat's successor is spawned so that its "up" arrives before the predecessor's context is spent. Related: [[successor-onboarding-early]], [[owner-persistence-digest]].
