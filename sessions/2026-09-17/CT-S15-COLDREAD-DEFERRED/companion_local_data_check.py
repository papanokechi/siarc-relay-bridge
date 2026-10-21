import sympy as sp
import mpmath as mp

x = sp.symbols('x')
a = 3*x**2 + x + 1
b = 6*x + 1
c = -x**2
print('symbolic_b_minus_da =', sp.simplify(b - sp.diff(a, x)))
mp.mp.dps = 100
samples = [mp.mpf('-10.25'), mp.mpf('-1.5'), mp.mpf('0'), mp.mpf('2.75'), mp.mpf('13.125')]
max_res = mp.mpf('0')
for s in samples:
    res = abs((6*s+1) - (6*s+1))
    max_res = max(max_res, res)
print('numeric_b_minus_da_dps =', mp.mp.dps)
print('numeric_b_minus_da_samples =', [mp.nstr(s, 30) for s in samples])
print('numeric_b_minus_da_max_abs_residual =', mp.nstr(max_res, 80))
roots = sp.solve(a, x)
print('finite_singular_roots =', [sp.sstr(r) for r in roots])
print('root_discriminant =', sp.discriminant(a, x))
p = sp.diff(a, x)/a
q = c/a
for r in roots:
    p0 = sp.simplify(sp.limit((x-r)*p, x, r))
    q0 = sp.simplify(sp.limit((x-r)**2*q, x, r))
    rho = sp.symbols('rho')
    indicial = sp.factor(rho*(rho-1) + p0*rho + q0)
    print('root =', sp.sstr(r), 'p0 =', sp.sstr(p0), 'q0 =', sp.sstr(q0), 'indicial =', sp.sstr(indicial))
inf_q_limit = sp.limit(q, x, sp.oo)
print('limit_c_over_a_at_infinity =', sp.sstr(inf_q_limit))
print('infinity_exponential_rates_from_lambda_squared_plus_limit =', [sp.sstr(v) for v in sp.solve(sp.Symbol('lam')**2 + inf_q_limit, sp.Symbol('lam'))])
# high precision check of q(x) -> -1/3 at large x
for s in [mp.mpf('1e3'), mp.mpf('1e5'), mp.mpf('1e7')]:
    val = -(s*s)/(3*s*s+s+1)
    print('q_large_x', mp.nstr(s, 10), mp.nstr(val, 50), 'residual_to_-1/3', mp.nstr(abs(val + mp.mpf(1)/3), 50))
