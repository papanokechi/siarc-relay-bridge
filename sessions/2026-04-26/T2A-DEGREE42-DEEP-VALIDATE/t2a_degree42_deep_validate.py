"""
T2A-DEGREE42-DEEP-VALIDATE — recompute Trans candidates at dps=150, K_1500
and re-classify against bilinear-pi basis.
"""
from __future__ import annotations
import json, time, hashlib, sys
from pathlib import Path
import mpmath as mp

INPUT = Path("t2a_degree42_results.json")
OUT   = Path("t2a_degree42_deep_results.json")

DPS_RECOMP = 150
N_ITER     = 1500
DPS_PSLQ   = 150
TOL_PSLQ   = mp.mpf(10) ** (-100)
HMAX       = 10**12

# Optional cap on candidates (set via env or arg). Default: process all.
LIMIT = None
if len(sys.argv) > 1:
    LIMIT = int(sys.argv[1])

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
            P_curr = P_curr / mag; Q_curr = Q_curr / mag
            P_prev1 = P_prev1 / mag; Q_prev1 = Q_prev1 / mag
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


def main():
    t0 = time.time()
    data = json.load(open(INPUT))
    trans = data["trans_families"]
    if LIMIT:
        trans = trans[:LIMIT]
    n_total = len(trans)
    print(f"[T2A-DV] Loaded {n_total} Trans candidates")
    print(f"[T2A-DV] Recomputing at dps={DPS_RECOMP}, K_{N_ITER}")

    # --- STEP 2: recompute ---
    mp.mp.dps = DPS_RECOMP
    PI  = mp.pi
    LN2 = mp.log(2)
    LN3 = mp.log(3)
    Z2  = mp.zeta(2)
    Z3  = mp.zeta(3)
    Z4  = mp.zeta(4)
    SQ2 = mp.sqrt(2)
    SQ3 = mp.sqrt(3)
    EUL = mp.euler

    recomputed = []
    diverged = 0
    err_recomp = 0
    t_recomp_0 = time.time()
    for i, r in enumerate(trans):
        a = r["coeffs_a"]   # [a4,a3,a2,a1,a0]
        b = r["coeffs_b"]   # [b2,b1,b0]
        try:
            res = kn_mp(a[0], a[1], a[2], a[3], a[4],
                        b[0], b[1], b[2], N_ITER, DPS_RECOMP)
        except Exception:
            err_recomp += 1
            recomputed.append({"r": r, "L": None, "diverged": True, "error": True})
            continue
        if res is None:
            err_recomp += 1
            recomputed.append({"r": r, "L": None, "diverged": True, "error": True})
            continue
        K_curr, K_prev = res
        diff = abs(K_curr - K_prev)
        if diff > mp.mpf("1e-40"):
            diverged += 1
            recomputed.append({"r": r, "L": K_curr, "diverged": True, "diff": diff})
        else:
            recomputed.append({"r": r, "L": K_curr, "diverged": False, "diff": diff})
        if (i+1) % 100 == 0:
            el = time.time() - t_recomp_0
            print(f"  recomp [{i+1}/{n_total}] diverged={diverged} err={err_recomp} elapsed={el:.1f}s")

    el = time.time() - t_recomp_0
    print(f"[T2A-DV] Recompute done: {n_total - diverged - err_recomp} converged, "
          f"{diverged} diverged, {err_recomp} errors in {el:.1f}s")

    if (diverged + err_recomp) > 0.10 * n_total:
        print(f"[HALT] >10% non-convergent at K_{N_ITER}. Will still proceed but flag.")

    # --- STEP 3: bilinear-pi PSLQ ---
    print(f"[T2A-DV] PSLQ bilinear-pi basis at dps={DPS_PSLQ}, tol=1e-100")
    log_bilin = []
    trans_hard = []
    pslq_err = 0
    t_pslq_0 = time.time()
    mp.mp.dps = DPS_PSLQ

    for i, e in enumerate(recomputed):
        if e.get("diverged") or e.get("L") is None:
            continue
        L = e["L"]
        basis = [mp.mpf(1), L, PI, L*PI, PI**2, L*PI**2, LN2, L*LN2, Z3]
        try:
            rel = mp.pslq(basis, maxcoeff=HMAX, tol=TOL_PSLQ)
        except Exception as ex:
            pslq_err += 1
            e["pslq_err_step3"] = str(ex)[:80]
            continue
        if rel is not None:
            e["log_bilin_relation"] = [int(x) for x in rel]
            log_bilin.append(e)
        else:
            trans_hard.append(e)
        if (i+1) % 200 == 0:
            el = time.time() - t_pslq_0
            print(f"  pslq [{i+1}/{n_total}] log_bilin={len(log_bilin)} trans_hard={len(trans_hard)} err={pslq_err} elapsed={el:.1f}s")

    el = time.time() - t_pslq_0
    print(f"[T2A-DV] PSLQ done: log_bilin={len(log_bilin)} trans_hard={len(trans_hard)} pslq_err={pslq_err} in {el:.1f}s")

    # --- STEP 4: ratios for trans_hard ---
    ratios = []
    for e in trans_hard:
        a = e["r"]["coeffs_a"]
        b = e["r"]["coeffs_b"]
        # leading coeffs: a[0]=a4, b[0]=b2
        if b[0] == 0:
            ratios.append(None)
        else:
            ratios.append(mp.mpf(a[0]) / mp.mpf(b[0])**2)

    # all equal?
    common = None
    distribution = {}
    if ratios:
        valid = [r for r in ratios if r is not None]
        for r in valid:
            key = mp.nstr(r, 12)
            distribution[key] = distribution.get(key, 0) + 1
        if len(distribution) == 1:
            common = list(distribution.keys())[0]
    print(f"[T2A-DV] trans_hard ratios: {len(ratios)} families, distribution={distribution}")
    if common:
        print(f"[T2A-DV] Common ratio a4/b2^2 = {common}")

    # --- STEP 5: extended PSLQ on trans_hard limits ---
    print(f"[T2A-DV] Extended PSLQ on trans_hard ({len(trans_hard)} families)")
    # NOTE: zeta(2)=pi^2/6 and zeta(4)=pi^4/90 are REMOVED to avoid
    # spurious PSLQ hits from basis-internal linear dependencies.
    extended_basis_names = ["1","pi","pi^2","pi^3","pi^4",
                            "zeta3",
                            "log2","log3","sqrt2","sqrt3","euler"]
    ext_consts = [mp.mpf(1), PI, PI**2, PI**3, PI**4,
                  Z3, LN2, LN3, SQ2, SQ3, EUL]
    ext_hits = 0
    ext_examples = []
    for e in trans_hard:
        L = e["L"]
        v = [L] + ext_consts
        try:
            rel = mp.pslq(v, maxcoeff=HMAX, tol=TOL_PSLQ)
        except Exception:
            continue
        # First entry of basis is L itself; require its coefficient nonzero,
        # otherwise the relation is purely between constants (spurious).
        if rel is not None and rel[0] != 0:
            e["ext_relation"] = [int(x) for x in rel]
            e["ext_basis_names"] = ["L"] + extended_basis_names
            ext_hits += 1
            if len(ext_examples) < 20:
                ext_examples.append({
                    "coeffs_a": e["r"]["coeffs_a"],
                    "coeffs_b": e["r"]["coeffs_b"],
                    "L": mp.nstr(L, 35),
                    "relation": [int(x) for x in rel],
                    "basis": ["L"] + extended_basis_names,
                })
    print(f"[T2A-DV] Extended PSLQ hits: {ext_hits} / {len(trans_hard)}")

    # --- STEP 6: verdict ---
    pi2_hits = sum(1 for e in trans_hard
                   if "ext_relation" in e and any(
                       e["ext_relation"][i+1] != 0
                       for i, name in enumerate(extended_basis_names) if name == "pi^2"))
    if len(trans_hard) > 0 and pi2_hits > 0:
        verdict = "SUPPORTED"
    elif len(trans_hard) > 0:
        verdict = "PARTIALLY_SUPPORTED"
    else:
        verdict = "INCONCLUSIVE_AT_CMAX_1"
    print(f"[T2A-DV] VERDICT: {verdict}  trans_hard={len(trans_hard)}  pi2_hits={pi2_hits}")

    # --- Output ---
    out = {
        "task": "T2A-DEGREE42-DEEP-VALIDATE",
        "input_trans_count": n_total,
        "dps_recompute": DPS_RECOMP,
        "iter_recompute": N_ITER,
        "dps_pslq": DPS_PSLQ,
        "pslq_tol": "1e-100",
        "hmax": HMAX,
        "recompute_diverged": diverged,
        "recompute_errors": err_recomp,
        "log_bilin_count": len(log_bilin),
        "trans_hard_count": len(trans_hard),
        "pslq_errors_step3": pslq_err,
        "common_ratio_a4_over_b2sq": common,
        "ratio_distribution": distribution,
        "extended_pslq_hits": ext_hits,
        "extended_pslq_examples": ext_examples,
        "pi2_relation_hits": pi2_hits,
        "verdict": verdict,
        "elapsed_total_sec": time.time() - t0,
        "log_bilin_examples": [
            {
                "coeffs_a": e["r"]["coeffs_a"],
                "coeffs_b": e["r"]["coeffs_b"],
                "L": mp.nstr(e["L"], 35),
                "relation": e["log_bilin_relation"],
                "basis": ["1","L","pi","L*pi","pi^2","L*pi^2","log2","L*log2","zeta3"],
            }
            for e in log_bilin[:30]
        ],
        "trans_hard_examples": [
            {
                "coeffs_a": e["r"]["coeffs_a"],
                "coeffs_b": e["r"]["coeffs_b"],
                "L": mp.nstr(e["L"], 35),
                "ratio_a4_over_b2sq": mp.nstr(mp.mpf(e["r"]["coeffs_a"][0]) / mp.mpf(e["r"]["coeffs_b"][0])**2, 12),
            }
            for e in trans_hard[:30]
        ],
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print(f"[T2A-DV] Wrote {OUT}  sha256={h}")


if __name__ == "__main__":
    main()
