# briefs/: how agents are spawned

A BRIEF is the spawn prompt of a subagent. In the single-agent profile (MAX_CONCURRENT_AGENTS = 1) it is the
task you write for yourself before a fresh pass: write it out in full, then execute it. Either way the
brief is a file on disk under `lead/briefs/<ROLE>_<item>_<HHMM>.md`, written from the template here,
never pasted from an older brief (METHODOLOGY 6.11).

## The templates

| file | role |
|---|---|
| `HEADER.md` | the safety and hygiene block pasted at the top of every brief |
| `OWNER_BRIEF.md` | the owner of one item: proves it in full first, splits only under the six criteria |
| `PROVER_BRIEF.md` | a dedicated prover on one open-mathematics input; a one-shot whole-item prover |
| `REVIEW_LENS.md` | the two lens prompts of a review pair (A breaks, B rebuilds) |
| `COORDINATOR_BRIEF.md` | a fresh agent per round: reads the cut of record, writes one packet and one memo |
| `CLOSER_BRIEF.md` | pre-checks an item's files in parallel with its review |
| `EDITOR_BRIEF.md` | writes the public document, outside the proving staff |
| `SUCCESSOR_BRIEF.md` | the short brief for the next seat of a persistent role |

## How a brief is built

1. Start from the template. Substitute every `{{PLACEHOLDER}}` at spawn time: the methodology version
   (its changelog's last entry), the item label, the consumer line quoted verbatim with its location,
   the ID block, the paths, the people. Nothing is left in braces.
2. Measure the required reads in bytes (`wc -c` on the exact files or ranges) and write the budget into
   the brief. A seat that spends its first hour reading was briefed badly (9.6).
3. Test every file name the brief mentions with `[ -e <exact name> ]` before the brief is sent (6.11).
   Patterns with braces or ranges are expanded in full.
4. Name roles, never stood-down agents (6.11). Give agent ids only for seats that are live.
5. Spawn with the strongest model and EFFORT set through the Agent tool's parameter; text in the prompt
   that says "effort max" does nothing (4.9). Run in the background. Record the spawn only after the
   tool's result prints the agent id (6.15).
6. Append the id, the ID block and the time to the lead's agent register (one line per spawn).

## The harness paragraph (in every persistent brief)

- Keep an append-only MEMO with a TO RESUME section at its end; write state and decisions as you go;
  never re-read the memo or large texts whole (9.1).
- Write your successor's ONBOARDING v1 by ONBOARDING_V1_AT of your own count and append one line per
  landing; add a SUCCESSOR STATE paragraph when the lead asks (9.3).
- The lead's count governs. Say HAND-OVER READY at HANDOVER_ASK_AT by the lead's count but KEEP THE
  SEAT; the hand-over is the lead's call (9.4).
- Write no FINAL unless the lead names your successor; the onboarding is the hand-over (9.5).
- A run that stops is resumed by the lead's next message with your context intact; keep working (9.5).
- Your successor's "up" is the last message you act on; after it, forward one line per landing and stop.

## Scaling down to one agent

With MAX_CONCURRENT_AGENTS = 1 the brief is still written, because writing the task fixes the object, the
consumer line and the grade words before the work starts (2.1, 2.2). Then:

- OWNER and PROVER briefs are executed by you, one item at a time, in the order of the ledger.
- REVIEW_LENS A and B are two separate passes in fresh context (a new session or a cleared context),
  B without A's notes; both outputs go to disk under new names before you compare them (5.1).
- COORDINATOR is a pass you run at each status: read the ledger since your last census, write the
  packet, apply it.
- SUCCESSOR is you after a context compaction: read your own onboarding and memo first (9.10).
