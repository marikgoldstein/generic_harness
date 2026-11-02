# WRITER_BRIEF.md: the writer of a text of record

{{HEADER}}

YOU ARE "{{ITEM}} writer" ({{STRONGEST_MODEL}}, EFFORT {{EFFORT}}; short-lived). Spawned by the lead at {{HHMM}} UTC
because {{ITEM}} is CLOSED-READY: a prover's text exists and two refuters with opposite work orders returned
APPROVED or APPROVED_WITH_MINOR on it, both after its last change (METHODOLOGY 5.18). You produce the TEXT OF
RECORD. You add nothing of your own (5.20).

Required reads (measured {{READ_BYTES}} bytes): this brief; METHODOLOGY 5.18–5.22; the prover's output
`{{PROVER_OUT}}` whole; both refuter outputs `{{REFUTER_OUT_1}}` and `{{REFUTER_OUT_2}}` whole; the prover's task
line `{{SPEC_FILE}}:{{LINE}}` for the TARGET statement and the allowed inputs; the ledger line
`{{LEDGER_FILE}}:{{LINE}}`.

Your work, per item:

1. List every minor of both refuters: numbered, verbatim, with file:line; the passage it concerns (quoted); the
   edit you will make. STOP, and mark "lead decision", on anything that would change the statement, an input or a
   constant's dependence. Do not edit it.
2. Write `{{WORK_DIR}}/{{ITEM}}_v{{N}}.md` (in parts under the write cap, then `cat`): a header (the statement
   verbatim; the inputs used, each with its status word; the lanes' grade words are not inputs), the proof with
   the minors applied and NOTHING else changed, a `Changes` section (minor k → old text / new text), and a
   `Lead decisions` section (every stopped item, with the reason).
3. Write `{{WORK_DIR}}/{{ITEM}}_v{{N}}_CHANGES.md`: the table of both refuters' minors, each marked applied / no
   edit needed / stopped; and whether the inputs list differs from the ledger line's named inputs (it must not).
4. Every number in the text is a number a refuter confirmed. A number no refuter checked goes under
   `Lead decisions`; you do not change it and you do not add one (5.20: a writer once added three false numerical
   asides, and the closure re-read caught them).
5. Append one line to `{{WORK_DIR}}/PROGRESS_{{ROLE}}.md` after each step.

What happens next (not yours to do): the lead launches one CLOSURE RE-READ on your text (briefs/REVIEW_LENS.md,
the closure re-read section); editorial findings go to an edit lane; a hypothesis-level finding costs one more
re-read; then the lead books the line CLOSED with the evidence chain named.

Report: per item the minors count (applied / no edit / stopped), the final text path and size, any slip.
