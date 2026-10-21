"""
Corroboration found at CT-S19 adjudication: the bracket missing its `t` in b(z)
is printed WITH the `t` in B_1's (1,2) entry, on the SAME page (journal 2655).

Tests the structural relation  b(z) first term  ==  z * B1[0,1]
and confirms which reading of b(z) makes it hold.
"""
import sympy as sp

z, p, q, t, th0, th1, thi = sp.symbols('z p q t theta0 theta1 theta_infinity')
out = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


# --- read off the page image: B_1 entry (1,2), which PRINTS the t
B1_12 = -((p + sp.Rational(1, 2) * (q - 1) * q * t)**2
          - th1**2 / 4
          + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4)) / q


def b_first_term(square_has_t):
    s = p + sp.Rational(1, 2) * (q - 1) * q * (t if square_has_t else 1)
    return -z * (s**2 - th1**2 / 4
                 + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4)) / q


say('=' * 74)
say('Is  b(z) first term  ==  z * B1[0,1] ?')
say('=' * 74)

results = {}
for name, has_t in (('printed  (no t)', False), ('corrected (with t)', True)):
    d = sp.simplify(sp.cancel(sp.together(b_first_term(has_t) - z * B1_12)))
    results[name] = d
    say(f'  {name:22s}  b_first - z*B1[0,1] = {d}')

assert results['corrected (with t)'] == 0, 'corrected reading does NOT match B1'
assert results['printed  (no t)'] != 0, 'printed reading unexpectedly matches B1'

say('')
say('  => With the t, b(z) first term is EXACTLY z * B1[0,1].')
say('     Without it, the identity fails.')
say('')
say('  difference between the two readings, factorised:')
say('   ', sp.factor(sp.cancel(b_first_term(True) - b_first_term(False))))

# ---- control that can fail: a bogus variant must be rejected
say('')
say('CONTROL  a bogus variant must be rejected by the same test')
U = sp.symbols('U')
for bogus, lab in ((t**2, 't^2'), (t + 1, 't+1'), (sp.Integer(2) * t, '2t')):
    s = p + sp.Rational(1, 2) * (q - 1) * q * bogus
    bb = -z * (s**2 - th1**2 / 4
               + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4)) / q
    d = sp.simplify(sp.cancel(sp.together(bb - z * B1_12)))
    say(f'  variant {lab:5s} -> difference {"ZERO (BAD)" if d == 0 else "nonzero, rejected"}')
    assert d != 0, f'control failed: bogus variant {lab} accepted'

say('')
say('  Control fires on all three bogus variants, so the test discriminates.')
say('=' * 74)
say('CONCLUSION: the omission in b(z) is a transcription slip of an expression')
say('the authors print CORRECTLY, with the t, elsewhere on the same page.')

with open('outputs/b1_corroboration.out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
