"""QL02 deep probe: a_n=2n+1, b_n=n^2+1, Delta=-4, Q(i).
Best Session C cell: D-A + P-III, residual 9.39e-4."""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from painleve_deep import deep_probe

def a_fn(n, t):  return mpf(2)*n + mpf(1)
def bA(n, t):    return n*n + (mpf(1) + t)
def bB(n, t):    return n*n + (mpf(1) + t)*(mpf(1) + t)

spec = {
    "family": "QL02",
    "recurrence": {"a_n": "2 n + 1", "b_n": "n^2 + 1"},
    "Delta": -4, "CM_field": "Q(i)", "Heegner": True,
    "L0_baseline": "2.04075671620311452077459081281928289091441029682552647125",
    "a_fn": a_fn, "b_fns": {"A": bA, "B": bB},
}

if __name__ == "__main__":
    res = deep_probe(spec, best_def="A", best_eq_name="P-III",
                     depth=3000, dps=400,
                     do_cold_scan_if_no_fit=True, extend_p2_p4=True)
    with open(Path(__file__).parent / "ql02_result.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nWrote ql02_result.json")
