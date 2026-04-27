"""
SPRINT-W3-SUBLEADING-BALANCE -- Part B
======================================
Convergence rate analysis.

For a 3-term recurrence  y_{n+1} = b_n y_n - a_n y_{n-1}  with two
linearly-independent solutions p_n (initial: p_-1 = 1, p_0 = 0) and
q_n (q_-1 = 0, q_0 = 1), the CF approximant is p_n / q_n.

We track:
   r_n  = p_n / q_n
   L    = r_N (last computed convergent at large N, our proxy for limit)
   rho_n = |r_n - L| * |q_n|^2
The subdominant char root mu_-  controls the rate, since
   p_n / q_n - L  ~  C * (mu_- / mu_+)^n / q_n^2  (heuristic).
For Trans families,  |mu_-/mu_+|  =  4/(13 + 3 sqrt 17)  =  (13 - 3 sqrt 17)/4
~ 0.1577.
"""

import json
import mpmath
from mpmath import mp, mpf, sqrt, log, fabs, pi as mpi

mp.dps = 200

def trans_families():
    fams = []
    # b1 in {3,6,9,12,15}, a2 = -2 b1^2/9
    for b1 in (3, 6, 9, 12, 15):
        a2 = -2 * (b1 // 3) ** 2
        fams.append((0,  0,  a2, 0, b1))
        fams.append((1,  0,  a2, 1, b1))
        if len(fams) >= 10:
            break
    while len(fams) < 10:
        fams.append((0, 0, -2, 0, 3))
    return fams[:10]

def log_families():
    return [
        (0, 0, -1, 0, 2),    # ratio -1/4
        (0, 1, -1, 1, 2),
        (0, 0, -1, 0, 3),    # ratio -1/9
        (0, 2, -1, 1, 3),
        (0, 0, -2, 0, 5),    # ratio -2/25
    ]

def alg_families():
    return [
        (0, 2, 1, 1, 3),     # complex char roots
        (0, 0, 4, 0, 3),
        (0, 0, 9, 0, 4),
        (0, 1, 1, 0, 2),     # repeated root mu=1
        (0, 4, 9, 2, 4),
    ]

def run_family(label, a0, a1, a2, b0, b1, N=600, n_lo=100, n_hi=600):
    a2_b1sq = mpf(a2) / (mpf(b1) * mpf(b1))
    # Recurrence
    def b_n(n):
        return mpf(b1) * n + mpf(b0)
    def a_n(n):
        nf = mpf(n)
        return mpf(a2) * nf * nf + mpf(a1) * nf + mpf(a0)

    # p_n: p_{-1}=1, p_0=0   (matches "numerator" branch)
    # q_n: q_{-1}=0, q_0=1   ("denominator" branch)
    p_prev, p_curr = mpf(1), mpf(0)
    q_prev, q_curr = mpf(0), mpf(1)
    pseq = [p_curr]
    qseq = [q_curr]
    for n in range(1, N + 1):
        p_nxt = b_n(n) * p_curr - a_n(n) * p_prev
        q_nxt = b_n(n) * q_curr - a_n(n) * q_prev
        p_prev, p_curr = p_curr, p_nxt
        q_prev, q_curr = q_curr, q_nxt
        pseq.append(p_curr)
        qseq.append(q_curr)

    # Take L as r_N
    if abs(qseq[-1]) == 0:
        return {"label": label, "ok": False, "reason": "qN zero"}
    L = pseq[-1] / qseq[-1]

    # Compute rho_n at sample points
    sample_n = [100, 200, 300, 400, 500]
    rhos = []
    for n in sample_n:
        if n >= len(qseq):
            continue
        if abs(qseq[n]) == 0:
            continue
        r_n = pseq[n] / qseq[n]
        rho = abs(r_n - L) * (qseq[n] ** 2)
        rhos.append((n, abs(r_n - L), abs(qseq[n]), rho))
    return {
        "label":   label,
        "ok":      True,
        "fam":     (a0, a1, a2, b0, b1),
        "a2_b1sq": a2_b1sq,
        "L":       L,
        "rhos":    rhos,
    }

def fmt(x, k=8):
    if isinstance(x, mpf):
        return mpmath.nstr(x, k)
    return str(x)

def main():
    print("="*84)
    print("Part B -- convergence rate analysis  (mp.dps = 200,  N = 600)")
    print("="*84)
    print(f"{'tag':<5}{'lab':<5}{'a2/b1^2':>10}{'L (12d)':>22}"
          f"{'rho_100':>14}{'rho_300':>14}{'rho_500':>14}")

    out = {}
    for tag, fams in (("T", trans_families()),
                      ("L", log_families()),
                      ("A", alg_families())):
        out[tag] = []
        for i, fam in enumerate(fams, 1):
            label = f"{tag}{i:02d}"
            r = run_family(label, *fam)
            out[tag].append(r)
            if not r.get("ok"):
                print(f"{tag:<5}{label:<5}  FAIL ({r.get('reason')})")
                continue
            rhos = r["rhos"]
            rho_dict = {n: rho for (n, _, _, rho) in rhos}
            print(f"{tag:<5}{label:<5}{fmt(r['a2_b1sq'],6):>10}"
                  f"{fmt(r['L'],14):>22}"
                  f"{fmt(rho_dict.get(100, mpf(0)),6):>14}"
                  f"{fmt(rho_dict.get(300, mpf(0)),6):>14}"
                  f"{fmt(rho_dict.get(500, mpf(0)),6):>14}")

    # ----- Test: is rho_n converging?  Look at log10(rho_n) trend -----
    print("\n" + "="*84)
    print("rho_n trend (log10 |r_n - L| at n = 100, 300, 500)")
    print("="*84)
    print(f"{'tag':<5}{'lab':<5}{'log10|r_100-L|':>18}{'log10|r_300-L|':>18}{'log10|r_500-L|':>18}")
    for tag, lst in out.items():
        for r in lst:
            if not r.get("ok"):
                continue
            d = {n: err for (n, err, _, _) in r["rhos"]}
            def lg(x):
                if x is None or abs(x) == 0:
                    return "-inf"
                return fmt(log(abs(x))/log(mpf(10)), 6)
            print(f"{tag:<5}{r['label']:<5}"
                  f"{lg(d.get(100)):>18}"
                  f"{lg(d.get(300)):>18}"
                  f"{lg(d.get(500)):>18}")

    # ----- PSLQ-test the rho_500 of Trans families against {1, sqrt(17), pi, log2} -----
    print("\n" + "="*84)
    print("PSLQ test: is rho_500 (Trans) algebraically simple?")
    print("="*84)
    for r in out["T"]:
        if not r.get("ok"):
            continue
        rho500 = next((rho for (n, _, _, rho) in r["rhos"] if n == 500), None)
        if rho500 is None:
            continue
        basis = [mpf(1), sqrt(mpf(17)), mpi, log(mpf(2)), rho500]
        try:
            rel = mpmath.pslq(basis, tol=mpf(10)**(-50), maxcoeff=10**6)
        except Exception as e:
            rel = None
        L_coeff = rel[-1] if rel is not None else None
        phantom = (L_coeff is not None and L_coeff == 0)
        status = "PHANTOM_HIT_REJECTED" if phantom else (
                 "found relation"      if rel is not None else "no relation")
        print(f"  {r['label']}: rho500 = {fmt(rho500, 8)}    PSLQ = {rel}  -> {status}")

    # ----- save -----
    def serialise(x):
        if isinstance(x, mpf):
            return str(x)
        if isinstance(x, tuple):
            return list(x)
        if isinstance(x, list):
            return [serialise(v) for v in x]
        if isinstance(x, dict):
            return {k: serialise(v) for k, v in x.items()}
        return x
    with open("convergence_rate.json", "w") as f:
        json.dump({tag: [serialise(r) for r in lst] for tag, lst in out.items()},
                  f, indent=2, default=str)
    print("\nWrote convergence_rate.json")

if __name__ == "__main__":
    main()
