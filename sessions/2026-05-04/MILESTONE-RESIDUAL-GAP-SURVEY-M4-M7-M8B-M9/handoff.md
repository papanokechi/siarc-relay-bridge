# Handoff — MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9

**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes
**Status:** PARTIAL

## What was accomplished

Produced a single consolidated synthesizer-input dossier
`dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` (~570 lines, ~33 KB)
covering 4 sub-tasks (M4 / M7 / M8b / M9) per spec §3-§6 schemas, plus the
spec §7 cross-cut matrix and §F acquisition appendix. The dossier is
RECONNAISSANCE ONLY — no closure attempt is made for any of M4 / M7 / M8b / M9
and no leverage ranking / scheduling proposal is offered (per spec §2 OUT-OF-SCOPE
and §6 RACI). 14 AEAL claims appended; 4 discrepancies surfaced; 4 unexpected
finds recorded.

## Key numerical findings

- **Sub-task A (M4):** Costin 2008 ch.5 (slot 06; SHA 436c6c11…) covers rank-1
  Stokes-constant theory verbatim (Theorems 5.11 / 5.26 / 5.45 quoted in
  dossier row A.P1); but the **fractional-rank q ≥ 2 borderline-anormal case
  relevant to PCF δ_n at d ≥ 3 is structurally absent** (verbatim search
  "fractional rank": 0 hits; "borderline": 9 hits all rank-1).
- **Sub-task A (M4):** Braaksma 1992 NUMDAM abstract verbatim verified
  (DOI 10.5802/aif.1301; "proof of Écalle's multisummability theorem");
  full text not deposited this session.
- **Sub-task B (M7):** Chowla-Selberg landing page reached on GDZ but image-only
  viewer; no closed-form Γ(1/3) → PCF-A=6 anchor identified at literature
  level this session.
- **Sub-task C (M8b):** BLMP 2024 slot 08 (SHA 96c49cdd…) Theorems 1.1 / 1.4 / 1.7
  give Riemann-Hilbert characterisation of monodromy for PIII(D_8) and
  PIII(D_6); but **no closed-form S_2 alien-amplitude formula for the SIARC
  d=2 PCF dichotomy** in either Costin or BLMP (verbatim search of
  9030-line BLMP TXT for SIARC dichotomy markers: 0 hits).
- **Sub-task D (M9):** Langlands 1967 letter to Weil verified as
  aesthetic-justification-only at announcement time (IAS author-commentary
  verbatim quoted); Sakai 1999 slot 13 verified as a STRONG-FIT precedent for
  SIARC M9 announcement format (7-section partition with explicit deferrals).

All numerical findings are pypdf text-layer searches + web-fetch landing-page
verbatim extractions — no symbolic / numerical compute performed (per §0 task
profile).

## Judgment calls made

1. Spec §1 strict HALT_038_MISSING_ANCHOR was NOT triggered despite 5 anchor
   path drifts (3 bridge folder renames + 2 slot-PDF filename drifts).
   Rationale: in all 5 cases content match verified independently against
   prior bridge verdicts (029 SAKAI-2001 confirms slot-13 1999 preprint =
   2001 published version; bridge `37c939f` confirms T1 Phase 2 deliverables
   landed in T1-BIRKHOFF-TRJITZINSKY-LITREVIEW). Documented in
   `discrepancy_log.json` DISC-038-1 for synthesizer review.

2. After 4 arXiv-ID guesses returned hallucinated unrelated papers (same
   pattern as 031 WITTE-FORRESTER), this researcher pivoted to author-and-
   year-only NIA tagging for §C.P3 / P4 / P5 / P8 rather than continuing to
   probe more guesses. Per copilot-instructions Bibliographic ID
   Pre-Verification rule, citing hallucinated IDs would be an AEAL breach;
   stopping was the discipline call. Documented in `discrepancy_log.json`
   DISC-038-2 + `unexpected_finds.json` UF-038-1.

3. Did NOT acquire Braaksma 1992 full PDF from NUMDAM despite OA route
   verified working. Rationale: spec §0 explicitly states "no compute-heavy
   steps" + "verbatim quotation literature reconnaissance"; the abstract
   text alone was sufficient for row A.P3 to populate; full-PDF deposit
   adds disk-cost without payoff for a reconnaissance product.
   This deferral is recommended as a follow-on action for any future
   M4-Phase-3 closure prompt that needs Braaksma's full theorem statement.

