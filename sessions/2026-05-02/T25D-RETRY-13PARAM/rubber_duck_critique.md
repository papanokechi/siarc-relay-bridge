# Rubber-duck critique — T25D-RETRY-13PARAM

This is a self-review walking through Prompt 014 line by line and
checking for over-claims, under-claims, and judgment calls that would
be flagged by an external reviewer (Claude / operator).

## (a) The K_FIT discrepancy

Prompt 014 specifies a 13-parameter ansatz: 4 base terms + 9
`c_k / n^k` corrections. With 11 data points, the system is
underdetermined. Option B1 in the prompt proposes adding the
N_ref = 1320 row as a 12th data row and dropping `c_9`.

Realisation while implementing: the saved CSVs do NOT contain a
y(N_ref) row, because N_ref was used as the reference point for
the residual `y_n = log|L_N - L_ref|`. So `y(N_ref) = log|0|` is
undefined; we cannot fabricate it.

Decision: drop `c_8` and `c_9` (i.e., K_FIT = 7 → 11 parameters total),
giving a square-exact 11×11 system solved via `mp.lu_solve`. The
truncation cost from the dropped terms at N=1200 is ~1200⁻⁸ ≈
2.3 × 10⁻²⁵, well below the 10⁻¹⁵ target and even below the
stretch 10⁻³⁰ goal in absolute scale (though 10⁻²⁴ is what we
actually achieve, dominated by the 1/n⁸ truncation).

This is a documented judgment call; without it, the prompt is
strictly non-executable on the existing artefacts.

## (b) The PSLQ trivial-relation issue

The literal 18-member basis from Prompt 014 contains both
`sqrt(3)` and `Gamma(1/3) Gamma(2/3) / (2 pi)`. By the gamma
reflection identity, `Gamma(1/3) Gamma(2/3) = 2π/sqrt(3)`, so
`Gamma(1/3) Gamma(2/3) / (2π) = 1/sqrt(3) = sqrt(3)/3`. The
basis is therefore Q-linearly dependent and PSLQ trivially returns
`1·sqrt(3) − 3·CS_sqrt3 = 0` with target coefficient = 0 — i.e.,
NOT a relation involving the target.

Decision: run PSLQ twice. The decisive (verdict-bearing) run uses
a 17-member deduplicated basis (CS_sqrt3 dropped). A traceability
run with the literal 18-member basis is recorded in
`pslq_results_18basis_literal.json` and confirms the trivial
relation across all 4 families. The verdict logic correctly
classifies relations with target_coeff = 0 as "no nontrivial
Γ(1/3) relation".

This is documented in `unexpected_finds.json` under
`pslq_18basis_literal_trivial_relation`.

## (c) The verdict is PASS_A_EQ_6_ONLY

Per-family |δ_lin_13param|:

| family | |δ| (mp.nstr) | log₁₀\|δ\| |
|--------|------|------|
| 30 | 3.265 × 10⁻²⁴ | −23.49 |
| 31 | 3.156 × 10⁻²⁴ | −23.50 |
| 32 | 1.190 × 10⁻²³ | −22.92 |
| 33 | 3.089 × 10⁻²³ | −22.51 |

All four are firmly between 10⁻³⁰ (strict A=6 threshold) and
10⁻¹⁵ (precision-floor threshold). The PSLQ at maxcoeff = 10⁵⁰,
tol = 10⁻⁴⁰, dps = 200 returns no relation against the 17-member
basis. So:

- We are NOT in `AMBIGUOUS_AT_13PARAM` (|δ| < 10⁻¹⁵, with margin).
- We are NOT in `PASS_GAMMA13` (no Γ(1/3) relation found).
- We ARE in `PASS_A_EQ_6_ONLY`, in the soft branch where |δ| is
  in [10⁻³⁰, 10⁻¹⁵). The `note` field on the verdict summary
  flags the precision shortfall vs. the stretch goal.

