"""Phase D.2 — numerical cross-check follow-up to 058R UPGRADE_V1_0_PARTIAL_NUMERICAL.

Session: 069 CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL.

This script attempts the four-step Phase D.2 sub-tasks (a) KNY pull at
V_quad parameter point, (b) symbolic gauge transformation construction
between V_quad's scalar-OGF Lax representation and KNY 2017 §8.5.17
eq. 8.239 second-order Lax form, (c) |det J(Phi_symp)| numerical
evaluation at the V_quad parameter point, (d) BLMP 2024 §4.28
connection-matrix evaluation at the KNY-side (a_1, a_2) parameter
point that corresponds to V_quad under the M-pullback, and (e) the
cross-check residual

    Delta = | |M^* C_V| - |S_{zeta_*}^can| | / max(|M^* C_V|, |S_{zeta_*}^can|)

against the verdict-ladder thresholds (FULL: <1e-5; PRECISION_DEGRADED:
[1e-5, 1e-2); MISMATCH: >=1e-2; PERSIST: incomputable).

Substrate (read-only; SHA-anchored):

    058R phase_a_birkhoff_match.py SHA 7B4DD7636A3D9AD3..
    058R phase_b_canonical_map.md  SHA F831F9BD58D1F306..
    KNY 2017 §8.5.17 eq. 8.239 (slot anchor g3b_2026-05-03 KNY 2017 PDF)
    BL2024 §4 eq. 4.28 (slot 08 SHA 96c49cdd..)
    H4 measurement (V_quad native): C = 8.12733679549507... (>=108 dps)

Open residuals carried forward from 058R (R1 closure):

    D1: R1 (Okamoto-convention identification of CT v1.3 §3.5 four-tuple
        (1/6, 0, 0, -1/2)) carry-forward open from 2026-05-02 partial.
    D2: the four-tuple sums to -1/3, violating Okamoto null-sum
        alpha_inf + alpha_0 + beta_inf + beta_0 = 0; the null-sum
        violation requires either an additional (a_0, a_1, a_2)-chart
        shift or a tau-function reparametrisation, neither of which
        is closed-form in the agent budget.
    D5: explicit gauge transformation G(x) between V_quad ODE and
        KNY L_1 = 0 requires R1 closure plus closed-form expansion
        of the Lax pair around its irregular singular point of
        Poincare rank 1.

Per envelope PRE-CONDITION 2 default (B), R1 is OUT OF SCOPE for 069.
This script therefore documents the obstruction map at each sub-step
and surfaces the runtime-fallback HALT_069_R1_SCOPE_AMBIGUOUS at
Phase D.2.d substrate-pull, routing the verdict to
UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST.
"""
from __future__ import annotations

import sympy as sp
from mpmath import mp, mpf, mpc, pi as mp_pi, sqrt as mp_sqrt

mp.dps = 50


# =====================================================================
# Phase D.2.a -- KNY 2017 §8.5.17 differential Lax pull at V_quad
#                parameter point (substrate-pull only; R1-gated)
# =====================================================================

