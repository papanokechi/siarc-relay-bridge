# CT-S2-RHO-D4 — growth exponent and ρ convention at d = 4

- **Session ID:** CT-S2-RHO-D4 · **Date:** 2026-09-17
- **Pre-registration:** `PREREG.md`, written before any computation. Thresholds
  were not changed after seeing results.
- **Nothing committed, pushed, tagged or deposited.**

## 1. What was done

1. Located the PCF2-SESSION-Q1 d = 4 material and extracted the 8 representative
   quartics.
2. Measured the growth exponent `s` in
   `Q_n / Γ(dn+1) ~ K (β_d/d^d)^n n^s` for each, at dps 80, n up to 20000, with
   4 levels of ratio-2 Richardson extrapolation.
3. Ran the pre-registered two-arm vacuity check.
4. Computed `r_∞` for each representative to confirm `Q_n` is not the minimal
   solution.
5. Derived the convention map between the stored ρ and `ρ_d = -s-1`, anchored at
   d = 2 (see §5 for why d = 2).

Estimator validation: on the P0-appendix reference tuple `(β₀..β₄) = (0,2,-1,3,5)`
the estimator returns `s = 2.099999999999985` against `s_pred = 2.1`, residual
`1.45e-14` at only N = 4000 — four orders tighter than the crude two-point
estimator in the appendix (which gave 2.0996).

## 2. Source data (exact paths)

| What | Path |
|---|---|
| 8 representatives, `coeffs_a4_a3_a2_a1_a0` | `sessions/2026-05-01/PCF2-SESSION-Q1/newton_d4_results.json` |
| Generating script | `sessions/2026-05-01/PCF2-SESSION-Q1/session_q1_newton.py` |
| 60-family main run | `sessions/2026-05-01/PCF2-SESSION-Q1/results.json` |
| d = 2 ρ anchor (V_quad) | `sessions/2026-05-01/CC-PIPELINE-G/results_vquad.json` |
| ρ derivation | `sessions/2026-05-01/CC-PIPELINE-G/newton_birkhoff.py` L385–410 |

> **Scope correction (from CT-S0-INVENTORY).** P2's brief says Q1 is an
> "8 quartic representatives" run. Q1's headline run is **60 families**; the 8
> are the separate Phase Q1-3 Newton-polygon subset in `newton_d4_results.json`.
> That subset is what was used.

## 3. Main table

`β` written high-to-low as `(β₄,β₃,β₂,β₁,β₀)`. `s_pred = β₃/β₄ + 3/2`.
Residual = `|s_measured − s_predicted|`. `r_∞` at N = 20000.

| representative | (β₄,β₃,β₂,β₁,β₀) | s_measured | s_pred | residual | r_∞ | sign changes in b |
|---|---|---|---|---|---|---|
| `mixed_S_4_smallD` | (1,−3,−3,1,1) | −1.500000000000000469344 | −1.5 | 4.69e-16 | 1.0203356510 | 1 |
| `mixed_S_4_largeD` | (1,−3,−3,−3,3) | −1.500000000000000676222 | −1.5 | 6.76e-16 | 1.0065455919 | 1 |
| `mixed_D_4` | (1,−3,−3,−3,1) | −1.500000000000000711818 | −1.5 | 7.12e-16 | 1.0023749614 | 1 |
| `+_real_D_4` | (1,−3,−3,3,1) | −1.500000000000000365417 | −1.5 | 3.65e-16 | 1.0794709735 | 1 |
| `anchor_x4_minus_2_D_4` | (1,0,0,0,−2) | 1.4999999999999999904135 | 1.5 | 9.59e-18 | 0.9295293462 | 1 |
| `anchor_x4_plus_1_V_4` | (1,0,0,0,1) | 1.5000000000000000047250 | 1.5 | 4.73e-18 | 1.0301861479 | 0 |
| `anchor_x4_minus_x_minus_1` | (1,0,0,−1,−1) | 1.4999999999999999937604 | 1.5 | 6.24e-18 | 0.9241312466 | 1 |
| `alpha4_eq_7_synthetic` | (7,0,0,1,0) | 1.4999999999999999999250 | 1.5 | 7.49e-20 | 1.0011130209 | 0 |

