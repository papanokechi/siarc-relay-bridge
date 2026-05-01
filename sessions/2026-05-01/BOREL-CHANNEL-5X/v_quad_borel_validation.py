"""V_quad Borel-channel validation.

V_quad PCF: a_n = 1, b_n = 3 n^2 + n + 1 (Delta=-11, Q(sqrt(-11))).
Known (L(t) channel): P-III(D6) (alpha,beta,gamma,delta) = (1/6, 0, 0, -1/2).

This is the pipeline gate.  It must produce a meaningful Borel-plane
catalog and (for full validation) recover the known P-III parameters in
the Borel channel.  If gate fails, we still report all 5 family scans
but flag the result honestly.
"""
import json, sys
from pathlib import Path
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from borel_channel import borel_probe

def a_fn(n):  return mpf(1)
def b_fn(n):  return mpf(3)*n*n + n + mpf(1)

spec = {
    "family": "V_quad",
    "recurrence": {"a_n": "1", "b_n": "3 n^2 + n + 1"},
    "Delta": -11, "CM_field": "Q(sqrt(-11))", "Heegner": True,
    "L_star_baseline": "1.94203213747112204647072823717022766370524655177",
    "a_fn": a_fn, "b_fn": b_fn,
}

if __name__ == "__main__":
    res = borel_probe(spec, depth=200, dps=2200, K=12, M_pade=5,
                      n_lo=15, n_hi=120)
    out = Path(__file__).parent / "vquad_result.json"
    with open(out, "w") as f:
        json.dump(res, f, indent=2)
    print(f"\nWrote {out}")
