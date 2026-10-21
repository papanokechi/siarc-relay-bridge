# REPORT — CT-S9-PVPARAMS

## Governance

INSPECTED — Work was confined to `sessions\2026-09-17\CT-S9-PVPARAMS\`. No commits, pushes, tags, PRs, deposits, or submissions were made. INSPECTED — HEAD at the required check is `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.

## What was done

INSPECTED — I wrote `PREREG.md` before symbolic computation, fixing the Painleve V equation convention and the local-data-to-parameter dictionary.

INSPECTED — PV equation convention used: DLMF Eq. 32.2.5, fetched to `refs\DLMF_32.2.E5.tex`, sha256 `613250E4AC93F60736348BBE063D535D3E3E790D7F7689E885483E043ED4943F`.

INSPECTED — PV Lax/dictionary convention used: Jimbo, "Monodromy Problem and the Boundary Condition for Some Painleve Equations," p. 1152, fetched to `refs\jimbo_1982_prims.pdf`, sha256 `255D4F079767FB050CB462DC91204AFAF09507BBA74789ADE1DA10DCE4F18815`. The page image used for inspection is `outputs\jimbo_page16-16.png`.

INSPECTED — The quoted Jimbo dictionary is:

```text
α = 1/8 (θ_0 - θ_t + θ_∞)^2,   β = -1/8 (θ_0 - θ_t - θ_∞)^2,
γ = 1 - θ_0 - θ_t,             δ = -1/2.
```

INSPECTED — van der Put-Saito Table 2.1 was inspected from the repo PDF extraction `outputs\vdp_pages24-28.txt`; it contains the D5/PV row with Katz invariants `(0,0,1)`.

## Symbolic recomputation of System C

PROVEN — The script `scripts\compute_system_c_local_data.py` produced `outputs\system_c_symbolic_local_data.json`, sha256 `2909D84BEACB1DC71B4310037D78F1A2174345074A580247AD73E927651C8D91`; all computations are exact SymPy expressions, no floats.

PROVEN — `b-a' = 0`, so System C is exactly self-adjoint: `d/dx[a(x)y'] + c(x)y = 0`.

PROVEN — The finite singular points are `-1/6 - sqrt(11)*I/6` and `-1/6 + sqrt(11)*I/6`.

PROVEN — At both finite singularities, `p0=1`, `q0=0`, and the scalar indicial polynomial is `lambda**2`; the local scalar exponents are `{0,0}` and the exponent difference is `0`.

PROVEN — The second Frobenius solution has a nonzero logarithmic coefficient: `sqrt(11)*I/11` at `-1/6 - sqrt(11)*I/6`, and `-sqrt(11)*I/11` at `-1/6 + sqrt(11)*I/6`, normalized by `y1(s)=1`.

STRUCTURAL — Therefore the finite singularities are not apparent; their local monodromy is unipotent and non-trivial.

PROVEN — The normal-form potential is `(12*x^4 + 4*x^3 + 4*x^2 + 11)/(4*(3*x^2+x+1)^2)`.

PROVEN — At both finite singularities the coefficient of `(x-s)^-2` in the normal-form potential is `-1/4`, giving repeated normal-form exponent `1/2`.

PROVEN — In `t=1/x`, the normal-form potential has pole order `4` at `t=0`, leading coefficient `1/3`, no fractional-power ramification, and Katz invariant `1`.

PROVEN — The scalar normal-form exponential factors at infinity begin `exp((sqrt(3)/3)*x)` and `exp((-sqrt(3)/3)*x)`, equivalently `exp(-(sqrt(3)/3)/t)` and `exp((sqrt(3)/3)/t)`. The Riccati log coefficients are recorded in the JSON output.

## Translation to PV parameters under the quoted convention

STRUCTURAL — The translation script `scripts\translate_jimbo_constraints.py` produced `outputs\jimbo_parameter_constraints.json`, sha256 `CECDE2120533FEF1EDA5D0176F868CD355D2239A4AA8ED1F50600A864A5DE328`.

