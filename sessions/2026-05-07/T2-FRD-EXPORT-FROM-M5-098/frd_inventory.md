# FRD inventory — M5 (relay 098)

**Generated:** 2026-05-07
**Source:** SIARC relay 098 (T2-FRD-EXPORT-FROM-M5-098)
**Substrate anchors:** picture_v1.19.md (SHA-16 8BD9043370872F07) +
PCF-1 v1.3 = `tex/submitted/p12_journal_main.tex` (SHA-16
82173A09521D6676)

This inventory enumerates the 9 Formalization-Ready Definitions
exported from M5 in this fire. Each row anchors the FRD to a
picture_v1.19 line (or line range) and a PCF-1 v1.3 section. The
Lean encoding lives in [m5_frds.lean](m5_frds.lean) under namespace
`SIARC.M5`.

## Inventory table

| ID | Lean name | Idiom | picture_v1.19 anchor | PCF-1 v1.3 anchor | Lean lines |
|----|-----------|-------|----------------------|-------------------|------------|
| B1 | `VQuad` | `structure` | line 919 (M5 row) | § 1.1 (eq:d2-class, L113-130) | L67-89 |
| B2 | `Stratum` + `R` | `inductive` + `def` | lines 295-298 (3-stratum partition) | § 1.1 L109-116 (PCF schema) | L97-130 |
| B3 | `indicialPoly` + `doubleRootCondition` + `indicialDiscriminant` | `def` + `Prop` | line 91 (Newton-polygon convention) | § 2.1 L326-336 (eq:char) + § 4 def:Delta | L138-170 |
| B4 | `StokesData` + `stratumOf` + `stokes` | `structure` + `def` | lines 295-298, 313-318, 347-353 | § 2.5 L419-445 + § 5 L710-922 | L178-211 |
| B5 | `zetaStar` | `noncomputable def` | line 360 (V_quad ζ*=4/√3) | § 6 L958-1046 (V_quad prototype) | L219-237 |
| B6 | `PCFLimit` | `noncomputable def` | line 919 (M5 closure) | § 1.1 L109-116 (eq:PCF) | L245-261 |
| B7 | `M8b_axis_residual_acceptance` | `theorem` (stub) | M8b row L1031-1041 | (forward-link to relay 092) | L268-284 |
| B8 | `wallisStep` + `wallisP` | `def` (recursive) | line 91 (Wallis convention) | § 2.1 L312-322 (eq:wallis) | L292-318 |
| B9 | `SpecK` + `specK` | `structure` + `def` | line 41 (Spec(K) reference) | § 2.2 L338-361 (eq:speck) | L326-360 |

**Total FRDs:** 9 (relay floor 5; soft cap 15; well within range)
**Total lines in m5_frds.lean:** 308
**Forbidden-verb scan on m5_frds.lean:** 0 hits (PASS)

## Per-FRD substrate cross-check

### B1 — VQuad family (5-parameter rational tuple)

- **Convention used:** SIARC F(2,4) leading-first per memory file
  `f1-base-d2d4-complete-2026-04-22.md` line 24:
  `a_coeffs = (a2, a1, a0)` with `a(n) = a2 n² + a1 n + a0`,
  `b_coeffs = (b1, b0)` with `b(n) = b1 n + b0`.
- **picture_v1.19 anchor:** line 919, the M5 milestone row
  "V_quad -> P_III(D_6) algebraic identity [DONE — CT v1.3]".
- **PCF-1 v1.3 anchor:** § 1.1 lines 113-130 with the d=2 class
  `a_n = δn + ε`, `b_n = αn² + βn + γ` (label-swapped from the
  SIARC convention; see `discrepancy_log.json` D-D3).
- **Lean idiom:** `structure VQuad where a2 a1 a0 b1 b0 : ℚ` with
  `deriving Repr, DecidableEq`.
- **Sorries:** 0 (definition only; no proof body).

### B2 — R(h) ratio + Stratum

- **picture_v1.19 anchor:** lines 295-298
  (3-stratum partition at 60+ digits; neg-rational a₁ /
  pos-rational a₁ / a₁ = 0).
- **PCF-1 v1.3 anchor:** § 1.1 lines 109-116 (PCF schema; ratio
  interpretation `b(h)/a(h)`).
- **Lean idiom:** `inductive Stratum` + `def R (V : VQuad) (h : ℚ) : ℚ`.
- **Sorries:** 0 in `R`; partial-function audit (D-D2) deferred.

### B3 — Indicial polynomial + double-root condition

- **picture_v1.19 anchor:** line 91 (Wimp-Zeilberger Newton-polygon
  convention; G23 borderline-case anormal ansatz).
- **PCF-1 v1.3 anchor:** § 2.1 lines 326-336 (Perron-Poincaré
  characteristic eq:char) + § 4 Definition 4.1 (`def:Delta`,
  balanced discriminant `Δ = β² - 4αγ`).
- **Lean idiom:** `def indicialPoly`, `def doubleRootCondition : Prop`,
  `def indicialDiscriminant`.
- **Sorries:** 0.

### B4 — Stokes data per stratum

