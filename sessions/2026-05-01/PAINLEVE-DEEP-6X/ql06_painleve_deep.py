"""QL06 deep probe: a_n=n, b_n=2n^2+n+1, Delta=-7, Q(sqrt(-7)).
Best Session C cell: D-A + P-V, residual 1.07e-4 (entry point for Session D)."""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from painleve_deep import deep_probe

def a_fn(n, t):  return n
def bA(n, t):    return mpf(2)*n*n + n + (mpf(1) + t)
def bB(n, t):
    s = (mpf(1) + t)
    return mpf(2)*n*n + s*n + s*s

spec = {
    "family": "QL06",
    "recurrence": {"a_n": "n", "b_n": "2 n^2 + n + 1"},
    "Delta": -7, "CM_field": "Q(sqrt(-7))", "Heegner": True,
    "L0_baseline": "1.23925719836293571720484944091320106542524505238218884667",
    "a_fn": a_fn, "b_fns": {"A": bA, "B": bB},
}

if __name__ == "__main__":
    res = deep_probe(spec, best_def="A", best_eq_name="P-V",
                     depth=3000, dps=400,
                     do_cold_scan_if_no_fit=True, extend_p2_p4=True)
    with open(Path(__file__).parent / "ql06_result.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nWrote ql06_result.json")
