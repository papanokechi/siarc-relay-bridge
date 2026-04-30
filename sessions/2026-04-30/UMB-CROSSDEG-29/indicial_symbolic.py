"""UMB-CROSSDEG-29 Step 4 (revised): symbolic indicial table for d in {2,4,6}.

Project conventions (verified from siarc-relay-bridge/sessions/2026-04-30/
T2B-LOG-MINUS-ONE-36/forensic.py):

  rho_d = a_d / b_{d/2}^2  (leading-first; a_d = a[0], b_{d/2} = b[0]).

  (BT)   Birkhoff-Trjitzinsky eigenvalue polynomial of asymptotic recurrence
         p_n = a(n) p_{n-1} + b(n) p_{n-2} :
                 lambda^2 - b_{d/2} lambda - a_d = 0
         Rescaled (t = lambda / b_{d/2}):
                 I_BT(t) = t^2 - t - rho_d = 0,    Disc_BT = 1 + 4 rho_d.

  (F)    Frobenius indicial polynomial at the apparent singularity of the
         deg-d PCF (Lean Thm66_ApparentSingularity, T2B-LOG-MINUS-ONE-36
         forensic.py line 111):
                 I_F(r) = r^2 - r + rho_d = 0,    Disc_F = 1 - 4 rho_d.

These are DIFFERENT polynomials. Each governs a different universality
class:

  Class A (BT-rational sum-1 stratum):  Disc_BT = 1 + 4 rho_d a rational
    square. Roots t_+ + t_- = 1 (Vieta) and rational. Closed form:
        rho_d = -m(b - m) / b^2,  1 <= m < b,  gcd(m, b) = 1
    yielding roots {m/b, (b-m)/b}. The simplest non-trivial case b=3, m=1
    gives rho = -2/9 with roots {1/3, 2/3} -- the canonical T2B Trans
    stratum. This formula is independent of d, hence "cross-degree".

  Class B (Frobenius apparent-singularity stratum):  Disc_F = 0, i.e.,
        rho_d = +1/4
    a single point, double Frobenius root r = 1/2 (Lean Thm 5/6). This is
    the Brouncker-shape stratum (a_d=1, b_{d/2}=2 up to scaling).

These two classes have distinct closed forms and are NOT a single family.
HENCE the prompt's HALT condition (Step 4 producing a closed-form for ALL
magic ratios as a SINGLE family) is NOT triggered. Universality is partial:
each locus is dimension-independent (the indicial polynomials only see d
through rho_d), so -2/9 and +1/4 reappear at every even d, but governed by
two different indicial criteria.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def magic_rho_table(b_max: int = 12):
    out = []
    for b in range(2, b_max + 1):
        for m in range(1, b // 2 + 1):
            if Fraction(m, b).denominator != b:
                continue
            rho = Fraction(-m * (b - m), b * b)
            roots = (Fraction(m, b), Fraction(b - m, b))
            out.append(
                {
                    "b": b,
                    "m": m,
                    "rho": str(rho),
                    "rho_float": float(rho),
                    "roots": [str(roots[0]), str(roots[1])],
                    "Disc_BT": str(Fraction(1) + 4 * rho),
                }
            )
    return out


def main():
    t, r, rho = sp.symbols("t r rho")
    d_values = [2, 4, 6]

    by_degree = []
    for d in d_values:
        k = d // 2
        I_BT = t * t - t - rho
        I_F = r * r - r + rho
        entry = {
            "d": d,
            "k": k,
            "ratio_def": f"rho_{d} = a_{d} / b_{k}^2",
            "BT": {
                "raw_polynomial": f"lambda^2 - b_{k} lambda - a_{d} = 0",
                "rescaled_polynomial": f"{I_BT} = 0  (t = lambda / b_{k})",
                "discriminant": f"1 + 4 rho_{d}",
                "rational_sum1_locus": "Disc_BT a rational square; roots t_+ + t_- = 1",
            },
            "Frobenius": {
                "polynomial": f"{I_F} = 0",
                "discriminant": f"1 - 4 rho_{d}",
                "apparent_singularity_locus": f"Disc_F = 0, i.e. rho_{d} = 1/4",
            },
        }
        by_degree.append(entry)

    classA = magic_rho_table(b_max=12)
    classB = {
        "rho_value": "1/4",
        "rho_float": 0.25,
        "Disc_F": "0",
        "Frobenius_double_root": "r = 1/2",
        "comment": (
            "Single isolated point. Realised by integer (a_d, b_{d/2}) with "
            "a_d / b_{d/2}^2 = 1/4 (e.g. a_d=1, b_{d/2}=2, Brouncker-shape). "
            "Universality across d trivial because rho is dimension-free."
        ),
    }

    cross_degree = {
        "claim": (
            "Both indicial polynomials I_BT and I_F depend on d only through "
            "rho_d. Their rational-roots loci are therefore "
            "DIMENSION-INDEPENDENT. So rho = -2/9 (Class A) and rho = +1/4 "
            "(Class B) appear identically in every even-d stratum. Whether "
            "PCFs at these loci converge and yield Trans/Log constants for "
            "d=4,6 is an EMPIRICAL question requiring CMAX>=3 censuses."
        ),
        "halt_assessment": (
            "Two distinct closed forms, NOT a single family: Class A "
            "rho = -m(b-m)/b^2 (infinite countable family, includes -2/9) "
            "and Class B rho = 1/4 (isolated). Prompt's HALT condition "
            "(single family unifying ALL magic ratios) is NOT met."
        ),
    }

    table = {
        "convention_note": (
            "BT polynomial governs the rescaled secondary growth rate; "
            "Frobenius polynomial governs the apparent-singularity exponents. "
            "Verified in T2B-LOG-MINUS-ONE-36/forensic.py (lines 110-128)."
        ),
        "by_degree": by_degree,
        "class_A_BT_rational_sum1": {
            "closed_form": "rho = -m(b-m)/b^2, 1 <= m < b, gcd(m,b)=1",
            "indicial_roots": "{m/b, (b-m)/b}, sum 1, rational",
            "examples_b_le_12": classA,
        },
        "class_B_Frobenius_double_root": classB,
        "cross_degree": cross_degree,
        "empirical_status": {
            "deg_2_1_at_-2/9": (
                "Trans CONFIRMED (T2B-RESONANCE-B67/B8-12; Bauer-style Log "
                "near-miss at -1/36)."
            ),
            "deg_4_2_at_+1/4_Brouncker_shape": (
                "Class B stratum populated: 26,622 Trans-candidates with "
                "R1=+1/4 in CMAX=2 census. Five deep-validated in "
                "UMB-CLASSB-SATURATION; verdict NOT-SATURATED."
            ),
            "deg_4_2_at_-2/9": (
                "UNRESOLVED. CMAX=2 lattice has |b_2|<=2 -> b_2^2 in {1,4}; "
                "9 unreachable. Distinct R1 in census: {1/4, 1/2, 1, 2}."
            ),
            "deg_6_3_at_-2/9": "UNRESOLVED (no census)",
        },
    }

    out = HERE / "indicial_table.json"
    with out.open("w", encoding="utf-8") as fh:
        json.dump(table, fh, indent=2, default=str)
    print("[write]", out)

    lines = ["# UMB-CROSSDEG-29 -- symbolic indicial table\n"]
    lines.append("## Conventions\n")
    lines.append("$\\rho_d = a_d / b_{d/2}^2$ (leading-first coefficients).\n")
    lines.append("- **BT** (rescaled): $I_{BT}(t) = t^2 - t - \\rho_d$, $\\Delta_{BT} = 1 + 4\\rho_d$\n")
    lines.append("- **Frobenius**: $I_F(r) = r^2 - r + \\rho_d$, $\\Delta_F = 1 - 4\\rho_d$\n\n")
    lines.append("## Per-degree symbolic table (d in {2, 4, 6})\n")
    lines.append("| d | k | BT (rescaled) | Frobenius | BT-disc | F-disc |")
    lines.append("|---|---|---------------|-----------|---------|--------|")
    for e in by_degree:
        lines.append(
            f"| {e['d']} | {e['k']} | $t^2 - t - \\rho_{e['d']}$ | "
            f"$r^2 - r + \\rho_{e['d']}$ | $1+4\\rho_{e['d']}$ | $1-4\\rho_{e['d']}$ |"
        )
    lines.append("\n*Polynomials are formally identical across d: dimension enters only through $\\rho_d$.*\n")
    lines.append("\n## Class A magic-rho catalogue (BT rational sum-1, $b \\le 12$)\n")
    lines.append("| b | m | $\\rho = -m(b-m)/b^2$ | indicial roots |")
    lines.append("|---|---|---------------------|----------------|")
    for ex in classA[:18]:
        lines.append(f"| {ex['b']} | {ex['m']} | {ex['rho']} | {{{ex['roots'][0]}, {ex['roots'][1]}}} |")
    lines.append("\nSimplest non-trivial entry: $b=3, m=1$, $\\rho = -2/9$, roots $\\{1/3, 2/3\\}$.\n")
    lines.append("## Class B (Frobenius double root)\n")
    lines.append("$\\rho = +1/4$ is the **unique** point where $\\Delta_F = 0$, double root $r = 1/2$.\n")
    lines.append("## HALT assessment\n")
    lines.append(
        "The two magic loci ({-2/9, +1/4, -2/25, ...}) are NOT a single "
        "family. Class A is the infinite family $\\rho = -m(b-m)/b^2$ "
        "(Vieta forces rational sum-1 BT roots); Class B is the isolated "
        "point $\\rho = 1/4$ (Frobenius double root). The prompt's HALT "
        "condition (single closed form unifying ALL magic ratios) is NOT met. "
        "Universality is **partial and dimension-independent**: each locus "
        "reappears at every even d, but they are governed by different "
        "indicial polynomials.\n"
    )
    (HERE / "indicial_table.md").write_text("\n".join(lines), encoding="utf-8")
    print("[write]", HERE / "indicial_table.md")


if __name__ == "__main__":
    main()
