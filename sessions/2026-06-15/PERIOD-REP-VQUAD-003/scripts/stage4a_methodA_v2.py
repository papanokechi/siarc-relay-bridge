#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 4 Method A (v2) — correct Borel-sum kernel.
#
# Borel sum:  φ(z) = a0 + ∫_0^∞ e^{-ξ/z} B̂(ξ) dξ   (kernel e^{-ξ/z}, derived from
#   a_{m+1} = b_m m! = b_m ∫_0^∞ e^{-t} t^m dt).  Laplace-along-contour rules:
#       D_ξ ↦ +1/z ,   ξ ↦ +z^2 D_z       (boundary terms vanish on rapid-decay γ).
# The thimble (difference of lateral sums) kills the a0 analytic part, so the difference
# integral I_γ(z) satisfies the HOMOGENEOUS L_phi.  Dualizing L_V must then give
# M = h(z)·L_phi.  We test all four kernel-sign conventions and report which one(s) work.
import json
import sympy as sp

z = sp.symbols('z'); f = sp.Function('f')
s3 = sp.sqrt(3); R = sp.Integer(418501)
c = {
 0: {0: sp.Integer(1)},
 1: {0: sp.Rational(659,431)+sp.Rational(150,431)*s3, 1: sp.Rational(432,431)+sp.Rational(12,431)*s3},
 2: {0: (2552175+199224*s3)/R, 1: (496044+61620*s3)/R, 2: (70092+3240*s3)/R},
 3: {0: (77760+560736*s3)/R, 1: (1685448+101124*s3)/R, 2: (70092+3240*s3)/R},
 4: {1: (19440+140184*s3)/R, 2: (210276+9720*s3)/R},
}
q0 = 1 + (sp.Rational(23,9)+sp.Rational(14,27)*s3)*z + (sp.Rational(-253,9)+sp.Rational(488,27)*s3)*z**2
q1 = (48-24*s3) + (-64+44*s3)*z + (sp.Rational(-68,3)+sp.Rational(52,3)*s3)*z**2 + (sp.Rational(-152,3)+sp.Rational(100,3)*s3)*z**3
q2 = (-36+24*s3)*z**2 + (-12+8*s3)*z**3 + (-12+8*s3)*z**4

def build_M(sign_D, sign_xi):
    # D_ξ ↦ sign_D * (1/z) ;  ξ ↦ sign_xi * z^2 D_z
    def opxi(expr):
        return sign_xi*z**2*sp.diff(expr, z)
    M = sp.Integer(0)
    for k in c:
        for a in c[k]:
            g = (sign_D**k) * z**(-k) * f(z)
            for _ in range(a):
                g = opxi(g)
            M += c[k][a]*g
    M = sp.expand(M)
    f0, f1, f2 = f(z), sp.diff(f(z), z), sp.diff(f(z), z, 2)
    M = sp.collect(M, [f2, f1, f0])
    return M.coeff(f2), M.coeff(f1), M.coeff(f0)

results = {}
best = None
for sD in (1, -1):
    for sX in (1, -1):
        cM2, cM1, cM0 = build_M(sD, sX)
        h2 = sp.simplify(cM2/q2); h1 = sp.simplify(cM1/q1); h0 = sp.simplify(cM0/q0)
        ok = (sp.simplify(h2-h1) == 0) and (sp.simplify(h1-h0) == 0)
        key = f"D_xi->{sD:+d}/z, xi->{sX:+d}z^2D_z"
        results[key] = {"proportional": bool(ok), "h(z)": str(sp.simplify(h2)) if ok else "n/a"}
        print(f"  [{key}]  M = h(z) L_phi : {ok}")
        if ok:
            best = (key, sp.simplify(h2))

methodA = best is not None
print("\n=== METHOD A verdict:", "PASS" if methodA else "FAIL", "===")
if methodA:
    print("  working convention:", best[0])
    print("  h(z) =", best[1])
    print("  => I_γ(z)=∫_γ e^{-ξ/z}B̂ dξ satisfies L_phi (homogeneous); its z->0 subdominant")
    print("     exponential coefficient is the Stokes multiplier = C.  Same diff structure. QED")

out = {"methodA_pass": bool(methodA),
       "conventions_tested": results,
       "working_convention": best[0] if methodA else None,
       "h(z)": str(best[1]) if methodA else None,
       "interpretation": "I_γ(z)=∫_γ e^{-ξ/z}B̂dξ solves L_phi; C is its subdominant Stokes coeff"}
path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
        r"\PERIOD-REP-VQUAD-003\scripts\stage4_methodA_results.json")
json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
print("[wrote]", path)
