# REPORT.md — CT-S6-APPARENCY

Session: `sessions/2026-09-17/CT-S6-APPARENCY/`  
Baseline script/output: `apparency.py`, `apparency_results.json`, sha256 `cd26694df8db89ba96766a5c60cd57ff3a87dd98b866d3ed8c95a8bc473c717d`  
Scope-update script/output: `system_c_analysis.py`, `system_c_results.json`, sha256 `f633b05539a30c00b90b6768cf460d420c3fc9dfd1b59f7fdb5ce808cc6d2e62`  
Arithmetic: exact SymPy 1.14.0; no floating point; `dps = null`.

## What was done

STRUCTURAL: I kept the earlier System B and System A work in scope.

STRUCTURAL: After the operator's update, I amended `PREREG.md` before running new System C computations, fixing the two Remark 2.2 test polynomials as `b=x+1` and `b=x^2+1`.

INSPECTED: I inspected the companion v1.2 PDF extract, van der Put--Saito PDF pages 25--26, CT-S4, CT-S5B, CT-R1, and VQ-N1 at HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.

PROVEN: I computed exact local exponents and symbolic repeated-root log tests for System C at `s_±`, and exact infinity formal type for System C.

PROVEN: I tested two preregistered instances of Remark 2.2's general apparent-root assertion.

PROVEN: I compared System C with System B after `z=1/x` in normal form and by explicit gauge.

## System C apparency table

| point | local exponents | symbolic log test | verdict |
|---|---:|---|---|
| `s_- = (-1-i*sqrt(11))/6` | `[0,0]` | repeated-root reduction-of-order residue `1` | PROVEN: NOT APPARENT |
| `s_+ = (-1+i*sqrt(11))/6` | `[0,0]` | repeated-root reduction-of-order residue `1` | PROVEN: NOT APPARENT |

PROVEN: The companion-claimed exponent set `{0,1}` is refuted for the scalar System C tested here; the exact indicial equation at both finite roots is `lambda^2`.

PROVEN: Because the exact log residue is nonzero at both finite roots, neither finite root is apparent for the scalar System C.

## System C at infinity

PROVEN: System C has normal-form potential
`(12*x**4 + 4*x**3 + 4*x**2 + 11)/(4*(3*x**2 + x + 1)**2)`.

PROVEN: At `x=infinity`, the transformed normal-form potential has pole order `4`, hence System C is irregular unramified with Katz invariant `1` and Poincare rank `1`.

## System C Katz multiset and Table 2.1 comparison

STRUCTURAL: Removing points actually proved apparent removes no System C finite point.

STRUCTURAL: System C's effective multiset is therefore `(0,0,1)`: two regular singular finite points and one unramified Katz-1 irregular point at infinity.

INSPECTED: van der Put--Saito Table 2.1 on p.2635 / PDF page 26 has row `D5  PV  0 0 1 -  dim P 3`.

STRUCTURAL: System C's effective multiset `(0,0,1)` matches the van der Put--Saito `D5/PV` row on p.2635.

STRUCTURAL: a matching Katz multiset is necessary but not sufficient; Table 2.1 classifies families of connections, and a single fixed operator matching a row does not make it a member of that isomonodromic family until the deformation parameter is specified.

## Remark 2.2 spot tests

PROVEN: For preregistered `b=x+1`, the root `-1` has indicial equation `lambda^2`, exponents `[0,0]`, and exact log residue `1`, so the tested root is NOT APPARENT.

PROVEN: For preregistered `b=x^2+1`, the roots `±i` have indicial equation `lambda^2`, exponents `[0,0]`, and exact log residue `1`, so the tested roots are NOT APPARENT.

PROVEN: These two exact tests refute the tested form of Remark 2.2's `always apparent` assertion.

## System C versus System B / inverted System B

PROVEN: Under `z=1/x`, System B has the same normal-form potential as System C:
`(12*x**4 + 4*x**3 + 4*x**2 + 11)/(4*(3*x**2 + x + 1)**2)`.

PROVEN: The original scalar equations are not literally identical: `P_invertedB - P_C = (-6*sqrt(3)*x - 18 + sqrt(3))/(9*x)` and `Q_invertedB != Q_C`.

PROVEN: If `Y(x)=y_B(1/x)`, then the normal-form gauge from inverted System B to System C is
`y_C(x)=x**(sqrt(3)/18 - 1)*exp(-sqrt(3)*x/3)*Y(x)`.

STRUCTURAL: System C and inverted System B are therefore the same in normal form after `z=1/x`, but the gauge is multivalued at `x=0`, so scalar-operator apparency/monodromy statements must specify the gauge convention.

## System B retained results

PROVEN: For System B at `rho_- = (-1-i*sqrt(11))/2`, the indicial equation is `lambda^2`, exponents are `[0,0]`, and the exact repeated-root log residue is `1`; verdict NOT APPARENT.

PROVEN: For System B at `rho_+ = (-1+i*sqrt(11))/2`, the indicial equation is `lambda^2`, exponents are `[0,0]`, and the exact repeated-root log residue is `1`; verdict NOT APPARENT.

PROVEN: For System B at infinity, local exponents are `1 - sqrt(3)/18` and `2 - sqrt(3)/18`; verdict NOT APPARENT because they are not integers.

STRUCTURAL: No apparent points are removed from System B, so its effective multiset remains `(1,0,0,0)`, which does not match the van der Put--Saito `D5/PV` row `(0,0,1,-)`.

## System A dash-slot justification

