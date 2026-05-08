"""
degeneration_submanifold_check.py
=================================

Phase B of 109 069r3-B Route B mechanism (a) symbolic test.

Tests whether the V_quad image (1/6, 0, 0, -1/2) sits on the FW
PV->PIII degeneration submanifold under three candidate orderings:

  - Prompt 109 ORDERING 1:  (v_1, v_2, v_3, v_4) =
        (eta_inf, theta_inf, eta_0, theta_0)
    surviving PIII pair (v_1, v_2) = (eta_inf, theta_inf);
    (v_3, v_4) = (eta_0, theta_0) absorb in PV->PIII limit.

  - Prompt 109 ORDERING 2:  (v_1, v_2, v_3, v_4) =
        (theta_0, theta_inf, eta_0, eta_inf)
    surviving PIII pair (v_1, v_2) = (theta_0, theta_inf);
    (v_3, v_4) = (eta_0, eta_inf) absorb in PV->PIII limit.

  - UF-110-3 LITERATURE-ANCHORED ordering: surviving PIII pair
    (v_1, v_2) = (theta_0, theta_inf), with the (v_3, v_4)
    absorption fixed by the FW S4.1 hard-edge scaling limit
    (anchored by FW vs Okamoto coefficient match under WLOG
    eta_inf = eta_0 = 1; cf. okamoto_substrate_extract.txt
    note 109-O2). Under this ordering, v_3, v_4 do NOT correspond
    to (eta_0, eta_inf) cleanly; they limit out together with
    the (v_3 - v_4) term in FW (2.5).

Phase B checks:
  B.1: parameter-space degeneration prescription
  B.2: FW (2.2) null-sum residual at V_quad image under each
       candidate ordering
  B.3: Okamoto WLOG compatibility (eta_inf = eta_0 = 1)
  B.4: verdict bin per Phase B.5 of prompt 109

Run:
  python degeneration_submanifold_check.py
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

# ----------------------------------------------------------------
# B.0 -- symbolic setup
# ----------------------------------------------------------------

eta_inf, eta_0, theta_inf, theta_0 = sp.symbols(
    'eta_inf eta_0 theta_inf theta_0',
    real=True,
)

# Project V_quad image per CT v1.3 sect 3.5.1 (3.5.1a)-(3.5.1d):
#   alpha_inf := eta_inf,  alpha_0 := eta_0,
#   beta_inf  := theta_inf, beta_0  := theta_0
v_quad_image_tuple = (sp.Rational(1, 6), sp.Integer(0),
                      sp.Integer(0), sp.Rational(-1, 2))

(eta_inf_val, eta_0_val, theta_inf_val, theta_0_val) = v_quad_image_tuple

print("================================================================")
print("PHASE B -- PV->PIII DEGENERATION SUBMANIFOLD CHECK")
print("================================================================")
print()
print(f"V_quad image (alpha_inf, alpha_0, beta_inf, beta_0)")
print(f"            = (eta_inf, eta_0, theta_inf, theta_0)")
print(f"            = {v_quad_image_tuple}")
print()

# ----------------------------------------------------------------
# B.1 -- parameter-space degeneration prescription
# ----------------------------------------------------------------

print("--- B.1: PV->PIII parameter-space degeneration prescription")
print()
print("FW S4 prose at .txt L3905-3911 describes PV->PIII as a")
print("hard-edge scaling COORDINATE-SPACE limit (eigenvalue spacing")
print("scaling). The PARAMETER-SPACE prescription mapping")
print("(v_1, v_2, v_3, v_4) -> (v_1, v_2) is NOT given verbatim in")
print("FW S4.1; FW just postulates the PIII Hamiltonian (4.1) with")
print("two surviving parameters, citing Okamoto [31] (Okamoto 1987).")
print()
print("Implicit FW prescription (anchored by S2.1 vs S4.1 coefficient")
print("match in okamoto_substrate_extract.txt note 109-O2):")
print("  The FW PIII' form (4.1) hardcodes eta_inf = eta_0 = 1")
print("  in the q^2 p and t p coefficients respectively.")
print("  The PV (2.1) form contains the four v_i without WLOG.")
print("  Going PV->PIII means *integrating out* the v_3 and v_4")
print("  dependence by sending the difference (v_3 - v_4) to the")
print("  hard-edge limit: see FW (2.5) where alpha = (1/2)(v_3-v_4)^2")
print("  is the *only* place v_3, v_4 enter the PV ODE coefficients")
print("  beyond combinations that absorb into Okamoto's (theta_0,")
print("  theta_inf) on the PIII side.")
print()

# ----------------------------------------------------------------
# B.2 -- FW (2.2) null-sum residual under three orderings
# ----------------------------------------------------------------

print("--- B.2: FW (2.2) null-sum  v_1 + v_2 + v_3 + v_4 = 0  residual")
print("         at V_quad image under three candidate orderings")
print()


def null_sum_residual(label, v1, v2, v3, v4):
    """Compute (v_1 + v_2 + v_3 + v_4) symbolically."""
    expr = v1 + v2 + v3 + v4
    val = sp.simplify(expr)
    print(f"  {label}:")
    print(f"    (v_1, v_2, v_3, v_4) = ({v1}, {v2}, {v3}, {v4})")
    print(f"    sum = {val}")
    print(f"    on FW (2.2) submanifold (sum == 0)?  {val == 0}")
    print()
    return val


# Ordering 1: surviving = (eta_inf, theta_inf), absorbing = (eta_0, theta_0)
sum_1 = null_sum_residual(
    "ORDERING 1 (prompt A.3 candidate-1)",
    eta_inf_val, theta_inf_val, eta_0_val, theta_0_val,
)

# Ordering 2: surviving = (theta_0, theta_inf), absorbing = (eta_0, eta_inf)
sum_2 = null_sum_residual(
    "ORDERING 2 (prompt A.3 candidate-2)",
    theta_0_val, theta_inf_val, eta_0_val, eta_inf_val,
)

# UF-110-3 anchored ordering: PIII surviving pair (v_1, v_2) =
# (theta_0, theta_inf). On the PIII side only two parameters
# survive; the PV null-sum check is well-defined only on the
# pre-degeneration PV side. Under the most natural "all four to
# absolute project values, lifted to PV under (3.5.1a)-(d)" reading:
sum_3 = null_sum_residual(
    "ORDERING 3 (UF-110-3 PIII surviving pair, lifted to PV)",
    theta_0_val, theta_inf_val, eta_0_val, eta_inf_val,
)
# Note: under any orderings respecting the (3.5.1a)-(d) trivial
# relabel, the four PV slots are populated by some permutation of
# {1/6, 0, 0, -1/2}. Sum is permutation-invariant so all permutations
# yield the same null-sum value -1/3.

print("--- B.2 SUMMARY:")
print(f"    All three orderings yield null-sum residual = -1/3")
print(f"    (sum is permutation-invariant; the four slots take values")
print(f"     {{1/6, 0, 0, -1/2}} in any order).")
print()
print(f"    -1/3 != 0  =>  V_quad image VIOLATES FW (2.2) by")
print(f"    additive c-number -1/3 under any ordering preserving the")
print(f"    (3.5.1a)-(d) trivial relabel.")
print()

# ----------------------------------------------------------------
# B.3 -- Okamoto WLOG compatibility
# ----------------------------------------------------------------

print("--- B.3: Okamoto WLOG eta_inf = eta_0 = 1  compatibility check")
print()
print(f"  V_quad image  eta_inf = {eta_inf_val}")
print(f"                eta_0   = {eta_0_val}")
print()
print(f"  WLOG eta_inf == 1  ?  {eta_inf_val == 1}")
print(f"  WLOG eta_0   == 1  ?  {eta_0_val == 1}")
print()
print("  Okamoto 1987 S1 standing assumption  eta_Delta != 0  ?")
print(f"    eta_inf != 0  ?  {eta_inf_val != 0}")
print(f"    eta_0   != 0  ?  {eta_0_val != 0}")
print()
print("  Conclusion (B.3):")
print("    V_quad image FAILS Okamoto WLOG (eta_inf, eta_0 not = 1)")
print("    AND additionally FAILS Okamoto S1 standing assumption")
print("    (eta_0 = 0 is on the assumption boundary).")
print()
print("  Since FW (4.1) hardcodes eta_inf = eta_0 = 1 in the q^2 p")
print("  and t p coefficients (cf. okamoto_substrate_extract.txt")
print("  note 109-O2), the FW (4.1) PIII' Hamiltonian does NOT model")
print("  the V_quad image directly without an additional gauge")
print("  rescale; the eta_0 = 0 value is moreover the *singular gauge")
print("  point* where the t p coefficient vanishes, a degeneration")
print("  of the Hamiltonian system.")
print()

# ----------------------------------------------------------------
# B.4 -- verdict
# ----------------------------------------------------------------

print("--- B.4: VERDICT (Phase B.5 of prompt 109)")
print()
print("Three independent obstructions place V_quad image OFF the FW")
print("PV->PIII degeneration submanifold:")
print()
print("  (i)   FW (2.2) null-sum residual = -1/3 != 0")
print("        (V_quad image is OFF the PV null-sum submanifold,")
print("         and so OFF every sub-submanifold of it including the")
print("         PV->PIII degeneration submanifold).")
print()
print("  (ii)  Okamoto S1 standing assumption eta_Delta != 0 fails")
print("        at eta_0 = 0  (V_quad image is on the assumption")
print("         boundary; canonical H_III Hamiltonian form is")
print("         singular here).")
print()
print("  (iii) Okamoto WLOG eta_inf = eta_0 = 1 fails")
print("        (FW (4.1) hardcodes the WLOG and so cannot model")
print("         V_quad image without additional gauge work; the")
print("         additional gauge is non-trivial precisely because")
print("         the singular gauge point coincides with the V_quad")
print("         image).")
print()
print("Verdict bin: NO_GO_OFF_DEGENERATION")
print()
print("Per prompt 109 HALT-109-3-SOFT directive: this halt is SOFT;")
print("Phase C still proceeds with the off-submanifold values for")
print("record, and the verdict at Phase D is NO_GO_OFF_DEGENERATION.")
print()

# ----------------------------------------------------------------
# Emit results JSON-style for handoff cross-reference
# ----------------------------------------------------------------

results = {
    "v_quad_image": {
        "alpha_inf": "1/6",
        "alpha_0": "0",
        "beta_inf": "0",
        "beta_0": "-1/2",
    },
    "rename_3_5_1a_to_d": {
        "alpha_inf": "eta_inf",
        "alpha_0": "eta_0",
        "beta_inf": "theta_inf",
        "beta_0": "theta_0",
    },
    "fw_2_2_null_sum_residual": {
        "ordering_1_prompt_a3_candidate_1": str(sum_1),
        "ordering_2_prompt_a3_candidate_2": str(sum_2),
        "ordering_3_uf_110_3_anchored": str(sum_3),
        "permutation_invariant_value": "-1/3",
    },
    "okamoto_wlog_compatibility": {
        "eta_inf_equals_1": False,
        "eta_0_equals_1": False,
        "eta_inf_nonzero": True,
        "eta_0_nonzero": False,
        "standing_assumption_eta_Delta_nonzero": (
            "FAILS at eta_0 = 0 (boundary)"
        ),
        "wlog_normalisation_compatibility": (
            "FAILS at both eta_inf and eta_0"
        ),
    },
    "verdict_bin": "NO_GO_OFF_DEGENERATION",
    "halt_marker": "HALT-109-3-SOFT (Phase B.5)",
    "obstructions_count": 3,
}

out_path = Path(__file__).with_name("phase_b_results.json")
out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

print(f"--- B.4: results written to {out_path.name}")
print()
print("PHASE B END.")
