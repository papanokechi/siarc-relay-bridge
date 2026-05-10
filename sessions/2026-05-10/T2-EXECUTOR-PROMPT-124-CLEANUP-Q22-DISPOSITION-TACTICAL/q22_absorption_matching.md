# Q22 absorption matching table -- T2-EXECUTOR-PROMPT-124-CLEANUP-Q22-DISPOSITION-TACTICAL

This document is the verbatim TASK 2 matching table called for in the prompt
TACTICAL spec (formerly slot 143). Per prompt TASK 2, the matching format is:

  | Q22 sub-question | Slot 137 location | Substantive treatment? | Status |

This fire's investigation revealed that the matching extends beyond slot 137:
slot 099 is the math-arbitration source, slot 124 is the halted artefact, and
slot 137 is the implementation. The expanded matching table follows.

## Single-question expanded matching

Q22 is a single-question arbitration (path-(a) vs path-(b)), not a multi-sub-
question fire. Per prompt 124 §1, the question is: which mathematical content
goes into PCF-2 v1.4 manuscript.

| Q22 question     | Slot 099 location (arbitration source) | Slot 124 location (halted artefact) | Slot 137 location (implementation) | Substantive treatment? | Status |
|------------------|----------------------------------------|-------------------------------------|------------------------------------|------------------------|--------|
| path-(a) vs path-(b) | `q22_deposit_readiness_memo.md` (canonical Q22 verdict; HIGH confidence path-(a) recommendation; Reviewer A/D both HIGH) + `precedent_table.md` + `threshold_sufficiency_analysis.md` (HIGH-confidence justification with 23-digit numerical agreement) | `supersession_memo.md` (chain-of-evidence back to 099; RULE 1 alignment check; recurrent-pattern note UF-124-1) + `halt_log.json` `HALT_124_PRIOR_ARBITRATION_EXISTS` | `pcf2_program_statement_v14.tex` L135 + L997 + L1017 (path-(b) forward-pointed); `b_amendment_v14.diff` L45 + L155 + L175 (path-(b) forward-pointed); `zenodo_v14_description_block.md` L71 (path-(b) forward-pointed); v1.4 manuscript body integrates path-(a) per 099 recommendation | YES | absorbed via 099 -> 137 chain |

## Slot-137-only matching (per prompt spec; reconciled)

| Q22 sub-question | Slot 137 location | Substantive treatment? | Status |
|------------------|-------------------|------------------------|--------|
| path-(a) vs path-(b) | `pcf2_program_statement_v14.tex` (path-(a) content integrated; path-(b) forward-pointed at L135 + L997 + L1017); `b_amendment_v14.diff` (path-(b) forward-pointed at L45 + L155 + L175) | YES | absorbed (math-content level; manuscript body now reflects path-(a) recommendation, with path-(b) preserved as forward-pointed numerical-escalation stretch goal) |

## Verdict on outcome classification

**Outcome A (REFINED)** per prompt TACTICAL §2 TASK 2:

  ALL Q22 sub-questions absorbed by slot 137 (math-content level), but
  the math-arbitration that drove slot 137 came from slot 099 (2026-05-07),
  NOT from slot 124. Slot 124 is the halted-and-superseded artefact.

The prompt's outcome-classification semantics (A: rename to `_ABSORBED_BY_137.txt`)
need refinement: slot 124 itself was NOT absorbed by 137 -- it was halted on
2026-05-09 with `HALT_124_PRIOR_ARBITRATION_EXISTS`. The rename target is
therefore `_HALTED_SUPERSEDED_BY_099.txt`, which more accurately reflects the
actual artefact state.

Net effect on Q22 disposition: identical to outcome A (Q22 fully resolved at
math-content level; no further arbitration required). Net effect on prompt 124
artefact: halted-and-superseded-rather-than-absorbed naming.

## Cross-references (verbatim from disposition note sec 4)

- Slot 139 verdict A-139-1 LOW (the trigger; bridge `72bb2c2`)
- Slot 099 (Q22 arbitration source; bridge folder
  `T1-Q22-DEPOSIT-READINESS-MEMO-099/`)
- Slot 124 (halted; bridge folder
  `T1-SYNTH-M2-Q22-MATH-ARBITRATION-124-HALT-SUPERSEDED-BY-099/`)
- Slot 137 (path-(a) implementation; bridge `45e236c`)
- Cascade-132 sec 5 (RULE 1 governance reference; bridge `fd669d3`)
