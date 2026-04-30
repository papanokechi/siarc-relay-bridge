# Handoff — SIARC-COHERENCE-AUDIT
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~50 minutes
**Status:** COMPLETE (audit done; 3 T1 mismatches surfaced as relay patch prompts; no submitted paper auto-edited per HALT clause)

## What was accomplished
Cross-paper coherence audit (P-10) over the 7 SIARC papers
(UMB, #14, T2A, T2B, P06, P08, P11). Extracted all
Conjecture/Theorem/Lemma/Proposition/Corollary/Observation/Definition/
Problem environments from each `.tex` source, ran a 30-probe regex
matrix for degree conventions, ratios, tier labels, DOIs, and
companion-paper venue strings, and built a coherence matrix +
mismatch list. 10 mismatches identified and triaged: 3 × T1, 5 × T2,
2 × T3. T1 mismatches were converted into stand-alone relay patch
prompts; no submitted paper was edited.

## Key numerical findings
- **Tier-1 mismatch counts:** UMB↔T2B (Class B omission), UMB↔#14 (T0..T3
  label collision under different semantics), P06↔P11 (degree (2,2) vs
  (2,1) regression at one paragraph in P06).
- Probe matrix (`probe_matrix.json`): `(2,2)` degree-profile token
  count = 1 in P06, 0 in every other audited paper.
- `Class A` / `Class B` token counts: 13 / 32 in T2B; 0 in UMB.
- `Tier T0..T3` token counts: UMB 8/6/9/8; #14 20/12/11/8; all other
  audited papers 0.
- Self-DOI 10.5281/zenodo.19885549 (UMB concept) is referenced 0 times
  inside UMB; only the version DOI 10.5281/zenodo.19885550 appears.
- T2A bibliography line 628: cites P11 as "Mathematics of Computation
  submission 260422-Papanokechi" — stale; current venue is JTNB-2400.
  (P11 source: `f1_mathcomp_submission/main_R1.tex` sha12=37a36a4a1684,
  T2A source: `t2a_paper_draft.tex` sha12=6d07e458ab12.)

## Judgment calls made
1. **#14 → `paper4_takeuchi_outline.tex`** rather than
   `paper14-ratio-universality-SUBMISSION.tex`. Justification: UMB's
   `\bibitem{Paper14}` is "Four-tier classification of PSL₂(ℤ)-uniformized
   PCFs", which is the takeuchi outline (cf. P11 references.bib
   `@article{spectral}`). The other file (Ratio Universality) is CMB
   row P13 (Acta Arith) on partition functions, unrelated to the
   PCF programme. Filename collision logged as MM-08.
2. **P06 source** taken as the IJNT-submission tree
   (`tex/submitted/p06_desert_ijnt_submission/pcf_desert_negative_result.tex`),
   not the duplicate `tex/submitted/pcf_desert_negative_result.tex`
   nor the bridge copies under `siarc-relay-bridge/sessions/2026-04-30/P06-DESERT-REVISION/`.
3. **HALT compliance.** Three T1 mismatches were found. Per the relay
   prompt, no submitted .tex was edited; instead three patch_relay_*.md
   prompts were produced as standalone deliverables.

## Anomalies and open questions
- **T2 vs trans-stratum membership of T2B Class B.** UMB's T2 definition
  (μ-asymptotic) is stated for sequence-indexed PCF families. T2B's
  Class B has limits in ℚ·π⁻¹ (single irrationals, not measure-asymptotic
  data). It is not 100% formally proven that Class B falls under UMB's
  T2 definition rather than UMB's T1. This bears on MM-03's framing —
  the patch prompt is conservative and only adds the Class B clause
  without claiming μ-asymptotic membership.
- **paper4_takeuchi_outline.tex** has NO formal `\begin{theorem}` or
  `\begin{conjecture}` environments; only `definition` and `remark`.
  Its T0..T3 are introduced narratively in §1. If #14 is to be cited
  as the source of a formal "Four-Tier Classification Theorem", the
  paper should be re-structured to expose the theorem statement.
- **MM-03 escalation.** Whether UMB Conjecture 2.1 was always intended
  to apply only to Class A (the CMB and earlier session memory both
  suggest the Class B picture is recent — see /memories/repo/umb-classb-saturation-2026-04-30.md
  — and that UMB v1 may pre-date the Class B characterisation) is a
  judgement Claude should make. The patch prompt presents the change
  as additive and reversible.

## What would have been asked (if bidirectional)
- Should the UMB v2 patch (MM-03) be released immediately, or held
  until T2B is itself accepted at a venue (currently Monatshefte short
  pending)?
- For MM-02, is renaming #14's tiers to O0..O3 acceptable, or should
  UMB's tiers be renamed instead (smaller blast radius vs higher
  importance of UMB nomenclature stability)?
- Is the partition-functions paper14 file expected to be renamed to
  paper13- to match CMB indexing (resolving MM-08)?

## Recommended next step
Execute `patch_relay_MM03.md` first (UMB Conjecture 2.1 ⊃ Class B).
This is the highest-leverage T1 mismatch: it is the umbrella
conjecture and is the most exposed to external review. MM-02 and
MM-01 can be batched in a follow-up relay.

## Files committed
- `claims.json` (37,351 bytes) — extracted environments per paper
- `claims.jsonl` (5 AEAL entries)
- `coherence_matrix.md` — paper × concept matrix + bidirectional cite graph + OP table
- `discrepancy_log.json` — empty per standing format
- `extract_claims.py` — environment extractor
- `extracted_claims.md` — flat dump of all extracted claims
- `halt_log.json` — three Tier-1 mismatches recorded; no auto-edit performed
- `mismatches_list.md` — 10 mismatches with paper_A, paper_B, claim, suggested fix
- `patch_relay_MM01.md` — P06 (2,2)→(2,1) regression patch
- `patch_relay_MM02.md` — UMB / #14 tier-label disambiguation
- `patch_relay_MM03.md` — UMB Conjecture 2.1 Class B addition
- `priority_ranking.md` — T1 / T2 / T3 ranked list of all 10
- `probe_matrix.json`, `probe_matrix.md`, `probe_matrix.py` — 30 regex × 9 file matrix
- `unexpected_finds.json` — empty per standing format
- `handoff.md` — this file

## AEAL claim count
5 entries written to `claims.jsonl` this session
