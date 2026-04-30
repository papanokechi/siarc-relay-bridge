"""
UMB-T0T1-CLASSIFIER (P-07) — dataset assembly.

Curates a labeled training set of 500 PCF families:
  - 300 T0 (rational / algebraic limit) — sampled from F(2,4) certificate's
    Rat stratum (113,270 families).
  - 200 T1 (transcendental) — 24 F(2,4) Trans families + 176 sampled from
    the 482-irrationals catalog (quadratic-denominator GCFs).

Features (per relay spec):
  1. deg_a, deg_b        — polynomial degree pair
  2. R_struct            — leading ratio a_top / b_top^2
  3. disc_a, disc_a_neg  — integer indicial discriminant flag
                           (a1^2 - 4 a2 a0 for deg-(2,*) entries)
  4. BT_disc, lam_ratio,
     int_resonance       — BT exponent ratio lambda_+/lambda_-,
                           integer-resonance flag
  5. stokes_idx          — Stokes index proxy from p06 desert paper:
                           +1 surd / oscillatory, 0 rational, -1 indicial-zero
  6. conv_slope          — convergence speed -d log10|r_n|/dn (numerical)

Coefficient ordering convention: a = [a_top, ..., a_const] (leading first),
matching f1_base_computation.py.

Outputs:
  dataset.csv, features.json, build.log
"""

import csv
import json
import math
import random
import sys
import time
from pathlib import Path

from mpmath import mp, mpf, mpc, log10, fabs

# -------------------------------------------------------------------------
# Reproducibility
# -------------------------------------------------------------------------
SEED = 20260430
random.seed(SEED)
mp.dps = 60

ROOT = Path(__file__).resolve().parents[4]  # repo root: claude-chat
HERE = Path(__file__).resolve().parent
F1_CERT = ROOT / "f1_base_certificate.json"
IRR_CSV = ROOT / "pcf-casoratian-identities" / "data" / "new_irrational_constants.csv"
OUT_CSV = HERE / "dataset.csv"
OUT_FEATURES = HERE / "features.json"
LOG = HERE / "build.log"

log_lines: list[str] = []


def log(msg: str) -> None:
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    log_lines.append(line)


# -------------------------------------------------------------------------
# Schema helpers
# -------------------------------------------------------------------------
def normalise_family(deg_a: int, deg_b: int, a_coeffs: list[int], b_coeffs: list[int]) -> dict:
    """Normalise to a unified record: leading coefficients first.
    Pads with zeros so a_coeffs has length deg_a+1 and b_coeffs length deg_b+1.
    """
    a_top = a_coeffs[0] if a_coeffs else 0
    b_top = b_coeffs[0] if b_coeffs else 0
    return {
        "deg_a": deg_a,
        "deg_b": deg_b,
        "a": list(a_coeffs),
        "b": list(b_coeffs),
        "a_top": a_top,
        "b_top": b_top,
    }


# -------------------------------------------------------------------------
# Feature computation
# -------------------------------------------------------------------------
def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    r = int(math.isqrt(n))
    return r * r == n


def feature_R_struct(a_top: int, b_top: int) -> float:
    if b_top == 0:
        return float("nan")
    return float(a_top) / float(b_top) ** 2


def feature_disc_a(a_coeffs: list[int]) -> tuple[int, int, int]:
    """Return (disc_a, disc_a_neg_flag, disc_a_psq_flag).

    disc_a = a1^2 - 4 a2 a0 for the deg-2 indicial polynomial of a(n).
    For deg(a) != 2 we return 0/0/0 as a degenerate sentinel.
    """
    if len(a_coeffs) == 3:  # [a2, a1, a0]
        a2, a1, a0 = a_coeffs
        d = a1 * a1 - 4 * a2 * a0
        return d, int(d < 0), int(is_perfect_square(d))
    return 0, 0, 0


