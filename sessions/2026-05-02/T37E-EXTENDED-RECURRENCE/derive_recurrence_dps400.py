"""T37E-EXTENDED-RECURRENCE Phase 0: extended Birkhoff recurrence.

Re-derives the four-rep d=2 PCF Birkhoff formal series at
dps=400, N=5000.  Recurrence kernel is lifted verbatim from
T35-STOKES-MULTIPLIER-DISCRIMINATION/t35_runner.py
(function ``birkhoff_series``), with only the precision and
truncation parameters changed.

Resumable: per-rep output CSV ``a_n_<rep>_dps400_N5000.csv`` is
written incrementally; on restart the runner scans the existing
CSV, recovers the last completed n, and continues from there.

Convention (T35-internal, inherited from 017c):
    a_n_lead := C * Gamma(n) * zeta_*^(-n)
NO 2*pi factor.  This is the documented deviation from the
prompt-016 literal; T35 / 017c authoritative.

Usage:
    python derive_recurrence_dps400.py
"""
from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import mpmath as mp

HERE = Path(__file__).resolve().parent
T35_DIR = HERE.parent / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

DPS = 400
N_MAX = 5000
WORK_DPS = DPS + 50  # guard digits, mirrors t35_runner.py

REP_NAMES = ["V_quad", "QL15", "QL05", "QL09"]


def load_reps() -> List[Dict]:
    with (T35_DIR / "representatives.json").open("r") as fh:
        data = json.load(fh)
    by_id = {r["id"]: r for r in data["representatives"]}
    return [by_id[n] for n in REP_NAMES]


def csv_path(rep_id: str) -> Path:
    return HERE / f"a_n_{rep_id}_dps400_N5000.csv"


def load_existing(path: Path) -> Tuple[List[Optional[mp.mpf]], int]:
    """Return (a_array_size_N_max+1, last_completed_n)."""
    a = [None] * (N_MAX + 1)
    last = -1
    if not path.exists():
        return a, last
    with path.open("r", newline="") as fh:
        rd = csv.reader(fh)
        header = next(rd, None)
        if header is None or header[0] != "n":
            return a, last
        for row in rd:
            try:
                k = int(row[0])
            except (ValueError, IndexError):
                continue
            if 0 <= k <= N_MAX:
                a[k] = mp.mpf(row[1])  # rec is real-valued
                if k > last:
                    last = k
    return a, last


def append_row(path: Path, n: int, value: mp.mpf):
    new = not path.exists()
    with path.open("a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["n", "a_n_real", "a_n_imag"])
        # Record at full WORK_DPS precision (well above target dps=400).
        s = mp.nstr(value, WORK_DPS, strip_zeros=False)
        w.writerow([n, s, "0"])


def derive_one(rep: Dict, log) -> Tuple[List[mp.mpf], mp.mpf, mp.mpf]:
    """Derive a_0, ..., a_{N_MAX} for one rep, resumable."""
    rid = rep["id"]
    path = csv_path(rid)

    mp.mp.dps = WORK_DPS

    alpha = mp.mpf(rep["alpha"])
    beta  = mp.mpf(rep["beta"])
    gamma = mp.mpf(rep["gamma"])
    delta = mp.mpf(rep["delta"])
    epsi  = mp.mpf(rep["epsilon"])

    # Sign pinning: T35 t35_runner.py uses sign=+1 when caching the
    # canonical CSV (borel_<rep>_dps250_N2000.csv).  Same here.
    sign = mp.mpf(+1)
    c = sign * mp.mpf(2) / mp.sqrt(alpha)
    rho = mp.mpf(-3) / 2 - beta / alpha
    zeta_star = 2 * abs(c)

    # Recurrence constants (verbatim t35_runner.py)
    coeff_km1_quad = alpha / mp.mpf(16)
    base_km1 = gamma - beta * beta / (4 * alpha)
    Ukm2 = -c * delta / 2
    base_km3 = epsi - beta * delta / (2 * alpha)
    diag_premul = alpha * c / 2

    a, last = load_existing(path)
    if last < 0:
        a[0] = mp.mpf(1)
        append_row(path, 0, a[0])
        last = 0
    log.write(f"[{rid}] resume from n={last}, target N={N_MAX}\n")
    log.flush()

    # Validate: first 3 entries match, otherwise the cache is stale.
    if last >= 1 and a[1] is not None:
        # Reconstruct a[1] freshly: U_{0}(1)*a[0] / diag(1) = U_{0}(1) / diag(1)
        two_km1 = mp.mpf(1)
        Ukm1 = coeff_km1_quad * (two_km1 ** 2) + base_km1
        diag = diag_premul * mp.mpf(1)
        a1_check = Ukm1 / diag
        if abs(a1_check - a[1]) > mp.mpf(10) ** (-DPS + 20):
            raise RuntimeError(
                f"Cache stale for {rid}: a[1] disagrees with re-derivation"
            )

    t0 = time.time()
    for k in range(last + 1, N_MAX + 1):
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
        append_row(path, k, a[k])
        if k % 200 == 0 or k == N_MAX:
            mag = int(mp.log10(abs(a[k]))) if a[k] != 0 else 0
            elapsed = time.time() - t0
            log.write(f"[{rid}] k={k:5d} a_k~10^{mag} t={elapsed:.1f}s\n")
            log.flush()

    return a, c, zeta_star


def main():
    HERE.mkdir(parents=True, exist_ok=True)
    log_path = HERE / "phase0_recurrence.log"
    summary = {}
    reps = load_reps()
    with log_path.open("a") as log:
        log.write(f"\n=== Phase 0 run start ({time.strftime('%Y-%m-%d %H:%M:%S')}) ===\n")
        log.write(f"DPS={DPS}, N_MAX={N_MAX}, WORK_DPS={WORK_DPS}\n")
        log.flush()
        for rep in reps:
            t_rep = time.time()
            a, c, zeta_star = derive_one(rep, log)
            elapsed = time.time() - t_rep
            log.write(f"[{rep['id']}] DONE in {elapsed:.1f}s\n")
            summary[rep["id"]] = {
                "c": mp.nstr(c, 80),
                "zeta_star": mp.nstr(zeta_star, 80),
                "a_N_max_log10_abs": (
                    int(mp.log10(abs(a[N_MAX]))) if a[N_MAX] != 0 else None
                ),
                "elapsed_sec": elapsed,
            }
            log.flush()
        log.write(f"=== Phase 0 run end ===\n")
    with (HERE / "phase0_summary.json").open("w") as fh:
        json.dump(summary, fh, indent=2, default=str)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()
