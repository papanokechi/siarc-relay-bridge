"""T36-S2-EXTRACTION post-halt diagnostic.

The main runner halted with T36_S2_CROSSMETHOD_MISMATCH because Richardson
on R_n = r_n * (2 zeta_*)^n / Gamma(n) diverged: the residual r_n is
dominated by polynomial-in-1/n corrections to the leading Birkhoff
amplitude, not by the next ladder rung at 2 zeta_*.

This script EMPIRICALLY measures the first polynomial correction a_1
in the ansatz
    a_n = C * Gamma(n) * zeta_*^(-n) * (1 + a_1/n + a_2/n^2 + ...)

via Richardson on the sequence
    s_n := n * (a_n / a_n_lead - 1)   ->   a_1.

This is itself a structural result: a_1 is a NEW measurement (not in
T35) that bears on Q19 (was beta_R = 0 universal really enough to
characterise the leading?).  Output written to a_1_polynomial_corrections.csv.

DOES NOT recompute any series; reads cached T35 dps=250 / N=2000 CSVs
exactly like t36_runner.py.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import List

import mpmath as mp

HERE = Path(__file__).resolve().parent
T35_DIR = HERE.parent / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

REPS = [
    {"id": "V_quad", "side": "neg", "A_pred": 3, "Delta_b": -11},
    {"id": "QL15",   "side": "neg", "A_pred": 3, "Delta_b": -20},
    {"id": "QL05",   "side": "pos", "A_pred": 4, "Delta_b": 8},
    {"id": "QL09",   "side": "pos", "A_pred": 4, "Delta_b": 1},
]


def load_csv(path: Path) -> List[mp.mpf]:
    rows = []
    with path.open("r", newline="") as fh:
        rd = csv.reader(fh)
        next(rd)  # header
        for row in rd:
            rows.append((int(row[0]), mp.mpf(row[1])))
    rows.sort(key=lambda r: r[0])
    out = [mp.mpf(0)] * (rows[-1][0] + 1)
    for k, a in rows:
        out[k] = a
    return out


def load_t35_C():
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


def richardson(seq, n0, max_order):
    cur = list(seq)
    n_grid = [mp.mpf(n0 + i) for i in range(len(cur))]
    rounds = min(max_order, len(cur) - 1)
    for r in range(1, rounds + 1):
        new, new_grid = [], []
        for i in range(len(cur) - 1):
            ni, nj = n_grid[i], n_grid[i + 1]
            wi, wj = mp.power(ni, r), mp.power(nj, r)
            new.append((wj * cur[i + 1] - wi * cur[i]) / (wj - wi))
            new_grid.append(nj)
        cur, n_grid = new, new_grid
        if len(cur) < 2:
            break
    return cur[-1] if cur else None


def main():
    mp.mp.dps = 280
    t35 = load_t35_C()

    rows = [["rep_id", "side", "A_pred", "Delta_b",
             "a1_richardson", "a1_at_n1500", "a1_at_n1900",
             "agree_a1_n_digits"]]

    print("# Empirical first polynomial correction a_1 (Richardson)")
    print(f"# ansatz: a_n = C * Gamma(n) * zeta_*^(-n) * (1 + a_1/n + a_2/n^2 + ...)")
    print()

    for rep in REPS:
        rid = rep["id"]
        a = load_csv(T35_DIR / f"borel_{rid}_dps250_N2000.csv")
        C = t35[rid]["C"]
        z = t35[rid]["zeta_star"]
        # Build s_n = n * (a_n / a_lead - 1) over a wide window
        N_lo, N_hi = 200, 1500
        s_seq = []
        for n in range(N_lo, N_hi):
            a_lead = C * mp.gamma(mp.mpf(n)) * mp.power(z, -mp.mpf(n))
            ratio = a[n] / a_lead
            s_seq.append(mp.mpf(n) * (ratio - 1))
        a1_rich = richardson(s_seq, n0=N_lo, max_order=40)
        # Sanity samples
        s_at_1500 = mp.mpf(1500) * (a[1500] / (C * mp.gamma(mp.mpf(1500)) * mp.power(z, -mp.mpf(1500))) - 1)
        s_at_1900 = mp.mpf(1900) * (a[1900] / (C * mp.gamma(mp.mpf(1900)) * mp.power(z, -mp.mpf(1900))) - 1)
        # Digit agreement between two endpoint-flavoured estimators
        # (s_at_1500 vs s_at_1900: should agree as a_1 + O(1/n) -> a_1)
        diff = abs(s_at_1500 - s_at_1900)
        agree = -mp.log10(diff / max(mp.mpf(1), abs(s_at_1500))) if diff != 0 else mp.mpf(280)
        print(f"{rid} (side={rep['side']}, A={rep['A_pred']}, Delta_b={rep['Delta_b']}):")
        print(f"   a1_richardson    = {mp.nstr(a1_rich, 30)}")
        print(f"   s(1500)          = {mp.nstr(s_at_1500, 18)}")
        print(f"   s(1900)          = {mp.nstr(s_at_1900, 18)}")
        print(f"   |s(1500)-s(1900)| -> rel digits ~ {mp.nstr(agree, 6)}")
        print()
        rows.append([rid, rep["side"], rep["A_pred"], rep["Delta_b"],
                     mp.nstr(a1_rich, 30),
                     mp.nstr(s_at_1500, 30),
                     mp.nstr(s_at_1900, 30),
                     mp.nstr(agree, 6)])

    with (HERE / "a1_polynomial_corrections.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        for r in rows:
            w.writerow(r)
    print(f"wrote {HERE / 'a1_polynomial_corrections.csv'}")


if __name__ == "__main__":
    main()
