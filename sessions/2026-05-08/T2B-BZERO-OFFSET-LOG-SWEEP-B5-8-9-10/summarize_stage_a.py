"""T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10 -- partial-state summarizer.

Reads stage_a_cache.json (Stage A convergence filter results) and emits
stage_a_summary.json with per-b1 counts.  Used to produce deterministic
AEAL claims for the partial-state HALT_044_WALL_BUDGET_EXCEEDED bridge
push (Stage B/C PSLQ classification did not complete in wall budget).

The b1=7 outlier and b1=6 Bauer-orbit data points referenced by the
relay are NOT part of this sweep range and are not enumerated here.
"""
import json
import hashlib
from collections import defaultdict
from pathlib import Path

OUT_DIR = Path(__file__).parent
CACHE = OUT_DIR / "stage_a_cache.json"
SUMMARY = OUT_DIR / "stage_a_summary.json"

B1_VALUES = [5, 8, 9, 10]
A2_VALUES = [a for a in range(-30, 31) if a != 0]
COEFFS_FREE = list(range(-5, 6))
EXPECTED_PER_B1_TOTAL = len(A2_VALUES) * len(COEFFS_FREE) ** 3  # 60 * 11^3 = 79860


def main():
    if not CACHE.exists():
        raise SystemExit("stage_a_cache.json missing")
    cache = json.loads(CACHE.read_text())
    convergent = cache["convergent"]
    cache_total = cache["total"]
    cache_dt = cache.get("stage_a_seconds")
    cache_n_stagea = cache.get("n_stagea")

    per_b1 = defaultdict(lambda: {
        "total_enumerated": EXPECTED_PER_B1_TOTAL,
        "convergent": 0,
        "convergent_a2_neg": 0,
        "convergent_a2_pos": 0,
    })
    for entry in convergent:
        b1, _ratio, coeffs, _L = entry
        a2 = coeffs[0]
        per_b1[b1]["convergent"] += 1
        if a2 < 0:
            per_b1[b1]["convergent_a2_neg"] += 1
        else:
            per_b1[b1]["convergent_a2_pos"] += 1

    summary = {
        "stage_a_total_enumerated": cache_total,
        "stage_a_total_convergent": len(convergent),
        "stage_a_seconds": cache_dt,
        "stage_a_n_stagea": cache_n_stagea,
        "per_b1": {str(b1): dict(per_b1[b1]) for b1 in B1_VALUES},
    }
    SUMMARY.write_text(json.dumps(summary, indent=2))
    print(f"[OK] wrote {SUMMARY.name} ({SUMMARY.stat().st_size} B)")
    print(f"  total: {cache_total}  convergent: {len(convergent)}")
    for b1 in B1_VALUES:
        d = per_b1[b1]
        print(f"  b1={b1}: enum={d['total_enumerated']} conv={d['convergent']}"
              f" (a2<0: {d['convergent_a2_neg']}, a2>=0: {d['convergent_a2_pos']})")
    h = hashlib.sha256(SUMMARY.read_bytes()).hexdigest()
    print(f"summary sha256: {h}")
    return summary, h


if __name__ == "__main__":
    main()
