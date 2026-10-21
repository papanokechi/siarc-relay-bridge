# CT-S13-COLDREAD5 Report

## 0. Scope, isolation, and HEAD

- Branch at start: `log-pv-01`.
- HEAD at start: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.
- Branch at end: `log-pv-01`.
- HEAD at end: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.
- Work directory: `sessions/2026-09-17/CT-S13-COLDREAD5/`.

I read only the packet, the two named rendered page images, the named PDF, and my own CT-S13 deliverables under `sessions/2026-09-17/`. I did not open the other cold packets, audit/report/draft/verify files, classification markdown, source claims files, or other session folders.

Scripts and outputs:

- `compute_system_a.py` -> `compute_system_a.out`, SHA-256 `610b420f55d319204bc8397ffadf8123e7368c8eed0419dbaa5f04f64846d090`.
- `source_hashes.py` -> `source_hashes.out`, SHA-256 `549f410d47fde7a7ad737ed7a7206f8fec49d0bce3b9a03d1476d3b87d2caf87`.

Source-file hashes recorded in `source_hashes.out`:

- `vdps_p2634.png`: `84b9dfc95b00d64c28ecb80a9477e64f07b44164b7db45bad8de819cb61ab9d0`.
- `vdps_p2635.png`: `56194f2639b0aa20d6e96863373e92ee599165e357b6b4b8c9221474b070da6b`.
- PDF: `1666bd6be824a99fc0b48adbe48233a9b2a520fd7e8adf187e98d22525473605`.

## 1. Published table and column meanings

From the rendered page image for journal p. 2635, the printed caption is:

> Table 2.1. Classification of Families

The table headings on p. 2635 are:

> Dynkin | Painlevé equation | r(0) | r(1) | r(∞) | r(t) | dim P

From the surrounding text on journal p. 2634:

> We consider a local family M(u) of differential modules, represented by a matrix equation d/dz + A(z,u) where A(z,u) is a 2 x 2-matrix with trace 0 and u lies in a small polydisk D around 0.

The same page says:

> A singular point p with Katz invariant r(p) contributes to the fibre the dimension r(p) if r(p) in Z>=0 and r+(p) = 1/2 + r(p) if r(p) in 1/2 + Z>=0.

It also says:

> Columns 3-6 of the next table present the ten resulting cases.

and:

> The space R is mapped to a space of parameters P (related to the parameters spaces of the Painlevé equations) consisting of traces or eigenvalues of the matrices involved in the construction of R.

Thus `r(0), r(1), r(∞), r(t)` are the Katz invariants at the corresponding possible singular points; a dash denotes that this point is absent in that case. `dim P` is the dimension of the parameter space `P`, not a count of individual scalar operators.

Rows used, transcribed from the rendered p. 2635 image of Table 2.1:

> D̃5 | PV | 0 | 0 | 1 | - | 3

> D̃6 | PIII(D6) | 1 | - | 1 | - | 2

> D̃8 | PIII(D8) | 1/2 | - | 1/2 | - | 0

## 2. Q1: Verify (A0)

The script generated `Q_n` exactly from `Q_-1=0`, `Q_0=1`, `Q_n=(3n^2+n+1)Q_(n-1)+Q_(n-2)`. It obtained:

`Q[0..10] = [1, 5, 76, 2361, 125209, 10144290, 1166718559, 180851520935, 36352322426494, 9197318425423917, 2860402382629264681]`.

Substitution into

`3z^3 f'' + 10z^2 f' + (z^2+5z-1)f = -1`

was checked by computing `3z^3 f'' + 10z^2 f' + (z^2+5z-1)f + 1`. All coefficients `z^0` through `z^30` are zero; with the chosen truncation, all safe coefficients through `z^43` are zero.

Verdict Q1: **SOUND**.

## 3. Q2: Verify (A1)

I used the normal-form convention

`y'' + p y' + q y = 0`, set `y = u exp(-1/2 ∫p dz)`, giving `u'' = r u` with

`r = p^2/4 + p'/2 - q`.

For `L_A`,

- `p = 10/(3z)`,
- `q = (z^2+5z-1)/(3z^3)`,
- `r_A = (-3z^2 - 5z + 3)/(9z^3)`.

This is exactly (A1) under this convention.

Verdict Q2: **SOUND**.

## 4. Q3: Verify (A2) and (A3)

At `z=0`, `r_A` has denominator `9z^3` and nonzero leading coefficient `1/3`; pole order is `3`. For a rank-2 scalar normal form `u''=r u`, pole order `m>2` gives Katz invariant `(m-2)/2`; if `m` is odd, the exponential parts are ramified and the ramification index is `2`. Hence at `0` the Katz invariant is `1/2`, ramification index `2`, and exponential parts are

`exp(∓ 2/sqrt(3) z^(-1/2))`.

There are no other finite singular points because the only finite pole of `p` and `q`, equivalently of `r_A`, is at `z=0`.

At infinity I used `t=1/z`. For `u''=r(z)u`, the transformed normal-form potential is

`R_inf(t) = t^(-4) r(1/t) = (3t^2 - 5t - 3)/(9t^3)`.

This has pole order `3` at `t=0`, leading coefficient `-1/3`, Katz invariant `1/2`, and ramification index `2`. The exponential parts are

`exp(∓ 2i/sqrt(3) t^(-1/2))`.

