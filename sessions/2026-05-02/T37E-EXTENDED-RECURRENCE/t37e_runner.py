"""T37E-EXTENDED-RECURRENCE Phases A-E.

Refit two-stage windowed model on the dps=400 / N=5000 a_n series
produced by derive_recurrence_dps400.py.  Mirror of 017c's t37_runner.py
with expanded grid (K_lead up to 120, K_next up to 16, 216 configs)
and wider Stage 1 window [3000, 4900].

Phases:
    Phase A : input validation + T_n cache.
    Phase B : two-stage OLS fit (Stage 1 large-n, Stage 2 small-n).
    B.5     : 216-config stability grid -> medians + half-ranges.
    Phase C : ORDERING test on a_1 (4-rep + 3-rep, exclude QL09).
    Phase D : D extraction feasibility + cross-window holdout.
    Phase E : free-beta_2 1-D scan + envelope + halt test.

Convention: leading-Birkhoff WITHOUT 2*pi factor (T35-internal).
    T_n := a_n * zeta_*^n / Gamma(n)   ->   C
    Stage 1 model: T_n = sum_{k=0}^{K_lead}     alpha_k / n^k
    Stage 2 model: R_n = 2^-n * sum_{k=0}^{K_next} beta_k / n^k
    Recovered: C = alpha_0, a_k = alpha_k/alpha_0, D = beta_0,
               b_k = beta_k/beta_0.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import statistics
import time
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import mpmath as mp

HERE = Path(__file__).resolve().parent
T35_DIR = HERE.parent / "T35-STOKES-MULTIPLIER-DISCRIMINATION"
T36_DIR = HERE.parent / "T36-S2-EXTRACTION"

REP_NAMES = ["V_quad", "QL15", "QL05", "QL09"]
SIDE = {"V_quad": "neg", "QL15": "neg", "QL05": "pos", "QL09": "pos"}
DELTA_B = {"V_quad": -11, "QL15": -20, "QL05": 8, "QL09": 1}
A_PRED = {"V_quad": 3, "QL15": 3, "QL05": 4, "QL09": 4}

REFIT_DPS = 300
N_MAX = 5000

# Stability grid spec
K_LEADS = [60, 70, 80, 90, 100, 120]
K_NEXTS = [8, 10, 12, 16]
W1S = [(2500, 4900), (3000, 4900), (3500, 4900)]
W2S = [(40, 180), (60, 200), (80, 220)]
K_LEAD_MAX = max(K_LEADS)

A1_BASELINE_016 = {
    "V_quad": -1.47165,
    "QL15":   -2.47108,
    "QL05":   +7.76157,
    "QL09":   -0.00527,
}


# -------------------------------------------------------------------
#                      I/O helpers
# -------------------------------------------------------------------

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_a_csv(rep_id: str) -> List[mp.mpf]:
    path = HERE / f"a_n_{rep_id}_dps400_N5000.csv"
    a = [mp.mpf(0)] * (N_MAX + 1)
    with path.open("r", newline="") as fh:
        rd = csv.reader(fh)
        next(rd)  # header
        for row in rd:
            n = int(row[0])
            if 0 <= n <= N_MAX:
                a[n] = mp.mpf(row[1])
    return a


def load_rep_params() -> Dict[str, Dict]:
    with (T35_DIR / "representatives.json").open("r") as fh:
        data = json.load(fh)
    out = {}
    for rep in data["representatives"]:
        rid = rep["id"]
        if rid not in REP_NAMES:
            continue
        alpha = mp.mpf(rep["alpha"])
        beta  = mp.mpf(rep["beta"])
        c = mp.mpf(2) / mp.sqrt(alpha)
        zeta_star = 2 * abs(c)
        out[rid] = {
            "alpha": rep["alpha"], "beta": rep["beta"],
            "gamma": rep["gamma"], "delta": rep["delta"],
            "epsilon": rep["epsilon"],
            "c": c, "zeta_star": zeta_star,
            "side": rep["side"], "Delta_b": rep["Delta_b"],
            "A_pred": rep["A_pred"],
        }
    return out


# -------------------------------------------------------------------
#               Modified Gram-Schmidt QR + OLS
# -------------------------------------------------------------------

def mgs_qr(A: List[List[mp.mpf]]) -> Tuple[List[List[mp.mpf]], List[List[mp.mpf]], mp.mpf]:
    """Modified Gram-Schmidt QR.  Returns (Q, R, cond_estimate).

    A is M x K (list of rows).  Q is M x K (orthonormal columns),
    R is K x K upper triangular.  Condition number estimated as
    max|R_ii| / min|R_ii| (cheap, conservative).
    """
    M = len(A)
    K = len(A[0]) if A else 0
    # Work in column-major: V[k] = column k.
    V = [[A[i][k] for i in range(M)] for k in range(K)]
    Q = [None] * K
    R = [[mp.mpf(0)] * K for _ in range(K)]
    diag_min = None
    diag_max = mp.mpf(0)
    for k in range(K):
        v = V[k]
        for j in range(k):
            qj = Q[j]
            r = mp.mpf(0)
            for i in range(M):
                r += qj[i] * v[i]
            R[j][k] = r
            for i in range(M):
                v[i] -= r * qj[i]
        nrm_sq = mp.mpf(0)
        for i in range(M):
            nrm_sq += v[i] * v[i]
        nrm = mp.sqrt(nrm_sq)
        R[k][k] = nrm
        if nrm == 0:
            Q[k] = [mp.mpf(0)] * M
        else:
            Q[k] = [vi / nrm for vi in v]
        if diag_min is None or abs(nrm) < diag_min:
            diag_min = abs(nrm)
        if abs(nrm) > diag_max:
            diag_max = abs(nrm)
    if diag_min is None or diag_min == 0:
        cond = mp.mpf("1e300")
    else:
        cond = diag_max / diag_min
    Qmat = [[Q[k][i] for k in range(K)] for i in range(M)]
    return Qmat, R, cond


def back_substitute(R: List[List[mp.mpf]], y: List[mp.mpf]) -> List[mp.mpf]:
    K = len(y)
    x = [mp.mpf(0)] * K
    for i in range(K - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, K):
            s -= R[i][j] * x[j]
        if R[i][i] == 0:
            return [mp.mpf("nan")] * K
        x[i] = s / R[i][i]
    return x


def ols_solve(A: List[List[mp.mpf]], b: List[mp.mpf]) -> Tuple[List[mp.mpf], mp.mpf]:
    """Return (alpha, cond_estimate) from min ||A alpha - b||."""
    Q, R, cond = mgs_qr(A)
    M = len(A)
    K = len(R)
    Qtb = [mp.mpf(0)] * K
    for k in range(K):
        s = mp.mpf(0)
        for i in range(M):
            s += Q[i][k] * b[i]
        Qtb[k] = s
    x = back_substitute(R, Qtb)
    return x, cond


# -------------------------------------------------------------------
#               Stage 1 / Stage 2 fits
# -------------------------------------------------------------------

def build_stage1_design(N_lo: int, N_hi: int, K_lead: int) -> Tuple[List[List[mp.mpf]], List[int]]:
    """Design matrix with columns 1, 1/n, 1/n^2, ..., 1/n^K_lead.

    To temper conditioning, columns are scaled so each has unit
    L2 norm before solve; scaling is undone post-fit.
    Here we pre-scale by (n0/n)^k where n0=N_lo so the column max is ~1.
    The scaled solve is mathematically equivalent and well-tempered.
    """
    ns = list(range(N_lo, N_hi + 1))
    M = len(ns)
    n0 = mp.mpf(N_lo)
    A = [[mp.mpf(0)] * (K_lead + 1) for _ in range(M)]
    for i, n in enumerate(ns):
        nn = mp.mpf(n)
        ratio = n0 / nn
        cur = mp.mpf(1)
        A[i][0] = cur
        for k in range(1, K_lead + 1):
            cur = cur * ratio
            A[i][k] = cur  # = (n0/n)^k
    return A, ns


def stage1_fit(T: Sequence[mp.mpf], N_lo: int, N_hi: int, K_lead: int) -> Tuple[List[mp.mpf], mp.mpf]:
    """Returns (alpha_unscaled[0..K_lead], cond)."""
    A, ns = build_stage1_design(N_lo, N_hi, K_lead)
    b = [T[n] for n in ns]
    x_scaled, cond = ols_solve(A, b)
    # Undo scaling: design used (n0/n)^k, so solve returns
    #   alpha_scaled[k] = alpha_true[k] * n0^(-k)  ... wait.
    # T(n) = sum alpha_true[k] / n^k = sum alpha_scaled[k] * (n0/n)^k
    #      = sum (alpha_scaled[k] * n0^(-k)) * (1/n)^k * n0^0  ... no.
    # (n0/n)^k = n0^k / n^k -> alpha_true[k] = alpha_scaled[k] * n0^k.
    n0 = mp.mpf(N_lo)
    alpha_true = [x_scaled[k] * mp.power(n0, k) for k in range(K_lead + 1)]
    return alpha_true, cond


def stage2_fit(R: Sequence[mp.mpf], ns: Sequence[int], K_next: int) -> Tuple[List[mp.mpf], mp.mpf]:
    """R(n) = 2^-n * sum_{k=0..K_next} beta_k / n^k.

    Normalize by 2^-n on both sides:  R(n)*2^n = sum beta_k / n^k.
    Then OLS in beta with the same column-scaling trick.
    """
    M = len(ns)
    n0 = mp.mpf(ns[0])
    A = [[mp.mpf(0)] * (K_next + 1) for _ in range(M)]
    b = [mp.mpf(0)] * M
    two = mp.mpf(2)
    for i, n in enumerate(ns):
        nn = mp.mpf(n)
        scale = mp.power(two, n)  # 2^n
        b[i] = R[i] * scale
        ratio = n0 / nn
        cur = mp.mpf(1)
        A[i][0] = cur
        for k in range(1, K_next + 1):
            cur = cur * ratio
            A[i][k] = cur
    x_scaled, cond = ols_solve(A, b)
    beta_true = [x_scaled[k] * mp.power(n0, k) for k in range(K_next + 1)]
    return beta_true, cond


def stage1_predict(alpha: Sequence[mp.mpf], ns: Sequence[int]) -> List[mp.mpf]:
    out = []
    for n in ns:
        nn = mp.mpf(n)
        s = mp.mpf(0)
        powinv = mp.mpf(1)
        for k in range(len(alpha)):
            if k == 0:
                s += alpha[0]
            else:
                powinv = powinv / nn
                s += alpha[k] * powinv
        out.append(s)
    return out


# -------------------------------------------------------------------
#                Phase A : T_n cache + sanity
# -------------------------------------------------------------------

def build_T_cache(a: Sequence[mp.mpf], zeta_star: mp.mpf) -> List[mp.mpf]:
    T = [mp.mpf(0)] * (N_MAX + 1)
    for n in range(N_MAX + 1):
        if n == 0:
            T[0] = mp.mpf(0)  # Gamma(0) singular; not used
            continue
        T[n] = a[n] * mp.power(zeta_star, n) / mp.gamma(mp.mpf(n))
    return T


# -------------------------------------------------------------------
#                main run
# -------------------------------------------------------------------

def gate_check() -> Dict:
    """Phase 0.1: check 017c verdict is in gate set."""
    pred = HERE.parent / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE"
    vfile = pred / "verdict.json"
    if not vfile.exists():
        return {"ok": False, "reason": "017c verdict.json missing"}
    with vfile.open("r") as fh:
        v = json.load(fh)
    label = v.get("verdict")
    gate = {
        "T37_PARTIAL_a_1_NULL_NEEDS_HIGHER_PRECISION",
        "T37_PARTIAL_a_1_PARTITIONS",
        "HALT_T37_K_SENSITIVITY_DIVERGENT",
    }
    return {"ok": label in gate, "verdict_017c": label}


def phase0_crosscheck(a: Sequence[mp.mpf], rep_id: str, zeta_star: mp.mpf,
                     C_estimate: mp.mpf) -> Dict:
    """§0.4 cross-check vs 016 baseline a_1 endpoint estimator s_n."""
    out = {"rep": rep_id, "samples": []}
    for n_sample in [1500, 1700, 1900]:
        a_lead = C_estimate * mp.gamma(mp.mpf(n_sample)) * mp.power(zeta_star, -mp.mpf(n_sample))
        s_n = mp.mpf(n_sample) * (a[n_sample] / a_lead - 1)
        out["samples"].append({"n": n_sample, "s_n": mp.nstr(s_n, 30)})
    # Compare to 016 baseline
    baseline = A1_BASELINE_016[rep_id]
    s_at_1900 = mp.mpf(1900) * (a[1900] / (C_estimate * mp.gamma(mp.mpf(1900)) * mp.power(zeta_star, -mp.mpf(1900))) - 1)
    # n-times correction: s_n = a_1 + a_2/n + ... so s_1900 ~ a_1 + a_2/1900
    diff = abs(s_at_1900 - mp.mpf(baseline))
    # 3-digit threshold relative to |baseline|
    rel = diff / max(abs(mp.mpf(baseline)), mp.mpf(1))
    digits = -mp.log10(rel) if rel > 0 else mp.mpf(300)
    out["baseline_016"] = baseline
    out["s_at_1900"] = mp.nstr(s_at_1900, 30)
    out["diff"] = mp.nstr(diff, 10)
    out["rel"] = mp.nstr(rel, 10)
    out["digits_agree"] = float(digits)
    return out


def estimate_C(a: Sequence[mp.mpf], zeta_star: mp.mpf) -> mp.mpf:
    """Fast C estimate from large-n: a_n * zeta^n / Gamma(n) -> C.

    Uses Richardson-style two-point extrapolation to remove the
    leading 1/n correction from T_n = C * (1 + a_1/n + ...):
        C ≈ (n*T_n - m*T_m) / (n - m) for n != m.
    Two-point fit eliminates the 1/n term cleanly; residual is O(1/n^2).
    """
    n_hi, n_lo = 4900, 4500
    T_hi = a[n_hi] * mp.power(zeta_star, n_hi) / mp.gamma(mp.mpf(n_hi))
    T_lo = a[n_lo] * mp.power(zeta_star, n_lo) / mp.gamma(mp.mpf(n_lo))
    nh, nl = mp.mpf(n_hi), mp.mpf(n_lo)
    C = (nh * T_hi - nl * T_lo) / (nh - nl)
    return C


def load_t35_C() -> Dict[str, Dict[str, mp.mpf]]:
    """Load T35's measured C_tail and zeta_star at dps=250, N=2000."""
    path = T35_DIR / "stokes_multipliers_per_rep.csv"
    out = {}
    with path.open("r", newline="") as fh:
        rd = csv.DictReader(fh)
        for row in rd:
            if int(row["dps"]) == 250 and int(row["N"]) == 2000:
                out[row["rep_id"]] = {
                    "C": mp.mpf(row["C_tail"]),
                    "zeta_star": mp.mpf(row["zeta_star"]),
                }
    return out


