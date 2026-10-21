import sympy as sp

z, x, rho = sp.symbols('z x rho')
r = (11*z**4 + 4*z**2 + 4*z + 12)/(4*z**4*(z**2 + z + 3)**2)
q = z**2 + z + 3


def pole_order_and_lead(expr, var, point, max_n=12):
    for n in range(max_n + 1):
        val = sp.simplify(sp.limit((var - point)**n * expr, var, point))
        if val not in (sp.oo, -sp.oo, sp.zoo) and not val.has(sp.oo, -sp.oo, sp.zoo):
            return n, sp.simplify(val)
    raise RuntimeError('pole order not found')

print('Object B normal form y\'\' = r(z)y')
print('r(z) =', sp.factor(r))
print()
print('Finite poles from denominator z^4*(z^2+z+3)^2:')
roots = [sp.Integer(0)] + sp.solve(q, z)
for p in roots:
    n, lead = pole_order_and_lead(r, z, p)
    print('point z =', p)
    print('  pole_order_of_r =', n)
    print('  leading_coefficient =', lead)
    if n == 2:
        exps = [sp.simplify(s) for s in sp.solve(sp.Eq(rho*(rho-1), lead), rho)]
        print('  regular_singular_exponents =', exps)
        print('  exponent_difference =', sp.simplify(max(exps) - min(exps)) if len(exps) == 2 else 0)
        print('  Newton_polygon_connection_slopes = [0, 0]')
        print('  ramification = 1')
        print('  Katz_invariant = 0')
    elif n == 4:
        am2, am1, a0, a1 = sp.symbols('am2 am1 a0 a1')
        s = am2*z**-2 + am1*z**-1 + a0 + a1*z
        expr = sp.series(s**2 - r, z, 0, 1).removeO().expand()
        for branch in [sp.sqrt(3)/3, -sp.sqrt(3)/3]:
            eqs = [sp.Eq(sp.expand(expr.subs({am2: branch})).coeff(z, k), 0) for k in [-3, -2, -1]]
            sol = sp.solve(eqs, [am1, a0, a1], dict=True)[0]
            log_exp = sp.simplify(sol[am1])
            exp_part = sp.simplify(-branch/z)
            print('  sqrt_branch_leading =', branch)
            print('    sqrt_branch_z^-1_coefficient =', log_exp)
            print('    exponential_factor = exp(', exp_part, ') * z^(', log_exp, ')')
        print('  Newton_polygon_connection_slopes = [1, 1]')
        print('  ramification = 1')
        print('  Katz_invariant = 1')
    print()

Rinf = sp.simplify(r.subs(z, 1/x)/x**4)
print('At z = infinity, x = 1/z and the trace-free normal form is u\'\' = R_inf(x)u')
print('R_inf(x) =', sp.factor(Rinf))
print('R_inf(0) =', sp.simplify(Rinf.subs(x, 0)))
print('  ordinary_point = True')
print('  ordinary_exponents = [0, 1]')
print('  Newton_polygon_connection_slopes = [0, 0]')
print('  ramification = 1')
print('  Katz_invariant = 0')
print()
print("Authors' Katz-invariant notation after moving the three singular points to {0,1,infinity}:")
print('  (0,0,1)')
