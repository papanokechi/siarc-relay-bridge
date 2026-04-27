"""
SPRINT-W3-SUBLEADING-BALANCE -- Part A
================================================================
Sub-leading Birkhoff expansion for the degree-(2,1) PCF.

The full Birkhoff-Adams ansatz used here is

    y_n = Gamma(n+1) * mu^n * n^alpha * (1 + c1/n + c2/n^2 + ...)

(the Gamma(n+1) is required for the leading-order balance because
a_n is degree-2 in n while b_n is degree-1).

Substituting into  y_{n+1} - b_n y_n + a_n y_{n-1} = 0 , dividing
through by  Gamma(n+1) mu^n n^alpha , one finds:

  Order n^1   :  characteristic eq. mu^2 - b1 mu + a2 = 0
  Order n^0   :  indicial linear equation in alpha (W1 closed form)
  Order n^-1  :  linear equation in c1, with coefficients depending
                 on (alpha, mu, a0, a1, a2, b0, b1)
  Order n^-2  :  linear in c2 (we do not need it here)

The W3 question: does the [n^-1] balance, after substituting the
W1-determined alpha = -((b1-b0) mu + a1 - a2)/(b1 mu - 2 a2), force
a constraint on (a0, a1, a2, b0, b1) which selects the Trans
locus a2/b1^2 = -2/9?

We compute the equation symbolically and inspect both:
  (i)  the c1 coefficient    [vanishing => resonance]
  (ii) the c1-free remainder [if non-zero => incompatibility]
"""

import sympy as sp
from sympy import (symbols, Rational, sqrt, simplify, expand, series,
                   together, Poly, factor, solve, Eq, collect, cancel, nsimplify)

# Symbols
n, mu, alpha = symbols("n mu alpha", positive=False)
a0, a1, a2, b0, b1 = symbols("a0 a1 a2 b0 b1")
c1, c2 = symbols("c1 c2")
u = symbols("u")    # u = 1/n

print("="*78)
print("Part A1/A2 -- Sub-leading Birkhoff expansion to order u^2 (= 1/n^2)")
print("="*78)

# ---------------------------------------------------------------
# Build the recurrence LHS / [Gamma(n+1) mu^n n^alpha]
# ---------------------------------------------------------------
# y_{n+1}/[Gamma(n+1) mu^n n^alpha]
#   = (n+1) * mu * (1+1/n)^alpha * (1 + c1/(n+1) + c2/(n+1)^2)
#
# y_n/[Gamma(n+1) mu^n n^alpha]
#   = 1 * (1 + c1/n + c2/n^2)
#
# y_{n-1}/[Gamma(n+1) mu^n n^alpha]
#   = (1/n) * (1/mu) * (1 - 1/n)^alpha * (1 + c1/(n-1) + c2/(n-1)^2)
#
# (since Gamma(n) = Gamma(n+1)/n, so y_{n-1}/Gamma(n+1) = (1/n) ...)

# Use u = 1/n; expand all 1/(n+-1) and (1+- 1/n)^alpha to order u^2.

def pow_expansion(sign, order=2):
    """(1 + sign u)^alpha to given order in u, removing O()."""
    return series((1 + sign*u)**alpha, u, 0, order+1).removeO()

# Series in u of 1/(1+u) and 1/(1-u)
inv_plus  = series(1/(1+u), u, 0, 4).removeO()    # 1 - u + u^2 - u^3
inv_minus = series(1/(1-u), u, 0, 4).removeO()    # 1 + u + u^2 + u^3
inv_plus_sq  = expand(inv_plus**2)
inv_minus_sq = expand(inv_minus**2)

L_plus  = pow_expansion(+1, 3)
L_minus = pow_expansion(-1, 3)

# --- y_{n+1} contribution ---
# (n+1) mu = mu*(1 + u)/u            (since n = 1/u, n+1 = (1+u)/u)
# 1/(n+1) = u/(1+u) = u * inv_plus
# 1/(n+1)^2 = u^2 * inv_plus_sq
T_plus = (mu * (1 + u) / u) * L_plus * (1 + c1 * u * inv_plus + c2 * u**2 * inv_plus_sq)

