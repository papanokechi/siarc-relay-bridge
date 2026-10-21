"""
CT-S4-FORMAL-TYPE (P5) steps 1-2: exact formal-type computation for the two
candidate linear systems.

SYSTEM A -- "Channel Theory object": the ODE annihilating f(z) = sum_n Q_n z^n
            for V_quad, b(n) = 3n^2 + n + 1.
SYSTEM B -- "D5^(1) object": the operator L_phi of the V_quad period-rep paper
            (sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/sections/section-2.md),
            the scalar reduction of the V_quad Painleve-V linear problem.

Everything below is exact symbolic computation over Q(sqrt 3); no floating point
enters any structural conclusion.  Outputs formal_type.json.
"""
import json
import hashlib
import sympy as sp

z, u, t, A, al = sp.symbols("z u t A alpha")
s3 = sp.sqrt(3)

OUT = {}

# ---------------------------------------------------------------- SYSTEM A ---
# Derivation.  f = sum_{n>=0} Q_n z^n,  Q_n = b(n) Q_{n-1} + Q_{n-2},
# Q_{-1} = 0, Q_0 = 1.  Summing the recurrence over n >= 1:
#     f - 1 = z * b(theta+1) f + z^2 f,     theta = z d/dz,
# with b(theta+1) = 3 theta^2 + 7 theta + 5 for b(n) = 3n^2+n+1.
# theta = zD, theta^2 = z^2 D^2 + z D, so
#     z*b(theta+1) = 3 z^3 D^2 + 10 z^2 D + 5 z.
# Hence  [1 - 3z^3 D^2 - 10 z^2 D - 5z - z^2] f = 1, i.e. the homogeneous
# operator (after an overall sign) is
#     L_A = 3 z^3 D^2 + 10 z^2 D + (z^2 + 5z - 1).

bpoly = lambda n: 3 * n**2 + n + 1
A2, A1, A0 = 3 * z**3, 10 * z**2, z**2 + 5 * z - 1


def verify_system_A(N=40):
    """Certify L_A annihilates sum Q_n z^n (inhomogeneous term = 1)."""
    Q = {-1: sp.Integer(0), 0: sp.Integer(1)}
    for n in range(1, N + 1):
        Q[n] = sp.expand(bpoly(n) * Q[n - 1] + Q[n - 2])
    f = sum(Q[n] * z**n for n in range(0, N + 1))
    resid = sp.expand(A2 * sp.diff(f, z, 2) + A1 * sp.diff(f, z) + A0 * f + 1)
    p = sp.Poly(resid, z)
    # coefficients of z^0..z^{N-2} must vanish; higher orders are truncation
    bad = [k for k in range(0, N - 1) if p.coeff_monomial(z**k) != 0]
    return bad, [Q[n] for n in range(6)]


bad_A, firstQ = verify_system_A()
OUT["system_A_certificate"] = {
    "operator": "3*z**3*D**2 + 10*z**2*D + (z**2 + 5*z - 1), inhomogeneous term 1",
    "b(n)": "3*n**2 + n + 1",
    "first_Q": [str(q) for q in firstQ],
    "orders_checked": "z^0 .. z^38",
    "nonvanishing_residual_orders": bad_A,
    "exact": bad_A == [],
}

# Normal form u'' = r u  for L_A  (gauge-invariant; kills the D^1 term).
a_A = sp.simplify(A1 / A2)
b_A = sp.simplify(A0 / A2)
r_A = sp.simplify(sp.Rational(1, 4) * a_A**2 + sp.Rational(1, 2) * sp.diff(a_A, z) - b_A)
r_A = sp.cancel(sp.together(r_A))
OUT["system_A_normal_form_r"] = str(sp.simplify(r_A))

# ---------------------------------------------------------------- SYSTEM B ---
# L_phi from section-2.md (verbatim transcription).
q0 = 1 + (sp.Rational(23, 9) + sp.Rational(14, 27) * s3) * z \
       + (-sp.Rational(253, 9) + sp.Rational(488, 27) * s3) * z**2
