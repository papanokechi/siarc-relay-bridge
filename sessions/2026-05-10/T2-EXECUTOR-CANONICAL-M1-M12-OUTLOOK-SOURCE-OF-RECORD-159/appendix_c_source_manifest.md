# Appendix C source manifest -- slot 159 Phase C

**Task:** T2-EXECUTOR-CANONICAL-M1-M12-OUTLOOK-SOURCE-OF-RECORD-159
**Purpose:** map the 10 candidate M1-M12 documents into composition roles for Umbrella v2.3 Appendix C "M1-M12 Closure Narrative & Operator Runbook" (per slot 157 verdict §Q4b item 2; 4 sub-sections).
**Canonical outlook:** `M1_M12_CLOSURE_OUTLOOK_20260510_POST_OPEN_ITEMS.md` (v7) -- see `canonical_declaration.md`.

---

## §1 Appendix C sub-section -> source mapping

| Appendix C sub-section | Source role | Recommended primary | Recommended secondary | Notes |
|------------------------|-------------|---------------------|------------------------|-------|
| (i) M1-M12 closure outlook synthesis (~3-5 polished pages) | content base | v7 (`POST_OPEN_ITEMS.md`) | v6 (`POST_DISCHARGE_PLAN.md`) for axis-by-axis status; ROADMAP for phase structure | v7 carries the full M1-M12 axis scoreboard (sec 1), the slot 149 absorption record, and the M10 V0 open-axis treatment. v6 holds the discharge-plan-operationalized axis treatment that immediately precedes v7 and is useful for cross-checking which axis-status changes were absorbed in v7 vs inherited from v6. ROADMAP §1-§4 phase structure is the natural skeleton for the "synthesis" prose. |
| (ii) M10 documented-commitment paragraph (D-153-3 SAFE phrasing) | content base | v4 (`POST_LEAN_REALITY.md`) -- first to absorb M10 reality | v7 for any subsequent SAFE-phrasing refinements; v6 for discharge-plan framing | v4 is the M10-axis first-absorption snapshot ("only the M10 decision row of section 5 changes vs predecessor"). It captures the original M10 reality. v7 carries the latest state (slot 148 first-halt at `ba81582` PRECONDITION_DIRTY_TREE pending OPT_A; slot 149 7 amendments absorbed). Operator chooses whether SAFE phrasing follows v4 baseline or v7 latest depending on Umbrella v2.3 freeze policy. |
| (iii) M8b d>=3 caveat preservation block | content base | v6 (`POST_DISCHARGE_PLAN.md`) -- M8b-axis treatment | sensitivity to `D-156-1` V0+ vs V1 -- operator decides at v2.3 substrate-prep | v6 carries the discharge-plan treatment of M8b. The M8b d>=3 caveat block is sensitive to the V0+ vs V1 distinction flagged by `D-156-1` (slot 156 anomaly); operator must decide which version is in force at v2.3 substrate-prep cut time before this sub-section is finalized. |
| (iv) reproduction-checklist pointer to bridge cascade records | content base | OPERATOR_RUNBOOK | ROADMAP §4 OP_* table for cross-reference | OPERATOR_RUNBOOK provides concrete commands + acceptance criteria per OP_*. ROADMAP §4 OP_* table provides the prompt-series planning context (sequencing, dependencies). Both are companion-class artefacts; canonical outlook v7 itself is not a reproduction-checklist source. |

---

## §2 Citation block (suggested for Appendix C front-matter)

The following citation block is suggested for inclusion at the head of Appendix C (sub-section labels match the slot 157 verdict §Q4b item 2 schema):

```
Appendix C sources -- M1-M12 closure narrative + operator runbook
=================================================================

Canonical M1-M12 closure outlook source-of-record:
  M1_M12_CLOSURE_OUTLOOK_20260510_POST_OPEN_ITEMS.md  (cut 2026-05-10 ~13:10 JST)

Sub-section (i)   M1-M12 closure outlook synthesis:
  primary    M1_M12_CLOSURE_OUTLOOK_20260510_POST_OPEN_ITEMS.md
  secondary  M1_M12_CLOSURE_OUTLOOK_20260510_POST_DISCHARGE_PLAN.md
             M1_M12_CLOSURE_ROADMAP_PROMPT_SERIES_20260510.md  (phase structure)

Sub-section (ii)  M10 documented-commitment paragraph (D-153-3 SAFE phrasing):
  primary    M1_M12_CLOSURE_OUTLOOK_20260510_POST_LEAN_REALITY.md  (M10 first-absorption)
  secondary  M1_M12_CLOSURE_OUTLOOK_20260510_POST_OPEN_ITEMS.md     (latest SAFE phrasing)

Sub-section (iii) M8b d>=3 caveat preservation block:
  primary    M1_M12_CLOSURE_OUTLOOK_20260510_POST_DISCHARGE_PLAN.md  (M8b axis treatment)
  note       sensitive to D-156-1 V0+ vs V1; operator decides at v2.3 cut time

Sub-section (iv)  Reproduction-checklist pointer to bridge cascade records:
  primary    M1_M12_OPERATOR_RUNBOOK_20260510.md
  secondary  M1_M12_CLOSURE_ROADMAP_PROMPT_SERIES_20260510.md  (sec 4 OP_* table)

Provenance anchors (bridge SHAs):
  228e757  slot 158 cascade-132 amendment-overlay (predecessor)
  34563a6  slot 157 zenodo-deposit-framing-consultation
  fd669d3  cascade-132 PATH_B Option alpha decision (operative substrate)
  b9aa881  slot 136 picture-chain v1.20+ substrate-prep
```

The citation block is offered as a turnkey insertion; F6 substrate-prep may adapt it to Umbrella v2.3 LaTeX conventions.

---

## §3 Out-of-scope candidates (NOT mapped to any sub-section as primary)

The following candidates are inventoried but not recommended as primary source for any Appendix C sub-section:

- v0 (`M1_M12_CLOSURE_OUTLOOK_20260509.md`) -- baseline; superseded by v1.
- v1 (`M1_M12_CLOSURE_OUTLOOK_20260509_RULE1.md`) -- RULE 1 retriage; superseded by v2.
- v2 (`M1_M12_CLOSURE_OUTLOOK_20260510.md`) -- pre-PATH_B; superseded by v3.
- v3 (`M1_M12_CLOSURE_OUTLOOK_20260510_PATH_B_COMPLETE.md`) -- PATH_B 3/3 complete state; superseded by v4 once M10 reality landed.
- v5 (`M1_M12_CLOSURE_OUTLOOK_20260510_POST_SYNTH_REVIEW.md`) -- 6 amendments absorbed (synth review); superseded by v6.

These are PRESERVED in place per `canonical_declaration.md` §7 retirement / archive recommendations -- they may be cited as historical context if Appendix C composition needs to track the evolution of any specific axis-status entry, but no sub-section recommends them as primary or secondary.

---

## §4 Open-question flag for F6 substrate-prep

`D-156-1` (V0+ vs V1 distinction for M8b d>=3 caveat) remains an open operator decision that affects sub-section (iii). F6 substrate-prep should resolve `D-156-1` before sub-section (iii) is finalized. This is flagged for the F6 absorbing agent.

---

## §5 Closing note

This manifest is informational; it does not bind F6 substrate-prep to a specific composition order or sub-section structure. F6 may adapt as the Umbrella v2.3 Appendix C draft evolves. The canonical outlook source-of-record (v7) is binding per `canonical_declaration.md`; the manifest's primary/secondary recommendations are advisory.
