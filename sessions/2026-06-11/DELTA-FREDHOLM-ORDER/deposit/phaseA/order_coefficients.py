"""
Phase A1/A3 -- coefficient-route entire order of R_infinity(lambda), robust version.

a_n = sum over sparse n-subsets S of {2,3,...} of prod_{i in S} u_i,
u_i = 1/(b(i-1) b(i)), b(k)=A k^2+B k+C.  Computed by the positive (cancellation-free)
recurrence P_m = P_{m-1} + lambda u_m P_{m-2}, P_0=P_1=1, truncated at vertex M.

KEY FIX: a_n^{(M)} -> a_n only polynomially (tail ~ c_n/M^3 because Sum_{j>M} u_j ~ 1/(3M^3)).
So a_n is RICHARDSON-extrapolated in h = 1/M^3 across several M, cross-checked against
the next-lower-level extrapolant.

Order rho = limsup_n n ln n / ln(1/a_n) = 1/(2d).  Estimators -> 2d:
   A_n = L_n / ln(n!),   Q_n = (L_n - L_{n-1})/ln n,   L_n = ln(1/a_n).
Robust extrapolation: least-squares fit L_n = c2 ln(n!) + c1 n + c0 ln n + c_,  c2 -> 2d;
plus quadratic LS of A_n,Q_n in x = 1/ln n.

Majorant/minorant (A3 rigorous bound): a_n <= e_n (coeffs of prod(1+u_i lambda)) and
a_n >= T_n = prod_{k=1}^n u_{2k}; each bound individually has order 1/(2d).
"""
import json, sys, hashlib
from mpmath import mp, mpf, log, factorial, fabs, matrix, lu_solve

mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 220


def make_u(coeffs):
    cc = [mpf(c) for c in coeffs]
    b = lambda k: sum(cc[j] * k ** j for j in range(len(cc)))
    return (lambda i: 1 / (b(i - 1) * b(i))), len(coeffs) - 1


def coeffs_sparse(u, M, nmax):
    P0 = [mpf(0)] * (nmax + 1); P0[0] = mpf(1)
    P1 = [mpf(0)] * (nmax + 1); P1[0] = mpf(1)
    for m in range(2, M + 1):
        um = u(m)
        cur = P1[:]
        for n in range(1, nmax + 1):
            cur[n] = P1[n] + um * P0[n - 1]
        P0, P1 = P1, cur
    return P1


def coeffs_elem(u, M, nmax):
    E = [mpf(0)] * (nmax + 1); E[0] = mpf(1)
    for m in range(2, M + 1):
        um = u(m)
        for n in range(nmax, 0, -1):
            E[n] = E[n] + um * E[n - 1]
    return E


def neville0(hs, ys):
    """Neville extrapolation to h=0."""
    k = len(hs); tab = list(ys)
    for j in range(1, k):
        tab = [(((0 - hs[i + j]) * tab[i] - (0 - hs[i]) * tab[i + 1]) / (hs[i] - hs[i + j]))
               for i in range(k - j)]
    return tab[0]


def richardson_M(u, Ms, nmax):
    seqs = [coeffs_sparse(u, M, nmax) for M in Ms]
    hs = [1 / mpf(M) ** 3 for M in Ms]
    a = [neville0(hs, [seqs[i][n] for i in range(len(Ms))]) for n in range(nmax + 1)]
    a_lo = [neville0(hs[:-1], [seqs[i][n] for i in range(len(Ms) - 1)]) for n in range(nmax + 1)]
    return a, a_lo, seqs[-1]


def ls_fit(X, y):
    m, n = len(X), len(X[0])
    XT_X = [[sum(X[r][i] * X[r][j] for r in range(m)) for j in range(n)] for i in range(n)]
    XT_y = [sum(X[r][i] * y[r] for r in range(m)) for i in range(n)]
    return lu_solve(matrix(XT_X), matrix(XT_y))


def quad_extrap(xs, ys):
    c = ls_fit([[mpf(1), x, x * x] for x in xs], ys)
    return c[0]


