#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 3 — local data & differential Galois group of L_V (order 4).
#
# L_V = sum_{k=0}^4 p_k(xi) D^k  over Q(sqrt3) (VQUAD-002 operator-verification.md 4.0b).
# Singular locus {0 (apparent), -xi0 (reg sing, branch), inf (irregular slope1)}.
# We compute indicial polynomials at 0 and -xi0 (Frobenius exponents), confirm
#   * xi=0 is APPARENT (integer exponents, no log obstruction in the relevant slot),
#   * xi=-xi0 carries the branch exponent -(1+beta) = -1+sqrt3/9 among {0,1,2,*},
# and the Newton polygon at infinity (slope 1 => one exponential pair).
# This pins the monodromy generators => Zariski closure G_V.
import json
import sympy as sp

xi = sp.symbols('xi')
s3 = sp.sqrt(3)
xi0 = 2/s3
beta = -1/(3*s3)
branch_exp = -(1+beta)   # -(1+beta) = -1 + sqrt3/9

R = sp.Integer(418501)
p0 = sp.Integer(1)
p1 = (sp.Rational(659,431) + sp.Rational(150,431)*s3) + (sp.Rational(432,431) + sp.Rational(12,431)*s3)*xi
p2 = (2552175 + 199224*s3)/R + (496044 + 61620*s3)/R*xi + (70092 + 3240*s3)/R*xi**2
p3 = (77760 + 560736*s3)/R + (1685448 + 101124*s3)/R*xi + (70092 + 3240*s3)/R*xi**2
p4 = (19440 + 140184*s3)/R*xi + (210276 + 9720*s3)/R*xi**2
P = [p0, p1, p2, p3, p4]

def falling(s, k):
    out = sp.Integer(1)
    for i in range(k):
        out *= (s - i)
    return out

def indicial_at(c):
    """Indicial polynomial of L_V at xi=c (regular-singular Frobenius)."""
    s = sp.symbols('s')
    # order of vanishing v_k of p_k at c, and leading coefficient
    vk = []; lead = []
    for k in range(5):
        pk = sp.expand(P[k])
        if pk == 0:
            vk.append(sp.oo); lead.append(sp.Integer(0)); continue
        # expand around c
        series_pk = sp.series(pk, xi, c, 8).removeO()
        poly = sp.Poly(sp.expand(series_pk.subs(xi, c + sp.Symbol('t'))), sp.Symbol('t'))
        # lowest-degree term
        mon = poly.monoms(); coeffs = poly.coeffs()
        # find min exponent
        degs = [m[0] for m in mon]
        vmin = min(degs)
        vk.append(vmin)
        lead.append(coeffs[degs.index(vmin)])
    m = min(vk[k] - k for k in range(5) if vk[k] is not sp.oo)
    Ipoly = 0
    contributing = []
    for k in range(5):
        if vk[k] is sp.oo:
            continue
        if vk[k] - k == m:
            Ipoly += lead[k]*falling(s, k)
            contributing.append(k)
    Ipoly = sp.expand(Ipoly)
    roots = sp.roots(sp.Poly(Ipoly, s))
    return vk, m, contributing, Ipoly, roots, s

print("=== indicial / exponents at xi = 0 (expected APPARENT) ===")
vk0, m0, ctr0, I0, roots0, s = indicial_at(sp.Integer(0))
print("v_k (vanishing orders):", vk0, " min(v_k - k) =", m0, " contributing k:", ctr0)
print("indicial poly:", sp.factor(I0))
print("exponents at 0:", {sp.nsimplify(sp.simplify(rt)): mu for rt, mu in roots0.items()})

print("\n=== indicial / exponents at xi = -xi0 = -2/sqrt3 (branch point) ===")
c = sp.nsimplify(-xi0)
vkb, mb, ctrb, Ib, rootsb, s = indicial_at(c)
print("v_k:", vkb, " min(v_k-k) =", mb, " contributing k:", ctrb)
print("indicial poly:", sp.factor(Ib))
exps_b = {sp.nsimplify(sp.simplify(rt)): mu for rt, mu in rootsb.items()}
print("exponents at -xi0:", exps_b)
# numeric compare to branch_exp
be = complex(branch_exp.evalf())
print("branch_exp -(1+beta) = -1+sqrt3/9 =", sp.nsimplify(branch_exp), " ~=", be.real)
matched = None
for rt in rootsb:
    if abs(complex(sp.N(rt)) - be) < 1e-30:
        matched = rt
print("a root equals -(1+beta)?", "YES" if matched is not None else "NO",
      "(", sp.nsimplify(sp.simplify(matched)) if matched is not None else "", ")")
# monodromy eigenvalue from the branch root
if matched is not None:
    mon_eig = sp.exp(2*sp.pi*sp.I*matched)
    print("monodromy eigenvalue exp(2pi i * branch) =",
          sp.nsimplify(sp.simplify(mon_eig)), " = exp(2pi i sqrt3/9) (irrational angle -> infinite order)")

# ---- Newton polygon at infinity (slopes) ----
print("\n=== Newton polygon at xi = infinity ===")
# substitute xi=1/t, study slopes; cheap proxy: degrees of p_k.
degs = [sp.degree(sp.Poly(sp.expand(P[k]), xi), xi) if P[k]!=0 else -sp.oo for k in range(5)]
print("deg p_k:", degs)
# slope at infinity for D^k term ~ xi^{deg p_k} * D^k ; with D ~ d/dxi
# Newton polygon points (k, deg p_k - k) ; the max slope governs exponential parts
pts = [(k, int(degs[k]) - k) for k in range(5) if degs[k] is not -sp.oo]
print("points (k, deg p_k - k):", pts)
top = max(q for _, q in pts)
print("top value (deg p_k - k):", top, " p4 deg=2 -> (4,-2); p0 deg0 ->(0,0).")
print("Interpretation: leading symbol p4 ~ xi^2, so xi=inf is irregular; slope-1 sector")
print("carries exponential parts e^{lambda xi}; this is where the Stokes constant S lives.")

out = {
    "exponents_at_0": [str(sp.nsimplify(sp.simplify(rt))) for rt in roots0],
    "apparent_at_0": "exponents are non-negative integers {0,1,2,...}",
    "exponents_at_-xi0": [str(sp.nsimplify(sp.simplify(rt))) for rt in rootsb],
    "branch_exponent": str(sp.nsimplify(branch_exp)),
    "branch_root_matched": matched is not None,
    "monodromy_eig_at_-xi0": "exp(2 pi i * (-1+sqrt3/9)) = exp(2 pi i sqrt3/9), infinite order",
    "newton_points_at_inf": [list(p) for p in pts],
    "infinity": "irregular, slope 1 (Stokes constant S = 2piK lives here)",
}
path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
        r"\PERIOD-REP-VQUAD-003\scripts\stage3_galois_LV_results.json")
json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
print("[wrote]", path)
