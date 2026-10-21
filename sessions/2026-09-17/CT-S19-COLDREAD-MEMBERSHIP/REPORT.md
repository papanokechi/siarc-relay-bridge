# REPORT

## Scope and isolation

[STRUCTURAL] Work was confined to `C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S19-COLDREAD-MEMBERSHIP\`; I did not read sibling session folders, git history, git diffs, or adjudication files.

## What was done

[VERIFIED] `PREREG.md` was written before computation, and the vacuity pre-check was run before membership computations.

[PROVEN] I derived both scalar reductions of a rank-2 trace-free system by elimination and used the first-component reduction for System C because its coefficient comparison is structurally the one matched by the scalar dependent variable.

[PROVEN] I normalized System C by mapping its finite singular points to `z=0,1`, corrected the given vdPS typo in `b(z)`, and found a U0 point whose first-component scalar reduction equals System C.

[VERIFIED] The decisive coefficient comparison checked both `P` and `Q`, not only normal form `R`; maximum high-precision coefficient residual was `1.1018116139846136e-280` at 90 dps.

[VERIFIED] Independent local system residuals using `Y'=NY` and `Y''=(N'+N^2)Y` over 9 point/vector tests had maximum `4.0132614818846019e-208` at 100 dps.

[STRUCTURAL] vdPS row hypotheses for `(0,0,1). PV` are satisfied by the trace-free local formal data, except monodromy coordinate/nonvanishing data remains undecided because monodromy/Stokes matrices were not in the packet and were not computed.

[STRUCTURAL] The sealed sentence verdict is `CORRECT WITH WORDING CHANGE`; the local type, U0 membership, and `t=∓2i√33/9` clauses are supported, but the isomonodromic-leaf phrase should avoid implying an independently identified leaf.

## Claims

[STRUCTURAL] Machine-readable claims are in `claims.jsonl` with prefix `S19-`.

## What was not established

[STRUCTURAL] I did not compute monodromy matrices, Stokes matrices, or the specific monodromy-space coordinates `(s1,s2,s3)`.

[STRUCTURAL] I did not establish a specific isomonodromic leaf by independent monodromy/Stokes computation.

[STRUCTURAL] I did not prove uniqueness of the U0 point globally over all branch/orientation choices; I exhibited and verified one exact representative and noted the conjugate/reversed choice.

## Open questions for the operator

[CONJECTURED] If the governance process requires leaf-level membership, the next step is an independent monodromy/Stokes computation for System C and comparison with the vdPS monodromy coordinates.

[CONJECTURED] If wording must distinguish de Rham moduli from monodromy moduli, use the replacement sentence in `VERDICT-5.md`.

## Deliverables and uncommitted files created/updated

[VERIFIED] Top-level deliverables: `PREREG.md`, `FINDINGS-1-4.md`, `outputs\stage1.sha256`, `VERDICT-5.md`, `claims.jsonl`, `REPORT.md`.

[VERIFIED] Scripts: `scripts\vacuity_precheck.py`, `scripts\membership_symbolic.py`, `scripts\dump_equations.py`, `scripts\derive_fast.py`, `scripts\solve_pq.py`, `scripts\solve_pk.py`, `scripts\solve_corrected.py`, `scripts\check_coeffs.py`, `scripts\point_values.py`, `scripts\check_hypotheses.py`, `scripts\verify_membership.py`.

[VERIFIED] Outputs: `outputs\vacuity_precheck.txt`, `outputs\membership_symbolic.txt`, `outputs\dump_equations.txt`, `outputs\derive_fast.txt`, `outputs\solve_pq.txt`, `outputs\solve_pk.txt`, `outputs\solve_corrected.txt`, `outputs\check_coeffs.txt`, `outputs\point_values.txt`, `outputs\check_hypotheses.txt`, `outputs\verify_membership.txt`, `outputs\page_inspection.txt`, `outputs\hashes.txt`, `outputs\top_hashes.txt`.
