"""
Phase B — Extended sweep at d ∈ [3, d_max=8] verifying:
    B.1 — chi_d(c) computed symbolically (subsumed in Phase A — verified)
    B.2 — Indicial exponents extracted (degree ≤ deg(chi_d))
    B.3 — Non-resonance: indicial exponents differ modulo Z
          (no two integers in their differences)
    B.4 — Non-degeneracy: leading coefficient of chi_d nonzero

For the SIARC PCF Wallis recurrence in normal-case Wimp-Zeilberger ansatz,
the indicial exponents are (μ_dom, μ_sub) for the two formal solutions.

Non-resonance: μ_dom - μ_sub = A_naive should NOT be a positive integer
(otherwise the formal solutions resonate; one becomes y_dom, the other
y_dom log + y_sub-correction). However, the Wallis recurrence is at
fractional rank q=1 (normal case), so A_naive integer is generic for
polynomial-coefficient recurrences and DOES NOT block the formal solution
existence — it just means the secondary solution may have a log term.

Non-degeneracy: leading coefficient c_b ≠ 0, i.e., the polynomial b_n has
its stated degree. For the SIARC stratum this is the Phase 0 assumption;
not violated.

Output: phase_b_extended_sweep.py + phase_b_summary.md + phase_b_findings.json
"""

import json
import hashlib

print("=" * 78)
print("PHASE B — Extended sweep at d ∈ [3, 8]")
print("=" * 78)

results = []
for d in range(3, 9):
    print(f"\n--- d = {d} ---")
    for conv, deg_a, deg_b in [
        ("alpha-direction (PCF-1 v1.3)", d-1, d),
        ("symmetric (gap_prop)",          d, d),
        ("delta-direction (class)",      d+1, d),
    ]:
        mu_dom = deg_b
        mu_sub = deg_a - deg_b
        A_naive = mu_dom - mu_sub
        # Non-resonance check: μ_dom − μ_sub ∉ Z>0 ?
        # In our case the difference IS an integer for polynomial coefficients;
        # this is a known structural feature of Wimp-Zeilberger normal case at q=1.
        # The "resonance" matters only if log corrections appear; the formal
        # series ansatz remains valid with possible log term in subdominant solution.
        nonres_strict = False  # always integer in our normal-case
        nonres_modular = (A_naive % 1 != 0)  # never true here
        # Non-degeneracy: c_b ≠ 0 by construction (polynomial of stated degree)
        nondegen = True

        results.append({
            "d": d, "convention": conv, "deg_a": deg_a, "deg_b": deg_b,
            "mu_dom": mu_dom, "mu_sub": mu_sub, "A_naive": A_naive,
            "A_target_B4": 2*d,
            "non_resonance_strict": nonres_strict,
            "non_resonance_modular": nonres_modular,
            "non_degeneracy": nondegen,
            "borderline_case_dega_eq_2degb": (deg_a == 2*deg_b),
        })
        print(f"  {conv:35s}: A_naive={A_naive:2d}, target=2d={2*d}, "
              f"borderline(deg_a=2deg_b)={'YES' if deg_a == 2*deg_b else 'no '}, "
              f"non-resonant(diff ∉ Z)={'yes' if nonres_modular else 'NO'}")

print()
print("=" * 78)
print("STRUCTURAL OBSERVATION (Phase B)")
print("=" * 78)
print()
print("Across d ∈ [3, 8] for all three conventions:")
print("  - Newton-polygon baseline A_naive ∈ {d-1, d, d+1}")
print("  - Borderline case deg_a = 2 deg_b is NEVER met for these conventions")
print("    (would require deg_a = 2d in α-dir or symmetric, which is δ+1 or δ)")
print("  - Indicial exponents are ALWAYS integers (normal case at q=1)")
print("  - Strict non-resonance (μ differences ∉ Z) FAILS GENERICALLY")
print()
print("This is the standard Wimp-Zeilberger normal case. The non-resonance/")
print("non-degeneracy that the relay prompt §2 Phase B asks for refers to the")
print("BORDERLINE case (q=2 fractional rank) where the two formal solutions")
print("coalesce at leading order and split at sub-leading sub-exponential order")
print("(exp(±B √n) corrections per Birkhoff-Trjitzinsky 1933 §1 anormal case).")
print()
print("VERDICT SIGNAL: B_BORDERLINE_NOT_MET_BY_NAIVE_ANSATZ")
print("  Phase B's naive sweep confirms the SIARC stratum at deg_a < 2 deg_b")
print("  sits in the NORMAL case, where A_naive ≤ d+1, not 2d. The empirical")
print("  A = 2d at d ≥ 3 must come from the SIARC stratum being at the")
print("  exceptional locus of the borderline case OR from a different")
print("  asymptotic-fitting convention than Wimp-Zeilberger predicts.")
print()
print("CONSEQUENCE:")
print("  Phase B (extended sweep) does not by itself close A = 2d at d ≥ 3.")
print("  Same structural observation as Phase A: the lift to A = 2d requires")
print("  P2.1 + P2.2 + P2.3 sub-claims, not just symbolic chi_d verification.")

# Hash the script for AEAL provenance
with open(__file__, 'rb') as f:
    script_sha = hashlib.sha256(f.read()).hexdigest()

findings = {
    "task": "T1-BIRKHOFF-PHASE2-LIFT-LOWER, Phase B",
    "method": "Naive Newton-polygon sweep d ∈ [3, 8], three conventions",
    "results": results,
    "verdict_signal": "B_BORDERLINE_NOT_MET_BY_NAIVE_ANSATZ",
    "non_resonance_summary": "All d ∈ [3,8] in all three conventions: μ_dom−μ_sub ∈ Z (normal case q=1; non-resonance fails strictly but does not block formal series ansatz, only introduces log correction in subdominant solution).",
    "non_degeneracy_summary": "All d ∈ [3,8] in all three conventions: c_b ≠ 0 by construction (polynomial of stated degree).",
    "borderline_check": "deg_a = 2 deg_b NEVER met for any of three conventions at d ∈ [3,8]; SIARC stratum is in NORMAL case, but empirical A=2d corresponds to BORDERLINE-case A.",
    "implication": "Phase B confirms Phase A baseline. The lift to A=2d at d≥3 cannot be achieved by symbolic chi_d sweep alone; requires structural argument that the SIARC stratum is at an exceptional locus where the normal-case A_naive is bumped to A=2d.",
    "script_sha256": script_sha,
}

with open("phase_b_findings.json", 'w', encoding='utf-8') as f:
    json.dump(findings, f, indent=2)
print(f"\nWritten findings to: phase_b_findings.json")
print()
print("=" * 78)
print("PHASE B COMPLETE")
print("=" * 78)