def phase_d_2_a_kny_pull():
    """Symbolic transcription of KNY 2017 §8.5.17 eq. 8.237 (Hamiltonian)
    and eq. 8.239 (differential Lax pair). At V_quad parameter point
    the (a_1, a_2) values are R1-gated and not pinned."""
    print("=" * 72)
    print("Phase D.2.a -- KNY 2017 §8.5.17 differential Lax pull")
    print("=" * 72)

    x, q, p, t = sp.symbols("x q p t", complex=True)
    a0, a1, a2 = sp.symbols("a_0 a_1 a_2", complex=True)
    H_KNY = sp.symbols("H", cls=sp.Function)(t)

    # KNY 2017 eq. 8.237 (Hamiltonian H_{D_6}^{KNY})
    H_expr = (1 / t) * (p * (p - 1) * q**2 + (a1 + a2) * q * p + t * p - a2 * q)
    print("\nKNY 2017 eq. 8.237 (Hamiltonian H_{D_6}^{KNY}):")
    print(f"  H = (1/t) * [p(p-1) q^2 + (a_1 + a_2) q p + t p - a_2 q]")
    print(f"     with a_0 + a_1 = 1.")

    # KNY 2017 eq. 8.239 (differential Lax form L_1)
    # L_1 = {-a_2/x + pq/(x(x-q)) - tH/x^2}
    #     + {(1+a_1+a_2)/x - 1/(x-q) + t/x^2 - 1} * d/dx
    #     + d^2/dx^2
    rho_0 = -a2 / x + p * q / (x * (x - q)) - t * H_KNY / x**2
    rho_1 = (1 + a1 + a2) / x - 1 / (x - q) + t / x**2 - 1
    print("\nKNY 2017 eq. 8.239 (Lax operator L_1):")
    print("  L_1 = rho_0(x; q, p, t, a_1, a_2)")
    print("      + rho_1(x; q, a_1, a_2, t) * d/dx")
    print("      + d^2/dx^2")
    print(f"  rho_0 = -a_2/x + p q / (x (x-q)) - t H / x^2")
    print(f"  rho_1 = (1 + a_1 + a_2)/x - 1/(x-q) + t/x^2 - 1")

    # V_quad parameter point in CT v1.3 §3.5 four-tuple form
    print("\nV_quad parameter point (CT v1.3 §3.5):")
    print(f"  (alpha_inf, alpha_0, beta_inf, beta_0) = (1/6, 0, 0, -1/2)")
    null_sum = sp.Rational(1, 6) + 0 + 0 + sp.Rational(-1, 2)
    print(f"  Okamoto null-sum: alpha_inf+alpha_0+beta_inf+beta_0 = {null_sum}")
    print(f"  ANOMALY D2: null-sum != 0; sums to -1/3.")

    print("\n[STATUS] R1 (CT four-tuple -> KNY (a_0, a_1, a_2)) carry-forward")
    print("         open per 058R + envelope PRE-CONDITION 2 default (B).")
    print("         (a_1, a_2) at V_quad point: NOT PINNED.")
    print("         Phi_resc scalar lambda = 1/3 (058R Phase B PINNED).")
    print("         Phi_shift parameter t_0 = -4*sqrt(3) (058R Phase B PINNED).")

    return {
        "H_KNY_symbolic": H_expr,
        "rho_0_symbolic": rho_0,
        "rho_1_symbolic": rho_1,
        "null_sum": null_sum,
        "lambda_resc": sp.Rational(1, 3),
        "t_shift": -4 * sp.sqrt(3),
        "R1_status": "OPEN",
    }


# =====================================================================
# Phase D.2.b -- symbolic gauge transformation construction
# =====================================================================

