"""
T2A-CMAX2-DEEP-VALIDATE — Recompute Trans-candidates from CMAX=2
search at dps=150, K_1500, then PSLQ against bilinear-pi basis.
Mandatory L-coefficient != 0 to prevent zeta(2)=pi^2/6 phantom trap.

Sampling: if # Trans-candidates > 5000, take a deterministic random
sample of 1000 (seed=20260427) to keep total work tractable
(per task spec).
"""
from __future__ import annotations

import json
import random
import time
import hashlib
from pathlib import Path

import mpmath as mp

IN_JSON = Path("t2a_cmax2_results.json")
OUT_JSON = Path("t2a_cmax2_deep_results.json")

DPS_DEEP = 150
ITER_DEEP = 1500
TOL_PSLQ = mp.mpf(10) ** (-100)
PSLQ_HMAX = 10**14
SAMPLE_SIZE = 1000
SAMPLE_SEED = 20260427


def kn_mp(a4, a3, a2, a1, a0, b2, b1, b0, N, dps):
    mp.mp.dps = dps
    b_at_0 = mp.mpf(b0)
    b_at_1 = mp.mpf(b2 + b1 + b0)
    a_at_1 = mp.mpf(a4 + a3 + a2 + a1 + a0)
    P_prev2 = b_at_0
    P_prev1 = b_at_1 * b_at_0 + a_at_1
    Q_prev2 = mp.mpf(1)
    Q_prev1 = b_at_1
    K_prev = K_curr = None
    for n in range(2, N + 1):
        an = a4*n*n*n*n + a3*n*n*n + a2*n*n + a1*n + a0
        bn = b2*n*n + b1*n + b0
        P_curr = bn * P_prev1 + an * P_prev2
        Q_curr = bn * Q_prev1 + an * Q_prev2
        if Q_curr == 0:
            return None
        K_prev = K_curr
        K_curr = P_curr / Q_curr
        if n % 16 == 0:
            mag = max(abs(P_curr), abs(Q_curr), mp.mpf(1))
            P_curr = P_curr / mag
            Q_curr = Q_curr / mag
            P_prev1 = P_prev1 / mag
            Q_prev1 = Q_prev1 / mag
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


def deep_classify(L):
    """Return (label, rel, phantoms). Bilinear-pi basis with strict
    L-coef != 0 defense."""
    pi = mp.pi
    log2 = mp.log(2)
    z3 = mp.zeta(3)
    # Index 0 = L (target slot)
    basis_bilin = [L, mp.mpf(1), pi, L*pi, pi**2, L*pi**2,
                   log2, L*log2, z3]
    phantoms = []
    rel = mp.pslq(basis_bilin, maxcoeff=PSLQ_HMAX, tol=TOL_PSLQ)
    if rel is not None:
        if int(rel[0]) == 0:
            phantoms.append(("bilin", [int(x) for x in rel]))
        else:
            return ("Log-bilin", [int(x) for x in rel], phantoms)
    # Extended basis (NO zeta(2)/zeta(4) - avoid identity traps)
    z5 = mp.zeta(5)
    cat = mp.catalan
    basis_ext = [L, mp.mpf(1), pi, L*pi, pi**2, L*pi**2,
                 log2, L*log2, z3, L*z3, z5, cat]
    rel = mp.pslq(basis_ext, maxcoeff=PSLQ_HMAX, tol=TOL_PSLQ)
    if rel is not None:
        if int(rel[0]) == 0:
            phantoms.append(("ext", [int(x) for x in rel]))
        else:
            return ("Log-bilin-ext", [int(x) for x in rel], phantoms)
    return ("Trans-hard", None, phantoms)


