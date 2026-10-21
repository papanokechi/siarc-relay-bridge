"""
Adjudication of CT-S19-COLDREAD-MEMBERSHIP.

CT-S19 derived its own point of U_0 without sight of CT-S16/S17.  It landed on
the OPPOSITE branch to CT-S17 (t -> -t, sqrt(33) -> -sqrt(33), sqrt(3) -> -sqrt(3)).
This re-verifies CT-S19's point in independent code, and checks that the two
branches are genuinely the two signs of the companion's  t = -+ 2 i sqrt(33)/9.
"""
import sympy as sp

I = sp.I
z = sp.symbols('z')
out = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


# ---- System C, normalised exactly as CT-S19 describes: x = alpha + (beta-alpha) z
alpha = (-1 + sp.sqrt(-11)) / 6
beta = (-1 - sp.sqrt(-11)) / 6
x_of_z = alpha + (beta - alpha) * z
delta = sp.simplify(beta - alpha)
D = z * (z - 1)

P_C = sp.cancel(sp.expand(delta * (6 * x_of_z + 1) / (3 * x_of_z**2 + x_of_z + 1)))
Q_C = sp.cancel(sp.expand(delta**2 * (-x_of_z**2) / (3 * x_of_z**2 + x_of_z + 1)))
say('affine map delta = beta - alpha =', sp.simplify(delta))
say('P_C =', sp.simplify(P_C))


def first_component_PQ(p, q, t, thi, th0=0, th1=0):
    """P_1 = D'/D - b'/b  and the matching Q_1, with the CORRECTED b(z)."""
    a = (p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q)
         - sp.Rational(1, 2) * t * (z - q)**2)
    b = (-(z * ((p + sp.Rational(1, 2) * (q - 1) * q * t)**2 - th1**2 / 4
                + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
         - ((q - 1) * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
            * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)
    c = -(z - q) / (q - 1)
    a, b, c = (sp.cancel(sp.expand(e)) for e in (a, b, c))
    P = sp.cancel(sp.diff(D, z) / D - sp.diff(b, z) / b)
    Q = sp.cancel(sp.diff(a, z) / D - a * sp.diff(b, z) / (D * b) - (a**2 + b * c) / D**2)
    return sp.cancel(sp.radsimp(P)), sp.cancel(sp.radsimp(Q)), b


# ---- CT-S19's point, transcribed from its FINDINGS-1-4.md
t19 = 2 * sp.sqrt(33) * I / 9
ti19 = -2 + sp.sqrt(3) / 9
q19 = (sp.Rational(1, 2)
       - 70425 * sp.sqrt(33) * I / 30602
       - 457937 * sp.sqrt(11) * I / 122408)
p19 = (5 * (156636384689044 * sp.sqrt(33) + 271939598721024 * sp.sqrt(11)
            + 46172647864885092 * I + 26659773733835227 * sp.sqrt(3) * I)
       / (371497152 * (457937 * sp.sqrt(11) + 281700 * sp.sqrt(33) - 61204 * I)))

# ---- CT-S17's point, the other branch
t17 = -2 * sp.sqrt(33) * I / 9
ti17 = -2 - sp.sqrt(3) / 9
q17 = sp.Rational(1, 2) + (-457937 * sp.sqrt(11) * I + 281700 * sp.sqrt(33) * I) / 122408
p17 = 5 * I * (-28151758571 * sp.sqrt(33) + 48874838016 * sp.sqrt(11)) / 4086468672

say('=' * 74)
for lab, (p0, q0, t0, ti0) in (('CT-S19 point', (p19, q19, t19, ti19)),
                               ('CT-S17 point', (p17, q17, t17, ti17))):
    P, Q, b = first_component_PQ(p0, q0, t0, ti0)
    dP = sp.cancel(sp.simplify(sp.expand(P - P_C)))
    dQ = sp.cancel(sp.simplify(sp.expand(sp.radsimp(Q - Q_C))))
    say(f'{lab}:')
    say('   db/dz =', sp.simplify(sp.diff(b, z)))
    say('   q in {0,1}? ', sp.simplify(q0) == 0 or sp.simplify(q0) == 1)
    say('   P - P_C =', dP)
    say('   Q - Q_C =', dQ)
    say('   t^2 =', sp.simplify(t0**2), ' (companion: -44/27 =', sp.nsimplify(-sp.Rational(44, 27)), ')')
    assert dP == 0 and dQ == 0, f'{lab} does NOT reproduce System C'
    say(f'   -> {lab} reproduces System C exactly.')

say('=' * 74)
say('branch relation between the two independently derived points:')
say('   t19 + t17 =', sp.simplify(t19 + t17), '   (so t19 = -t17)')
say('   both satisfy t^2 = -44/27:', sp.simplify(t19**2 + sp.Rational(44, 27)) == 0,
    sp.simplify(t17**2 + sp.Rational(44, 27)) == 0)
say('   q19 - conj-in-sqrt33 of q17 =',
    sp.simplify(q19 - q17.subs(sp.sqrt(33), -sp.sqrt(33))))
say('   ti19 - ti17 flipped in sqrt(3) =',
    sp.simplify(ti19 - ti17.subs(sp.sqrt(3), -sp.sqrt(3))))

# ---- control that can fail
say('=' * 74)
say('CONTROL  perturbed points must be rejected')
fired = 0
for name, pt in (('q nudged', (p19, q19 + sp.Rational(1, 1000), t19, ti19)),
                 ('p nudged', (p19 + sp.Rational(1, 1000), q19, t19, ti19)),
                 ('t sign only', (p19, q19, t17, ti19))):
    P, Q, _ = first_component_PQ(*pt)
    d = sp.simplify(sp.cancel(sp.expand(P - P_C))) == 0 and \
        sp.simplify(sp.cancel(sp.expand(sp.radsimp(Q - Q_C)))) == 0
    say(f'   {name:12s} -> matches System C? {d}')
    assert not d, f'control failed: {name} still matched'
    fired += 1
say(f'   control fired on {fired}/3 perturbations.')

say('=' * 74)
say('CONCLUSION: CT-S19 independently derived a VALID point of U_0 on the')
say('OPPOSITE branch to CT-S17. Both reproduce System C exactly. The two')
say('branches are the two signs of the companion\'s t = -+ 2 i sqrt(33)/9,')
say('so two isolated sessions between them exhibited both.')

with open('outputs/adjudicate_s19.out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
