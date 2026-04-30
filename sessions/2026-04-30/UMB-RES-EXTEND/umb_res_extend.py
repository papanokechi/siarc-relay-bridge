"""UMB-RES-EXTEND -- resonance sweep at ratio -2/9 for b1 >= 8.

Tests whether the -2/9 Trans phenomenon survives beyond
b1 in {2,3} (the integer-resonance regime where Class A is
empirically verified).

Coefficient ordering: a-coeffs stored [a2, a1, a0]
(leading first), per project convention. This script
unpacks (a2, a1, a0, b1, b0).

INTEGRALITY NOTE
  Exact ratio a2/b1^2 = -2/9 with integer a2,b1 forces
  b1 = 3k and a2 = -2*k^2 for k in Z\\{0}. From the
  prompt's list {8,9,10,12,15,20,30} only b1 in
  {9,12,15,30} satisfy 3 | b1; b1 in {8,10,20} have NO
  integer (a2, b1) realising exactly -2/9 and yield
  empty enumerations. This is recorded explicitly.

PIPELINE (matches T2B-RESONANCE-B8-12)
  Stage A : float64 K_500, rel-tol 1e-8 (convergence filter)
  Stage B : PSLQ dps=100 N=600 algebraic basis [1, L^j]
  Stage C : PSLQ dps=100 N=600 transcendental basis
            [1, L, pi, L*pi, pi^2, L*pi^2, log2, L*log2]
            with phantom guard (L-coefficient must be != 0).

DEEP VALIDATION (Trans hits only)
  dps=150, N=2000, residual tol 1e-90.
  Cross-talk probe: evaluate 1/L, pi/L, L/pi, 2*L/pi,
                    4/L, L/(2*pi), L+pi against [1, pi, pi^2,
                    log2, log3] via PSLQ at dps=150.

HALT IF
  Trans rate is 0 for ALL b1 in scope >= 8 (i.e. no Trans
  family discovered at -2/9 above b1=3 in any tested H).
  This would indicate the uniformization explanation
  (Remark 8) requires revision.
"""
import json
import math
import multiprocessing as mp_proc
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath
from mpmath import mp, mpf

OUT = Path(__file__).parent

# Step 1 base ratio
RATIO_BASE = Fraction(-2, 9)

# Prompt list of b1 magnitudes
PROMPT_B1 = [8, 9, 10, 12, 15, 20, 30]

# H envelope for free coefficients on the base sweep (a1,a0,b0).
H_BASE = 5
# Smaller H for offset probes (more ratios to test).
H_OFFSET = 3

N_STAGEA = 500
TOL_STAGEA = 1e-8
DPS_PSLQ = 100
N_PSLQ = 600
PSLQ_HMAX_RAT = 10**6
PSLQ_HMAX_TRANS = 10**9
RESIDUAL_TOL_RAT = mpf(10) ** (-40)
RESIDUAL_TOL_TRANS = mpf(10) ** (-30)

# Deep validation
DPS_DEEP = 150
N_DEEP = 2000
PSLQ_HMAX_DEEP = 10**12
RESIDUAL_TOL_DEEP = mpf(10) ** (-90)

HALT_CAP = 200_000  # families enumerated cap


# ---------- enumeration ----------------------------------------------------

def integer_a2_for_ratio(ratio: Fraction, b1: int):
    """Return integer a2 such that a2/b1^2 = ratio, or None."""
    num = ratio.numerator * b1 * b1
    den = ratio.denominator
    if num % den != 0:
        return None
    return num // den


def base_minus_2_9_targets():
    """For each prompt b1, compute integer a2 (or note empty)."""
    out = []
    for b1 in PROMPT_B1:
        a2 = integer_a2_for_ratio(RATIO_BASE, b1)
        out.append({"b1": b1, "a2_pos_b1": a2})
    return out


def offset_targets():
    """For b1 >= 12 in scope, produce ratio -2/9 +- 1/b1^2 with integer a2."""
    out = []
    for b1 in [12, 15, 20, 30]:
        for sign in (+1, -1):
            ratio = RATIO_BASE + Fraction(sign, b1 * b1)
            a2 = integer_a2_for_ratio(ratio, b1)
            out.append({"b1": b1, "ratio": str(ratio), "a2": a2, "sign": sign})
    return out


