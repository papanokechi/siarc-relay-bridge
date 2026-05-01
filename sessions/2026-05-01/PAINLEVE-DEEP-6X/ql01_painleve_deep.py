"""QL01 deep probe: a_n=n, b_n=n^2-n+1, Delta=-3, Q(sqrt(-3)).
Best Session B/C cell: D-A (constant-term scaling) + P-III, residual 0.0084.
NB: Session A2 used three deformations D1/D2/D3; we keep D-A (=D2) and
D-B (root-radius) here for a uniform two-deformation framing."""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from painleve_deep import deep_probe

def a_fn(n, t):  return n
def bA(n, t):    return n*n - n + (mpf(1) + t)             # gamma -> (1+t) gamma
def bB(n, t):
    s = (mpf(1) + t)
    return n*n - s*n + s*s                                  # roots r=(1+/-i sqrt 3)/2 -> (1+t) r

spec = {
    "family": "QL01",
    "recurrence": {"a_n": "n", "b_n": "n^2 - n + 1"},
    "Delta": -3, "CM_field": "Q(sqrt(-3))", "Heegner": True,
    "L0_baseline": "1.39174520027073529821247847379",
    "a_fn": a_fn, "b_fns": {"A": bA, "B": bB},
}

if __name__ == "__main__":
    res = deep_probe(spec, best_def="A", best_eq_name="P-III",
                     depth=3000, dps=400,
                     do_cold_scan_if_no_fit=True, extend_p2_p4=True)
    with open(Path(__file__).parent / "ql01_result.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nWrote ql01_result.json")
