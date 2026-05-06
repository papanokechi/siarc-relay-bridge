# CMB.txt paste-target instructions for `[OQ-2026-05-06-048R-EARLY-FIRE]`

**Scope:** OPERATOR-DISPATCH ONLY. T2 (056 executer) DOES NOT
modify `tex/submitted/CMB.txt`. This file surfaces the paste
target so the operator can paste at the next CMB-edit
session, avoiding the 052 HALT_LINE_LOCATION_MISMATCH pattern
(executer cited line numbers without operator validation).

**Anchor:** `tex/submitted/CMB.txt` pre-edit SHA-256
`74073D94F247B59CCAB42A5AA96D608F87070CDBDE20F3D06263778FCF68A5DC`,
1900 lines, 84473 B (matches the 048R post-edit state pinned
in the 048R handoff §Key numerical findings).

---

## CMB section-existence triage (per relay 056 STEP 4)

**Branch (a):** *"Open questions" or "Open issues for T1
Synth" section.*
**Result:** **NOT FOUND.** A whole-file regex scan for
`[Oo]pen [Qq]uestion|[Oo]pen [Ii]ssue` returned 4 matches,
all of which are inside the L1400-L1468 narrative block
recording the PCF-1 v3.1 manuscript's §"Further open
questions" addition. None of these constitute a CMB-level
Open-Questions section for T1 Synth. There is no
`## Open questions` or `## Open issues` second-level header
anywhere in the file.

**Branch (b):** *"T1 SYNTH WEEKLY QUEUE" or "SYNTH-TRACK"
section.*
**Result:** **PARTIALLY FOUND — `SYNTH-TRACK` exists as a
recurring banner block, NOT as a single section.** The
SYNTH-TRACK banner appears 9 times across the file
(L1116, L1325, L1374, L1444, L1482, L1523, L1567, L1590,
L1652, L1869) as repeated dated entries, each delimited by
`================================================================`
separator bars. There is no single "T1 SYNTH WEEKLY QUEUE"
section that aggregates Open Questions; the dated SYNTH-TRACK
entries are a chronological journal, not a queue.

**Branch (c):** *Neither exists; append at end-of-CMB with a
new section.*
**Result:** **APPLIES.** Per STEP 4 (c), append at
end-of-CMB with a new `=====` separator + a section header
in the established CMB style.

---

## RECOMMENDED PASTE TARGET (branch (c))

**Location:** end-of-file (currently L1900, the trailing
`================================================================`
separator bar that closes the 2026-05-06 W19 CLOSING + W20
WSB SYNTH-TRACK entry).

**Line-anchor instructions:**

> Paste **after L1900**. The preceding line (L1900) reads:
>
> ```
> ================================================================
> ```
>
> (the closing separator of the `SYNTH-TRACK 2026-05-06
> W19 CLOSING + W20 WSB (relay 048 re-fire)` block, which
> opens at L1869 with
> `SYNTH-TRACK  2026-05-06  W19 CLOSING + W20 WSB (relay 048 re-fire)`).

**Suggested header** (matches the established CMB style of
ALL-CAPS dashed headers between `=====` separator bars; cf.
the headers at L1869 and prior):

```text


================================================================
OPEN QUESTIONS FOR T1 SYNTH (W19 close)
================================================================

[OQ-2026-05-06-048R-EARLY-FIRE]
048R W19-closing artefact (bridge 6bbd3f0, 2026-05-06)
was operator-dispatched 5 days before the prompt-header
"Sunday primary" schedule (2026-05-11). All four W19
inputs (044, 045, 046, 047) had landed at fire time; the
cli_log/2026-W19.md is anchored "as of 2026-05-06"
rather than "as of 2026-05-10 close-of-week". 3 options
enumerated in
sessions/2026-05-06/048R-EARLY-FIRE-DECISION-SUBSTRATE/
decision_matrix.md (OPT_1 accept canonical; OPT_2
require 2026-05-10 brief re-fire addendum-only; OPT_3
amend 048 prompt-spec to add early-fire branch).
T1 Synth W20 weekly: select OPT_*.

================================================================
```

The leading **two blank lines** match the spacing pattern
between adjacent SYNTH-TRACK blocks elsewhere in the file
(cf. the gap between L1614 / L1620 closing 052 SYNTH-TRACK
and L1652 opening 047 SYNTH-TRACK).

---

## ID-format note

The bracketed token `[OQ-2026-05-06-048R-EARLY-FIRE]` follows
a **candidate** convention:

```text
[OQ-<YYYY-MM-DD>-<TASK_OR_REF_TOKEN>]
```

This is **not** an established CMB convention — a regex scan
for `OQ-\d` returned **zero** existing matches, so this is the
first OQ-prefixed entry. If the operator later establishes a
different Open-Question ID convention (e.g., `[OQ-001]` /
`[Q-W19-001]` / `[T1-SYNTH-Q1]`), the entry can be renamed in
place at the next CMB edit; the substrate content of the
entry (the body paragraph) is unchanged by the ID format
choice.

---

## Halt-recurrence guard

**HALT_056_CMB_MODIFIED:** PASS. As of this writeup, neither
`tex/submitted/CMB.txt` nor any other workspace file has been
modified by the 056 executer. The CMB.txt SHA-256 above
matches the 048R post-edit deposit-time state.

**Operator paste-flow recommendation** (substrate-only):

1. Open `tex/submitted/CMB.txt` at next CMB-edit session.
2. Verify SHA-256 still matches
   `74073D94F247B59CCAB42A5AA96D608F87070CDBDE20F3D06263778FCF68A5DC`
   (or note any intervening edits that have re-anchored the
   file).
3. Verify the L1900 final line still reads
   `================================================================`
   (the closing separator of the 048R SYNTH-TRACK block).
4. Paste the block above (header + entry body + trailing
   separator) after L1900.
5. After save, confirm the new entry's `[OQ-...]` token
   matches what `cmb_open_question_entry.txt` contains
   verbatim, modulo any ID-format adjustment per the
   ID-format note above.

If between this writeup and the operator-paste step a
subsequent SYNTH-TRACK or other CMB edit lands at end-of-file
(shifting L1900 to a new line number), the paste target
re-anchors to "after the new last line of the file"; the
section header + entry body are unchanged, but the operator
re-verifies the line-anchor instruction at paste time.

---

## End cmb_paste_target.md