# --- y_n contribution: -b_n * (...) ---
# b_n = b1 n + b0 = b1/u + b0
T_zero = -(b1/u + b0) * (1 + c1*u + c2*u**2)

# --- y_{n-1} contribution ---
# a_n / (n mu) = (a2 n^2 + a1 n + a0) * u / mu
#              = (a2/u^2 + a1/u + a0) * u / mu
#              = (a2/u + a1 + a0*u) / mu
# 1/(n-1) = u/(1-u) = u * inv_minus
T_minus = ((a2/u + a1 + a0*u) / mu) * L_minus * (1 + c1*u*inv_minus + c2*u**2*inv_minus_sq)

LHS = T_plus + T_zero + T_minus
LHS_expanded = expand(LHS)

# Multiply by u^3 to clear all 1/u and 1/u^2 factors that appear with c2.
# We only need terms up to and including u^1 in the result (corresponds to
# original order n^{-1}).  So multiply by u and look at coefficients of
# u^{-1}, u^0, u^1.
LHS_u = series(LHS_expanded, u, 0, 4).removeO()
# Strip terms beyond u^1 (we don't need c2's full constraint, only c1)
LHS_u_simpl = expand(LHS_u)

# Now isolate coefficients in u: need [u^{-1}], [u^0], [u^1].
# Use sympy series of the symbolic expression in u and read coefficients.
sr = series(LHS_expanded, u, 0, 3)   # captures up to and including u^2
# convert to dict {power: coeff}
coeff_neg1 = simplify(LHS_expanded.coeff(u, -1))
coeff_0    = simplify(LHS_expanded.coeff(u, 0))
coeff_1    = simplify(LHS_expanded.coeff(u, 1))

print("\n[u^{-1}] coefficient (== leading n^1 balance):")
print(f"   {coeff_neg1}")
print("\n[u^{0}] coefficient (== indicial / next-to-leading n^0 balance):")
print(f"   {coeff_0}")
print("\n[u^{+1}] coefficient (== sub-leading n^-1 balance, contains c1):")
print(f"   {coeff_1}")

# Sanity:  [u^{-1}] should reduce to (mu^2 - b1 mu + a2)/mu after multiplying
# by mu.
print("\nSanity:  mu * [u^{-1}]  =", simplify(coeff_neg1 * mu))

# ---------------------------------------------------------------
# Step A3: [u^0] gives the indicial relation.  Solve for alpha modulo
# the characteristic equation mu^2 = b1 mu - a2.
# ---------------------------------------------------------------
print("\n" + "="*78)
print("Sanity: solve [u^0] for alpha after imposing mu^2 = b1 mu - a2.")
print("="*78)
# Reduce powers of mu using mu^2 = b1 mu - a2
def reduce_mu(expr):
    expr = expand(expr)
    # repeatedly substitute mu^k for k>=2 down to mu, mu^0
    for k in range(8, 1, -1):
        expr = expr.subs(mu**k, mu**(k-2) * (b1*mu - a2))
        expr = expand(expr)
    return simplify(expr)

# The c1 term in [u^0] should be zero, since c1 only enters via 1/(n+- 1)
# at order >= u^1.  Confirm:
print("  c1 in [u^0]:", coeff_0.coeff(c1))   # expected 0

# Now [u^0] = 0 should determine alpha.  The c1-coefficient is 0, so [u^0]
# is independent of c1.  Multiply by mu to clear and solve for alpha.
ind_balance = simplify(coeff_0 * mu)
ind_balance_red = reduce_mu(ind_balance)
print(f"  mu * [u^0] (after mu^2 -> b1 mu - a2): {ind_balance_red}")
alpha_sol = solve(ind_balance_red, alpha)
print(f"  alpha solutions: {alpha_sol}")

if not alpha_sol:
    print("  HALT (analytic): no solution for alpha.")
    raise SystemExit(1)

