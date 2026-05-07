# Handoff — T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073
**Date:** 2026-05-07
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~ 90 minutes (single continuous run with one
mid-session token-budget summarisation)
**Status:** COMPLETE
**Verdict:** CLEAN_EXTRACT

## What was accomplished

Verbatim T3-mechanical readthrough of Birkhoff-Trjitzinsky 1933
§§4-6 (Acta Math. 60, 1933, "Analytic theory of singular difference
equations"). Produced 15 deliverables + AEAL quartet covering: (a) the
verbatim §§4-6 transcripts with [p.NN] page anchors; (b) per-section
claim tables totalling 53 [CLAIM-B∗] tags and 1
[CHART-MAP-CANDIDATE-B1] surfacing; (c) main-theorems index over T1=§4
Lemma 8, T2=§5 Theorem I, T2.cor=m=1 corollary, T3=§6 Lemma 9; (d)
internal cross-reference table (24 §§4-6→§§1-3 deps + 4 internal §4→§5
cites + 12 BT 1930 (I)/(II) cites); (e) updated Adams×BT ladder map
v2 with §-level BT granularity that resolves all 6/9 of 072 v1's
DEFER markers; (f) extended sectorial-upgrade-gap status report v2;
(g) D2-NOTE v2.1 §4.5 BT-citation audit (3/3 EXACT page-anchor matches
+ 3/3 form-of-equation/object substrate-inventory agreement); (h)
consolidated I.1-I.7 + I.8 self-check scans (PASS 7/7).

## Key numerical findings

- BT 1933 PDF SHA-256 = `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`; verified against bridge SHA256SUMS slot 03; verified `_073_extract_bt1933.py` page count 89/89 (100% extraction; 0 empty pages).
- Predecessor session 072 bridge HEAD = `5b297cb` (pinned; 073 builds on this state).
- §§4-6 verbatim claim count = 53 [CLAIM-B∗] tags (§4: 19 / §5: 18 / §6: 16).
- Main-theorems = 3 explicitly labelled (T1 Lemma 8 p.30, T2 Theorem I p.41, T3 Lemma 9 p.48) + 1 sub-corollary (T2.cor m=1 case).
- Adams T1-T9 ↔ BT §§4-6 ladder distribution v2 (post-073) = 1 ABSORBED-VERBATIM, **6 EXTENDED**, 1 SUPERSEDED, 1 PARALLEL (T6 promoted PARALLEL→EXTENDED on the strength of BT §5 (13 a) [CHART-MAP-CANDIDATE-B1] substrate; only label change vs 072 v1).
- All 6 of 9 072 v1 DEFER markers RESOLVED at §-level BT granularity in `adams_bt_ladder_map_v2_with_bt_4_6.md`. **072 D4 RESOLVED** for §§4-6 content.
- D2-NOTE v2.1 §4.5 BT-citation audit = 3/3 EXACT page-anchor matches (p.30 Lemma 8 / p.41 Theorem I / p.48 Lemma 9) + 3/3 form-of-equation/object substrate-inventory agreement.
- [CHART-MAP-CANDIDATE-B1] = 1 sentence at BT §5 p.47 eq. (13 a) (across-strip periodic-functions expansion); surfaced WITH explicit "NOT R1 closure / NOT chart-map-discharge claim" caveat per Phase C.4 spec.
- I.1-I.7 self-check aggregate = **PASS 7/7**; all forbidden-verb token matches are inside policy-exempt recital lines.
- AEAL claim count C1-C12 = 12 entries deposited in `claims.jsonl`.

## Judgment calls made

- **§6 "Faetorization" font-drift (D2 in discrepancy log):** kept the
  pypdf-delivered glyph drift in the verbatim §6 extract rather than
  silently correcting (verbatim policy preserved); documented in
  discrepancy_log.json. This contrasts with the §-symbol → "w" drift
  (D1) which was silently restored in section-headers because the
  context is unambiguous and the substitution is uniform.
- **T6 PARALLEL → EXTENDED reclassification:** 072 v1's PARALLEL
  label was based on the absence of a separately-titled "§ Periodic
  functions" header in BT 1933. The verbatim 073 readthrough surfaces
  the same periodic-functions object inside the BT §5 Theorem I
  proof at p. 47 (13 a). Reclassified to EXTENDED with explicit
  SUBSTRATE-INVENTORY framing; **NOT** asserted as a chart-map-discharge
  or R1-closure claim. This is the only ladder-label change vs 072 v1.
- **§§7-9 verbatim DEFER:** the 072 v1 quick-scan touched §§7-9 page
  anchors only; the 073 verbatim readthrough is scoped to §§4-6 per
  the relay prompt. §§7-9 verbatim extraction is recorded as residual
  item §5(5) of `sectorial_upgrade_gap_status_v2_with_bt_4_6.md` for
  a future session.
- **D8 main-theorems index format:** chose to provide both a
  paraphrase row (for content fidelity, where the verbatim opener
  alone exceeds 30 words) AND a separate ≤ 30-word verbatim opening
  clause table (for direct citation use), to satisfy both the
  fidelity-of-content and the ≤ 30-word per-quote ceiling.

## Anomalies and open questions

- **U1 [CHART-MAP-CANDIDATE-B1]** at BT §5 p.47 (13 a) — the
  across-strip periodic-functions expansion is a substrate-inventory
  candidate for chart-map analysis at W21 LANE-1 Phase 3 arbitration.
  **For synthesizer review:** is the (13 a) periodic-functions
  structure (combined with the i, j-indexed `p^{r, r+1}_{i j}` matrix
  at (10) p.46) the substrate that the synthesizer expects to chart-
  map onto Adams's P(x) = H^{-1}(x) G(x) construction (Adams 1928 §3
  p.517)? If so, this gives the BT-side §-level granularity for an
  Adams-T6-style chart-map analysis. The 073 deliverables do **not**
  make any closure claim; the synthesizer arbitrates.
