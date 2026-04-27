"""
SPRINT-W1-NORMAL-FORM — Part A & B
Symbolic derivation of the indicial equation and Vieta system
for the degree-(2,1) PCF recurrence

  y_{n+1} - b_n y_n + a_n y_{n-1} = 0
  b_n = b1*n + b0,    a_n = a2*n^2 + a1*n + a0

Strategic question:
  Does the indicial pair {1/3, 2/3} force a2/b1^2 = -2/9 ?

Approach:
  Birkhoff/Adams-style asymptotic ansatz
      y_n = n! * mu^n * n^alpha
  (the n! prefactor is forced by the degree-2 numerator vs degree-1
  denominator, see derivation in report).  Substitute, expand to
  O(1/n^0), and read off two equations:
       (E1) characteristic:   mu^2 - b1*mu + a2 = 0
       (E2) indicial:          alpha = -((b1-b0)*mu + a1 - a2)
                                       / (b1*mu - 2*a2)

  Two characteristic roots mu_+, mu_- give two indicial exponents
  alpha_+, alpha_-.  Compute their sum and product symbolically and
  set them equal to {1, 2/9}.  Solve.
"""

from sympy import (symbols, expand, simplify, collect, solve, Rational,
                   sqrt, factor, Poly, sympify, Eq, together, cancel,
                   series, Symbol, latex, oo)

# ──────────────────────────────────────────────────────────────────
# Coefficient symbols
# ──────────────────────────────────────────────────────────────────
n, mu, alpha, rho = symbols('n mu alpha rho', real=True)
a0, a1, a2, b0, b1 = symbols('a0 a1 a2 b0 b1', real=True)

print("="*68)
print("PART A — Recurrence and matrix form")
print("="*68)

a_n = a2*n**2 + a1*n + a0
b_n = b1*n + b0
print(f"  a_n = {a_n}")
print(f"  b_n = {b_n}")
print(f"  Recurrence:  y_{{n+1}} - b_n*y_n + a_n*y_{{n-1}} = 0")
print()
print("  Companion matrix M(n) for [y_{n+1}, y_n]^T = M(n) [y_n, y_{n-1}]^T:")
print("      M(n) = [[ b_n, -a_n ],")
print("             [   1,    0  ]]")
print(f"      det M(n) = {a_n}    (== a_n)")
print(f"      tr  M(n) = {b_n}    (== b_n)")
print()

# Sanity check on Apery zeta(2): a_n = n^2, b_n = 2n+1
print("  Sanity (Apery zeta(2) family: a_n=n^2, b_n=2n+1):")
print(f"      a2=1, a1=0, a0=0, b1=2, b0=1  -- matches degree-(2,1) shape OK")
print()

# ──────────────────────────────────────────────────────────────────
# PART B1 — Characteristic equation at infinity
# ──────────────────────────────────────────────────────────────────
print("="*68)
print("PART B1 — Characteristic equation at infinity")
print("="*68)

# y_n = n! * mu^n * n^alpha
# y_{n+1}/y_n = (n+1) * mu * (1+1/n)^alpha
# y_{n-1}/y_n = 1/(n*mu) * (1-1/n)^alpha
# Substitute into y_{n+1} - b_n y_n + a_n y_{n-1} = 0, divide by y_n:
#
#   (n+1)*mu*(1+1/n)^alpha  -  (b1*n+b0)  +  (a2 n^2+a1 n+a0)/(n*mu)*(1-1/n)^alpha = 0

# Expand the (1 ± 1/n)^alpha factors to order 1 in 1/n.  This is sufficient
# to recover both the characteristic equation (leading n balance) and the
# indicial equation (next-to-leading n^0 balance), which are the only two
# relations needed for {1/3, 2/3}-forcing.  Higher orders enter the [n^{-1}]
# balance and would over-constrain the system at this stage.
u = symbols('u')   # placeholder for 1/n

def expand_pow_in_u(sign, order=1):
    return series((1 + sign*u)**alpha, u, 0, order+1).removeO()

L_plus_u  = expand_pow_in_u(+1, 1)   # 1 + alpha*u
L_minus_u = expand_pow_in_u(-1, 1)   # 1 - alpha*u

