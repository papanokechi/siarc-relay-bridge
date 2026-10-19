"""Self-contained checks for addendum 2 to the F(2,4) KNOWN-ISSUES notice (items 1 and 3).

Needs only Python 3 and mpmath. Uses the paper's convention:
    K = b(0) + a(1)/(b(1) + a(2)/(b(2) + ...)),  a(n) = a0 + a1 n + a2 n^2,  b(n) = b0 + b1 n + b2 n^2.
The checks use direct convergents K_N. In every case below the error of K_N falls like a power of N
(about N^-4 for item 1, about N^-sqrt(D) for item 3), so the depths 10^4 and 10^5 are chosen to give
at least 15 digits for item 1 and at least 12 digits for item 3. The digits are agreement between a
convergent and a closed form, not a proof; the identities themselves are numerical.
Exit code 0 iff every check passes.
"""
import sys

from mpmath import mp, mpf, pi, sqrt, nstr, floor

mp.dps = 50
DEPTHS = (10 ** 4, 10 ** 5)
fails = 0


def check(name, ok, detail):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)
    fails += 0 if ok else 1


def convergents(a, b, depths):
    """K_N for each N in depths; forward recurrence, rescaled by Q each step so the numbers stay O(1)."""
    pa = lambda n: a[0] + a[1] * n + a[2] * n * n
    pb = lambda n: b[0] + b[1] * n + b[2] * n * n
    P0, P1, Q0, Q1 = mpf(1), mpf(pb(0)), mpf(0), mpf(1)
    out = {}
    for n in range(1, max(depths) + 1):
        an, bn = pa(n), pb(n)
        P0, P1 = P1, bn * P1 + an * P0
        Q0, Q1 = Q1, bn * Q1 + an * Q0
        P0, P1, Q0, Q1 = P0 / Q1, P1 / Q1, Q0 / Q1, mpf(1)
        if n in depths:
            out[n] = P1
    return out


def digits(err):
    return -float(mp.log10(err)) if err > 0 else float("inf")


# Item 1: a(n) = n^2, b(n) = +-4 has limit +-6/(3 pi - 8)
L = 6 / (3 * pi - 8)
for sign in (1, -1):
    K = convergents((0, 0, 1), (4 * sign, 0, 0), DEPTHS)
    target = sign * L
    e4, e5 = abs(K[DEPTHS[0]] - target), abs(K[DEPTHS[1]] - target)
    check("item 1, A[0,0,1]B[%d,0,0] -> %s6/(3pi-8)" % (4 * sign, "+" if sign > 0 else "-"),
          digits(e5) >= 15 and e5 < e4,
          "agreement %.1f digits at N=%d, %.1f digits at N=%d; limit %s"
          % (digits(e4), DEPTHS[0], digits(e5), DEPTHS[1], nstr(K[DEPTHS[1]], 15)))

# Item 3: one family of each subgroup D in the list of 40 (a2 = -1, b2 = 0, |b1| = 2).
# Closed form: L = s (m - 1 + sqrt(D)) / 2 with s = sign(b1), m = s b0, D = (1 + m)^2 + 4 (a0 + a1 - 1), D not a square.
REPS = [
    ((-1, 4, -1), (-3, 2, 0), 12),
    ((1, -3, -1), (-4, -2, 0), 13),
    ((2, -3, -1), (-4, -2, 0), 17),
    ((1, 4, -1), (-3, 2, 0), 20),
    ((3, -3, -1), (-4, -2, 0), 21),
    ((2, 4, -1), (-3, 2, 0), 24),
    ((3, 4, -1), (-3, 2, 0), 28),
    ((4, 4, -1), (-3, 2, 0), 32),
]
for a, b, Dexp in REPS:
    s = 1 if b[1] > 0 else -1
    m = s * b[0]
    D = (1 + m) ** 2 + 4 * (a[0] + a[1] - 1)
    root = int(floor(sqrt(D)))
    shape = a[2] == -1 and b[2] == 0 and abs(b[1]) == 2 and D == Dexp and root * root != D
    target = s * (m - 1 + sqrt(D)) / 2
    K = convergents(a, b, DEPTHS)
    e4, e5 = abs(K[DEPTHS[0]] - target), abs(K[DEPTHS[1]] - target)
    check("item 3, A%s B%s, D=%d" % (list(a), list(b), D),
          shape and digits(e5) >= 12 and e5 < e4,
          "agreement %.1f digits at N=%d, %.1f digits at N=%d; limit %s"
          % (digits(e4), DEPTHS[0], digits(e5), DEPTHS[1], nstr(target, 15)))

# Examples quoted in the text
K = convergents((-1, 4, -1), (-3, 2, 0), DEPTHS)[DEPTHS[1]]
check("item 3, example A[-1,4,-1]B[-3,2,0] = -2 + sqrt(3)", abs(K - (-2 + sqrt(3))) < mpf(10) ** -12,
      "|K - (-2 + sqrt3)| = %s at N=%d" % (nstr(abs(K - (-2 + sqrt(3))), 3), DEPTHS[1]))
K = convergents((1, -3, -1), (-4, -2, 0), DEPTHS)[DEPTHS[1]]
check("notice example a(n) = -n^2-3n+1, b(n) = -2n-4 -> -(3+sqrt13)/2",
      abs(K + (3 + sqrt(13)) / 2) < mpf(10) ** -12,
      "|K + (3+sqrt13)/2| = %s at N=%d" % (nstr(abs(K + (3 + sqrt(13)) / 2), 3), DEPTHS[1]))

print("ALL PASS" if fails == 0 else "%d FAIL" % fails)
sys.exit(1 if fails else 0)
