"""QL26 deep probe: a_n=-3n+1, b_n=4n^2-2n+2, Delta=-28, Q(sqrt(-7)) non-Heegner.
Best Session C cell: D-A + P-III, residual 0.024."""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from painleve_deep import deep_probe

def a_fn(n, t):  return mpf(-3)*n + mpf(1)
def bA(n, t):    return mpf(4)*n*n - mpf(2)*n + mpf(2)*(mpf(1) + t)
def bB(n, t):
    s = (mpf(1) + t)
    return mpf(4)*n*n - mpf(2)*s*n + mpf(2)*s*s

spec = {
    "family": "QL26",
    "recurrence": {"a_n": "-3 n + 1", "b_n": "4 n^2 - 2 n + 2"},
    "Delta": -28, "CM_field": "Q(sqrt(-7))", "Heegner": False,
    "L0_baseline": "1.44999402142624643523267445097379592094820809549459309494",
    "a_fn": a_fn, "b_fns": {"A": bA, "B": bB},
}

if __name__ == "__main__":
    res = deep_probe(spec, best_def="A", best_eq_name="P-III",
                     depth=3000, dps=400,
                     do_cold_scan_if_no_fit=True, extend_p2_p4=True)
    with open(Path(__file__).parent / "ql26_result.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nWrote ql26_result.json")