def phase_d_2_b_gauge():
    """Attempt the symbolic gauge transformation G(x) such that
    L_1^V_quad(x) o G = G o L_1^KNY(x) at the V_quad parameter point."""
    print("\n" + "=" * 72)
    print("Phase D.2.b -- symbolic gauge transformation construction")
    print("=" * 72)

    z, u = sp.symbols("z u", complex=True)
    f = sp.Function("f")

    # V_quad scalar OGF ODE (058R Phase A; 7B4DD763.. SHA-anchored):
    #   3 z^3 f''(z) + 10 z^2 f'(z) + (5 z + z^2 - 1) f(z) = 0
    ode_V = 3 * z**3 * f(z).diff(z, 2) + 10 * z**2 * f(z).diff(z) + (5 * z + z**2 - 1) * f(z)
    print("\nV_quad scalar OGF ODE (z-coordinate; 058R Phase A):")
    print(f"  3 z^3 f'' + 10 z^2 f' + (z^2 + 5 z - 1) f = 0")
    print(f"  order: 2 (NOT 3 -- envelope wording 'third-order' refers to")
    print(f"  the Newton-polygon-edge slope being non-trivial, not derivative order)")

    # Compute Schwarzian invariant (Liouville normal form) of V_quad's ODE
    # For y'' + p(z) y' + q(z) y = 0, the Schwarzian invariant after
    # gauge transformation y = exp(-int p/2) v is
    #   I = q - p^2/4 - p'/2.
    p_V = sp.Rational(10, 3) / z  # = 10 z^2 / (3 z^3)
    q_V = (5 * z + z**2 - 1) / (3 * z**3)
    I_V = sp.simplify(q_V - p_V**2 / 4 - sp.diff(p_V, z) / 2)
    print(f"\nV_quad Liouville normal-form invariant I_V(z):")
    print(f"  I_V(z) = {sp.together(I_V)}")

    # Apply Phi_resc: z = t/3, t = 3 z. So d/dz = 3 d/dt, etc.
    # This gives a different I_V(t/3) we can compare with KNY's I_KNY(x)
    # at the relevant parameter point. KNY's I_KNY depends on (q, p, t, a_1, a_2)
    # so requires R1 closure (for a_1, a_2) plus Hamiltonian flow integration
    # (for q(t), p(t)) at t_0 = -4 sqrt(3) (post-shift).

    print("\nKNY L_1 invariant I_KNY(x; q, p, t, a_1, a_2):")
    print("  I_KNY = rho_0 - rho_1^2/4 - rho_1'/2")
    print("  -- closed-form requires (a_1, a_2) (R1-gated) + (q(t_0), p(t_0))")
    print("     (Hamiltonian flow integration at t_0 = -4 sqrt(3)).")
    print("  -- neither is in scope for 069 default (B) PRE-CONDITION.")

    print("\n[OBSTRUCTION] Closed-form symbolic gauge G(x) requires:")
    print("  1. R1 closure -> (a_1, a_2) at V_quad point;")
    print("  2. Hamiltonian flow integration of KNY system at t_0 = -4 sqrt(3);")
    print("  3. Schwarzian invariant matching I_V(z(x)) == I_KNY(x).")
    print("  Steps 1+2 are R1-gated; step 3 is conditional on step 1+2 outputs.")
    print("\n[TRIGGER] HALT_069_GAUGE_TRANSFORM_FAILURE candidate at envelope-")
    print("          tier; surfaced for Phase F handoff judgment-call selection.")

    return {
        "I_V_symbolic": I_V,
        "p_V": p_V,
        "q_V": q_V,
        "gauge_status": "OBSTRUCTED_R1_GATED",
    }


# =====================================================================
# Phase D.2.c -- |det J(Phi_symp)| numerical evaluation
# =====================================================================

def phase_d_2_c_jacobian():
    """Numerical evaluation of |det J(Phi_symp)| at V_quad parameter
    point. Phi_symp is the gauge transform from V_quad's scalar-OGF
    representation to KNY 2017 §8.5.17 second-order scalar Lax form."""
    print("\n" + "=" * 72)
    print("Phase D.2.c -- |det J(Phi_symp)| numerical evaluation")
    print("=" * 72)

    # 058R Phase B established structurally:
    #   det J(Phi_resc) = lambda^2 = (1/3)^2 = 1/9 on (q, p), * 1 on t.
    #   det J(Phi_shift) = 1.
    #   det J(Phi_symp) = open numerical residual at V_quad parameter point.
    lam = sp.Rational(1, 3)
    det_resc = lam**2
    det_shift = sp.Integer(1)
    print(f"\ndet J(Phi_resc) = lambda^2 = {det_resc} (058R Phase B PINNED)")
    print(f"det J(Phi_shift) = {det_shift} (058R Phase B PINNED)")

    print(f"\ndet J(Phi_symp) at V_quad parameter point:")
    print(f"  -- depends on the explicit gauge G(x) from Phase D.2.b;")
    print(f"  -- gauge G(x) is OBSTRUCTED_R1_GATED at envelope-tier;")
    print(f"  -- numerical Jacobian factor: NOT COMPUTABLE in this session.")

    print(f"\nStructural form (058R phase_b_canonical_map.md F831F9BD..):")
    print(f"  Phi_symp is the canonical (q, p) <-> (q, p) gauge transformation")
    print(f"  identifying Okamoto 1987 H_III with KNY 2017 H_{{D_6}}^{{KNY}}.")
    print(f"  Mapping is bijective on relevant chart; Jacobian non-degenerate.")
    print(f"  Numerical value at V_quad point requires explicit gauge G(x).")

    print(f"\n[STATUS] Phase D.2.c numerical Jacobian: NOT COMPUTABLE")
    print(f"         (R1-gated via Phase D.2.b obstruction).")
    return {
        "det_resc": det_resc,
        "det_shift": det_shift,
        "det_symp_status": "NOT_COMPUTABLE_R1_GATED",
    }