- **D2 (§6 "Faetorization" drift)** is a curiosity for any future
  session that re-extracts BT §6 with a different PDF tool — the
  drift may or may not appear there. Recorded for reproducibility
  audit.
- **D2-NOTE v2.1 §4.5 wording check:** v2.1 says "the formal series
  of the recurrence solutions and the formal series of the ODE
  solution f at z = 0 are mutually computable by formal Borel-Laplace
  transforms in the duality variable" (PDF p.7). This is v2.1's own
  framing of the BT 1933 → ODE-side bridge; whether the bridge is
  formally valid is a synthesizer question (out-of-scope for 073).
  Surface for synthesizer review.
- **072 v1's "Class-2a / Class-2b" sub-classification absence in
  BT 1933:** Adams 1928 §2 makes an explicit Class-2a/Class-2b sub-
  classification (cf. 072 ladder T5). BT 1933 §§4-6 carries a unified
  "completely proper" notion (Def. 6 of §1) that subsumes both, but
  does **not** explicitly mirror the Class-2a/Class-2b boundary.
  This is a substrate-coverage observation, not a problem; recorded
  for synthesizer awareness.
- **069r1 OQ-W21-LITERATURE-ALTERNATIVE remains OPEN:** the §§4-6
  verbatim layer does not by itself answer this open question. Per
  HALT_073_LADDER_OVERREACH, no inference from §§4-6 substrate to
  069r1 closure is made.

## What would have been asked (if bidirectional)

- Should the §§7-9 verbatim readthrough (the natural follow-up
  recorded as residual §5(5)) be queued as a 074 relay, or held
  pending synthesizer review of the 073 ladder-map v2 first?
- Is the 072 D4 RESOLVED status (6 of 9 DEFER → §-level resolution)
  the resolution scope the synthesizer expected, or did the
  synthesizer expect a §-level resolution that also covers the §§7-9
  carry-over (T1 + T2 + T9 reach into §§7-9 in the 073 ladder map)?
- For the [CHART-MAP-CANDIDATE-B1] at (13 a): is the candidate
  best-positioned as a U1 entry only, or should it be promoted to a
  named CHART-MAP-CANDIDATE in a separate registry the synthesizer
  consumes?
