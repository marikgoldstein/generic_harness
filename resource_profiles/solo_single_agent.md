# RESOURCES.md (profile: one agent, no helpers) = the shipped default in ../RESOURCES.md

USER: <you>
DECIDERS: USER
COLLABORATORS: none
PUBLIC_NAME_POLICY: no people's names, emails or process notes in any public document

CLAUDE_CODE: yes
API_KEYS: no
STRONGEST_MODEL: default      # the session's model; set an id to override
REVIEW_MODEL: <same>
EFFORT: max
OUTPUT_CAP: default

MAX_CONCURRENT_AGENTS: 1            # the main agent alone: you are owner, prover, reviewer and coordinator in turn
LANES_PER_PIECE: 0
LANES_PER_BIG_ITEM: 0
API_CONCURRENT_LANES: 0
REVIEW_LENSES: 2              # two fresh-context passes by you: lens A (break it) in one session, lens B (rebuild) in another

PROVE_PROMPT_CAP: n/a
REVIEW_PROMPT_CAP: n/a
ATTACHMENT_CAP: n/a

HOST: laptop
SHARED_FS: no
BATCH_SYSTEM: none
LOCAL_COMPUTE: light
LOCAL_CORES: 1
BATCH_USE: no
NUMERICS_PYTHON: python3
MEMORY_CAP_KB: 2500000
LOCAL_COMPUTE_TIMEOUT: 55m
SCRATCH_DIR: ./scratch

CHANNEL: terminal
POST_CAP_CHARS: none
STATUS_INTERVAL_MIN: 30       # a status block in the terminal at every natural pause
TIMEZONES: UTC

HELD_DECISIONS: money or keys; settings, hooks or config changes; a final theorem's statement or hypotheses
DEFAULT_WHEN_AWAY: decide, start, report
DELETE_POLICY: strict
FORBIDDEN_SOURCES: none

HANDOVER_ASK_AT: n/a          # no subagents; the lead itself keeps a memo with TO RESUME and re-reads it after any compaction
HANDOVER_SPAWN_AT: n/a
ONBOARDING_V1_AT: n/a

# What changes in the method with this profile:
# - "lane" means a fresh pass by you with the task written out first (METHODOLOGY 4, preamble).
# - "pair" means two separate passes in fresh context, A before B, B without A's notes (5.1).
# - "the level never decays" means: every open piece has a NAMED next route in the ledger at all times (3.11).
# - the status is a block you write in the terminal; the self-check runs before it (7.12, 7.14).
# - everything about memos, TO RESUME and onboarding applies to you (9.1, 9.10).
