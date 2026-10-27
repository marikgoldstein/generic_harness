# RESOURCES.md (profile: one account, a few subagents)

USER: <you>
DECIDERS: USER
COLLABORATORS: none
PUBLIC_NAME_POLICY: no people's names, emails or process notes in any public document

CLAUDE_CODE: yes
API_KEYS: no
STRONGEST_MODEL: default      # the session's model; set an id to override
REVIEW_MODEL: <same, or one tier down for refuters>
EFFORT: max
OUTPUT_CAP: default

MAX_CONCURRENT_AGENTS: 4            # the main agent + 3 subagents, e.g. two owners and one reviewer or closer
LANES_PER_PIECE: 0
LANES_PER_BIG_ITEM: 0
API_CONCURRENT_LANES: 0
REVIEW_LENSES: 2              # two fresh subagents per load-bearing text

PROVE_PROMPT_CAP: n/a
REVIEW_PROMPT_CAP: n/a
ATTACHMENT_CAP: n/a

HOST: workstation
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
STATUS_INTERVAL_MIN: 30
TIMEZONES: UTC

HELD_DECISIONS: money or keys; settings, hooks or config changes; a final theorem's statement or hypotheses
DEFAULT_WHEN_AWAY: decide, start, report
DELETE_POLICY: strict
FORBIDDEN_SOURCES: none

HANDOVER_ASK_AT: 450k
HANDOVER_SPAWN_AT: 600k
ONBOARDING_V1_AT: 150k

# What changes with this profile:
# - owners are subagents spawned with the strongest model and EFFORT through the tool parameter (4.9).
# - "lanes" are extra subagents when the cap allows; otherwise the owner cycles routes itself (3.4 fallback).
# - review pairs are two fresh subagents; the lead relays verdicts verbatim (5.1, 6.5).
# - the lead reads every task notification's token count and runs the hand-over marks (9.4).
