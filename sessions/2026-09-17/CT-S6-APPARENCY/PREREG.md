# PREREG.md — CT-S6-APPARENCY

## Hypothesis
System B has exactly one apparent point among `rho+`, `rho-`, and `infinity`, so after removing apparent singularities its effective Katz multiset is `(0, 0, 1)`. System A's dash slot denotes a singular point that is NOT FOUND in the finite affine line outside `z=0` by denominator/leading-coefficient inspection and is not an apparent/regular point being dropped.

## Observable
Exact symbolic local exponents for System B at `rho+`, `rho-`, and `infinity`; exact symbolic Frobenius log-obstruction tests through the exponent difference when the exponents are integers; exact pole-order/Katz recomputation after removing points proved apparent. For System A, exact symbolic enumeration of finite singular candidates plus infinity and the same exponent/log test if any dropped regular/apparent point is found.

## Falsifier and threshold
Falsifier F1 fires if any algebraic simplification, indicial equation, recurrence residual, or log-obstruction identity required by the script is nonzero. Threshold: exact equality to zero in SymPy; no numerical tolerance and `dps = null`.

Falsifier F2 fires if a point classified APPARENT has non-integer exponents, a nonzero symbolic log obstruction, or a negative shifted holomorphic order. Threshold: exact symbolic zero/nonzero; no numerical tolerance and `dps = null`.

Falsifier F3 fires if the Table 2.1/PV row text cannot be inspected in the named PDF page extraction or classification table. Threshold: required row tokens `D`, `PV`, `0`, `0`, `1`, `-` found in the extracted/inspected source.

Falsifier F4 fires if repository HEAD differs from `08aa0e2381b3dc37ee54a3200b7272755ca11d59` at final verification, or if files were modified outside `sessions/2026-09-17/CT-S6-APPARENCY/` by this session.

## Vacuity pre-check
Before evaluating the target points, compute an indicial/log test for a parameterized Euler-type regular singular normal-form potential `lambda/s^2`. Confirm the observable changes when `lambda` changes by verifying the indicial exponent difference changes symbolically. Also compute a synthetic apparent regular singular example with exponents `0,2` and verify the log obstruction vanishes only for the apparent-form test case and is detected as nonzero after perturbing the relevant coefficient.

## Fixed classification rule reused from CT-S4
For `u'' = r u` with `m` the pole order of `r` at `z0`: `m <= 2` gives a regular singular point; `m = 2k` even gives unramified Katz `k-1`; `m` odd gives ramified index 2 and Katz `m/2 - 1`. At infinity use `r_inf(t) = r(1/t)/t^4 - (3/4)/t^2`. The observable is an integer pole order, so no numerical tolerance is involved.

## Scope update preregistration addendum (2026-09-17T18:16:53+09:00 operator update)

The operator supplied new primary-source evidence: the V_quad companion v1.2 PDF is now present in `sessions/2026-09-17/CT-R1-AUDIT/refs/vquad_resurgence_v1.2_zenodo-20481592.pdf`, and Conjecture 4.1 concerns a third ODE, System C.

### Added hypothesis
System C, `a(x)y'' + a'(x)y' - x^2 y = 0` with `a(x)=3*x^2+x+1`, has finite candidate singularities `s1,s2=(-1 ± i*sqrt(11))/6`. The companion asserts these are apparent with exponents `{0,1}`; this session will test that assertion exactly rather than assume it. System C at infinity is expected by the companion to be unramified irregular of Poincare rank 1.

### Added observables
For System C: exact local exponents at `s1,s2`, exact symbolic log-term test when integer exponents occur, exact infinity normal-form pole order/Katz invariant, and exact Katz multiset after removing points actually proved apparent. For the relation task: exact comparison of System C under `x=1/z` to System B and exact comparison of System C to CT-S5B's inverted System B normal-form potential.

### Added falsifiers and thresholds
F5 fires if System C finite exponents are not the companion-claimed `{0,1}`. Threshold: exact symbolic equality of the indicial roots; no dps.

F6 fires if a System C finite point classified APPARENT has a nonzero symbolic log obstruction or non-holomorphic shifted local solution. Threshold: exact symbolic zero/nonzero; no dps.

F7 fires if System C infinity has normal-form pole order other than `4` or Katz invariant other than `1`. Threshold: exact integer pole order; no dps.

F8 fires if the explicit System C/System B relation check leaves a nonzero exact normal-form difference after the tested coordinate/gauge maps. Threshold: exact symbolic zero/nonzero; no dps.

### Added Remark 2.2 test cases, fixed before running
To test the general claim that for PCF-derived continuum equations with polynomial `b`, the roots of `chi=b` are always apparent, I will test two additional polynomials:

1. `b_test_1(x)=x+1`, using continuum equation `b*y'' + b'*y' - x^2*y = 0`.
2. `b_test_2(x)=x^2+1`, using continuum equation `b*y'' + b'*y' - x^2*y = 0`.

At every simple root of these `b_test_i`, I will compute exact local exponents and the same symbolic log-term test. If the apparent claim fails, I will report it as a finding.

### Priority if runtime becomes excessive
Follow the operator's priority order: System C finite apparency; System C infinity/Table comparison; Remark 2.2 tests; System C/System B relation; existing System B results; System A dash slot.
