"""
Phase A — Symbolic derivation of indicial polynomial chi_d(c)
            for the SIARC PCF Wallis-convergent recurrence at infinity.

Task: T1-BIRKHOFF-PHASE2-LIFT-LOWER, Phase A.

Setup:
    Recurrence (PCF-1 v1.3 §2.a): p_n = b_n p_{n-1} + a_n p_{n-2}
    Or equivalently: p_n - b_n p_{n-1} - a_n p_{n-2} = 0  (linear difference equation)

    Three SIARC conventions for the polynomial degrees of (a_n, b_n) in n:
      α-direction (PCF-1 v1.3 §6 Thm 5):  deg a = d-1, deg b = d
      symmetric (gap_proposition §1):     deg a = d,   deg b = d
      δ-direction (PCF-2 §-classifier):   deg a = d+1, deg b = d

Ansatz (Birkhoff 1930 §1 + B-T 1933 §1 normal case, p=1):
    y(n) = Γ(n)^μ · γ^n · n^ρ · S(1/n)
    where S(t) = 1 + s_1 t + s_2 t^2 + ... is a formal power series.

    log y(n) = μ log Γ(n) + n log γ + ρ log n + log S(1/n)
             = μ (n log n - n + (1/2) log(2π n) + ...) + n log γ + ρ log n + ...
             = μ n log n + (log γ - μ) n + (μ/2 + ρ) log n + ...

    So the asymptotic ansatz has:
        coefficient of  n log n :  μ
        coefficient of  n       :  log γ - μ
        coefficient of  log n   :  μ/2 + ρ

Phase A.1-A.3: derive the leading-order equation in n for the (μ, γ) pair.

A_PCF (the SIARC error decay coefficient) relates to (μ_dom, μ_sub) via:
    |δ_n| ~ |y_sub(n) / y_dom(n)|  at leading order
    log|δ_n| ~ (μ_sub - μ_dom) n log n + ...
    A = -(μ_sub - μ_dom) = μ_dom - μ_sub

Output: print analysis at d ∈ {2, 3, 4} for all three conventions; compare with PCF-1 v1.3 §6.
"""

import sympy as sp
from sympy import symbols, Rational, expand, simplify, solve, Poly, factor, log, Symbol, S, gamma
from sympy.abc import n, c, mu, gamma as sym_gamma, rho
import json
import hashlib

print("=" * 78)
print("PHASE A — Symbolic derivation of formal exponents")
print("=" * 78)
print()

def analyze_recurrence(d, conv_name, deg_a, deg_b):
    """
    Analyze the formal solutions of the recurrence
        y(n) - b_n y(n-1) - a_n y(n-2) = 0
    where b_n, a_n are polynomials in n of degrees deg_b, deg_a.

    Returns (μ_dom, γ_dom, μ_sub, γ_sub, A_predicted).
    """
    print(f"--- d = {d}, convention = {conv_name} (deg a = {deg_a}, deg b = {deg_b}) ---")

    # Symbolic leading coefficients
    c_a, c_b, mu_s, gamma_s, n_s = symbols('c_a c_b mu gamma n', positive=False, real=True)

    # b_n ~ c_b n^{deg_b} (1 + lower)
    # a_n ~ c_a n^{deg_a} (1 + lower)
    # ratio y(n)/y(n-1) ~ n^μ γ (using Γ(n)/Γ(n-1) = n-1 ≈ n)
    # ratio y(n)/y(n-2) ~ n^{2μ} γ^2

    # Substitute into y(n) - b_n y(n-1) - a_n y(n-2) = 0 and divide by y(n):
    #   1 - b_n n^{-μ}/γ - a_n n^{-2μ}/γ^2 = 0
    # Leading order in n:
    #   1 - c_b n^{deg_b - μ}/γ - c_a n^{deg_a - 2μ}/γ^2 = 0

    # Three balance possibilities:
    #   (I)  Term {n^0=1} balances {c_b n^{deg_b-μ}/γ}:  deg_b - μ = 0 → μ = deg_b
    #        Then deg_a - 2μ = deg_a - 2 deg_b. Subdominant if < 0.
    #        Equation: γ = c_b.
    #
    #   (II) Term {1} balances {c_a n^{deg_a-2μ}/γ^2}:  deg_a - 2μ = 0 → μ = deg_a/2
    #        Then deg_b - μ = deg_b - deg_a/2. Subdominant if < 0.
    #
    #   (III) The two RHS terms balance each other: deg_b - μ = deg_a - 2μ → μ = deg_a - deg_b
    #         Then both at order n^{deg_b - μ} = n^{deg_b - deg_a + deg_b} = n^{2 deg_b - deg_a}.
    #         If positive, RHS dominates LHS=1; the leading equation is
    #             c_b n^{...}/γ + c_a n^{...}/γ^2 = 0 → γ = -c_a/c_b.
    #         (Subleading correction: 1 = lower order; OK.)
    #
    # For the SIARC PCF cases, balance (I) gives the dominant solution (μ_dom = deg_b),
    # and balance (III) gives the subdominant solution.

    mu_dom = deg_b
    gamma_dom = "c_b"
    print(f"  Balance (I)   dominant solution:  μ_dom = {mu_dom}, γ_dom = c_b")
    print(f"     (subdominant check: deg_a - 2μ_dom = {deg_a} - {2*deg_b} = {deg_a - 2*deg_b}"
          f" {'< 0 ✓' if deg_a - 2*deg_b < 0 else '≥ 0 — not subdominant!'})")

    # Balance (III): μ = deg_a - deg_b
    mu_sub = deg_a - deg_b
    gamma_sub = "-c_a / c_b"
    if 2*deg_b - deg_a > 0:
        print(f"  Balance (III) subdominant solution: μ_sub = {mu_sub}, γ_sub = -c_a/c_b")
        print(f"     (RHS dominates LHS check: 2 deg_b - deg_a = {2*deg_b - deg_a} > 0 ✓)")
    else:
        print(f"  Balance (III) DEGENERATE: μ_sub = {mu_sub}, γ_sub = -c_a/c_b "
              f"but 2 deg_b - deg_a = {2*deg_b - deg_a} ≤ 0; further analysis needed")

    # Predicted A = μ_dom - μ_sub
    A_pred = mu_dom - mu_sub
    print(f"  PREDICTION: A = μ_dom - μ_sub = {mu_dom} - ({mu_sub}) = {A_pred}")
    print(f"  TARGET (Conjecture B4): A = 2d = {2*d}")
    print(f"  MATCH B4? {'YES ✓' if A_pred == 2*d else 'NO ✗ (DRIFT by ' + str(2*d - A_pred) + ')'}")
    print()
    return (mu_dom, gamma_dom, mu_sub, gamma_sub, A_pred)


