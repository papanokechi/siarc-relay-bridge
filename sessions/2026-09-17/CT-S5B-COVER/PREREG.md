# PREREG.md — CT-S5B-COVER (P5b)

## Hypothesis

H1: Pullback of System A along the ramified double cover `z = w^2`, with the correct normal-form Jacobian/Schwarzian correction, changes the local type at the branch point from ramified Katz `1/2` to unramified Katz `1`, matching System B only at that local invariant.

H2: Applying the inversion `z -> 1/x` to System B exchanges the irregular point at `z=0` with `x=infinity` and yields a singular configuration comparable to VQ-N1's recorded configuration.

## Observable

Exact symbolic normal-form potentials and exact pole orders at every finite singular point and at infinity. Derived observables are formal type, ramification index, and Katz invariant via the CT-S4 rule, reused verbatim:

For `u'' = r u` with `m` = pole order of `r` at `z0`: `m <= 2` implies regular singular; `m` even `= 2k` implies unramified with Katz invariant `k - 1`; `m` odd implies RAMIFIED with ramification index 2 and Katz invariant `m/2 - 1`. At infinity use `r_inf(t) = r(1/t)/t^4 - (3/4)/t^2`.

The observable is integer pole orders and integer/half-integer Katz invariants from exact SymPy computation; no floating point and no numerical tolerance are allowed.

## Falsifier

F1: Halt if the symbolic pullback rule fails an independent Euler-equation exponent-doubling test under `z = w^2`.

F2: Halt if the vacuity pre-check shows the observable does not move: specifically, if a deliberately unramified pole-order-4 test operator becomes ramified under `z = w^2`, or if System A's pole order at `0` does not change under `z = w^2`.

F3: Halt if any required comparison data named in the prompt is missing from the repository.

F4: Halt if exact recomputation of the copied CT-S4 System A/B baseline fails.

## Vacuity pre-check

Before drawing conclusions, the script must verify that `r_test(z)=1/z^4` pulls back along `z=w^2` to a pole of order 6 at `w=0`, hence remains even/unramified rather than spuriously becoming ramified; and that System A's `r_A` pole order at `0` changes from `3` in `z` to `4` in `w` after pullback.

## Runtime budget

This exact symbolic check is expected to complete in under 60 seconds on the provided machine. Halt and report if runtime exceeds 180 seconds.