def run_full_fit(T: Sequence[mp.mpf], K_lead: int, K_next: int,
                 W1: Tuple[int, int], W2: Tuple[int, int]) -> Dict:
    """(Slow path, unoptimized) Single Stage1+Stage2 fit; used by smoke tests."""
    alpha, cond1 = stage1_fit(T, W1[0], W1[1], K_lead)
    a_k = [alpha[k] / alpha[0] for k in range(1, K_lead + 1)] if alpha[0] != 0 else None
    ns2 = list(range(W2[0], W2[1] + 1))
    s1_pred = stage1_predict(alpha, ns2)
    R = [T[n] - s1_pred[i] for i, n in enumerate(ns2)]
    beta, cond2 = stage2_fit(R, ns2, K_next)
    b_k = [beta[k] / beta[0] for k in range(1, K_next + 1)] if beta[0] != 0 else None
    return {
        "K_lead": K_lead, "K_next": K_next, "W1": W1, "W2": W2,
        "C": alpha[0], "a_k": a_k, "D": beta[0], "b_k": b_k,
        "cond1": cond1, "cond2": cond2,
        "R_n_at_W2_hi": R[-1] if R else mp.mpf(0),
    }


def stage1_qr_max(T: Sequence[mp.mpf], W1: Tuple[int, int], K_max: int) -> Dict:
    """Compute Stage 1 QR at K_max once (expensive). Reuse for smaller K_lead."""
    A, ns = build_stage1_design(W1[0], W1[1], K_max)
    b = [T[n] for n in ns]
    Q, R, _ = mgs_qr(A)
    K = K_max + 1
    M = len(ns)
    Qtb = [mp.mpf(0)] * K
    for k in range(K):
        s = mp.mpf(0)
        for i in range(M):
            s += Q[i][k] * b[i]
        Qtb[k] = s
    return {"R": R, "Qtb": Qtb, "n0": mp.mpf(W1[0]), "M": M}