STRUCTURAL — If the two finite scalar exponent differences of System C are identified with Jimbo's finite residue eigenvalue differences, then `θ_0=0` and `θ_t=0`.

STRUCTURAL — Substituting `θ_0=θ_t=0` into Jimbo's dictionary gives:

```text
α = θ_∞^2/8,
β = -θ_∞^2/8,
γ = 1,
δ = -1/2.
```

STRUCTURAL — Thus `γ=0` does not survive in the Jimbo convention; the finite exponent data gives `γ=1` under the stated identification.

STRUCTURAL — Thus `β=0` is not forced by finite apparentness. In the Jimbo convention with `θ_0=θ_t=0`, `β=-α`; if the companion's `α=1/6` were retained, Jimbo's dictionary would give `β=-1/6`, not `0`.

STRUCTURAL — `δ=-1/2` is Jimbo's normalization in the quoted Lax convention; it is consistent as a convention, not computed from System C by a displayed deformation.

STRUCTURAL — `α` depends on `θ_∞`. The scalar infinity computation gives exponential factors and scalar Riccati log coefficients, but this session did not exhibit an unambiguous scalar-to-Jimbo Lax embedding fixing Jimbo's `θ_∞`. Therefore `α=1/6` is not decided by local scalar data alone.

## Four-parameter comparison with companion claim

| parameter | companion value | status | reasoning |
|---|---:|---|---|
| `α` | `1/6` | UNDETERMINED BY LOCAL DATA | STRUCTURAL — In Jimbo's convention `α=θ_∞^2/8`; no unambiguous map from System C's scalar infinity formal data to Jimbo `θ_∞` was established here. |
| `β` | `0` | CONTRADICTED AS PART OF THE CLAIMED TUPLE | STRUCTURAL — With `θ_0=θ_t=0`, Jimbo gives `β=-α`; retaining `α=1/6` gives `β=-1/6`, not `0`. |
| `γ` | `0` | CONTRADICTED | STRUCTURAL — With `θ_0=θ_t=0`, Jimbo gives `γ=1`, not `0`. |
| `δ` | `-1/2` | CONSISTENT | INSPECTED/STRUCTURAL — Jimbo fixes `δ=-1/2` in this normalization. |

## What local data cannot decide

STRUCTURAL — The operator's standing caveat is reproduced verbatim: *a matching Katz multiset is necessary but not sufficient; Table 2.1 classifies families of connections, and a single fixed operator matching a row does not make it a member of that isomonodromic family until the deformation parameter is specified.*

STRUCTURAL — Nothing in this task establishes that System C belongs to a PV isomonodromic family. System C, as written, has no free deformation parameter. A PV time variable would have to arise from an explicit family of rank-2 connections containing this scalar equation or from a specified deformation of the singularity/exponential data; that family/time was NOT FOUND in the inspected local computation and sources by the methods above.

## Open questions for the operator

STRUCTURAL — To turn the parameter constraints into a family-membership result, an explicit Lax embedding/deformation family is still needed: which rank-2 connection contains System C, what is the PV time `t`, and how exactly do the scalar infinity formal data map to Jimbo's `θ_∞`?

STRUCTURAL — If a different PV convention is intended, the corresponding quotable Lax dictionary must be supplied or fetched before any different parameter comparison is valid.

## Uncommitted files created in this session folder

INSPECTED — Files under `sessions\2026-09-17\CT-S9-PVPARAMS\`:

```text
PREREG.md
REPORT.md
claims.jsonl
refs\B02_003.pdf
refs\DLMF_32.2.E5.tex
refs\DLMF_32.4.html
refs\jimbo_1982_prims.pdf
outputs\B02_003_text.txt
outputs\head_start_end_check.txt
outputs\jimbo_1982_prims_text.txt
outputs\jimbo_page16-16.png
outputs\jimbo_page23-23.png
outputs\jimbo_parameter_constraints.json
outputs\system_c_symbolic_local_data.json
outputs\vdp_pages24-28.txt
outputs\vquad_v1.2_text.txt
scripts\compute_system_c_local_data.py
scripts\translate_jimbo_constraints.py
```

