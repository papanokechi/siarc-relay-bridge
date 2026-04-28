"""T2C — PSLQ sweep at dps=300 over an extended basis.

For each of the 24 Trans families, compute L at dps=300 and run PSLQ against
{L, L^2, sqrt(17), pi, log(2), zeta(3), exp(1), gamma, 1}.

Phantom-hit rule: any relation with L-coefficient (index 0) AND L^2-coefficient
(index 1) both zero is REJECTED (no L appears at all). Otherwise accepted.

Records all accepted hits — expected count: 0 (confirms Trans-hard).
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import mpmath as mp

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from precision_escalation import TRANS_FAMILIES, cf_limit_stable

OUT = Path(__file__).resolve().parent / "pslq_sweep_300.json"
DPS = 300


def extended_basis(L: mp.mpf):
    return [
        mp.mpf(L),
        mp.mpf(L) * mp.mpf(L),
        mp.sqrt(17),
        mp.pi,
        mp.log(2),
        mp.zeta(3),
        mp.e,
        mp.euler,   # Euler-Mascheroni gamma
        mp.mpf(1),
    ]


def main():
    t0 = time.time()
    mp.mp.dps = DPS + 20
    hits = []
    rows = []

    for name, coeffs in TRANS_FAMILIES:
        t_fam = time.time()
        L = cf_limit_stable(coeffs, DPS + 30)
        mp.mp.dps = DPS
        B = extended_basis(L)
        tol = mp.mpf(10) ** (-(DPS - 5))
        try:
            rel = mp.pslq(B, tol=tol, maxcoeff=10 ** 30)
        except Exception as exc:
            rel = None
            print(f"[ERR] {name}: {exc}")

        accepted = False
        if rel is not None:
            # phantom rule: reject if neither L nor L^2 appears.
            if rel[0] != 0 or rel[1] != 0:
                accepted = True

        elapsed = time.time() - t_fam
        rows.append({
            "name": name,
            "coeffs": coeffs,
            "relation": list(rel) if rel is not None else None,
            "accepted": accepted,
            "elapsed_s": elapsed,
        })
        if accepted:
            hits.append({"name": name, "relation": list(rel)})
            print(f"[HIT!] {name}: rel={rel} ({elapsed:.1f}s)")
        else:
            print(f"[ok ] {name}: rel={rel} ({elapsed:.1f}s)")

    out = {
        "dps": DPS,
        "basis": ["L", "L^2", "sqrt(17)", "pi", "log(2)", "zeta(3)", "exp(1)", "gamma", "1"],
        "n_families": len(TRANS_FAMILIES),
        "n_hits": len(hits),
        "hits": hits,
        "rows": rows,
        "wall_seconds": time.time() - t0,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {OUT}")
    print(f"Hits: {len(hits)} / {len(TRANS_FAMILIES)} (expected 0)")
    print(f"Wall: {out['wall_seconds']:.1f}s")


if __name__ == "__main__":
    main()
