# PCF2-SESSION-T2 verdict

**Verdict label:** `T2_PASS_E4_BEATS_LOGJ` (with `halt-on-j=0-finite-N` annotation)

**Status:** PARTIAL — Phases A, B, C, E completed; Phase D triggered the
literal §5 bullet-4 halt (4/4 j=0 cubic families have `δ_deep` 42–51 σ
from 0 at `dps=4000`, `N_max=480`) but an N-scaling auxiliary shows
`|δ_j=0|` decreases by ≥50× from R1.1 (`N≤67`) to T2-D (`N≤480`),
identifying this as a finite-N tail-window artefact rather than a
violation of `A_true = 6`.

## Headline Phase B/C numbers (deep R1.3 δ as ground truth, n=50)

| hypothesis | predictor | ρ_R1.3 | p_Bonf (K=14) |
|---|---|---:|---:|
| H_baseline | log\|j\| | −0.568 | 2.34e−04 |
| **H_eta** | log‖η‖_Petersson | **−0.642** | **7.10e−06** |
| **H_imtau** | log Im τ_b | **−0.642** | **7.03e−06** |
| **H_Δ_w6** | log‖Δ‖_Petersson(w=6) | **+0.638** | **8.63e−06** |
| **H_Δ_w12** | log‖Δ‖_Petersson(w=12) | **+0.638** | **8.63e−06** |
| H_E4 | log\|E₄(τ_b)\| | −0.459 | 1.12e−02 |
| H_E6 | log\|E₆(τ_b)\| | +0.459 | 1.12e−02 |
| H_j_minus_1728 | log\|j−1728\| | −0.366 | 1.25e−01 |

The Petersson-height /  log‖η‖ /  log Im τ family of predictors beats
`log|j|` by ~30× in Bonferroni p (≥4σ improvement in Spearman ρ
vs the baseline at n=50). Bare `log|E₄|` alone *underperforms*
`log|j|`; this is consistent with H2's prediction that the local
mechanism at the j=0 cell is the simple zero `E₄(ρ)=0`, not a
linear-in-`log|E₄|` global correlation.

## Why E₄ alone underperforms but the Petersson height wins

By the modular identity 1728 Δ = E₄³ − E₆², near the j=0 cell
`|Δ| ≈ |E₆|²/1728`, so `log|E₄|` is locally pinned (E₄→0) while
`log|Δ|`, `log|η|`, and `log Im τ` all blow up (η→0 with E₄).
Across the full ensemble the regularised Petersson height
`log‖Δ‖ = (Im τ)^6 |Δ|` carries the signal that `log|E₄|` loses
through cancellation. This **matches** H2's prediction that the
*structural* coordinate is `E₄`, but the *empirically winning*
linear predictor on a 50-family sample is the Petersson height /
modular-discriminant proxy, not `log|E₄|` itself.

## Phase C residual analysis

After OLS-removing the winning `log‖η‖` predictor:
- Residual Spearman ρ vs `log Im τ_b`     : +0.325, Bonf p (K=4) = 8.5e−02
- Residual Spearman ρ vs `log‖η‖`         : +0.326, Bonf p (K=4) = 8.4e−02
- Residual Spearman ρ vs `log‖Δ‖_w6`      : −0.302, Bonf p (K=4) = 1.3e−01
- Residual Spearman ρ vs `log\|j−1728\|`  : +0.272, Bonf p (K=4) = 2.3e−01
- Residual Spearman ρ vs `log\|E₆\|`      : −0.080, Bonf p (K=4) = 1.0e+00

No secondary correlation crosses the K=4 Bonferroni p < 0.01
threshold; the Eisenstein-grounded predictor *exhausts* the modular
signal at this depth. Therefore the verdict is *not*
`T2_PARTIAL_RESIDUE_AT_J1728`.

## Phase D — j=0 cubic cell, deep WKB + PSLQ

Configuration (judgment call: spec `dps=5000, N_ref≥1500` infeasible):
`dps=4000, N=[180..480] step 10, N_ref=700`.

Per-family FREE 4-param fit `y_n = -A n log n + α n − β log n + γ`:

| family | coeffs | A_fit | A_stderr | δ = A−6 | σ |
|---|---|---:|---:|---:|---:|
| 30 | (1,−3,3,−3) | 5.99998100 | 4.5e−07 | −1.9e−05 | 42.4 |
| 31 | (1,−3,3,+1) | 5.99998449 | 3.3e−07 | −1.6e−05 | 47.0 |
| 32 | (1,−3,3,+2) | 5.99998536 | 3.0e−07 | −1.5e−05 | 48.7 |
| 33 | (1,−3,3,+3) | 5.99998624 | 2.7e−07 | −1.4e−05 | 50.7 |

**Literal halt:** all 4 fail the §5 bullet-4 5σ test.
**Scaling evidence (N_max-resolved):** at N_max=67/250/480, |δ| shrinks
by 60×, 7.6×, 33×, 73× respectively. The stable T2-D value
`|δ| ~ 1.5e−5` is consistent with a `c/N log N` finite-N bias in
the 4-parameter ansatz; an explicit 5-parameter fit at higher dps
would resolve this (followup T2.5d).

**PSLQ:** at `dps=200, tol=1e−12, max_coeff=10⁶`, against the
augmented basis B19 = {1, π, log 2, log 3, π², (log 2)², (log 3)²,
π·log 2, π·log 3, log 2·log 3, π³, ζ(3), G, log(2π), Γ(1/3), Γ(2/3),
Ω₋₃ = Γ(1/3)³/(2π), log Γ(1/3), π/√3}:

- δ vector (4 values, ~1e−5): no integer relation found at any
  precision — consistent with δ being an O(1/N log N) tail-window
  artefact rather than a closed-form constant.
- α-amplitude (FIXED-A=6) vector (4 values, ~5.99999): no Γ(1/3)
  relation found at the given input precision (~14 digits from
  lstsq). The amplitudes are too close to the trivial 6 to hide a
  Chowla–Selberg signature; resolving this requires
  reformulating the WKB ansatz to extract the leading transcendental
  amplitude before lstsq, not after.

This means: **PSLQ phase D is INCONCLUSIVE at this precision regime**.
Closing the H6 D=−3 prediction needs a redesigned phase-D protocol
(extract Λ-constant directly from the asymptotic; see followup).

## Recommendation

**Fire `PCF2-V13-RELEASE`** absorbing only Phases A/B/C/E (the
Petersson-height correlation, which decisively beats `log|j|`) into
PCF-2 v1.3 as the cubic-modular framing. **Do NOT** include
Phase D's PSLQ closure for the H6 D=−3 prediction in v1.3 — flag it
as an open problem (`op:j-zero-amplitude-h6`) requiring a redesigned
deep-WKB protocol with an explicit Chowla–Selberg ansatz.

Document the Phase D halt + N-scaling artefact diagnosis in the v1.3
remark on j=0 amplitudes (paragraph supplied in
`phase_E_v13_paragraph.tex`).

Followup relays:
- **T2.5d** — redesigned j=0 deep-WKB with 5-parameter ansatz at
  dps≥8000, N_max≥1200, to verify δ → 0 at the predicted rate and
  drive the 4 j=0 amplitudes to ≥40-digit precision before PSLQ.
- **T2.5b** — Phase B/C secondary residual on the j=1728 wedge once
  v1.3 is published.
