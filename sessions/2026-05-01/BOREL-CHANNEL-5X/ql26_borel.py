"""QL26 Borel-channel probe: a_n=-3n+1, b_n=4n^2-2n+2, Delta=-28, Q(sqrt(-7)), non-Heegner."""
import json, sys
from pathlib import Path
from mpmath import mpf
sys.path.insert(0, str(Path(__file__).resolve().parent))
from borel_channel import borel_probe

def a_fn(n):  return -mpf(3)*n + mpf(1)
def b_fn(n):  return mpf(4)*n*n - mpf(2)*n + mpf(2)

spec = {"family": "QL26",
        "recurrence": {"a_n": "-3 n + 1", "b_n": "4 n^2 - 2 n + 2"},
        "Delta": -28, "CM_field": "Q(sqrt(-7))", "Heegner": False,
        "a_fn": a_fn, "b_fn": b_fn}

if __name__ == "__main__":
    res = borel_probe(spec, depth=200, dps=2200, K=12, M_pade=5,
                      n_lo=15, n_hi=120)
    out = Path(__file__).parent / "ql26_result.json"
    with open(out, "w") as f: json.dump(res, f, indent=2)
    print(f"\nWrote {out}")
