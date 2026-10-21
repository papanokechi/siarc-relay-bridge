"""TASK 2: b-route and c-route at the point of SS3, compared with System C.
Exact test: cancel(difference, z, extension=True) over Q(I,sqrt3,sqrt11)
-- radicals are never compared with ==.  Plus a numeric check at dps 40.
"""
import os
from sympy import *

z = symbols('z')
s3, s11 = sqrt(3), sqrt(11)
s33 = s3 * s11


def exact_zero(d):
    return cancel(d, z, extension=True)


def num_max(d, dps=40):
    vals = []
    for zz in [Rational(1, 3) + Rational(1, 7) * I, Rational(-2, 5),
               Rational(7, 4) + Rational(2, 9) * I, Rational(3, 11) * I]:
        vals.append(N(Abs(N(d.subs(z, zz), dps)), 6))
    return max(vals, key=lambda v: float(v))


# ---- the point (SS3) -------------------------------------------------------
p = 5 * I * (-28151758571 * s33 + 48874838016 * s11) / 4086468672
q = Rational(1, 2) + (-457937 * s11 * I + 281700 * s33 * I) / 122408
t = -2 * s33 * I / 9
thi = -2 - s3 / 9
th0 = Integer(0)
th1 = Integer(0)

# ---- the system (SS1) ------------------------------------------------------
D = z * (z - 1)
a = p + Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) - Rational(1, 2) * t * (z - q)**2
b = (-(z * ((p + Rational(1, 2) * (q - 1) * q * t)**2 - th1**2 / 4
            + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
     - ((q - 1) * (p + Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
        * (p + Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)
c = -(z - q) / (q - 1)
n11, n12, n21, n22 = -a / D, -b / D, -c / D, a / D

# reductions, as derived in task 1
P_b = -n11 - n22 - diff(n12, z) / n12
Q_b = n11 * n22 + n11 * diff(n12, z) / n12 - n12 * n21 - diff(n11, z)
P_c = -n11 - n22 - diff(n21, z) / n21
Q_c = n11 * n22 + n22 * diff(n21, z) / n21 - n12 * n21 - diff(n22, z)

# ---- System C (SS2) --------------------------------------------------------
delta = -I * s11 / 3
x = (-1 + I * s11) / 6 + delta * z
P_C = delta * (6 * x + 1) / (3 * x**2 + x + 1)
Q_C = delta**2 * (-x**2) / (3 * x**2 + x + 1)

rows = [('P_b - P_C', P_b - P_C), ('Q_b - Q_C', Q_b - Q_C),
        ('P_c - P_C', P_c - P_C), ('Q_c - Q_C', Q_c - Q_C),
        ('(P_b - P_c) - d/dz log(c/b)', (P_b - P_c) - diff(log(c / b), z))]

L = ["# TASK 2 - b-route and c-route at the point of SS3 vs System C", "",
     "Exact test: cancel(difference, z, extension=True) over Q(i,sqrt3,sqrt11).",
     "Numeric: max |difference| at z = 1/3+i/7, -2/5, 7/4+2i/9, 3i/11, dps 40.", ""]
for name, d in rows:
    e = exact_zero(d)
    L += ["## %s" % name,
          "    exact cancel(...) = %s   -> zero: %s" % (e, e == 0),
          "    numeric max |.| at dps 40 = %s" % num_max(d), ""]

# ---- CONTROLS THAT CAN FAIL ------------------------------------------------
sep = exact_zero(P_b - P_c)
control_separates = (sep != 0)
bad = exact_zero(P_b.subs(q, q + 1) - P_C)
control_discriminates = (bad != 0)
L += ["## Controls that can fail", "",
      "    control_separates: fires (PASS=False) if P_b - P_c vanished at this",
      "      point, which would make the b/c distinction vacuous here.",
      "      P_b - P_c = %s" % sep,
      "      PASS = %s" % control_separates,
      "      numeric max |P_b - P_c| at dps 40 = %s" % num_max(P_b - P_c),
      "",
      "    control_discriminates: fires (PASS=False) if the same exact test also",
      "      accepted a deliberately wrong point (q -> q+1), i.e. if it were",
      "      rubber-stamping anything put in front of it.",
      "      PASS = %s" % control_discriminates,
      "      cancel(P_b[q+1] - P_C) = %s" % bad, ""]

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'outputs', 'task2.md')
with open(out, 'w', encoding='utf-8') as f:
    f.write("\n".join(L) + "\n")
with open(out, encoding='utf-8') as f:
    back = f.read()
assert 'P_b - P_C' in back and 'control_discriminates' in back, 'WRITE-BACK FAILED'
print(back)
print('READBACK OK', out, len(back))
