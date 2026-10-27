# ONBOARDING_TEMPLATE.md: how a fresh lead takes over a running project

The outgoing lead (or the user) fills this in and the fresh lead reads it first. It is the ONE document;
everything else is referenced from here with paths. Keep it current while a project runs: one line per
landing in section 7, a new "state at HH:MM" stamp whenever it is rewritten. Rule numbers refer to
METHODOLOGY.md. Written at {{HHMM}} UTC on {{DATE}} by {{OUTGOING_LEAD}}.

Paths used below: `ROOT` = {{PROJECT_ROOT}}; `REC` = the record tree ({{RECORD_DIR}}); `WORK` = the items'
working files ({{WORK_DIR}}); `LANES` = lane outputs ({{LANE_DIR}}, under SCRATCH_DIR; never list it);
`LEAD` = the lead's folder ({{LEAD_DIR}}: inbox, briefs, tools, logs). The lead's own memory index loads
automatically from `memory/MEMORY.md`.

Older background documents, valid where this one does not override them: `CLAUDE.md` (the standing
briefing), `METHODOLOGY.md`, `SELF_CHECK.md`, `RESOURCES.md`, `briefs/README.md`.

---

## 1. What we are proving

**The goal (one printed statement):** {{GOAL_STATEMENT}}.
**Its hypotheses:** {{HYPOTHESES}}. The following are HYPOTHESES taken as others' work and never go on
our open list: {{ASSUMED_AS_OTHERS_WORK}}.
**Purpose:** {{PURPOSE_ONE_LINE}} (for example: existence only; digits are a separate deliverable).
**The route in two or three lines:** {{ROUTE}}.
**The ledger** (`{{LEDGER_FILE}}`): items {{FIRST_LABEL}} … {{LAST_LABEL}}, never renumbered (1.2). The
census of record at {{HHMM}}: open {{N}} of {{M}} ({{OPEN_LABELS}}); dependent {{D}} ({{DEP_LABELS}});
closed {{C}}; open algorithmic {{A}} / open mathematics {{MM}} by name: {{OPEN_MATH_NAMES}}.
**The user's standing order:** {{STANDING_ORDER}}.

## 2. People, and how to talk to them

- **USER** ({{USER}}) and **DECIDERS** ({{DECIDERS}}): who may change a final theorem's statement or
  hypotheses. COLLABORATORS ({{COLLABORATORS}}): equal say on direction where RESOURCES.md says so; the
  latest word governs, and you tell the other. Never give a collaborator secrets or spend money on their
  behalf without the user.
- Routing: {{ROUTING}} (for example: items X and Y to the user, items Z to the collaborator).
- THE QUESTION FILTER (7.3): state the GOAL to yourself; does it answer the question? Does the
  METHODOLOGY? Ask only when a final theorem's statement or hypotheses would change, and say why the
  first two did not decide it.
- Questions in PLAIN FORM (7.4): the plan said X / we found Y / we do not know Z / options, each saying
  whether the main result stays unconditional / recommended / default with the time you act on it.
  Decisions in THREE LINES (7.5).
- NEVER IDLE (7.1): do not wait on a pending choice; pick the useful default, start it, tell them. Hold
  only for HELD_DECISIONS: {{HELD_DECISIONS}}.
- PLAIN WORDS (7.6–7.11): what is proved, what is computed, what is assumed and how it gets proved; "you
  are right" plus the cause; counts as x of y; every item in Done / Open algorithmic / Open mathematics /
  Now; no difficulty or urgency words; neutral todos; agents by role, never a bare letter; public
  labels only.
- RELAY VERBATIM (6.5); TIMESTAMPS from the clock in an earlier step (6.4); times in TIMEZONES
  ({{TIMEZONES}}).

## 3. The channel ({{CHANNEL}})

{{CHANNEL_NOTES}} (for a chat channel: how inbound messages reach you; the outbound command; the post
cap POST_CAP_CHARS measured by script before posting; which turns the Stop hook posts and which need an
explicit post; the posting policy: status every STATUS_INTERVAL_MIN min, replies, selected structural
results, no raw agent output). For the terminal: a status block at every natural pause and in
`STATE_LOG.md`.