q1 = (48 - 24 * s3) + (-64 + 44 * s3) * z \
       + (-sp.Rational(68, 3) + sp.Rational(52, 3) * s3) * z**2 \
       + (-sp.Rational(152, 3) + sp.Rational(100, 3) * s3) * z**3
q2 = (-36 + 24 * s3) * z**2 + (-12 + 8 * s3) * z**3 + (-12 + 8 * s3) * z**4

# The paper also states q2 = 4(2 sqrt3 - 3) z^2 (z^2+z+3); check that.
q2_claimed = 4 * (2 * s3 - 3) * z**2 * (z**2 + z + 3)
q2_ok = sp.simplify(sp.expand(q2 - q2_claimed)) == 0

# and states the normal-form potential r(z). Independently recompute it.
a_B = sp.cancel(q1 / q2)
b_B = sp.cancel(q0 / q2)
r_B = sp.cancel(sp.together(
    sp.Rational(1, 4) * a_B**2 + sp.Rational(1, 2) * sp.diff(a_B, z) - b_B))
r_B_claimed = (11 * z**4 + 4 * z**2 + 4 * z + 12) / (4 * z**4 * (z**2 + z + 3) ** 2)
r_B_ok = sp.simplify(sp.radsimp(sp.cancel(r_B - r_B_claimed))) == 0

OUT["system_B_certificate"] = {
    "source": ("sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/sections/"
               "section-2.md, Theorem thm:Lphi and eq:r"),
    "q2_factorisation_reproduced": bool(q2_ok),
    "normal_form_r_reproduced_from_q0q1q2": bool(r_B_ok),
    "r_recomputed": str(sp.simplify(r_B)),
    "r_as_printed_in_paper": str(r_B_claimed),
}

# --------------------------------------------------- formal type from r(z) ---
# For u'' = r u, at a point z0 with r having a pole of order m:
#   m <= 2            -> regular singular
#   m = 2k   (even)   -> unramified irregular, Poincare rank k-1, Katz inv k-1
#   m = 2k+1 (odd)    -> RAMIFIED, ramification index 2, Katz invariant m/2 - 1
# The exponential parts solve S' ~ +- sqrt(r).


def _root_multiplicity(poly_expr, z0, maxk=12):
    """Multiplicity of z0 as a root of poly_expr, via derivatives."""
    e = sp.expand(poly_expr)
    k = 0
    while k < maxk:
        val = sp.simplify(sp.radsimp(sp.expand(sp.diff(e, z, k).subs(z, z0))))
        if val != 0:
            return k
        k += 1
    return k


def pole_order(rexpr, z0):
    num, den = sp.fraction(sp.cancel(sp.together(rexpr)))
    return _root_multiplicity(den, z0) - _root_multiplicity(num, z0)


def classify(rexpr, z0, label):
    m = pole_order(rexpr, z0)
    if m <= 2:
        typ, ram, katz, rank = "regular singular", 1, sp.Integer(0), sp.Integer(0)
    elif m % 2 == 0:
        k = m // 2
        typ, ram = "irregular, UNRAMIFIED", 1
        katz = sp.Integer(k - 1)
        rank = sp.Integer(k - 1)
    else:
        typ, ram = "irregular, RAMIFIED", 2
        katz = sp.Rational(m, 2) - 1
        rank = katz
    # leading Laurent coefficient of r at z0 and the exponential parts
    lead = sp.simplify(sp.limit(sp.expand((z - z0) ** m * sp.cancel(rexpr)), z, z0))
    # S' ~ +- sqrt(lead) (z-z0)^{-m/2};  S ~ +- sqrt(lead) (z-z0)^{1-m/2}/(1-m/2)
    if m > 2:
        expo = sp.simplify(sp.sqrt(lead) * (z - z0) ** (1 - sp.Rational(m, 2))
                           / (1 - sp.Rational(m, 2)))
    else:
        expo = None
    return {
        "point": str(z0), "pole_order_of_r": int(m), "formal_type": typ,
        "ramification_index": ram, "Katz_invariant": str(katz),
        "Poincare_rank": str(rank),
        "leading_Laurent_coeff_of_r": str(sp.radsimp(sp.simplify(lead))),
        "exponential_parts_S": (None if expo is None
                                else ["+(" + str(sp.radsimp(sp.simplify(expo))) + ")",
                                      "-(" + str(sp.radsimp(sp.simplify(expo))) + ")"]),
        "_label": label,
    }


