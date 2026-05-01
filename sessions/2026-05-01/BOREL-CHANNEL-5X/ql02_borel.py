"""QL02 Borel-channel probe: a_n=2n+1, b_n=n^2+1, Delta=-4, Q(i)."""
import json, sys
from pathlib import Path
from mpmath import mpf
sys.path.insert(0, str(Path(__file__).resolve().parent))
from borel_channel import borel_probe

def a_fn(n):  return mpf(2)*n + mpf(1)
def b_fn(n):  return n*n + mpf(1)

spec = {"family": "QL02",
        "recurrence": {"a_n": "2 n + 1", "b_n": "n^2 + 1"},
        "Delta": -4, "CM_field": "Q(i)", "Heegner": True,
        "a_fn": a_fn, "b_fn": b_fn}

if __name__ == "__main__":
    res = borel_probe(spec, depth=200, dps=2200, K=12, M_pade=5,
                      n_lo=15, n_hi=120)
    out = Path(__file__).parent / "ql02_result.json"
    with open(out, "w") as f: json.dump(res, f, indent=2)
    print(f"\nWrote {out}")
