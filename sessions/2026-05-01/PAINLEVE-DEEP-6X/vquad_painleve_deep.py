"""V_quad cross-validation: a_n=1, b_n=3n^2+n+1, Delta=-11, Q(sqrt(-11)).
Known: P-III(D6) with (alpha, beta, gamma, delta) = (1/6, 0, 0, -1/2).
Pipeline sanity check.  We try both deformations against P-III, P-V, P-VI."""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from painleve_deep import deep_probe

def a_fn(n, t):  return mpf(1)                        # a_n = 1, t-independent
def bA(n, t):    return mpf(3)*n*n + n + (mpf(1) + t)   # gamma -> (1+t) gamma
def bB(n, t):
    s = (mpf(1) + t)
    return mpf(3)*n*n + s*n + s*s                       # roots r -> (1+t) r

spec = {
    "family": "V_quad",
    "recurrence": {"a_n": "1", "b_n": "3 n^2 + n + 1"},
    "Delta": -11, "CM_field": "Q(sqrt(-11))", "Heegner": True,
    "L0_baseline": "1.94203213747112204647072823717022766370524655177",
    "a_fn": a_fn, "b_fns": {"A": bA, "B": bB},
}

if __name__ == "__main__":
    # we don't pre-pick a winner: try D-A + P-III first (matches the
    # known Painleve identification class), and force a cold scan to
    # cover D-B too.
    res = deep_probe(spec, best_def="A", best_eq_name="P-III",
                     depth=3000, dps=400,
                     do_cold_scan_if_no_fit=True,   # falls through if step1 best > 1e-4
                     extend_p2_p4=False)
    with open(Path(__file__).parent / "vquad_result.json", "w") as f:
        json.dump(res, f, indent=2)
    print("\nWrote vquad_result.json")