print("\n[A.1-A.4] Analysis at d = 2, 3, 4 for three conventions")
print("=" * 78)
results = []
for d in [2, 3, 4]:
    print(f"\n══ DEGREE d = {d} ══")
    for conv, deg_a, deg_b in [
        ("α-direction (PCF-1 v1.3 §6)", d-1, d),
        ("symmetric (gap_prop §1)",     d,   d),
        ("δ-direction (class label)",   d+1, d),
    ]:
        r = analyze_recurrence(d, conv, deg_a, deg_b)
        results.append((d, conv, deg_a, deg_b, r))


print("=" * 78)
print("[A.5] Verify against PCF-1 v1.3 §6 Theorem 5 (d=2)")
print("=" * 78)
print()
print("PCF-1 v1.3 §6 Theorem 5 statement: 'A ∈ {3, 4}' at d=2.")
print("                                    A = 4 for V_quad")
print("                                    A = 3 for QL01, QL02, QL06, QL15, QL26")
print()
print("Naive Newton-polygon predictions at d=2:")
print("  α-direction (deg a=1, deg b=2):  A = 3 = d+1")
print("  symmetric  (deg a=2, deg b=2):   A = 2 = d")
print("  δ-direction (deg a=3, deg b=2):  A = 1 = d-1")
print()
print("✓ α-direction A=3 MATCHES the PCF-1 v1.3 lower branch (QL families)")
print("✗ A=4 (V_quad upper branch = 2d) is NOT recovered by naive Newton-polygon")
print("    analysis. This branch requires the SIARC stratum to sit at an")
print("    EXCEPTIONAL LOCUS where the leading-order Γ(n)^{-(d+1)} cancellation")
print("    occurs (P2.1 + P2.2 sub-claims of gap_proposition_for_d_ge_3.md).")
print()


