"""
phase_a_path_alpha.py — 071 M6-CC-R1-CLOSURE-PREFLIGHT-069R1 Path α script.

Purpose: produce verifiable sympy artefacts documenting the path α
chart-shift attempt at the V_quad parameter point. Per envelope STEP
A.1.5, the explicit (a_0, a_1, a_2) -> (alpha_inf, alpha_0, beta_inf,
beta_0) chart-map IS the open R1 itself (058R phase_b_canonical_map.md
L136-140; SHA F831F9BD58D1F306..). A.1.5.F1 (substrate gap) is therefore
TRIGGERED at fire time. This script:

  (1) sympy-verifies the Okamoto null-sum violation -1/3 != 0.
  (2) sympy-derives Delta_0 + Delta_1 = 0 (E2) from KNY a_0 + a_1 = 1.
  (3) sympy-verifies V_quad scalar-OGF Liouville invariant
      I_V(z) = (3 z^2 + 5 z - 3) / (9 z^3) by re-derivation from
      ODE coefficients p_V(z) = 10/(3 z), q_V(z) = (z^2+5z-1)/(3 z^3)
      via I_V = q_V - (1/4) p_V^2 - (1/2) p_V'.
  (4) declares the (E1) null-sum-restoration constraint formally
      via abstract sympy.Function placeholders f_alpha_inf, f_alpha_0,
      f_beta_inf, f_beta_0 — NOT fabricated closed forms. The script
      documents that these placeholders are NOT substrate-supplied
      and therefore the (E1) system cannot be solved at fire time.

NOTE on component-order discipline (per envelope STEP A.1.5):
  This script uses the KNY 2017 §8.5.17 component order
  (a_0, a_1, a_2). The project-wide PCF tuple-ordering convention
  [a2, a1, a0] (LEADING-FIRST) does NOT apply here — KNY chart != PCF
  tuple. Symbol names: a0, a1, a2 (no zero-indexed prefix).

Substrate anchors (read-only at fire time):
  058R phase_b_canonical_map.md     SHA F831F9BD58D1F306..
  058R phase_a_birkhoff_match.py    SHA 7B4DD7636A3D9AD3..
  058R phase_b5_affine_weyl_crosswalk.md SHA B9D4FFD2F279A33C..
  069  phase_d_numerical.md         SHA E98D74EBD30EB43C..
  069  phase_d_numerical.py         SHA 89D9EEFC57D9FA47..
"""

from sympy import (
    Symbol, Rational, sqrt, simplify, expand, diff, solve, Eq,
    Function, latex
)


