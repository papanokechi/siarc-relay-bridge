"""
QL02 Stokes / Painleve probe under two CM-respecting deformations.
  a_n = 2 n + 1
  b_n = n^2 + 1
  Disc(b) = -4         CM field Q(i)            h(-4)=1 (Heegner)
  Roots of b: +/- i in Q(i)
  Prior L(0) = 2.04075671620311452077459081281928289091441029682552647125...
  (results/pcf_spectral_smoke40.json, "limit_300_digits", QL02)

Deformations:
  A: constant-term scaling  gamma -> (1+t) gamma
       b_n(t) = n^2 + (1+t)
  B: root-radius scaling    r -> (1+t) r
       b(x;t) = (x - i(1+t))(x + i(1+t)) = x^2 + (1+t)^2
       b_n(t) = n^2 + (1+t)^2
"""
from mpmath import mpf
from stokes_session_b import run_session_b

def a_fn(n, t):
    return mpf(2)*n + mpf(1)

def bA(n, t):
    return n*n + (mpf(1) + t)

def bB(n, t):
    return n*n + (mpf(1) + t)*(mpf(1) + t)

spec = {
    "family": "QL02",
    "recurrence": {"a_n": "2 n + 1", "b_n": "n^2 + 1"},
    "Delta": -4,
    "CM_field": "Q(i)",
    "class_number_disc": 1,
    "Heegner": True,
    "heun_roots": "+/- i in Q(i)",
    "L0_baseline": "2.04075671620311452077459081281928289091441029682552647125742914541615342377055251177005814103804026394521394428245516393",
    "a_fn": a_fn,
    "b_fns": {"A": bA, "B": bB},
    "deformations": {
        "A": "constant-term scaling: b_n = n^2 + (1+t)",
        "B": "root-radius scaling:   b_n = n^2 + (1+t)^2",
    },
    "pslq_status": "carried forward from prior PSLQ scans (no closed-form identification, oscillatory-unknown)",
}

if __name__ == "__main__":
    run_session_b(spec, out_json_path="ql02_residuals.json")