# =====================================================================
# Phase D.2.d -- BLMP 2024 §4.28 connection-matrix evaluation
# =====================================================================

def phase_d_2_d_bl2024():
    """Attempt BLMP 2024 §4 connection-matrix integral evaluation
    at the KNY-side (a_1, a_2) parameter point that corresponds to
    the V_quad parameter point under the M-pullback. R1-gated."""
    print("\n" + "=" * 72)
    print("Phase D.2.d -- BLMP 2024 §4.28 connection-matrix evaluation")
    print("=" * 72)

    # BLMP 2024 §4 connection-matrix integral (eq. 4.28) gives
    # |S_{zeta_*}^can| as a function of monodromy parameters
    # (e_1, e_2) in (C^*)^2 (Definition 1.3, eq. 1.16). Conversion
    # from KNY (a_1, a_2) to BLMP (e_1, e_2) requires the explicit
    # formula at slot 08 BLMP 2024 §4 + (a_1, a_2) values from R1.

    print("\nBLMP 2024 §4 connection-matrix formula (eq. 4.28):")
    print("  |S_{zeta_*}^can| = | integrand(e_1, e_2; a_1, a_2) |")
    print("  with monodromy parameters (e_1, e_2) in (C^*)^2")
    print("  (BLMP 2024 Definition 1.3, eq. 1.16).")

    print("\n[STATUS] (a_1, a_2) at V_quad parameter point: NOT PINNED")
    print("         (R1 carry-forward open per 058R + envelope PRE-CONDITION 2).")
    print("         BLMP 2024 §4.28 integrand at V_quad point: NOT EVALUABLE.")
    print("         |S_{zeta_*}^can| at V_quad point: NOT COMPUTABLE in this session.")

    print("\n[TRIGGER] Runtime-fallback HALT_069_R1_SCOPE_AMBIGUOUS surfaced")
    print("          (NOT halt-listed in envelope; runtime-safety fallback only;")
    print("           operator-decidable PRE-CONDITION 2 default = (B) routes")
    print("           to clean halt for 069r1 preflight relay).")

    # H4 baseline available without R1:
    print("\nH4 baseline (V_quad-native; PINNED at >=108 dps):")
    mp.dps = 50
    C_V_str = "8.127336795495072367112578732020"  # 30 digits
    C_V = mpf(C_V_str)
    abs_S_zeta = 2 * mp_pi * C_V
    print(f"  |C_V|        = {C_V}")
    print(f"  |S_{{zeta_*}}^V| = 2 pi C_V (V_quad native; pre-canonical):")
    print(f"               = {abs_S_zeta}")
    print(f"  (THIS IS THE V_quad-NATIVE Stokes amplitude, not the BLMP")
    print(f"   canonical-form value. The cross-check requires |M^* C_V|")
    print(f"   on the LEFT and INDEPENDENT |S_{{zeta_*}}^can| from BLMP §4.28")
    print(f"   on the RIGHT. Without R1 the right-hand side is incomputable.)")

    return {
        "C_V": C_V,
        "abs_S_zeta_V_native": abs_S_zeta,
        "abs_S_zeta_canonical_status": "NOT_COMPUTABLE_R1_GATED",
        "BL2024_evaluation_status": "NOT_COMPUTABLE_R1_GATED",
    }


# =====================================================================
# Phase D.2.e -- cross-check + verdict selection
# =====================================================================

