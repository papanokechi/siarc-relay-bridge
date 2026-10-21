import sympy as sp
from math import prod

z, t, w = sp.symbols('z t w')
N = 45
Q = {-1: sp.Integer(0), 0: sp.Integer(1)}
for n in range(1, N + 1):
    b = 3*n*n + n + 1
    Q[n] = sp.Integer(b) * Q[n-1] + Q[n-2]
print('Q[0..10]=', [Q[i] for i in range(0, 11)])

# Verify inhomogeneous ODE through z^30.
f = sum(Q[n] * z**n for n in range(0, N + 1))
lhs_plus_1 = sp.expand(3*z**3*sp.diff(f,z,2) + 10*z**2*sp.diff(f,z) + (z**2 + 5*z - 1)*f + 1)
coeffs = [sp.expand(lhs_plus_1).coeff(z, n) for n in range(0, 31)]
print('A0 residual coefficients z^0..z^30=', coeffs)
print('A0 all_zero_through_30=', all(c == 0 for c in coeffs))
# Extra: coefficients through N-2, since truncation can affect top two degrees only via z^2 f and derivatives.
max_safe = N - 2
coeffs_safe = [sp.expand(lhs_plus_1).coeff(z, n) for n in range(0, max_safe + 1)]
print('A0 all_zero_through_%d='%max_safe, all(c == 0 for c in coeffs_safe))

# Normal form y'' + p y' + q y = 0, y = u exp(-1/2 integral p dz), u'' = r u.
p = sp.Rational(10, 3)/z
q = (z**2 + 5*z - 1)/(3*z**3)
r = sp.simplify(p**2/4 + sp.diff(p,z)/2 - q)
print('p=', p)
print('q=', q)
print('r_A=', sp.factor(r))
print('r_A numerator denominator=', sp.fraction(sp.factor(r)))

# Pole order helper at variable 0: order of pole of rational expr.
def pole_order_at_zero(expr, var):
    expr = sp.factor(sp.together(expr))
    num, den = sp.fraction(expr)
    num_poly = sp.Poly(num, var)
    den_poly = sp.Poly(den, var)
    def valuation(poly):
        terms = poly.terms()
        return min(exp[0][0] for exp in terms if exp[1] != 0)
    return valuation(den_poly) - valuation(num_poly)

po0 = pole_order_at_zero(r, z)
print('pole_order_r_at_z0=', po0)
print('finite_singular_denominator_roots=', sp.factor(sp.denom(sp.together(r))))
Rinf = sp.simplify(t**-4 * r.subs(z, 1/t))
print('R_infinity_t=t^-4*r(1/t)=', sp.factor(Rinf))
print('pole_order_at_infinity=', pole_order_at_zero(Rinf, t))
print('leading_z0=', sp.limit(z**po0 * r, z, 0))
print('leading_infinity_t0=', sp.limit(t**pole_order_at_zero(Rinf,t) * Rinf, t, 0))
print('katz_z0=(pole_order-2)/2=', sp.Rational(po0-2, 2))
print('katz_infinity=(pole_order-2)/2=', sp.Rational(pole_order_at_zero(Rinf,t)-2, 2))
print('ramification_z0=2 because pole order 3 is odd')
print('ramification_infinity=2 because pole order 3 is odd')
print('exponential_z0_pair= exp(± integral sqrt(1/(3*z^3)) dz) = exp(∓ 2/sqrt(3) * z^(-1/2))')
print('exponential_infinity_t_pair= exp(± integral sqrt(-1/(3*t^3)) dt) = exp(∓ 2*I/sqrt(3) * t^(-1/2))')

# Pullback z=w^2 for normal equation y''=r(z)y. Y'' - (1/w)Y' - 4*w^2*r(w^2)Y = 0.
pw = -1/w
qw = -4*w**2 * r.subs(z, w**2)
Rw = sp.simplify(pw**2/4 + sp.diff(pw,w)/2 - qw)
print('pullback_p_w=', pw)
print('pullback_q_w=', sp.factor(qw))
print('pullback_R_w=', sp.factor(Rw))
pow0 = pole_order_at_zero(Rw, w)
print('pullback_pole_order_w0=', pow0)
print('pullback_leading_w0=', sp.limit(w**pow0 * Rw, w, 0))
print('pullback_katz_w0=', sp.Rational(pow0-2, 2))
print('pullback_ramification_w0=1 because pole order 4 is even/unramified')
Rwinf = sp.simplify(t**-4 * Rw.subs(w, 1/t))
print('pullback_R_infinity_t=', sp.factor(Rwinf))
powinf = pole_order_at_zero(Rwinf, t)
print('pullback_pole_order_winfinity=', powinf)
print('pullback_leading_winfinity_t0=', sp.limit(t**powinf * Rwinf, t, 0))
print('pullback_katz_winfinity=', sp.Rational(powinf-2, 2))
print('pullback_ramification_winfinity=1 because pole order 4 is even/unramified')
print('pullback_exponential_w0_pair= exp(∓ 2/sqrt(3) * w^(-1))')
print('pullback_exponential_winfinity_t_pair= exp(∓ 2*I/sqrt(3) * t^(-1))')
