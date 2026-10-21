"""CT-S3B-RINF : r_infinity for V_quad, the leading amplitude K, and a PSLQ probe.

Pre-registered in PREREG.md.  The 1e-3000 brute-force tail bound is ill-posed
(finding S3B-F1); the substitute Neville-extrapolation procedure declared in
PREREG.md Sec.1 is used instead, and only N-vs-2N confirmed digits are claimed.
"""
import hashlib
import json
import sys
import time

from mpmath import mp, mpf, mpc, loggamma, gamma, log, pi, sqrt, nstr, pslq
import sympy as sp

V_QUAD = [1, 1, 3]          # beta low->high : b(n) = 3n^2 + n + 1


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def b_value(beta, n):
    acc = mpf(0) * n
    for k in range(len(beta) - 1, -1, -1):
        acc = acc * n + beta[k]
    return acc


def roots_of(beta):
    """Exact roots via sympy, converted to mpmath at current precision."""
    x = sp.Symbol("x")
    poly = sum(sp.Integer(int(c)) * x**k for k, c in enumerate(beta))
    rts = sp.Poly(poly, x).all_roots()
    out = []
    for r in rts:
        v = sp.N(r, mp.dps + 10)
        out.append(mpc(str(sp.re(v)), str(sp.im(v))))
    return rts, out


def neville_at_zero(xs, ys):
    """Polynomial extrapolation through (xs, ys) evaluated at x = 0."""
    n = len(xs)
    c = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = ((0 - xs[i - j]) * c[i] - (0 - xs[i]) * c[i - 1]) / (
                xs[i] - xs[i - j]
            )
    return c[-1]


# --------------------------------------------------------------------------
# Part A : r_infinity
# --------------------------------------------------------------------------
def r_tail_values(beta, N, L):
    """r_n for n = N .. N+L  (r_n = r_{n-1} + r_{n-2}/(b(n-1)b(n)))."""
    r_pp, r_p = mpf(1), mpf(1)          # r_0, r_1
    bprev = b_value(beta, mpf(1))
    out = []
    for n in range(2, N + L + 1):
        bn = b_value(beta, mpf(n))
        r_pp, r_p = r_p, r_p + r_pp / (bprev * bn)
        bprev = bn
        if n >= N:
            out.append((n, r_p))
    return out


def r_infinity(beta, N, L, dps):
    mp.dps = dps
    vals = r_tail_values(beta, N, L)
    xs = [mpf(1) / n for n, _ in vals]
    ys = [v for _, v in vals]
    return neville_at_zero(xs, ys)


# --------------------------------------------------------------------------
# Part B : amplitude K
# --------------------------------------------------------------------------
def K_closed_form(beta, r_inf):
    """K = r_inf * (2 pi)^((d-1)/2) * d^(-1/2) / prod_i Gamma(1 - r_i)."""
    d = len(beta) - 1
    _, rts = roots_of(beta)
    prod = mpc(1)
    for r in rts:
        prod *= gamma(1 - r)
    val = r_inf * (2 * pi) ** (mpf(d - 1) / 2) / sqrt(mpf(d)) / prod
    return val, prod


def K_numeric(beta, N, L, dps, drop_gamma_factor=False):
    """Extrapolate Q_n / (Gamma(dn+1) (beta_d/d^d)^n n^s) to n -> infinity."""
    mp.dps = dps
    d = len(beta) - 1
    s = mpf(beta[d - 1]) / mpf(beta[d]) + mpf(d - 1) / 2
    A = log(mpf(d) ** d / beta[d])

    prev, cur = mpf(0), mpf(1)
    scale = mpf(0)
    vals = []
    for n in range(1, N + L + 1):
        bn = b_value(beta, mpf(n))
        prev, cur = cur, bn * cur + prev
        m = abs(cur)
        prev /= m
        cur /= m
        scale += log(m)
        if n >= N:
            logK = scale - loggamma(d * mpf(n) + 1) + n * A - s * log(mpf(n))
            # `cur` is Q_n rescaled to unit modulus, so it carries sign(Q_n),
            # which log|Q_n| discards.  K may be negative.
            vals.append((n, mp.sign(cur) * mp.e**logK))
    xs = [mpf(1) / n for n, _ in vals]
    ys = [v for _, v in vals]
    return neville_at_zero(xs, ys), s


def digits_agree(a, b):
    if a == b:
        return mpf(mp.dps)
    if b == 0:
        return mpf(0)
    return -log(abs((a - b) / b), 10)


