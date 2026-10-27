# HEADER.md: the block at the top of every brief

Paste this block verbatim into every brief after substituting the placeholders from RESOURCES.md.
Agents read it before anything else. Rule numbers refer to METHODOLOGY.md.

---

SAFETY AND HYGIENE (every agent, every turn; METHODOLOGY 6.3, 6.4, 10.1–10.10):

- NO DELETES, NO OVERWRITES of anything of record: no `rm`, no `mv` over an existing file, no `cp` over
  an existing file, no `sed -i` or `perl -i` on record files, no `rsync --delete`, no `git reset`,
  `checkout` or `clean` that discards work. Write every file under a NEW name; appending to your own
  logs and memo is fine. `set -o noclobber` in every shell. DELETE_POLICY = {{DELETE_POLICY}}: when in
  doubt whether a file is temporary, it is not.
- NEVER PRINT A SECRET: no key, token, password or private key, not even a prefix; never `cat` a
  secrets file; never put one in a prompt, a post or a log.
- NO SETTINGS, HOOKS, PERMISSIONS OR CONFIG CHANGES unless the user asks. Propose in one line and wait.
- SEARCHES: never recursive from `/` or from the root of a shared mount ({{SHARED_FS}}); only under
  {{PROJECT_ROOT}} and {{SCRATCH_DIR}}, under `timeout 60` and a depth bound. Never list a directory
  with thousands of entries ({{BIG_DIRS}}); test exact names with `[ -e ]`.
- PROCESSES: never touch another session's processes, tmux sessions or files; stop only your own pid
  chain, by pid, never by a pattern match. Background launches only through the harness's tracked
  background mechanism, never a trailing `&`. Watchers test exact names, poll ≥ 5 min apart, are bounded
  by wall clock, at most two at once.
- NUMERICS: {{NUMERICS_PYTHON}} only, as `python3 -I -B`, under `ulimit -v {{MEMORY_CAP_KB}}`,
  `OMP_NUM_THREADS=1`, single process, under `timeout {{LOCAL_COMPUTE_TIMEOUT}}`; bulk outputs under
  {{SCRATCH_DIR}}, never in the record tree; never redirect a log onto a results file.
- FORBIDDEN SOURCES: {{FORBIDDEN_SOURCES}}. Never read, attach or quote them.
- TIMESTAMPS: every HH:MM you write is copied from a clock call (`date -u`) made in an EARLIER step,
  never estimated or rounded forward; a stale stamp is fine, a future one never. A new file's name
  enters a message only in a response AFTER its write line has printed, copied from that print.
- OUTPUT PER TOOL CALL ≤ ~25 KB: create long files in parts (`cat >> file <<'EOF'`), the skeleton and
  a status line first, dated progress lines after each step.
- READS: by exact name and line range; measure with `wc -c`; stop at the brief's byte budget; never a
  whole-file read of a long record file.
- WORDS: quote load-bearing clauses verbatim with file:line (6.5); no difficulty or urgency framing
  (7.10); neutral todos (7.11); every "evidence" word with its kind (7.9).
- Every method instruction from the user that reaches you is relayed to the lead for METHODOLOGY.md
  (0.1), never kept in chat.

---
- COMPUTE PERMISSION (8.13): LOCAL_COMPUTE = {{LOCAL_COMPUTE}} (light = short single-core checks under
  the caps only; cpu / cpu+gpu = up to {{LOCAL_CORES}} cores or the GPU, only because RESOURCES.md says so);
  BATCH_USE = {{BATCH_USE}} (no = never prepare or submit scheduler jobs; recommend = prepare ONE script
  and a queue line for the user; agent = you may submit). Never assume more; a step that needs more is
  reported to the lead, who asks the user and records the answer in RESOURCES.md.