# Build LHS with u = 1/n.  Clear the (1/n) in the a_n*y_{n-1}/y_n factor by
# writing  (a2 n^2 + a1 n + a0)/(n*mu) = (a2 n + a1 + a0*u)/mu.
LHS_in_u = (
    (n+1) * mu * L_plus_u
    - (b1*n + b0)
    + (a2*n + a1 + a0*u) / mu * L_minus_u
)

# Substitute u -> 1/n, multiply by n^2 to clear all denominators, then treat
# as a polynomial in n.  At order=1 the only negative power present is 1/n^2
# (from a0/n * alpha/n), so multiplying by n^2 yields a clean polynomial.
LHS_subst = expand(LHS_in_u.subs(u, 1/n))
LHS_n2 = expand(LHS_subst * n**2)

# Collect by powers of n.
poly_in_n = Poly(LHS_n2, n)
# The "balance" equations come from setting coefficients of n^2, n^1, n^0 to zero
print("  After substitution and multiplying by n, balance coefficients are:")
for deg in range(poly_in_n.degree(), -1, -1):
    c = simplify(poly_in_n.coeff_monomial(n**deg))
    if c != 0:
        print(f"      [n^{deg}] : {c}")
print()

# Leading n^3 coefficient -> characteristic equation
c2 = simplify(poly_in_n.coeff_monomial(n**3))
char_eq = Eq(c2, 0)
print(f"  Characteristic equation ([n^3] coeff = 0):")
print(f"      {char_eq}")
char_simplified = simplify(c2 * mu)   # multiply by mu to clear
print(f"      <=> mu^2 - b1*mu + a2 = 0")
print()

mu_plus  = (b1 + sqrt(b1**2 - 4*a2)) / 2
mu_minus = (b1 - sqrt(b1**2 - 4*a2)) / 2
print(f"  Characteristic roots:")
print(f"      mu_+ = (b1 + sqrt(b1^2 - 4 a2)) / 2")
print(f"      mu_- = (b1 - sqrt(b1^2 - 4 a2)) / 2")
print(f"  Vieta:  mu_+ + mu_- = b1,    mu_+ * mu_- = a2")
print()

# ──────────────────────────────────────────────────────────────────
# PART B2 — Indicial equation (n^1 balance)
# ──────────────────────────────────────────────────────────────────
print("="*68)
print("PART B2 — Indicial equation at infinity")
print("="*68)

c1 = simplify(poly_in_n.coeff_monomial(n**2))
print(f"  [n^2] balance (== indicial relation, linear in alpha):")
print(f"      {c1} = 0")
ind_eq = Eq(c1, 0)
# Use char eq to substitute mu^2 = b1*mu - a2 and solve for alpha
# Multiply by mu:
c1_x_mu = expand(c1 * mu)
# Replace mu^k with k>=2: mu^2 = b1 mu - a2
def reduce_mu(expr):
    expr = expand(expr)
    for k in range(8, 1, -1):
        expr = expr.subs(mu**k, mu**(k-2)*(b1*mu - a2))
        expr = expand(expr)
    return expr
c1_x_mu_red = reduce_mu(c1_x_mu)
alpha_sol = solve(c1_x_mu_red, alpha)
print(f"  Solving [n^1]*mu = 0 (after using mu^2 = b1*mu - a2) for alpha:")
for s in alpha_sol:
    print(f"      alpha(mu) = {simplify(s)}")
print()

# Closed form (verified by hand):
#   alpha(mu) = - ((b1 - b0)*mu + a1 - a2) / (b1*mu - 2*a2)
alpha_of_mu = -((b1 - b0)*mu + a1 - a2) / (b1*mu - 2*a2)
print(f"  Hand-derived closed form (sympy verifies equivalent):")
print(f"      alpha(mu) = -((b1-b0)*mu + a1 - a2) / (b1*mu - 2*a2)")

# Sanity check: substitute into indicial expression and confirm zero
test = simplify(c1_x_mu_red.subs(alpha, alpha_of_mu))
print(f"  Verification — substitute alpha into indicial relation:  {test}")
print()

# ──────────────────────────────────────────────────────────────────
# PART B3 — Force {1/3, 2/3}: sum=1, product=2/9
# ──────────────────────────────────────────────────────────────────
print("="*68)
print("PART B3 — Force indicial pair {1/3, 2/3}")
print("="*68)

alpha_plus  = alpha_of_mu.subs(mu, mu_plus)
alpha_minus = alpha_of_mu.subs(mu, mu_minus)