## 4. The rules, consolidated

### 4.1 Roles (glossary; scaled to RESOURCES.md)
| role | who | what it does |
|---|---|---|
| lead (you) | the main session | launches, relays landings verbatim, keeps the ledger and the agent register, posts status, answers the user; does not prescribe routes (3.13); does mathematics when it unblocks (3.14) |
| owner | one persistent agent per open item | proves the item in full first; splits under the six criteria; writes lane lines; refills; confirms consumed forms for its consumers (3.1–3.11) |
| dedicated prover | one per open-mathematics input | proves in full or bypasses with the consumer owner's written confirmation (3.12) |
| one-shot prover | an independent agent per item where resources allow | an end-to-end attempt by its own route (3.5) |
| coordinator | a fresh agent per round, or you | the census and class words; one packet per round (6.1) |
| review pair | REVIEW_LENSES lenses per text | A breaks, B rebuilds (5.1) |
| closer | per item with many failed rounds or certified runs | pre-checks in parallel with the review (3.7) |
| editor | outside the proving staff | the public document from the claim tree and the record |

### 4.2 Models and effort
STRONGEST_MODEL = {{STRONGEST_MODEL}} for owners, provers, writers, syntheses; REVIEW_MODEL =
{{REVIEW_MODEL}} for refuters on highly questionable claims (5.10). EFFORT = {{EFFORT}}, set through the
Agent tool's parameter or the API's output configuration, never by prompt text (4.9); audit the
effective effort before relying on a verdict. After an oversight, raise that line and re-audit.

### 4.3 Staffing (RESOURCES.md)
MAX_CONCURRENT_AGENTS = {{MAX_CONCURRENT_AGENTS}} (soft in the transient sense, 8.2); LANES_PER_PIECE =
{{LANES_PER_PIECE}}; LANES_PER_BIG_ITEM = {{LANES_PER_BIG_ITEM}}; the level reached never decays (3.4);
every open piece has its lanes or its named reason (3.11); local slots go to owners, dedicated provers,
the round's coordinator and closers; breadth goes to lanes (8.1); holding roles stand down with respawn
triggers (8.3); resources per open item in every status; a zero is flagged and staffed the same turn.

### 4.4 Judging and closing
Every load-bearing text gets its pair (5.1); verdict words and the clerical / mathematical classing
(5.2, 5.3); the one-NOT rule and the both-NOT clerical rule (5.4, 5.5); a correcting finding = new
version + re-pair (5.6); every blocking item relayed, numbered (5.7); parallel re-review (5.8).
CLOSED strictly by 1.4; DEPENDENT only on another item (1.5); the discharge list (1.6); a reduction
closes nothing (1.7); a census move only on files on disk (1.10). Class words: proved / named reading /
named computation / open but algorithmic / open mathematics (glossary).

### 4.5 Other standing rules
Pin the object and quote the consumer (2.1, 2.2); truth first and numbers first, intermediate steps
included, the threshold quoted before any certified run (2.3, 2.4, 2.4a, 2.4b); the literature sweep
(2.6); targets state scale and quantifiers (2.8); prove, never reduce (3.3); no deletes or overwrites
(6.3); no secrets printed, no settings changes, no searches from a mount root, no touching other
sessions' processes (10.1–10.5); numerics under the caps (10.9); every method instruction into
METHODOLOGY.md the same turn (0.1).

### 4.6 How to launch
A local agent: from the template in `briefs/`, placeholders substituted, reads measured, file names
tested, EFFORT by parameter, in the background; the spawn line in the agent register only after the
tool's result prints (6.15). A lane (if API_KEYS = yes): the owner writes the lane file; the launcher
dry-builds, pre-checks (ranges within files, sizes within caps, the text last), launches one lane per
tracked background run, exports by exact name; the stop-reason census before any verdict (4.6–4.8).
With several launchers: the launch registry (optional/launch_registry). The lane tool: `tools/api_lanes`.

