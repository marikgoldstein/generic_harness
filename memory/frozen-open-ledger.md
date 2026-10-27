---
name: frozen-open-ledger
description: A frozen, numbered list of open items, never renumbered; every status leads "open N of M"; DEPENDENT only when every remaining part sits in ANOTHER item (1.2, 1.5, 1.8)
metadata:
  type: feedback
---

Keep one numbered ledger of items. Never renumber or reuse a label; splits get suffixes; new items are appended and flagged NEW. Every status leads with "open N of M" and names closures and new items by label.

**Why:** once, in a running project, detailed per-lane reports hid whether the open set was shrinking or growing; the co-author asked for labels on the leftover independent things, saying that if the list were frozen one could number it and watch the number go down. Days later an item was booked DEPENDENT on its own parts; the co-author pointed out that was a reduction, and it went back to OPEN.

**How to apply:** DEPENDENT only if everything the item waits on sits on another item's list. Sub-parts get public tags extending the frozen labels (item.01-A), mapped in one file before use; never a fresh top-level numbering in a status. Improvements not needed for the goal are listed separately and not counted. A struck entry prints a struck column, never a smaller total. Related: [[closed-means-criteria-hold]], [[status-count-first]].
