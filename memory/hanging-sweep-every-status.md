---
name: hanging-sweep-every-status
description: At every status, one printed line: lanes out more than 30 minutes without a landing; questions unanswered more than 30 minutes; items silent more than 60 minutes; decisions pending and since when; act on each the same turn (7.16)
metadata:
  type: feedback
---

Print the hanging sweep as its own status line and act on every entry the same turn: a nudge, a re-launch, a re-ask, a default taken.

**Why:** once, in a running project, questions posted to a shared register sat forty-five minutes unanswered because the agent that owned them was idle and nobody resumed it; a named input sat at zero effort for forty-five minutes after its pool landed because the owner missed the landing; an item sat seven hours without an owner with five verdicts unclassified. Idle subagents watch nothing; a posted question moves only when someone resumes its owner.

**How to apply:** in the same turn that any question for an agent is posted, message that agent with the question and its priority. Check that every open question has an owner that is running or was resumed. The user's instruction behind this: revisit anything hanging for a while, and relay a method from one line to the others when it informs them (7.15). Related: [[leftovers-sweep-after-switch]], [[dedicated-prover-per-open-input]].
