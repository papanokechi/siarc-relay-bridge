# Slot 148 -- BEFORE / AFTER axiom signature comparison

**Status:** BEFORE-only. No edit was attempted (fire HALTED at STEP 0.4(c)
PRECONDITION_DIRTY_TREE before reaching TASK 3).

## BEFORE -- verbatim from `lean/Thm66_ApparentSingularity.lean` lines 88-96

The file uses Unicode (complex-C double-strike, Greek rho, arrow `->`,
not-equal `!=`). Rendered here in ASCII transliteration for FV-discipline; the
file content is preserved unchanged because no edit was made.

```
-- AXIOM: Frobenius theory gives indicial polynomial = rho^2 at apparent singularity.
-- AEAL-status: blocked | mathlib_gap: Frobenius ODE theory
axiom frobenius_double_root_at_apparent_singularity
    (a c : C -> C) (s : C)
    (ha_root : a s = 0)
    (ha_simple : deriv a s != 0)
    (h_exact : forall x, HasDerivAt (fun x => a x * deriv (fun y => y) x)
                     (a x) x) :
    IndicialPoly a s = fun rho => rho ^ 2
```

Parameter count: 5 explicit (`a`, `c`, `s` plus 3 hypotheses).
Hypothesis count: 3 (`ha_root`, `ha_simple`, `h_exact`).
Conclusion: `IndicialPoly a s = fun rho => rho ^ 2`.
AEAL status: `blocked | mathlib_gap: Frobenius ODE theory`.

## AFTER -- planned (per slot 148 sec 1 TASK 3); NOT APPLIED in this fire

```
axiom frobenius_double_root_at_apparent_singularity
    (a c : C -> C) (s : C)
    (ha_root : a s = 0)
    (ha_simple : deriv a s != 0) :
    IndicialPoly a s = fun rho => rho ^ 2
```

Parameter count: 4 explicit.
Hypothesis count: 2 (`ha_root`, `ha_simple`).
Conclusion: identical to BEFORE.
AEAL status: unchanged.

## Auxiliary diagnostic (from slot 148 sec 1 TASK 2)

The deleted hypothesis `h_exact : forall x, HasDerivAt (fun x => a x * deriv
(fun y => y) x) (a x) x` admits the following reduction:

- `deriv (fun y => y) x = 1` for any `x` (derivative of identity).
- LHS function reduces to `fun x => a x * 1 = a x`.
- The hypothesis becomes `forall x, HasDerivAt a (a x) x`, i.e., `a' = a`
  pointwise.
- This is FALSE for general `a`; the only solutions are `a(x) = a*e^x` and the
  zero function. For the specific `a_coeff_c` coefficient used at the L118 +
  L120 use sites in `apparent_singularity_thm_i`, this hypothesis is
  generically unsatisfiable.

Conclusion: `h_exact` is a vestigial parameter, not a meaningful Frobenius
hypothesis. Pattern alpha (delete `h_exact`) is the correct closure path for
S1 + S2.

## Theorem-strength comparison (R6 review skeleton; per slot 148 sec 1 TASK 6)

(NOT executed in this fire because edit was not applied. Skeleton recorded
here for re-fire continuity.)

(1) BEFORE and AFTER have identical conclusion: `IndicialPoly a s = fun rho =>
    rho ^ 2`.
(2) AFTER has fewer hypotheses (2 vs 3); strictly stronger as a claim.
(3) Any downstream theorem reachable via AFTER is also reachable via BEFORE
    (with extra `h_exact` hypothesis, which was vacuously requiring an
    unsatisfiable claim at the use sites).
(4) `apparent_singularity_thm_i` (Thm66:113) theorem strength: preserved or
    strengthened post-edit (strict strengthening here, because the pre-edit
    invocation depended on the unsatisfiable `h_exact` discharged by `(by
    sorry)`).
(5) AEAL status: axiom remains tagged `mathlib_gap: Frobenius ODE theory`; the
    math-content claim is the standard Frobenius result independent of the
    vestigial parameter.

R6 review status: NOT_RUN (fire halted before edit). Successor fire must
re-run TASK 6 in-context before commit.

## Use-site cleanup (planned; NOT applied)

```
-- BEFORE (lines 117-120):
        . exact frobenius_double_root_at_apparent_singularity
            a_coeff_c c_coeff_c s_1 root_s1 a_deriv_s1_ne_zero (by sorry)
        . exact frobenius_double_root_at_apparent_singularity
            a_coeff_c c_coeff_c s_2 root_s2 a_deriv_s2_ne_zero (by sorry)

-- AFTER (lines 117-120):
        . exact frobenius_double_root_at_apparent_singularity
            a_coeff_c c_coeff_c s_1 root_s1 a_deriv_s1_ne_zero
        . exact frobenius_double_root_at_apparent_singularity
            a_coeff_c c_coeff_c s_2 root_s2 a_deriv_s2_ne_zero
```

Both `(by sorry)` arguments deleted. Project active sorry count would drop
from 2 to 0 (D-143-1 canonical interpretation: 2 active terms; comment-narrative
matches at proof_targets.lean L2 and Thm66 L63 are not active terms).

Cross-check at TASK 4: only 3 grep matches expected for
`frobenius_double_root_at_apparent_singularity` (axiom decl L90 + L117 + L119).
Verified by this fire (read-only) -- 3 matches, all in
`Thm66_ApparentSingularity.lean`. No use sites in `WallisFamily.lean`,
`CardEvenOfInvolution.lean`, `proof_targets.lean`, or `lakefile.lean`.
HALT_148_UNEXPECTED_USE_SITE risk: LOW.
