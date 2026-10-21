"""TASK 1: how do the b-route and c-route scalar reductions differ?

Derived from the system itself, assuming no formula: eliminate one component
and read off P.
"""
import os
from sympy import *

z = symbols('z')
n11, n12, n21, n22 = [Function(s)(z) for s in ('n11', 'n12', 'n21', 'n22')]
y1, y2 = Function('y1')(z), Function('y2')(z)


def reduce_route(u, v, m_uu, m_uv, m_vu, m_vv):
    """Eliminate v from  u' = m_uu u + m_uv v,  v' = m_vu u + m_vv v.
    Returns (P, Q) with u'' + P u' + Q u = 0."""
    v_of_u = (Derivative(u, z) - m_uu * u) / m_uv
    resid = expand(simplify((diff(v_of_u, z) - (m_vu * u + m_vv * v_of_u)) * m_uv))
    lead = resid.coeff(Derivative(u, z, 2))
    P = simplify(resid.coeff(Derivative(u, z), 1) / lead)
    Q = simplify(resid.coeff(u, 1).coeff(Derivative(u, z), 0) / lead)
    return simplify(P), simplify(Q)


# b-route: scalar equation for y1 (eliminate y2)
P_b, Q_b = reduce_route(y1, y2, n11, n12, n21, n22)
# c-route: scalar equation for y2 (eliminate y1) -- same elimination with the
# roles of the two components swapped
P_c, Q_c = reduce_route(y2, y1, n22, n21, n12, n11)

diff_P = simplify(P_b - P_c)
claimed = simplify(diff(log(n21 / n12), z))
match_generic = simplify(diff_P - claimed) == 0

# under the convention of SS1
a, b, c, D = [Function(s)(z) for s in ('a', 'b', 'c', 'D')]
sub = {n11: -a / D, n12: -b / D, n21: -c / D, n22: a / D}
diff_P_conv = simplify(diff_P.subs(sub).doit())
match_conv = simplify(diff_P_conv - simplify(diff(log(c / b), z))) == 0

# CONTROLS THAT CAN FAIL
control_nonzero = simplify(diff_P) != 0
control_shared = simplify((P_b + diff(n12, z) / n12) - (P_c + diff(n21, z) / n21)) == 0

lines = [
    "# TASK 1 - difference between the b-route and c-route reductions",
    "",
    "Derived by elimination from y' = N y with generic entries n11,n12,n21,n22.",
    "No formula assumed; the c-route is the same elimination with the two",
    "components swapped.",
    "",
    "## b-route (eliminate y2; scalar equation for y1)",
    "",
    "    P_b = %s" % P_b,
    "    Q_b = %s" % Q_b,
    "",
    "## c-route (eliminate y1; scalar equation for y2)",
    "",
    "    P_c = %s" % P_c,
    "    Q_c = %s" % Q_c,
    "",
    "## Difference, closed form",
    "",
    "    P_b - P_c = %s" % diff_P,
    "              = d/dz log(n21/n12)",
    "    simplify(P_b - P_c - d/dz log(n21/n12)) == 0 : %s" % match_generic,
    "",
    "Under SS1 (n12 = -b/D, n21 = -c/D) the 1/D cancels in the ratio:",
    "",
    "    P_b - P_c = %s = d/dz log(c/b)" % diff_P_conv,
    "    simplify(check) == 0 : %s" % match_conv,
    "",
    "## Controls that can fail",
    "",
    "    control_nonzero  (fires if P_b-P_c collapsed to 0 identically, which",
    "      would make the b/c distinction invisible): PASS=%s" % control_nonzero,
    "    control_shared   (fires if the two routes differed anywhere outside",
    "      the logarithmic-derivative term): PASS=%s" % control_shared,
]
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'outputs', 'task1.md')
with open(out, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines) + "\n")
with open(out, encoding='utf-8') as f:
    back = f.read()
assert 'd/dz log(n21/n12)' in back and len(back) > 400, 'WRITE-BACK FAILED'
print(back)
print('READBACK OK', out, len(back))