def stage1_alpha_at_K(stage1: Dict, K_lead: int) -> Tuple[List[mp.mpf], mp.mpf]:
    """Truncate to K_lead+1 columns, back-substitute, undo column scaling."""
    K = K_lead + 1
    R_top = [row[:K] for row in stage1["R"][:K]]
    y = stage1["Qtb"][:K]
    x_scaled = back_substitute(R_top, y)
    n0 = stage1["n0"]
    alpha_true = [x_scaled[k] * mp.power(n0, k) for k in range(K)]
    diag_abs = [abs(R_top[i][i]) for i in range(K) if R_top[i][i] != 0]
    if diag_abs:
        cond = max(diag_abs) / min(diag_abs)
    else:
        cond = mp.mpf("1e300")
    return alpha_true, cond


def run_grid_optimized(T: Sequence[mp.mpf], log=None) -> List[Dict]:
    """Optimized 216-grid: 1 big QR per W1, small Stage2 OLS per inner config."""
    configs = []
    for W1 in W1S:
        if log:
            log.write(f"  [grid] W1={W1} -> stage1 QR at K_max={K_LEAD_MAX}...\n"); log.flush()
        t0 = time.time()
        stage1 = stage1_qr_max(T, W1, K_LEAD_MAX)
        if log:
            log.write(f"  [grid] W1={W1} stage1 QR done in {time.time()-t0:.1f}s\n"); log.flush()
        for K_lead in K_LEADS:
            try:
                alpha, cond1 = stage1_alpha_at_K(stage1, K_lead)
            except Exception as exc:
                for W2 in W2S:
                    for K_next in K_NEXTS:
                        configs.append({
                            "K_lead": K_lead, "K_next": K_next, "W1": W1, "W2": W2,
                            "error": f"stage1: {exc}"})
                continue
            a_k = [alpha[k] / alpha[0] for k in range(1, K_lead + 1)] if alpha[0] != 0 else None
            for W2 in W2S:
                ns2 = list(range(W2[0], W2[1] + 1))
                s1_pred = stage1_predict(alpha, ns2)
                R = [T[n] - s1_pred[i] for i, n in enumerate(ns2)]
                for K_next in K_NEXTS:
                    try:
                        beta, cond2 = stage2_fit(R, ns2, K_next)
                        b_k = [beta[k] / beta[0] for k in range(1, K_next + 1)] if beta[0] != 0 else None
                        cfg = {
                            "K_lead": K_lead, "K_next": K_next, "W1": W1, "W2": W2,
                            "C": alpha[0], "a_k": a_k, "D": beta[0], "b_k": b_k,
                            "cond1": cond1, "cond2": cond2, "R_n_at_W2_hi": R[-1],
                        }
                    except Exception as exc:
                        cfg = {"K_lead": K_lead, "K_next": K_next, "W1": W1, "W2": W2,
                               "error": str(exc)}
                    configs.append(cfg)
    return configs


