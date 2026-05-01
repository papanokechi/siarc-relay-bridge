"""QL15 deep probe: a_n=n, b_n=3n^2-2n+2, Delta=-20, Q(sqrt(-5)) non-Heegner.
Best Session B cell: D-A + P-III, residual 0.0187."""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from painleve_deep import deep_probe

def a_fn(n, t):  return n
def bA(n, t):    return mpf(3)*n*n + mpf(-2)*n + mpf(2)*(mpf(1) + t)
def bB(n, t):
    s = (mpf(1) + t)
    return mpf(3)*n*n - mpf(2)*s*n + mpf(2)*s*s

spec = {
    "family": "QL15",
    "recurrence": {"a_n": "n", "b_n": "3 n^2 - 2 n + 2"},
    "Delta": -20, "CM_field": "Q(sqrt(-5))", "Heegner": False,
    "L0_baseline": "2.31275065430181514701803599927",
    "a_fn": a_fn, "b_fns": {"A": bA, "B": bB},
}

if __name__ == "__main__":
    res = deep_probe(spec, best_def="A", best_eq_name="P-III",
                     depth=3000, dps=400,
                     do_cold_scan_if_no_fit=True, extend_p2_p4=True)
    with open(Path(__file__).parent / "ql15_result.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nWrote ql15_result.json")
