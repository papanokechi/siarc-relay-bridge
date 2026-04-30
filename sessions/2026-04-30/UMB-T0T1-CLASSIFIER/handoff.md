# Handoff — UMB-T0T1-CLASSIFIER
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE (HALT criterion satisfied)

## What was accomplished
Executed P-07 in full: built a 500-family labeled dataset (300 T0 from F(2,4) Rat stratum + 24 F(2,4) Trans + 176 sampled from the 482-irrationals quadratic GCF catalog), engineered 13 features per relay spec (degree pair, R_struct, indicial discriminant flags, BT spectral, Stokes index proxy, conv_slope), trained interpretable DecisionTree(max_depth=6) and GradientBoosting classifiers, and extracted leaf rules in plain text. Holdout (100 stratified families) accuracy = 1.0000 for both models; HALT criterion (>97%) triggered. Companion F(2,4)-only stratified analysis (324 families, 5-fold CV) also achieves 1.0000 +/- 0.0000.

## Key numerical findings
- **DecisionTree(depth=6) holdout accuracy = 1.0000** (60/60 T0, 40/40 T1); AUC = 1.0000 — train_classifier.py, dps=60.
- **GradientBoosting(300, depth=4, lr=0.05) holdout accuracy = 1.0000**; AUC = 1.0000.
- **Tree extracts only 3 leaves**, using only 2 of 13 features (disc_a_psq + conv_slope):
  - **R0**: `disc_a_psq <= 0.5` → T1 (n=176, purity 1.000).
  - **R1**: `disc_a_psq > 0.5 AND conv_slope <= 0.15` → T0 (n=240, purity 1.000).
  - **R2**: `disc_a_psq > 0.5 AND conv_slope > 0.15` → T1 (n=24, purity 1.000).
- **F(2,4)-only restricted (deg_pair held constant)**: 5-fold CV mean acc = 1.0000 ± 0.0000; pooled CV confusion [[300,0],[0,24]]; full-fit DT collapses to single split `conv_slope <= 0.1495 → T0`.
- F(2,4) re-enumeration found **58,464 Rat families** vs cert's 113,270 (see discrepancy_log.json).

## Judgment calls made
1. **Sampling strategy.** The 482-irrationals catalog has unit numerators (deg_a=0), structurally distinct from F(2,4). I encoded both shapes in a unified record schema with deg_a/deg_b as features, padding when the deg-2 indicial features were not applicable (returning 0 sentinels). This enabled training over the heterogeneous corpus, but it also meant the most powerful early split (`disc_a_psq=0`) effectively becomes a "from-irr-482" shape detector. I therefore added a **second F(2,4)-only stratified analysis** to surface the genuine internal T0/T1 effective rule. Both analyses are shipped.
2. **conv_slope window.** Computed at dps=60, N=200 backward recurrence, fitting log10|K_n − K_{n−1}| over n ∈ [50, 180]. This window proved too late: by n=200 even genuinely-T1 sequences fall below the 10^-55 numerical floor, so finite_termination=1 collapsed to all-rows. The classifier still works because the window was occasionally early enough on the 24 F24-Trans, but the feature is degraded. See unexpected_finds.json.
3. **HALT response.** Per the prompt's halt directive ("Tree accuracy >97% on held-out → proceed to formal verification of the top 3 rules"), I wrote halt_log.json with halt_triggered=true and tagged the 3 leaf rules as Lemma candidates in rules_extracted.md. I did NOT begin formal verification (Lean 4) in this session — that is the next relay.
4. **No graphviz binary on PATH.** Rendered tree.svg via matplotlib's plot_tree fallback; tree.dot is also retained for re-rendering with Graphviz if desired.

## Anomalies and open questions
**THE THREE EXTRACTED RULES ARE PROBABLY KNOWN-THEOREM RESTATEMENTS, NOT NEW LEMMAS.** Claude must read this section before celebrating.