def feature_BT(a_top: int, b_top: int) -> tuple[int, float, int, int]:
    """BT spectral features for the recurrence x = b_top + a_top / x.

    Characteristic polynomial: lambda^2 - b_top lambda - a_top = 0
    Discriminant D = b_top^2 + 4 a_top.

    Returns (BT_disc, lam_ratio, int_resonance_flag, stokes_idx).
      stokes_idx = +1 if D > 0 and not a perfect square (irrational surd)
                 =  0 if D > 0 and a perfect square (rational lambdas)
                 = -1 if D < 0 (complex conjugate / oscillatory)
                 =  0 if D == 0 (degenerate double root).
    """
    D = b_top * b_top + 4 * a_top
    if D < 0:
        # |lam_+| = |lam_-|, ratio modulus = 1
        return D, 1.0, 0, -1
    if D == 0:
        return D, 1.0, 0, 0
    sqrtD = math.sqrt(D)
    lp = (b_top + sqrtD) / 2.0
    lm = (b_top - sqrtD) / 2.0
    if lm == 0:
        return D, float("inf"), 0, +1 if not is_perfect_square(D) else 0
    ratio = abs(lp / lm)
    psq = is_perfect_square(D)
    int_res = 0
    if psq:
        # Lambdas are rational; check integer ratio >= 2
        try:
            r_int = round(ratio)
            if r_int >= 2 and abs(ratio - r_int) < 1e-9:
                int_res = 1
        except Exception:
            pass
    stokes = 0 if psq else +1
    return D, ratio, int_res, stokes


def feature_conv_slope(
    a_coeffs: list[int],
    b_coeffs: list[int],
    N: int = 200,
    dps: int = 60,
    tail_window: tuple[int, int] = (50, 180),
) -> tuple[float, float, int]:
    """Compute -d log10|r_n|/dn slope where r_n = K_n - K_{n-1}.

    Uses backward recurrence form:  K = b0 + a(1)/(b(1) + a(2)/(b(2) + ...))
    Returns (slope, r_final_log10, finite_termination_flag).

    finite_termination_flag = 1 iff |r_n| collapses to 0 at machine precision
    (a hallmark of the Rat stratum).
    """
    mp.dps = dps

    def a_of(n: int) -> mpf:
        # a evaluated at n (top-down poly evaluation)
        deg = len(a_coeffs) - 1
        v = mpf(0)
        for k, c in enumerate(a_coeffs):
            v += mpf(c) * mpf(n) ** (deg - k)
        return v

    def b_of(n: int) -> mpf:
        deg = len(b_coeffs) - 1
        v = mpf(0)
        for k, c in enumerate(b_coeffs):
            v += mpf(c) * mpf(n) ** (deg - k)
        return v

    def K_of(M: int) -> mpf:
        # backward recurrence with safety: tail value 0
        # K_M = b(0) + a(1)/(b(1) + a(2)/(b(2) + ...))
        # we accumulate as denom_M = b(M); denom_{k} = b(k) + a(k+1)/denom_{k+1}
        try:
            v = b_of(M)
            for k in range(M - 1, 0, -1):
                if v == 0:
                    return mpf("nan")
                v = b_of(k) + a_of(k + 1) / v
            if v == 0:
                return mpf("nan")
            return b_of(0) + a_of(1) / v
        except (ZeroDivisionError, OverflowError):
            return mpf("nan")

    Ks: list[mpf] = []
    # Sample Ks every step in the tail window (cheap relative to one-shot N)
    last = None
    for n in range(2, N + 1):
        Ks.append(K_of(n))
    # Now compute log10|r_n|
    eps = mpf(10) ** (-dps + 5)
    log_rs: list[float] = []
    finite_term = 0
    for i in range(1, len(Ks)):
        d = fabs(Ks[i] - Ks[i - 1])
        if d == 0 or d < eps:
            log_rs.append(float("-inf"))
            finite_term = 1
        else:
            try:
                log_rs.append(float(log10(d)))
            except Exception:
                log_rs.append(float("nan"))
    # Slope via least squares over tail window where log_rs is finite
    lo, hi = tail_window
    xs: list[float] = []
    ys: list[float] = []
    for i, lv in enumerate(log_rs):
        n = i + 3  # mapping back to actual index (Ks[i] corresponds to K_of(i+2), r_i = K_of(i+3)-K_of(i+2))
        if lo <= n <= hi and math.isfinite(lv):
            xs.append(float(n))
            ys.append(lv)
    if len(xs) >= 5:
        # least squares slope
        mx = sum(xs) / len(xs)
        my = sum(ys) / len(ys)
        num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        den = sum((x - mx) ** 2 for x in xs)
        slope = -num / den if den != 0 else float("nan")
    else:
        slope = float("nan")
    r_final_log10 = log_rs[-1] if log_rs else float("nan")
    if not math.isfinite(r_final_log10):
        r_final_log10 = -1e9 if finite_term else float("nan")
    return slope, r_final_log10, finite_term


