---
name: launch-hygiene
description: Dry-run every spec before launch; one range per file entry; attachments ranged under the cap with every quoted line inside a range and the text under review last; never a trailing '&' or a self-matching pgrep waiter; check a spec has one line before running it N times (4.7, 4.8, 8.9)
metadata:
  type: feedback
---

Before any launch: dry-run the build; compare each lane's attachment count with its source line; no cut markers; sizes within the caps. Launch as the foreground command of the harness's tracked background mechanism, one lane per run, so each landing is replaced alone and a completion notice arrives.

**Why:** once, in a running project, each of these cost an hour or a wrong report: a multi-range attachment token the builder did not support (the round silently never ran); a waiter on a process-name pattern that matched its own command line (it never fired); a run launched with a bare ampersand (its output and completion notice were lost; this slipped four times); a twelve-lane spec run once per lane "by index" that actually ran the whole spec twelve times; a builder that silently dropped every attachment with an unknown path prefix (most of a pool ran with no attachments and "proved" weaker statements).

**How to apply:** one statement per line; attachments over the cap carry explicit line ranges, with the last line counted by content (a final line without a newline is undercounted); the text under review goes last and whole; after every build compare attachment counts; before launching N runs from one spec, check the spec has one line; never chain synchronous runs in one shell. Related: [[stop-reason-census-before-verdicts]], [[comms-audit-every-status]], [[api-lanes-write-early-and-split]].

**Added 2026-11-02 (a second project; 4.19–4.21):** attachments by absolute path, and the dry-run from the runner's own directory (a relative path passed a dry-run from the project root and failed in the runner's directory); every attachment path tested before the run (a spec that named a writer's future file under a guessed name failed the whole build with no output); one runner per group when the runner processes groups sequentially (later groups sat idle for twenty minutes); landed verdicts read for "cut at" / "ends at line N" phrases before ruling (two re-reads returned a gap only because the per-file cap had cut their text). Related: [[output-cap-floors-rebuild-not-retry]], [[never-edit-running-script]].