def phase_d_2_e_verdict(d2a, d2b, d2c, d2d):
    """Compute Delta and select honest verdict per envelope verdict ladder."""
    print("\n" + "=" * 72)
    print("Phase D.2.e -- cross-check + verdict selection")
    print("=" * 72)

    print("\nCross-check identity (058R phase_d_verdict.md L62-95):")
    print("  | M^* C_V |  ?=  | S_{zeta_*}^can |")

    print("\nLeft-hand side  | M^* C_V |:")
    print(f"  |C_V|                    = {d2d['C_V']} (H4; PINNED)")
    print(f"  | det J(Phi_resc) |      = {d2c['det_resc']} (058R Phase B; PINNED)")
    print(f"  | det J(Phi_shift) |     = {d2c['det_shift']} (058R Phase B; PINNED)")
    print(f"  | det J(Phi_symp) |      = {d2c['det_symp_status']}")
    print(f"  -> | M^* C_V |             NOT COMPUTABLE without Phase D.2.b output.")

    print("\nRight-hand side | S_{zeta_*}^can |:")
    print(f"  BL2024 §4.28 evaluation  = {d2d['BL2024_evaluation_status']}")
    print(f"  -> | S_{{zeta_*}}^can |     NOT COMPUTABLE without R1 closure.")

    print("\nDelta = | LHS - RHS | / max(LHS, RHS):")
    print(f"  Delta status              = INCOMPUTABLE")
    print(f"  Reason                    = both LHS and RHS R1-gated")

    print("\nVerdict-ladder selection (envelope §VERDICT LADDER):")
    print(f"  UPGRADE_V1_0_FULL                            (Delta < 1e-5)        : NOT MET")
    print(f"  UPGRADE_V1_0_PARTIAL_NUMERICAL_PRECISION_DEGRADED                    : NOT MET")
    print(f"  HALT_069_STOKES_NUMERICAL_MISMATCH           (Delta >= 1e-2)        : NOT MET")
    print(f"  UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST       (Delta incomputable)   : SELECTED")

    print("\nSelected verdict: UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST")
    print("  (058R verdict UPGRADE_V1_0_PARTIAL_NUMERICAL re-confirmed at 069;")
    print("   no progress on the residual; refire requires either")
    print("   (a) operator dispatch of 069r1 R1-closure preflight, or")
    print("   (b) extended agent budget for inline R1 closure (PRE-COND 2 path A).)")

    return {
        "delta_status": "INCOMPUTABLE",
        "verdict": "UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST",
        "M6_CC_status": "STRUCTURALLY_CLOSED_AT_058R; numerical residual unchanged",
        "M9_gating_status": "{M6.CC numerical residual} (no change from 058R)",
    }


def main():
    print("Phase D.2 numerical follow-up to 058R.")
    print(f"mpmath dps = {mp.dps}")
    print()
    d2a = phase_d_2_a_kny_pull()
    d2b = phase_d_2_b_gauge()
    d2c = phase_d_2_c_jacobian()
    d2d = phase_d_2_d_bl2024()
    d2e = phase_d_2_e_verdict(d2a, d2b, d2c, d2d)

    print("\n" + "=" * 72)
    print("Phase D.2 summary")
    print("=" * 72)
    print(f"  Phase D.2.a (KNY pull):                substrate captured; R1-gated parameter point")
    print(f"  Phase D.2.b (gauge transformation):    OBSTRUCTED_R1_GATED")
    print(f"  Phase D.2.c (|det J(Phi_symp)|):       NOT_COMPUTABLE_R1_GATED")
    print(f"  Phase D.2.d (BL2024 §4.28):            NOT_COMPUTABLE_R1_GATED")
    print(f"  Phase D.2.e (cross-check + verdict):   UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST")
    print()
    print(f"Verdict: {d2e['verdict']}")
    print(f"M6.CC status: {d2e['M6_CC_status']}")
    print(f"M9 gating: {d2e['M9_gating_status']}")


if __name__ == "__main__":
    main()