Verdict Q3: **SOUND**.

## 5. Q4: Verify (A5), the quadratic cover

For `z=w^2`, the normal-form equation pulls back as

`Y'' - (1/w)Y' - 4w^2 r(w^2)Y = 0`.

Renormalizing to scalar normal form gives

`R_w = 3/(4w^2) + 4w^2 r(w^2) = -(48w^4 + 53w^2 - 48)/(36w^4)`.

At `w=0`, pole order is `4`, leading coefficient `4/3`, Katz invariant `(4-2)/2 = 1`, and the singularity is unramified because the pole order is even. At `w=∞`, with `t=1/w`,

`R_{w,∞}(t) = t^(-4) R_w(1/t) = (48t^4 - 53t^2 - 48)/(36t^4)`,

again pole order `4`, leading coefficient `-4/3`, Katz invariant `1`, and unramified. Thus the cover doubles the two Katz invariants from `1/2` to `1` and removes the quadratic ramification.

Verdict Q4: **SOUND**.

## 6. Q5: Check table lookups (A4) and (A5)

The original system has singular points at `0` and `∞` only, so in the table's order `(r(0), r(1), r(∞), r(t))` its data are `(1/2, -, 1/2, -)`. On journal p. 2635, Table 2.1 contains the row:

> D̃8 | PIII(D8) | 1/2 | - | 1/2 | - | 0

So the lookup in (A4) matches the printed D̃8 / PIII(D8) row. The claimed three-entry notation `(1/2, -, 1/2)` is a shorthand omitting the final `r(t)=-`; it is compatible with the table only if read in the table order as `(r(0), r(1), r(∞))` with `r(t)` also absent.

For the quadratic cover, the table-order data are `(1, -, 1, -)`. On journal p. 2635, Table 2.1 contains the row:

> D̃6 | PIII(D6) | 1 | - | 1 | - | 2

So the lookup in (A5) matches the printed D̃6 / PIII(D6) row. The dash entries correspond to absence of singularities at `1` and `t`, as the claim assumes.

Verdict Q5: **SOUND WITH CAVEAT** because the arithmetic lookup is correct, but the claimed “multiset” notation suppresses the full four table columns and should be read with the table's ordered-column convention.

## 7. Q6: Critical assessment of (A6)

The row match is a necessary classification datum for the listed Painlevé-type families, not by itself a sufficient proof that this particular scalar operator belongs to the corresponding family.

The paper says on p. 2634 that it considers:

> a local family M(u) of differential modules, represented by a matrix equation d/dz + A(z,u) where A(z,u) is a 2 x 2-matrix with trace 0

and the caption on p. 2635 is:

> Table 2.1. Classification of Families

Thus the table classifies families of rank-2 trace-zero connections/differential modules and their monodromy/parameter data, not arbitrary individual scalar differential operators merely because their Katz invariants match a row.

The table's `dim P` for the PIII(D8) row is `0`. That means the corresponding parameter space `P` has dimension zero in this classification. It does not mean that every fixed rank-2 object with Katz data `(1/2, -, 1/2, -)` is automatically the particular family used later in the paper, nor does it turn a necessary row match into a sufficient membership criterion.

There is also a scalar-versus-connection gap. `L_A` is a scalar second-order operator. It determines a rank-2 differential module by the usual companion/cyclic-vector construction; in companion form the connection has trace `-p`, and passing to trace-zero normal form requires a scalar gauge/twist equivalent to removing the first-derivative term. Such regular twists/gauges should not change the irregular Katz slopes, but the actual rank-2 trace-zero connection, determinant condition, irreducibility, singular set, and any required strong Riemann-Hilbert condition would have to be checked. This is especially relevant because p. 2634 says:

> For a differential module M corresponding to one of the types, the strong Hilbert-Riemann problem has a positive answer, except possibly for (1/2, -, 1/2) and (-, -, 5/2) ... For these two types we only consider the modules M(u) for which the strong Riemann-Hilbert problem does have a positive answer.

The `(1/2, -, 1/2, -)` case is exactly the D̃8 / PIII(D8) row. The packet's chain does not check that extra condition.

Verdict Q6: **ERROR** for the strong conclusion “therefore the object sits in the PIII(D8) row” if this is meant as sufficient family membership. It is only justified as a Katz-data row match, subject to the scalar-to-connection and strong-Riemann-Hilbert checks.

## 8. Q7: Overall verdict and D̃5 / PV sentence

- (A0)–(A3): exact computation supports them.
- (A4) and (A5): table row lookups are correct as ordered Katz-data matches.
- (A6): overstates what the table lookup proves. The published table is a classification of families of rank-2 connections/differential modules; a row match is not alone sufficient to prove family membership of a specific scalar operator.

Overall verdict on the chain: **SOUND WITH CAVEAT up to the table lookup; ERROR for the sufficiency/family-membership inference in (A6)**.

The final sentence “neither is D̃5 / PV” is **SOUND WITH CAVEAT** at the level of the computed Katz data and the direct quadratic pullback: Table 2.1 p. 2635 lists

> D̃5 | PV | 0 | 0 | 1 | - | 3

which does not match `(1/2, -, 1/2, -)` or `(1, -, 1, -)`. It is not, by itself, a complete statement about all possible transformations or embeddings into Painlevé-type families.