def classify_infinity(rexpr, label):
    """z = 1/t.  u'' = r u  becomes, in t, normal form with
       r_inf(t) = r(1/t)/t^4 - (3/4)/t^2   (Schwarzian/normal-form correction)."""
    rt = sp.cancel(rexpr.subs(z, 1 / t))
    r_inf = sp.cancel(sp.together(rt / t**4 - sp.Rational(3, 4) / t**2))
    m = pole_order(r_inf.subs(t, z), 0)  # reuse in variable z
    if m <= 2:
        typ, ram, katz = "regular singular", 1, sp.Integer(0)
    elif m % 2 == 0:
        typ, ram, katz = "irregular, UNRAMIFIED", 1, sp.Integer(m // 2 - 1)
    else:
        typ, ram, katz = "irregular, RAMIFIED", 2, sp.Rational(m, 2) - 1
    return {"point": "infinity (t = 1/z)", "pole_order_of_r_inf": int(m),
            "formal_type": typ, "ramification_index": ram,
            "Katz_invariant": str(katz), "r_inf": str(sp.simplify(r_inf)),
            "_label": label}


# singular points
sing_A = [sp.Integer(0)]
roots_B = sp.solve(sp.Eq(z**2 + z + 3, 0), z)
sing_B = [sp.Integer(0)] + roots_B

OUT["system_A_formal_type"] = [classify(r_A, p, "A") for p in sing_A] + \
                              [classify_infinity(r_A, "A")]
OUT["system_B_formal_type"] = [classify(r_B_claimed, p, "B") for p in sing_B] + \
                              [classify_infinity(r_B_claimed, "B")]

# ------------------------------------------- action differences (Stokes loci) ---
def action_difference(entry):
    ep = entry.get("exponential_parts_S")
    if not ep:
        return None
    val = sp.sympify(ep[0][1:])
    return sp.radsimp(sp.simplify(2 * val))


OUT["action_differences"] = {
    "system_A_at_0": str(action_difference(OUT["system_A_formal_type"][0])),
    "system_B_at_0": str(action_difference(OUT["system_B_formal_type"][0])),
    "xi0_literature": str(sp.radsimp(2 / s3)),
    "zeta_star_literature": str(sp.radsimp(4 / s3)),
}

# ---------------------- the ramified 2:1 covering z = w^2 applied to system B ---
# Pulling back u'' = r u along z = w^2 multiplies the Katz invariant by 2.
OUT["covering_check"] = {
    "statement": ("Pullback along the ramified double cover z = w^2 multiplies "
                  "the Katz invariant at 0 by 2 and divides the ramification "
                  "index by 2 when it was 2."),
    "system_A_Katz_at_0": OUT["system_A_formal_type"][0]["Katz_invariant"],
    "system_A_Katz_after_pullback_z_eq_w2":
        str(2 * sp.Rational(OUT["system_A_formal_type"][0]["Katz_invariant"])),
    "system_B_Katz_at_0": OUT["system_B_formal_type"][0]["Katz_invariant"],
}

with open("formal_type.json", "w") as f:
    json.dump(OUT, f, indent=2)

print(json.dumps(OUT, indent=2))
print("\nsha256(formal_type.json) =",
      hashlib.sha256(open("formal_type.json", "rb").read()).hexdigest())
print("sympy", sp.__version__)