print("=" * 78)
print("[A.6+A.7] Verify against PCF-2 v1.3 R1.1 + R1.3 + Q1 (d=3, d=4)")
print("=" * 78)
print()
print("PCF-2 v1.3 R1.1 + R1.3 + Q1 empirical record:")
print("  d=3: 50/50 cubic families A_fit ≈ 6 = 2d (high-precision tail-window fit)")
print("  d=4: 60/60 quartic families mean A_fit = 7.954 ≈ 8 = 2d, σ = 3.7e-3")
print()
print("Naive Newton-polygon predictions at d=3, d=4:")
print("  d=3: α-dir A=4=d+1, symmetric A=3=d, δ-dir A=2=d-1")
print("  d=4: α-dir A=5=d+1, symmetric A=4=d, δ-dir A=3=d-1")
print()
print("✗ NONE of the three naive Newton-polygon predictions match 2d at d ≥ 3.")
print("  This is a FACTOR-OF-2 DISCREPANCY (consistent across d=3, d=4).")
print()
print("DIAGNOSTIC INTERPRETATION:")
print("  The empirical A = 2d at d ≥ 3 implies the SIARC PCF stratum sits at a")
print("  SPECIAL LOCUS where the leading-order formal expansion exhibits a")
print("  structural cancellation of the n^μ_dom γ_dom^n leading factor relative")
print("  to the naive Newton-polygon prediction. This is exactly P2.1 (Newton-")
print("  polygon non-degeneracy: the SIARC stratum has SINGLE slope at d, with")
print("  no spurious lower-slope vertices) + P2.2 (formal-exponent extremality:")
print("  no resonance cancellation drops -A n log n to lower-slope -A' n log n).")
print()
print("Naive Newton-polygon analysis CANNOT recover A = 2d without the additional")
print("argument that the stratum is at this exceptional locus.")
print()
print("VERDICT SIGNAL: A_INDICIAL_DRIFT_AT_d_GE_3")
print("  (Phase A's chi_d(c) at d ≥ 3 doesn't recover the empirical 2d via")
print("  naive Newton-polygon analysis; the upper branch / exceptional-locus")
print("  argument is the actual content of Phase 2 P2.1 + P2.2 sub-claims and")
print("  is NOT closed by symbolic derivation alone.)")
print()
print("=" * 78)
print("[A.5'-A.7'] HONEST INTERPRETATION OF PHASE A RESULT")
print("=" * 78)
print()
print("The naive Newton-polygon analysis is the formal-level baseline. It says:")
print("  - For GENERIC (c_a, c_b) with no algebraic cancellation, A = d+1 (α-dir)")
print("    or A = d (symmetric) or A = d-1 (δ-dir).")
print("  - The d=2 lower branch (A=3 for QL families) MATCHES generic α-direction.")
print("  - The d=2 upper branch (A=4 for V_quad) and d≥3 (A=2d) require the SIARC")
print("    PCF stratum to be at a SPECIAL LOCUS where this baseline is bumped up.")
print()
print("This is a STRUCTURAL OBSERVATION: the empirical A = 2d cannot be derived")
print("from Newton-polygon analysis ALONE without specifying:")
print("  (i)  the algebraic condition defining the special locus (P2.1)")
print("  (ii) the proof that all SIARC PCF strata at d ≥ 3 lie on this locus (P2.2)")
print("  (iii) the formal-to-analytic upgrade (P2.3) — out of scope for Phase A.")
print()
print("Output structural summary at end-of-script.")
print("=" * 78)


# Output JSON-structured findings for AEAL
findings = {
    "task": "T1-BIRKHOFF-PHASE2-LIFT-LOWER, Phase A",
    "method": "naive Newton-polygon balance analysis on y(n) - b_n y(n-1) - a_n y(n-2) = 0",
    "ansatz": "y(n) ~ Γ(n)^μ γ^n n^ρ S(1/n)",
    "results_by_d_and_convention": [
        {"d": d, "convention": conv, "deg_a": da, "deg_b": db,
         "mu_dom": r[0], "gamma_dom": r[1], "mu_sub": r[2], "gamma_sub": r[3],
         "A_predicted_naive": r[4], "A_target_B4": 2*d, "match_B4": (r[4] == 2*d)}
        for (d, conv, da, db, r) in results
    ],
    "verdict_signal": "A_INDICIAL_DRIFT_AT_d_GE_3",
    "interpretation": (
        "Naive Newton-polygon analysis recovers d=2 lower branch (A=3 = d+1 for "
        "α-direction asymmetric coefficients) but NOT V_quad upper branch (A=4 = "
        "2d at d=2) nor the empirical A=2d at d ≥ 3. The 'upper branch' requires "
        "the SIARC stratum to sit at an EXCEPTIONAL LOCUS where the leading-order "
        "formal expansion exhibits a structural cancellation of the dominant "
        "Γ(n)^{μ_dom} γ_dom^n factor relative to the naive prediction. This is "
        "the actual content of P2.1 (Newton-polygon non-degeneracy) + P2.2 "
        "(formal-exponent extremality) sub-claims of gap_proposition_for_d_ge_3.md, "
        "and IS NOT closed by symbolic derivation of chi_d(c) alone — it requires "
        "the additional algebraic + analytic-upgrade argument (P2.3 sectorial "
        "uniformity)."
    ),
    "structural_finding": (
        "At every d ∈ {2,3,4}, naive Newton-polygon analysis gives a baseline "
        "A_naive ∈ {d-1, d, d+1} depending on (deg a, deg b) convention. The "
        "empirical A = 2d at d ≥ 3 is BELOW the literature upper bound 2d only "
        "in the sense that 2d = A_naive at d=1 only; for d ≥ 2 there is a "
        "consistent gap between A_naive (Newton-polygon baseline) and A_target "
        "(empirical / B4). The gap is closed not by chi_d(c) at the formal "
        "level but by the SIARC-stratum-specific algebraic condition — "
        "Phase 2 sub-claim P2.2 (formal-exponent extremality)."
    )
}

# Hash the script content for AEAL provenance
with open(__file__, 'rb') as f:
    script_sha = hashlib.sha256(f.read()).hexdigest()

findings["script_sha256"] = script_sha
findings["script_path"] = "phase_a_symbolic_derivation.py"

print()
print("=" * 78)
print("PHASE A FINDINGS (JSON for AEAL claims.jsonl)")
print("=" * 78)
print(json.dumps(findings, indent=2))

# Write findings to file for downstream phases
out_path = "phase_a_findings.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(findings, f, indent=2)
print(f"\nWritten findings to: {out_path}")
print()
print("=" * 78)
print("PHASE A COMPLETE (with HALT signal)")
print("=" * 78)