# -------------------------------------------------------------------------
# Dataset assembly
# -------------------------------------------------------------------------
def load_F24_certificate() -> dict:
    return json.loads(F1_CERT.read_text(encoding="utf-8"))


def enumerate_F24_rat_families() -> list[dict]:
    """Re-enumerate Rat families deterministically.

    The certificate stores Rat counts but not full family lists (too large).
    We replicate the F(2,4) enumeration over [-4,4]^6 and apply the same
    structural Rat predicates used in f1_base_computation.py:
      - "trivial zero": a == 0 polynomial
      - "finite termination": there exists n>=1 with a(n)=0 in integer arith
        AND b(0..n-1) all nonzero (the recurrence terminates).
    """
    fams = []
    # iterate (a2, a1, a0, b2, b1, b0) in [-4,4]^6
    for a2 in range(-4, 5):
        for a1 in range(-4, 5):
            for a0 in range(-4, 5):
                a = (a2, a1, a0)
                triv_zero = a == (0, 0, 0)
                for b2 in range(-4, 5):
                    for b1 in range(-4, 5):
                        for b0 in range(-4, 5):
                            b = (b2, b1, b0)
                            if b == (0, 0, 0):
                                continue
                            if triv_zero:
                                fams.append({"a": list(a), "b": list(b), "rat_kind": "trivial_zero"})
                                continue
                            # Search integer root n in [1, 12] of a(n) = a2 n^2 + a1 n + a0
                            n_root = None
                            for n in range(1, 13):
                                v = a2 * n * n + a1 * n + a0
                                if v == 0:
                                    n_root = n
                                    break
                            if n_root is None:
                                continue
                            # Need b(0..n_root-1) all nonzero
                            ok = True
                            for k in range(0, n_root):
                                bv = b2 * k * k + b1 * k + b0
                                if bv == 0:
                                    ok = False
                                    break
                            if ok:
                                fams.append({"a": list(a), "b": list(b), "rat_kind": "finite_termination"})
    return fams


def load_F24_trans() -> list[dict]:
    cert = load_F24_certificate()
    out = []
    for f in cert["strata"]["Trans"]["families"]:
        a = f["family"]["a"]
        b = f["family"]["b"]
        out.append({"a": list(a), "b": list(b), "trans_basis": f.get("basis", "T1")})
    return out


def load_irrationals_482() -> list[dict]:
    rows = []
    with IRR_CSV.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            A = int(r["A"])
            B = int(r["B"])
            C = int(r["C"])
            # b(n) = A n^2 + B n + C  (deg=2),  a(n) = 1 (constant, deg=0).
            rows.append({
                "id": int(r["id"]),
                "a": [1],         # deg_a = 0
                "b": [A, B, C],   # deg_b = 2
                "value": r["value"],
            })
    return rows


