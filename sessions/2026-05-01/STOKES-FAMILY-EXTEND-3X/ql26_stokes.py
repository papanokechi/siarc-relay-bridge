"""
QL26 Stokes / Painleve probe under two CM-respecting deformations.
  a_n = -3 n + 1
  b_n = 4 n^2 - 2 n + 2
  Disc(b) = 4 - 32 = -28   CM field Q(sqrt(-7))  (non-fundamental disc -28,
                                                   intra-field cross-check vs QL06)
  Roots of b: (1 +/- i sqrt(7))/4 in Q(sqrt(-7))
  Prior L(0) = 1.44999402142624643523267445097379592094820809549459309494...
  (results/pcf_spectral_smoke40.json, "limit_300_digits", QL26)

Deformations:
  A: constant-term scaling  gamma -> (1+t) gamma
       b_n(t) = 4 n^2 - 2 n + 2 (1+t)
  B: root-radius scaling    r -> (1+t) r
       4 (x - (1+t) r)(x - (1+t) rbar) = 4 x^2 - 2 (1+t) x + 2 (1+t)^2
       b_n(t) = 4 n^2 - 2 (1+t) n + 2 (1+t)^2
"""
from mpmath import mpf
from stokes_session_b import run_session_b

def a_fn(n, t):
    return mpf(-3)*n + mpf(1)

def bA(n, t):
    return mpf(4)*n*n - mpf(2)*n + mpf(2)*(mpf(1) + t)

def bB(n, t):
    s = (mpf(1) + t)
    return mpf(4)*n*n - mpf(2)*s*n + mpf(2)*s*s

spec = {
    "family": "QL26",
    "recurrence": {"a_n": "-3 n + 1", "b_n": "4 n^2 - 2 n + 2"},
    "Delta": -28,
    "CM_field": "Q(sqrt(-7))",
    "class_number_disc": 1,  # h(-28) for the non-maximal order Z[sqrt(-7)] is 1
    "Heegner": False,        # disc -28 is NON-fundamental; QL06 (fund disc -7) is the Heegner partner
    "heun_roots": "(1 +/- i sqrt(7))/4 in Q(sqrt(-7))",
    "L0_baseline": "1.44999402142624643523267445097379592094820809549459309494389087987289114089194401545584853585813146358443828993345913798",
    "a_fn": a_fn,
    "b_fns": {"A": bA, "B": bB},
    "deformations": {
        "A": "constant-term scaling: b_n = 4 n^2 - 2 n + 2(1+t)",
        "B": "root-radius scaling:   b_n = 4 n^2 - 2(1+t) n + 2(1+t)^2",
    },
    "pslq_status": "carried forward from prior PSLQ scans (no closed-form identification, oscillatory-unknown)",
}

if __name__ == "__main__":
    run_session_b(spec, out_json_path="ql26_residuals.json")
