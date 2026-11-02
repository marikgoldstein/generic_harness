# CHANGELOG

Dated entries, newest first. Each entry is also the portable note for its change: what was updated, where, with
what information, so that a project already running on this harness can take exactly the pieces it wants.
Everything here is generic: no field, project, person or machine is named.

## 2026-11-02 (later the same day): the graph view, and an examples/ directory

Source: the same project's process explainer, written by its owner for colleagues who formalize proofs. The
abstract counterparts of its ideas were added to the rules first; the explainer itself went into `examples/`
as an illustration (its field, models and numbers are the project's, not defaults of this harness).

| what was updated | where | with what information |
|---|---|---|
| glossary | `METHODOLOGY.md` section G | LINE (a numbered thread of items about one obstacle; the headline count), MISMATCH, CONFIRMATION versus CERTIFICATION, CONDITIONAL-ON MARK, LEAVES |
| lines and the mark | `METHODOLOGY.md` 1.13 | the count of open lines computed each time; re-opening; the goal's conditional-on mark; zero is not the end, the leaves remain and are listed |
| numerics | `METHODOLOGY.md` 2.15 | confirmation (evidence) versus certification (a computed input); CLOSED rel. the certification; OPEN BUT ALGORITHMIC for the waiting item; enumerations run by independent routes |
| provers and briefs | `METHODOLOGY.md` 4.23, 4.24 | the prover output format (status first, inputs used, numbered steps citing inputs, "what a referee should check first"; a GAP names a new item); every brief written from the source and checked by a second agent; what a brief says |
| two leads | `METHODOLOGY.md` 7.25 | a sub-programme's own lead: own ledger and agents; numbered audit findings and suggestions through write-only inboxes, never instructions; direction from the user and deciders only |
| the graph | `METHODOLOGY.md` new section 14 (14.1–14.5) | the ledger as a DAG (hypotheses in, consumers out, leaves); what the graph decides; refutation propagation and mismatch resolution; the proof-assistant correspondence; the caveat said in every hand-off |
| version note | `METHODOLOGY.md` Changelog, v2.1 | the list above |
| examples | `examples/README.md` (new); `examples/process_explainer_lattice_qft_2026-11-02.md` (new) | what the directory is, how to read it, that project details are illustrations; one project's explainer verbatim under a two-line header naming the METHODOLOGY sections it illustrates |
| pointer | `README.md` ("Where to look") | one line to `examples/` |

How to adopt: the new rules are additions tagged "(added 2026-11-02, later)"; append them under the same
numbers. The example is optional reading; nothing in it is a default of this harness.

## 2026-11-02: closure by adversarial confirmation, waves, edit lanes, extractable public text

Source: a second running project's week of closing a large proof record with API lanes, local writers,
adjudicators and outside models. Project specifics were removed; the lessons kept their episodes in neutral words.

| what was updated | where | with what information |
|---|---|---|
| glossary | `METHODOLOGY.md` section G, after BOOKING | AXES of a ledger line (status / consumption / text of record); TEXT OF RECORD; the optional STATUS LADDER (OPEN, HYPOTHESIS, PRINTED / SKETCHED / ASSERTED, PROVED-SINGLE, DERIVED rel., CLOSED-READY, CLOSED rel., VERIFIED); REFUTER with opposite work orders; CLOSURE RE-READ; WRITER; EDIT LIST / EDIT LANE; WAVE; BUILDER; ADJUDICATOR; PERMANENT AGENT |
| ledger axes and tally | `METHODOLOGY.md` 1.11, 1.12 | three axes per line, "closed" booked per axis; a numbered CLOSED tally; hand-offs carry open counts and the ledger path; "0 open" on a build means clean build |
| literature and certification | `METHODOLOGY.md` 2.12–2.14 | PRINTED / SKETCHED / ASSERTED grades, gap lines for printed steps that do not follow, read at the page image; two blind readers for anything read off an image; what a numerical certification does and does not certify; constants carried with dependence lists |
| lane hygiene | `METHODOLOGY.md` 4.19–4.22 | absolute paths, dry-run from the runner's directory, paths tested, no guessed future files; output-cap floors and rebuild-not-retry; one runner per group, "cut at" phrases read before ruling; outside models as claims until two readers confirm, packets with verbatim definitions by a writer and a referee |
| closure and the judge loop | `METHODOLOGY.md` 5.18–5.22 | the closure rule (prover text, two refuters with opposite work orders postdating the last change, writer's text of record, one closure re-read; a refuter blocks only with a false displayed sentence; named clauses; one re-read per hypothesis-level change, none for editorial); the judge loop (one OK + one OK-with-clerical = confirmed; adjudicate, do not re-run; mechanical verdict list first; grade words are not arguments); the writer adds nothing; a prescription is a claim and two failed repairs end patching; edit lanes, Lead decisions read before a re-read, triage after every editorial pass |
| bookkeeping | `METHODOLOGY.md` 6.17, 6.18 | counts computed from the id list in the same step; edit lists applied by script to a copy, each Old once, census and checksum, hunks verified against the current tree |
| cadence | `METHODOLOGY.md` 7.24 | a parallelism check every 30 minutes; a dated method-lessons file consulted before launches and questions |
| safety | `METHODOLOGY.md` 10.11–10.14 | device files only as redirect targets, no process substitution, no placeholder commands; `test -e` before creating, one process per job, capped writes, `python3 -I` for downloaded files; never edit a running script; report every slip at once |
| the wave pipeline | `METHODOLOGY.md` section 12 (12.1–12.6) | builder → provers, refuters, readers in parallel → adjudicator → lead, writers, re-reads, edit lanes; coarse to fine; whole-context work local, isolated mathematics in lanes; permanent agents on lines open across waves; two confirmations with opposite work orders; cross-campaign transfer |
| extractable public text | `METHODOLOGY.md` section 13 (13.1–13.7; 13.6 PROPOSED) | labelled environments and cross-references only; named hypotheses listed per theorem; a conventions group per part with a self-test; no process words; a map from ledger line to theorem label; the extraction test (reference closure) as a proposal; the text pipeline (hunks to a copy, census, checksum log, rulings RIGHT / DONE-BEFORE / WRONG / RECORD / LOG) |
| version note | `METHODOLOGY.md` Changelog, v2 | the list of rules added; no rule renumbered or retired |
| self-check | `SELF_CHECK.md` section 1 questions 21–24; section 3, four new drifts | confirmed how; verdict list or count; Lead decisions read; counts computed |
| new briefs | `briefs/WRITER_BRIEF.md`, `briefs/ADJUDICATOR_BRIEF.md`, `briefs/EDIT_LANE_BRIEF.md`, `briefs/BUILDER_BRIEF.md` | spawn prompts for the four wave roles, in the existing brief format (HEADER, required reads measured in bytes, numbered work, report line) |
| briefs index | `briefs/README.md` table | one row per new brief |
| safety block | `briefs/HEADER.md`, appended section | the one-line SAFETY form for short briefs (no deletes; device files only as redirect targets; no process substitution; no placeholder commands; scoped, time-limited searches; one process per job; capped writes; `test -e`; downloaded files untrusted; write paths named; report slips) |
| refuters and re-reads | `briefs/REVIEW_LENS.md`, appended section | the refuter task text with opposite work orders; the closure re-read task text; what the lead does when each lands |
| templates | `templates/EDIT_LIST.md` (new); `templates/LEDGER.md`, appended optional block | the Old/New block format with `STATUS: EDITS n` and `Lead decisions`; the three axes and the evidence chain as optional lines per item |
| memory seed set | `memory/` 13 new files: `closure-two-refuters-writer-reread`, `adjudicator-mechanical-verdict-list`, `writer-adds-nothing`, `prescription-is-a-claim`, `edit-lane-lead-decisions-before-reread`, `counts-computed-from-id-list`, `two-blind-image-readers`, `outside-answers-claims-until-two-readers`, `packets-verbatim-definitions`, `output-cap-floors-rebuild-not-retry`, `never-edit-running-script`, `named-clauses-not-silent-weakening`, `certification-semantics`; `memory/launch-hygiene.md` appended; `memory/MEMORY.md` index (new section, two hygiene lines) | one lesson per file in the seed set's Why / How to apply form, each citing its episode in neutral words |
| pointers | `README.md` ("Where to look"), `CLAUDE.md` (Roles) | one line each to this file and to the wave-role briefs |

How to adopt in a project already installed from this repo: `git pull`; the new briefs, templates and memory
files are new names and can be copied in as they are (`install.sh` never overwrites); for `METHODOLOGY.md`,
`SELF_CHECK.md` and `CLAUDE.md`, which a project may have edited, every addition carries the tag
"(added 2026-11-02)", so `grep -n "added 2026-11-02"` on the pulled copy lists each one to append by hand under
the same numbers; add the new section of `memory/MEMORY.md` to the project's index. Nothing in this entry removes
or renumbers an earlier rule.