def enumerate_families():
    """Build full family list. Returns (label, ratio, coeffs)."""
    families = []
    # Base sweep at -2/9
    for b1_pos in PROMPT_B1:
        a2 = integer_a2_for_ratio(RATIO_BASE, b1_pos)
        if a2 is None:
            continue
        # both signs of b1 (a2 stays the same since denominator b1^2 even)
        for b1 in (b1_pos, -b1_pos):
            for a1 in range(-H_BASE, H_BASE + 1):
                for a0 in range(-H_BASE, H_BASE + 1):
                    for b0 in range(-H_BASE, H_BASE + 1):
                        families.append(("base", str(RATIO_BASE),
                                         (a2, a1, a0, b1, b0)))
    # Offset sweep
    for tgt in offset_targets():
        a2 = tgt["a2"]
        if a2 is None:
            continue
        ratio_str = tgt["ratio"]
        b1_pos = tgt["b1"]
        for b1 in (b1_pos, -b1_pos):
            for a1 in range(-H_OFFSET, H_OFFSET + 1):
                for a0 in range(-H_OFFSET, H_OFFSET + 1):
                    for b0 in range(-H_OFFSET, H_OFFSET + 1):
                        families.append(("offset", ratio_str,
                                         (a2, a1, a0, b1, b0)))
    return families


# ---------- Stage A : float64 -----------------------------------------------

def stage_a_float(coeffs):
    a2, a1, a0, b1, b0 = coeffs
    Pp, Pc = 1.0, float(b0)
    Qp, Qc = 0.0, 1.0
    last_vals = []
    for n in range(1, N_STAGEA + 1):
        an = a2 * n * n + a1 * n + a0
        bn = b1 * n + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if not (math.isfinite(Pc) and math.isfinite(Qc)):
            return None
        if n % 50 == 0 and abs(Qc) > 1e100:
            s = abs(Qc)
            Pc /= s; Pp /= s; Qc /= s; Qp /= s
        if Qc == 0:
            return None
        if n >= N_STAGEA - 50:
            v = Pc / Qc
            if not math.isfinite(v):
                return None
            last_vals.append(v)
    if len(last_vals) < 20:
        return None
    arr = np.array(last_vals[-20:])
    spread = float(np.max(arr) - np.min(arr))
    mid = float(np.mean(arr))
    rel = spread / max(abs(mid), 1e-30)
    if rel < TOL_STAGEA:
        return mid
    return None


def eval_pcf_mpmath(coeffs, N, dps):
    mp.dps = dps + 50
    a2, a1, a0, b1, b0 = (mpf(c) for c in coeffs)
    Pp, Pc = mpf(1), b0
    Qp, Qc = mpf(0), mpf(1)
    for n in range(1, N + 1):
        an = a2 * n * n + a1 * n + a0
        bn = b1 * n + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 50 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10) ** 20:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s
    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)


# ---------- Stage B/C : PSLQ ------------------------------------------------

def classify_pslq_worker(item):
    idx, coeffs = item
    try:
        K = eval_pcf_mpmath(coeffs, N_PSLQ, DPS_PSLQ)
    except Exception as exc:
        return (idx, "eval_fail", {"error": str(exc)})
    if K is None:
        return (idx, "eval_fail", {})
    mp.dps = DPS_PSLQ
    K = mpf(K)

    rat_basis = [K ** j for j in range(5)]
    try:
        rel = mpmath.pslq(rat_basis, maxcoeff=PSLQ_HMAX_RAT)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, rat_basis)))
        if residual < RESIDUAL_TOL_RAT:
            if all(int(c) == 0 for c in rel[2:]):
                return (idx, "Rat", {"relation": [int(c) for c in rel],
                                     "residual": float(residual)})
            return (idx, "Alg", {"relation": [int(c) for c in rel],
                                 "residual": float(residual)})

    pi_v = mp.pi
    ln2 = mp.log(2)
    trans_basis = [mpf(1), K, pi_v, K * pi_v, pi_v ** 2,
                   K * pi_v ** 2, ln2, K * ln2]
    basis_names = ["1", "L", "pi", "L*pi", "pi^2",
                   "L*pi^2", "log(2)", "L*log(2)"]
    try:
        rel = mpmath.pslq(trans_basis, maxcoeff=PSLQ_HMAX_TRANS)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, trans_basis)))
        if residual < RESIDUAL_TOL_TRANS:
            L_idx = [1, 3, 5, 7]
            if sum(abs(int(rel[i])) for i in L_idx) == 0:
                return (idx, "Phantom", {
                    "relation": [int(c) for c in rel],
                    "basis": basis_names,
                    "residual": float(residual)})
            uses_log = any(int(rel[i]) != 0 for i in (6, 7))
            uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
            label = "Log" if (uses_log and not uses_pi) else "Trans"
            return (idx, label, {"relation": [int(c) for c in rel],
                                 "basis": basis_names,
                                 "residual": float(residual)})
    return (idx, "Desert", {})


# ---------- Deep validation -------------------------------------------------

