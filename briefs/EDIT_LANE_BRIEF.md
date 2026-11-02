# EDIT_LANE_BRIEF.md: the edit lane (a byte-exact edit list)

{{HEADER}}

An EDIT LANE turns a ruling (a re-read's REQUIRED and MINOR lists, or the lead's rulings on them) into a byte-exact
EDIT LIST that a script applies to a copy of the text (METHODOLOGY 5.22, 6.18; the format is
`templates/EDIT_LIST.md`). It runs as an API lane or as a short-lived local agent. It never applies its own
edits, never edits in place, and never fills a gap.

## Task text (fill the fields; attach the text LAST and whole, or in line ranges under ATTACHMENT_CAP)

> EDIT LIST for `{{TEXT}}` version {{V}}. Attached: the ruling `{{RULING_FILE}}` with its numbered items, every
> source file the ruling cites ({{SOURCES}}), and the text itself. For each ruled item produce one block headed
> `### E<k> (ruling item <j>; kind: editorial | statement-level | hypothesis-level)`, then `Old:` with the exact
> bytes to replace, copied from the attached text and occurring there exactly once, then `New:` with the
> replacement. A statement-level or hypothesis-level change is written as a NAMED CLAUSE ("rel. (H-k)") exactly
> as the ruling words it, never as a silent weakening. First line of your output: `STATUS: EDITS n` (n = the
> number of blocks). Last section: `Lead decisions`: every ruled item you could not place, with the reason
> ("source not in the excerpts", "Old occurs twice", "would change the statement beyond the ruling"). Add no
> sentence the ruling does not require.

## What the lead does with the output (5.22)

1. Reads `Lead decisions` BEFORE launching any re-read. An item "not applied: source not in the excerpts" means
   the lane is rebuilt with that source attached; the ruling's own words are never enough for the New text.
2. Applies the list by script to a copy: the script asserts that each Old occurs exactly once, writes the new
   version under a new name, and logs the checksum of the result (6.18).
3. Launches one closure re-read if any block is hypothesis-level; none if every block is editorial; rules
   explicitly on each statement-level block at closure (named clause into the ledger line).
4. After an editorial pass over several texts, one triage agent classifies every `Lead decisions` item of every
   output against its re-read (REQUIRED / OPTIONAL / DONE) before any item books at the new version.

## Output cap

An edit lane reads a long text and a long list before it writes: set its cap at the floor of 4.20 or above
(one project used 48k, and 64k to 96k when the text was over 50 KB or the list long). A lane that returns no
text with stop reason "output limit" is rebuilt at a higher cap, never retried at the same one.
