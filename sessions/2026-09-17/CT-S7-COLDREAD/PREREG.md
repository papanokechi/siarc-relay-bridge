# Pre-registration: CT-S7-COLDREAD

Scope: cold mathematical review of `sessions/2026-09-17/CT-S1-THEOREM/theorem.tex` only, at repository HEAD observed before review.

## Target 1: Theorem `thm:radius`, Step 3
Observable: the exact LaTeX text of Step 3 and any sub-lemma/exchange argument therein concerning the multinomial coefficient `(dn)!/(n!)^d`, especially the claimed maximum of multinomial coefficients over compositions of `dn` into `d` nonnegative parts.
Defects before computation/inspection of outputs:
- GAP if balanced maximality is asserted without a complete proof or if an exchange argument does not show all maximisers have parts within 1 and hence equal to `n` under sum `dn`.
- ERROR if any displayed inequality direction, off-by-one count, or edge case is false.
- GAP if a load-bearing lower bound depends on an unproved maximality claim rather than a proved average/max argument.

Numerical observable: exact-integer checks of `d^(dn)/(dn+1)^(d-1) <= (dn)!/(n!)^d <= d^(dn)` for small `d,n`, including `d=1`.
Defect: any counterexample.

## Target 2: Theorem `thm:growth`, Step 3 / G1
Observable: the exact LaTeX text of Step 3 and its closure of G1; exact symbolic expansion of `(1-r/n)(1-1/n)^(-r)` through at least order `n^-2`; finite-product tail reasoning; and DLMF 5.11.12 fetched from `dlmf.nist.gov`.
Defects before computation/inspection of outputs:
- ERROR if the `1/n` terms do not cancel in symbolic expansion.
- GAP if convergence of the product is used to claim `1+O(1/n)` without a sufficient tail estimate.
- ERROR if DLMF 5.11.12 does not state an asymptotic implying the limiting constant for `Gamma(n+1-r)n^r/Gamma(n+1)` is 1 under the theorem's hypotheses.
- GAP/ERROR if hypotheses do not cover complex `r` or large `Re(r)`, or if the argument assumes the gamma ratio asymptotic it is trying to prove.

Criteria are fixed by this preregistration and will not be changed after seeing computational outputs.