### 4.7 The lead's memory, and why leads froze
Many local agents share the lead's process; freezes came at about a dozen live agents, and resuming
agents with huge transcripts raised memory within minutes (8.5). So: keep far fewer live than that;
spawn fresh from memos rather than resume old transcripts; keep your own tool outputs small (head, cut,
never cat a large file); after a freeze resume nothing without the user's word; grow on the lane side
where lanes exist. Read every task notification's token count and run the hand-over marks (9.4):
HANDOVER_ASK_AT = {{HANDOVER_ASK_AT}}, HANDOVER_SPAWN_AT = {{HANDOVER_SPAWN_AT}}.

## 5. Where to look for progress

| what | where |
|---|---|
| census, rulings, bookings | `{{COORD_MEMO}}` (end of file = latest); `{{DEF_FILE}}` (definitions and rulings of record, appended by packets) |
| the ledger and the discharge lists | `{{LEDGER_FILE}}`; `{{LIST_FILES}}` |
| owners' roster and agent ids | `{{AGENT_REGISTER}}` |
| per-item work | `WORK/<item>/` (texts vN, errata, memos, onboardings; open by exact name from messages) |
| every lane output and verdict | `LANES/<exact stem>.md` (exact names only) |
| clerical passes and bookings | `{{CLERICAL_LEDGER}}` |
| the lead's state log | `STATE_LOG.md` (its last block = where to resume) |
| what was said to the user | the channel's history tool, or `STATE_LOG.md` |
| the public document | `{{PAPER_DIR}}` (claim tree + script-assembled draft) |
| the lead's lessons | `memory/MEMORY.md` and the files it indexes |

## 6. Running processes (do not duplicate)

| process | pid / id | purpose | restart line |
|---|---|---|---|
| backup loop | {{PID}} | versioned mirror every 2 h (tools/backup_versioned.sh) | `{{RESTART_LINE}}` |
| status cron | {{CRON_ID}} | the STATUS_INTERVAL_MIN post | check `CronList` before re-creating; two leads = two statuses |
| channel poller | {{PID}} | inbound messages | {{START_LINE}}, only if not running |
| batch jobs | {{JOB_IDS}} | {{WHAT_EACH_IS_FOR}} | read their output files by exact name; never poll the scheduler |
| lanes in flight | {{COUNT}} | {{LABELS}} | landings land as files; the stop-reason census first |

Run the leftovers sweep before anything else (8.11): orphan processes with no known owner; open items
without a live owner; landed-but-unbooked verdicts; launch logs with MISSING or CUT markers (the run
log, not the dry log); batch outputs without their done marker.

## 7. The open items: state and next step (as of {{HHMM}} UTC)

One block per open item, in the order the user wants them closed:

- **{{ITEM}}** ({{TITLE}}; local {{n}} / lanes {{m}}):
  - Done: {{WHAT_IS_FINISHED_WITH_VERDICTS}}.
  - Open algorithmic ({{a}}): {{CERTIFIED_COMPUTATIONS_AND_REVIEWS_WITH_GATES}}.
  - Open mathematics ({{mm}}): {{EACH_NAMED_INPUT_WITH_ROUTE_STATE}}.
  - Now: {{WHO_IS_DOING_WHAT_EXPECTED_WHEN}}.
  - Owed: {{RELAYS_OR_FILES_OWED_TO_WHOM}}.
- **{{ITEM_2}}** …

Decisions pending with the user or collaborators, and since when: {{PENDING_DECISIONS_WITH_DEFAULTS}}.

## 8. First todos for the fresh lead (in this order)

1. Read sections 1–7, the last block of `STATE_LOG.md`, and the end of `{{COORD_MEMO}}`.
2. Run the leftovers sweep (section 6; 8.11).
3. Check `RESOURCES.md` still matches what you have; if the user has not said how many local agents to
   run, work on the lane side and the bookkeeping until they do, and ask in one line.
4. Relaunch anything killed at the switch: {{KILLED_LAUNCHES_BY_EXACT_NAME}}.
5. With the cap settled, respawn fresh seats from their onboardings in this order: {{RESPAWN_ORDER}}.
   Each owes the relays listed under "Owed" in section 7.
6. Post a short note that you have taken over (the count first). From then on, the status every
   STATUS_INTERVAL_MIN minutes after running SELF_CHECK.md.
