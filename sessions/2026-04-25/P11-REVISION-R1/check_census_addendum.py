"""Self-contained checks for the F(2,4) KNOWN-ISSUES addendum (items 1, 2, 3, 5, 8, and the Alg(0) counterexamples).

Needs only Python 3 and mpmath. Uses the paper's convention:
    K = b(0) + a(1)/(b(1) + a(2)/(b(2) + ...)),  a(n) = a0 + a1 n + a2 n^2,  b(n) = b0 + b1 n + b2 n^2,
    all six coefficients in {-4,...,4}.
Items 4 (convergent count) and 6 (Trans count) need the full census and are not checked here.
Exit code 0 iff every check passes.
"""
import itertools
import sys

from mpmath import mp, mpf, pi, sqrt

R = range(-4, 5)
A = list(itertools.product(R, repeat=3))          # (a0, a1, a2)
fails = 0


def check(name, ok, detail):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)
    fails += 0 if ok else 1


def pos_roots(a):
    # any positive integer root k satisfies |k| <= 4 when a != 0 (k | a0, or k = -a1/a2 if a0 = 0); scan generously
    return [k for k in range(1, 1000) if a[0] + a[1] * k + a[2] * k * k == 0]


def limit(a, b, N):
    pa = lambda n: a[0] + a[1] * n + a[2] * n * n
    pb = lambda n: b[0] + b[1] * n + b[2] * n * n
    P0, P1, Q0, Q1 = 1, pb(0), 0, 1
    for n in range(1, N + 1):
        P0, P1 = P1, pb(n) * P1 + pa(n) * P0
        Q0, Q1 = Q1, pb(n) * Q1 + pa(n) * Q0
    return mpf(P1) / Q1


# Item 1: trivial-zero count (paper: 729)
t1 = sum(1 for a in A if sum(a) == 0)
check("item 1, a(1)=0 families", t1 * 729 == 44469, "%d a-triples x 729 = %d (paper states 729)" % (t1, t1 * 729))

# Item 2: termination ceiling (paper: 112,540 terminations at k >= 2; 1,971 at k in 21..100)
nz = [a for a in A if a != (0, 0, 0)]
roots = {a: pos_roots(a) for a in nz}
kmax = max(max(r) for r in roots.values() if r)
k1 = sum(1 for r in roots.values() if r)
k2 = sum(1 for r in roots.values() if any(k >= 2 for k in r))
check("item 2, largest positive integer root", kmax == 4, "max k = %d, so no termination at k in 21..100" % kmax)
check("item 2, families terminating at some k>=1", k1 * 729 == 67068, "%d triples x 729 = %d (+729 with a = 0)" % (k1, k1 * 729))
check("item 2, families terminating at some k>=2", k2 * 729 == 26244, "%d triples x 729 = %d (paper states 112,540)" % (k2, k2 * 729))

# Item 3: the -2/9 law; the 4/pi family a(n) = n^2, b(n) = 2n+1 has a2/b1^2 = 1/4
mp.dps = 60
L = limit((0, 0, 1), (1, 2, 0), 3000)
check("item 3, a=n^2, b=2n+1 gives 4/pi", abs(L - 4 / pi) < mpf(10) ** -50, "|K - 4/pi| = %s; a2/b1^2 = 1/4, not -2/9" % mp.nstr(abs(L - 4 / pi), 3))

# Alg(0) counterexamples: golden ratio
phi = (1 + sqrt(5)) / 2
for a, b in [((1, 0, 0), (1, 0, 0)), ((-1, 0, 4), (1, 2, 0))]:
    x, y = limit(a, b, 1500), limit(a, b, 3000)
    check("Alg(0) counterexample a=%s b=%s" % (a, b), abs(x - phi) < mpf(10) ** -50 and abs(x - y) < mpf(10) ** -50,
          "|K - phi| = %s at two depths" % mp.nstr(abs(y - phi), 3))

# Item 5: arithmetic
check("item 5, 729 + 112,540", 729 + 112540 == 113269, "= %d (paper: 113,270)" % (729 + 112540))
check("item 5, 513,387 - 113,270", 513387 - 113270 == 400117, "= %d (paper: 400,119)" % (513387 - 113270))

# Item 8: F(3,4) has 4 coefficients per polynomial
check("item 8, size of F(3,4)", 9 ** 8 == 43046721, "9^8 = %d (paper: 9^6 = 531,441)" % 9 ** 8)

print("ALL PASS" if fails == 0 else "%d FAIL" % fails)
sys.exit(1 if fails else 0)
