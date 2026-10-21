import hashlib
import sympy as sp


def line(title):
    print()
    print(f"=== {title} ===")


x = sp.symbols("x")
a = 3*x**2 + x + 1
c_op = -x**2
p = sp.diff(a, x) / a
q = c_op / a
R = sp.factor(p**2 / 4 + sp.diff(p, x) / 2 - q)
R_claim = (12*x**4 + 4*x**3 + 4*x**2 + 11) / (4*(3*x**2 + x + 1)**2)

line("C1 normal-form potential")
print("a =", a)
print("p = a'/a =", sp.factor(p))
print("q = c/a =", sp.factor(q))
print("R =", R)
print("R - R_claim =", sp.simplify(R - R_claim))

line("C2 finite singular exponents")
roots = sp.solve(sp.Eq(a, 0), x)
print("roots =", roots)
for idx, s in enumerate(roots, 1):
    residue = sp.simplify(sp.limit((x - s)**2 * R, x, s))
    exponent_difference = sp.simplify(sp.sqrt(1 + 4*residue))
    print(f"root_{idx} =", s)
    print(f"lim (x-root_{idx})^2 R =", residue)
    print(f"sqrt(1+4*residue) =", exponent_difference)

line("C3 infinity")
print("limit R at infinity =", sp.limit(R, x, sp.oo))
print("sqrt(limit) =", sp.sqrt(sp.limit(R, x, sp.oo)))
print("WKB exponential leading factors: exp(± x/sqrt(3)); difference = (2/sqrt(3))*x")

line("C4-C5 parameter arithmetic")
theta0, thetat, thetainf = sp.symbols("theta0 thetat thetainf")
alpha = sp.Rational(1, 8) * (theta0 - thetat + thetainf)**2
beta = -sp.Rational(1, 8) * (theta0 - thetat - thetainf)**2
gamma = 1 - theta0 - thetat
delta = -sp.Rational(1, 2)
subs_zero = {theta0: 0, thetat: 0}
print("alpha|theta0=thetat=0 =", sp.simplify(alpha.subs(subs_zero)))
print("beta|theta0=thetat=0 =", sp.simplify(beta.subs(subs_zero)))
print("gamma|theta0=thetat=0 =", sp.simplify(gamma.subs(subs_zero)))
print("delta =", delta)
print("beta + alpha under theta0=thetat=0 =", sp.simplify((alpha + beta).subs(subs_zero)))
print("If beta=0 then theta_inf solutions =", sp.solve(sp.Eq(beta.subs(subs_zero), 0), thetainf))
print("alpha at those solutions =", [sp.simplify(alpha.subs(subs_zero).subs(thetainf, sol)) for sol in sp.solve(sp.Eq(beta.subs(subs_zero), 0), thetainf)])
print("published tuple tested arithmetically: (1/6, 0, 0, -1/2)")
print("gamma conflict with derived gamma=1:", sp.Rational(0) != sp.Rational(1))

line("C6 PV scaling derivation")
z, k = sp.symbols("z k", nonzero=True)
w, wp = sp.symbols("w wp")
alpha_s, beta_s, gamma_s, delta_s = sp.symbols("alpha beta gamma delta")
shape = sp.Rational(1, 2)/w + 1/(w - 1)
finite = (w - 1)**2 * (alpha_s*w + beta_s/w)
last = w*(w + 1)/(w - 1)

def pv_rhs(var, deriv, A, B, G, D):
    return shape*deriv**2 - deriv/var + finite/var**2 + G*w/var + D*last

# New dependent variable W(z) = old_w(k*z).  If old_w solves PV in variable Z
# with parameters (alpha,beta,gamma,delta), then W' = k old_w' and
# W'' = k^2 old_w'' evaluated at Z=k*z.
transformed_rhs = sp.factor(k**2 * pv_rhs(k*z, wp/k, alpha_s, beta_s, gamma_s, delta_s))
claimed_new_rhs = sp.factor(pv_rhs(z, wp, alpha_s, beta_s, k*gamma_s, k**2*delta_s))
print("For W(z)=w(k*z), transformed RHS =")
print(transformed_rhs)
print("PV RHS with (alpha,beta,k*gamma,k^2*delta) =")
print(claimed_new_rhs)
print("difference =", sp.simplify(transformed_rhs - claimed_new_rhs))

# Conversely, if the new coordinate is Z=k*z and V(Z)=w(Z/k), the transformed
# parameters are reciprocal in gamma and delta.
reciprocal_rhs = sp.factor((1/k**2) * pv_rhs(z/k, k*wp, alpha_s, beta_s, gamma_s, delta_s))
inverse_new_rhs = sp.factor(pv_rhs(z, wp, alpha_s, beta_s, gamma_s/k, delta_s/k**2))
print("For V(Z)=w(Z/k), transformed RHS =")
print(reciprocal_rhs)
print("PV RHS with (alpha,beta,gamma/k,delta/k^2) difference =", sp.simplify(reciprocal_rhs - inverse_new_rhs))

line("C7 affine normalization")
s_plus = roots[0]
s_minus = roots[1]
separation = sp.simplify(s_plus - s_minus)
k_forced = sp.Rational(2) / sp.sqrt(3)
print("root separation s_plus - s_minus =", separation)
print("k forced by 2/sqrt(3) WKB difference matching Jimbo exp difference z:", k_forced)
print("t values from the two orderings:")
print("k*(s_plus - s_minus) =", sp.simplify(k_forced * separation))
print("k*(s_minus - s_plus) =", sp.simplify(-k_forced * separation))
print("|t|^2 =", sp.simplify((k_forced * separation) * sp.conjugate(k_forced * separation)))
print("|t| =", 2*sp.sqrt(33)/9)

