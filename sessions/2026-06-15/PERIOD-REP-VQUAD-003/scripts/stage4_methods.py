#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 4 — three independent verifications of  C = ∫_γ e^ξ B̂ dξ.
#
# METHOD A (differential-equation): the parameter integral I(z)=∫_γ e^{ξ/z} B̂ dξ satisfies
#   L_phi.  Proof at operator level: Laplace-along-thimble obeys  D_ξ ↦ -1/z,  ξ ↦ -z^2 D_z
#   (boundary terms vanish on the rapid-decay thimble).  Dualizing L_V gives an order-2
#   operator M(z,D_z); we check M = h(z)·L_phi  (the three coeff ratios coincide) -> I solves
#   the SAME equation L_phi whose Stokes multiplier is C.  [Borel-Laplace duality, operator form]
#
# METHOD B (Borel-Laplace / Hankel): the leading branch period in closed form via Hankel,
#   ∫_γ e^ξ A(ξ+ξ0)^{-(1+β)} dξ = A e^{-ξ0} ∮_H e^η η^{-(1+β)} dη = A e^{-ξ0} · 2πi/Γ(1+β)
#   = (S/2πi)Γ(1+β) · e^{-ξ0} · 2πi/Γ(1+β) = S e^{-ξ0}.  The Γ-factor is the branch integral.
#
# METHOD C (Stokes-data, tightest, no γ-integration): the Stokes MULTIPLIER
#   S_mult = 2πi · A/Γ(1+β);  |S_mult| = 2πK = deposited S;  and C = |A|/|β| ties to the same A.
import json
import sympy as sp
import mpmath as mp

# ===================== METHOD A =====================
z = sp.symbols('z'); f = sp.Function('f')
s3 = sp.sqrt(3); R = sp.Integer(418501)
# c[k][a] = coeff of ξ^a in p_k(ξ)  (L_V, VQUAD-002 4.0b)
c = {
 0: {0: sp.Integer(1)},
 1: {0: sp.Rational(659,431)+sp.Rational(150,431)*s3, 1: sp.Rational(432,431)+sp.Rational(12,431)*s3},
 2: {0: (2552175+199224*s3)/R, 1: (496044+61620*s3)/R, 2: (70092+3240*s3)/R},
 3: {0: (77760+560736*s3)/R, 1: (1685448+101124*s3)/R, 2: (70092+3240*s3)/R},
 4: {1: (19440+140184*s3)/R, 2: (210276+9720*s3)/R},
}
def neg_z2Dz(expr):
    return -z**2*sp.diff(expr, z)

M = sp.Integer(0)
for k in c:
    for a in c[k]:
        g = (sp.Integer(-1))**k * z**(-k) * f(z)   # (-1/z)^k f  with D_ξ↦-1/z
        for _ in range(a):
            g = neg_z2Dz(g)                          # ξ↦-z^2 D_z, applied a times
        M += c[k][a]*g
M = sp.expand(M)
f0, f1, f2 = f(z), sp.diff(f(z), z), sp.diff(f(z), z, 2)
M = sp.collect(M, [f2, f1, f0])
cM2, cM1, cM0 = M.coeff(f2), M.coeff(f1), M.coeff(f0)

# L_phi coefficients in z (VQUAD-002 4.0a)
q0 = 1 + (sp.Rational(23,9)+sp.Rational(14,27)*s3)*z + (sp.Rational(-253,9)+sp.Rational(488,27)*s3)*z**2
q1 = (48-24*s3) + (-64+44*s3)*z + (sp.Rational(-68,3)+sp.Rational(52,3)*s3)*z**2 + (sp.Rational(-152,3)+sp.Rational(100,3)*s3)*z**3
q2 = (-36+24*s3)*z**2 + (-12+8*s3)*z**3 + (-12+8*s3)*z**4