- **picture_v1.19 anchor:** lines 295-298 (a₁ partition) +
  313-318 (G20 sharpening) + 347-353 (Prompt 010 verdict
  G6B_PARTIAL_HIGHER_ORDER_NEEDED with per-rep S₁ values).
- **PCF-1 v1.3 anchor:** § 2.5 lines 419-445 (Stokes phenomenon
  background) + § 5 lines 710-922 (Stokes-exponent diagnostic
  with eq:S definition).
- **Lean idiom:** `structure StokesData`, `def stratumOf := sorry`,
  `def stokes := sorry`.
- **Sorries:** 2 (`stratumOf`, `stokes`); tracked in
  `coverage_gap_analysis.md` row B4 for next-fire backlog.

### B5 — zetaStar (target convergence value)

- **picture_v1.19 anchor:** line 360 (V_quad ζ* = 4/√3 exact;
  CC-MEDIAN-RESURGENCE-EXECUTE 2026-05-02).
- **PCF-1 v1.3 anchor:** § 6 lines 958-1046 (V_quad Painlevé III
  prototype; `(α_PIII, β_PIII, γ_PIII, δ_PIII) = (1/6, 0, 0, -1/2)`).
- **Lean idiom:** `noncomputable def zetaStar (V : VQuad) : ℝ := sorry`.
- **Sorries:** 1.

### B6 — PCFLimit operator

- **picture_v1.19 anchor:** line 919 (M5 closure row).
- **PCF-1 v1.3 anchor:** § 1.1 lines 109-116
  (`L = b₀ + a₁/(b₁ + a₂/(b₂ + ...))`, eq:PCF).
- **Lean idiom:** `noncomputable def PCFLimit (V : VQuad) : ℝ := sorry`.
- **Sorries:** 1; gated on Mathlib4 continued-fraction anchor
  (see `mathlib4_anchor_opportunities.md` row B6).

### B7 — M8b axis residual acceptance

- **picture_v1.19 anchor:** M8b row at lines 1031-1041
  (S₂ PERMANENTLY FORECLOSED via Stage-2-LSQ + Borel-Padé).
- **Forward-link anchor:** sessions/2026-05-07/T1-017M-BOREL-PADE-S2-092/
  handoff.md (15 AEAL claims; verdict M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE).
- **Lean idiom:** `theorem ... : True := by trivial` (statement-only stub).
- **Sorries:** 0 (proof body is `trivial`); substantive predicate
  upgrade tracked in `coverage_gap_analysis.md` row B7.

### B8 — Wallis recurrence

- **picture_v1.19 anchor:** line 91 (Newton-polygon convention).
- **PCF-1 v1.3 anchor:** § 2.1 lines 312-322 (eq:wallis with
  seeds `(p₋₁, p₀, q₋₁, q₀) = (1, b₀, 0, 1)`).
- **Lean idiom:** `def wallisStep`, `def wallisP : ℕ → ℚ` (recursive).
- **Sorries:** 1 (`wallisP` body for `_ + 2`).

### B9 — Spec(K) classification

- **picture_v1.19 anchor:** line 41 (Spec(K) classification reference).
- **PCF-1 v1.3 anchor:** § 2.2 lines 338-361 (Spec(K) 5-tuple
  `(d, Λ, Δ, ρ, τ)` with eq:speck).
- **Lean idiom:** `structure SpecK`, `noncomputable def specK := sorry`.
- **Sorries:** 1.

## Anchor coverage summary

- **picture_v1.19 lines covered:** 41, 91, 295-298, 313-318, 347-353,
  360, 919, 1031-1041 (8 distinct line ranges).
- **PCF-1 v1.3 sections covered:** § 1.1 (d=2 class + eq:PCF),
  § 2.1 (Wallis recurrence + eq:char), § 2.2 (Spec(K)),
  § 2.5 (Stokes phenomenon), § 4 (def:Delta + dichotomy table),
  § 5 (Stokes-exponent diagnostic), § 6 (V_quad prototype) =
  7 of 7 substantive sections referenced.
- **PCF-1 v1.3 sections NOT covered:** § 2.3 (Spec(K)
  classification details — included in B9 but not enumerated
  per row), § 2.4 (Heun & Painlevé equations) — partial
  coverage flagged in `coverage_gap_analysis.md` row CG-1.

## Sorry count summary

| FRD | Sorry count | Discharge target |
|-----|-------------|------------------|
| B1 | 0 | — |
| B2 | 0 | — |
| B3 | 0 | — |
| B4 | 2 | M10-PROOF-DRAFT or B4-discharge fire |
| B5 | 1 | Mathlib4 algebraic-number anchor |
| B6 | 1 | Mathlib4 continued-fraction anchor |
| B7 | 0 | (statement strengthening only) |
| B8 | 1 | Wallis-recurrence discharge fire |
| B9 | 1 | M10-PROOF-DRAFT |
| **Total** | **6 sorries** | distributed across 5 FRDs |

This is consistent with the relay's scope: **SCAFFOLD only**, not
proof-grade. The 6 sorries are the principal next-fire backlog.
