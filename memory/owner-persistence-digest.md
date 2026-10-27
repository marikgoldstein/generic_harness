---
name: owner-persistence-digest
description: Keep owners as long as quality holds; they read landings through a one-line-per-file digest and open full files only for the lines they cure; the lead's relays are names and verdict words only (9.2)
metadata:
  type: feedback
---

Replacement of an owner is the exception. Owners read landed verdicts and prover files through a digest (one line per file: the verdict word or final status sentence, the most serious issue, the count of required items), open a full file only for the lines they cure, write their state into their memo as they go, and never re-read their memo or large texts whole.

**Why:** once, in a running project, owners were replaced about ten times in a night at a few hundred thousand tokens because the lead handed over proactively before big batches landed; each hand-over cost about ten minutes of reading in and some loss of judgement continuity. The co-author asked to persist owners longer by handling context better, for example through a local digest document.

**How to apply:** the lead's relays to owners carry lane names and verdict words, not verbatim paragraphs; the owner digests the files itself. Hand over at HANDOVER_SPAWN_AT by the harness count or when the owner itself reports degraded output, not merely because a batch is in flight. Related: [[watch-agent-token-counts]], [[successor-onboarding-early]].
