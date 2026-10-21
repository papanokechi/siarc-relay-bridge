"""
CT-S18 adjudication: does the cold read's ERROR verdict refute C3?

CT-S17 computed  P = D'/D - b'/b   (eliminate y2; scalar ODE for y1)
CT-S18 computed  P = D'/D - c'/c   (eliminate y1; scalar ODE for y2)

Both are correct reductions OF THE SAME SYSTEM to a scalar equation; they are
the equations satisfied by the two different components of the solution vector.
This script derives both from scratch, shows which one System C is, and tests
the derivation with a control that CAN fail.
"""
import sympy as sp

I = sp.I
z = sp.symbols('z')
out = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


# ===================================================================== PART A
# Generic derivation of both scalar reductions.  Nothing numeric, nothing
# assumed: the two ODEs are derived from the system by elimination.
say('=' * 74)
say('PART A  generic elimination, from scratch (no formula assumed)')

n11, n12, n21, n22 = [sp.Function(f'n{k}')(z) for k in ('11', '12', '21', '22')]
y1, y2 = sp.Function('y1')(z), sp.Function('y2')(z)

sys1 = sp.Eq(sp.diff(y1, z), n11 * y1 + n12 * y2)
sys2 = sp.Eq(sp.diff(y2, z), n21 * y1 + n22 * y2)

# route 1: solve sys1 for y2, substitute into sys2  ->  ODE for y1
y2_of_y1 = sp.solve(sys1, y2)[0]
ode1 = sp.expand(sp.diff(y2_of_y1, z) - (n21 * y1 + n22 * y2_of_y1))
ode1 = sp.collect(sp.expand(ode1 * n12), [sp.diff(y1, z, 2), sp.diff(y1, z), y1])
A2 = ode1.coeff(sp.diff(y1, z, 2))
P1 = sp.simplify(ode1.coeff(sp.diff(y1, z)) / A2)
Q1 = sp.simplify(sp.expand(ode1 - A2 * sp.diff(y1, z, 2)
                           - A2 * P1 * sp.diff(y1, z)).coeff(y1) / A2)
say('  route 1 (ODE for y1):  P =', sp.simplify(P1))

# route 2: by the symmetry 1<->2 of the system
P2 = P1.subs({n11: n22, n22: n11, n12: n21, n21: n12}, simultaneous=True)
say('  route 2 (ODE for y2):  P =', sp.simplify(P2))

say('  -> the two routes differ by  n21\'/n21 - n12\'/n12, i.e. by d/dz log(c/b).')
say('     They are NOT the same scalar equation and are not meant to be.')

# ===================================================================== PART B
say('=' * 74)
say('PART B  the located point: which route is System C?')

s_p = (-1 + I * sp.sqrt(11)) / 6
delta = -I * sp.sqrt(11) / 3
x_of_z = s_p + delta * z
D = z * (z - 1)

P_C = sp.cancel(sp.expand(delta * (6 * x_of_z + 1) / (3 * x_of_z**2 + x_of_z + 1)))
Q_C = sp.cancel(sp.expand(delta**2 * (-x_of_z**2) / (3 * x_of_z**2 + x_of_z + 1)))

p0 = 5 * I * (-28151758571 * sp.sqrt(33) + 48874838016 * sp.sqrt(11)) / 4086468672
q0 = sp.Rational(1, 2) + (-457937 * sp.sqrt(11) * I + 281700 * sp.sqrt(33) * I) / 122408
t0 = -2 * sp.sqrt(33) * I / 9
ti0 = -2 - sp.sqrt(3) / 9