def deep_validate_trans(coeffs):
    """Re-evaluate K at dps=150, N=2000; re-run trans PSLQ at high precision.
    Return dict with the relation found (if any) and L value to many digits."""
    mp.dps = DPS_DEEP
    K = eval_pcf_mpmath(coeffs, N_DEEP, DPS_DEEP)
    if K is None:
        return {"deep_eval_fail": True}
    pi_v = mp.pi
    ln2 = mp.log(2)
    trans_basis = [mpf(1), K, pi_v, K * pi_v, pi_v ** 2,
                   K * pi_v ** 2, ln2, K * ln2]
    basis_names = ["1", "L", "pi", "L*pi", "pi^2",
                   "L*pi^2", "log(2)", "L*log(2)"]
    rel = mpmath.pslq(trans_basis, maxcoeff=PSLQ_HMAX_DEEP)
    out = {"L_str": mp.nstr(K, 60), "deep_rel": None, "deep_basis": basis_names}
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, trans_basis)))
        if residual < RESIDUAL_TOL_DEEP:
            out["deep_rel"] = [int(c) for c in rel]
            out["deep_residual"] = float(residual)
    return out


def cross_talk_probe(coeffs):
    """Step 3: probe whether transforms of L land in Q(pi)."""
    mp.dps = DPS_DEEP
    K = eval_pcf_mpmath(coeffs, N_DEEP, DPS_DEEP)
    if K is None or K == 0:
        return {"cross_eval_fail": True}
    pi_v = mp.pi
    ln2 = mp.log(2)
    ln3 = mp.log(3)
    qpi_basis_names = ["1", "pi", "pi^2", "log(2)", "log(3)"]
    qpi_basis = [mpf(1), pi_v, pi_v ** 2, ln2, ln3]
    transforms = {
        "1/L": 1 / K,
        "L*pi": K * pi_v,
        "pi/L": pi_v / K,
        "L/pi": K / pi_v,
        "2L/pi": 2 * K / pi_v,
        "pi/(2L)": pi_v / (2 * K),
        "4/L": 4 / K,
        "L+pi": K + pi_v,
        "L*pi^2": K * pi_v ** 2,
    }
    hits = []
    for name, val in transforms.items():
        basis = [val] + qpi_basis
        rel = mpmath.pslq(basis, maxcoeff=PSLQ_HMAX_DEEP)
        if rel is None:
            continue
        residual = abs(sum(r * b for r, b in zip(rel, basis)))
        if residual < RESIDUAL_TOL_DEEP and int(rel[0]) != 0:
            hits.append({"transform": name,
                         "relation": [int(c) for c in rel],
                         "basis": ["T(L)"] + qpi_basis_names,
                         "residual": float(residual)})
    return {"cross_hits": hits}


# ---------- driver ----------------------------------------------------------

