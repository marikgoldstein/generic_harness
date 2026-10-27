# RESOURCES.md (profile: Claude Code account + an Anthropic API key)

USER: <you>
DECIDERS: USER
COLLABORATORS: none
PUBLIC_NAME_POLICY: no people's names, emails or process notes in any public document

CLAUDE_CODE: yes
API_KEYS: yes                 # ANTHROPIC_API_KEY in your shell or a secrets file the lane runner reads; never in a prompt or post
STRONGEST_MODEL: default      # the session's model; set an id to override
REVIEW_MODEL: <same, or one tier down for refuters>
EFFORT: max
OUTPUT_CAP: default          # the lane runner's max_tokens; lanes write partial results by half of it (4.4)

MAX_CONCURRENT_AGENTS: 6            # the main agent + 5: owners, dedicated provers, a coordinator, a closer
LANES_PER_PIECE: 2            # two independent API prove lanes per open piece, refilled the same turn they land
LANES_PER_BIG_ITEM: 4         # 2–6; once reached, the level never decays until the item closes
API_CONCURRENT_LANES: 20      # your spend ceiling; the runner staggers starts (4.16)
REVIEW_LENSES: 2              # the pair runs as two API lanes (lens A break-it, lens B rebuild)

PROVE_PROMPT_CAP: 125 KB
REVIEW_PROMPT_CAP: 150 KB
ATTACHMENT_CAP: 55 KB

HOST: workstation
SHARED_FS: no
BATCH_SYSTEM: none
LOCAL_COMPUTE: cpu                 # the user allowed local cores for numerics
LOCAL_CORES: 8
BATCH_USE: no
NUMERICS_PYTHON: python3
MEMORY_CAP_KB: 2500000
LOCAL_COMPUTE_TIMEOUT: 55m
SCRATCH_DIR: ./scratch        # lane run dirs go under SCRATCH_DIR/lanes/<tag>_<MMDD_HHMM>

CHANNEL: terminal
POST_CAP_CHARS: none
STATUS_INTERVAL_MIN: 30
TIMEZONES: UTC

HELD_DECISIONS: raising API_CONCURRENT_LANES or spend; settings, hooks or config changes; a final theorem's statement or hypotheses
DEFAULT_WHEN_AWAY: decide, start, report
DELETE_POLICY: strict
FORBIDDEN_SOURCES: none

HANDOVER_ASK_AT: 450k
HANDOVER_SPAWN_AT: 600k
ONBOARDING_V1_AT: 150k

# What changes with this profile:
# - breadth goes to the API: every open piece has LANES_PER_PIECE lanes, run with tools/api_lanes (4.1–4.17).
# - local subagents are owners and persistent provers; they write lane lines, the lead (or the owner from a
#   reserved ID block) launches them (4.11).
# - the stop-reason census and the comms audit run at every landing and status (4.6, 6.10).
# - review pairs are API lanes; the assembled argument still gets two local reviewers at half and end (5.9).