def main():
    print(f"[DEEP] loading {IN_JSON}")
    with IN_JSON.open() as f:
        data = json.load(f)

    trans = [r for r in data["results"]
             if r["classification"] == "Trans-candidate"]
    n_trans = len(trans)
    print(f"[DEEP] Trans-candidates in input: {n_trans}")

    sampled = False
    if n_trans > 5000:
        random.seed(SAMPLE_SEED)
        # Sample over UNIQUE limit values to maximise diversity
        by_limit = {}
        for r in trans:
            by_limit.setdefault(r["limit"], []).append(r)
        unique_limits = list(by_limit.keys())
        print(f"[DEEP] unique L values among Trans-cand: {len(unique_limits)}")
        if len(unique_limits) > SAMPLE_SIZE:
            sample_keys = random.sample(unique_limits, SAMPLE_SIZE)
        else:
            sample_keys = unique_limits
        # take 1 representative family per sampled L
        trans_subset = [by_limit[k][0] for k in sample_keys]
        sampled = True
        print(f"[DEEP] sampled {len(trans_subset)} representatives "
              f"(seed={SAMPLE_SEED})")
    else:
        trans_subset = trans

    print(f"[DEEP] recompute at dps={DPS_DEEP}, K_{ITER_DEEP}")
    deep_results = []
    counts = {"Log-bilin":0, "Log-bilin-ext":0, "Trans-hard":0,
              "DivergeAt150":0, "ERR":0}
    phantoms_total = 0
    t0 = time.time()
    for i, r in enumerate(trans_subset):
        a4,a3,a2,a1,a0 = r["coeffs_a"]
        b2,b1,b0 = r["coeffs_b"]
        try:
            out = kn_mp(a4,a3,a2,a1,a0,b2,b1,b0, ITER_DEEP, DPS_DEEP)
            if out is None or out[1] is None:
                label, rel, phlog, L_str, diff_str = (
                    "DivergeAt150", None, [], None, None)
            else:
                Kn, Kn_1 = out
                diff = abs(Kn - Kn_1)
                if diff > mp.mpf("1e-100"):
                    label, rel, phlog = "DivergeAt150", None, []
                    L_str = mp.nstr(Kn, 30)
                    diff_str = mp.nstr(diff, 5)
                else:
                    mp.mp.dps = 100
                    label, rel, phlog = deep_classify(Kn)
                    L_str = mp.nstr(Kn, 60)
                    diff_str = mp.nstr(diff, 5)
        except Exception as e:
            label, rel, phlog, L_str, diff_str = ("ERR", str(e), [], None, None)
        counts[label] = counts.get(label, 0) + 1
        phantoms_total += len(phlog)
        rec = {
            "coeffs_a": [a4,a3,a2,a1,a0],
            "coeffs_b": [b2,b1,b0],
            "L_dps150": L_str,
            "diff": diff_str,
            "classification": label,
            "pslq_relation": rel,
            "phantoms_rejected": phlog,
            "a4_b2sq_ratio": float(mp.mpf(a4)/(mp.mpf(b2)**2)),
            "limit_dps50": r["limit"],
        }
        deep_results.append(rec)
        if (i+1) % 50 == 0:
            print(f"  [{i+1}/{len(trans_subset)}] {counts} "
                  f"phantoms={phantoms_total} "
                  f"elapsed={time.time()-t0:.1f}s")
    elapsed = time.time() - t0
    print(f"[DEEP] done: {counts}, phantoms_rejected={phantoms_total}, "
          f"{elapsed:.1f}s")

    summary = {
        "input_file": str(IN_JSON),
        "trans_candidates_total": n_trans,
        "sampled": sampled,
        "sample_size": len(trans_subset),
        "sample_seed": SAMPLE_SEED if sampled else None,
        "dps": DPS_DEEP,
        "iter": ITER_DEEP,
        "tol_pslq": "1e-100",
        "classification_counts": counts,
        "phantoms_rejected_total": phantoms_total,
        "elapsed_sec": elapsed,
        "results": deep_results,
    }
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"[DEEP] wrote {OUT_JSON}")
    sha = hashlib.sha256(OUT_JSON.read_bytes()).hexdigest()
    print(f"[DEEP] sha256={sha}")


if __name__ == "__main__":
    main()
