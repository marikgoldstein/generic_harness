# discord_bridge/: a Discord channel for the lead

Turned on by `CHANNEL: discord` in RESOURCES.md. The user (and collaborators) follow the work from a
phone; the lead posts statuses and answers there; the Stop hook posts the lead's final answer of every
human-started turn so nothing is typed twice.

## Pieces

- `discord-notify` (python, stdlib only): posts stdin or its argument to the channel of `$DISCORD_ROUTE`
  through the bot API. Secrets come from `$DISCORD_ENV_FILE` (default `~/.config/harness/discord.env`,
  mode 600) with `DISCORD_BOT_TOKEN=...` and one `DISCORD_CHANNEL_ID_<ROUTE>=...` per route. A route with
  no channel id is an error, never a fallback to another channel. Posts over 1900 characters are split on
  line boundaries. `--file x.png "caption"` posts an image. The speaker label is `**$AGENT_LABEL:**`
  (default `Claude`) unless the text already starts with a label.
- `discord-history --hours N [--out FILE]`: dumps the channel as plain text, oldest first (read-only).
- `hooks/stop-post-reply.sh` (a Claude Code Stop hook): posts the turn's final text when the turn was
  STARTED by a human message; stays silent for turns started by a cron, a task notification or a system
  message. Gated by the hook's cwd being under `$HARNESS_ROOT`. Waits until the transcript stops growing,
  prefers the final text the Stop event carries, de-duplicates by md5. Log: `hooks/stop_post_reply.log`.
- `hooks/echo-user-prompt.sh` (a UserPromptSubmit hook): mirrors prompts typed in the terminal as
  `**$USER_LABEL:** ...` so the channel carries both sides. Skips prompts that came from the channel (a
  speaker prefix or `[discord]` within the first 16 characters), machine prompts (cron, task
  notifications, system reminders) and agent messages.
- `settings.json.example`: the hook registration and the env block; copy into `.claude/settings.json`
  of the lead's folder after editing the paths.

Inbound (channel to terminal) is not included: either run the lead interactively and paste, or write a
small poller that fetches new messages from allowed speakers every 30–60 seconds and types them into the
lead's terminal as `<Speaker>: <text>` (the hooks above already recognise that prefix). Keep one poller
per channel; make it hold messages while the lead is not running; have it react with an emoji as a
receipt.

## Setup

1. Create a bot in the Discord developer portal with the "Send Messages", "Read Message History" and
   "Add Reactions" permissions; invite it to your server; copy the token and the channel id(s).
2. Write `~/.config/harness/discord.env` (mode 600):
   ```
   DISCORD_BOT_TOKEN=...
   DISCORD_CHANNEL_ID_MAIN=...
   ```
3. In the lead's shell or `settings.json` env: `DISCORD_ROUTE=main`, `DISCORD_ENV_FILE=...`,
   `HARNESS_ROOT=<the lead's folder>`, `AGENT_LABEL=Claude`, `USER_LABEL=<your handle>`.
4. Test: `echo "[setup test]" | ./discord-notify`, then `./discord-history --hours 0.1`.
5. Register the hooks (see `settings.json.example`); `chmod +x` the scripts.

## Rules (METHODOLOGY 7.12, 7.13, 10.2)

- Posts ≤ POST_CAP_CHARS (1800 for Discord: the API cuts at 2000). Build every status in a script that
  asserts the length BEFORE writing the post file; split at a section boundary into numbered parts; one
  retry at most on an over-length single post. Never let Discord cut a post mid-sentence.
- A status every STATUS_INTERVAL_MIN minutes while anything is live, replies to the user, and selected
  structural results. No raw agent output, no routine landings.
- Times as TIMEZONES ("HH:MM UTC / HH:MM <local>"), copied from a clock call in an earlier step.
- The Stop hook posts ONLY turns started by a human message. In a turn started by a cron or a task
  notification, an answer the user must see goes by `discord-notify`. Never both (the user gets two
  copies). When unsure, check with `discord-history` after the turn.
- Everything is mirrored, so never print a secret, not even a prefix.
- One channel per project; nothing from another channel is acted on, echoed or logged here.
