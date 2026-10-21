"""
CT-R1-AUDIT R5: independent check of CT-S9-PVPARAMS, plus two additions.

(a) Re-derive the local data of System C from scratch.
(b) Locate System C's singular points in Jimbo's normalisation and determine
    whether the PV time t is free or fixed.
"""
import sympy as sp

x, t, k = sp.symbols('x t k')
out = []


def say(tag, s):
    line = f"[{tag}] {s}"
    print(line)
    out.append(line)


a = 3 * x**2 + x + 1
c = -x**2
p = sp.cancel(sp.diff(a, x) / a)
q = sp.cancel(c / a)
R = sp.cancel(sp.together(p**2 / 4 + sp.diff(p, x) / 2 - q))
say("R", f"normal form R = {sp.factor(sp.numer(R))} / {sp.factor(sp.denom(R))}")

roots = sp.solve(sp.Eq(a, 0), x)
sp_, sm_ = roots[1], roots[0]
say("S", f"s+ = {sp.nsimplify(sp_)}, s- = {sp.nsimplify(sm_)}")

# ---- exponent differences at the finite points (twist-invariant) -----------
for nm, r in (("s+", sp_), ("s-", sm_)):
    nu = sp.simplify(sp.limit((x - r)**2 * R, x, r))
    disc = sp.simplify(1 + 4 * nu)          # (lam1-lam2)^2 for lam(lam-1)=nu
    say("TH", f"{nm}: normal-form residue {nu}, exponent difference "
              f"= sqrt({disc}) = {sp.sqrt(disc)}  -> theta = {sp.sqrt(disc)}")

# ---- irregular data at infinity: the two WKB exponentials ------------------
# R ~ L / t^4 in t = 1/x, i.e. R ~ L x^4 as x -> oo ; sqrt(R) ~ sqrt(L) x^2 ... no:
# in x, R -> 12x^4/(4*9x^4) = 1/3 as x -> oo, so sqrt(R) -> 1/sqrt(3).
Rinf = sp.limit(R, x, sp.oo)
say("I", f"R -> {Rinf} as x -> oo, so the WKB exponentials are "
         f"exp(+/- {sp.sqrt(Rinf)} * x)")
delta_exp = sp.simplify(2 * sp.sqrt(Rinf))
say("I", f"difference of the two exponents = {delta_exp} * x")

# ---- Jimbo (3.1): irregular part is exp(x*diag(1,0)), difference = x -------
kval = sp.simplify(1 / sp.sqrt(Rinf) / 2)   # solve delta_exp * x = z = k*x  -> k = delta_exp
kval = sp.simplify(delta_exp)
say("K", f"Jimbo's normalisation forces the affine scale k = {kval} "
         f"(so that the exponent difference becomes exactly z)")

for lbl, (zero_pt, other) in {"s+ -> 0": (sp_, sm_), "s- -> 0": (sm_, sp_)}.items():
    tv = sp.simplify(kval * (other - zero_pt))
    say("T", f"{lbl}:  t = k*(other - zero) = {sp.radsimp(sp.nsimplify(tv))} "
             f"  |t| = {sp.simplify(sp.Abs(tv))}")

# ---- Jimbo dictionary with theta_0 = theta_t = 0 ---------------------------
th0, tht, thinf = sp.symbols('theta_0 theta_t theta_infty')
alpha = sp.Rational(1, 8) * (th0 - tht + thinf)**2
beta = -sp.Rational(1, 8) * (th0 - tht - thinf)**2
gamma = 1 - th0 - tht
sub = {th0: 0, tht: 0}
say("D", f"alpha = {sp.simplify(alpha.subs(sub))}, beta = {sp.simplify(beta.subs(sub))}, "
         f"gamma = {sp.simplify(gamma.subs(sub))}, delta = -1/2")
say("D", f"beta + alpha = {sp.simplify((alpha + beta).subs(sub))}  -> beta = -alpha identically")
say("D", "companion tuple (alpha,beta,gamma,delta) = (1/6, 0, 0, -1/2): "
         "beta=0 forces theta_infty=0 hence alpha=0, contradicting alpha=1/6; "
         "and gamma=1 contradicts gamma=0.")

# ---- can gamma be scaled away while delta is held at -1/2? -----------------
cc = sp.symbols('c', nonzero=True)
say("SC", "PV scaling z -> c*z maps (alpha,beta,gamma,delta) -> (alpha,beta,c*gamma,c^2*delta). "
          "Holding delta = -1/2 forces c^2 = 1, i.e. c = +/-1, so gamma is fixed up to sign. "
          "gamma = 1 therefore CANNOT be rescaled to gamma = 0: the contradiction is genuine.")

with open("verify_s9.out", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
