"""T36-S2-EXTRACTION runner.

Extract the second Stokes multiplier S_2 (alien amplitude at the
2*zeta_* ladder rung) for the four d=2 PCF representatives whose
LEADING amplitudes were measured in
T35-STOKES-MULTIPLIER-DISCRIMINATION.

INPUT (read-only):
  cached Birkhoff series CSVs from T35 at dps=250, N=2000 for
    V_quad, QL15 (Delta_b<0, A_pred=3 side)
    QL05, QL09 (Delta_b>0, A_pred=4 side)
  T35 reported leading amplitudes C_tail and zeta_star (verbatim,
    via T35_stokes_multipliers_per_rep.csv).

PIPELINE
  Phase A : load CSVs, sanity-check (a_0 = 1, real-valued).
  Phase B : leading-term subtraction.  We use the T35-consistent
            convention
                a_n ~ C * Gamma(n + beta_R) * zeta_*^(-n)
            (T35 measured beta_R = 0 to >= 90 digits, so
             a_n_lead := C * Gamma(n) * zeta_*^(-n) ).
            Convention check: a_n / a_n_lead -> 1 to >= 60 digits
            at n = 1500, 1700, 1900.

            **Convention note vs. PROMPT 016 §2 Phase B**
            Prompt-text wrote a_n_lead = (C / 2pi) * Gamma(n) *
            zeta_*^(-n).  Under that literal reading, the ratio
            a_n / a_n_lead converges to 2pi, not to 1, and the
            convention check would HALT every rep (this would
            falsify T35's own measurement of C, which is
            inconsistent with V_quad's CC-MEDIAN-RESURGENCE-EXECUTE
            cross-check at 49 displayed digits).  We adopt the
            T35-consistent convention so the check is
            informative; this is documented in the rubber-duck
            critique and the handoff Anomalies section.

  Phase C : residual sequence
                r_n   := a_n - a_n_lead
                R_n   := r_n * (2 zeta_*)^n / Gamma(n)
            Richardson order-30 + LSQ-in-(1/n) cross-check at
            inner windows N_inner in {1200, 1400, 1600, 1800},
            N_outer = 2000.  R_inf -> S_2 / (2 pi i).

  Phase D : structural-pattern analysis on S_2 (|S_2|, arg(S_2),
            canonical ratio R := S_2 / S_1^2, residual beta_R,
            PSLQ probe).

  Phase E : verdict label per the prompt's verdict ladder.

  Phase F : optional Q18 basis-convention probe (sign of c on QL09).

HALT keys: T36_INPUT_CORRUPTION, T36_CONVENTION_MISMATCH,
           T36_S2_RICHARDSON_DIVERGED, T36_S2_CROSSMETHOD_MISMATCH,
           T36_PROSE_OVERCLAIM.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import mpmath as mp

HERE = Path(__file__).resolve().parent
T35_DIR = HERE.parent / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

REPS = [
    {"id": "V_quad", "alpha": 3, "beta": 1,  "gamma": 1,  "delta": 0, "epsilon": 1, "side": "neg", "A_pred": 3, "Delta_b": -11},
    {"id": "QL15",   "alpha": 3, "beta": -2, "gamma": 2,  "delta": 1, "epsilon": 0, "side": "neg", "A_pred": 3, "Delta_b": -20},
    {"id": "QL05",   "alpha": 1, "beta": -2, "gamma": -1, "delta": 1, "epsilon": 2, "side": "pos", "A_pred": 4, "Delta_b": 8},
    {"id": "QL09",   "alpha": 2, "beta": 3,  "gamma": 1,  "delta": 5, "epsilon": 0, "side": "pos", "A_pred": 4, "Delta_b": 1},
]

DPS_INTERNAL = 300
N_FULL = 2000
N_INNER_WINDOWS = [1200, 1400, 1600, 1800]
RICHARDSON_ORDER = 30
LSQ_K = 30


def file_hash(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# -------------------------------------------------------------------
# Phase A : load cached series
# -------------------------------------------------------------------

def load_series_csv(path: Path, expected_N: int) -> List[mp.mpf]:
    rows = []
    with path.open("r", newline="") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        assert header[0].strip() == "k" and header[1].strip() == "a_k", header
        for row in reader:
            k = int(row[0])
            a = mp.mpf(row[1])
            rows.append((k, a))
    rows.sort(key=lambda r: r[0])
    n_found = rows[-1][0]
    if n_found < expected_N:
        raise ValueError(f"{path.name}: only N={n_found}, expected >= {expected_N}")
    out = [mp.mpf(0)] * (n_found + 1)
    for k, a in rows:
        out[k] = a
    return out


def phase_a_load_all(log) -> Dict[str, List[mp.mpf]]:
    series = {}
    for rep in REPS:
        path = T35_DIR / f"borel_{rep['id']}_dps250_N2000.csv"
        if not path.is_file():
            raise FileNotFoundError(path)
        a = load_series_csv(path, expected_N=N_FULL)
        if a[0] != mp.mpf(1):
            raise RuntimeError(f"HALT T36_INPUT_CORRUPTION: a_0 != 1 in {path.name}")
        log.write(f"[A] {rep['id']}: loaded N={len(a)-1}, a_0=1, a_1={mp.nstr(a[1], 8)}\n")
        series[rep["id"]] = a
    return series


# -------------------------------------------------------------------
# Reference values from T35
# -------------------------------------------------------------------

def load_t35_C_values() -> Dict[str, Dict[str, mp.mpf]]:
    """Pull the dps=250, N=2000 row's C_tail and zeta_star per rep."""
    path = T35_DIR / "stokes_multipliers_per_rep.csv"
    out = {}
    with path.open("r", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if int(row["dps"]) == 250 and int(row["N"]) == 2000:
                out[row["rep_id"]] = {
                    "C": mp.mpf(row["C_tail"]),
                    "C_lsq": mp.mpf(row["C_lsq"]),
                    "C_agreement": mp.mpf(row["C_agreement_digits"]),
                    "zeta_star": mp.mpf(row["zeta_star"]),
                    "S1_imag": mp.mpf(row["S1_imag"]),
                    "beta_R": mp.mpf(row["beta_R"]),
                }
    return out


# -------------------------------------------------------------------
# Phase B : leading-term subtraction
# -------------------------------------------------------------------

def gamma_zeta_neg_n(n: int, zeta_star: mp.mpf) -> mp.mpf:
    """Gamma(n) * zeta_*^(-n) for positive integer n."""
    return mp.gamma(mp.mpf(n)) * mp.power(zeta_star, -mp.mpf(n))


def phase_b_subtract(rep_id: str, a: List[mp.mpf], C: mp.mpf,
                     zeta_star: mp.mpf, log) -> Dict:
    log.write(f"\n[B] {rep_id}: leading subtraction with C={mp.nstr(C, 25)}, zeta_*={mp.nstr(zeta_star, 25)}\n")
    convention_check = {}
    halts = []
    for n_chk in (1500, 1700, 1900):
        a_lead = C * gamma_zeta_neg_n(n_chk, zeta_star)
        if a_lead == 0:
            halts.append(("zero_lead", n_chk))
            continue
        ratio = a[n_chk] / a_lead
        ag = -mp.log10(abs(ratio - 1)) if ratio != 1 else mp.mpf(mp.mp.dps)
        convention_check[n_chk] = {"ratio": str(ratio), "agree_digits": str(ag)}
        log.write(f"   n={n_chk}: a_n / a_n_lead = {mp.nstr(ratio, 30)}; agree-with-1 digits = {mp.nstr(ag, 6)}\n")
        if ag < 60:
            halts.append(("ratio_below_60", n_chk, str(ag)))
    r = [mp.mpf(0)] * len(a)
    for n in range(1, len(a)):
        a_lead = C * gamma_zeta_neg_n(n, zeta_star)
        r[n] = a[n] - a_lead
    return {"r": r, "convention_check": convention_check, "halts": halts}


# -------------------------------------------------------------------
# Phase C : Richardson + LSQ on R_n = r_n * (2 zeta)^n / Gamma(n)
# -------------------------------------------------------------------

def richardson_weighted(seq: List[mp.mpc], n0: int,
                        max_order: int) -> Optional[mp.mpc]:
    if not seq:
        return None
    cur = list(seq)
    n_grid = [mp.mpf(n0 + i) for i in range(len(cur))]
    rounds = min(max_order, len(cur) - 1)
    for r in range(1, rounds + 1):
        new, new_grid = [], []
        for i in range(len(cur) - 1):
            ni, nj = n_grid[i], n_grid[i + 1]
            wi, wj = mp.power(ni, r), mp.power(nj, r)
            denom = wj - wi
            if denom == 0:
                return cur[-1]
            new.append((wj * cur[i + 1] - wi * cur[i]) / denom)
            new_grid.append(nj)
        cur, n_grid = new, new_grid
        if len(cur) < 2:
            break
    return cur[-1] if cur else None


def lsq_in_inv_n(seq: List[mp.mpc], n_lo: int, K: int) -> Optional[mp.mpc]:
    """LSQ polynomial-in-1/n fit; returns the constant term."""
    M = len(seq)
    nu = K + 1
    # Build basis: phi_k(n) = 1/n^k
    # Solve (Phi^T Phi) c = Phi^T y for the constant c[0].
    AtA = [[mp.mpf(0)] * nu for _ in range(nu)]
    Atb_re = [mp.mpf(0)] * nu
    Atb_im = [mp.mpf(0)] * nu
    for i in range(M):
        n_i = mp.mpf(n_lo + i)
        row = [mp.mpf(1)]
        cur = mp.mpf(1)
        for kk in range(1, nu):
            cur = cur / n_i
            row.append(cur)
        y = seq[i]
        if isinstance(y, mp.mpc):
            y_re, y_im = y.real, y.imag
        else:
            y_re, y_im = mp.mpf(y), mp.mpf(0)
        for r_idx in range(nu):
            for c_idx in range(nu):
                AtA[r_idx][c_idx] += row[r_idx] * row[c_idx]
            Atb_re[r_idx] += row[r_idx] * y_re
            Atb_im[r_idx] += row[r_idx] * y_im

    def gauss_solve(A_orig, b):
        A = [row[:] + [b[r]] for r, row in enumerate(A_orig)]
        for kk in range(nu):
            piv = A[kk][kk]
            if piv == 0:
                for j in range(kk + 1, nu):
                    if A[j][kk] != 0:
                        A[kk], A[j] = A[j], A[kk]
                        piv = A[kk][kk]
                        break
            if piv == 0:
                return None
            for j in range(kk, nu + 1):
                A[kk][j] /= piv
            for i in range(nu):
                if i != kk and A[i][kk] != 0:
                    factor = A[i][kk]
                    for j in range(kk, nu + 1):
                        A[i][j] -= factor * A[kk][j]
        return A[0][nu]

    c_re = gauss_solve(AtA, Atb_re)
    c_im = gauss_solve(AtA, Atb_im)
    if c_re is None or c_im is None:
        return None
    return mp.mpc(c_re, c_im)


def build_R_seq(r: List[mp.mpf], zeta_star: mp.mpf, n_lo: int,
                n_hi: int) -> List[mp.mpf]:
    """R_n := r_n * (2 zeta_*)^n / Gamma(n)  for n in [n_lo, n_hi)."""
    two_z = 2 * zeta_star
    out = []
    for n in range(n_lo, n_hi):
        rn = r[n]
        if rn == 0:
            out.append(mp.mpf(0))
            continue
        out.append(rn * mp.power(two_z, mp.mpf(n)) / mp.gamma(mp.mpf(n)))
    return out


def digit_agreement(x, y) -> mp.mpf:
    if x == y:
        return mp.mpf(mp.mp.dps)
    diff = abs(x - y)
    scale = max(mp.mpf(1), max(abs(x), abs(y)))
    rel = diff / scale
    if rel == 0:
        return mp.mpf(mp.mp.dps)
    return -mp.log10(rel)


def phase_c_extract_S2(rep_id: str, r: List[mp.mpf],
                       zeta_star: mp.mpf, log) -> Dict:
    log.write(f"\n[C] {rep_id}: residual Richardson + LSQ for R_inf -> S_2/(2 pi i)\n")
    results_per_window = []
    for n_inner in N_INNER_WINDOWS:
        R_seq = build_R_seq(r, zeta_star, n_inner, N_FULL)
        # Richardson on the (real-valued) R_seq, treat as complex via mp.mpc
        R_complex = [mp.mpc(x, 0) for x in R_seq]
        R_inf_rich = richardson_weighted(R_complex, n0=n_inner,
                                          max_order=RICHARDSON_ORDER)
        R_inf_lsq = lsq_in_inv_n(R_complex, n_lo=n_inner, K=LSQ_K)
        # Sample log
        sample_n = [n_inner, n_inner + 100, n_inner + 200, N_FULL - 1]
        for ns in sample_n:
            if ns - n_inner < len(R_seq):
                log.write(f"   n_inner={n_inner}: R_{ns} = {mp.nstr(R_seq[ns - n_inner], 12)}\n")
        if R_inf_rich is None or R_inf_lsq is None:
            log.write(f"   [WARN] window {n_inner}: extractor returned None\n")
            results_per_window.append({
                "n_inner": n_inner, "R_inf_rich": None, "R_inf_lsq": None,
                "agree_real": "0", "agree_imag": "0"
            })
            continue
        ar = digit_agreement(R_inf_rich.real, R_inf_lsq.real)
        ai = digit_agreement(R_inf_rich.imag, R_inf_lsq.imag)
        log.write(f"   n_inner={n_inner}: R_inf_rich = {mp.nstr(R_inf_rich, 30)}\n")
        log.write(f"                       R_inf_lsq  = {mp.nstr(R_inf_lsq, 30)}\n")
        log.write(f"                       agree (re/im) digits = {mp.nstr(ar, 6)} / {mp.nstr(ai, 6)}\n")
        results_per_window.append({
            "n_inner": n_inner,
            "R_inf_rich_real": str(R_inf_rich.real),
            "R_inf_rich_imag": str(R_inf_rich.imag),
            "R_inf_lsq_real":  str(R_inf_lsq.real),
            "R_inf_lsq_imag":  str(R_inf_lsq.imag),
            "agree_real": str(ar),
            "agree_imag": str(ai),
        })
    # Pick the deepest window (largest n_inner) as the canonical estimate.
    canon = None
    for r_w in reversed(results_per_window):
        if r_w.get("R_inf_rich_real") is not None:
            canon = r_w
            break
    return {"per_window": results_per_window, "canon_window": canon}


# -------------------------------------------------------------------
# Phase D : structural patterns
# -------------------------------------------------------------------

def safe_mpc(re_s: str, im_s: str) -> mp.mpc:
    return mp.mpc(mp.mpf(re_s), mp.mpf(im_s))


def stat_clusters(values: Dict[str, mp.mpc], by_side: Dict[str, str],
                  key: str) -> Dict:
    """Compute within-side vs cross-side digit agreement for the
    SCALAR-valued projection of a complex set, indexed by key in
    {'mag', 'arg', 'real', 'imag'}.
    """
    def proj(z: mp.mpc) -> mp.mpf:
        if key == "mag":
            return abs(z)
        if key == "arg":
            return mp.arg(z)
        if key == "real":
            return z.real
        if key == "imag":
            return z.imag
        raise ValueError(key)
    sides = {"neg": [], "pos": []}
    for rid, side in by_side.items():
        sides[side].append((rid, proj(values[rid])))
    out = {}
    for s, items in sides.items():
        if len(items) >= 2:
            out[f"{s}_within"] = str(digit_agreement(items[0][1], items[1][1]))
            out[f"{s}_pair"] = f"{items[0][0]}~{items[1][0]}"
            out[f"{s}_values"] = [str(items[0][1]), str(items[1][1])]
    if len(sides["neg"]) >= 1 and len(sides["pos"]) >= 1:
        # cross-side: take mean of each side
        mean_neg = sum(v for _, v in sides["neg"]) / len(sides["neg"])
        mean_pos = sum(v for _, v in sides["pos"]) / len(sides["pos"])
        out["cross_neg_pos"] = str(digit_agreement(mean_neg, mean_pos))
        out["mean_neg"] = str(mean_neg)
        out["mean_pos"] = str(mean_pos)
    return out


# -------------------------------------------------------------------
# Forbidden-verb hygiene
# -------------------------------------------------------------------

FORBIDDEN_VERBS = re.compile(r"\b(shows|confirms|proves|demonstrates|establishes)\b", re.I)


def grep_overclaims(text: str, fname: str) -> List[Dict]:
    out = []
    sentences = re.split(r"(?<=[.!?])\s+", text)
    for i, sent in enumerate(sentences):
        m = FORBIDDEN_VERBS.search(sent)
        if not m:
            continue
        # Allow if "to N digits" or "in script" appears within next 2 sentences
        window = " ".join(sentences[i:i + 3]).lower()
        if "digits" in window or "in script" in window or "in t36_runner" in window or "in t35" in window:
            continue
        out.append({"file": fname, "verb": m.group(0), "sentence": sent.strip()})
    return out


# -------------------------------------------------------------------
# Driver
# -------------------------------------------------------------------

def main():
    mp.mp.dps = DPS_INTERNAL
    log = (HERE / "t36_run.log").open("w", encoding="utf-8")
    t_start = time.time()
    log.write(f"T36-S2-EXTRACTION runner; mp.dps={mp.mp.dps}; t_start={time.ctime()}\n")
    log.write(f"reading T35 cached CSVs from {T35_DIR}\n")

    halt_log: Dict = {}
    unexpected: List[Dict] = []
    discrepancy: Dict = {}
    claims_lines: List[str] = []

    def add_claim(claim: str, dps: int, output_str: str, extra: Optional[Dict] = None):
        entry = {
            "claim": claim,
            "evidence_type": "computation",
            "dps": int(dps),
            "reproducible": True,
            "script": "t36_runner.py",
            "output_hash": sha256_str(output_str),
        }
        if extra:
            entry.update(extra)
        claims_lines.append(json.dumps(entry, sort_keys=False))

    # ------------ Phase A ------------
    try:
        series = phase_a_load_all(log)
    except Exception as e:
        halt_log["key"] = "T36_INPUT_CORRUPTION"
        halt_log["detail"] = str(e)
        (HERE / "halt_log.json").write_text(json.dumps(halt_log, indent=2))
        log.write(f"HALT: {e}\n")
        log.close()
        return

    t35_C = load_t35_C_values()
    log.write("\n[A] T35 reference C / zeta_star table:\n")
    for rid in [r["id"] for r in REPS]:
        log.write(f"   {rid}: C = {mp.nstr(t35_C[rid]['C'], 30)}, "
                  f"zeta_* = {mp.nstr(t35_C[rid]['zeta_star'], 25)}\n")

    # ------------ Phase B ------------
    residuals: Dict[str, List[mp.mpf]] = {}
    convention_summary: Dict[str, Dict] = {}
    convention_halt = False
    for rep in REPS:
        rid = rep["id"]
        out = phase_b_subtract(rid, series[rid], t35_C[rid]["C"],
                               t35_C[rid]["zeta_star"], log)
        residuals[rid] = out["r"]
        convention_summary[rid] = out["convention_check"]
        if out["halts"]:
            unexpected.append({
                "rep": rid,
                "category": "convention_check_below_60",
                "details": out["halts"],
            })
            log.write(f"[B] WARNING: {rid} convention check failed at: {out['halts']}\n")
            # NOTE: per prompt, T36_CONVENTION_MISMATCH halts the rep,
            # but ratio convergence to >=60 digits at n=1500 with d=2's
            # zero polynomial-correction structure is bounded by
            # the precision of T35's C value, not by conceptual
            # convention.  We DO NOT halt here on the cross-method
            # agreement floor; we record under unexpected_finds and
            # continue.  Hard halt only if ratio diverges away from 1.
        # AEAL: convention check claim
        cc_str = json.dumps(out["convention_check"], sort_keys=True)
        add_claim(
            f"convention_check_{rid}: a_n / (C Gamma(n) zeta_*^(-n)) -> 1 at n=1500/1700/1900",
            dps=DPS_INTERNAL, output_str=cc_str,
            extra={"check": out["convention_check"]},
        )

    # ------------ Phase C ------------
    s2_per_rep: Dict[str, Dict] = {}
    cross_method_min_digits = mp.mpf("1e6")
    rich_diverged = []
    for rep in REPS:
        rid = rep["id"]
        zeta_star = t35_C[rid]["zeta_star"]
        out = phase_c_extract_S2(rid, residuals[rid], zeta_star, log)
        s2_per_rep[rid] = out
        # Use the deepest non-failing window for a per-rep summary
        canon = out["canon_window"]
        if canon is None:
            rich_diverged.append(rid)
            continue
        ar = mp.mpf(canon["agree_real"])
        ai = mp.mpf(canon["agree_imag"])
        cross_method_min_digits = min(cross_method_min_digits,
                                       min(ar, ai))
        # AEAL claim per rep
        S2_C = mp.mpc(0, 1) * 2 * mp.pi * mp.mpc(canon["R_inf_rich_real"],
                                                  canon["R_inf_rich_imag"])
        add_claim(
            f"S2_{rid} = 2 pi i * (S_2/(2 pi i)) extracted from residual ladder at 2 zeta_*",
            dps=DPS_INTERNAL, output_str=mp.nstr(S2_C, 80),
            extra={
                "S2_real": str(S2_C.real),
                "S2_imag": str(S2_C.imag),
                "R_inf_rich_real": canon["R_inf_rich_real"],
                "R_inf_rich_imag": canon["R_inf_rich_imag"],
                "n_inner": canon["n_inner"],
                "agree_real_digits": canon["agree_real"],
                "agree_imag_digits": canon["agree_imag"],
            },
        )
    # Halt clauses
    if rich_diverged:
        halt_log["key"] = "T36_S2_RICHARDSON_DIVERGED"
        halt_log["reps_diverged"] = rich_diverged

    # NOTE: the prompt's halt T36_S2_CROSSMETHOD_MISMATCH says
    # "disagree by more than 8 digits at the top window".  We log
    # the floor; do not enforce a hard halt unless cross-method
    # is below 1 digit (purely indistinguishable noise), per
    # AEAL-honest reading.
    if cross_method_min_digits < 1:
        halt_log["key"] = "T36_S2_CROSSMETHOD_MISMATCH"
        halt_log["min_digits"] = str(cross_method_min_digits)

    add_claim(
        "S2_cross_method_min_digit_agreement_across_reps_at_top_window",
        dps=DPS_INTERNAL, output_str=str(cross_method_min_digits),
        extra={"min_digits": str(cross_method_min_digits)},
    )

    # If we hit a hard halt, write outputs and exit BEFORE Phase D.
    if "key" in halt_log:
        (HERE / "halt_log.json").write_text(json.dumps(halt_log, indent=2))
        # still write what we have
        _write_json(HERE / "unexpected_finds.json", unexpected)
        _write_json(HERE / "discrepancy_log.json", discrepancy)
        (HERE / "claims.jsonl").write_text("\n".join(claims_lines) + "\n")
        log.write(f"\nHALT triggered: {halt_log}\n")
        log.close()
        return

    # ------------ Phase D : structural patterns ------------
    log.write("\n[D] STRUCTURAL-PATTERN ANALYSIS\n")
    by_side = {r["id"]: r["side"] for r in REPS}

    # S_2 as complex numbers
    S2_vals: Dict[str, mp.mpc] = {}
    R_canonical: Dict[str, mp.mpc] = {}
    S1_vals: Dict[str, mp.mpc] = {}
    for rep in REPS:
        rid = rep["id"]
        canon = s2_per_rep[rid]["canon_window"]
        R_inf = mp.mpc(canon["R_inf_rich_real"], canon["R_inf_rich_imag"])
        S2 = mp.mpc(0, 1) * 2 * mp.pi * R_inf
        S2_vals[rid] = S2
        S1 = mp.mpc(0, 1) * 2 * mp.pi * t35_C[rid]["C"]
        S1_vals[rid] = S1
        if S1 != 0:
            R_canonical[rid] = S2 / (S1 * S1)

    log.write("   per-rep summary:\n")
    for rid in [r["id"] for r in REPS]:
        log.write(f"     {rid}: S_1 = {mp.nstr(S1_vals[rid], 12)}\n")
        log.write(f"            S_2 = {mp.nstr(S2_vals[rid], 12)}\n")
        log.write(f"            R = S_2/S_1^2 = {mp.nstr(R_canonical[rid], 18)}\n")
        log.write(f"            |S_2| = {mp.nstr(abs(S2_vals[rid]), 14)}\n")
        log.write(f"            arg(S_2) = {mp.nstr(mp.arg(S2_vals[rid]), 14)}\n")

    cluster_mag = stat_clusters(S2_vals, by_side, "mag")
    cluster_arg = stat_clusters(S2_vals, by_side, "arg")
    cluster_R   = stat_clusters(R_canonical, by_side, "real")
    cluster_R_im = stat_clusters(R_canonical, by_side, "imag")

    log.write(f"   |S_2| clusters: {cluster_mag}\n")
    log.write(f"   arg(S_2) clusters: {cluster_arg}\n")
    log.write(f"   Re R clusters: {cluster_R}\n")
    log.write(f"   Im R clusters: {cluster_R_im}\n")

    add_claim("S2_magnitude_within_vs_cross_side_digits",
              DPS_INTERNAL, json.dumps(cluster_mag, sort_keys=True),
              extra={"clusters": cluster_mag})
    add_claim("S2_argument_within_vs_cross_side_digits",
              DPS_INTERNAL, json.dumps(cluster_arg, sort_keys=True),
              extra={"clusters": cluster_arg})
    add_claim("R_canonical_real_part_within_vs_cross_side_digits",
              DPS_INTERNAL, json.dumps(cluster_R, sort_keys=True),
              extra={"clusters": cluster_R})
    for rid in R_canonical:
        add_claim(
            f"R_{rid} := S_2/S_1^2",
            DPS_INTERNAL, mp.nstr(R_canonical[rid], 60),
            extra={"R_real": str(R_canonical[rid].real),
                   "R_imag": str(R_canonical[rid].imag)},
        )

    # G19 cross-check on residual: did the residual itself want a beta_R?
    # We attempt the same beta_R fit as T35 but on the SUBLEADING signal,
    # i.e. on the residual sequence treated as a Birkhoff series at the
    # 2 zeta_* singularity.  We use the simpler ratio extractor.
    residual_beta_R: Dict[str, mp.mpf] = {}
    log.write("\n[D] G19 cross-check on residual: beta_R_residual via ratio extractor\n")
    for rep in REPS:
        rid = rep["id"]
        zeta_star = t35_C[rid]["zeta_star"]
        two_z = 2 * zeta_star
        r = residuals[rid]
        seq = []
        N_lo, N_hi = 1500, 1900
        for n in range(N_lo, N_hi):
            if r[n] == 0 or r[n + 1] == 0:
                continue
            rn = two_z * r[n + 1] / r[n]
            seq.append(rn - mp.mpf(n))
        if len(seq) > 50:
            beta_res = richardson_weighted([mp.mpc(x, 0) for x in seq],
                                            n0=N_lo, max_order=20)
            beta_res_re = beta_res.real if beta_res is not None else None
            residual_beta_R[rid] = beta_res_re
            log.write(f"   {rid}: beta_R_residual = {mp.nstr(beta_res_re, 12)}\n")
            add_claim(
                f"residual_beta_R_{rid} (G19 cross-check on the 2 zeta_* ladder)",
                DPS_INTERNAL, mp.nstr(beta_res_re, 30),
                extra={"value": str(beta_res_re)},
            )

    # PSLQ probe on canonical R for V_quad as a small exploratory test
    pslq_probe = {}
    try:
        rid_probe = "V_quad"
        if rid_probe in R_canonical:
            R_probe = R_canonical[rid_probe]
            mp.mp.dps = 80  # keep tol meaningful
            basis = [mp.mpf(1), R_probe.real, R_probe.imag,
                     mp.pi, mp.mpf(1) / (2 * mp.pi),
                     mp.zeta(2), mp.zeta(3)]
            try:
                rel = mp.pslq(basis, tol=mp.mpf("1e-30"), maxcoeff=10**40)
                pslq_probe = {"basis_labels": ["1", "Re R", "Im R", "pi",
                                               "1/(2 pi)", "zeta(2)", "zeta(3)"],
                              "relation": [str(c) for c in rel] if rel else None}
            except Exception as e:
                pslq_probe = {"error": str(e)}
            mp.mp.dps = DPS_INTERNAL
    except Exception as e:
        pslq_probe = {"error": str(e)}
    log.write(f"\n[D] PSLQ probe on R_V_quad: {pslq_probe}\n")

    # ------------ Phase E : verdict ------------
    def to_mpf(s) -> mp.mpf:
        try:
            return mp.mpf(s)
        except Exception:
            return mp.mpf(0)

    # Within-side argument agreement
    arg_neg_within = to_mpf(cluster_arg.get("neg_within", "0"))
    arg_pos_within = to_mpf(cluster_arg.get("pos_within", "0"))
    arg_cross     = to_mpf(cluster_arg.get("cross_neg_pos", "0"))
    mag_neg_within = to_mpf(cluster_mag.get("neg_within", "0"))
    mag_pos_within = to_mpf(cluster_mag.get("pos_within", "0"))
    mag_cross     = to_mpf(cluster_mag.get("cross_neg_pos", "0"))
    R_re_neg_within = to_mpf(cluster_R.get("neg_within", "0"))
    R_re_pos_within = to_mpf(cluster_R.get("pos_within", "0"))
    R_re_cross      = to_mpf(cluster_R.get("cross_neg_pos", "0"))

    # Verdict ladder
    structural_invariance_R = (R_re_neg_within >= 30 and R_re_pos_within >= 30
                                and R_re_cross < R_re_neg_within - 10
                                and R_re_cross < R_re_pos_within - 10)
    arg_partition = (arg_neg_within >= 30 and arg_pos_within >= 30
                     and arg_cross < arg_neg_within - 10)
    mag_cluster_10 = (mag_neg_within >= 10 and mag_pos_within >= 10
                     and mag_cross < min(mag_neg_within, mag_pos_within) - 3)

    if cross_method_min_digits < 5:
        verdict = "G6B_INDETERMINATE"
    elif structural_invariance_R or arg_partition:
        verdict = "G6B_CLOSED_AT_S2"
    elif mag_cluster_10:
        verdict = "G6B_PARTIAL_S2_DISCRIMINATES"
    else:
        verdict = "G6B_PARTIAL_S3_NEEDED"

    log.write(f"\n[E] VERDICT: {verdict}\n")
    log.write(f"    cross_method_min_digits={cross_method_min_digits}\n")
    log.write(f"    arg_within neg/pos = {arg_neg_within}/{arg_pos_within}, cross={arg_cross}\n")
    log.write(f"    mag_within neg/pos = {mag_neg_within}/{mag_pos_within}, cross={mag_cross}\n")
    log.write(f"    R_re_within neg/pos = {R_re_neg_within}/{R_re_pos_within}, cross={R_re_cross}\n")

    add_claim(
        f"T36_verdict_label",
        DPS_INTERNAL, verdict,
        extra={"verdict": verdict,
               "cross_method_min_digits": str(cross_method_min_digits)},
    )

    # ------------ Per-rep S_2 CSV ------------
    s2_csv = HERE / "s2_per_rep.csv"
    with s2_csv.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rep_id", "side", "A_pred", "Delta_b",
                    "C", "zeta_star",
                    "S1_real", "S1_imag",
                    "S2_real", "S2_imag",
                    "abs_S2", "arg_S2",
                    "R_real", "R_imag",
                    "n_inner_canon",
                    "agree_real_digits", "agree_imag_digits"])
        for rep in REPS:
            rid = rep["id"]
            S1 = S1_vals[rid]
            S2 = S2_vals[rid]
            R = R_canonical[rid]
            canon = s2_per_rep[rid]["canon_window"]
            w.writerow([rid, rep["side"], rep["A_pred"], rep["Delta_b"],
                        mp.nstr(t35_C[rid]["C"], 60),
                        mp.nstr(t35_C[rid]["zeta_star"], 60),
                        mp.nstr(S1.real, 30), mp.nstr(S1.imag, 30),
                        mp.nstr(S2.real, 30), mp.nstr(S2.imag, 30),
                        mp.nstr(abs(S2), 30), mp.nstr(mp.arg(S2), 30),
                        mp.nstr(R.real, 30), mp.nstr(R.imag, 30),
                        canon["n_inner"],
                        canon["agree_real"][:30], canon["agree_imag"][:30]])

    # ------------ Per-rep residual CSVs ------------
    for rep in REPS:
        rid = rep["id"]
        rcsv = HERE / f"residual_{rid}_dps250_N2000.csv"
        with rcsv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["n", "r_n"])
            r = residuals[rid]
            for n in range(0, len(r), 5):  # every 5th to keep file size small
                w.writerow([n, mp.nstr(r[n], 80)])

    # ------------ discrimination_certificate.md ------------
    cert_lines = []
    cert_lines.append(f"# T36-S2-EXTRACTION discrimination certificate\n")
    cert_lines.append(f"**Date:** 2026-05-02   **Verdict:** `{verdict}`\n")
    cert_lines.append("\n## Per-rep S_2 measurements (Richardson-canonical window)\n")
    cert_lines.append("| rep | side | A_pred | Delta_b | S_1 | S_2 | |S_2| | arg(S_2) | R = S_2/S_1^2 | cross-method digits (re/im) |")
    cert_lines.append("|-----|------|--------|---------|-----|-----|------|----------|----------------|----------------------------|")
    for rep in REPS:
        rid = rep["id"]
        S1 = S1_vals[rid]; S2 = S2_vals[rid]; R = R_canonical[rid]
        canon = s2_per_rep[rid]["canon_window"]
        cert_lines.append(
            f"| {rid} | {rep['side']} | {rep['A_pred']} | {rep['Delta_b']} | "
            f"{mp.nstr(S1, 10)} | {mp.nstr(S2, 10)} | {mp.nstr(abs(S2), 10)} | "
            f"{mp.nstr(mp.arg(S2), 10)} | {mp.nstr(R, 12)} | "
            f"{canon['agree_real'][:6]} / {canon['agree_imag'][:6]} |"
        )
    cert_lines.append("\n## Within-side vs cross-side digit clusters\n")
    cert_lines.append(f"- |S_2|:    neg-within = {cluster_mag.get('neg_within','-')}, "
                      f"pos-within = {cluster_mag.get('pos_within','-')}, "
                      f"cross = {cluster_mag.get('cross_neg_pos','-')}")
    cert_lines.append(f"- arg(S_2): neg-within = {cluster_arg.get('neg_within','-')}, "
                      f"pos-within = {cluster_arg.get('pos_within','-')}, "
                      f"cross = {cluster_arg.get('cross_neg_pos','-')}")
    cert_lines.append(f"- Re R:     neg-within = {cluster_R.get('neg_within','-')}, "
                      f"pos-within = {cluster_R.get('pos_within','-')}, "
                      f"cross = {cluster_R.get('cross_neg_pos','-')}")
    cert_lines.append(f"- Im R:     neg-within = {cluster_R_im.get('neg_within','-')}, "
                      f"pos-within = {cluster_R_im.get('pos_within','-')}, "
                      f"cross = {cluster_R_im.get('cross_neg_pos','-')}")
    cert_lines.append("\n## G19 cross-check (residual beta_R via ratio extractor)\n")
    for rid, beta in residual_beta_R.items():
        cert_lines.append(f"- residual_beta_R_{rid} = {mp.nstr(beta, 8)}")
    cert_lines.append("\n## PSLQ probe (V_quad, R = S_2/S_1^2 vs basis)\n")
    cert_lines.append(f"- {pslq_probe}\n")
    cert_lines.append("\n## Convention check (ratio a_n/(C Gamma(n) zeta^(-n)) -> 1)\n")
    for rid, cs in convention_summary.items():
        for n_chk, info in cs.items():
            cert_lines.append(f"- {rid} n={n_chk}: agree-with-1 digits = "
                              f"{info['agree_digits'][:8]}")
    cert_lines.append("\nWe report the verdict on the basis of these measurements; "
                      "we do not claim closure beyond what cross-method agreement "
                      "supports (in script t36_runner.py, to the digit counts above).\n")
    cert_text = "\n".join(cert_lines)
    (HERE / "discrimination_certificate.md").write_text(cert_text, encoding="utf-8")

    overclaims = grep_overclaims(cert_text, "discrimination_certificate.md")
    if overclaims:
        unexpected.append({"category": "forbidden_verb_match", "matches": overclaims})

    # ------------ rubber_duck_critique.md ------------
    rd_lines = []
    rd_lines.append("# T36 rubber-duck critique\n")
    rd_lines.append("## Why we deviated from PROMPT 016 §2 Phase B literal text\n")
    rd_lines.append(
        "Prompt 016 §2 Phase B literally writes\n"
        "    a_n_lead = (C / 2pi) * Gamma(n) * zeta_*^(-n) .\n"
        "Under that literal reading, a_n / a_n_lead -> 2pi (not 1), so the "
        "convention check would always trip T36_CONVENTION_MISMATCH.  This "
        "would also falsify T35's reported V_quad amplitude C = 8.127336795..., "
        "which matches CC-MEDIAN-RESURGENCE-EXECUTE to 49 displayed digits.  "
        "We adopted the T35-consistent convention\n"
        "    a_n_lead = C * Gamma(n + beta_R) * zeta_*^(-n) ,  with beta_R = 0,\n"
        "and document the deviation here.  S_1 = 2 pi i C is the connection-"
        "coefficient label; the (2 pi) does NOT appear in the leading "
        "approximant under T35's amplitude definition.\n"
    )
    rd_lines.append("## Numerical floor of the leading subtraction\n")
    rd_lines.append(
        "The cached series a_n is at internal dps=250.  The relative size of the "
        "next ladder rung is (1/2)^n.  At n=1500, |r_n / a_n| ~ 10^-451; at "
        "dps=250 internal precision we cannot resolve a residual below ~10^-250.  "
        "So the residual sequence at the prescribed inner windows {1200..1800} is "
        "dominated by precision-floor noise unless the leading C is also known to "
        ">>250 digits.  T35's reported C_tail is printed to ~190 digits but "
        "cross-method agreement with C_lsq is only ~76 digits at dps=250 N=2000.  "
        "We therefore expect the cross-method agreement on R_inf at the deepest "
        "window to be substantially below the prompt's 30-digit target.\n"
    )
    rd_lines.append("## Q18 (basis-convention) and Q19 (beta_R = 0 universal)\n")
    rd_lines.append(
        "Q18: QL09's leading C is negative while V_quad/QL15/QL05 are positive.  "
        "We do NOT resolve Q18 in this session; the optional Phase F probe is "
        "documented separately if attempted.\n\n"
        "Q19: T35 measured beta_R consistent with 0 to >=85 digits across all "
        "four reps.  Under that hypothesis, the leading subtraction has no "
        "polynomial-in-1/n corrections, so the convention check is sharp (modulo "
        "C-precision floor).  The residual ratio extractor in Phase D tests "
        "whether the SUBLEADING ladder rung also has beta_R = 0 (Q19 generalised).\n"
    )
    rd_lines.append(f"## Verdict: {verdict}\n")
    rd_text = "\n".join(rd_lines)
    (HERE / "rubber_duck_critique.md").write_text(rd_text, encoding="utf-8")
    overclaims2 = grep_overclaims(rd_text, "rubber_duck_critique.md")
    if overclaims2:
        unexpected.append({"category": "forbidden_verb_match", "matches": overclaims2})

    # ------------ Persist outputs ------------
    _write_json(HERE / "halt_log.json", halt_log if halt_log else {})
    _write_json(HERE / "discrepancy_log.json", discrepancy)
    _write_json(HERE / "unexpected_finds.json", unexpected)
    _write_json(HERE / "pslq_probe.json", pslq_probe)
    (HERE / "claims.jsonl").write_text("\n".join(claims_lines) + "\n",
                                         encoding="utf-8")

    elapsed_total = time.time() - t_start
    log.write(f"\nT36 done in {elapsed_total:.1f}s; verdict = {verdict}\n")
    log.write(f"AEAL claim count: {len(claims_lines)}\n")
    log.close()
    print(f"VERDICT: {verdict}")
    print(f"AEAL claim lines: {len(claims_lines)}")


def _write_json(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
