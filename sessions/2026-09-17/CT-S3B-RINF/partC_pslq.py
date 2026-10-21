"""CT-S3B-RINF Part C : high-precision r_inf for V_quad, then the pre-registered
PSLQ probe.  Basis and acceptance rules are frozen in PREREG.md Sec.5.
"""
import hashlib
import json
import time

from mpmath import mp, mpf, mpc, gamma, log, pi, sqrt, nstr, pslq
import sympy as sp

V_QUAD = [1, 1, 3]


def b_value(beta, n):
    acc = mpf(0)
    for k in range(len(beta) - 1, -1, -1):
        acc = acc * n + beta[k]
    return acc


def neville_at_zero(xs, ys):
    c = list(ys)
    n = len(xs)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = ((-xs[i - j]) * c[i] - (-xs[i]) * c[i - 1]) / (xs[i] - xs[i - j])
    return c[-1]


def r_inf(beta, N, L, stride=1):
    r_pp, r_p = mpf(1), mpf(1)
    bprev = b_value(beta, mpf(1))
    xs, ys = [], []
    want = {N + i * stride for i in range(L + 1)}
    top = N + L * stride
    for n in range(2, top + 1):
        bn = b_value(beta, mpf(n))
        r_pp, r_p = r_p, r_p + r_pp / (bprev * bn)
        bprev = bn
        if n in want:
            xs.append(mpf(1) / n)
            ys.append(r_p)
    return neville_at_zero(xs, ys)


def digits(a, b):
    return mpf(0) if a == b else -log(abs((a - b) / b), 10)


def high_precision_rinf(target_dps, N=20000, L=640, stride=520):
    mp.dps = target_dps + 800
    t0 = time.time()
    a = r_inf(V_QUAD, N, L, stride)
    b = r_inf(V_QUAD, 2 * N, L, stride)
    d = digits(a, b)
    print(f"  N={N} L={L} stride={stride} dps={mp.dps}: N-vs-2N agreement = "
          f"{nstr(d, 8)} digits   ({time.time()-t0:.0f}s)", flush=True)
    return b, float(d)


def main():
    print("[C] high-precision r_inf")
    r, conf = high_precision_rinf(2000)
    print(f"  confirmed digits: {conf:.1f}")

    runs = []
    for dps in (500, 1000, 2000):
        if conf < dps + 20:
            runs.append({"dps": dps, "status": "SKIPPED",
                         "reason": f"r_inf confirmed to only {conf:.0f} digits"})
            print(f"  dps={dps}: SKIPPED (insufficient confirmed digits)")
            continue
        mp.dps = dps
        rts = sp.Poly(3 * sp.Symbol("x") ** 2 + sp.Symbol("x") + 1,
                      sp.Symbol("x")).all_roots()
        r1 = mpc(str(sp.re(sp.N(rts[0], dps + 10))),
                 str(sp.im(sp.N(rts[0], dps + 10))))
        g1 = gamma(1 - r1)
        basis = [
            ("r_inf", +r),
            ("1", mpf(1)),
            ("pi", +pi),
            ("sqrt3", sqrt(mpf(3))),
            ("Gamma(1/3)", gamma(mpf(1) / 3)),
            ("Gamma(2/3)", gamma(mpf(2) / 3)),
            ("log2", log(mpf(2))),
            ("log3", log(mpf(3))),
            ("|Gamma(1-r1)|", abs(g1)),
            ("Re Gamma(1-r1)", mp.re(g1)),
        ]
        names = [n for n, _ in basis]
        vec = [v for _, v in basis]
        t0 = time.time()
        rel = pslq(vec, maxcoeff=10**6, maxsteps=100000)
        runs.append({
            "dps": dps, "basis": names,
            "relation": [int(c) for c in rel] if rel else None,
            "status": "RELATION" if rel else "NULL",
            "elapsed_s": round(time.time() - t0, 1),
        })
        print(f"  dps={dps}: {'RELATION ' + str(rel) if rel else 'NULL'} "
              f"({time.time()-t0:.0f}s)", flush=True)

    mp.dps = 220
    r200 = nstr(+r, 200)
    mp.dps = 60
    out = {
        "r_inf_confirmed_digits": conf,
        "r_inf_first_200_digits": r200,
        "pslq_runs": runs,
        "basis_frozen_in": "PREREG.md Sec.5",
        "maxcoeff": 10**6,
        "acceptance": ("identical at 500/1000/2000 dps AND height <= 1e6 AND "
                       "verifies at dps 3000"),
    }
    json.dump(out, open("pslq.json", "w"), indent=2)

    with open("rinf_highprec.txt", "w") as f:
        mp.dps = int(conf) - 10
        f.write(nstr(+r, int(conf) - 20) + "\n")
    print("wrote pslq.json, rinf_highprec.txt")


if __name__ == "__main__":
    main()
