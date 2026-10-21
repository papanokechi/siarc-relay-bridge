# PREREG

Written before computation beyond reading TASK.md and listing the packet files.

## Hypotheses

H1: System C, after the affine map sending its two finite singular points to z=0 and z=1, matches at most one scalar reduction of a point in vdPS family (4.1) on U0.

H2: The correct component comparison is determined by elimination: if a scalar equation's dependent variable is the first component of Y, compare it with the first-component scalar reduction; if it is the second component, compare it with the second-component scalar reduction. The paper's definition of q is relevant only if it identifies which component is used as scalar dependent variable.

H3: The source typo noted in TASK.md is a typographical omission of t in b(z), not a convention change.

## Observables

O1: Exact formulas P_i(z), Q_i(z) for both component reductions of Y'=N Y, derived by elimination.
O2: Exact affine-transformed P_C(z), Q_C(z) for System C.
O3: Exact or high-precision residuals for P_i-P_C and Q_i-Q_C at the derived parameter point, using corrected b(z).
O4: Independent numerical residuals from solving the first-order system and testing the relevant scalar ODE on multiple initial conditions.
O5: Direct page-image quotes for q and vdPS hypotheses on M in the (0,0,1) row.

## Falsifiers and thresholds

F1: If the affine map is ambiguous or the packet does not contain enough data to reconstruct family (4.1), halt and report missing data.
F2: For exact comparisons, any nonzero simplified/cancelled difference falsifies equality.
F3: For numerical checks at 80 dps, any absolute residual > 1e-60 in algebraic re-substitution falsifies the proposed match.
F4: For independent numerical ODE residuals at 80 dps, any absolute residual > 1e-45 at ordinary test points falsifies the proposed component match.
F5: A vacuity pre-check must demonstrate each computational test fails on a deliberately wrong input: wrong P/Q or wrong parameter/component must produce a residual above threshold.

## Vacuity pre-check to run

Run scripts\vacuity_precheck.py before membership computations. It will compare System C against a deliberately perturbed scalar equation (Q shifted by 1/7) and require a residual > 1e-3. If this does not fail as expected, computational testing is void and work halts.
