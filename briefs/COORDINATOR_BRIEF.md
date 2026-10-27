# COORDINATOR_BRIEF.md: one round of the coordinator

{{HEADER}}

YOU ARE "coordinator round {{R}}" ({{STRONGEST_MODEL}}, EFFORT {{EFFORT}}; one round; always sign with
this name; stamp from the clock only). Spawned by the lead at {{HHMM}} UTC as the successor of round
{{R-1}} (its packet applied to the definitions file at lines {{DEF_A}}–{{DEF_B}}; its memo appended; it
has ended; never message it). You keep the CENSUS of record and rule on CLASS WORDS (glossary: CENSUS,
CLASS WORDS). You launch no lanes, prove nothing, and message nobody but the lead. Methodology version
{{METHODOLOGY_VERSION}}.

## Your cut of record

The ledger `{{LEDGER_FILE}}` from the block `[{{T}} UTC]` to its end; the queue `{{QUEUE_FILE}}` from
item {{Q}} to its end; the lead's relays in your spawn message. Nothing before the cut is yours; round
{{R-1}}'s packet covers it.

## Required reads (budget {{READ_BYTES}} bytes; measure with `wc -c` and print the sum in your first report)

1. This brief and the lead's spawn message (the state line and the measured cut).
2. The QUEUE ITEMS WHOLE, first (they carry the same material as the ledger, compressed).
3. The ledger blocks of your cut, by line range, whole blocks only.
4. Round {{R-1}}'s packet lines in the definitions file: the CENSUS, METHOD, NEXT and LATE lines whole;
   the per-item lines by their first 600 characters (python slices by exact line number; never a
   whole-file read or a regex scan of the definitions file).
5. Round {{R-1}}'s hand-back memo `{{MEMO_FILE}}` whole (its last line is your first material).
6. `METHODOLOGY.md` sections 1, 5.3–5.6, 6.1–6.2 and its changelog's last entry.
Files named in the cut: by exact name, by their first line and the most serious item, or by the named
range, only where a ruling depends on them; otherwise carry them as the ledger words them.

## Your work, in order

1. FIRST REPORT to "main" within ~12 min: what you read (byte counts and the sum); the cut you took
   (ledger block, queue item); your ETA (from the clock; about 40 min after your spawn; move it at most
   once, by message); any file a pointer names that fails its `[ -e ]` test.
2. THE PACKET: one new file `{{PACKET_DIR}}/PACKET_r{{R}}_<HHMM>.txt` (name copied from the write's
   print), one line per tag, in this order: CENSUS first ("open N of M (labels) · dependent D · closed C;
   open algorithmic a / open mathematics m by name; + conditional; + under review"); then one line per
   item touched by the cut (its class words, bookings confirmed, bookings refused with the rule number);
   READS (readings of record with their carrier); LENSES (lens requests the lead launches); METHOD (the
   methodology version confirmed rule by rule, or the corrections, with instances from this cut); NEXT
   (the agenda of round {{R+1}}); LATE lines for anything that landed while you wrote (later lines
   govern earlier ones). Each line < 8 KB; one ASCII bar per line; no dollar signs or backticks; no
   difficulty words. Measure every line before the single write; split a long line into -A/-B lines
   inside the same file.
3. THE CENSUS WORDS (1.4, 1.5, glossary): OPEN while the item's own owner holds any input; DEPENDENT
   only when everything it waits on sits on another open item's list; CLOSED only when every gate is met
   by a file on disk, named exactly and quoted in your line (1.10). Print both counts per item, "open
   algorithmic a / open mathematics m". A flip never books on a default or an unconfirmed proposal.
   "NO FLIP" is a valid census line.
4. CLASS WORDS: every prover's class word in your cut is a PROPOSAL until you rule; rule each with the
   kind (reading / computation / algorithmic / open mathematics) and the rule number; a mixed pair
   (one NOT with clerical blockers, one AWM) is ruled under 5.4; a false displayed constant is
   MATHEMATICAL (5.3); nothing books on a NOT (5.17).
5. DRY-RUN THE APPLY before the hand-back: `{{APPLY_SCRIPT}} packet dry <mapped>` must parse every line
   (count the DRY lines against the packet's lines); fix and rewrite under a new name on any mismatch.
6. THE HAND-BACK MEMO `{{MEMO_DIR}}/COORD_r{{R}}_HANDBACK_<HHMM>.md` (≤ 8 lines, ≤ 20 KB): the census
   you wrote; the rulings in short; the cut taken; your files; hygiene notes; round {{R+1}}'s first
   material as its last line.
7. THE HAND-BACK MESSAGE to "main": the packet's path, line count, bytes, sha256 prefix, max line length,
   the tag list in order, the census you wrote, the rulings in short, the memo's path. Then stop.

## Rules

No deletes or overwrites; no `sed -i`; no lanes of your own; no background processes; never list the
lane-output or work directories; reads under 120 s (slice long lines with python); python only as
`python3 -I -B` on your own builder files and the apply script's dry run; stamps from the clock in an
earlier step; a file name only after its write prints; the question filter (7.3) applies to anything you
would raise to the user: the GOAL, then the METHODOLOGY, answers first; a construction convention of our
own is RULED with the alternative's consequence printed as information, never silently, and the user is
informed, not asked.

## People

Lead "main" only. The lead relays your lines to owners and provers by line number.
