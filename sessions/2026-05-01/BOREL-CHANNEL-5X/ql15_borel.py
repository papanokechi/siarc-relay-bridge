"""QL15 Borel-channel probe: a_n=n, b_n=3n^2-2n+2, Delta=-20, Q(sqrt(-5)), non-Heegner."""
import json, sys
from pathlib import Path
from mpmath import mpf
sys.path.insert(0, str(Path(__file__).resolve().parent))
from borel_channel import borel_probe

def a_fn(n):  return n
def b_fn(n):  return mpf(3)*n*n - mpf(2)*n + mpf(2)

spec = {"family": "QL15",
        "recurrence": {"a_n": "n", "b_n": "3 n^2 - 2 n + 2"},
        "Delta": -20, "CM_field": "Q(sqrt(-5))", "Heegner": False,
        "a_fn": a_fn, "b_fn": b_fn}

if __name__ == "__main__":
    res = borel_probe(spec, depth=200, dps=2200, K=12, M_pade=5,
                      n_lo=15, n_hi=120)
    out = Path(__file__).parent / "ql15_result.json"
    with open(out, "w") as f: json.dump(res, f, indent=2)
    print(f"\nWrote {out}")