PROVEN: For System A, finite affine singular candidates outside `z=0` are NOT FOUND in `A2=3*z^3` and denominator factorization by exact SymPy solve at HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.

PROVEN: System A has pole order `3` at `z=0` and pole order `3` at `infinity`, hence Katz multiset `(1/2,-,1/2)`.

PROVEN: The `-` slot means an absent singular point in the classification tuple, not a point dropped as regular or apparent.

## Falsifiers

PROVEN: F5 fired: System C finite exponents are `[0,0]`, not `{0,1}`.

PROVEN: F6 did not fire: no System C finite point was classified APPARENT.

PROVEN: F7 did not fire: System C infinity has pole order `4` and Katz/Poincare rank `1`.

PROVEN: F8 did not fire: the System C and inverted System B normal-form difference is exactly `0`.

## Claims

INSPECTED: S6-C1 — CT-R1 `CLASSIFICATION-TABLE.md` and van der Put--Saito PDF pages 25--26 were inspected; the D5/PV Table 2.1 row is `(0,0,1,-)` on p.2635 and the selection rule is on p.2634.

INSPECTED: S6-C2 — VQ-N1's `verdict.md` line recording two apparent Fuchsian points with indices `[0,0]` was inspected.

PROVEN: S6-C3 — System B transcription reproduces the stated `q2` factorization and normal-form `r` exactly.

PROVEN: S6-C4 — System B `rho_-` is NOT APPARENT.

PROVEN: S6-C5 — System B `rho_+` is NOT APPARENT.

PROVEN: S6-C6 — System B infinity is NOT APPARENT.

STRUCTURAL: S6-C7 — System B's effective multiset `(1,0,0,0)` does not match the D5/PV row `(0,0,1,-)`.

PROVEN: S6-C8 — System A finite affine candidates outside `z=0` are NOT FOUND by exact factorization; infinity is the second Katz-`1/2` entry.

PROVEN: S6-C9 — System A's dash slot means an absent singular point, not a dropped regular/apparent point.

STRUCTURAL: S6-C10 — Matching a row would still be necessary but not sufficient for family membership without a deformation parameter.

INSPECTED: S6-C11 — The companion v1.2 PDF was inspected; Conjecture 4.1, Remark 2.2, and System C equation tokens were found in extracted pages.

PROVEN: S6-C12 — System C is in self-adjoint form because `b(x)=a'(x)` exactly.

PROVEN: S6-C13 — System C `s_-` has exponents `[0,0]`, nonzero log residue, and is NOT APPARENT.

PROVEN: S6-C14 — System C `s_+` has exponents `[0,0]`, nonzero log residue, and is NOT APPARENT.

PROVEN: S6-C15 — System C infinity is unramified Katz/Poincare rank `1`.

STRUCTURAL: S6-C16 — System C's effective multiset `(0,0,1)` matches the van der Put--Saito `D5/PV` row on p.2635.

PROVEN: S6-C17 — The two preregistered Remark 2.2 test polynomials produce NOT APPARENT roots and refute the tested `always apparent` assertion.

PROVEN: S6-C18 — System C and inverted System B have identical normal form under `z=1/x`, with explicit gauge factor `x**(sqrt(3)/18 - 1)*exp(-sqrt(3)*x/3)`.

STRUCTURAL: S6-C19 — The companion's `beta=gamma=0` explanation via apparent finite singularities is not supported by the scalar System C apparency test here.

## What was NOT established

STRUCTURAL: I did not establish System C membership in the D5/PV isomonodromic family; only the necessary Katz-row match was established.

STRUCTURAL: I did not reconcile the companion's finite-apparency assertion with the exact scalar log-term test.

STRUCTURAL: I did not determine whether a different connection-level gauge convention makes the finite points apparent.

STRUCTURAL: I did not edit Conjecture 4.1 or any file outside this session folder.

## Open questions for the operator

CONJECTURED: Is apparency intended for the scalar operator exactly as printed, or for a gauge-equivalent connection where the finite monodromy is quotiented differently?

CONJECTURED: Should the companion's Theorem/Conjecture wording be audited separately against the exact scalar exponents/log terms?

CONJECTURED: Should future classification use System C's normal form rather than System B's original `z` coordinate operator?

## Uncommitted files created in this session folder

STRUCTURAL: Files created here are:

- `sessions/2026-09-17/CT-S6-APPARENCY/PREREG.md`
- `sessions/2026-09-17/CT-S6-APPARENCY/apparency.py`
- `sessions/2026-09-17/CT-S6-APPARENCY/apparency_results.json`
- `sessions/2026-09-17/CT-S6-APPARENCY/claims.jsonl`
- `sessions/2026-09-17/CT-S6-APPARENCY/git-status-uall.txt`
- `sessions/2026-09-17/CT-S6-APPARENCY/pdf_pages_25_26_extract.txt`
- `sessions/2026-09-17/CT-S6-APPARENCY/run.log`
- `sessions/2026-09-17/CT-S6-APPARENCY/system_c_analysis.py`
- `sessions/2026-09-17/CT-S6-APPARENCY/system_c_results.json`
- `sessions/2026-09-17/CT-S6-APPARENCY/system_c_run.log`
- `sessions/2026-09-17/CT-S6-APPARENCY/vquad_resurgence_v1.2_relevant_extract.txt`
- `sessions/2026-09-17/CT-S6-APPARENCY/REPORT.md`

INSPECTED: Final git status check reports HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`; it also reports pre-existing dirty/untracked entries outside this session folder, listed in `git-status-uall.txt`.