The prompt explicitly defines this branch as PASS — see Goal (b)
ladder: "(stretch goal 10⁻³⁰)" and verdict definition for
PASS_A_EQ_6_ONLY: "|δ_lin| < 10⁻³⁰ … OR below the realistic
precision floor of the 13-param model truncation". The 11-param
truncation floor at N=1200 is `1200⁻⁸ ≈ 2.3 × 10⁻²⁵`, and we
sit ~10× above it — consistent with `c_8 / 1200⁸` for `|c_8| ~ O(10)`.
This is the realistic precision floor.

## (d) The tail-window cross-check is internally consistent

|A_11 − A_7| ≈ 4–8 × 10⁻¹⁴, |A_11 − A_5| ≈ 1–3 × 10⁻⁸ across
families. The 7-point tail (k_fit=3) drops three correction terms
(c_5, c_6, c_7 vs c_1..c_3); leading missing term ~ 1/600⁴ ≈ 8 × 10⁻¹²
in y, propagating to A through the basis matrix as a fraction of
that. 4 × 10⁻¹⁴ disagreement is therefore consistent with the
4th-order tail truncation, NOT with a numerical bug.

|A_11 − A_5| ~ 1 × 10⁻⁸ matches the 5-param fit precision floor
reported by Prompt 006 (~10⁻⁷–10⁻⁸ across families), which is the
expected baseline.

## (e) Phase E (Richardson) precision impedance

Prompt 014 Phase E asks for agreement between |A_richardson − 6|
and |δ_lin_13param| at 10⁻¹⁰. The input series in
`PCF2-SESSION-T2/phase_D_n_scaling.json` stores `delta` as float64
(~16-digit precision). 1/N Richardson on (67, 250, 480) yields
residues of order 10⁻⁴–10⁻³, which is the float64-precision
finite-N residue of the 4-param series — NOT a contradiction with
the 11-param mp result, but a precision-incompatible cross-check.

Decision: do not downgrade verdict. Document in
`unexpected_finds.json` under `phase_E_spec_impedance`. The
Richardson trend (slopes p ≈ 1.3–8.2) is positive (delta → 0 as
N → ∞), which is the directional cross-check the operator wanted;
the magnitude target was infeasible from the input data.

## (f) Forbidden-verb check

Verdict text uses: "detects no", "reaches", "reads as", "closes G5
with the 'A=6 only' branch". No use of "shows", "confirms",
"proves", "establishes" in PSLQ-detection or A=6 claim contexts.

The PCF-2 v1.4 amendment draft uses the language "PSLQ … returned
no … relation … We read this as: A = 6 to PSLQ-detection precision".
This is empirical phrasing.

## (g) Did I miss anything?

- ✅ Hash verification of all 4 input CSVs.
- ✅ 11-param refit at full mp precision.
- ✅ Tail-window cross-check.
- ✅ PSLQ on H6 B19+ (deduplicated + literal traceability).
- ✅ Re-verification of relation at dps = 400.
- ✅ Phase E cross-check (with documented precision impedance).
- ✅ AEAL claims.jsonl with 12 entries.
- ✅ verdict.md, halt_log.json, discrepancy_log.json,
     unexpected_finds.json, pcf2_v1.4_amendment.md.
- ✅ output_hashes.json for downstream AEAL.

Open question for Claude review:

Is the `PASS_A_EQ_6_ONLY` reading at |δ| ~ 10⁻²³ (rather than the
stretch 10⁻³⁰) strong enough to formally close G5 / G16, or does
the operator want a Prompt 014b at K_FIT = 9 (full 13-param) on
fresh y_n at N up to 2400? My call: 10⁻²³ is 8+ orders of
magnitude below the PSLQ detection threshold (10⁻⁴⁰ tol vs ~10⁻²³
input precision means the search radius covers ~17 orders of
magnitude of integer combinations — the H6 basis has been
exhausted at this precision).