alpha_W1 = alpha_sol[0]
print(f"\nW1 indicial closed form: alpha = {alpha_W1}")

# Cross-check against the W1 closed form
alpha_closedform = -((b1 - b0)*mu + (a1 - a2)) / (b1*mu - 2*a2)
diff = simplify(alpha_W1 - alpha_closedform)
print(f"  matches W1 closed form?  diff = {simplify(diff)}")

# ---------------------------------------------------------------
# Step A3 cont'd / A4: [u^1] balance is linear in c1.  Extract.
# ---------------------------------------------------------------
print("\n" + "="*78)
print("Step A3/A4 -- [u^1] balance as linear equation in c1.")
print("="*78)

eq_subleading = simplify(coeff_1)
# Extract c1- and c2-coefficients robustly via Poly().  Note that c2 also
# enters at this order; its coefficient should equal mu^2 - b1 mu + a2
# (the characteristic polynomial), so it drops out automatically on the
# characteristic locus.
poly_c12 = Poly(eq_subleading, c1, c2)
A_c1 = simplify(poly_c12.coeff_monomial(c1))               # c1 coefficient
A_c2 = simplify(poly_c12.coeff_monomial(c2))               # c2 coefficient
B_c1 = simplify(poly_c12.coeff_monomial(1))                # c1- and c2-free remainder
print(f"  Coefficient of c1:  A_c1 = {A_c1}")
print(f"  Coefficient of c2:  A_c2 = {A_c2}")
print(f"  c1- and c2-free remainder:  B = {B_c1}")
print()
print("  The [u^1] balance is  A_c1 * c1 + A_c2 * c2 + B = 0.")
print("  RESONANCE if  A_c1 = 0  while  B != 0  (after eliminating c2 via char eq).")
print()

# ---------------------------------------------------------------
# Reduce A_c1 and B_c1 modulo (mu^2 = b1 mu - a2) and substitute alpha
# ---------------------------------------------------------------
print("="*78)
print("Reduce A and B modulo the characteristic equation, then substitute")
print("alpha = -((b1-b0) mu + a1 - a2) / (b1 mu - 2 a2).")
print("="*78)
A_red   = reduce_mu(A_c1)
A_c2_red = reduce_mu(A_c2)
B_red   = reduce_mu(B_c1)
print(f"  A_c1 (mu^2 reduced) = {A_red}")
print(f"  A_c2 (mu^2 reduced) = {A_c2_red}    (should be 0 on char locus)")
print(f"  B    (mu^2 reduced) = {B_red}")

# Substitute alpha
A_sub_alpha = simplify(A_red.subs(alpha, alpha_closedform))
B_sub_alpha = simplify(B_red.subs(alpha, alpha_closedform))
print()
print(f"  A | alpha=W1 :  {A_sub_alpha}")
print(f"  B | alpha=W1 :  {B_sub_alpha}")

# Reduce mu^2 once more (alpha-substitution introduced new mu's)
A_final = simplify(reduce_mu(together(A_sub_alpha)))
B_final = simplify(reduce_mu(together(B_sub_alpha)))
print()
print(f"  A_final = {A_final}")
print(f"  B_final = {B_final}")

# ---------------------------------------------------------------
# Step A4 -- resonance:  A_final = 0 ?
# ---------------------------------------------------------------
print()
print("="*78)
print("RESONANCE TEST -- when does A_final vanish?")
print("="*78)

# A_final is a polynomial / rational function in (mu, a0, a1, a2, b0, b1).
# Its denominator vanishing is a constraint on params alone (no mu).
A_num, A_den = sp.fraction(together(A_final))
B_num, B_den = sp.fraction(together(B_final))
print(f"  A numerator   = {factor(A_num)}")
print(f"  A denominator = {factor(A_den)}")
print(f"  B numerator   = {factor(B_num)}")
print(f"  B denominator = {factor(B_den)}")

# Solve A_num = 0 for a2 (treating mu, b0, b1, a1, a0 as known)
print()
print("Solve A_num = 0 for various unknowns:")

