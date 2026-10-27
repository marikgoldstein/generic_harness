# memory/: the lead's persistent lessons

Claude Code gives each project a persistent memory directory at
`~/.claude/projects/<project-slug>/memory/`. Its index, `MEMORY.md`, is loaded into context at the start
of every session; the individual files are read on demand. This folder is a seed set: the lessons one
lead learned over two weeks of running the method, with the project specifics removed.

## How the memory works

- One file per fact. Each file has frontmatter with `name` (the slug, equal to the file name without
  `.md`), `description` (one line, used to decide relevance), and `metadata.type`: `user` (who the
  user is), `feedback` (how to work, with the why), `project` (ongoing work not derivable from the
  files), or `reference` (pointers to tools and external resources).
- Feedback files carry a **Why:** paragraph (what happened, in neutral words) and a **How to apply:**
  paragraph (the concrete behaviour). Related memories are linked with `[[name]]`.
- `MEMORY.md` holds one line per memory: `- [Title](file.md) — hook`. Never put memory content in the
  index; it is loaded every session and must stay short.
- Before saving a new memory, check for an existing file that covers it and update that one. Delete
  nothing of record; a memory that turns out wrong is corrected in place with the date.
- After any context compaction, re-read the files relevant to the next action before writing a stamped
  message or a status (METHODOLOGY 9.10). Compactions were where the slips of this seed set recurred.
- Rule numbers in these files refer to `../METHODOLOGY.md`; parameters in CAPITALS to `../RESOURCES.md`.

## Using the seed set

Either copy this folder into your project's memory directory
(`cp -r memory/* ~/.claude/projects/<project-slug>/memory/`), or make that directory a symlink to a
copy kept inside your project tree so it is backed up with the project. Then let the lead add its own
lessons under the same conventions. The seed files are starting points: when your project disagrees
with one, edit it and say why in the file.