def analyze(name, coeffs, Ms, nmax, fit_lo=12):
    u, d = make_u(coeffs)
    a, a_lo, a_raw = richardson_M(u, Ms, nmax)
    e = coeffs_elem(u, max(Ms), nmax)
    T = [mpf(1)] * (nmax + 1)
    for n in range(1, nmax + 1):
        T[n] = T[n - 1] * u(2 * n)

    xcheck = max(float(fabs((a[n] - a_lo[n]) / a[n])) for n in range(2, nmax + 1))
    raw_err = max(float(fabs((a[n] - a_raw[n]) / a[n])) for n in range(2, nmax + 1))

    L = [None] + [log(1 / a[n]) for n in range(1, nmax + 1)]
    bounds_ok = all(a[n] >= T[n] and a[n] <= e[n] * (1 + mpf(10) ** (-mp.dps + 30))
                    for n in range(1, nmax + 1))

    ns = list(range(fit_lo, nmax + 1))
    X = [[log(factorial(n)), mpf(n), log(n), mpf(1)] for n in ns]
    c = ls_fit(X, [L[n] for n in ns])
    twod_direct = c[0]

    xs = [1 / log(n) for n in ns]
    A_seq = [L[n] / log(factorial(n)) for n in ns]
    Q_seq = [(L[n] - L[n - 1]) / log(n) for n in ns]
    twod_A = quad_extrap(xs, A_seq)
    twod_Q = quad_extrap(xs, Q_seq)

    print(f"\n=== {name}: b={coeffs} (d={d}); Ms={Ms}, nmax={nmax}, dps={mp.dps} ===")
    print(f"  raw trunc err (M={max(Ms)})   : {raw_err:.2e}")
    print(f"  Richardson(1/M^3) xcheck      : {xcheck:.2e}")
    print(f"  a_n in [T_n, e_n] all n       : {bounds_ok}")
    print(f"  --- estimators -> 2d={2*d}  (rho=1/(2d)={mp.nstr(mpf(1)/(2*d),8)}) ---")
    print(f"  2d direct 4-param LS = {mp.nstr(twod_direct,12)}  -> rho={mp.nstr(1/twod_direct,10)}")
    print(f"  2d quad-extrap A_n   = {mp.nstr(twod_A,12)}  -> rho={mp.nstr(1/twod_A,10)}")
    print(f"  2d quad-extrap Q_n   = {mp.nstr(twod_Q,12)}  -> rho={mp.nstr(1/twod_Q,10)}")
    for n in [n for n in ns if n % 7 == 0 or n >= nmax - 1]:
        print(f"   n={n:2d}: A_n={mp.nstr(L[n]/log(factorial(n)),9):>11}  Q_n={mp.nstr((L[n]-L[n-1])/log(n),9):>11}")
    return {
        "name": name, "coeffs": coeffs, "degree": d, "Ms": Ms, "nmax": nmax,
        "raw_trunc_err": raw_err, "richardson_xcheck": xcheck, "bounds_ok": bounds_ok,
        "twod_direct_LS": mp.nstr(twod_direct, 14), "rho_direct": mp.nstr(1 / twod_direct, 14),
        "twod_A": mp.nstr(twod_A, 14), "twod_Q": mp.nstr(twod_Q, 14),
        "rho_A": mp.nstr(1 / twod_A, 14), "rho_Q": mp.nstr(1 / twod_Q, 14),
        "expect_2d": 2 * d, "expect_rho": mp.nstr(mpf(1) / (2 * d), 14),
    }


if __name__ == "__main__":
    nmax = 40
    res = []
    res.append(analyze("(1,0,1)", [1, 0, 1], Ms=[1200, 2400, 4800], nmax=nmax))
    res.append(analyze("(1,0,5)", [5, 0, 1], Ms=[1200, 2400, 4800], nmax=nmax))
    res.append(analyze("(1,3,2)", [2, 3, 1], Ms=[1200, 2400, 4800], nmax=nmax))
    res.append(analyze("b=k+1 (d=1)", [1, 1], Ms=[2000, 4000, 8000], nmax=nmax))
    res.append(analyze("b=k^3+1 (d=3)", [1, 0, 0, 1], Ms=[800, 1600, 3200], nmax=nmax))

    out = {"dps": mp.dps, "nmax": nmax, "results": res}
    js = json.dumps(out, indent=2)
    with open("out/order_coefficients_result.json", "w", newline="\n") as f:
        f.write(js)
    print("\nsha256(result json) =", hashlib.sha256(js.encode()).hexdigest())
