# Memory index (seed set; see README.md)

## Autonomy and decisions
- [First run: one question, then defaults](first-run-one-question-then-defaults.md) — ask max concurrent agents (default 1), detect the rest, start (7.21, 7.22)
- [Effort through the parameter](effort-through-the-parameter.md) — subagent model/effort via the Agent tool parameters; prompt text does nothing (4.9)
- [Wish list: keep asking](wish-list-keep-asking.md) — one resource request per status with its default until yes / no / later / stop (7.23)
- [Never idle](never-idle-next-useful.md) — a free resource plus a pending decision = pick the default, start, tell (7.1)
- [Question filter](question-filter-goal-then-method.md) — goal first, then the methodology; ask only if a final statement changes (7.3)
- [Questions in plain form](questions-plain-format.md) — plan said / found / unknown / options / recommended / default (7.4)
- [Decision posts: three lines](decision-posts-three-lines.md) — fact, my call and default, the one thing needed; act first (7.5)
- [Methodology auto-add](methodology-auto-add.md) — every method instruction becomes a numbered rule the same turn (0.1)
- [Lead orchestrates, owners decide](lead-orchestrator-not-strategist.md) — logistics, direction, information; never routes (3.13)

## Proving
- [Expect the truth first](expect-truth-first.md) — belief, evidence, sharp form; weakest sufficient statement (2.3)
- [Numbers first](numbers-first-gate.md) — no proof round without numerical evidence that could fail; probes decide routes (2.4)
- [Consumer-exact object](consumer-exact-object.md) — quote the consumer line verbatim; neither stronger nor weaker (2.2)
- [Targets state the scale](targets-state-scale.md) — uniformity and quantifiers in words; fix the scale before launch (2.8)
- [Prove, never reduce](prove-not-reduce.md) — "derived given X" closes nothing unless X is of record (3.3)
- [Split rule](split-rule-six-criteria.md) — one owner proves in full first; split only under six criteria (3.2)
- [Dedicated prover per open input](dedicated-prover-per-open-input.md) — never "no date"; route line within the first hour (3.12)
- [Outside-prompt orientation](outside-prompt-orientation.md) — direction, sign, ratios, units against the consumer line (4.18)
- [Literature sweep](literature-sweep-before-not-printed.md) — "not printed" = not found by a stated search; test the library by exact names (2.6)
- [Route refuted: close the route](route-refuted-close-route-not-item.md) — record what fell, re-locate, keep the truth word, re-cut (7.19)

## Review and closing
- [Closed means the criteria hold](closed-means-criteria-hold.md) — strict, continuous; own inputs left = OPEN (1.4)
- [Frozen open ledger](frozen-open-ledger.md) — never renumber; "open N of M"; DEPENDENT only on another item (1.2)
- [Clerical one-NOT rule](clerical-one-not-rule.md) — all blockers clerical: erratum + ledger + one diff lens; no exceptions (5.4)
- [Relay verbatim, every item](relay-verbatim-all-blocking-items.md) — load-bearing clause with file:line; all blocking items numbered (6.5)
- [Parallel re-review](parallel-rereview.md) — same owner resumed; fix filed and named at once; self-check in parallel (5.8)
- [Errata hygiene](errata-hygiene-digits-by-script.md) — anchors exact, digits by script, safe rounding, no extra sentences (5.12)
- [Open but algorithmic](open-but-algorithmic-class.md) — proved and paired, waiting only on a guaranteed computation
- [Stop-reason census first](stop-reason-census-before-verdicts.md) — cut, refused or empty = not landed, whatever the summary says (4.6)

## Communication
- [Count first](status-count-first.md) — "open N of M, now: ..."; one or two lines per item with resources (1.8)
- [Progress as x of y](progress-x-of-y.md) — counts, never "basically done except a few inputs" (6.9)
- [Done / Still needed / Now](done-needed-now-format.md) — labelled clauses per item; never a floaty "X runs" (7.7)
- [No difficulty framing](no-difficulty-framing.md) — not hard, crux, critical, central, setback; "close" and "other todos" (7.10)
- [Todos are todos](todos-neutral.md) — neutral list with worker and waits-on; no tonight/later, no easy/hard (7.11)
- [Name the kind of evidence](evidence-kind-named.md) — open math / computed input with incomplete certification / reading (7.9)
- [Running computations are attempts](running-computations-are-attempts.md) — name the gate and the shortfall modes (7.8)
- [Timestamps from the clock](timestamps-from-clock.md) — copied from an earlier clock call; stale is fine, future never (6.4)
- [Post length measured](post-length-measured.md) — assert the cap by script; split at a boundary; one retry (7.12)
- [Algorithmic vs mathematics lists](status-algorithmic-vs-mathematics.md) — two labelled lists per item; parts by item group

## Staffing and context
- [Watch agent token counts](watch-agent-token-counts.md) — the harness count governs; ask at HANDOVER_ASK_AT, spawn at HANDOVER_SPAWN_AT (9.4)
- [Owner persistence via digest](owner-persistence-digest.md) — one line per landed file; relays are names and verdict words (9.2)
- [Successor onboarding early](successor-onboarding-early.md) — v1 early, addenda per landing; successors read small; seat until "up" (9.3)
- [No restart after a freeze](no-restart-after-freeze.md) — resume nothing without the user; spawn fresh from memos (8.5)
- [Hanging sweep](hanging-sweep-every-status.md) — lanes, questions, items, decisions overdue; act the same turn (7.16)
- [Leftovers sweep](leftovers-sweep-after-switch.md) — orphans, ownerless items, unbooked verdicts, cut logs, "partial" outputs (8.11)
- [Cap is soft in the transient sense](cap-soft-transient.md) — steady count bounded; holding roles stand down with respawn triggers (8.2)
- [Comms audit every status](comms-audit-every-status.md) — void, truncated, refused, lost, cut, missing; flags to owners (6.10)

## Hygiene and failure modes
- [No deletes, new names](no-deletes-new-names.md) — nothing of record removed or overwritten; tmp only if the user allows (6.3)
- [Volume safety](volume-safety-no-root-search.md) — never search from / or a shared mount root; never name a device file (10.4)
- [Never glob-poll big dirs](never-glob-poll-big-dirs.md) — exact names; five-minute polls; wall-clock bounds; two watchers (8.7)
- [Launch hygiene](launch-hygiene.md) — dry-run, ranged attachments, text last, no '&', no self-matching waiter, one-line specs (4.7)
- [No settings changes unasked](no-settings-changes-unasked.md) — propose a guard in one line and wait (10.3)
- [Midnight rollover](midnight-rollover.md) — dates in names; "latest" by content; scope minute comparisons to today
- [Background shells outlive the session](background-shells-outlive-session.md) — list orphans at every restart; stop only your own
- [Python caps enforced](python-caps-enforced.md) — ulimit and timeout in the command, never only in the brief (8.8)
- [Compute is never assumed](compute-not-assumed.md) — light checks always; heavier local compute or scheduler use only when granted (8.13)

## Infrastructure (optional)
- [API lanes: write early, split](api-lanes-write-early-and-split.md) — result section first; one lemma per lane; stagger starts (4.4)
- [Launch registry](launch-registry-pattern.md) — shared append-only registry when several agents launch
- [Batch queue: one standing line](batch-queue-one-standing-line.md) — one package, one queue line, the user's unchanging submit line
- [Channel Stop hook](channel-stop-hook-posts-human-turns-only.md) — human- and agent-started turns post; cron turns do not; never both