# -------------------------------------------------------------------------
# Main
# -------------------------------------------------------------------------
def main():
    t0 = time.time()
    log(f"SEED={SEED}, mp.dps={mp.dps}")
    log("Phase 1: assemble Rat (T0) families from F(2,4) re-enumeration ...")
    rat_all = enumerate_F24_rat_families()
    log(f"  Rat enumerated: {len(rat_all)} (cert says 113270)")

    log("Phase 2: assemble Trans (T1) families from F(2,4) certificate ...")
    trans_24 = load_F24_trans()
    log(f"  Trans loaded: {len(trans_24)}")

    log("Phase 3: load 482-irrationals catalog ...")
    irr_482 = load_irrationals_482()
    log(f"  Irrationals loaded: {len(irr_482)}")

    # -- sample
    rng = random.Random(SEED)
    rat_sample = rng.sample(rat_all, 300)
    irr_sample = rng.sample(irr_482, 200 - len(trans_24))
    log(f"  Sampled: {len(rat_sample)} Rat (T0)  +  {len(trans_24)} F24-Trans + {len(irr_sample)} irr-482 (T1)")

    # -- assemble unified records
    records: list[dict] = []
    for r in rat_sample:
        records.append({
            "label": "T0",
            "source": "F24_Rat_" + r["rat_kind"],
            "deg_a": 2,
            "deg_b": 2,
            "a": r["a"],
            "b": r["b"],
        })
    for r in trans_24:
        records.append({
            "label": "T1",
            "source": "F24_Trans",
            "deg_a": 2,
            "deg_b": 2,
            "a": r["a"],
            "b": r["b"],
        })
    for r in irr_sample:
        records.append({
            "label": "T1",
            "source": "irr_482",
            "deg_a": 0,
            "deg_b": 2,
            "a": r["a"],
            "b": r["b"],
        })

    rng.shuffle(records)
    log(f"Total records: {len(records)}  ({sum(1 for x in records if x['label']=='T0')} T0 / "
        f"{sum(1 for x in records if x['label']=='T1')} T1)")

    # -- compute features
    log("Phase 4: feature engineering (this is the slow phase: conv_slope at dps=60, N=200) ...")
    rows: list[dict] = []
    t_feat = time.time()
    for i, rec in enumerate(records):
        a_top = rec["a"][0]
        b_top = rec["b"][0]
        a_full = rec["a"] if rec["deg_a"] >= 1 else rec["a"]
        # disc_a only meaningful when deg(a)==2
        d, d_neg, d_psq = feature_disc_a(rec["a"]) if rec["deg_a"] == 2 else (0, 0, 0)
        Rs = feature_R_struct(a_top, b_top)
        BT_d, lam_ratio, int_res, stokes = feature_BT(a_top, b_top)
        slope, r_final, fin_term = feature_conv_slope(rec["a"], rec["b"])

        row = {
            "idx": i,
            "label": rec["label"],
            "source": rec["source"],
            "deg_a": rec["deg_a"],
            "deg_b": rec["deg_b"],
            "a_str": ",".join(str(x) for x in rec["a"]),
            "b_str": ",".join(str(x) for x in rec["b"]),
            "a_top": a_top,
            "b_top": b_top,
            "R_struct": Rs,
            "disc_a": d,
            "disc_a_neg": d_neg,
            "disc_a_psq": d_psq,
            "BT_disc": BT_d,
            "lam_ratio": lam_ratio if math.isfinite(lam_ratio) else 1e9,
            "int_resonance": int_res,
            "stokes_idx": stokes,
            "conv_slope": slope if math.isfinite(slope) else 0.0,
            "r_final_log10": r_final if math.isfinite(r_final) else -1e9,
            "finite_termination": fin_term,
        }
        rows.append(row)
        if (i + 1) % 50 == 0:
            log(f"  {i+1}/{len(records)}  elapsed {time.time()-t_feat:.1f}s")
    log(f"Feature phase done in {time.time()-t_feat:.1f}s")

    # -- write CSV
    fieldnames = list(rows[0].keys())
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    log(f"Wrote {OUT_CSV.name}: {len(rows)} rows")

    # -- write features schema
    schema = {
        "seed": SEED,
        "dps": int(mp.dps),
        "n_records": len(rows),
        "n_T0": sum(1 for r in rows if r["label"] == "T0"),
        "n_T1": sum(1 for r in rows if r["label"] == "T1"),
        "feature_columns": [
            "deg_a", "deg_b",
            "R_struct",
            "disc_a", "disc_a_neg", "disc_a_psq",
            "BT_disc", "lam_ratio", "int_resonance",
            "stokes_idx",
            "conv_slope", "r_final_log10", "finite_termination",
        ],
        "label_column": "label",
        "label_values": ["T0", "T1"],
        "source_columns": ["source", "a_str", "b_str", "a_top", "b_top"],
        "build_seconds": round(time.time() - t0, 2),
    }
    OUT_FEATURES.write_text(json.dumps(schema, indent=2), encoding="utf-8")
    log(f"Wrote {OUT_FEATURES.name}")

    LOG.write_text("\n".join(log_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
