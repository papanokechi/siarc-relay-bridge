# Verdict — T37L-A1ZERO-CATALOGUE-SCAN

**Verdict label:** `T37L_THIRD_STRATUM_HIGHER_DIM`

**Date:** 2026-05-03

## One-line

The locus B(α, β, γ) := α/16 + γ − β²/(4α) = 0 is a 2-dimensional
quadric surface in (α, β, γ)-space; 6/6 algebraically-distinct
integer-lattice candidates on it numerically confirm a₁ = 0 at
dps=300, N=2000, with envelope half-range 10⁻⁴⁰ to 10⁻⁴⁷ — consistent
with sub-stratum (iii) being a higher-dimensional algebraic
sub-variety, with QL09 just one of infinitely many lattice points.

## Numbers (consolidated)

| Candidate          | (α, β, γ, δ, ε)   | recurrence a₁  | fit a₁ central | env half-range | confirms |
|--------------------|-------------------|----------------|----------------|----------------|----------|
| Q1 (QL09 repro)    | (2, 3, 1, 5, 0)   | 0 (exact)      | 10⁻⁴⁹          | 10⁻⁴⁰          | True     |
| Q2 (α=2, β=1)      | (2, 1, 0, 1, 0)   | 0 (exact)      | 10⁻⁵¹          | 10⁻⁴³          | True     |
| Q3 (α=2, β=5)      | (2, 5, 3, 1, 0)   | 0 (exact)      | 10⁻⁵²          | 10⁻⁴⁴          | True     |
| Q4 (α=4, β=2)      | (4, 2, 0, 1, 0)   | 0 (exact)      | 10⁻⁵³          | 10⁻⁴⁶          | True     |
| Q5 (α=4, β=6)      | (4, 6, 2, 1, 0)   | 0 (exact)      | 10⁻⁵⁴          | 10⁻⁴⁷          | True     |
| Q6 (α=8, β=4)      | (8, 4, 0, 1, 0)   | 0 (exact)      | 10⁻⁵⁶          | 10⁻⁴⁷          | True     |

Tolerances: |a₁| < 10⁻³⁰ counts as zero; envelope half-range < 10⁻²⁵
counts as flat. All 6 candidates clear both by margin ≥ 10¹⁰.

## Algebraic locus

```
B(α, β, γ) = α/16 + γ − β²/(4α) = 0
⇔ α² + 16αγ − 4β² = 0
⇔ γ = (4β² − α²) / (16α)
```

Free parameters: α, β. γ is determined. Dimension: 2.

Integer lattice in box (α ≤ 10, |β| ≤ 20): 21 lattice points
including QL09's (2, 3, 1).

## Picture v1.11 amendment recommendation

G20 sub-stratum (iii) at d=2: the a₁ = 0 sub-stratum is a
**2-dimensional algebraic sub-variety** of (α, β, γ)-space, defined
by α/16 + γ − β²/(4α) = 0 (equivalently α² + 16αγ − 4β² = 0). When
the auxiliary parameters (δ, ε) are included, the sub-stratum lifts
to a 4-dimensional cylinder, since (δ, ε) do not enter the bracket B
and do not affect a₁ at d=2 (the k=1 step of the Birkhoff recurrence
has no a₍ₖ₋₂₎, a₍ₖ₋₃₎ contributions).

QL09 is one integer-lattice point on this surface among infinitely
many. T35's 4-rep catalogue intersects sub-stratum (iii) only at
QL09 by the contingent choice of the 4 representatives, NOT because
the sub-stratum is sparse.

## What this verdict does NOT claim

* It does NOT claim the new lattice points (Q2–Q6) are realised by
  natural Painlevé-Lax / arithmetic PCF families. The Q-side
  invariants (A_pred, Δ_b, side, c0, ρ) are not computed for the new
  candidates; that requires Conte–Musette family-extension which is
  out of T37L scope.
* It does NOT prove the structure. Per controlled vocabulary, the
  algebraic + numerical evidence is "consistent with" sub-stratum
  (iii) being a 2-d quadric. AEAL elevation requires Claude review.
