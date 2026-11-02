# EDIT_LIST (the output of an edit lane; METHODOLOGY 5.22, 6.18; applied by script to a COPY of the text, never in place)

STATUS: EDITS <n>
Text: <path of the attached text, with its version> · Ruling: <path; items ruled> · Written: <HH:MM UTC, by the clock>

### E1 (ruling item <j>; kind: editorial | statement-level | hypothesis-level)
Old:
~~~
<the exact bytes to replace, copied from the attached text; they must occur there exactly once>
~~~
New:
~~~
<the replacement; a statement-level or hypothesis-level change is a NAMED CLAUSE, "rel. (H-k)", worded as the ruling words it>
~~~

### E2 (ruling item <j>; kind: ...)
Old:
~~~
...
~~~
New:
~~~
...
~~~

## Lead decisions
- ruling item <j>: NOT applied: <source not in the excerpts | Old occurs twice | would change the statement beyond the ruling>. Needed: <the file or decision>.

<!--
The applying script: asserts each Old occurs exactly once in the current text; writes version <v+1> under a new
name; logs the checksum of the result; refuses the whole list when any Old is missing or ambiguous.
The lead: reads `Lead decisions` BEFORE launching any re-read ("source not in the excerpts" = rebuild the lane with
the source attached); one closure re-read follows only if any block is hypothesis-level; statement-level blocks
are ruled on explicitly at closure and their named clauses enter the ledger line.
-->
