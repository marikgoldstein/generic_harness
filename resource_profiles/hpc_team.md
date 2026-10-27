# RESOURCES.md (profile: shared cluster, a co-author, a chat channel)

USER: <you>
DECIDERS: USER, <co-author>   # equal say on direction; the latest word governs and the other is told
COLLABORATORS: <co-author>    # never give a collaborator secrets or spend money on their behalf without USER
PUBLIC_NAME_POLICY: no people's names, emails or process notes in any public document

CLAUDE_CODE: yes
API_KEYS: yes
STRONGEST_MODEL: default      # the session's model; set an id to override
REVIEW_MODEL: <same, or one tier down for refuters>
EFFORT: max
OUTPUT_CAP: default

MAX_CONCURRENT_AGENTS: 10           # the main agent + 9; soft in the transient sense (8.2); holding roles stand down with respawn triggers (8.3)
LANES_PER_PIECE: 2
LANES_PER_BIG_ITEM: 6
API_CONCURRENT_LANES: 100
REVIEW_LENSES: 2

PROVE_PROMPT_CAP: 125 KB
REVIEW_PROMPT_CAP: 150 KB
ATTACHMENT_CAP: 55 KB

HOST: HPC login node
SHARED_FS: yes /path/to/shared/mount        # never list or glob-poll big dirs; exact names; two watchers max (8.7, 10.4)
BATCH_SYSTEM: slurm
LOCAL_COMPUTE: light               # a login node: never heavy compute locally
LOCAL_CORES: 1
BATCH_USE: recommend          # the agent prepares ONE script + a queue line; the user runs one standing submit line (optional/batch_queue). Set agent where the cluster allows the agent to submit.
NUMERICS_PYTHON: /path/to/python3
MEMORY_CAP_KB: 2500000
LOCAL_COMPUTE_TIMEOUT: 55m
SCRATCH_DIR: /path/to/scratch

CHANNEL: discord              # optional/discord_bridge; the Stop hook posts final answers of human-started turns
POST_CAP_CHARS: 1800
STATUS_INTERVAL_MIN: 30
TIMEZONES: UTC / ET

HELD_DECISIONS: money or keys; heavy local compute; scheduler submission (the user runs the submit line; the agent may cancel its own superseded jobs with notice); settings, hooks or config changes; a final theorem's statement or hypotheses
DEFAULT_WHEN_AWAY: decide, start, report
DELETE_POLICY: tmp-allowed    # a job's own intermediates by a result-gated last step; records never
FORBIDDEN_SOURCES: <list>

HANDOVER_ASK_AT: 450k
HANDOVER_SPAWN_AT: 600k
ONBOARDING_V1_AT: 150k

# What changes with this profile:
# - read-only scheduler queries are one-shot, never polled; outputs are watched by exact file name (8.8, 8.13).
# - a status every 30 minutes on the channel in parts of ≤ 1800 characters, times in both zones (7.12, 7.13).
# - questions to the co-author pass the question filter and the plain form (7.3, 7.4); the co-author is
#   asked only what changes a final theorem's statement or hypotheses.
# - with several launching agents, the launch registry prevents same-minute bursts (optional/launch_registry).
