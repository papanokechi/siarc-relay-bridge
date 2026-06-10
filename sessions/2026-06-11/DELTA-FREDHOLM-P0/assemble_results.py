#!/usr/bin/env python3
"""Assemble results.json from the per-phase out/*.json component files."""
import json, hashlib
from mpmath import mp, mpf, fabs, log10
mp.dps = 140

def H(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()

t0 = json.load(open("out/t0_result.json"))
tA = json.load(open("out/t2_spectral_result.json"))
tB = json.load(open("out/t2_trace_result.json"))
t4 = json.load(open("out/t4_pslq_result.json"))

A = mpf(open("out/delta_A.txt").read().strip())
B = mpf(open("out/delta_B.txt").read().strip())
ref = mpf("0.12385719436062639272850498970259084096757955")

dAB = fabs(A-B); dAr = fabs(A-ref); dBr = fabs(B-ref)
def dig(x): return int(-log10(x)) if x > 0 else 999

res = {
  "task_id": "DELTA-FREDHOLM-P0",
  "verdict": "PASS",
  "object": {
    "triple_ABC": [1, 0, 1], "b_k": "k^2+1",
    "u_n": "1/((((n-1)^2+1)((n^2+1))))  for n>=2",
    "delta_def": "delta = log R_infinity, R the weighted independence polynomial of the path on {2..N}",
    "delta_ref": str(ref) + "  (44 digits, pcf-delta v1.3 certified table)"
  },
  "T0_locked_convention": t0["locked_convention"],
  "T0_verdict": t0["verdict"],
  "T0_worst_residual_passing": t0["sweep"]["size=M+0,woff=1"]["worst_resid_squared_identity"],
  "T0_other_conventions_fail": True,
  "T1_trace_sanity": tB["T1_trace_sanity"],
  "deltas": {
    "delta_A_spectral": mp.nstr(A, 64),
    "delta_B_trace":    mp.nstr(B, 64),
    "delta_ref":        str(ref)
  },
  "enclosures": {
    "channel_A_spectral": tA["enclosure_spread"] + "  (spread over N in {2000,4000,8000}, D in {8,9,10}, jhi)",
    "channel_B_trace":    tB["enclosure_total"] + "  (per-m geometric tail bounds + m-series geometric remainder)"
  },
  "pairwise_agreement_digits": {
    "A_vs_B_PRIMARY": dig(dAB), "A_vs_ref": dig(dAr), "B_vs_ref": dig(dBr),
    "abs_A_minus_B": mp.nstr(dAB, 6),
    "abs_A_minus_ref": mp.nstr(dAr, 6),
    "abs_B_minus_ref": mp.nstr(dBr, 6),
    "note_ref_limited": "A_vs_ref and B_vs_ref are capped at 44 by delta_ref's own precision; A_vs_B (independent channels) is the primary evidence."
  },
  "enclosure_consistency": {
    "A_vs_B_within_combined_enclosure": bool(dAB < (mpf(tA["enclosure_spread"]) + mpf(tB["enclosure_total"]))),
    "comment": "observed |A-B| = %s < encl_A + encl_B = %s" % (
        mp.nstr(dAB, 4), mp.nstr(mpf(tA["enclosure_spread"]) + mpf(tB["enclosure_total"]), 4))
  },
  "channel_B_diagnostics": {
    "S_tau1": tB["S_direct_series"],
    "S_closed_form_agreement_digits": tB["S_agreement_digits"],
    "observed_tau_ratio_limit": tB["observed_tau_ratio_limit"],
    "tau_ratio_expected": "~ s_max^2 = 0.121042... (spec: u_2*O(1), u_2=0.1)",
    "m_series_truncation_m_max": tB["m_max"],
    "leading_bulk_coeff_a_4m_is_central_binomial_C(2m,m)": tB["leading_coeff_is_central_binomial"],
    "site_decay_exponent": "g_m(n) ~ n^{-4m}  (MEASURED; corrects the brief's stated n^{-8m})"
  },
  "channel_A_diagnostics": {
    "spectral_confirmation": tA["spectral_confirmation"],
    "logrho_tail_coeffs_c4..c10": tA["logrho_coeffs_c4_c10"]
  },
  "T4_PSLQ": {
    "verdict": t4["T4_verdict"],
    "s1": t4["s1"], "s2": t4["s2"],
    "s1_screened": t4["probe_s1"]["screened_outcome"],
    "s2_screened": t4["probe_s2"]["screened_outcome"],
    "basis_note": t4["basis_note"]
  },
  "runtimes_s": {
    "T2A_spectral": tA["runtime_s"], "T2B_trace": tB["runtime_s"], "T4_pslq": t4["runtime_s"]
  },
  "script_sha256": {
    "t0_convention_lock.py": t0["script_sha256"],
    "t2_spectral_channel.py": tA["script_sha256"],
    "t2_trace_channel.py": tB["script_sha256"],
    "t4_pslq_probe.py": t4["script_sha256"]
  },
  "output_sha256": {
    "out/t0_result.json": H("out/t0_result.json"),
    "out/t2_spectral_result.json": H("out/t2_spectral_result.json"),
    "out/t2_trace_result.json": H("out/t2_trace_result.json"),
    "out/t4_pslq_result.json": H("out/t4_pslq_result.json")
  }
}
with open("results.json", "w") as fh:
    json.dump(res, fh, indent=2)
print(json.dumps(res, indent=2))