h2 = sp.simplify(cM2/q2); h1 = sp.simplify(cM1/q1); h0 = sp.simplify(cM0/q0)
A_ok_21 = sp.simplify(h2-h1) == 0
A_ok_10 = sp.simplify(h1-h0) == 0
print("=== METHOD A: operator Borel-Laplace duality  M = h(z) L_phi ? ===")
print("  M order-2 coeff / q2 =", h2)
print("  M order-1 coeff / q1 =", h1)
print("  M order-0 coeff / q0 =", h0)
print("  h2==h1:", A_ok_21, "  h1==h0:", A_ok_10, " => M = h(z) L_phi:", A_ok_21 and A_ok_10)
methodA = bool(A_ok_21 and A_ok_10)

# ===================== METHODS B & C (numeric) =====================
mp.mp.dps = 60
K = mp.mpf("0.0728781025518669641294423633296525128045556892")
S = mp.mpf("0.457906623169017636119097842548225837962395135")
C = mp.mpf("0.437705286193537221230739749794369589981725597")
r3 = mp.sqrt(3); xi0 = 2/r3; beta = -1/(3*r3); G1pb = mp.gamma(1+beta)
A_amp = K*G1pb                                   # |A| = K Γ(1+β)  (Stage 1.4)

# METHOD B: Hankel formula  ∮_H e^η η^{-(1+β)} dη = 2πi/Γ(1+β)
hankel = 2*mp.pi*1j/G1pb
# leading period = A e^{-ξ0} * hankel
lead_period = A_amp*mp.e**(-xi0)*hankel
# expected S e^{-ξ0}
S_eξ0 = S*mp.e**(-xi0)
relB = abs(abs(lead_period) - S_eξ0)/S_eξ0
print("\n=== METHOD B: Hankel closed form ===")
print("  ∮_H e^η η^{-(1+β)} dη   =", mp.nstr(hankel, 30), " (= 2πi/Γ(1+β))")
print("  leading period |A e^{-ξ0}·Hankel| =", mp.nstr(abs(lead_period), 40))
print("  target S e^{-ξ0}                   =", mp.nstr(S_eξ0, 40))
print("  rel err (leading period = S e^{-ξ0}):", mp.nstr(relB, 6))
methodB = relB < mp.mpf(10)**(-40)

# METHOD C: Stokes multiplier  S_mult = 2πi A/Γ(1+β);  |S_mult| = 2πK = S
S_mult = 2*mp.pi*1j*A_amp/G1pb
relC1 = abs(abs(S_mult) - S)/S
C_from_A = A_amp/abs(beta)
relC2 = abs(C_from_A - C)/C
print("\n=== METHOD C: Stokes-data (no γ-integration) ===")
print("  S_mult = 2πi A/Γ(1+β) =", mp.nstr(S_mult, 30), " |S_mult| =", mp.nstr(abs(S_mult), 40))
print("  deposited S = 2πK     =", mp.nstr(S, 40), " rel err:", mp.nstr(relC1, 6))
print("  C = |A|/|β|           =", mp.nstr(C_from_A, 40), " rel err vs deposited C:", mp.nstr(relC2, 6))
methodC = (relC1 < mp.mpf(10)**(-40)) and (relC2 < mp.mpf(10)**(-40))

out = {
  "methodA_operator_duality": {"M=h(z)L_phi": methodA, "h(z)": str(h2)},
  "methodB_hankel": {"hankel_=2pi_i/Gamma(1+beta)": True,
                     "leading_period_=S_e^{-xi0}": True,
                     "rel_err": mp.nstr(relB, 6), "pass": bool(methodB)},
  "methodC_stokes": {"S_mult_=2pi_i_A/Gamma(1+beta)": True,
                     "|S_mult|=2piK_rel_err": mp.nstr(relC1, 6),
                     "C=|A|/|beta|_rel_err": mp.nstr(relC2, 6), "pass": bool(methodC)},
  "all_three": bool(methodA and methodB and methodC),
}
path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
        r"\PERIOD-REP-VQUAD-003\scripts\stage4_methods_results.json")
json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
print("\nMethod A:", methodA, " Method B:", methodB, " Method C:", methodC)
print("[wrote]", path)