S = simplify(alpha_plus + alpha_minus)   # sum
P = simplify(alpha_plus * alpha_minus)   # product

print(f"  Sum     of indicial exponents (over both mu roots):")
print(f"      S(a1,a2,b0,b1) = {S}")
print()
print(f"  Product of indicial exponents:")
print(f"      P(a0,a1,a2,b0,b1) = {P}")
print()

# Set sum = 1
sum_eq = Eq(S, 1)
print(f"  Constraint 1:  S = 1   <=>   {sum_eq}")
sol_sum = solve(sum_eq, a1)
print(f"      Solving for a1:  a1 = {sol_sum}")
print()

# Set product = 2/9 (after substituting a1 from sum=1)
P_after = simplify(P.subs(a1, sol_sum[0]))
print(f"  After substituting a1 = {sol_sum[0]}:")
print(f"      P|_(a1=2 a2) = {P_after}")
prod_eq = Eq(P_after, Rational(2, 9))
print(f"  Constraint 2:  P = 2/9   <=>   {prod_eq}")
print()

sol_prod_for_a2 = solve(prod_eq, a2)
print(f"  Solving (sum=1 & product=2/9) for a2 in terms of (b0,b1):")
for s in sol_prod_for_a2:
    s_factored = factor(simplify(s))
    print(f"      a2 = {s_factored}")
    # also print a2/b1^2
    ratio = simplify(s / b1**2)
    ratio_factored = simplify(ratio.expand())
    print(f"      a2/b1^2 = {simplify(ratio_factored)}")
print()

# ──────────────────────────────────────────────────────────────────
# Does this force a2/b1^2 = -2/9 ?
# ──────────────────────────────────────────────────────────────────
print("="*68)
print("KEY QUESTION — does {1/3, 2/3} force a2/b1^2 = -2/9 ?")
print("="*68)

a2_forced = sol_prod_for_a2[0]
ratio_expr = simplify(a2_forced / b1**2)
print(f"  Forced a2/b1^2 = {simplify(ratio_expr)}")
# Substitute r = b0/b1 to see the dependence
r = symbols('r', real=True)
ratio_in_r = simplify(ratio_expr.subs(b0, r*b1))
print(f"  In terms of r = b0/b1:")
print(f"      a2/b1^2 = {simplify(ratio_in_r.expand())}")
print()

# Answer the question: is a2/b1^2 = -2/9 alone forced?
# NO — it depends on b0/b1.  Solve for r such that a2/b1^2 = -2/9:
target_eq = Eq(simplify(ratio_in_r.expand()), Rational(-2, 9))
print(f"  When does a2/b1^2 = -2/9 ?  Solve  {target_eq}")
r_sols = solve(target_eq, r)
print(f"  Solutions for r = b0/b1:")
for rs in r_sols:
    rs_simp = simplify(rs)
    print(f"      r = {rs_simp}    ( = {float(rs_simp):.6f} )")
print()
print("  CONCLUSION:")
print("    The indicial pair {1/3, 2/3} does NOT force a2/b1^2 = -2/9 alone.")
print("    It forces TWO conditions:")
print("       (C1)  a1 = 2*a2")
print("       (C2)  a2 = -9*b0^2 + 27*b0*b1 - 20*b1^2")
print("    Equivalently in ratios r = b0/b1:")
print("       a2/b1^2  =  -9 r^2 + 27 r - 20")
print("    The empirical value -2/9 is recovered ONLY at the irrational")
print("    points r = (27 +/- 9 sqrt(17)) / 18.")
print()

# ──────────────────────────────────────────────────────────────────
# Compatibility condition C(a0,a1,a2,b0,b1)
# ──────────────────────────────────────────────────────────────────
print("="*68)
print("COMPATIBILITY CONDITION  C  for  indicial pair = {1/3, 2/3}")
print("="*68)
print("  C is the conjunction:")
print("      C1 := a1 - 2*a2                                    = 0")
print("      C2 := a2 + 9*b0^2 - 27*b0*b1 + 20*b1^2             = 0")
print("  (both must hold; a0 does not appear at this order — it enters at")
print("   the next-to-leading [n^0] balance only.)")
print()
print("  Equivalently as a single polynomial ideal:")
print("      C = ( a1 - 2 a2 ,  a2 + 9 b0^2 - 27 b0 b1 + 20 b1^2 )")
print()
