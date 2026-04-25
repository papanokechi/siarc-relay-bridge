"""
bsd_ratio_sweep.py — BSD-RATIO-RANK2-N10000-C1 (HALTED, NOT RUN)

Status: this script was NOT executed in BSD-RATIO-RANK2-N10000-C1
because the runtime environment is missing an L-function engine
(no Sage, no cypari2, no PARI/gp on PATH) and LMFDB's bulk API is
currently gated by a Google reCAPTCHA challenge that prevents
paginated retrieval of the 2388-curve list. See halt_log.json.

The skeleton below is preserved so that a follow-up session
(after installing cypari2 or invoking Sage) can plug in a real
L-value engine and complete the sweep. It is intentionally
written so that the L''(E,1) computation is the only stub: the
remaining BSD-ratio arithmetic uses LMFDB-cached
real_period / regulator / sha_an / tamagawa_product / torsion.

Usage (after L-engine is available):
    python bsd_ratio_sweep.py --build-curve-list   # writes bsd_curves_rank2.json
    python bsd_ratio_sweep.py --all                # writes bsd_results.jsonl
    python bsd_ratio_sweep.py --stat max_deviation # prints max |R-1|

Convention:
    R(E) = (L^(r)(E,1) / r!) / (Omega * Reg * prod_cp * Sha_an / |T|^2)
    For rank r=2, numerator is L''(E,1)/2 = special_value.

NOTE: 200 dp target is unattainable from LMFDB cache alone
(LMFDB's special_value is stored at prec=133 bits ≈ 40 dp). A
true 200 dp run requires a local L-engine.
"""

from __future__ import annotations
import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

try:
    from mpmath import mp, mpf
except ImportError:
    print("mpmath required", file=sys.stderr); sys.exit(2)

LMFDB_API = "https://www.lmfdb.org/api"
SESSION_DIR = Path(__file__).parent
CURVES_PATH = SESSION_DIR / "bsd_curves_rank2.json"
RESULTS_PATH = SESSION_DIR / "bsd_results.jsonl"

# Per-curve fatigue guard, seconds (per relay spec STEP 4 / fatigue guard).
FATIGUE_LIMIT_S = 5 * 60


def lmfdb_get(table: str, query: dict) -> dict:
    q = dict(query)
    q.setdefault("_format", "json")
    url = f"{LMFDB_API}/{table}/?{urllib.parse.urlencode(q)}"
    with urllib.request.urlopen(url, timeout=60) as r:
        body = r.read()
    if not body.lstrip().startswith(b"{"):
        raise RuntimeError(f"LMFDB returned non-JSON (likely reCAPTCHA gate) for {url}")
    return json.loads(body)


def fetch_rank2_curves(max_conductor: int = 10000) -> list[dict]:
    """Paginate LMFDB ec_curvedata for rank=2, conductor<=max_conductor."""
    out: list[dict] = []
    offset = 0
    while True:
        d = lmfdb_get(
            "ec_curvedata",
            {"rank": "i2", "conductor": f"i1-{max_conductor}", "_offset": offset},
        )
        batch = d.get("data", [])
        if not batch:
            break
        out.extend(batch)
        if not d.get("next"):
            break
        offset += len(batch)
        time.sleep(0.2)
    return out


def fetch_mwbsd(label: str) -> dict:
    d = lmfdb_get("ec_mwbsd", {"lmfdb_label": label})
    return d["data"][0]


def realfloat(rec) -> mpf:
    """Decode an LMFDB RealLiteral dict into mpf at current mp.dps."""
    if isinstance(rec, dict) and "data" in rec:
        return mpf(rec["data"])
    return mpf(rec)


def bsd_ratio_from_lmfdb(curve: dict, mw: dict) -> dict:
    """
    Compute R(E) using LMFDB-cached values.
    Returns dict with R_numerator, R_denominator, R_ratio, digits_confirmed.
    """
    special_value = realfloat(mw["special_value"])      # = L''(E,1)/2 for rank-2
    real_period = realfloat(mw["real_period"])
    sha_an = realfloat(mw["sha_an"])
    tam = mpf(mw["tamagawa_product"])
    torsion = mpf(curve["torsion"])
    # Regulator from heights[] — heights are pairwise inner products' diagonal.
    # LMFDB only stores diagonal heights; off-diagonals are not exposed via API,
    # so regulator from heights alone is incomplete for rank-2. Use curvedata.regulator.
    reg = realfloat(curve["regulator"])
    numerator = special_value
    denom = real_period * reg * tam * sha_an / (torsion * torsion)
    ratio = numerator / denom
    deviation = abs(ratio - 1)
    # Conservative count of confirmed digits versus 1 (cap at LMFDB cache precision).
    if deviation == 0:
        digits = 30
    else:
        from mpmath import log10
        digits = max(0, int(-log10(deviation)))
    return {
        "R_numerator": str(numerator),
        "R_denominator": str(denom),
        "R_ratio": str(ratio),
        "deviation": str(deviation),
        "digits_confirmed": int(min(digits, 30)),  # LMFDB cache ceiling
    }


def cmd_build_curve_list():
    curves = fetch_rank2_curves(10000)
    CURVES_PATH.write_text(json.dumps(curves, indent=2))
    print(f"wrote {len(curves)} curves to {CURVES_PATH}")


def cmd_all():
    mp.dps = 50  # LMFDB cache supports at most ~30-40 dp
    if not CURVES_PATH.exists():
        cmd_build_curve_list()
    curves = json.loads(CURVES_PATH.read_text())
    with RESULTS_PATH.open("w") as fh:
        for c in curves:
            t0 = time.time()
            label = c["lmfdb_label"]
            try:
                mw = fetch_mwbsd(label)
                res = bsd_ratio_from_lmfdb(c, mw)
                flag = float(res["deviation"]) > 1e-10
                rec = {
                    "label": label,
                    "conductor": c["conductor"],
                    **res,
                    "flag": flag,
                    "evidence_class": "near_miss" if flag else "numerical_identity",
                }
            except Exception as e:
                rec = {"label": label, "error": str(e), "flag": True,
                       "evidence_class": "near_miss"}
            fh.write(json.dumps(rec) + "\n")
            if time.time() - t0 > FATIGUE_LIMIT_S:
                print(f"fatigue guard tripped on {label}", file=sys.stderr)


def cmd_stat(which: str):
    devs = []
    with RESULTS_PATH.open() as fh:
        for line in fh:
            r = json.loads(line)
            if "deviation" in r:
                devs.append(float(r["deviation"]))
    if which == "max_deviation":
        print(max(devs) if devs else "n/a")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build-curve-list", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--stat", default=None)
    args = ap.parse_args()
    if args.build_curve_list:
        cmd_build_curve_list()
    elif args.all:
        cmd_all()
    elif args.stat:
        cmd_stat(args.stat)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