def entries(p, q, t, thi, th0=0, th1=0):
    a = (p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q)
         - sp.Rational(1, 2) * t * (z - q)**2)
    b = (-(z * ((p + sp.Rational(1, 2) * (q - 1) * q * t)**2 - th1**2 / 4
                + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
         - ((q - 1) * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
            * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)
    c = -(z - q) / (q - 1)
    return (sp.cancel(sp.expand(a)), sp.cancel(sp.expand(b)), sp.cancel(sp.expand(c)))


a_F, b_F, c_F = entries(p0, q0, t0, ti0)

# N = -A/D, the convention both prior sessions used (vdPS write z d/dz + A)
N11, N12, N21, N22 = -a_F / D, -b_F / D, -c_F / D, a_F / D
sub = {n11: N11, n12: N12, n21: N21, n22: N22}


def instantiate(expr):
    e = expr
    for f, g in sub.items():
        e = e.subs(sp.Derivative(f, z), sp.diff(g, z)).subs(f, g)
    return sp.cancel(sp.radsimp(sp.simplify(e)))


P1v, Q1v = instantiate(P1), instantiate(Q1)
P2v = instantiate(P2)

say('  b(z) constant?  db/dz =', sp.simplify(sp.diff(b_F, z)))
say('  q0 in {0,1}?   ', sp.simplify(q0) == 0 or sp.simplify(q0) == 1)

d1P = sp.cancel(sp.simplify(sp.expand(P1v - P_C)))
d1Q = sp.cancel(sp.simplify(sp.expand(sp.radsimp(Q1v - Q_C))))
d2P = sp.cancel(sp.simplify(sp.expand(P2v - P_C)))

say('  route 1  P - P_C =', d1P)
say('  route 1  Q - Q_C =', d1Q)
say('  route 2  P - P_C =', sp.factor(d2P))
say('  route 2 predicted mismatch  -c\'/c = ', sp.factor(sp.cancel(-sp.diff(c_F, z) / c_F)))

assert d1P == 0 and d1Q == 0, 'route 1 does NOT reproduce System C'
assert d2P != 0, 'route 2 unexpectedly matches'
assert sp.simplify(d2P + sp.diff(c_F, z) / c_F) == 0, 'route-2 mismatch is not c-route'
say('  => System C IS route 1 exactly; route 2 misses it by exactly -c\'/c.')

# ===================================================================== PART C
# CONTROL THAT CAN FAIL.  Solve the SYSTEM at an ordinary point and test which
# scalar ODE its first component actually satisfies.
say('=' * 74)
say('PART C  control: solve the system, test both ODEs on its y1 component')

Q2v = instantiate(Q1.subs({n11: n22, n22: n11, n12: n21, n21: n12},
                          simultaneous=True))

z0 = sp.Rational(3, 10) + sp.Rational(1, 7) * I
dps = 60


def resid(Pex, Qex, v1, v2):
    """y1'' + P y1' + Q y1, with y1', y1'' taken FROM THE SYSTEM."""
    d = {z: z0}
    f11, f12, f21, f22 = [sp.N(e.subs(d), dps) for e in (N11, N12, N21, N22)]
    g11, g12, g21, g22 = [sp.N(sp.diff(e, z).subs(d), dps)
                          for e in (N11, N12, N21, N22)]
    y1p = f11 * v1 + f12 * v2
    y2p = f21 * v1 + f22 * v2
    y1pp = g11 * v1 + f11 * y1p + g12 * v2 + f12 * y2p
    return sp.N(y1pp + sp.N(Pex.subs(d), dps) * y1p + sp.N(Qex.subs(d), dps) * v1, dps)


for (v1, v2) in ((sp.Integer(1), sp.Integer(0)), (sp.Rational(2, 5), sp.Rational(-3, 4) + I)):
    r1 = abs(complex(resid(P1v, Q1v, v1, v2)))
    r2 = abs(complex(resid(P2v, Q2v, v1, v2)))
    say(f'  initial (y1,y2)=({v1},{v2}):  |route-1 residual| = {r1:.3e}   '
        f'|route-2 residual| = {r2:.3e}')
    assert r1 < 1e-40, 'route 1 failed its own system'
    assert r2 > 1e-6, 'route 2 control did not fire'

say('  The control fires on both seeds: y1 of the system satisfies route 1 and')
say('  NOT route 2, so the test is capable of distinguishing them.')

# ===================================================================== PART D
say('=' * 74)
say('PART D  CT-S18 method notes')
say('  (i)  CT-S18 asserted  simplify(Pfam - Pfam) == 0  as its "P control".')
say('       That expression is identically zero for ANY Pfam, so the control')
say('       cannot fail and certifies nothing.')
say('  (ii) CT-S18 evaluated its mismatch at a GENERIC sample')
say('       (q=2/3, p=1/5, t=7/11) and never at the located point. Since the')
say('       route-2 mismatch is -1/(z-q), which has no zero in z, no choice of')
say('       point could ever have made route 2 match. The test was therefore')
say('       insensitive to the very thing it was meant to decide.')
say('=' * 74)
say('CONCLUSION: CT-S18 tasks 1 and 2 stand. Task 3 computation is correct but')
say('answers a different question; its inference, and the ERROR verdict resting')
say('on it, are REJECTED.')

with open('outputs/adjudicate.out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
