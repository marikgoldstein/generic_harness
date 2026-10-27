# optional/: plug-ins

None of these is required. The methodology works with a terminal, one agent and no scheduler. Each
plug-in is turned on by a value in `RESOURCES.md`:

| plug-in | turned on by | what it adds |
|---|---|---|
| `discord_bridge/` | `CHANNEL: discord` | outbound posts from the lead, a Stop hook that posts final answers, a prompt-echo hook, a history dump |
| `batch_queue/` | `BATCH_SYSTEM:` anything but `none` AND `BATCH_USE: recommend` or `agent` (never assumed; the lead asks first) | the "agent prepares, user submits" queue: one standing submit line for the user, done markers, a line checker |
| `launch_registry/` | several launching agents and `API_KEYS: yes` | a shared append-only registry that staggers lane launches across agents and a waiter script |

Each directory has its own README with the pieces and the rules. Scripts take their configuration from
environment variables or arguments; nothing is hard-coded to a machine. Secrets live in a file outside
the project tree with mode 600 and are never printed.