**Worst residual: 7.12e-16.** The pre-registered falsifier
(`> 1e-6`) **did not fire** on any representative.

`r_∞` columns "their ρ (if stored)" and "mapped ρ_d" are **empty by necessity**:
Q1 stores no ρ at d = 4 (§5).

### 3a. Minimality / `r_∞`

All 8 have `r_∞ ≠ 0`, in the range 0.9241–1.0795, with N/2-vs-N agreement of
**28.8–30.5 decimal digits**. So `Q_n` is not the minimal solution in any case
and every representative is in scope for the falsifier.

**Sign-changing `b`:** 6 of 8 (spec required ≥ 2). The four `mixed_*`/`+_real_D_4`
quartics and the three `anchor_*` cases with negative constant/linear terms all
have `b(n) < 0` for small `n` before turning positive.

**Root precheck:** no representative has a positive integer root, so no
`Γ(1-r_i)` singularity arises. Two *grid* points (not representatives) were
correctly halted by this precheck — see §4.

## 4. Vacuity pre-check — both arms PASS

Run at N = 8000, ladder `500,1000,2000,4000,8000`, dps 80.

- **Arm (i), insensitivity.** `β₄=1, β₃=−3` fixed; `(β₂,β₁,β₀)` over the
  pre-registered 16-point grid. Spread of `s_measured` = **7.86e-14**, i.e. `s`
  is independent of the lower coefficients, as H1 requires. PASS.
  Two grid points, `(β₂,β₁,β₀) = (0,1,1)` at both `β₃=−3` and `β₃=0`, were
  **halted by the precheck** because `b(1) = 0` (a positive integer root). That
  is the designed behaviour, not a failure.
- **Arm (ii), sensitivity.** `β₃` varied over `{−4..4}` at `β₄=1`: `s_measured`
  returns `−2.5, −1.5, −0.5, 0.5, [halted], 2.5, 3.5, 4.5, 5.5` — moving by
  **exactly `Δβ₃/β₄`**. At `β₄=7`, `β₃ ∈ {0,1,7,14}` gives
  `1.5, 1.642857142857142834…(=3/2+1/7), 2.5, 3.5`, confirming the observable
  tracks the **ratio** `β₃/β₄`, not `β₃` alone. Max residual **8.32e-13**. PASS.

> Arm (ii) is the one that matters: had it failed, the observable would not have
> been sensitive to the hypothesis and the session would have halted. It passed
> decisively, so the arm (i) null is meaningful rather than vacuous.

## 5. Convention map

**The premise of P2 task 1 is false and this is the session's main negative
finding.** PCF2-SESSION-Q1 **stores no ρ at d = 4**. A case-insensitive search of
the entire Q1 folder for `rho` / `ρ` / `\rho` returns **zero** matches. What Q1
stores is:

- `ξ₀ = d/β_d^{1/d}` (at d=4, `4/a_4^{1/4}`; `char_poly_chi = 1 - c⁴/256`;
  edge slope 1/4; spread 0 at 50 dp), and
- WKB fit parameters `A, α, β, γ` per family.

So there is nothing at d = 4 to map ρ onto. The map was therefore anchored at the
only stored ρ in the corpus, the d = 2 V_quad value.

**Derivation.** With `d = 2`, `s = β₁/β₂ + 1/2` and
`ρ_d = −s − 1 = −3/2 − β₁/β₂`.
For V_quad, `b(n) = 3n² + n + 1`, so `β₂ = 3, β₁ = 1`, giving
`s = 1/3 + 1/2 = 5/6` and `ρ_d = −11/6`.

**Measured:** `s = 0.8333333333333333326758824` (predicted `5/6`, residual
**6.57e-19**), `r_∞ = 1.0166044410585062…`, hence

```
ρ_d = −s − 1 = −1.833333333333333332675882
stored ρ      = −1.833333333333333333333333…   (results_vquad.json)
|difference|  = 6.57e-19
```