for var in (a2, a1, a0, b0):
    try:
        sols = solve(A_num, var)
        print(f"  A_num = 0  ->  {var} = {sols}")
    except Exception as e:
        print(f"  A_num = 0 for {var}: solve failed ({e})")

# Now also reduce A_num modulo mu^2 = b1 mu - a2 once more, then
# extract coefficient of mu^0 and mu^1: each must vanish independently
# for the equation to hold with no constraint on mu.
A_num_red = reduce_mu(A_num)
print(f"\n  A_num reduced (lowest mu form) = {expand(A_num_red)}")
A_poly_in_mu = Poly(A_num_red, mu)
print(f"  As polynomial in mu:  degree = {A_poly_in_mu.degree()}")
for k, c in enumerate(A_poly_in_mu.all_coeffs()[::-1]):
    print(f"    [mu^{k}] = {factor(simplify(c))}")

print()
print("If A_num is identically zero in mu, then resonance holds")
print("along the ENTIRE locus of those parameter constraints.")
print("If A_num has nonzero mu-coefficients, resonance is conditional on")
print("a specific value of mu (= specific characteristic root).")

# ---------------------------------------------------------------
# Substitute the Trans constraint a2 = -2 b1^2 / 9 and re-examine
# ---------------------------------------------------------------
print()
print("="*78)
print("Examine A_final / B_final on the Trans locus a2 = -2 b1^2 / 9")
print("="*78)
trans_sub = {a2: -Rational(2)*b1**2/9}
A_trans = simplify(reduce_mu(together(A_final.subs(trans_sub))))
B_trans = simplify(reduce_mu(together(B_final.subs(trans_sub))))
print(f"  A | Trans = {A_trans}")
print(f"  B | Trans = {B_trans}")

# Substitute mu = b1 (3+sqrt17)/6 (one of the two char roots).
mu_plus = b1 * (3 + sqrt(17))/6
A_T_mu  = simplify(A_trans.subs(mu, mu_plus))
B_T_mu  = simplify(B_trans.subs(mu, mu_plus))
print(f"\n  A | Trans, mu_+   =  {A_T_mu}")
print(f"  B | Trans, mu_+   =  {B_T_mu}")

# Substitute mu = b1 (3-sqrt17)/6
mu_minus = b1 * (3 - sqrt(17))/6
A_T_mu_m  = simplify(A_trans.subs(mu, mu_minus))
B_T_mu_m  = simplify(B_trans.subs(mu, mu_minus))
print(f"\n  A | Trans, mu_-   =  {A_T_mu_m}")
print(f"  B | Trans, mu_-   =  {B_T_mu_m}")

# ---------------------------------------------------------------
# A4 final test:  is the resonance A=0 equivalent to a2/b1^2 = -2/9 ?
# Concretely, test on a non-Trans locus (e.g. a2 = -b1^2/4) whether
# A still vanishes.
# ---------------------------------------------------------------
print()
print("="*78)
print("Comparison: A on non-Trans loci")
print("="*78)
for ratio_label, ratio_val in [("a2/b1^2 = -2/9 (Trans)", -Rational(2)/9),
                               ("a2/b1^2 = -1/4   (Log)", -Rational(1)/4),
                               ("a2/b1^2 = -1/9   (Log)", -Rational(1)/9),
                               ("a2/b1^2 = -1/36  (Log)", -Rational(1)/36)]:
    sub = {a2: ratio_val * b1**2}
    A_s = simplify(reduce_mu(together(A_final.subs(sub))))
    # try to simplify by substituting mu = mu_+ for that ratio
    # For -2/9:  mu = b1(3+sqrt17)/6
    # For -1/4:  disc = b1^2 - 4*(-b1^2/4) = 2 b1^2 -> mu = b1(1+sqrt2)/2
    print(f"  {ratio_label:<32}:  A_final = {A_s}")

print()
print("If A is identically zero on the Trans locus but nonzero elsewhere,")
print("we have a NEW invariant.  If A is identically zero everywhere,")
print("the [n^-1] balance is degenerate and provides no constraint.")
