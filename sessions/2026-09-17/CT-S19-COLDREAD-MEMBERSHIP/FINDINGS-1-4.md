# FINDINGS-1-4

## Task 1: component question

[PROVEN] For a trace-free rank-2 system `Y'=N Y`, `N=[[a,b],[c,-a]]`, the first component `y=Y_1` satisfies
`y'' + P_1 y' + Q_1 y=0`, where `P_1=-(b'/b)` and `Q_1=-(a' + b c - a b'/b + a^2)`.

[PROVEN] The second component `y=Y_2` satisfies `y'' + P_2 y' + Q_2 y=0`, where `P_2=-(c'/c)` and `Q_2=-((-a)' + b c + a c'/c + a^2)`.

[STRUCTURAL] Therefore a scalar equation must be compared against the scalar reduction for the component that is its dependent variable; switching components changes the logarithmic derivative term from `b'/b` to `c'/c`, so the two reductions are generally inequivalent.

[INSPECTED] `vdPS_p2655.png` rendered; I saw the displayed U0/family matrices and the text saying the first basis vector is chosen as cyclic vector and that `q` is the unique zero of `c`.

[STRUCTURAL] Since `q` is read from the lower-left entry `c`, it bears on the second-component reduction (`P_2` has the `c'/c` term), not on the first-component comparison unless the scalar variable is structurally identified with the second component.

## Task 2: locating System C

[PROVEN] The finite singular points of `(3x^2+x+1)y''+(6x+1)y'-x^2 y=0` are `alpha=(-1+sqrt(-11))/6` and `beta=(-1-sqrt(-11))/6`; with `x=alpha+(beta-alpha)z`, they map to `z=0,1` and the normalized equation is `y'' + ((2z-1)/(z(z-1))) y' + Q_C y=0`, `Q_C= -(-1+sqrt(-11)(1-2z))^2/(108 z(z-1))`.

[INSPECTED] `vdPS_p2655.png` rendered; I saw the printed `b(z)` square with the known missing `t`; the corrected expression includes the missing `t`.

[PROVEN] The one-line determinant check gives `det(A0_corrected)+theta0^2/4 = 0`, while the printed omission gives `-q*(q*t - q - t + theta_inf + 1)*(4*p + q^2*t + q^2 - q*t + q*theta_inf - q)/4`, not identically zero.

[PROVEN] A point in U0 exists for the first-component scalar reduction. One exact representative is:
`t=2*sqrt(33)*I/9`, `theta_inf=-2+sqrt(3)/9`, `theta0=theta1=0`,
`q=1/2 - 70425*sqrt(33)*I/30602 - 457937*sqrt(11)*I/122408`,
`p=5*(156636384689044*sqrt(33)+271939598721024*sqrt(11)+46172647864885092*I+26659773733835227*sqrt(3)*I)/(371497152*(457937*sqrt(11)+281700*sqrt(33)-61204*I))`.

[VERIFIED] Substitution comparing both normalized coefficients gives `P_1-P_C=0` symbolically and `Q_1-Q_C=0` after `cancel/radsimp`; numeric residuals at 90 dps over 6 points have maximum `1.1018116139846136e-280` (`outputs/verify_membership.txt`, hash `0EFAAD8485514DBE7F15C69DEE1CD0C8ACDDA33D0DCF224AEEDB07C1FE005A04`).

[PROVEN] The second-component reduction is not System C: `P_2-P_C` equals a nonzero rational radical expression displayed in `outputs/verify_membership.txt`.

## Task 3: independent control

[VERIFIED] The preregistered vacuity pre-check failed on a deliberately wrong `Q` shift by `1/7`, residual `0.142857142857... > 1e-3` (`outputs/vacuity_precheck.txt`, hash `6E82D411BED700B92B4DCDD282FF7F1E5543F50F7AEE359F38CDB49BDD079DF0`).

[VERIFIED] A local numerical system route evaluated `Y'=NY`, `Y''=(N'+N^2)Y` for 3 ordinary points and 3 independent values of `Y(z)`; batch counts were in=9/out=9, dps=100, maximum residual `4.0132614818846019e-208` (`outputs/verify_membership.txt`).

[VERIFIED] The wrong-component control at the same sample points produced maximum `|P_2-P_C|=0.0390174438931215 > 1e-3`, so the control can fail.

## Task 4: hypotheses for the (0,0,1) row

[INSPECTED] `vdPS_p2636.png` rendered; I saw the row headed `(0,0,1). PV.` with `d/dz + A0/z + A1/(z-1) + t/2*(-1 0; 0 1), all tr(A_*)=0`.

[INSPECTED] On the same rendered page I saw the monodromy equation and `with s1, s2 in C, s3 in C*`.

[STRUCTURAL] System C's trace-free normal form has finite regular singularities at `z=0,1`, an irregular rank-1 singularity at infinity, `R` double coefficients `-1/4` at both finite points, and `t^2=-44/27`, matching the `(0,0,1)` pattern (`outputs/check_hypotheses.txt`, hash `2594720597D6E1491A94BD7FDA4593F7FC26DED83F7FE50069A5D663550D39EC`).

[STRUCTURAL] Hypothesis status: PV row SATISFIED; connection shape SATISFIED after affine normalization and trace-free gauge; `all tr(A_*)=0` SATISFIED by the trace-free form; finite residues SATISFIED with `theta0=theta1=0`; infinity rank-1/t nonzero SATISFIED since `t^2=-44/27`; monodromy-space coordinate nonvanishing `s3 in C*` is UNDECIDED because the packet does not provide monodromy matrices for System C.

## Counts and hashes

[VERIFIED] Script/output hashes are recorded in `outputs/hashes.txt`; batch operations reported counts in and out in their outputs.
