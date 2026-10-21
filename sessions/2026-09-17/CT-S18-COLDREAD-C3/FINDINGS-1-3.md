# FINDINGS-1-3 — CT-S18-COLDREAD-C3

Stage-1 file written before opening `packet\sealed\C3-AS-DRAFTED.md`.

## Rendered-page confirmations

- [INSPECTED] `packet\pages\vdPS_p2655.png` rendered; I saw page header "MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS" and page number 2655, the displayed family `A = z(z-1)(A_infinity + A_0/z + A_1/(z-1)) = [[a(z), b(z)], [c(z), -a(z)]]`, the sentence "q is the unique zero of c(z) and p = a(q)", and `U_0 ~= C x (C \ {0,1})`.
- [INSPECTED] `packet\pages\vdPS_p2637.png` rendered; I saw Section 3.2, the matrix form `z d/dz + A(z)` with `A(z)=A_0 + A_1 z + A_2 z^2`, and the constraint `det A_i = -theta_i^2/4 for i=0,1`.
- [INSPECTED] `packet\pages\vdPS_p2636.png` rendered; I saw the table row labelled `(0,0,1)` and the parameter line for `PV`.
- [INSPECTED] `packet\pages\companion_v12_p2.png` rendered; I saw System C printed as `(3x^2+x+1)y'' + (6x+1)y' - x^2 y = 0`.

## Task 1 — determinant constraint for printed `b(z)`

- [INSPECTED] On p. 2655 I read the printed first square in `b(z)` as `(p + 1/2 (q-1)q)^2`, i.e. with no `t`; other nearby terms contain `(q-1)qt`.
- [PROVEN] With the printed no-`t` square, the determinant residual is not identically zero:

  `det A(1) + theta_1^2/4 = -(q - 1)(t - 1)(4*p + q^2*t + q^2 - q*t - q)/4`.

- [PROVEN] The corrected entry is to replace only that square by

  `(p + 1/2 (q-1)q t)^2`.

  With this correction, `det A(1) + theta_1^2/4` simplifies/cancels/togethers to `0` identically.
- [VERIFIED] At 90-digit evaluation on two complex/rational points, the corrected residual had absolute value `0.000e+00`; the printed residuals were `4.700e-01` and `8.616e-01`. A deliberately wrong `U=t+1` variant was rejected with residuals `2.897e-01` and `2.802e+00`.

## Task 2 — hypotheses for membership in the `(0,0,1)` row

- [INSPECTED] The setup pages require the connection/module to have singularities at `0,1,infinity`, trace-free/trivial determinant data, finite determinant constraints `det A_i=-theta_i^2/4` for `i=0,1`, and row `(0,0,1)` local data; p. 2655 additionally requires the chart coordinates to lie in `U_0 ~= C x (C \ {0,1})` with `q` the unique zero of `c(z)` and `p=a(q)`.
- [STRUCTURAL] After the affine change sending the roots of `3x^2+x+1` to `z=0,1`, System C has finite singularities only at `0` and `1`; the indicial equation at each is `rho^2`, so `theta_0=theta_1=0` is the necessary finite local data.
- [STRUCTURAL] The normal-form coefficient has nonzero finite limit `11/27` at infinity, which is consistent with Katz invariant `1` rather than a regular singular infinity.
- [PROVEN] The rank-one rational Riccati obstruction check found no forced rational solution `w=1/(2z)+1/(2(z-1))+L`; the coefficient equations for `L` have no solution. The deliberate fake-`R` control was accepted, so the check is non-vacuous.
- [STRUCTURAL] Thus System C passes the broad local-data checks for the `(0,0,1)` row, but the open-chart requirement `q notin {0,1}` is not satisfied by the direct `P,Q` comparison in Task 3.

## Task 3 — chart `U_0` and `P,Q` re-substitution

- [PROVEN] From p. 2655's corrected family and the cyclic scalar equation associated to the component governed by `c(z)`, the scalar `P` coefficient is

  `P_U0 = (z^2 - 2*q*z + q)/(z*(z-q)*(z-1))`.

  System C after the same root-normalising affine change has

  `P_C = (2*z - 1)/(z*(z-1))`.

  Their exact difference is

  `P_U0 - P_C = -1/(z-q)`,

  which is not identically zero for any admissible `q in C \ {0,1}`.
- [VERIFIED] At 90-digit evaluation with `q=2/3`, the absolute `P` mismatch at `z=5/4` was `1.714e+00`; the self-comparison control was accepted.
- [STRUCTURAL] Therefore I do **not** locate System C in the affine chart `U_0` as printed on p. 2655 when comparing `P` and `Q` rather than normal-form `R` alone. A rank-1 twist/normal-form comparison may obscure this `P` mismatch; I did not establish an admissible `U_0` point separated only by a rank-1 twist.

## Computation outputs

- Main script: `scripts\coldread_checks.py`; output `outputs\coldread_checks.txt`; sha256 `122c98e8ec41561c6a61f47932ca38427f17338fc08514af3a9535177006ee51`.
- Determinant-focused script: `scripts\derive_b_constraint.py`; output `outputs\derive_b_constraint.txt`; sha256 `95b1e96ecd99e41088243a867f2e82b8d4ec16d937f6b5a44cd15215b3aa14d5`.
- Hash manifest: `outputs\hashes.sha256`.