**Why this is not tautological.** CC-PIPELINE-G obtains its ρ from a *different*
derivation: the `u¹`-order indicial equation of the Birkhoff formal solution
`f_±(u) = exp(c/u) u^ρ (1 + Σ a_k u^k)` in the uniformiser `u = √z`. The algebra
is written out in `newton_birkhoff.py` L385–394 and coded at L410:

> `#   rho = -3/2 - beta1 / beta2.`
> `#  So rho = -3/2 - beta1/beta2 (independent of sign of c).`
> `rho = mp.mpf(-3) / 2 - beta1 / beta2`

It never references `Q_n` or the growth law. So the agreement between the
indicial exponent in `u = √z` and `−s−1` from the `Q_n/Γ(dn+1)` asymptotic is a
genuine coincidence of two independent computations, not a restatement.

**Label:** the d = 2 numerical agreement is **VERIFIED** (residual 6.57e-19 at
dps 80). The identification `ρ_CT = ρ_d = −(d+1)/2 − β_{d-1}/β_d` **as the same
object for general d** is **STRUCTURAL**: it is established as an identity of
formulae at d = 2 only, and the generalisation rests on the unverified assumption
that the CT indicial construction in `u = z^{1/d}` continues to produce
`−s−1` for d > 2. No d = 4 indicial computation exists in the repo to test it.

## 6. Claims with labels

| id | claim | label |
|---|---|---|
| S2-01 | growth law `s = β₃/β₄ + 3/2` on all 8 d=4 representatives, worst residual 7.12e-16 | **VERIFIED** (dps 80, N=20000) |
| S2-02 | all 8 have `r_∞ ≠ 0` (28.8–30.5 digits stable); 6/8 sign-changing | **VERIFIED** |
| S2-03 | vacuity check passes both arms; observable is sensitive to `β_{d-1}/β_d` | **VERIFIED** |
| S2-04 | `ρ_stored = −s−1` at d=2 to 6.57e-19, from two independent derivations | **VERIFIED** at d=2 / **STRUCTURAL** as a general map |
| S2-05 | Q1 stores no ρ at d=4 | **VERIFIED** (file inspection) |

## 7. What was NOT established

- **No d = 4 ρ was validated**, because none is stored. The convention map is
  anchored at d = 2 and extrapolated structurally.
- The growth law is **VERIFIED, not PROVEN**. This session ran no proof. The
  proof is P4's job.
- The constant `K` was not extracted; only the exponent `s`. That is P3 Part B.
- Nothing here bears on the *analytic type* of the Borel singularity.
- The claim that CT's ρ "is an indicial exponent in `u = √z`, which is not
  automatically the same object" is **confirmed as a real distinction** — the two
  objects were shown to coincide numerically at d = 2, which is evidence, not
  identity.

## 8. Open questions for the operator

1. Confirm the d = 2 anchoring is acceptable given no d = 4 ρ exists, or supply
   a d = 4 indicial/Birkhoff computation so the map can be tested at d = 4.
2. `β₃` across the 8 representatives takes only two values (−3 and 0), so the
   representatives alone give poor leverage on `β_{d-1}`. The sensitivity
   evidence comes from the pre-registered synthetic grid. Is that acceptable, or
   should Q1 be re-run with a `β₃`-spread representative set?
3. Should `ρ_d = −s−1` be adopted as the *definition* at general d, or does CT
   require the indicial route at `u = z^{1/d}`?

## 9. Uncommitted files

All under `sessions/2026-09-17/CT-S2-RHO-D4/`:

- `PREREG.md`
- `s_exponent.py` · `d2_anchor.py` · `make_claims.py`
- `s_table.json` (sha256 `0cb1c1cf8b15c45cf702b45f907211c4061580f299760c128681e10e7dbda094`)
- `vacuity.json` (sha256 `bfd87fa685572d873724ba3e9d52632104bba33a2fcaf2688f224874b6c99a28`)
- `d2_anchor.json` (sha256 `900c9207932437a3e3ba8f4a740e44fdf3d8ae774d06366710ff6fbbb9b81512`)
- `run.log` · `d2_anchor.log` · `claims.jsonl` · `REPORT.md`
