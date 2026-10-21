# CT-S15-COLDREAD-DEFERRED REPORT

Session: CT-S15-COLDREAD-DEFERRED

Repository HEAD at start: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.
Repository HEAD at end: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.
HEAD unchanged: yes.

Isolation statement: I read the packet, the five permitted page images, and my own deliverables only. I did not open the forbidden prior-session files listed in the packet.

Source sha256 values:

- `PACKET-E-deferred.md`: `2bd36257f68cc38f9ed0ebf934bd5a56bae22419feec4d59143252de1b314804`
- `vdps_p2634.png`: `84b9dfc95b00d64c28ecb80a9477e64f07b44164b7db45bad8de819cb61ab9d0`
- `vdps_p2635.png`: `56194f2639b0aa20d6e96863373e92ee599165e357b6b4b8c9221474b070da6b`
- `jimbo_p1152.png`: `84f548ceadd8d4a0e2d2f618b0bc384190bdfd9331c1138dd004ba9faa2cd2b5`
- `companion_v12_p2.png`: `5ecb9f5d10af1f45a05b7c2a60f1fc2d12ca79adf75f4cfc417adb6561261b7c`
- `companion_v12_p3.png`: `7393d63dbff7cbb8ce49596ea2f0e1376c885c556a1da9bf3b08b6c65cf16f66`

## Task 1 — what `P` is

INSPECTED: On van der Put--Saito p. 2634, the page says: "The local Riemann-Hilbert map RH : D -> R forgets the formal data, namely the position of the set of singular points S and the coefficients of the eigenvalues at the irregular singular points."

INSPECTED: On van der Put--Saito p. 2634, the page defines `P` for this setup: "The space R is mapped to a space of parameters P (related to the parameters spaces of the Painleve equations) consisting of traces or eigenvalues of the matrices involved in the construction of R."

INSPECTED: On van der Put--Saito p. 2635, the page says: "It turns out that R -> P is a family of affine cubic surfaces."

## Task 2 — meaning of `dim P = 0`

INSPECTED: On van der Put--Saito p. 2635, Table 2.1 is headed "Classification of Families" and has columns including "Painleve equation" and "dim P"; the `PIII(D8)` row has `dim P` equal to `0`.

STRUCTURAL: In this source, `dim P = 0` means the parameter space `P` for the corresponding monodromy/cubic-surface family is zero-dimensional. This supports the statement's "no free parameters" wording if "parameters" means the authors' `P`, i.e. traces/eigenvalues/Painleve-equation parameters; it is not a statement that there is no deformation variable.

## Task 3 — relation to isomonodromic time and the table's `t`

INSPECTED: On van der Put--Saito p. 2634, the page describes the table entries as singular-point data: for example, "#S = 4, then S = {0,1, oo,t}, only regular singular points"; and it says "A singular point p with Katz invariant r(p) contributes to the fibre...".

INSPECTED: On van der Put--Saito p. 2635, after Table 2.1, the page says: "We will also describe the corresponding one-dimensional families of differential modules M(t)."

STRUCTURAL: The `r(t)` table column is a Katz-invariant column for a singular point labelled `t` when such a point is present, not by itself the isomonodromic deformation time. The same letter is later used in `M(t)` for the one-dimensional differential-module family. Therefore `dim P = 0` does not, from this table, negate the existence of a one-dimensional deformation direction.

## Task 4 — expected or anomalous

STRUCTURAL: The PIII(D8) `dim P = 0` entry is expected within the source's own construction: the row is one of the "ten resulting cases" produced by the stated fibre-dimension requirement, and the text presents it as part of the classification rather than as an exception or defect.

## Task 5 — verdict on Statement 1

STRUCTURAL: Verdict: **CORRECT WITH WORDING CHANGE**. Suggested change: replace "`P` is the parameter space of the family" with "`P` is the authors' space of trace/eigenvalue parameters for the monodromy/cubic-surface family, related to the Painleve parameter space." With that precision, the rest is supported by the permitted pages.

## Task 6 — Jimbo system `(3.1)` and required data

INSPECTED: On Jimbo p. 1152, system `(3.1)` is read from the page as

