# MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9 — pre-fire SPEC

**Status:** DRAFT-PENDING-OPERATOR-FIRE-AUTHORIZATION (synthesizer-Claude Q38.1–Q38.6 arbitration ABSORBED 2026-05-04 ~22:10 JST)
**Composed:** 2026-05-04 ~19:35 JST
**Deposited:** 2026-05-04 ~21:15 JST (initial)
**Re-staged (post-Q38-amendment):** 2026-05-04 ~22:10 JST
**Workspace path:** `tex/submitted/control center/prompt/038_milestone_residual_gap_survey_m4_m7_m8b_m9.txt`
**Bridge path:** `sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9-SPEC/prompt_spec.txt`
**Size:** 34,522 B (post-amendment)
**SHA256:** `E58F1BC2D81B67385573BC882829E9CFB1FA4D8C449404E5F0D9DF628ACE7A4A`
**Pre-amendment SHA256 (for audit):** `24F658806C673AD12C8F6F80D54B6C02CBAAF2495DA5172BE083540D91557E6A` (29,405 B initial)

## Q38 arbitration absorbed (2026-05-04 ~21:40 JST synthesizer-Claude pass)

| ID | Outcome | Spec patch |
| --- | --- | --- |
| Q38.1 | ALL parallel ~3-4 hr (high conf, default confirmed) | None |
| Q38.2 | KEEP M9 with §6 CONTEXT M6-INDEX-2-final starting context (medium conf) | YES — §6 CONTEXT |
| Q38.3 | Default §2 + §8 coverage (low conf, no spec read) | None |
| Q38.4 | Slot 038 (high conf, default confirmed) | None |
| Q38.5 | ~3-4 hr full (high conf) | None |
| Q38.6 | EXTENDED forbidden-verb list 4 families (medium-high conf) | YES — §9 |

Full arbitration audit: `sessions/2026-05-04/SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-ABSORB/`

## Purpose

Researcher-prompt spec for a 4-sub-task literature reconnaissance dossier
covering residual gaps around milestones **M4 / M7 / M8b / M9**. Pure
lit-recon, no compute. Output: single dossier deposited to
`sessions/<DATE>/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/` with
§A–§G structure + standard B1–B5 artefacts. Does **not** duplicate
prompt 019 (Wasow §X.3 OCR), prompt 033 (M6 W-homomorphism primary
derivation), or prompt 037 (endorser templates).

## Pre-fire QA gate (synthesizer arbitration required)

| ID | Question | Default in draft |
| --- | --- | --- |
| Q38.1 | Sub-task scope: 4 parallel vs sequential triage by leverage | ALL parallel, single ~3-4 hr session |
| Q38.2 | M9 sub-task scope: keep / narrow to 1-page / drop entirely | Keep as drafted (8 precedents) |
| Q38.3 | M8b foreclosure-guard adequacy — extra forbidden-list of numerical-revival paths? | Current §2 OUT-OF-SCOPE + §8 HALT_038_OUT_OF_SCOPE_NUMERICAL_REVIVAL covers it |
| Q38.4 | Slot assignment — 038 (next free) vs thematic re-slot | 038 |
| Q38.5 | Compute budget — ~3-4 hr full vs shrunken if §6 dropped | ~3-4 hr |
| Q38.6 | Forbidden-verb list completeness | shows / proves / confirms / establishes / demonstrates that / implies that / follows that |

## Sub-task summary

| § | Sub-task | Milestone state | Candidate sources |
| --- | --- | --- | --- |
| §3 A | Post-Wasow §X.3 borderline-ansatz lit | M4 PARTIAL 2026-05-04 (T1 Phase 2 UPGRADE_PARTIAL_FORMAL_LEVEL); A∈[d,2d] needs lift to A=2d at d≥3 | Costin 2008 ch.4-6, Loday-Richaud 2014, Braaksma 1992, Immink, Ramis-Sibuya 1996, Sauzin 2015, Balser 2000, Sternin-Shatalov, Ecalle |
| §4 B | Chowla-Selberg / Γ(1/3) hard-branch at j=0 | M7 ✅ soft-branch (014); 🛑 hard-branch HALTED 006 AMBIGUOUS_AT_DPS8000 (5-param ansatz cap ~7 digits vs 30-digit threshold) | Chowla-Selberg 1949, Borwein-Zucker 1992, BBB 1989, Aldea-Ohno, Yamamoto, Zudilin (lit only — no contact), Glaisher/Watson, Borwein-Crandall |
| §5 C | Post-foreclosure structural Stokes-multiplier S_2 lit | M8b 🛑 NUMERICALLY foreclosed (017d permanent block + 017m HALT_T37M_PADE_DIVERGENT); structurally well-defined | Costin 2008 ch.5, Loday-Richaud II, Mazzocco (lit only — no contact), Bonelli-Lisovyy-Tanzini, Iwaki-Saenz, Iwaki resurgent series, Lisovyy-Roussillon, JMU 1981+descendants |
| §6 D | Announcement-protocol meta-precedent | M9 gating now {M4-partial only} after R5 NUMDAM retry → M6 ✅ | Langlands 1967 letter, BSD 1965, Iwasawa 1969, Painlevé 1900 / Gambier 1910, Sakai 2001, Conte-Musette, Wiles 1995 |

## Discipline guards built in

- `HALT_038_AEAL_LANGUAGE_BREACH` — forbidden verbs outside verbatim-quotation context
- `HALT_038_OUT_OF_SCOPE_NUMERICAL_REVIVAL` — anti-S_2-numerical-revival
- `HALT_038_DUPLICATE_OF_019` — anti-Wasow-OCR-collision
- `HALT_038_DUPLICATE_OF_033` — anti-M6-primary-derivation-collision
- `HALT_038_MISSING_ANCHOR` — pre-fire file-existence check
- AEAL three-channel regimen: (a) verbatim quote with DOI/page/theorem# ; (b) NIA-tag with explicit failure mode ; (c) zero-occurrence-count for negative findings

## Operator note

Synthesizer can answer Q38.1–Q38.6 in one pass. Once arbitrated +
operator authorizes, prompt fires (researcher session ~3-4 hr).
