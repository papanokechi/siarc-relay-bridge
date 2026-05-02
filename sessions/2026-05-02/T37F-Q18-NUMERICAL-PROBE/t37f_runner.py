"""T37F-Q18-NUMERICAL-PROBE runner.

Re-derives QL09's Birkhoff formal series in the *opposite* dominant-
balance branch (c = -2/sqrt(alpha)) at dps=300, N=2000, performs the
same lead+next-rung extraction as 017c (T37-S2-EXTRACTION-POLYNOMIAL-
AWARE), and compares branch (+) vs branch (-) invariants to decide
between the "convention-shadow" interpretation (b) and the
"third-stratum" interpretation (a) of the QL09 a_1 = 0 anomaly
(017c verdict T37_PARTIAL_a_1_PARTITIONS, ql09_a1_value_float
~= -1.7e-57).

Per Phase 0 symbolic derivation
(derive_recurrence_QL09_opposite_branch.py), the recurrence

    (alpha c / 2) k a_k =
        U_{k-1}(k) a_{k-1} + U_{k-2} a_{k-2} + U_{k-3}(k) a_{k-3}

with
    U_{k-1}(k) = (2k-1)^2 alpha/16 + gamma - beta^2/(4 alpha),
    U_{k-2}    = -c delta / 2,
    U_{k-3}(k) = (2k-1) delta / 4 + epsilon - beta delta/(2 alpha),

is symbolic in c.  Branch (+) and branch (-) differ only in
sign(c) appearing in the diagonal premultiplier (alpha c / 2)
and in U_{k-2}.  At k=1 the diagonal premultiplier is the only
denominator, U_{k-2} and U_{k-3} do not contribute (k=1 < 2),
and the U_{k-1}(1) numerator bracket alpha/16 + gamma -
beta^2/(4 alpha) for QL09 evaluates to 1/8 + 1 - 9/8 = 0
exactly.  Hence a_1 = 0 in BOTH branches as an algebraic
identity, not a numerical coincidence.

This runner verifies that result numerically (Phase B fit on the
branch-(-) series should report a_1_opposite = 0 to >>30 digits)
and reports invariant comparison + classification.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import mpmath as mp


HERE = Path(__file__).resolve().parent
INPUTS = {
    "t37c_verdict": HERE.parent / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE" / "verdict.json",
    "t37c_d_extr": HERE.parent / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE" / "d_extraction_feasibility.json",
    "t35_repr": HERE.parent / "T35-STOKES-MULTIPLIER-DISCRIMINATION" / "representatives.json",
}

# QL09 family parameters (matches T35 representatives.json).
QL09 = {
    "id": "QL09", "alpha": 2, "beta": 3, "gamma": 1, "delta": 5,
    "epsilon": 0, "side": "pos", "A_pred": 4, "Delta_b": 1,
}

DPS = 300
N_TARGET = 2000
K_LEAD = 25            # 017c-measured stable optimum
W1 = (400, 1900)       # primary stage1 window
K_LEAD_GRID = [20, 25, 30]
W1_GRID = [(400, 1900), (600, 1900), (800, 1900)]
K_NEXT = 6
W2 = (40, 100)


# ---------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------

def file_hash(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(p: Path, obj):
    with p.open("w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, default=str)


def append_claim(claim_path: Path, claim: Dict):
    with claim_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(claim) + "\n")


# ---------------------------------------------------------------
# Phase A: gate check + baseline load
# ---------------------------------------------------------------

def gate_check(log) -> Dict:
    log.write("=== Phase A: gate check + baseline load ===\n")
    if not INPUTS["t37c_verdict"].exists():
        raise SystemExit("HALT_T37F_INPUT_INVALID: 017c verdict.json missing")
    verdict = json.loads(INPUTS["t37c_verdict"].read_text(encoding="utf-8"))
    label = verdict.get("verdict", "")
    accepted = {
        "T37_PARTIAL_a_1_PARTITIONS",
        "T37_PARTIAL_BASIS_CONVENTION_AMBIGUOUS",
        "T37E_PARTIAL_BASIS_CONVENTION_AMBIGUOUS",
    }
    if label not in accepted:
        raise SystemExit(f"HALT_T37F_GATE_NOT_SATISFIED: 017c verdict {label!r} not in gate set")

    if label == "T37_PARTIAL_a_1_PARTITIONS":
        if not verdict.get("ql09_a1_anomalous", False):
            raise SystemExit("HALT_T37F_GATE_NOT_SATISFIED: ql09_a1_anomalous flag absent")
        a1_val = abs(mp.mpf(str(verdict.get("ql09_a1_value_float", 1.0))))
        if a1_val > mp.mpf("1e-20"):
            raise SystemExit(
                f"HALT_T37F_GATE_NOT_SATISFIED: |QL09 a_1_branch_plus| = {a1_val} "
                f"exceeds 1e-20 threshold"
            )
        log.write(f"  gate G1 satisfied: ql09_a1_anomalous=True, |a_1|~{a1_val}\n")

    if not INPUTS["t37c_d_extr"].exists():
        raise SystemExit("HALT_T37F_INPUT_INVALID: 017c d_extraction_feasibility.json missing")
    feas = json.loads(INPUTS["t37c_d_extr"].read_text(encoding="utf-8"))
    if "QL09" not in feas:
        raise SystemExit("HALT_T37F_INPUT_INVALID: QL09 row missing from d_extraction_feasibility.json")
    ql09_p = feas["QL09"]
    baseline = {
        "C_branch_plus": ql09_p["C_median"],
        "C_branch_plus_half_range": ql09_p["C_half_range"],
        "a_1_branch_plus": ql09_p["a_1_median"],
        "a_2_branch_plus": ql09_p["a_2_median"],
        "a_3_branch_plus": ql09_p["a_3_median"],
        "D_branch_plus": ql09_p["D_median"],
        "D_branch_plus_half_range": ql09_p["D_half_range"],
        "K_lead_optimum_017c": ql09_p["K_lead_optimal"],
        "feasibility_017c": ql09_p["feasibility"],
        "stage1_window_017c": ql09_p["stage1_window"],
    }
    log.write(f"  baseline loaded: C+ = {baseline['C_branch_plus'][:30]}..., "
              f"a_1+ = {baseline['a_1_branch_plus'][:30]}...\n")
    return {"verdict_label": label, "baseline": baseline,
            "verdict_hash": file_hash(INPUTS["t37c_verdict"]),
            "feas_hash": file_hash(INPUTS["t37c_d_extr"])}


# ---------------------------------------------------------------
# Phase 0: opposite-branch recurrence at dps=300, N=2000
# ---------------------------------------------------------------

def birkhoff_series(rep: Dict, N: int, dps: int, sign: int, log) -> Dict:
    """Compute a_0=1, ..., a_N for branch sign in {+1, -1}."""
    work_dps = dps + 50
    mp.mp.dps = work_dps

    alpha = mp.mpf(rep["alpha"])
    beta = mp.mpf(rep["beta"])
    gamma = mp.mpf(rep["gamma"])
    delta = mp.mpf(rep["delta"])
    epsi = mp.mpf(rep["epsilon"])

    c = mp.mpf(sign) * mp.mpf(2) / mp.sqrt(alpha)
    rho = mp.mpf(-3) / 2 - beta / alpha
    zeta_signed = 2 * c   # signed dominant action; sign(zeta_signed)=sign(c).
    zeta_abs = abs(zeta_signed)

    base_km1 = gamma - beta * beta / (4 * alpha)
    coeff_km1_quad = alpha / mp.mpf(16)
    Ukm2 = -c * delta / 2
    base_km3 = epsi - beta * delta / (2 * alpha)
    diag_premul = alpha * c / 2

    a = [mp.mpf(0)] * (N + 1)
    a[0] = mp.mpf(1)

    t0 = time.time()
    for k in range(1, N + 1):
        two_km1 = mp.mpf(2 * k - 1)
        Ukm1 = coeff_km1_quad * (two_km1 ** 2) + base_km1
        Ukm3 = (two_km1 / 4) * delta + base_km3
        rhs = Ukm1 * a[k - 1]
        if k - 2 >= 0:
            rhs += Ukm2 * a[k - 2]
        if k - 3 >= 0:
            rhs += Ukm3 * a[k - 3]
        diag = diag_premul * mp.mpf(k)
        a[k] = rhs / diag
        if k % 400 == 0 or k == N:
            mag = int(mp.log10(abs(a[k]))) if a[k] != 0 else 0
            log.write(f"    [B sign={sign:+d}] k={k:5d} a_k~10^{mag} t={time.time()-t0:.1f}s\n")
            log.flush()

    mp.mp.dps = dps
    a = [+x for x in a]
    return {
        "a": a, "c": +c, "rho": +rho,
        "zeta_signed": +zeta_signed, "zeta_abs": +zeta_abs,
        "sign": sign, "dps": dps, "N": N,
    }


def write_an_csv(p: Path, a: List[mp.mpf]):
    with p.open("w", encoding="utf-8", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow(["n", "a_n_real", "a_n_imag"])
        for n, val in enumerate(a):
            wr.writerow([n, mp.nstr(mp.re(val), 60), mp.nstr(mp.im(val), 60)])


# ---------------------------------------------------------------
# Phase B: lead-only LSQ stage1 fit + stage2
# ---------------------------------------------------------------

def column_scaled_solve(cols: List[List[mp.mpf]], b: List[mp.mpf]):
    """Normal-equation solve with column scaling (T37 convention)."""
    M = len(b)
    K = len(cols)
    scales = [max(abs(v) for v in col) for col in cols]
    scales = [s if s != 0 else mp.mpf(1) for s in scales]
    sc_cols = [[v / scales[k] for v in col] for k, col in enumerate(cols)]
    AtA = [[mp.mpf(0)] * K for _ in range(K)]
    Atb = [mp.mpf(0)] * K
    for r in range(K):
        for cc in range(r, K):
            s = mp.mpf(0)
            for i in range(M):
                s += sc_cols[r][i] * sc_cols[cc][i]
            AtA[r][cc] = s
            AtA[cc][r] = s
        s = mp.mpf(0)
        for i in range(M):
            s += sc_cols[r][i] * b[i]
        Atb[r] = s
    # Solve via Gauss with partial pivoting.
    aug = [row[:] + [Atb[r]] for r, row in enumerate(AtA)]
    rank = K
    for kk in range(K):
        piv = abs(aug[kk][kk])
        piv_row = kk
        for j in range(kk + 1, K):
            if abs(aug[j][kk]) > piv:
                piv = abs(aug[j][kk])
                piv_row = j
        if piv == 0:
            rank = kk
            break
        if piv_row != kk:
            aug[kk], aug[piv_row] = aug[piv_row], aug[kk]
        pv = aug[kk][kk]
        for j in range(kk, K + 1):
            aug[kk][j] /= pv
        for i in range(K):
            if i != kk and aug[i][kk] != 0:
                f = aug[i][kk]
                for j in range(kk, K + 1):
                    aug[i][j] -= f * aug[kk][j]
    x_sc = [aug[r][K] for r in range(K)]
    x = [x_sc[r] / scales[r] for r in range(K)]
    # residual
    res = mp.mpf(0)
    for i in range(M):
        s = mp.mpf(0)
        for r in range(K):
            s += cols[r][i] * x[r]
        d = abs(b[i] - s)
        if d > res:
            res = d
    return x, res, rank


def build_T_n(a: List[mp.mpf], zeta_signed: mp.mpf) -> List[mp.mpf]:
    """T_n = a_n * zeta_signed^n / Gamma(n).  Using Gamma(n) (n>=1)."""
    N = len(a) - 1
    T = [mp.mpf(0)] * (N + 1)
    for n in range(1, N + 1):
        T[n] = a[n] * mp.power(zeta_signed, n) / mp.gamma(mp.mpf(n))
    return T


def stage1_fit(T: List[mp.mpf], n_lo: int, n_hi: int, K_lead: int) -> Dict:
    ns = list(range(n_lo, n_hi + 1))
    cols = []
    for k in range(K_lead + 1):
        col = []
        for n in ns:
            if k == 0:
                col.append(mp.mpf(1))
            else:
                col.append(mp.mpf(1) / (mp.mpf(n) ** k))
        cols.append(col)
    b = [T[n] for n in ns]
    x, r_inf, rank = column_scaled_solve(cols, b)
    C_fit = x[0]
    if C_fit == 0:
        a_coeff = [mp.mpf(0)] + [mp.mpf(0)] * K_lead
    else:
        a_coeff = [x[k] / C_fit for k in range(K_lead + 1)]
    return {
        "n_lo": n_lo, "n_hi": n_hi, "K_lead": K_lead,
        "alpha_coeff": x, "C_fit": C_fit, "a_coeff": a_coeff,
        "residual_inf": r_inf, "rank": rank,
    }


def stage1_predict(stage1: Dict, n: int) -> mp.mpf:
    alpha = stage1["alpha_coeff"]
    K = stage1["K_lead"]
    n_mp = mp.mpf(n)
    s = alpha[0]
    for k in range(1, K + 1):
        s += alpha[k] / (n_mp ** k)
    return s


def stage2_fit(T: List[mp.mpf], stage1: Dict, n_lo: int, n_hi: int,
               K_next: int, branch_sign: int) -> Dict:
    """Next-rung 2^(-n) sum_k beta_k / n^k fit.

    In branch (-) the next-rung action is also flipped sign-wise, so the
    natural variable is (-2)^(-n) = (-1)^n * 2^(-n).  We fit using
    branch-aware factor = (sign_factor)^n * 2^(-n) where sign_factor is
    -1 for branch (-) and +1 for branch (+).  This keeps |D| comparable
    across branches (basis-independent magnitude); a relative SIGN flip
    in D is captured by branch_sign.
    """
    sign_factor = mp.mpf(branch_sign)  # +1 or -1
    ns = list(range(n_lo, n_hi + 1))
    r_data = [T[n] - stage1_predict(stage1, n) for n in ns]
    cols = []
    two = mp.mpf(2)
    for k in range(K_next + 1):
        col = []
        for n in ns:
            base = mp.power(sign_factor, n) / (two ** n)
            if k == 0:
                col.append(base)
            else:
                col.append(base / (mp.mpf(n) ** k))
        cols.append(col)
    x, r_inf, rank = column_scaled_solve(cols, r_data)
    D_fit = x[0]
    return {
        "n_lo": n_lo, "n_hi": n_hi, "K_next": K_next,
        "beta_coeff": x, "D_fit": D_fit,
        "residual_inf": r_inf, "rank": rank,
    }


def stability_envelope(T: List[mp.mpf], branch_sign: int) -> List[Dict]:
    grid = []
    for K_lead in K_LEAD_GRID:
        for w1 in W1_GRID:
            s1 = stage1_fit(T, w1[0], w1[1], K_lead)
            grid.append({
                "K_lead": K_lead, "w1": list(w1),
                "C_fit": s1["C_fit"],
                "a_1": s1["a_coeff"][1] if K_lead >= 1 else mp.mpf(0),
                "a_2": s1["a_coeff"][2] if K_lead >= 2 else mp.mpf(0),
                "a_3": s1["a_coeff"][3] if K_lead >= 3 else mp.mpf(0),
                "residual_inf": s1["residual_inf"],
                "rank": s1["rank"],
            })
    return grid


def median_half_range(values: List[mp.mpf]) -> Tuple[mp.mpf, mp.mpf]:
    if not values:
        return mp.mpf(0), mp.mpf(0)
    s = sorted(values, key=lambda v: mp.re(v))
    n = len(s)
    if n % 2 == 1:
        med = s[n // 2]
    else:
        med = (s[n // 2 - 1] + s[n // 2]) / 2
    half = (s[-1] - s[0]) / 2
    return med, half


# ---------------------------------------------------------------
# Phase C: invariant comparison + PSLQ
# ---------------------------------------------------------------

def pslq_probe(value: mp.mpf, basis: List[Tuple[str, mp.mpf]],
               tol: mp.mpf, maxcoeff: int = 10**15) -> Optional[Dict]:
    """Run mpmath.pslq over [value] + [b for _,b in basis]. Return relation if found."""
    vec = [value] + [b for _, b in basis]
    try:
        rel = mp.pslq(vec, tol=tol, maxcoeff=maxcoeff)
    except Exception:
        rel = None
    if rel is None:
        return None
    if rel[0] == 0:
        return None
    if max(abs(r) for r in rel) > maxcoeff:
        return None
    return {
        "tol": str(tol),
        "relation": [int(r) for r in rel],
        "labels": ["value"] + [name for name, _ in basis],
    }


def rational_reconstruction(value: mp.mpf, q_max: int = 100) -> Optional[str]:
    """Continued fraction reconstruction with denominator <= q_max."""
    if value == 0:
        return "0"
    if abs(value) > mp.mpf("1e-100"):
        try:
            cf = mp.taylor  # placeholder reference; use mp.identify below
        except Exception:
            pass
        # Direct CF via mp.pslq with [value, 1]; or use rational from mp.identify
        try:
            ident = mp.identify(value, ['1', '1/2', '1/3', '1/4', '1/6',
                                        '1/9', '1/36', '1/72'])
            if ident:
                return ident
        except Exception:
            pass
        # Fallback: simple CF with denominator cap.
        x = value
        coeffs = []
        for _ in range(20):
            ai = int(mp.floor(x))
            coeffs.append(ai)
            frac = x - ai
            if abs(frac) < mp.mpf(f"1e-{30}"):
                break
            x = mp.mpf(1) / frac
        # Reconstruct convergents; take the largest with q <= q_max.
        p_prev, q_prev = 1, 0
        p_cur, q_cur = coeffs[0], 1
        for ai in coeffs[1:]:
            p_next = ai * p_cur + p_prev
            q_next = ai * q_cur + q_prev
            if q_next > q_max:
                break
            p_prev, q_prev = p_cur, q_cur
            p_cur, q_cur = p_next, q_next
        return f"{p_cur}/{q_cur}"
    return "0"


# ---------------------------------------------------------------
# Phase D: classification
# ---------------------------------------------------------------

def classify(a_1_minus_abs: mp.mpf, C_minus: mp.mpf, C_plus: mp.mpf,
             rank_phaseB: int) -> str:
    if rank_phaseB < K_LEAD + 1:
        return "BRANCH_DEGENERATE"
    if abs(C_minus) < mp.mpf("1e-50"):
        return "BRANCH_DEGENERATE"
    if a_1_minus_abs < mp.mpf("1e-30"):
        return "THIRD_STRATUM_CONFIRMED"
    if a_1_minus_abs > mp.mpf("1e-3"):
        return "BASIS_SHADOW_CONFIRMED"
    return "BASIS_SHADOW_PARTIAL"


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main():
    log_path = HERE / "t37f_run.log"
    log = log_path.open("w", encoding="utf-8")
    log.write(f"T37F-Q18-NUMERICAL-PROBE  start  {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log.write(f"  dps={DPS}  N={N_TARGET}  K_lead={K_LEAD}  W1={W1}  W2={W2}\n")

    claims_path = HERE / "claims.jsonl"
    if claims_path.exists():
        claims_path.unlink()
    halt_log = {"halts": []}
    discrepancy_log = {"discrepancies": []}
    unexpected = {"finds": []}

    # ============= Phase A =============
    gate = gate_check(log)
    baseline = gate["baseline"]
    C_plus = mp.mpf(baseline["C_branch_plus"])
    a_1_plus = mp.mpf(baseline["a_1_branch_plus"])
    a_2_plus = mp.mpf(baseline["a_2_branch_plus"])
    a_3_plus = mp.mpf(baseline["a_3_branch_plus"])
    D_plus = mp.mpf(baseline["D_branch_plus"])

    # ============= Phase 0: derive both branches =============
    log.write("\n=== Phase 0: derive series in both branches ===\n")
    rec_plus = birkhoff_series(QL09, N_TARGET, DPS, sign=+1, log=log)
    rec_minus = birkhoff_series(QL09, N_TARGET, DPS, sign=-1, log=log)

    # Sanity: a[1] should be exactly 0 (or numerical zero) in both branches.
    a1_plus_recurr = rec_plus["a"][1]
    a1_minus_recurr = rec_minus["a"][1]
    log.write(f"  recurrence a_1_plus  = {mp.nstr(a1_plus_recurr, 5)}\n")
    log.write(f"  recurrence a_1_minus = {mp.nstr(a1_minus_recurr, 5)}\n")
    if abs(a1_plus_recurr) > mp.mpf("1e-200") or abs(a1_minus_recurr) > mp.mpf("1e-200"):
        log.write("  WARNING: recurrence a_1 not exactly 0; check\n")

    # Sanity ratio at n=100.
    n_check = 100
    rp = rec_plus["a"][n_check]
    rm = rec_minus["a"][n_check]
    ratio = abs(rm / rp) if rp != 0 else mp.mpf("inf")
    log.write(f"  sanity n=100: |a_minus/a_plus| = {mp.nstr(ratio, 6)}\n")
    if ratio > mp.mpf("1e10") or ratio < mp.mpf("1e-10"):
        msg = ("Sanity ratio at n=100 outside [1e-10,1e10]: scale mismatch")
        halt_log["halts"].append({"key": "T37F_RECURRENCE_OPPOSITE_BRANCH_SCALE_MISMATCH",
                                  "ratio": str(ratio), "message": msg})
        write_json(HERE / "halt_log.json", halt_log)
        log.write(f"  HALT: {msg}\n")
        log.close()
        raise SystemExit("HALT_T37F_RECURRENCE_OPPOSITE_BRANCH_SCALE_MISMATCH")

    # Persist a_n series.
    csv_path = HERE / "a_n_QL09_opposite_dps300_N2000.csv"
    write_an_csv(csv_path, rec_minus["a"])
    csv_hash = file_hash(csv_path)

    append_claim(claims_path, {
        "claim": "Phase 0 branch pinning: in branch (-), c=-2/sqrt(2), zeta_signed=2c=-2*sqrt(2); recurrence form invariant under sign(c) flip; a_1=0 algebraic identity for QL09",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "derive_recurrence_QL09_opposite_branch.py",
        "output_hash": file_hash(HERE / "phase_0_branch_pinning.json"),
    })
    append_claim(claims_path, {
        "claim": f"Phase 0 sanity at n=100: |a_n_branch_minus/a_n_branch_plus| = {mp.nstr(ratio, 12)}, within [1e-10,1e10] band",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })

    # ============= Phase B: refit =============
    log.write("\n=== Phase B: stage1+stage2 fit, opposite branch ===\n")
    T_minus = build_T_n(rec_minus["a"], rec_minus["zeta_signed"])
    T_plus = build_T_n(rec_plus["a"], rec_plus["zeta_signed"])

    stage1_minus = stage1_fit(T_minus, W1[0], W1[1], K_LEAD)
    log.write(f"  stage1 (-) C={mp.nstr(stage1_minus['C_fit'],30)} "
              f"a_1={mp.nstr(stage1_minus['a_coeff'][1],10)} "
              f"a_2={mp.nstr(stage1_minus['a_coeff'][2],15)} "
              f"a_3={mp.nstr(stage1_minus['a_coeff'][3],15)}\n")
    log.write(f"  stage1 residual_inf={mp.nstr(stage1_minus['residual_inf'],3)} "
              f"rank={stage1_minus['rank']}\n")

    if stage1_minus["rank"] < K_LEAD + 1:
        halt_log["halts"].append({"key": "T37F_RANK_LOSS",
                                  "rank": stage1_minus["rank"],
                                  "K_plus_1": K_LEAD + 1})
        write_json(HERE / "halt_log.json", halt_log)
        log.close()
        raise SystemExit("HALT_T37F_RANK_LOSS")

    stage1_plus = stage1_fit(T_plus, W1[0], W1[1], K_LEAD)
    log.write(f"  stage1 (+) C={mp.nstr(stage1_plus['C_fit'],30)} "
              f"a_1={mp.nstr(stage1_plus['a_coeff'][1],10)}  (cross-check vs 017c)\n")

    # Stability envelope (opposite branch).
    env_minus = stability_envelope(T_minus, branch_sign=-1)
    Cs_m = [g["C_fit"] for g in env_minus]
    a1s_m = [g["a_1"] for g in env_minus]
    a2s_m = [g["a_2"] for g in env_minus]
    a3s_m = [g["a_3"] for g in env_minus]
    C_med_m, C_hr_m = median_half_range(Cs_m)
    a1_med_m, a1_hr_m = median_half_range(a1s_m)
    a2_med_m, a2_hr_m = median_half_range(a2s_m)
    a3_med_m, a3_hr_m = median_half_range(a3s_m)

    # Stage 2 (next-rung) — opposite branch: branch_sign=-1.
    stage2_minus = stage2_fit(T_minus, stage1_minus, W2[0], W2[1],
                              K_NEXT, branch_sign=-1)
    stage2_plus = stage2_fit(T_plus, stage1_plus, W2[0], W2[1],
                             K_NEXT, branch_sign=+1)
    D_minus = stage2_minus["D_fit"]
    D_plus_recomputed = stage2_plus["D_fit"]
    log.write(f"  stage2 D_minus={mp.nstr(D_minus,30)} "
              f"residual_inf={mp.nstr(stage2_minus['residual_inf'],3)}\n")
    log.write(f"  stage2 D_plus (recomputed) ={mp.nstr(D_plus_recomputed,30)}\n")

    append_claim(claims_path, {
        "claim": f"Phase B stage1 (branch -) at K_lead={K_LEAD} W1={W1}: C_minus_median = {mp.nstr(C_med_m, 30)}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })
    append_claim(claims_path, {
        "claim": f"Phase B stage1 a_1_minus median = {mp.nstr(a1_med_m, 30)} (envelope half-range {mp.nstr(a1_hr_m, 6)})",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })
    append_claim(claims_path, {
        "claim": f"Phase B stage1 a_2_minus median = {mp.nstr(a2_med_m, 30)} (envelope half-range {mp.nstr(a2_hr_m, 6)})",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })
    append_claim(claims_path, {
        "claim": f"Phase B stage1 a_3_minus median = {mp.nstr(a3_med_m, 30)} (envelope half-range {mp.nstr(a3_hr_m, 6)})",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })
    append_claim(claims_path, {
        "claim": f"Phase B.3 stability envelope (9 configs): C_half_range/|C_median| = {mp.nstr(abs(C_hr_m / C_med_m) if C_med_m != 0 else mp.mpf(0), 6)}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })
    append_claim(claims_path, {
        "claim": f"Phase B.4 D_minus extraction (W2={W2}, K_next={K_NEXT}): D_minus = {mp.nstr(D_minus, 12)}, residual_inf = {mp.nstr(stage2_minus['residual_inf'], 3)}; 017c reported D_branch_plus as BLOCKED so |D| comparison is provisional only",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": csv_hash,
    })

    # ============= Phase C: invariants =============
    log.write("\n=== Phase C: invariant comparison ===\n")
    sign_C_flip = (mp.sign(C_plus) != mp.sign(stage1_minus["C_fit"]))
    a1_shift = abs(a1_med_m) - abs(a_1_plus)
    a1_sign = mp.sign(a1_med_m) if a1_med_m != 0 else mp.mpf(0)
    C_ratio = abs(stage1_minus["C_fit"]) / abs(C_plus) if C_plus != 0 else mp.mpf("inf")
    D_ratio = abs(D_minus) / abs(D_plus_recomputed) if D_plus_recomputed != 0 else mp.mpf("inf")
    S2_minus = abs(2 * mp.pi * D_minus)
    S2_plus = abs(2 * mp.pi * D_plus_recomputed)

    invariants = {
        "C_branch_plus": mp.nstr(C_plus, 60),
        "C_branch_minus_median": mp.nstr(C_med_m, 60),
        "C_branch_minus_half_range": mp.nstr(C_hr_m, 30),
        "SIGN_C_FLIP": bool(sign_C_flip),
        "a_1_branch_plus": mp.nstr(a_1_plus, 30),
        "a_1_branch_minus_median": mp.nstr(a1_med_m, 60),
        "a_1_branch_minus_half_range": mp.nstr(a1_hr_m, 30),
        "abs_a1_shift": mp.nstr(a1_shift, 30),
        "a_1_branch_minus_sign": int(a1_sign) if a1_med_m != 0 else 0,
        "a_2_branch_plus": mp.nstr(a_2_plus, 30),
        "a_2_branch_minus_median": mp.nstr(a2_med_m, 60),
        "a_3_branch_plus": mp.nstr(a_3_plus, 30),
        "a_3_branch_minus_median": mp.nstr(a3_med_m, 60),
        "abs_C_ratio_minus_over_plus": mp.nstr(C_ratio, 30),
        "D_branch_plus_017c_BLOCKED_median": mp.nstr(D_plus, 30),
        "D_branch_plus_recomputed_017f": mp.nstr(D_plus_recomputed, 30),
        "D_branch_minus_017f": mp.nstr(D_minus, 30),
        "abs_D_ratio_minus_over_plus_recomputed": mp.nstr(D_ratio, 30),
        "abs_S_2_branch_plus": mp.nstr(S2_plus, 30),
        "abs_S_2_branch_minus": mp.nstr(S2_minus, 30),
    }
    write_json(HERE / "invariant_comparison.json", invariants)

    append_claim(claims_path, {
        "claim": f"Phase C invariant SIGN_C_FLIP = {bool(sign_C_flip)} (C_plus sign vs C_minus sign)",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })
    append_claim(claims_path, {
        "claim": f"Phase C invariant |a_1| SHIFT = {mp.nstr(a1_shift, 30)}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })
    append_claim(claims_path, {
        "claim": f"Phase C invariant |C| RATIO = {mp.nstr(C_ratio, 30)}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })
    append_claim(claims_path, {
        "claim": f"Phase C invariant |D| RATIO = {mp.nstr(D_ratio, 30)} (017c-vs-017f recomputed branch +; D_branch_plus_017c was BLOCKED)",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })

    # PSLQ probe (only meaningful if |a_1_minus| > 1e-3)
    pslq_result_strict = None
    pslq_result_loose = None
    a1_abs = abs(a1_med_m)
    if a1_abs > mp.mpf("1e-3"):
        basis = [
            ("1", mp.mpf(1)), ("1/2", mp.mpf(1)/2), ("1/3", mp.mpf(1)/3),
            ("1/4", mp.mpf(1)/4), ("1/6", mp.mpf(1)/6),
            ("1/9", mp.mpf(1)/9), ("1/36", mp.mpf(1)/36), ("1/72", mp.mpf(1)/72),
            ("Delta_b", mp.mpf(QL09["Delta_b"])),
            ("1/A", mp.mpf(1)/QL09["A_pred"]),
            ("Delta_b/A", mp.mpf(QL09["Delta_b"])/QL09["A_pred"]),
        ]
        pslq_result_loose = pslq_probe(a1_med_m, basis, tol=mp.mpf("1e-8"))
        pslq_result_strict = pslq_probe(a1_med_m, basis, tol=mp.mpf("1e-12"))
        if pslq_result_loose and not pslq_result_strict:
            halt_log["halts"].append({
                "key": "T37F_PSLQ_OVERCLAIM",
                "loose_relation": pslq_result_loose,
            })
            write_json(HERE / "halt_log.json", halt_log)
            log.close()
            raise SystemExit("HALT_T37F_PSLQ_OVERCLAIM")
    append_claim(claims_path, {
        "claim": f"Phase C.4 PSLQ (tol=1e-12) on a_1_minus median: relation = {pslq_result_strict}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })
    append_claim(claims_path, {
        "claim": f"Phase C.4 PSLQ (tol=1e-8) hard-hygiene cross-check: relation = {pslq_result_loose}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })

    rat_recon = "0 (|a_1_minus|<1e-30)"
    if a1_abs > mp.mpf("1e-30"):
        rat_recon = rational_reconstruction(a1_med_m, q_max=100)
    append_claim(claims_path, {
        "claim": f"Phase C.5 rational reconstruction of a_1_minus (q<=100): {rat_recon}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })

    # ============= Phase D: classify =============
    log.write("\n=== Phase D: classification ===\n")
    classification = classify(a1_abs, stage1_minus["C_fit"], C_plus,
                              stage1_minus["rank"])
    log.write(f"  classification: {classification}\n")

    if classification == "THIRD_STRATUM_CONFIRMED":
        verdict_label = "T37F_Q18_THIRD_STRATUM"
    elif classification == "BASIS_SHADOW_CONFIRMED":
        verdict_label = "T37F_Q18_BASIS_SHADOW_CONFIRMED"
    elif classification == "BASIS_SHADOW_PARTIAL":
        verdict_label = "T37F_Q18_PARTIAL"
    else:
        verdict_label = "T37F_Q18_BRANCH_DEGENERATE"

    append_claim(claims_path, {
        "claim": f"Phase D classification: {classification}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })
    append_claim(claims_path, {
        "claim": f"Verdict label: {verdict_label}",
        "evidence_type": "computation",
        "dps": DPS, "reproducible": True,
        "script": "t37f_runner.py",
        "output_hash": file_hash(HERE / "invariant_comparison.json"),
    })

    # Certificate
    cert = build_certificate(
        gate, baseline, rec_minus, rec_plus,
        stage1_minus, stage1_plus, env_minus,
        C_med_m, C_hr_m, a1_med_m, a1_hr_m,
        a2_med_m, a2_hr_m, a3_med_m, a3_hr_m,
        D_minus, D_plus_recomputed,
        invariants, pslq_result_strict, pslq_result_loose,
        rat_recon, classification, verdict_label,
    )
    (HERE / "q18_numerical_certificate.md").write_text(cert, encoding="utf-8")

    # Verdict + halt + discrepancy + unexpected
    verdict_obj = {
        "verdict_label": verdict_label,
        "classification": classification,
        "a_1_branch_minus_median": mp.nstr(a1_med_m, 60),
        "C_branch_minus_median": mp.nstr(C_med_m, 60),
        "rank_phaseB": stage1_minus["rank"],
    }
    write_json(HERE / "verdict.json", verdict_obj)
    write_json(HERE / "halt_log.json", halt_log)
    write_json(HERE / "discrepancy_log.json", discrepancy_log)
    write_json(HERE / "unexpected_finds.json", unexpected)

    log.write(f"\nDONE. verdict={verdict_label}\n")
    log.close()
    print(f"verdict: {verdict_label}")
    print(f"classification: {classification}")
    print(f"|a_1_branch_minus| = {mp.nstr(a1_abs, 6)}")


def build_certificate(gate, baseline, rec_minus, rec_plus,
                      stage1_minus, stage1_plus, env_minus,
                      C_med_m, C_hr_m, a1_med_m, a1_hr_m,
                      a2_med_m, a2_hr_m, a3_med_m, a3_hr_m,
                      D_minus, D_plus_recomputed,
                      invariants, pslq_strict, pslq_loose,
                      rat_recon, classification, verdict_label) -> str:
    lines = [
        "# Q18 Numerical Certificate (T37F-Q18-NUMERICAL-PROBE)",
        "",
        f"**Verdict:** `{verdict_label}`",
        f"**Classification:** `{classification}`",
        "",
        "## 1. Baseline (017c branch +)",
        f"- C_branch_plus = `{baseline['C_branch_plus']}`",
        f"- a_1_branch_plus = `{baseline['a_1_branch_plus']}`",
        f"- a_2_branch_plus = `{baseline['a_2_branch_plus']}`",
        f"- a_3_branch_plus = `{baseline['a_3_branch_plus']}`",
        f"- D_branch_plus (017c, BLOCKED median) = `{baseline['D_branch_plus']}`",
        f"- 017c verdict label = `{gate['verdict_label']}`",
        "",
        "## 2. Branch (-) measurement (017f, dps=300, N=2000)",
        f"- C_branch_minus median = `{mp.nstr(C_med_m, 60)}`",
        f"  - half-range = `{mp.nstr(C_hr_m, 30)}`",
        f"- a_1_branch_minus median = `{mp.nstr(a1_med_m, 60)}`",
        f"  - half-range = `{mp.nstr(a1_hr_m, 30)}`",
        f"- a_2_branch_minus median = `{mp.nstr(a2_med_m, 60)}`",
        f"  - half-range = `{mp.nstr(a2_hr_m, 30)}`",
        f"- a_3_branch_minus median = `{mp.nstr(a3_med_m, 60)}`",
        f"  - half-range = `{mp.nstr(a3_hr_m, 30)}`",
        f"- D_branch_minus (provisional) = `{mp.nstr(D_minus, 30)}`",
        "",
        "## 3. Invariant comparison",
        f"- SIGN_C_FLIP = {invariants['SIGN_C_FLIP']}",
        f"- |a_1| SHIFT = `{invariants['abs_a1_shift']}`",
        f"- |C| RATIO (|C-|/|C+|) = `{invariants['abs_C_ratio_minus_over_plus']}`",
        f"- |D| RATIO (017f recomputed) = `{invariants['abs_D_ratio_minus_over_plus_recomputed']}`",
        f"- |S_2| branch + = `{invariants['abs_S_2_branch_plus']}`",
        f"- |S_2| branch - = `{invariants['abs_S_2_branch_minus']}`",
        "",
        "## 4. Hypothesis tests",
        f"- |a_1_minus| > 1e-3 ?  -> {abs(a1_med_m) > mp.mpf('1e-3')}",
        f"- |a_1_minus| < 1e-30 ?  -> {abs(a1_med_m) < mp.mpf('1e-30')}",
        f"- PSLQ tol=1e-12 relation = {pslq_strict}",
        f"- PSLQ tol=1e-8  relation = {pslq_loose}",
        f"- Rational reconstruction (q<=100) = `{rat_recon}`",
        "",
        "## 5. Classification",
        f"Phase D classifies as **{classification}**.",
        "",
    ]
    if classification == "THIRD_STRATUM_CONFIRMED":
        lines += [
            "Branch-(-) re-derivation reports a_1_minus = 0 to >> 30 digits, "
            "consistent with the algebraic identity established in Phase 0: "
            "the U_{k-1}(1) bracket alpha/16 + gamma - beta^2/(4 alpha) "
            "evaluates to 1/8 + 1 - 9/8 = 0 for QL09, which is "
            "c-INDEPENDENT and therefore basis-independent.",
            "",
            "The (a) THIRD_STRATUM interpretation is the parsimonious "
            "reading: QL09's a_1 = 0 is a structural feature of its "
            "(alpha, beta, gamma) coefficients, not a convention shadow.",
            "",
            "## 6. Recommendation: picture v1.10 vs v1.11",
            "Picture v1.11 amendment is consistent with this finding: at d=2, "
            "G20 admits THREE strata distinguished by a_1: "
            "(i) Delta_b<0 negative-rational a_1 (V_quad: -53/36; QL15: -89/36), "
            "(ii) Delta_b>0 positive-rational a_1 (QL05: +31/4), "
            "(iii) Delta_b>0 a_1 = 0 sub-stratum (QL09).  "
            "Recommend a follow-on prompt to characterise the QL09 family "
            "structurally (Galois bin, conductor, j-invariant) and to scan "
            "the d=2 catalogue for additional members of the a_1=0 sub-stratum.",
        ]
    elif classification == "BASIS_SHADOW_CONFIRMED":
        lines += [
            f"Branch-(-) re-derivation reports a_1_minus = {mp.nstr(a1_med_m, 30)} "
            "(non-zero, > 1e-3).  PSLQ relation under hard-hygiene "
            f"= {pslq_strict}.",
            "",
            "The (b) CONVENTION-SHADOW interpretation is parsimonious: "
            "QL09 was inadvertently in the wrong dominant-balance branch "
            "in T35/010/017c.  Picture v1.10 is consistent with this "
            "reading; QL09 should be re-classified into the Delta_b>0 "
            "positive-a_1 stratum once the branch is flipped.",
            "",
            "## 6. Recommendation",
            "Recommend a follow-on T35-style refit of QL09 in the corrected "
            "branch, plus a full-catalogue audit prompt to verify no other "
            "rep silently suffers the same branch shadow.",
        ]
    elif classification == "BASIS_SHADOW_PARTIAL":
        lines += [
            f"Branch-(-) a_1_minus = {mp.nstr(a1_med_m, 30)} sits in the "
            "indeterminate band [1e-30, 1e-3].  dps=300 may be insufficient.",
            "",
            "## 6. Recommendation",
            "Escalate to dps=400 / N=5000 in the opposite branch.",
        ]
    else:
        lines += [
            "Branch (-) is structurally degenerate (rank loss or vanishing C).",
            "",
            "## 6. Recommendation",
            "Dedicated structural analysis of QL09's branch-(-) recurrence.",
        ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