# --------------------------------------------------------------------------
def part_a(dps=400, N=60000, L=40):
    print(f"[A] r_inf for V_quad  dps={dps} N={N} L={L}", flush=True)
    t0 = time.time()
    r_N = r_infinity(V_QUAD, N, L, dps)
    r_2N = r_infinity(V_QUAD, 2 * N, L, dps)
    ag = digits_agree(r_N, r_2N)
    print(f"    r_inf(N)  = {nstr(r_N, 40)}")
    print(f"    r_inf(2N) = {nstr(r_2N, 40)}")
    print(f"    N vs 2N agreement digits = {nstr(ag, 8)}   ({time.time()-t0:.0f}s)")
    return {
        "dps": dps, "N": N, "L": L,
        "r_inf_N": nstr(r_N, 120),
        "r_inf_2N": nstr(r_2N, 120),
        "agreement_digits": float(ag),
        "r_inf_nonzero": bool(abs(r_N) > mpf("1e-50")),
        "note": ("brute-force 1e-3000 tail bound is unreachable (needs "
                 "N ~ 1e999.5); Neville extrapolation per PREREG Sec.1"),
    }, r_2N


CASES = [
    ("V_quad_d2_3n2+n+1", [1, 1, 3]),
    ("d2_n2+1", [1, 0, 1]),
    ("d2_2n2-3n+5", [5, -3, 2]),
    ("d3_n3-2n-3", [-3, -2, 0, 1]),
    ("d3_2n3+n2+1", [1, 0, 1, 2]),
    ("d4_x4-3x3-3x2+x+1", [1, 1, -3, -3, 1]),
    ("d4_x4+1", [1, 0, 0, 0, 1]),
    ("d4_7x4+x", [0, 1, 0, 0, 7]),
]


def part_b(dps=260, N=4000, L=34, Nr=40000, Lr=40):
    print(f"[B] amplitude K   dps={dps} N={N} L={L}", flush=True)
    rows = []
    for label, beta in CASES:
        mp.dps = dps
        sym_roots, _ = roots_of(beta)
        bad = [str(r) for r in sym_roots
               if r.is_real and r.is_integer and r > 0]
        if bad:
            rows.append({"label": label, "halt": f"positive integer root {bad}"})
            print(f"    {label:24s} HALT positive integer root")
            continue
        t0 = time.time()
        r_inf = r_infinity(beta, Nr, Lr, dps)
        K_cf, gprod = K_closed_form(beta, r_inf)
        K_num, s = K_numeric(beta, N, L, dps)
        ag = digits_agree(K_num, K_cf)
        # control: same formula with the Gamma product omitted
        K_ctrl = r_inf * (2 * pi) ** (mpf(len(beta) - 2) / 2) / sqrt(
            mpf(len(beta) - 1))
        ag_ctrl = digits_agree(K_num, K_ctrl)
        rows.append({
            "label": label, "beta_low_to_high": [int(x) for x in beta],
            "d": len(beta) - 1, "s": nstr(s, 20),
            "r_inf": nstr(r_inf, 40),
            "gamma_product": nstr(gprod, 30),
            "K_closed_form": nstr(K_cf, 40),
            "K_numeric": nstr(K_num, 40),
            "agreement_digits": float(ag),
            "control_no_gamma_agreement_digits": float(ag_ctrl),
            "elapsed_s": round(time.time() - t0, 1),
        })
        print(f"    {label:24s} K={nstr(K_cf,18):<24s} "
              f"agree={float(ag):7.2f}d  control={float(ag_ctrl):6.2f}d",
              flush=True)
    return rows


def part_c(r_inf, dpss=(500, 1000, 2000)):
    print("[C] PSLQ probe on r_inf", flush=True)
    results = []
    for dps in dpss:
        mp.dps = dps + 30
        r = r_infinity(V_QUAD, 60000, 40, dps + 30)
        _, rts = roots_of(V_QUAD)
        basis = {
            "r_inf": r,
            "1": mpf(1),
            "pi": pi,
            "sqrt3": sqrt(3),
            "Gamma(1/3)": gamma(mpf(1) / 3),
            "Gamma(2/3)": gamma(mpf(2) / 3),
            "log2": log(2),
            "log3": log(3),
            "|Gamma(1-r1)|": abs(gamma(1 - rts[0])),
            "arg-free ReGamma(1-r1)": mp.re(gamma(1 - rts[0])),
        }
        names = list(basis)
        vec = [basis[k] for k in names]
        mp.dps = dps
        rel = pslq([mpf(v.real) if isinstance(v, mpc) else mpf(v) for v in vec],
                   maxcoeff=10**6, maxsteps=20000)
        results.append({"dps": dps, "basis": names,
                        "relation": [int(c) for c in rel] if rel else None})
        print(f"    dps={dps}: {'relation ' + str(rel) if rel else 'NULL'}",
              flush=True)
    return results


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "a"):
        a, r_ref = part_a()
        json.dump(a, open("rinf.json", "w"), indent=2)
    if which in ("all", "b"):
        rows = part_b()
        json.dump({"cases": rows}, open("amplitude.json", "w"), indent=2)
    if which in ("all", "c"):
        c = part_c(None)
        json.dump({"runs": c}, open("pslq.json", "w"), indent=2)
    print("done")