- **Rule R0 (disc_a_psq=0 ⇒ T1)** is dataset-specific. In our sample, disc_a_psq=0 happens iff deg(a) ≠ 2, which holds iff the family is from the 482-irrationals catalog. R0 therefore says "unit-numerator quadratic GCFs are transcendental" — exactly the published 482-irrationals theorem (P02). It is not a new lemma; it is a recovery test.
- **Rule R1/R2 (within F(2,4): conv_slope <= 0.15 ⇒ T0)** captures finite-termination vs non-termination. Per f1_base_certificate.json, all 113,270 Rat families in F(2,4) are either trivial_zero (729) or finite_termination (112,540) — there is no "non-terminating-but-rational-limit" Rat family in F(2,4). Our rule confirms this dichotomy on a 300-sample but does not generalize beyond F(2,4).
- **finite_termination=1 for all 500 records** — a numerical-floor artifact. The conv_slope feature is therefore much weaker than intended; only 4 T1 records had non-zero slope in the late tail window. **Re-run with dps=200 and tail window n ∈ [10, 30]** before drawing any inference about asymptotic decay rates.
- **5/13 features (BT_disc, lam_ratio, R_struct, int_resonance, stokes_idx) were never used.** The depth-6 tree found 100% accuracy without them. This means the classifier did not test whether the BT/Stokes spectral data is genuinely discriminative on this corpus. To stress-test: extend the corpus to F(2,6) or F(4,2), where Rat is sparser and Trans more diverse, and the easy shape/termination features no longer suffice.
- **Discrepancy: local Rat enumeration = 58,464 vs cert's 113,270** (-48.4%). My structural predicates miss the certificate's mechanism for nearly half of Rat. This does not affect the T0 sample (300 << 58,464) but Claude should know the T0 distribution is biased toward the structurally-easy half.

## What would have been asked (if bidirectional)
- Should the classifier corpus span more deg-pairs than {(2,2), (0,2)}? Including F(2,6), F(4,2), F(6,4) would let the BT/Stokes features earn their keep and produce genuinely-novel rules.
- Is the 482-irrationals data the only available T1 source, or do we have an algebraic-irrational (T0_alg) catalog with concrete coefficients? The current "T0" label conflates rational and algebraic limits.
- Is conv_slope fit window [50,180] at dps=60 the intended setup, or should I have used a larger dps and earlier window from the outset?

## Recommended next step
**UMB-T0T1-CLASSIFIER-V2**: extend the corpus to (deg_a, deg_b) ∈ {(2,2), (4,2), (2,4), (4,4), (0,2)} with ≥100 T0 + ≥100 T1 per shape; recompute conv_slope at dps=200 over n ∈ [10, 30]; re-train. The depth-6 tree must use ≥4 features to maintain >97% accuracy in the multi-shape regime — that is the genuine effective-criterion test. Only then does it make sense to lift R0/R1/R2 to formal Lean verification.

## Files committed
- build_dataset.py — dataset assembly + feature engineering (10 KB)
- train_classifier.py — DT + GBM training, leaf walker, ROC, SVG export
- train_f24_only.py — F(2,4)-only stratified 5-fold CV (companion analysis)
- dataset.csv — 500 records × 21 columns (idx, label, source, coeffs + 13 features)
- features.json — feature schema and build metadata
- metrics.json — full holdout metrics for both classifiers
- f24_only_metrics.json — F(2,4)-only CV metrics + leaf rules
- confusion.json — confusion matrices (holdout)
- roc.json — ROC curve points + AUC
- tree.svg — depth-6 decision tree visualization (matplotlib render)
- tree.dot — Graphviz source (re-render with `dot -Tsvg tree.dot`)
- tree.txt — text export of tree splits
- leaf_rules.json — all leaves with conditions, support, purity
- rules_extracted.md — Lemma-candidate rules (top-level + F(2,4)-only)
- misclassified_holdout.json — holdout misclassifications (empty: 0 cases)
- halt_log.json — HALT triggered, escalation directive
- discrepancy_log.json — Rat enumeration count discrepancy
- unexpected_finds.json — feature-engineering caveats (read these)
- claims.jsonl — 6 AEAL entries
- build.log, train.log, stdout.log, train_stdout.log, f24_train_stdout.log

## AEAL claim count
6 entries written to claims.jsonl this session (also appended to top-level claims.jsonl).