def main():
    t0 = time.time()
    print("[STEP 1] Integrality check at -2/9 for prompt b1 list:")
    base_tgt = base_minus_2_9_targets()
    for r in base_tgt:
        print(f"  b1={r['b1']:>2}: a2_at_-2/9 = {r['a2_pos_b1']}")
    off_tgt = offset_targets()
    print("\n[STEP 1] Offset targets -2/9 +- 1/b1^2 (b1 >= 12):")
    for r in off_tgt:
        print(f"  b1={r['b1']:>2} sign={r['sign']:+d}  "
              f"ratio={r['ratio']}  a2={r['a2']}")

    families = enumerate_families()
    total = len(families)
    print(f"\n[STEP 2] Total families enumerated: {total}")
    if total > HALT_CAP:
        raise RuntimeError(f"HALT: total {total} > cap {HALT_CAP}")

    # bookkeeping
    by_b1_total = {}
    for label, ratio, coeffs in families:
        by_b1_total[(coeffs[3], ratio, label)] = by_b1_total.get(
            (coeffs[3], ratio, label), 0) + 1

    # Stage A
    print(f"\n[STAGE A] float64 K_{N_STAGEA} convergence filter")
    t_a = time.time()
    convergent = []
    for i, (label, ratio, coeffs) in enumerate(families):
        if i % max(1, total // 20) == 0:
            print(f"  Stage A {i}/{total}", flush=True)
        L = stage_a_float(coeffs)
        if L is not None:
            convergent.append((label, ratio, coeffs, L))
    t_a = time.time() - t_a
    print(f"  convergent {len(convergent)}/{total} in {t_a:.1f}s")

    # Stage B/C
    print(f"\n[STAGE B/C] PSLQ classification dps={DPS_PSLQ} N={N_PSLQ}")
    items = [(i, c[2]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"  PSLQ done in {t_bc:.1f}s")

    # Aggregate
    counts_total = {}
    by_b1_class = {}        # b1_pos -> {label: n}  for base sweep
    by_b1_conv = {}         # b1_pos -> n_convergent
    by_b1_total_count = {}  # b1_pos -> n_total
    trans_recs, log_recs, alg_recs, rat_recs, phantom_recs = [], [], [], [], []
    for idx, (lbl, info) in enumerate([(r[1], r[2]) for r in results]):
        sweep_label, ratio, coeffs, L = convergent[idx]
        b1_pos = abs(coeffs[3])
        counts_total[lbl] = counts_total.get(lbl, 0) + 1
        if sweep_label == "base":
            by_b1_class.setdefault(b1_pos, {})[lbl] = (
                by_b1_class.get(b1_pos, {}).get(lbl, 0) + 1)
            by_b1_conv[b1_pos] = by_b1_conv.get(b1_pos, 0) + 1
        rec = {"sweep": sweep_label, "ratio": ratio,
               "coeffs": list(coeffs), "L": float(L), "info": info}
        if lbl == "Trans":
            trans_recs.append(rec)
        elif lbl == "Log":
            log_recs.append(rec)
        elif lbl == "Alg":
            alg_recs.append(rec)
        elif lbl == "Rat":
            rat_recs.append(rec)
        elif lbl == "Phantom":
            phantom_recs.append(rec)

    # totals enumerated per b1_pos for the base sweep
    for label, ratio, coeffs in families:
        if label != "base":
            continue
        bp = abs(coeffs[3])
        by_b1_total_count[bp] = by_b1_total_count.get(bp, 0) + 1

    # Trans-rate per b1 (base sweep)
    rates = {}
    for b1_pos in PROMPT_B1:
        tot = by_b1_total_count.get(b1_pos, 0)
        conv = by_b1_conv.get(b1_pos, 0)
        n_trans = by_b1_class.get(b1_pos, {}).get("Trans", 0)
        rates[b1_pos] = {
            "total": tot,
            "convergent": conv,
            "trans": n_trans,
            "trans_rate_total": (n_trans / tot) if tot else None,
            "trans_rate_convergent": (n_trans / conv) if conv else None,
        }

    # Deep validate Trans hits + cross-talk
    print(f"\n[DEEP] {len(trans_recs)} Trans hit(s) -> dps={DPS_DEEP}")
    for r in trans_recs:
        deep = deep_validate_trans(tuple(r["coeffs"]))
        cross = cross_talk_probe(tuple(r["coeffs"]))
        r["deep"] = deep
        r["cross_talk"] = cross

    # halt logic
    halt = {}
    nontrivial_b1 = [b for b in PROMPT_B1 if b >= 8 and by_b1_conv.get(b, 0) > 0]
    if nontrivial_b1 and all(by_b1_class.get(b, {}).get("Trans", 0) == 0
                             for b in nontrivial_b1):
        halt = {
            "halt_triggered": True,
            "reason": "Trans rate is 0 for all tested b1 >= 8 with "
                      "non-empty convergent stratum at -2/9; "
                      "uniformization explanation in UMB Remark 8 "
                      "(indicial roots {1/3,2/3}) needs revision.",
            "tested_b1": nontrivial_b1,
        }

    out = {
        "task": "UMB-RES-EXTEND",
        "config": {
            "ratio_base": str(RATIO_BASE),
            "prompt_b1": PROMPT_B1,
            "H_base": H_BASE,
            "H_offset": H_OFFSET,
            "halt_cap": HALT_CAP,
            "dps_pslq": DPS_PSLQ,
            "n_pslq": N_PSLQ,
            "dps_deep": DPS_DEEP,
            "n_deep": N_DEEP,
        },
        "integrality_base": base_tgt,
        "integrality_offsets": off_tgt,
        "total_families": total,
        "convergent_total": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "counts_total": counts_total,
        "rates_by_b1_base_sweep": rates,
        "trans_records": trans_recs,
        "log_records": log_recs,
        "alg_count": len(alg_recs),
        "rat_count": len(rat_recs),
        "phantom_count": len(phantom_recs),
        "phantom_records": phantom_recs,
        "halt": halt,
    }
    (OUT / "umb_res_extend_results.json").write_text(
        json.dumps(out, indent=2, default=str))

    # Trans-rate CSV
    csv_lines = ["b1_pos,total,convergent,trans,trans_rate_total,trans_rate_convergent"]
    for b in PROMPT_B1:
        r = rates[b]
        csv_lines.append(
            f"{b},{r['total']},{r['convergent']},{r['trans']},"
            f"{r['trans_rate_total']},{r['trans_rate_convergent']}")
    (OUT / "trans_rate_vs_b1.csv").write_text("\n".join(csv_lines) + "\n")

    print(f"\nCounts: {counts_total}")
    print("Trans-rate per b1 (base sweep at -2/9):")
    for b in PROMPT_B1:
        r = rates[b]
        print(f"  b1={b:>2}: tot={r['total']:>6}  "
              f"conv={r['convergent']:>6}  trans={r['trans']}")
    if halt:
        print(f"\nHALT: {halt['reason']}")
        (OUT / "halt_log.json").write_text(json.dumps(halt, indent=2))
    else:
        (OUT / "halt_log.json").write_text(json.dumps({}, indent=2))

    print(f"\nWall: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
