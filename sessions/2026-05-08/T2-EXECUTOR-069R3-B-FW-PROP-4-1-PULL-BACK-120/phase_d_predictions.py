"""
phase_d_predictions.py
======================

Phase D of 109 069r3-B Route B mechanism (a) symbolic test.

Emits per_coord_hamiltonian_prediction.json with the four
Hamiltonian parameter predictions at the V_quad image, in the
canonical Okamoto (eta_inf, eta_0, theta_inf, theta_0) format
at >= 50 dps mpmath strings.

Per prompt 109 D.5: under verdict NO_GO_OFF_DEGENERATION the
four predictions are still emitted (marked off-submanifold);
110's numerical Route D extraction becomes the canonical
Hamiltonian parameter source.

Run:
  python phase_d_predictions.py
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath
import sympy as sp

mpmath.mp.dps = 50

# ----------------------------------------------------------------
# D.1 -- per-coordinate Hamiltonian predictions
# ----------------------------------------------------------------

# CT v1.3 sect 3.5.1 (3.5.1a)-(3.5.1d) trivial relabel pins
#   (alpha_inf, alpha_0, beta_inf, beta_0)
#     := (eta_inf, eta_0, theta_inf, theta_0)
# V_quad image (project tuple): (1/6, 0, 0, -1/2)

eta_inf_pred_sp = sp.Rational(1, 6)
eta_0_pred_sp = sp.Integer(0)
theta_inf_pred_sp = sp.Integer(0)
theta_0_pred_sp = sp.Rational(-1, 2)


def to_mpmath_str(x_sp):
    """Convert a SymPy rational to mpmath at dps>=50 and return string."""
    return mpmath.nstr(mpmath.mpf(str(x_sp)), 50)


eta_inf_pred_mp = to_mpmath_str(eta_inf_pred_sp)
eta_0_pred_mp = to_mpmath_str(eta_0_pred_sp)
theta_inf_pred_mp = to_mpmath_str(theta_inf_pred_sp)
theta_0_pred_mp = to_mpmath_str(theta_0_pred_sp)

# Sum check (FW (2.2) null-sum residual; expected -1/3)
sum_check = (eta_inf_pred_sp + eta_0_pred_sp
             + theta_inf_pred_sp + theta_0_pred_sp)
sum_check_mp = to_mpmath_str(sum_check)

print("================================================================")
print("PHASE D -- PER-COORDINATE HAMILTONIAN PREDICTION")
print("================================================================")
print()
print("Per-coordinate predictions at V_quad image (off-submanifold;")
print("project tuple by construction):")
print()
print(f"  eta_inf_pred    = {eta_inf_pred_sp}  =  {eta_inf_pred_mp}")
print(f"  eta_0_pred      = {eta_0_pred_sp}  =  {eta_0_pred_mp}")
print(f"  theta_inf_pred  = {theta_inf_pred_sp}  =  {theta_inf_pred_mp}")
print(f"  theta_0_pred    = {theta_0_pred_sp}  =  {theta_0_pred_mp}")
print()
print(f"FW (2.2) null-sum residual at V_quad image:")
print(f"  eta_inf + eta_0 + theta_inf + theta_0 = {sum_check}")
print(f"                                         = {sum_check_mp}")
print()
print("Canonical PIII pair (UF-110-3 anchored):")
print(f"  v_1 = theta_0   = {theta_0_pred_sp}")
print(f"  v_2 = theta_inf = {theta_inf_pred_sp}")
print()
print("FW (4.3) shift constants at this canonical PIII pair:")
print(f"  c_constant_part = (1/4) v_1^2 = 1/16")
print(f"  c_t_coefficient = -1/2")
print()

# ----------------------------------------------------------------
# D.2 / D.3 / D.4 -- emit JSON
# ----------------------------------------------------------------

prediction_payload = {
    "schema_version": "109-phase-d-v1.0",
    "session_id": "T2-EXECUTOR-069R3-B-FW-PROP-4-1-PULL-BACK-120",
    "v_quad_image_input": {
        "alpha_inf": "1/6",
        "alpha_0": "0",
        "beta_inf": "0",
        "beta_0": "-1/2",
        "tuple_form": [
            "1/6", "0", "0", "-1/2",
        ],
        "rename_3_5_1a_to_d": {
            "alpha_inf": "eta_inf",
            "alpha_0": "eta_0",
            "beta_inf": "theta_inf",
            "beta_0": "theta_0",
        },
    },
    "ordering_chosen": "ordering_3_uf_110_3_anchored",
    "ordering_3_definition": (
        "(v_1, v_2)_FW_PIII = (theta_0, theta_inf)_Okamoto under "
        "WLOG eta_inf = eta_0 = 1; anchored by FW S2.1 vs S4.1 "
        "coefficient match in okamoto_substrate_extract.txt note "
        "109-O2 (line range 60-95 of that file)."
    ),
    "ordering_pin_source_citation": (
        "UF-110-3 from sessions/2026-05-08/T2-TIER-B-PASTE-PACKET-"
        "PRESTAGE-110/handoff.md (anchored by ODE coefficient match "
        "alpha_ODE = -4 v_2 vs alpha_ODE = -4 theta_inf, beta_ODE = "
        "4(v_1 + 1) vs beta_ODE = 4(theta_0 + 1))."
    ),
    "alternative_orderings_evaluated": {
        "ordering_1_prompt_a3_candidate_1": {
            "definition": (
                "v_1 = eta_inf = 1/6, v_2 = theta_inf = 0 surviving; "
                "(v_3, v_4) = (eta_0, theta_0) absorbing."
            ),
            "fw_4_3_constant_part": "1/144",
            "fw_4_3_t_linear_coefficient": "-1/2",
            "matches_minus_one_third": False,
        },
        "ordering_2_prompt_a3_candidate_2": {
            "definition": (
                "v_1 = theta_0 = -1/2, v_2 = theta_inf = 0 surviving; "
                "(v_3, v_4) = (eta_0, eta_inf) absorbing."
            ),
            "fw_4_3_constant_part": "1/16",
            "fw_4_3_t_linear_coefficient": "-1/2",
            "matches_minus_one_third": False,
        },
        "ordering_3_uf_110_3_anchored": {
            "definition": (
                "v_1 = theta_0 = -1/2, v_2 = theta_inf = 0 (UF-110-3 "
                "literature-anchored; numerically identical to "
                "ordering 2)."
            ),
            "fw_4_3_constant_part": "1/16",
            "fw_4_3_t_linear_coefficient": "-1/2",
            "matches_minus_one_third": False,
        },
    },
    "hamiltonian_predictions_at_v_quad_image": {
        "eta_inf": eta_inf_pred_mp,
        "eta_0": eta_0_pred_mp,
        "theta_inf": theta_inf_pred_mp,
        "theta_0": theta_0_pred_mp,
    },
    "hamiltonian_predictions_off_submanifold": True,
    "off_submanifold_basis": {
        "obstruction_i_fw_2_2_null_sum_residual": "-1/3",
        "obstruction_ii_okamoto_standing_assumption": (
            "FAILS at eta_0 = 0 (Okamoto S1 boundary)"
        ),
        "obstruction_iii_okamoto_wlog": (
            "FAILS (eta_inf = 1/6 != 1, eta_0 = 0 != 1; FW (4.1) "
            "hardcodes WLOG)"
        ),
    },
    "fw_4_3_shift_at_canonical_piii_pair": {
        "v_1_value": "-1/2",
        "v_2_value": "0",
        "constant_part": "1/16",
        "t_linear_coefficient": "-1/2",
        "matches_target_minus_one_third": False,
    },
    "expected_per_coord_3_digit_match_with_110": True,
    "per_coord_3_digit_match_basis": (
        "Predictions equal the project tuple by construction "
        "(symbol substitution under (3.5.1a)-(d)). 110's numerical "
        "Route D extraction at V_quad image must agree to >= 3 "
        "decimal digits per UF-113-3 sharpened criterion. Under "
        "verdict_bin = NO_GO_OFF_DEGENERATION, this cross-validation "
        "is mathematically vacuous (both sides emit the same project "
        "tuple); the actual decision substrate for 069r3 FINAL is "
        "whether V_quad image lies on the FW PV submanifold, which "
        "is decided negatively by Phase B obstructions (i)+(ii)+(iii)."
    ),
    "verdict_bin": "NO_GO_OFF_DEGENERATION",
    "verdict_basis_summary": (
        "Phase B: V_quad image OFF FW PV null-sum submanifold (residual "
        "-1/3) under any (3.5.1a)-(d)-respecting ordering; AND fails "
        "Okamoto WLOG; AND fails Okamoto S1 standing assumption. Phase "
        "C: FW (4.3) shift constants {1/144, 1/16} unequal to -1/3 "
        "under any tested ordering."
    ),
    "cascade_implication_for_069r3_final": (
        "Mechanism (a) ruled out for Route B path. Cascade to "
        "mechanism (b) additive shift (-1/12 per coordinate working "
        "hypothesis logged in 110 prestage UF-110-2 fallback note) or "
        "(c) Sakai surface-type artefact gated to Route F machinery."
    ),
    "computation_environment": {
        "sympy_version": sp.__version__,
        "mpmath_version": mpmath.__version__,
        "mpmath_dps": mpmath.mp.dps,
        "python_version": "3.10+",
    },
}

out_path = Path(__file__).with_name("per_coord_hamiltonian_prediction.json")
out_path.write_text(json.dumps(prediction_payload, indent=2),
                    encoding="utf-8")

print(f"--- D.3: per_coord_hamiltonian_prediction.json written")
print(f"         size = {out_path.stat().st_size} bytes")
print()
print("PHASE D END.")
