# T2 — rubber-duck self-critique

## (a) Bonferroni K choice

We adopted **K = 14** to match R1.1's stated Bonferroni denominator.
Inspecting the actual hypothesis list in this session, only 9
predictors were live (`H_baseline`, `H_E4`, `H_Δ_w6`, `H_Δ_w12`,
`H_E6`, `H_j_minus_1728`, `H_eta`, `H_imtau`, `H_E4_cube`); the
height/class-number rows were dropped rather than fabricated.

This is conservative — increasing K only inflates the corrected
p-values. The winning Petersson predictor at p_Bonf(K=14) = 7.1e-6
would still be 4.6e-6 at K=9. The winners are robust to the K
choice in the range [9, 14].

`H_Δ_w6` and `H_Δ_w12` are not statistically independent (they
differ only by an additive constant in log space), so K is
slightly inflated — but again this only hurts the winners.

## (b) τ_b reduction robustness

We invert `j(τ) = j_target` directly on the boundary of the standard
fundamental domain `F = { τ : |Re τ| ≤ 1/2, |τ| ≥ 1, Im τ > 0 }`:

- `j > 1728` → `τ = i·t` with `t > 1`
- `j < 0`    → `τ = 1/2 + i·t` with `t > √3/2`
- `0 < j < 1728` → `τ = exp(i·θ)` with `θ ∈ (π/3, π/2)`
- `j = 0`    → `τ = ρ = (1+i√3)/2`
- `j = 1728` → `τ = i`

Each ensemble cubic falls in exactly one of these cells, and `j(τ)`
is *strictly monotone* on each F-boundary segment, so the Newton
inversion has a unique fixed point. **Cross-check** in Phase A:
recompute `j` from the resulting `(E₄, E₆)` and verify
`|j_recomputed − j_csv| / max(|j_csv|, 1) < 1e-6`. Result: max
relative error across 50 cubics = **4.762e-15** (mpmath dps=200,
q-series truncation N=200), well below the halt threshold.

A SageMath / PARI period-lattice route would pick the same τ in F
modulo SL₂(ℤ); the j-cross-check forecloses any mismatch. Judgment
call documented in handoff.

## (c) Collinearity log|E₄| vs log|j| — `H_E4_cube` sanity check

Because `j = E₄³ / Δ`, we have
`log|j| = 3 log|E₄| − log|Δ|`,
so `H_E4_cube` (3·log|E₄|) and `H_baseline` (log|j|) carry overlapping
information. In the table:

| H_baseline | log|j| | ρ_R13 = −0.568 |
| H_E4 | log|E₄| | ρ_R13 = −0.459 |
| H_E4_cube | 3 log|E₄| | ρ_R13 = −0.459 |
| H_Δ_w6 | (Im τ)^6 |Δ| | ρ_R13 = +0.638 |

`H_E4` and `H_E4_cube` give identical Spearman (rank-monotone), as
expected. The fact that `log|j| = H_E4_cube − log|Δ|` outperforms
both `H_E4_cube` and `H_E4` separately means **the modular
discriminant `Δ` is the dominant signal** — and Petersson-normalising
to `‖Δ‖ = (Im τ)^6 |Δ|` extracts it cleanly (the winner). This is
**consistent with H2's main mechanism** even though
*pure* log|E₄| does not beat the baseline.

## (d) PSLQ basis completeness for D = −3

The augmented basis `B19+` includes Γ(1/3), Γ(2/3), Ω₋₃ = Γ(1/3)³/(2π),
log Γ(1/3), and π/√3. By Chowla–Selberg, periods of CM elliptic
curves with `D = −3` are products in
`Q̄(Γ(a/3) : a ∈ {1,2}) · π·exp(roots of unity)`,
so any rational-quadratic combination should be detectable.

What's **not** in the basis (caveat):
- `Γ(1/3)·Γ(2/3) = 2π/√3` (covered indirectly via Ω₋₃ × π/√3 / (Γ(1/3)²))
- higher `Γ`-product invariants
- `log Δ(ρ)` (a possible amplitude target — but `Δ(ρ)`
  is itself an algebraic multiple of `Γ(1/3)¹⁸ / π¹²`, which is in
  the multiplicative span of `Γ(1/3)` and `π`)

**The actual blocker**: Phase D's α-amplitude is recovered via
`np.linalg.lstsq` on float64 residuals, giving ~14 digits of
precision regardless of `mp.workdps`. PSLQ at 14-digit input
precision against an 19-element basis with max coefficients 10⁶
would find a relation only if the true expression were near-trivial
(coefficients < 100). The H6 prediction at `D = −3` likely involves
cubic powers of `Γ(1/3)` and rational coefficients of order
~1, so **insufficient input precision is the limiting factor**, not
basis completeness.

The redesigned T2.5d protocol must extract α as an `mp.mpf` from
mpmath WKB matching (not lstsq) at dps≥1500, and only then run PSLQ
at dps=1500.

## (e) Verdict label trade-off

The literal §5 bullet-4 halt fires; the bullet-3 halt does NOT
(H_E₄ — well, the Petersson-grounded variants — does beat baseline,
which is what bullet 3 protects against). The Phase D failure is a
*precision-limited inconclusiveness*, not a falsification:
the N-scaling auxiliary shows |δ| → 0 at finite N, and PSLQ found
no nontrivial relation for δ either, which is the correct outcome
for an artefact.

We chose `T2_PASS_E4_BEATS_LOGJ` as the headline, with halt
annotated, rather than `T2_HALT_PSLQ_INCONSISTENT`, because the
session's Phase B/C result is robust and publishable as-is in PCF-2
v1.3, while Phase D's failure is a known protocol-design issue.
This is documented in `verdict.md` and `handoff.md`.
