# REPORT — CT-S18-COLDREAD-C3

## What was done

- Obeyed staging: wrote `PREREG.md` before computation; wrote and hashed `FINDINGS-1-3.md` in `outputs\stage1.sha256` before opening `packet\sealed\C3-AS-DRAFTED.md`.
- Rendered and inspected the packet page images one at a time.
- Wrote reproducible SymPy scripts under `scripts\` and saved outputs under `outputs\`.
- Validated controls: determinant wrong variants rejected; Riccati fake-control accepted; `P` self-comparison accepted; batches reported counts.

## Claims

- S18-001 [INSPECTED]: p. 2655 prints `(p + 1/2(q-1)q)^2` in `b(z)` with no `t`.
- S18-002 [PROVEN]: the printed `b(z)` has residual `-(q - 1)(t - 1)(4*p + q^2*t + q^2 - q*t - q)/4`.
- S18-003 [PROVEN]: replacing that square by `(p + 1/2(q-1)qt)^2` makes the residual identically zero.
- S18-004 [VERIFIED]: 90-digit numeric determinant checks accepted the correction and rejected printed/wrong variants.
- S18-005 [INSPECTED]: packet pages show the `(0,0,1)` setup, determinant constraints, and `U_0` coordinate restrictions.
- S18-006 [STRUCTURAL]: System C finite local data give `theta_0=theta_1=0` after normalising roots to `0,1`.
- S18-007 [STRUCTURAL]: System C is consistent with Katz invariant `1` at infinity.
- S18-008 [PROVEN]: the forced rational Riccati rank-one obstruction has no solution.
- S18-009 [PROVEN]: corrected `U_0` gives `P_U0=(z^2-2*q*z+q)/(z*(z-q)*(z-1))`.
- S18-010 [PROVEN]: `P_U0-P_C=-1/(z-q)`, so System C does not match `P` in admissible `U_0`.
- S18-011 [VERIFIED]: the 90-digit `P` mismatch sample was `1.714e+00`.
- S18-012 [STRUCTURAL]: C3 is correct about the `b(z)` typo but not about the drafted moduli-membership/deformation assertion as established by this packet.

See `claims.jsonl` for machine-readable records.

## What was NOT established

- I did not establish an admissible `U_0` chart point for System C.
- I did not compute monodromy/Stokes data.
- I did not establish that a rank-1 twist alone separates System C from the `U_0` family; the direct `P,Q` comparison blocks the identification used here.
- I did not inspect any withheld session material or git history.

## Open questions for the operator

- Is there another vdPS chart, not in this packet, where System C is claimed to land with a full `P,Q` comparison?
- Was the prior matching based only on normal-form `R` rather than the scalar `P,Q` coefficients?
- Is an author notification or erratum status known for the missing `t` in `b(z)`?

## Verdict on C3

`VERDICT-4.md`: **ERROR**.

## Uncommitted files created/modified in this session folder

- `PREREG.md`
- `FINDINGS-1-3.md`
- `VERDICT-4.md`
- `REPORT.md`
- `claims.jsonl`
- `scripts\coldread_checks.py`
- `scripts\derive_b_constraint.py`
- `scripts\explore_family_R.py`
- `scripts\irreducible_check.py`
- `scripts\nsolve_chart.py`
- `scripts\nsolve_components.py`
- `scripts\solve_chart.py`
- `scripts\solve_chart_sequential.py`
- `scripts\solve_orientations.py`
- `scripts\try_orientations.py`
- `outputs\coldread_checks.txt`
- `outputs\derive_b_constraint.txt`
- `outputs\explore_family_R.txt`
- `outputs\hashes.sha256`
- `outputs\irreducible_check.txt`
- `outputs\nsolve_chart.txt`
- `outputs\nsolve_components.txt`
- `outputs\page_hashes.sha256`
- `outputs\solve_chart_sequential.txt`
- `outputs\solve_orientations.txt`
- `outputs\stage1.sha256`