```text
partial_x Y = (A_0(t)/x + A_t(t)/(x-t) + (1/2) sigma_3) Y,
partial_t Y = - A_t(t)/(x-t) Y.
```

INSPECTED: On Jimbo p. 1152, the page says: "We set the eigenvalues of A_v(t)= +/- theta_v/2 (v=0,t)" and gives the diagonal of `A_0(t)+A_t(t)` in terms of `theta_infty`.

INSPECTED: On Jimbo p. 1152, the page states that a scalar function built from entries of `A_0(t)` and `A_t(t)` "satisfies (PV) with the parameters" including `alpha = (theta_0 - theta_t + theta_infty)^2/8`, `beta = -(theta_0 - theta_t - theta_infty)^2/8`, `gamma = 1 - theta_0 - theta_t`, and `delta = -1/2`.

INSPECTED: On Jimbo p. 1152, the standing assumption line is read as `(A1)_PV` with non-integrality of the theta parameters (`theta_infty`, `theta_0`, `theta_t`). The OCR retained the line imperfectly, so I do not use the exact typography of that line beyond the non-integrality requirement.

STRUCTURAL: To be an instance of `(3.1)`, an operator must supply a two-by-two matrix connection with matrices `A_0(t)` and `A_t(t)`, the irregular term `(1/2) sigma_3`, the singular points `x=0` and `x=t`, the eigenvalue/diagonal theta data, and the deformation equation `partial_t Y = -A_t(t)/(x-t)Y`. In this system, `t` is both the moving finite singular point and the deformation variable.

## Task 7 — whether the companion scalar local data suffice

INSPECTED: On companion p. 2, the operator is given as `a(x)y'' + b(x)y' + c(x)y = 0`, with `a(x)=3x^2+x+1`, `b(x)=6x+1`, and `c(x)=-x^2`.

INSPECTED: On companion p. 2, the page says the ODE has "exactly two finite regular singular points" at `s_{1,2}=(-1 +/- i sqrt(11))/6` and "one irregular singular point of Poincare rank 1 at x = infinity".

VERIFIED: `companion_local_data_check.py` verifies symbolically that `b(x)-a'(x)=0` and numerically at 100 dps with maximum residual `0.0`; it verifies finite roots `-1/6 +/- sqrt(11) I/6`, discriminant `-11`, finite indicial equation `rho^2`, and `lim_{x->infinity} c(x)/a(x)=-1/3`.

STRUCTURAL: These scalar local data match only a coarse confluent-Heun/PV-type singularity pattern. They do not provide Jimbo matrices `A_0(t), A_t(t)`, a deformation-dependent family, the second equation of `(3.1)`, theta data satisfying Jimbo's dictionary and assumption, or a scalar-to-matrix gauge/coordinate construction identifying `x=0` and `x=t` with the companion singularities.

STRUCTURAL: Therefore the scalar local data alone do not exhibit a Jimbo Lax embedding and do not exhibit a Painleve V deformation time. What is missing is an explicit `t`-dependent two-by-two Lax pair satisfying both equations of `(3.1)` and its parameter dictionary.

## Task 8 — verdict on Statement 2

STRUCTURAL: Verdict: **CORRECT**.

## Could not establish / open questions

INSPECTED: I could not establish from the permitted companion pages an explicit Jimbo `A_0(t), A_t(t)` pair, compatibility calculation, or deformation time for the companion operator. The companion page itself says explicit HeunC parameters require a coordinate change and gauge transformation and that their derivation is omitted.

INSPECTED: The exact printed typography of Jimbo's `(A1)_PV` line was not fully recovered by OCR, but the non-integrality role of the theta parameters is clear enough for the structural conclusion above.

## Produced files

- `REPORT.md`
- `claims.jsonl`
- `companion_local_data_check.py`
- `companion_local_data_check.out.txt`
- `ocr_allowed_sources.py`
- `ocr_allowed_sources.out.txt`
- `ocr_allowed_sources.ps1`
- `ocr_jimbo_top_variants.py`
- `ocr_jimbo_top_variants.out.txt`
- `ocr_jimbo_lower_variants.py`
- `ocr_jimbo_lower_variants.out.txt`
- `OUTPUT_HASHES.txt`
