"""UMB-CROSSDEG-29 Step 3: PSLQ validate limits at top-3 R1 concentrations.

For each top-3 R1 in {1/4, 1/2, 2/1}, pick the minimal-|coeffs| Trans
candidate, recompute the PCF limit at dps=300 with K=2500, and PSLQ
against {1, pi, pi^2, log 2, log pi} (per prompt).
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CENSUS = ROOT / "t2a_cmax2_results.json"

DPS = 300
K_TERMS = 2500
PSLQ_HMAX = 10**12
PSLQ_TOL = mp.mpf("1e-200")
RESID_THR = mp.mpf("1e-150")

TARGET_R1 = [Fraction(1, 4), Fraction(1, 2), Fraction(2, 1)]


def coeffs_norm(rec):
    return sum(abs(int(x)) for x in rec["coeffs_a"]) + sum(
        abs(int(x)) for x in rec["coeffs_b"]
    )


def pcf_limit(coeffs_a, coeffs_b, K=K_TERMS):
    """Backward recurrence for K{b(n)/a(n)}, leading-first coefficients."""
    a = [mp.mpf(int(x)) for x in coeffs_a]
    b = [mp.mpf(int(x)) for x in coeffs_b]
    da = len(a) - 1
    db = len(b) - 1

    def aval(n):
        s = mp.mpf(0)
        for i, c in enumerate(a):
            s += c * mp.mpf(n) ** (da - i)
        return s

    def bval(n):
        s = mp.mpf(0)
        for i, c in enumerate(b):
            s += c * mp.mpf(n) ** (db - i)
        return s

    # Forward Wallis-style recurrence on numerator/denominator continuants.
    # PCF: a(0) + K{b(n)/a(n), n=1..}; project convention.
    P_prev = mp.mpf(1)
    P_curr = aval(0)
    Q_prev = mp.mpf(0)
    Q_curr = mp.mpf(1)
    last = []
    for n in range(1, K + 1):
        an = aval(n)
        bn = bval(n)
        P_new = an * P_curr + bn * P_prev
        Q_new = an * Q_curr + bn * Q_prev
        P_prev, P_curr = P_curr, P_new
        Q_prev, Q_curr = Q_curr, Q_new
        s = max(abs(P_curr), abs(Q_curr), mp.mpf(1))
        if s > mp.mpf("1e+1000"):
            P_prev /= s
            P_curr /= s
            Q_prev /= s
            Q_curr /= s
        if n > K - 30 and Q_curr != 0:
            last.append(P_curr / Q_curr)
    if not last or Q_curr == 0:
        return None, None
    val = P_curr / Q_curr
    spread = max(last) - min(last)
    rel = spread / max(abs(val), mp.mpf("1e-50"))
    return val, rel


def pslq_check(L, names_basis):
    rel = mp.pslq(names_basis[1], maxcoeff=PSLQ_HMAX, tol=PSLQ_TOL)
    if rel is None:
        return None, "no relation"
    s = sum(int(c) * x for c, x in zip(rel, names_basis[1]))
    if abs(s) > RESID_THR:
        return None, f"residual {mp.nstr(abs(s),3)}"
    # phantom guard: require non-zero coefficient on L-bearing index 0
    if rel[0] == 0:
        return None, "phantom (no L coefficient)"
    return rel, mp.nstr(abs(s), 5)


def main():
    mp.mp.dps = DPS
    print(f"[load] {CENSUS}")
    with CENSUS.open("r", encoding="utf-8") as fh:
        records = json.load(fh)["results"]
    trans = [r for r in records if r["classification"] == "Trans-candidate"]
    print(f"[trans] {len(trans)}")

    picks = []
    for q in TARGET_R1:
        # choose minimum coeffs_norm with R1 == q
        cand = []
        for r in trans:
            a = r["coeffs_a"]
            b = r["coeffs_b"]
            R1 = Fraction(int(a[0]), int(b[0]) ** 2)
            if R1 == q:
                cand.append(r)
        cand.sort(key=lambda r: (coeffs_norm(r), abs(int(r["coeffs_a"][0]))))
        if cand:
            picks.append((q, cand[0], len(cand)))
    print(f"[picks] {[(str(q), p['coeffs_a'], p['coeffs_b'], n) for q,p,n in picks]}")

    out = {"dps": DPS, "K": K_TERMS, "picks": []}
    for q, rec, count in picks:
        a = rec["coeffs_a"]
        b = rec["coeffs_b"]
        print(f"\n[R1={q}] family a={a} b={b} (concentration={count})")
        L, rel_spread = pcf_limit(a, b)
        if L is None:
            print("  ABORT: divergent")
            out["picks"].append(
                {
                    "R1": str(q),
                    "a": a,
                    "b": b,
                    "L": None,
                    "status": "divergent",
                }
            )
            continue
        print(f"  L = {mp.nstr(L, 30)}, rel_spread = {mp.nstr(rel_spread, 3)}")

        ln2 = mp.log(2)
        lnpi = mp.log(mp.pi)
        # basis: [L, 1, pi, pi^2, log2, log pi]
        basis = [L, mp.mpf(1), mp.pi, mp.pi * mp.pi, ln2, lnpi]
        names = ["L", "1", "pi", "pi^2", "log2", "log_pi"]
        rel, info = pslq_check(L, (names, basis))
        # also check L*basis hits (multiplicative relations).
        basis2 = [L, L * mp.pi, L * ln2, mp.mpf(1), mp.pi, ln2]
        names2 = ["L", "L*pi", "L*log2", "1", "pi", "log2"]
        rel2, info2 = pslq_check(L, (names2, basis2))

        out["picks"].append(
            {
                "R1": str(q),
                "concentration_count": count,
                "a": a,
                "b": b,
                "L": mp.nstr(L, 60),
                "rel_spread": mp.nstr(rel_spread, 3),
                "pslq_additive": {
                    "names": names,
                    "rel": [int(c) for c in rel] if rel else None,
                    "info": info,
                },
                "pslq_multiplicative": {
                    "names": names2,
                    "rel": [int(c) for c in rel2] if rel2 else None,
                    "info": info2,
                },
            }
        )
        print(f"  PSLQ-add  : {rel} ({info})")
        print(f"  PSLQ-mult : {rel2} ({info2})")

    out_path = HERE / "pslq_top3_validate.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print(f"\n[write] {out_path}")


if __name__ == "__main__":
    main()
