"""
QL06 Stokes / Painleve probe under two CM-respecting deformations.
  a_n = n
  b_n = 2 n^2 + n + 1
  Disc(b) = 1 - 8 = -7    CM field Q(sqrt(-7))   h(-7)=1 (Heegner)
  Roots of b: (-1 +/- i sqrt(7))/4 in Q(sqrt(-7))
  Prior L(0) = 1.23925719836293571720484944091320106542524505238218884667...
  (results/pcf_spectral_smoke40.json, "limit_300_digits", QL06)

Deformations:
  A: constant-term scaling  gamma -> (1+t) gamma
       b_n(t) = 2 n^2 + n + (1+t)
  B: root-radius scaling    r -> (1+t) r  (sum and product of roots scale by 1+t and (1+t)^2)
       2 (x - (1+t) r)(x - (1+t) rbar) = 2 x^2 + (1+t) x + (1+t)^2
       b_n(t) = 2 n^2 + (1+t) n + (1+t)^2
"""
from mpmath import mpf
from stokes_session_b import run_session_b

def a_fn(n, t):
    return n

def bA(n, t):
    return mpf(2)*n*n + n + (mpf(1) + t)

def bB(n, t):
    s = (mpf(1) + t)
    return mpf(2)*n*n + s*n + s*s

spec = {
    "family": "QL06",
    "recurrence": {"a_n": "n", "b_n": "2 n^2 + n + 1"},
    "Delta": -7,
    "CM_field": "Q(sqrt(-7))",
    "class_number_disc": 1,
    "Heegner": True,
    "heun_roots": "(-1 +/- i sqrt(7))/4 in Q(sqrt(-7))",
    "L0_baseline": "1.23925719836293571720484944091320106542524505238218884667684209639163004678289109585382207093591911422476737928433406480",
    "a_fn": a_fn,
    "b_fns": {"A": bA, "B": bB},
    "deformations": {
        "A": "constant-term scaling: b_n = 2 n^2 + n + (1+t)",
        "B": "root-radius scaling:   b_n = 2 n^2 + (1+t) n + (1+t)^2",
    },
    "pslq_status": "carried forward from prior PSLQ scans (no closed-form identification, oscillatory-unknown)",
}

if __name__ == "__main__":
    run_session_b(spec, out_json_path="ql06_residuals.json")
