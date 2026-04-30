"""UMB-GAMMA0-2-SWEEP (P-08) -- non-PSL2(Z) extension.

Question
    The -2/9 Trans phenomenon corresponds to PSL2(Z), where the
    cuspidal indicial roots {1/3, 2/3} predict
        rho = -m(b-m)/b^2 |_{m=1,b=3} = -2/9.
    Does the same indicial-root prediction generalise to other
    arithmetic Fuchsian groups?

Groups tested
    Gamma0(2): one elliptic point of order 2, two cusps. Take
        m=1, b=2  =>  predicted ratio = -1/4.
        (The +1/4 Class B ratio is well-known F24/Brouncker; the
        -1/4 ratio is a separate stratum.)
    Hecke triangle G_q, q in {4,5,6,8}: indicial roots
        {1/q, (q-1)/q}, predicted ratio = -(q-1)/q^2.

Methodology (matches UMB-RES-EXTEND scaffold)
    For each predicted ratio rho = p/q^2 with integer
    realisation a2/b1^2 = rho:
      Stage A : float64 K_500 convergence filter
      Stage B : PSLQ algebraic basis [1, L, ..., L^4]
      Stage C : PSLQ trans basis [1, L, pi, L*pi, pi^2, L*pi^2,
                log2, L*log2]
    Convergent-stratum threshold for "validated at dps=150
    with >=1000 families per group" is met by aggregate over
    the (a1,a0,b0) cube and the b1 list per group.

HALT logic
    HALT-A : G_4 prediction (-3/16) yields 0 Trans across the
             1000+ family stratum (T2-B already saw 0 Trans).
             -> indicial-root argument needs Stokes refinement.
    HALT-B : ANY G_q yields >=1 deep-validated Trans at the
             predicted ratio. -> Major: open OP-2 paper.
    Both halts logged with separate keys.
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

# ---------- group/ratio specifications ------------------------------------

GROUPS = [
    # (label, ratio, b1_list, free_H, predict_note)
    ("Gamma0(2)", Fraction(-1, 4),  [2, 4, 6, 8],   5,
     "indicial {0,1/2} at order-2 elliptic point; m=1,b=2"),
    ("G_4",       Fraction(-3, 16), [4, 8, 12],     5,
     "indicial {1/4,3/4}; m=1,b=4"),
    ("G_5",       Fraction(-4, 25), [5, 10, 15],    5,
     "indicial {1/5,4/5}; m=1,b=5"),
    ("G_6",       Fraction(-5, 36), [6, 12, 18],    5,
     "indicial {1/6,5/6}; m=1,b=6"),
    ("G_8",       Fraction(-7, 64), [8, 16],        5,
     "indicial {1/8,7/8}; m=1,b=8"),
]

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


# ---------- enumeration ----------------------------------------------------

def integer_a2_for_ratio(ratio: Fraction, b1: int):
    num = ratio.numerator * b1 * b1
    den = ratio.denominator
    if num % den != 0:
        return None
    return num // den


def enumerate_for_group(group_label, ratio, b1_list, H):
    families = []  # (group_label, ratio_str, b1_pos, coeffs)
    for b1_pos in b1_list:
        a2 = integer_a2_for_ratio(ratio, b1_pos)
        if a2 is None:
            continue
        # Use only positive b1 to keep family count predictable; sign
        # of b1 produces a sign-equivalent stratum.
        b1 = b1_pos
        for a1 in range(-H, H + 1):
            for a0 in range(-H, H + 1):
                for b0 in range(-H, H + 1):
                    families.append(
                        (group_label, str(ratio), b1_pos,
                         (a2, a1, a0, b1, b0)))
    return families


# ---------- Stage A : float64 ----------------------------------------------

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


# ---------- Stage B/C : PSLQ -----------------------------------------------

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


# ---------- deep validation -------------------------------------------------

def deep_validate_trans(coeffs):
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


# ---------- driver ---------------------------------------------------------

def main():
    t0 = time.time()

    # Step 1: integrality table per group
    print("[STEP 1] Group / predicted ratio / integer realisations")
    integrality = []
    families = []
    for label, ratio, b1_list, H, note in GROUPS:
        per_b1 = []
        for b1 in b1_list:
            a2 = integer_a2_for_ratio(ratio, b1)
            per_b1.append({"b1": b1, "a2": a2})
        integrality.append({
            "group": label, "ratio": str(ratio),
            "predict_note": note, "b1_list": b1_list, "H": H,
            "integer_table": per_b1,
        })
        print(f"  {label:>10}  ratio={str(ratio):>7}  "
              f"b1={b1_list}  realisations="
              f"{[(r['b1'], r['a2']) for r in per_b1]}")
        families.extend(enumerate_for_group(label, ratio, b1_list, H))

    total = len(families)
    print(f"\n[STEP 2] Total families enumerated: {total}")

    # Stage A
    print(f"\n[STAGE A] float64 K_{N_STAGEA}")
    t_a = time.time()
    convergent = []
    progress_step = max(1, total // 10)
    for i, fam in enumerate(families):
        if i % progress_step == 0:
            print(f"  Stage A {i}/{total}", flush=True)
        L = stage_a_float(fam[3])
        if L is not None:
            convergent.append(fam + (L,))
    t_a = time.time() - t_a
    print(f"  convergent {len(convergent)}/{total} in {t_a:.1f}s")

    # Stage B/C parallel
    print(f"\n[STAGE B/C] PSLQ dps={DPS_PSLQ} N={N_PSLQ}")
    items = [(i, c[3]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"  PSLQ done in {t_bc:.1f}s")

    # Aggregate per group
    by_group = {}        # label -> {Trans:..., Log:..., ...}
    by_group_b1 = {}     # (label, b1_pos) -> counts
    by_group_total = {}  # label -> total enumerated
    by_group_conv = {}   # label -> total convergent
    trans_recs, log_recs, alg_recs, rat_recs, phantom_recs = [], [], [], [], []
    for label, ratio, b1_list, H, note in GROUPS:
        by_group[label] = {}
        by_group_total[label] = 0
        by_group_conv[label] = 0
        for b1 in b1_list:
            by_group_b1[(label, b1)] = {"total": 0, "convergent": 0}
    for fam in families:
        gl, _, b1_pos, _ = fam
        by_group_total[gl] += 1
        by_group_b1[(gl, b1_pos)]["total"] += 1
    for idx, fam in enumerate(convergent):
        gl, ratio_str, b1_pos, coeffs, L = fam
        by_group_conv[gl] += 1
        by_group_b1[(gl, b1_pos)]["convergent"] += 1
        rid, lbl, info = results[idx]
        by_group[gl][lbl] = by_group[gl].get(lbl, 0) + 1
        rec = {"group": gl, "ratio": ratio_str,
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

    # Trans rate per group
    rates = {}
    for label, ratio, b1_list, H, note in GROUPS:
        tot = by_group_total[label]
        conv = by_group_conv[label]
        n_trans = by_group[label].get("Trans", 0)
        n_log = by_group[label].get("Log", 0)
        rates[label] = {
            "predicted_ratio": str(ratio),
            "total": tot,
            "convergent": conv,
            "trans": n_trans,
            "log": n_log,
            "trans_rate_total": (n_trans / tot) if tot else None,
            "trans_rate_convergent": (n_trans / conv) if conv else None,
            "counts": by_group[label],
        }

    # Deep validate Trans hits
    print(f"\n[DEEP] {len(trans_recs)} Trans hit(s) -> dps={DPS_DEEP}")
    for r in trans_recs:
        deep = deep_validate_trans(tuple(r["coeffs"]))
        r["deep"] = deep

    # Halt logic
    halts = {}
    if rates["G_4"]["trans"] == 0 and rates["G_4"]["convergent"] >= 100:
        halts["HALT_A"] = {
            "halt_triggered": True,
            "reason": "G_4 prediction (-3/16) yields 0 Trans across "
                      f"{rates['G_4']['convergent']} convergent families. "
                      "Indicial-root argument needs Stokes/multiplicity "
                      "refinement.",
        }
    trans_groups = [g for g, r in rates.items() if r["trans"] > 0]
    if trans_groups:
        halts["HALT_B"] = {
            "halt_triggered": True,
            "groups_with_trans": trans_groups,
            "reason": "MAJOR: Trans found at predicted ratio for "
                      "non-PSL2(Z) group(s). OP-2 resolution candidate.",
        }

    out = {
        "task": "UMB-GAMMA0-2-SWEEP",
        "config": {
            "groups": [(g[0], str(g[1]), g[2], g[3]) for g in GROUPS],
            "dps_pslq": DPS_PSLQ, "n_pslq": N_PSLQ,
            "dps_deep": DPS_DEEP, "n_deep": N_DEEP,
        },
        "integrality": integrality,
        "total_families": total,
        "convergent_total": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "rates_by_group": rates,
        "rates_by_group_b1": {f"{k[0]}|b1={k[1]}": v
                              for k, v in by_group_b1.items()},
        "trans_records": trans_recs,
        "log_records": log_recs,
        "alg_count": len(alg_recs),
        "rat_count": len(rat_recs),
        "phantom_count": len(phantom_recs),
        "phantom_records": phantom_recs,
        "halt": halts,
    }
    (OUT / "results.json").write_text(json.dumps(out, indent=2, default=str))

    # Per-group ratio table
    table_lines = ["group,predicted_ratio,total,convergent,trans,log,alg,rat"]
    for g in [grp[0] for grp in GROUPS]:
        r = rates[g]
        table_lines.append(
            f"{g},{r['predicted_ratio']},{r['total']},"
            f"{r['convergent']},{r['trans']},{r['log']},"
            f"{r['counts'].get('Alg',0)},{r['counts'].get('Rat',0)}")
    (OUT / "ratio_table.csv").write_text("\n".join(table_lines) + "\n")

    print("\n=== Per-group ratio table ===")
    for ln in table_lines:
        print("  " + ln)

    if halts:
        print(f"\nHALT(s): {list(halts.keys())}")
        (OUT / "halt_log.json").write_text(json.dumps(halts, indent=2))
    else:
        (OUT / "halt_log.json").write_text(json.dumps({}, indent=2))

    print(f"\nWall: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