def main():
    print("=" * 70)
    print("071 M6-CC-R1-CLOSURE-PREFLIGHT-069R1 Path alpha -- sympy run")
    print("=" * 70)

    # -----------------------------------------------------------------
    # STEP 1 — Okamoto null-sum violation at V_quad parameter point
    # -----------------------------------------------------------------
    print("\n[STEP 1] Okamoto null-sum at V_quad parameter point")
    alpha_inf = Rational(1, 6)
    alpha_0 = Rational(0)
    beta_inf = Rational(0)
    beta_0 = Rational(-1, 2)
    null_sum = alpha_inf + alpha_0 + beta_inf + beta_0
    print(f"  (alpha_inf, alpha_0, beta_inf, beta_0) "
          f"= ({alpha_inf}, {alpha_0}, {beta_inf}, {beta_0})")
    print(f"  null_sum = alpha_inf + alpha_0 + beta_inf + beta_0 = {null_sum}")
    assert null_sum == Rational(-1, 3), "expected -1/3"
    print(f"  -> -1/3 != 0; Okamoto null-sum VIOLATED (anomaly D2)")

    # -----------------------------------------------------------------
    # STEP 2 — KNY linear relation invariance => Delta_0 + Delta_1 = 0
    # -----------------------------------------------------------------
    print("\n[STEP 2] KNY linear-relation invariance (E2)")
    a0, a1, a2 = Symbol('a0', real=True), Symbol('a1', real=True), Symbol('a2', real=True)
    D0, D1, D2 = Symbol('D0', real=True), Symbol('D1', real=True), Symbol('D2', real=True)
    pre_rel = Eq(a0 + a1, 1)
    post_rel = Eq((a0 + D0) + (a1 + D1), 1)
    print(f"  pre-shift KNY relation:  {pre_rel}")
    print(f"  post-shift KNY relation: {post_rel}")
    # subtract pre from post -> Delta_0 + Delta_1 = 0
    e2 = simplify(post_rel.lhs - post_rel.rhs - (pre_rel.lhs - pre_rel.rhs))
    print(f"  (post - pre) simplified: {e2}")
    e2_solution = solve(e2, D1)
    print(f"  (E2) closed-form: D1 = {e2_solution[0]}")
    assert e2_solution[0] == -D0, "expected D1 = -D0"
    print(f"  -> (E2) PASS: Delta_0 + Delta_1 = 0")

    # -----------------------------------------------------------------
    # STEP 3 — V_quad Liouville invariant re-derivation
    # -----------------------------------------------------------------
    print("\n[STEP 3] V_quad scalar-OGF Liouville invariant re-derivation")
    z = Symbol('z', real=True, positive=True)
    p_V = Rational(10, 3) / z              # p_V(z) = 10/(3 z)
    q_V = (z**2 + 5*z - 1) / (3 * z**3)    # q_V(z) = (z^2+5z-1) / (3 z^3)
    I_V = simplify(q_V - Rational(1, 4) * p_V**2 - Rational(1, 2) * diff(p_V, z))
    I_V_canon = (3 * z**2 + 5 * z - 3) / (9 * z**3)
    print(f"  p_V(z) = {p_V}")
    print(f"  q_V(z) = {q_V}")
    print(f"  I_V(z) = q_V - (1/4) p_V^2 - (1/2) p_V'")
    print(f"         = {I_V}")
    print(f"  069 anchor:")
    print(f"  I_V(z) = (3 z^2 + 5 z - 3) / (9 z^3) = {I_V_canon}")
    diff_I = simplify(I_V - I_V_canon)
    print(f"  difference (sympy-simplified): {diff_I}")
    assert diff_I == 0, "expected zero difference"
    print(f"  -> Liouville invariant MATCHES 069 substrate at SHA E98D74EBD30EB43C..")

    # -----------------------------------------------------------------
    # STEP 4 — Pinned Phi_resc + Phi_shift parameters at V_quad
    # -----------------------------------------------------------------
    print("\n[STEP 4] 058R Phase B pinned parameters at V_quad")
    c0 = 2 / sqrt(3)
    lam = simplify(c0**2 / 4)
    # 058R substrate: t_0 = -zeta_*/lambda where zeta_* = 4/sqrt(3) is the
    # leading-edge irregular-singular-point coordinate (Phase A scaling),
    # giving t_0 = -(4/sqrt(3))/(1/3) = -3*4/sqrt(3) = -4*sqrt(3).
    zeta_star = 4 / sqrt(3)
    t0 = simplify(-zeta_star / lam)
    print(f"  c_0 = 2/sqrt(3); lambda = c_0^2/4 = {lam}")
    print(f"  zeta_* = 4/sqrt(3); t_0 = -zeta_*/lambda = {t0}")
    assert lam == Rational(1, 3), "expected lambda = 1/3"
    assert simplify(t0 + 4 * sqrt(3)) == 0, "expected t_0 = -4*sqrt(3)"
    print(f"  -> 058R Phase B pin: lambda = 1/3, t_0 = -4*sqrt(3) (verified)")

    # -----------------------------------------------------------------
    # STEP 5 — Path α (E1) substrate-gap detection (A.1.5.F1)
    # -----------------------------------------------------------------
    print("\n[STEP 5] Path alpha (E1) null-sum restoration -- A.1.5 substrate gap")
    print("  Required: closed-form expressions for f_alpha_inf, f_alpha_0,")
    print("            f_beta_inf, f_beta_0 as functions of (a_0, a_1, a_2)")
    print("            from 058R + 069 substrate.")
    print("  Substrate search result:")
    print("    058R phase_b_canonical_map.md L136-140:")
    print("      'explicit conversion of CT v1.3 sec.3.5 4-tuple")
    print("       (alpha_inf, alpha_0, beta_inf, beta_0) = (1/6, 0, 0, -1/2)")
    print("       to KNY (a_0, a_1, a_2) -- this is residual R1 partially closed'")
    print("    058R phase_b5_affine_weyl_crosswalk.md L88-89:")
    print("      'alpha = 4(1+2 a_0 - 2 a_1), beta = -4(1+a_0-a_1),")
    print("       gamma = 4, delta = -4'")
    print("      [these are P_III equation coeffs (alpha,beta,gamma,delta);")
    print("       NOT Okamoto's four-tuple (alpha_inf, alpha_0, beta_inf, beta_0)]")
    print("    069 phase_d_numerical.md zero hits for f_alpha or chart-map")
    # Declare placeholders (NOT fabricated closed forms)
    f_alpha_inf = Function('f_alpha_inf')(a0, a1, a2)
    f_alpha_0 = Function('f_alpha_0')(a0, a1, a2)
    f_beta_inf = Function('f_beta_inf')(a0, a1, a2)
    f_beta_0 = Function('f_beta_0')(a0, a1, a2)
    print("  Abstract placeholders (not substrate-supplied):")
    print(f"    f_alpha_inf(a_0, a_1, a_2) = {f_alpha_inf}")
    print(f"    f_alpha_0(a_0, a_1, a_2)   = {f_alpha_0}")
    print(f"    f_beta_inf(a_0, a_1, a_2)  = {f_beta_inf}")
    print(f"    f_beta_0(a_0, a_1, a_2)    = {f_beta_0}")
    print("  (E1) constraint: f_alpha_inf(a_0+D_0, a_1+D_1, a_2+D_2)")
    print("                 + f_alpha_0(a_0+D_0, a_1+D_1, a_2+D_2)")
    print("                 + f_beta_inf(a_0+D_0, a_1+D_1, a_2+D_2)")
    print("                 + f_beta_0(a_0+D_0, a_1+D_1, a_2+D_2) = 0")
    print("  STATUS: NotImplemented_substrate_gap")
    print("  -> A.1.5.F1 TRIGGERED")
    print("  -> Path alpha closed without producing closed-form (a_1', a_2')")
    print("  -> verdict path: NO_GO_PATH_ALPHA via A.1.5.F1")
    print("  -> envelope verdict: NO_GO_SUBSTRATE_INSUFFICIENT")

    # -----------------------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("Path alpha sympy run summary")
    print("=" * 70)
    print(f"  Okamoto null-sum at V_quad:      -1/3 != 0 (anomaly D2)")
    print(f"  KNY linear-relation invariance:  D_0 + D_1 = 0 (E2 closed-form)")
    print(f"  V_quad Liouville invariant:      MATCHES 069 substrate")
    print(f"  058R Phase B pin:                lambda=1/3, t_0=-4*sqrt(3)")
    print(f"  Explicit four-tuple map:         ABSENT from 058R + 069 substrate")
    print(f"  A.1.5.F1 (substrate gap):        TRIGGERED")
    print(f"  Phase A.3 (a_1, a_2) extraction: NOT REACHED")
    print(f"  Path alpha verdict:              NO_GO_PATH_ALPHA via A.1.5.F1")
    print()
    print("END phase_a_path_alpha.py")


if __name__ == "__main__":
    main()
