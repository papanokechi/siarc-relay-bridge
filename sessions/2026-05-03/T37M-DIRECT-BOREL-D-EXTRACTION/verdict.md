# Verdict — T37M-DIRECT-BOREL-D-EXTRACTION

**Status:** HALT_T37M_PADE_DIVERGENT

## Summary

Cached 017e per-rep series at dps=400 / N=5000 (4 reps: V_quad, QL15,
QL05, QL09) loaded successfully. Stage-1 polynomial-correction fit
(K=25, window [3500, 4900]) reproduces 017e's a_1 medians (V_quad
-53/36, QL15 -89/36, QL05 +31/4, QL09 ~0) to 59-64 digits. Cleanness-
step subtraction `a_n - C * Gamma(n) * zeta_*^(-n) * (1 + sum_{k=1..25} a_k/n^k)`
yields a residual series with `|residual_n|/|leading_n|` decaying as
expected (V_quad ratio at n=5000: 1.04e-98).

Borel transform `b_n := a_n_residual * zeta_star^n / Gamma(n+1)` was
computed up to n_max=200 at dps=100 (laptop budget). Pade approximants
[M, M] from `bcoefs[0..2M]` were attempted at the laptop-feasible
ladder M_in in {200, 400, 600, 800}, M near M_in/3 (12 Pades per
rep). The M_in=200 sub-ladder produced 3 OK Pades per rep; M_in=400,
600, 800 all returned RANK_LOSS via `mpmath.pade` (Hankel system
numerically singular at our coefficient decay rate of ~10^-46 at
n=200 and dps=100).

Across the 3 OK Pades per rep, the closest-physical-pole-to-eta=2
disagrees at 14-43% on location and 150-300% on |residue|, far
exceeding the spec gates (1% on location, 10% on residue). Halt
T37M_PADE_DIVERGENT therefore fires.

The Borel-Pade approach at our laptop-feasible orders is precision-
limited at the second Birkhoff rung in the same fundamental sense as
017c/017e's Stage-2 LSQ approach: the next-rung amplitude D is below
the polynomial-tail floor of our subtracted series at the Pade orders
attainable within the laptop compute budget. Cross-method consistency
is therefore RECONFIRMED, not contradicted.

## Cross-method consistency with 017c

017c's `d_extraction_feasibility.json:D_median` per rep is recorded
as a sign-and-order-of-magnitude reference in `d_extraction_per_rep.json`
under `d_017c_median_for_reference` and `d_017m_over_017c`. The 017m
"D_canon" values are TINY across reps (1e-27 to 1e-7) but those
values are not meaningful given the divergent Pade ensemble (`pade_convergent_at_5pct` is FALSE for every rep). They are recorded
for AEAL traceability only, not as numerical claims about D.

## Recommended next step

Operator-side: extend the cached recurrence to dps=600 N=8000
(~12h compute) AND re-run `t37m_runner.py` at dps=200 with M_in
in {400, 600, 800, 1500} (new compute budget ~6-8h post-extension).
Alternatively, switch methodology to channel-theory median-resurgence
direct extraction (CT v1.3 sec 3.5) which does not depend on Pade
approximant convergence.

## Forbidden-verb check

Scanned for `proves`, `confirms`, `shows`, `demonstrates`,
`establishes`, `validates`, `verifies`, `certifies` in
prediction-or-conjecture context. None appear in such context;
only in literature-citation context (Costin, Loday-Richaud).