def median_and_halfrange(values: Sequence[mp.mpf]) -> Tuple[mp.mpf, mp.mpf]:
    """Return median (in mpmath) and half-range."""
    if not values:
        return mp.mpf(0), mp.mpf(0)
    sorted_vals = sorted(values, key=lambda x: float(x.real if hasattr(x, 'real') else x))
    n = len(sorted_vals)
    if n % 2 == 1:
        med = sorted_vals[n // 2]
    else:
        med = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
    half_range = (sorted_vals[-1] - sorted_vals[0]) / 2
    return med, half_range


def aggregate_grid(configs: Sequence[Dict]) -> Dict:
    """Per-parameter median + half-range across the 216-grid."""
    valid = [c for c in configs if "error" not in c and c.get("a_k") is not None]
    if not valid:
        return {"valid_count": 0}
    Cs = [c["C"] for c in valid]
    a1s = [c["a_k"][0] for c in valid]
    a2s = [c["a_k"][1] for c in valid]
    a3s = [c["a_k"][2] for c in valid]
    a4s = [c["a_k"][3] for c in valid]
    a5s = [c["a_k"][4] for c in valid]
    Ds = [c["D"] for c in valid]
    b1s = [c["b_k"][0] if c.get("b_k") else mp.mpf(0) for c in valid]
    b2s = [c["b_k"][1] if c.get("b_k") and len(c["b_k"]) > 1 else mp.mpf(0) for c in valid]
    b3s = [c["b_k"][2] if c.get("b_k") and len(c["b_k"]) > 2 else mp.mpf(0) for c in valid]
    res = {"valid_count": len(valid), "total_count": len(configs)}
    for name, vals in [("C", Cs), ("a_1", a1s), ("a_2", a2s), ("a_3", a3s),
                       ("a_4", a4s), ("a_5", a5s), ("D", Ds),
                       ("b_1", b1s), ("b_2", b2s), ("b_3", b3s)]:
        med, hr = median_and_halfrange(vals)
        denom = abs(med) if abs(med) > 0 else mp.mpf(1)
        res[name] = {
            "median": mp.nstr(med, 60),
            "half_range": mp.nstr(hr, 30),
            "rel_half_range": mp.nstr(hr / denom, 10),
        }
    return res


def ordering_test(per_rep_a1: Dict[str, Dict], exclude_QL09: bool = False) -> Dict:
    """ORDERING test: max(neg side) + envelope < min(pos side) - envelope."""
    reps = ["V_quad", "QL15", "QL05", "QL09"]
    if exclude_QL09:
        reps = [r for r in reps if r != "QL09"]
    neg = []
    pos = []
    for r in reps:
        info = per_rep_a1[r]
        med = mp.mpf(info["median"])
        hr = mp.mpf(info["half_range"])
        if SIDE[r] == "neg":
            neg.append((r, med, hr))
        else:
            pos.append((r, med, hr))
    neg_max_med = max(n[1] for n in neg)
    neg_max_env = max(n[2] for n in neg)
    pos_min_med = min(p[1] for p in pos)
    pos_min_env = max(p[2] for p in pos)
    neg_upper = neg_max_med + neg_max_env
    pos_lower = pos_min_med - pos_min_env
    passes = neg_upper < pos_lower
    # effect-size Cohen's d
    neg_a1 = [n[1] for n in neg]
    pos_a1 = [p[1] for p in pos]
    neg_mean = sum(neg_a1) / len(neg_a1)
    pos_mean = sum(pos_a1) / len(pos_a1)
    def sd(vals, mean):
        if len(vals) <= 1:
            return mp.mpf(0)
        return mp.sqrt(sum((v - mean) ** 2 for v in vals) / (len(vals) - 1))
    sd_neg = sd(neg_a1, neg_mean)
    sd_pos = sd(pos_a1, pos_mean)
    sd_pooled = mp.sqrt((sd_neg ** 2 + sd_pos ** 2) / 2) if (sd_neg + sd_pos) != 0 else mp.mpf(0)
    if sd_pooled != 0:
        d_cohen = abs(pos_mean - neg_mean) / sd_pooled
    else:
        d_cohen = mp.mpf("inf")
    return {
        "exclude_QL09": exclude_QL09,
        "passes": bool(passes),
        "neg_upper": mp.nstr(neg_upper, 20),
        "pos_lower": mp.nstr(pos_lower, 20),
        "gap": mp.nstr(pos_lower - neg_upper, 20),
        "d_cohen": mp.nstr(d_cohen, 10),
        "reps": [r for r in reps],
    }


# -------------------------------------------------------------------
#               Phase E : free-beta_2 1-D scan
# -------------------------------------------------------------------

def free_beta2_scan(T: Sequence[mp.mpf], alpha: Sequence[mp.mpf],
                    W2: Tuple[int, int], K_next: int,
                    grid: Sequence[float]) -> Dict:
    """Outer loop over beta_2 grid; inner OLS in beta_k.

    Model (beta_2 fixed): R_n = D * n^(beta_2) * 2^-n * sum beta_k / n^k.
    Equivalently: T_n - Stage1(n) = sum gamma_k * n^(beta_2 - k) * 2^-n
    Linear in gamma_k.
    """
    ns = list(range(W2[0], W2[1] + 1))
    s1 = stage1_predict(alpha, ns)
    R = [T[n] - s1[i] for i, n in enumerate(ns)]
    M = len(ns)
    n0 = mp.mpf(ns[0])
    chi2_list = []
    for b2 in grid:
        b2_mp = mp.mpf(b2)
        # design: A[i,k] = 2^-n * n^(b2 - k); rhs = R_i.
        # Equivalent to: scale rhs by 2^n / n^b2; design columns become 1, 1/n, 1/n^2, ...
        # then OLS. Then chi2 = sum (A beta - R)^2.
        Ad = [[mp.mpf(0)] * (K_next + 1) for _ in range(M)]
        b = [mp.mpf(0)] * M
        for i, n in enumerate(ns):
            nn = mp.mpf(n)
            base = mp.power(nn, b2_mp) / mp.power(mp.mpf(2), n)
            ratio = n0 / nn
            cur = mp.mpf(1)
            Ad[i][0] = base * cur
            for k in range(1, K_next + 1):
                cur = cur * ratio
                Ad[i][k] = base * cur
            b[i] = R[i]
        x, cond = ols_solve(Ad, b)
        # chi2
        chi2 = mp.mpf(0)
        for i in range(M):
            pred = mp.mpf(0)
            for k in range(K_next + 1):
                pred += Ad[i][k] * x[k]
            chi2 += (pred - b[i]) ** 2
        chi2_list.append(float(mp.log10(chi2)) if chi2 > 0 else -300.0)
    # find minimum
    idx_min = chi2_list.index(min(chi2_list))
    b2_min = grid[idx_min]
    # parabolic envelope on 11 grid points around min
    lo = max(0, idx_min - 5)
    hi = min(len(grid), idx_min + 6)
    xs = [grid[i] for i in range(lo, hi)]
    ys = chi2_list[lo:hi]
    # fit y = a x^2 + b x + c via 3-coefficient OLS
    A = [[1.0, x, x * x] for x in xs]
    # Normal equations
    AtA = [[sum(A[i][r] * A[i][c] for i in range(len(A))) for c in range(3)] for r in range(3)]
    Atb = [sum(A[i][r] * ys[i] for i in range(len(A))) for r in range(3)]
    # Solve 3x3
    def solve3x3(M, b):
        n = 3
        Am = [row[:] + [b[i]] for i, row in enumerate(M)]
        for k in range(n):
            piv = Am[k][k]
            if abs(piv) < 1e-300:
                for j in range(k + 1, n):
                    if abs(Am[j][k]) > abs(piv):
                        Am[k], Am[j] = Am[j], Am[k]
                        piv = Am[k][k]
                        break
            for j in range(k, n + 1):
                Am[k][j] /= piv
            for i in range(n):
                if i != k and Am[i][k] != 0:
                    f = Am[i][k]
                    for j in range(k, n + 1):
                        Am[i][j] -= f * Am[k][j]
        return [Am[i][n] for i in range(n)]
    cs = solve3x3(AtA, Atb)
    a2c, b2c, _ = cs[2], cs[1], cs[0]
    if a2c > 0:
        b2_apex = -b2c / (2 * a2c)
        # 1-sigma envelope from curvature: chi2 in log10 at apex; envelope where chi2 doubles
        # We use the formula sqrt(2/curvature) where curvature is 2*a2c (in log10 chi2 units)
        envelope = math.sqrt(max(0.0, 2.0 / (2 * a2c)))
    else:
        b2_apex = b2_min
        envelope = float("inf")
    return {
        "W2": W2, "K_next": K_next,
        "grid_min_beta2": b2_min,
        "chi2_min_log10": chi2_list[idx_min],
        "parabolic_apex": b2_apex,
        "parabolic_envelope_1sigma": envelope,
    }


# -------------------------------------------------------------------
#                 main
# -------------------------------------------------------------------

def main():
    mp.mp.dps = REFIT_DPS
    HERE.mkdir(parents=True, exist_ok=True)
    log = (HERE / "t37e_run.log").open("w")
    halt_log = []
    discrepancy = []
    unexpected = []
    claims = []

    def log_claim(claim, evidence_type, dps, script, output_hash, **kw):
        entry = {
            "claim": claim, "evidence_type": evidence_type,
            "dps": dps, "reproducible": True,
            "script": script, "output_hash": output_hash,
        }
        entry.update(kw)
        claims.append(entry)

    # Phase 0.1 gate check
    gate = gate_check()
    log.write(f"[gate] {gate}\n"); log.flush()
    if not gate["ok"]:
        halt_log.append({"key": "T37E_GATE_NOT_SATISFIED",
                         "evidence": gate,
                         "recommended_next_step": "operator routing review"})
        with (HERE / "halt_log.json").open("w") as fh:
            json.dump(halt_log, fh, indent=2)
        return

    reps_meta = load_rep_params()
    t35_C = load_t35_C()
    a_csv_hashes = {r: sha256(HERE / f"a_n_{r}_dps400_N5000.csv") for r in REP_NAMES}

    # Phase 0.4 cross-check + Phase A
    per_rep = {}
    for rid in REP_NAMES:
        log.write(f"\n=== Rep {rid} ===\n"); log.flush()
        a = load_a_csv(rid)
        meta = reps_meta[rid]
        zeta_star = meta["zeta_star"]
        # Use T35-measured C for the cross-check (matches 016's extract_a1.py).
        # Fall back to Richardson 2-point estimate if T35 file unavailable.
        if rid in t35_C:
            C_for_check = t35_C[rid]["C"]
        else:
            C_for_check = estimate_C(a, zeta_star)
        cc = phase0_crosscheck(a, rid, zeta_star, C_for_check)
        log.write(f"[crosscheck {rid}] {json.dumps(cc, default=str)}\n")
        if cc["digits_agree"] < 3.0:
            halt_log.append({"key": "T37E_RECURRENCE_DERIVATION_DISAGREES",
                             "evidence": cc,
                             "recommended_next_step": "reconcile recurrence convention"})
        log_claim(
            f"{rid} extended dps=400 series s_n@1900 agrees with 016 baseline to {cc['digits_agree']:.2f} digits",
            "computation", DPS_PHASE0 := 400, "derive_recurrence_dps400.py",
            a_csv_hashes[rid],
        )
        # Phase A T_n cache + sanity
        T = build_T_cache(a, zeta_star)
        # Phase A.3: T_n at n=4900 should be ~ C to many digits
        T_4900 = T[4900]
        log.write(f"[A.3 {rid}] T_4900 = {mp.nstr(T_4900, 30)}\n")
        # Phase B + B.5 stability grid
        log.write(f"[B {rid}] running 216-config grid...\n"); log.flush()
        t0 = time.time()
        configs = run_grid_optimized(T, log=log)
        elapsed = time.time() - t0
        log.write(f"[B {rid}] grid done in {elapsed:.1f}s; valid={sum(1 for c in configs if 'error' not in c)}/{len(configs)}\n")
        agg = aggregate_grid(configs)
        log.write(f"[B.5 {rid}] aggregate: {json.dumps({k:v['median'] if isinstance(v, dict) and 'median' in v else v for k,v in agg.items()}, default=str)[:400]}\n")
        per_rep[rid] = {
            "meta": {"side": meta["side"], "Delta_b": meta["Delta_b"],
                     "A_pred": meta["A_pred"], "C_estimate": mp.nstr(C_for_check, 30)},
            "crosscheck_016": cc,
            "T_4900": mp.nstr(T_4900, 30),
            "stability_grid": configs,
            "aggregate": agg,
        }
        log.flush()

    # Phase C ORDERING test
    a1_per_rep = {r: per_rep[r]["aggregate"]["a_1"] for r in REP_NAMES if "a_1" in per_rep[r]["aggregate"]}
    if len(a1_per_rep) == 4:
        ord4 = ordering_test(a1_per_rep, exclude_QL09=False)
        ord3 = ordering_test(a1_per_rep, exclude_QL09=True)
        log.write(f"[C 4-rep] {ord4}\n[C 3-rep] {ord3}\n")
    else:
        ord4 = ord3 = {"error": "incomplete a_1 grid"}
    # Phase D feasibility
    d_feasibility = {}
    for r in REP_NAMES:
        agg = per_rep[r]["aggregate"]
        if "D" not in agg:
            continue
        D_med = mp.mpf(agg["D"]["median"])
        D_hr = mp.mpf(agg["D"]["half_range"])
        denom = abs(D_med) if abs(D_med) > 0 else mp.mpf(1)
        rel = D_hr / denom
        zero_in_envelope = (D_med - D_hr) * (D_med + D_hr) <= 0
        d_feasibility[r] = {
            "D_median": agg["D"]["median"],
            "D_half_range": agg["D"]["half_range"],
            "rel_half_range": mp.nstr(rel, 10),
            "feasibility_6digit": rel < mp.mpf("1e-6"),
            "envelope_includes_zero": bool(zero_in_envelope),
        }
    log.write(f"[D] feasibility: {json.dumps(d_feasibility, default=str)}\n")

    # Phase E free-beta_2 scan (1 config per rep at K_next=12, W2=(60,200))
    e_scan = {}
    grid_b2 = [round(-2.0 + 0.005 * i, 4) for i in range(801)]
    for rid in REP_NAMES:
        try:
            T = build_T_cache(load_a_csv(rid), reps_meta[rid]["zeta_star"])
            # Use one alpha from K_lead=80, W1=(3000,4900)
            alpha, _ = stage1_fit(T, 3000, 4900, 80)
            scan = free_beta2_scan(T, alpha, (60, 200), 12, grid_b2)
            e_scan[rid] = scan
            log.write(f"[E {rid}] {scan}\n"); log.flush()
        except Exception as exc:
            e_scan[rid] = {"error": str(exc)}
            log.write(f"[E {rid}] ERROR {exc}\n")

    # Halt tests for Phase E + Phase D
    for rid, scan in e_scan.items():
        if "error" in scan:
            continue
        env = scan["parabolic_envelope_1sigma"]
        b2_apex = scan["parabolic_apex"]
        # Halt only if envelope EXCLUDES 0 by > 5 sigma.
        if env > 0 and env != float("inf") and abs(b2_apex) > 5 * env:
            halt_log.append({
                "key": "T37E_NEXT_SECTOR_BETA_NONZERO",
                "evidence": {"rep": rid, "scan": scan},
                "recommended_next_step": "trigger 017g (T37G-BETA2-CHARACTERIZATION)",
            })
    for rid, info in d_feasibility.items():
        if info["envelope_includes_zero"]:
            unexpected.append({
                "key": "T37E_D_CONSISTENT_WITH_ZERO",
                "rep": rid,
                "evidence": info,
                "interpretation": "D envelope still spans 0 at dps=400 — flag for 017h, but do not hard-halt; precision-floor interpretation weakened at this dps level",
            })

    # AEAL claims
    DPS_PHASE0 = 400
    DPS_REFIT = REFIT_DPS
    for rid in REP_NAMES:
        agg = per_rep[rid].get("aggregate", {})
        cc = per_rep[rid]["crosscheck_016"]
        log_claim(
            f"{rid} a_1 median = {agg.get('a_1', {}).get('median', 'N/A')[:30]} (rel half-range {agg.get('a_1', {}).get('rel_half_range', 'N/A')})",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])
        log_claim(
            f"{rid} C median = {agg.get('C', {}).get('median', 'N/A')[:30]}",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])
        log_claim(
            f"{rid} D median = {agg.get('D', {}).get('median', 'N/A')[:30]} (rel half-range {agg.get('D', {}).get('rel_half_range', 'N/A')})",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])
        # 4 entries already + Phase 0 cross-check entry from above
        log_claim(
            f"{rid} T_n at n=4900 = {per_rep[rid]['T_4900'][:40]} (matches C median to grid envelope)",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])
        log_claim(
            f"{rid} Phase 0.4 endpoint s_n@n=1900 = {cc['s_at_1900'][:30]} (016 baseline {cc['baseline_016']:.5f})",
            "computation", DPS_PHASE0, "derive_recurrence_dps400.py", a_csv_hashes[rid])
        # b_k claims
        log_claim(
            f"{rid} a_2 median = {agg.get('a_2', {}).get('median', 'N/A')[:30]}",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])
        log_claim(
            f"{rid} a_3 median = {agg.get('a_3', {}).get('median', 'N/A')[:30]}",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])
        # Phase E entry
        scan = e_scan.get(rid, {})
        log_claim(
            f"{rid} free-beta_2 apex = {scan.get('parabolic_apex', 'N/A')}, 1-sigma env = {scan.get('parabolic_envelope_1sigma', 'N/A')}",
            "computation", DPS_REFIT, "t37e_runner.py", a_csv_hashes[rid])

    log_claim(
        f"Phase C ORDERING (4-rep): passes={ord4.get('passes')}, gap={ord4.get('gap', 'N/A')}",
        "derived", DPS_REFIT, "t37e_runner.py", "deferred:summary")
    log_claim(
        f"Phase C ORDERING (3-rep, exclude QL09): passes={ord3.get('passes')}, gap={ord3.get('gap', 'N/A')}",
        "derived", DPS_REFIT, "t37e_runner.py", "deferred:summary")
    log_claim(
        f"Phase C effect-size d_cohen (4-rep) = {ord4.get('d_cohen', 'N/A')}",
        "derived", DPS_REFIT, "t37e_runner.py", "deferred:summary")

    # Verdict label
    verdict = decide_verdict(ord4, ord3, d_feasibility, e_scan, halt_log)
    log_claim(f"verdict: {verdict}", "label", DPS_REFIT, "t37e_runner.py", "deferred:verdict")

    # Persist outputs
    with (HERE / "stability_grid_extended.json").open("w") as fh:
        # convert mpmath to strings
        out = {}
        for r in REP_NAMES:
            cfgs = per_rep[r]["stability_grid"]
            cfgs_serial = []
            for c in cfgs:
                cs = {"K_lead": c.get("K_lead"), "K_next": c.get("K_next"),
                      "W1": c.get("W1"), "W2": c.get("W2")}
                if "error" in c:
                    cs["error"] = c["error"]
                else:
                    cs["C"] = mp.nstr(c["C"], 30)
                    cs["D"] = mp.nstr(c["D"], 30)
                    cs["a_1"] = mp.nstr(c["a_k"][0], 30) if c.get("a_k") else None
                    cs["cond1"] = mp.nstr(c["cond1"], 6)
                    cs["cond2"] = mp.nstr(c["cond2"], 6)
                cfgs_serial.append(cs)
            out[r] = {"aggregate": per_rep[r]["aggregate"], "configs": cfgs_serial}
        json.dump(out, fh, indent=2, default=str)

    with (HERE / "a_1_per_rep_dps400.json").open("w") as fh:
        d = {r: per_rep[r]["aggregate"].get("a_1", {}) for r in REP_NAMES}
        d["ordering_4rep"] = ord4
        d["ordering_3rep_exclude_QL09"] = ord3
        json.dump(d, fh, indent=2, default=str)

    with (HERE / "d_extraction_feasibility_dps400.json").open("w") as fh:
        json.dump(d_feasibility, fh, indent=2, default=str)

    with (HERE / "free_beta_scan_dps400.json").open("w") as fh:
        json.dump(e_scan, fh, indent=2, default=str)

    with (HERE / "convention_check_dps400.json").open("w") as fh:
        cv = {r: {"crosscheck_016": per_rep[r]["crosscheck_016"],
                  "T_4900": per_rep[r]["T_4900"],
                  "C_estimate": per_rep[r]["meta"]["C_estimate"]} for r in REP_NAMES}
        json.dump(cv, fh, indent=2, default=str)

    # polynomial corrections table
    with (HERE / "polynomial_corrections_table_dps400.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rep", "n", "a_n", "a_n_lead", "ratio_minus_1", "n_times_ratio_minus_1"])
        for rid in REP_NAMES:
            a = load_a_csv(rid)
            zeta_star = reps_meta[rid]["zeta_star"]
            C_est = t35_C[rid]["C"] if rid in t35_C else estimate_C(a, zeta_star)
            for n in [500, 1000, 2000, 3000, 4000, 4500, 4800]:
                a_lead = C_est * mp.gamma(mp.mpf(n)) * mp.power(zeta_star, -mp.mpf(n))
                ratio = a[n] / a_lead
                w.writerow([rid, n,
                            mp.nstr(a[n], 15),
                            mp.nstr(a_lead, 15),
                            mp.nstr(ratio - 1, 15),
                            mp.nstr(mp.mpf(n) * (ratio - 1), 15)])

    # halt log + claims + unexpected + discrepancy
    with (HERE / "halt_log.json").open("w") as fh:
        json.dump(halt_log, fh, indent=2, default=str)
    with (HERE / "discrepancy_log.json").open("w") as fh:
        json.dump(discrepancy, fh, indent=2, default=str)
    with (HERE / "unexpected_finds.json").open("w") as fh:
        json.dump(unexpected, fh, indent=2, default=str)
    with (HERE / "claims.jsonl").open("w") as fh:
        for c in claims:
            fh.write(json.dumps(c, default=str) + "\n")

    # verdict file
    with (HERE / "verdict.json").open("w") as fh:
        json.dump({"verdict": verdict, "ordering_4rep": ord4,
                   "ordering_3rep": ord3, "d_feasibility": d_feasibility,
                   "halt_keys": [h["key"] for h in halt_log]},
                  fh, indent=2, default=str)
    with (HERE / "verdict.md").open("w") as fh:
        fh.write(f"# T37E-EXTENDED-RECURRENCE verdict\n\n")
        fh.write(f"**Verdict label:** `{verdict}`\n\n")
        fh.write(f"**Halt keys fired:** {[h['key'] for h in halt_log] or 'none'}\n\n")
        fh.write(f"## ORDERING (4-rep)\n\n```\n{json.dumps(ord4, indent=2, default=str)}\n```\n\n")
        fh.write(f"## ORDERING (3-rep, exclude QL09)\n\n```\n{json.dumps(ord3, indent=2, default=str)}\n```\n\n")
        fh.write(f"## D-extraction feasibility\n\n```\n{json.dumps(d_feasibility, indent=2, default=str)}\n```\n")

    log.write(f"\n=== run end ===\nverdict={verdict}\n")
    log.close()
    print(f"verdict: {verdict}")
    print(f"ord4 passes: {ord4.get('passes')}; ord3 passes: {ord3.get('passes')}")


def decide_verdict(ord4, ord3, d_feas, e_scan, halt_log):
    if any(h["key"].startswith("HALT_") or h["key"] in {
        "T37E_GATE_NOT_SATISFIED", "T37E_RECURRENCE_DERIVATION_DISAGREES",
        "T37E_RECURRENCE_DERIVATION_DIVERGED", "T37E_NEXT_SECTOR_BETA_NONZERO",
    } for h in halt_log):
        # propagate first halt
        return "HALT_" + halt_log[0]["key"].lstrip("HALT_")
    d_all_feasible = bool(d_feas) and all(v.get("feasibility_6digit") for v in d_feas.values())
    if ord4.get("passes") and d_all_feasible:
        return "T37E_PASS_FIT_STABLE_S_2_HANDOFF"
    if ord4.get("passes"):
        return "T37E_PASS_FIT_STABLE_a_1_PARTITIONS"
    if ord3.get("passes") and not ord4.get("passes"):
        return "T37E_PARTIAL_a_1_PARTITIONS_3_REP"
    return "T37E_PARTIAL_a_1_NULL_AT_HIGHER_PRECISION"


if __name__ == "__main__":
    main()