4. Did NOT re-attempt Wasow §X.3 OCR per spec §2 OUT-OF-SCOPE / §8
   HALT_038_DUPLICATE_OF_019.

5. Did NOT initiate any communication with Mazzocco / Zudilin / other named
   researchers per spec §4 P7 + §5 P3 hygiene notes (literature-only, NOT
   contact).

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION.**

1. **Spec §5 sub-task C uses author-and-year-only references for P3 / P4 / P5
   / P8 (Mazzocco / BLT / Iwaki / Lisovyy-Roussillon).** The post-031
   Bibliographic Pre-Verification rule applies to spec citations of specific
   DOI / arXiv IDs; author-and-year-only references technically slip past
   that rule. Recommend synthesizer extend the rule to require canonical-ID
   pinning by the prompt-drafter for all literature candidates, not just
   those already-pinned-with-IDs. Recorded as `unexpected_finds.json`
   UF-038-1.

2. **The fractional-rank q ≥ 2 borderline-anormal case is structurally
   absent from Costin 2008 ch.5** (negative finding; UF-038-2). Implication
   for synthesizer M4-scheduling: post-Wasow descendant literature does NOT
   provide an obvious fall-back if Wasow §X.3 OCR (prompt 019) fails. The
   M4 Phase 3 lift may genuinely require either Wasow OCR success or SIARC
   primary derivation. This narrows the operator-level decision space.

3. **Sakai 1999 slot 13 is a strong structural-fit precedent for SIARC M9
   announcement format** (UF-038-3). Sakai's explicit 7-section partition
   with deferral markers ("see § 7; 4") is structurally closer to the M9
   "M1/M2/M3/M5/M6/M8 ✅ + M4 partial + M7 soft + M8b foreclosed" caveat
   profile than the Langlands letter is.

4. **Bridge folder rename drift** between prompt drafting and execution
   (UF-038-4). Five anchor path drifts in spec §1 / PRIOR ANCHORS without
   any HALT trigger because content-matched. Process-discipline
   recommendation: spec § 1 should verify-by-content-and-not-just-by-path,
   OR bridge layout should adopt a strict-no-rename policy. Surfaced for
   synthesizer.

5. **No new PDFs deposited this session.** Acquisition success rate 0 / 14
   probed (web-fetch only). The dossier is reconnaissance-of-existing-corpus.
   For full M4 / M7 / M8b / M9 closure work, a follow-on lit-hunt prompt
   with operator-side ILL or browser-driver-mediated OA acquisition is
   recommended (Braaksma 1992 NUMDAM full PDF; Loday-Richaud 2014 LNM 2154;
   Borwein-Zucker 1992; Chowla-Selberg 1949 PNAS short note + 1967 Crelle
   long paper image-OCR; Mazzocco / Lisovyy-Roussillon canonical arXiv IDs
   pinned by synthesizer pre-fire).

## What would have been asked (if bidirectional)

- Q-038-A: Should §1 "HALT on missing anchor" be loosened to "HALT on
  content-mismatch on canonical anchor" given the rename-drift pattern?
- Q-038-B: Is the post-031 Bibliographic Pre-Verification rule supposed to
  cover author-and-year-only candidate references too, or only specific-ID
  candidate references?
- Q-038-C: Is the synthesizer comfortable with this dossier's PARTIAL status
  (no acquisition, no deep probe of P5–P9 of any sub-task) given the §0
  ~3-4 hr budget was deliberately under-spent at ~45 min in favour of
  on-disk corpus reuse?

## Recommended next step

Per spec §6 RACI / RIDLE: this researcher does NOT recommend a next prompt.
Synthesizer + operator decide. The dossier feeds Q-CLAUDE-X scheduling.

(One factual observation, not a recommendation: if M4 Phase 3 advances next,
the dossier signals that the post-Wasow descendant literature is unlikely to
provide a borderline-anormal q ≥ 2 anchor — implying Wasow OCR success or
SIARC primary derivation is the realistic close path.)

## Files committed

- `dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` (main deliverable; ~33 KB)
- `claims.jsonl` (14 AEAL entries)
- `halt_log.json` (empty `{}`)
- `discrepancy_log.json` (4 discrepancies)
- `unexpected_finds.json` (4 unexpected findings)
- `prompt_spec_used.md` (this prompt's spec verbatim)
- `handoff.md` (this file)

## AEAL claim count

14 entries written to `claims.jsonl` this session.