- D2-NOTE v2.1's §4.5 calls the §4 + §5 + §6 trio "the
  Borel-summability content"; the 073 audit verifies the page anchors
  are exact but does not verify the "Borel-summability" framing
  itself. Should a future relay add a verbatim BT 1933 § that
  explicitly characterises the analytic-existence theory as
  Borel-summability (most plausibly via Costin 2008 ch.5 cross-walk),
  or is the substrate-inventory agreement at (13 a) sufficient for
  the synthesizer's purposes?

## Recommended next step

**Queue a 074 relay for verbatim BT 1933 §§7-9 readthrough** parallel
to the 072 (Adams) and 073 (BT §§4-6) sessions. §7 contains
Theorem II (Acta p.51); §9 contains the Fundamental Existence
Theorem (Acta p.69). Both are downstream consumers of the §§4-6 main
theorems + BT 1930 (I)/(II) results. Completing §§7-9 would close the
BT-side §-level granularity for Adams T1, T2, T9 (which reach into
§§7-9 in the 073 ladder map) and supply the verbatim text the
W21 LANE-1 Phase 3 arbitration substrate would consume for the
"Fundamental Existence Theorem" framing of the formal-to-analytic
sectorial-upgrade question.

## Files committed

| # | File | SHA-256 (first 16 hex) |
| --- | --- | --- |
| 1 | `bt_1933_section_index_4_6.md` | `ddf5296c950d577b…` |
| 2 | `bt_1933_section_4_extract.md` | `b3abede24ff368d0…` |
| 3 | `bt_1933_section_4_claim_table.md` | `2c14404dd9ee0ca0…` |
| 4 | `bt_1933_section_5_extract.md` | `ec2c0d5a2dadef3b…` |
| 5 | `bt_1933_section_5_claim_table.md` | `00103c17ff3b7a99…` |
| 6 | `bt_1933_section_6_extract.md` | `744a197dec758e0d…` |
| 7 | `bt_1933_section_6_claim_table.md` | `64bd696b3108403c…` |
| 8 | `bt_1933_sections_4_6_main_theorems.md` | `eddfe12431a9b29f…` |
| 9 | `bt_1933_sections_4_6_internal_xref.md` | `f170e30b3886a8ef…` |
| 10 | `adams_bt_ladder_map_v2_with_bt_4_6.md` | `dc3b048c39aca27a…` |
| 11 | `sectorial_upgrade_gap_status_v2_with_bt_4_6.md` | `d6bc0b7f72f27a9a…` |
| 12 | `d2_note_v21_bt_citation_audit.md` | `7cf2279aa15df44f…` |
| 13 | `forbidden_verb_scan.md` | `b4a1b8400bbbc203…` |
| 14 | `substrate_anchor_shas.md` | (post-write SHA at commit time) |
| 15 | `handoff.md` | (this file) |
| Q1 | `claims.jsonl` (12 entries C1-C12) | (post-write SHA at commit time) |
| Q2 | `halt_log.json` (empty {}) | (post-write SHA at commit time) |
| Q3 | `discrepancy_log.json` (D1 pypdf glyph drift, D2 §6 "Faetorization") | (post-write SHA at commit time) |
| Q4 | `unexpected_finds.json` (U1 [CHART-MAP-CANDIDATE-B1]) | (post-write SHA at commit time) |
| W1 | `bt_1933_pypdf_text.txt` (working pypdf raw output, 89 pages, 141 283 B) | `0bf983cbd5109fb1…` |
| W2 | `_d2_note_v21_text.txt` (working pypdf raw output of v2.1 PDF, 31 952 B) | `0a45847117646216…` |
| W3 | `_073_extract_bt1933.py` (extraction script, kept for reproducibility) | (post-write SHA at commit time) |

Total bridged: **15 deliverables** (D1-D15) + **4 AEAL artefacts**
(Q1-Q4) + **3 working artefacts** (W1-W3). Listed under
"Files committed" because they are all included in the 073 bridge
commit.

## AEAL claim count

**12 entries** written to `claims.jsonl` this session (C1-C12); see
the full enumeration in `claims.jsonl`.
