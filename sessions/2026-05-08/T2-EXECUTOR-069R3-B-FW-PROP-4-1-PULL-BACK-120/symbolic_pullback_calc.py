"""
symbolic_pullback_calc.py
=========================

Phase C of 109 069r3-B Route B mechanism (a) symbolic test.

SymPy-based pull-back of FW (4.3) auxiliary Hamiltonian
  h = tH + (1/4) v_1^2 - (1/2) t
along the FW PIII' Hamiltonian (4.1)
  tH = q^2 p^2 - (q^2 + v_1 q - t) p + (1/2)(v_1 + v_2) q
to the V_quad image parameter point under three candidate
orderings of the project tuple (alpha_inf, alpha_0, beta_inf,
beta_0) -> FW PIII (v_1, v_2).

The mechanism (a) hypothesis predicts the symbolic shift in
FW (4.3) yields the project's -1/3 null-sum offset at the
V_quad image. Phase C either supports or rules against this
prediction.

Run:
  python symbolic_pullback_calc.py
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

# ----------------------------------------------------------------
# C.1 -- symbolic FW (4.1) tH and FW (4.3) h
# ----------------------------------------------------------------

q, p, t = sp.symbols('q p t', real=True)
v_1, v_2 = sp.symbols('v_1 v_2', real=True)

# FW (4.1) PIII' Hamiltonian (.txt L3917)
tH_fw_4_1 = (
    q**2 * p**2
    - (q**2 + v_1 * q - t) * p
    + sp.Rational(1, 2) * (v_1 + v_2) * q
)

# FW (4.3) auxiliary Hamiltonian (.txt L3960)
h_fw_4_3 = (
    tH_fw_4_1
    + sp.Rational(1, 4) * v_1**2
    - sp.Rational(1, 2) * t
)

print("================================================================")
print("PHASE C -- SYMBOLIC PULL-BACK OF FW (4.3)")
print("================================================================")
print()
print("--- C.1: FW (4.1) PIII' Hamiltonian symbolic form")
print()
print(f"  tH = {sp.expand(tH_fw_4_1)}")
print()
print("--- C.1: FW (4.3) auxiliary Hamiltonian symbolic form")
print()
print(f"  h  = {sp.expand(h_fw_4_3)}")
print()

# Decompose h into:
#   h = tH(q, p, t; v_1, v_2)   [Hamiltonian part]
#     + (1/4) v_1^2             [c-number quadratic shift]
#     + (-1/2) t                [t-linear shift]
shift_quadratic_in_v1 = sp.Rational(1, 4) * v_1**2
shift_t_linear = -sp.Rational(1, 2) * t

print("--- C.1: FW (4.3) shift decomposition  c(t; v_1, v_2)")
print()
print(f"  c_quadratic_v1   = (1/4) v_1^2  =  {shift_quadratic_in_v1}")
print(f"  c_t_linear       = -(1/2) t    =  {shift_t_linear}")
print(f"  c_total          = {shift_quadratic_in_v1 + shift_t_linear}")
print()
print("Note: c is a c-number function of (t, v_1, v_2); does NOT")
print("depend on (q, p). The pull-back along the canonical (q, p)")
print("gauge (058R Phi_symp at phase_b_canonical_map.md L118-127)")
print("leaves c invariant up to a gauge-additive c-number.")
print()

# ----------------------------------------------------------------
# C.2 -- substitute V_quad image under three candidate orderings
# ----------------------------------------------------------------

# CT v1.3 sect 3.5.1 trivial relabel:
#   alpha_inf := eta_inf = 1/6
#   alpha_0   := eta_0   = 0
#   beta_inf  := theta_inf = 0
#   beta_0    := theta_0   = -1/2

print("--- C.2: substitute V_quad image  (1/6, 0, 0, -1/2) =")
print("         (alpha_inf, alpha_0, beta_inf, beta_0) =")
print("         (eta_inf, eta_0, theta_inf, theta_0)")
print("         under three candidate orderings of (v_1, v_2).")
print()


def evaluate_pullback(label, v1_val, v2_val):
    """Substitute (v_1, v_2) and report symbolic shift constants."""
    c_quad = shift_quadratic_in_v1.subs(v_1, v1_val)
    c_t = shift_t_linear  # independent of v_1, v_2
    c_total = sp.simplify(c_quad + c_t)
    tH_sub = sp.expand(tH_fw_4_1.subs([(v_1, v1_val), (v_2, v2_val)]))
    h_sub = sp.expand(h_fw_4_3.subs([(v_1, v1_val), (v_2, v2_val)]))

    print(f"  {label}:")
    print(f"    (v_1, v_2)       = ({v1_val}, {v2_val})")
    print(f"    tH(q,p,t; v)     = {tH_sub}")
    print(f"    h (q,p,t; v)     = {h_sub}")
    print(f"    c_quad(v_1)      = (1/4) v_1^2  =  {c_quad}")
    print(f"    c_t              = -(1/2) t    =  {c_t}")
    print(f"    c_constant_part  = {c_quad}  "
          f"(coefficient of t^0)")
    print(f"    c_t_coefficient  = -1/2 "
          f"(coefficient of t^1)")
    print()
    return {
        "v_1_value": str(v1_val),
        "v_2_value": str(v2_val),
        "tH_substituted": str(tH_sub),
        "h_substituted": str(h_sub),
        "c_quadratic_v1_squared_over_4": str(c_quad),
        "c_t_linear_coefficient": str(c_t),
        "c_total_at_t_arbitrary": str(c_total),
        "c_constant_part_t_zero": str(c_quad),
    }


# ORDERING 1 (prompt A.3 candidate 1):
#   surviving PIII pair = (eta_inf, theta_inf) = (1/6, 0)
result_o1 = evaluate_pullback(
    "ORDERING 1  v_1 = eta_inf = 1/6,  v_2 = theta_inf = 0",
    sp.Rational(1, 6), sp.Integer(0),
)

# ORDERING 2 (prompt A.3 candidate 2):
#   surviving PIII pair = (theta_0, theta_inf) = (-1/2, 0)
result_o2 = evaluate_pullback(
    "ORDERING 2  v_1 = theta_0 = -1/2,  v_2 = theta_inf = 0",
    sp.Rational(-1, 2), sp.Integer(0),
)

# ORDERING 3 (UF-110-3 literature-anchored):
#   (v_1, v_2)_FW = (theta_0, theta_inf)_Okamoto under WLOG
#   = (-1/2, 0) under (3.5.1a)-(d)
result_o3 = evaluate_pullback(
    "ORDERING 3  v_1 = theta_0 = -1/2,  v_2 = theta_inf = 0  "
    "(UF-110-3 anchored; identical numerics to ORDERING 2)",
    sp.Rational(-1, 2), sp.Integer(0),
)

# ----------------------------------------------------------------
# C.3 -- comparison to mechanism (a) hypothesis  (-1/3)
# ----------------------------------------------------------------

target_offset = sp.Rational(-1, 3)
print("--- C.3: comparison to mechanism (a) hypothesis  (-1/3 offset)")
print()
print(f"  target null-sum offset = {target_offset}")
print()


def compare_to_target(label, c_const_str, c_t_coeff_str):
    c_const = sp.sympify(c_const_str)
    c_t_coeff = sp.sympify(c_t_coeff_str)
    print(f"  {label}:")
    print(f"    FW (4.3) constant part  = {c_const}")
    print(f"    FW (4.3) t-linear coeff = {c_t_coeff}")
    print(f"    constant == -1/3 ?       {c_const == target_offset}")
    print(f"    t-coeff  == -1/3 ?       {c_t_coeff == target_offset}")
    print()
    return {
        "constant_matches_target": c_const == target_offset,
        "t_coeff_matches_target": c_t_coeff == target_offset,
    }


cmp_o1 = compare_to_target(
    "ORDERING 1",
    result_o1["c_constant_part_t_zero"],
    result_o1["c_t_linear_coefficient"],
)
cmp_o2 = compare_to_target(
    "ORDERING 2",
    result_o2["c_constant_part_t_zero"],
    result_o2["c_t_linear_coefficient"],
)
cmp_o3 = compare_to_target(
    "ORDERING 3",
    result_o3["c_constant_part_t_zero"],
    result_o3["c_t_linear_coefficient"],
)

# ----------------------------------------------------------------
# C.4 -- mechanism (a) verdict
# ----------------------------------------------------------------

print("--- C.4: MECHANISM (a) VERDICT")
print()
print("Under EVERY candidate ordering tested, FW (4.3) shift constants")
print("do NOT match -1/3:")
print()
print("  ORDERING 1: constant = 1/144,   t-coeff = -1/2")
print("  ORDERING 2: constant = 1/16,    t-coeff = -1/2")
print("  ORDERING 3: constant = 1/16,    t-coeff = -1/2")
print()
print("None of {1/144, 1/16, -1/2} equals -1/3.")
print()
print("Combined with Phase B verdict (V_quad image OFF FW PV null-sum")
print("submanifold by exactly -1/3), the conclusion is:")
print()
print("  Mechanism (a) [FW Prop 4.1 / eq (4.3) auxiliary Hamiltonian]")
print("  does NOT structurally produce the project's -1/3 null-sum")
print("  offset under any straightforward symbolic pull-back to the")
print("  V_quad image parameter point.")
print()
print("Verdict bin (mechanism (a)): NO_GO_OFF_DEGENERATION")
print()
print("Cascade implication: 069r3 FINAL synthesis treats mechanism (a)")
print("as ruled out for this Route B path. The cascade falls back to")
print("mechanism (b) additive shift (-1/12 per coordinate working")
print("hypothesis logged in 110 prestage UF-110-2 fallback note) or")
print("(c) Sakai surface-type artefact gated to Route F machinery.")
print()

# ----------------------------------------------------------------
# C.5 -- emit results JSON
# ----------------------------------------------------------------

results = {
    "fw_4_1_th_form": str(sp.expand(tH_fw_4_1)),
    "fw_4_3_h_form": str(sp.expand(h_fw_4_3)),
    "fw_4_3_shift_decomposition": {
        "c_quadratic_in_v1": str(shift_quadratic_in_v1),
        "c_t_linear": str(shift_t_linear),
    },
    "v_quad_pullback_under_three_orderings": {
        "ordering_1_eta_inf_theta_inf_surviving": result_o1,
        "ordering_2_theta_0_theta_inf_surviving": result_o2,
        "ordering_3_uf_110_3_anchored": result_o3,
    },
    "comparison_to_minus_one_third": {
        "target_offset": "-1/3",
        "ordering_1": cmp_o1,
        "ordering_2": cmp_o2,
        "ordering_3": cmp_o3,
        "any_ordering_matches": (
            cmp_o1["constant_matches_target"]
            or cmp_o1["t_coeff_matches_target"]
            or cmp_o2["constant_matches_target"]
            or cmp_o2["t_coeff_matches_target"]
            or cmp_o3["constant_matches_target"]
            or cmp_o3["t_coeff_matches_target"]
        ),
    },
    "mechanism_a_verdict_bin": "NO_GO_OFF_DEGENERATION",
    "verdict_basis": (
        "Phase B obstructions (i)+(ii)+(iii)  AND  Phase C "
        "FW (4.3) shift constants {1/144, 1/16, -1/2} all unequal "
        "to target -1/3."
    ),
    "sympy_version": sp.__version__,
}

out_path = Path(__file__).with_name("phase_c_results.json")
out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

print(f"--- C.5: results written to {out_path.name}")
print()
print("PHASE C END.")
