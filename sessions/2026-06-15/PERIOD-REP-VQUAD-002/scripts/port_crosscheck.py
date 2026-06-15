#!/usr/bin/env python3
# PERIOD-REP-VQUAD-002 Stage 3 (AEAL provenance) — persist the exact-port vs
# mpmath cross-check for the V_quad a_n.
#
# The exact Q(sqrt3) port lives in holonomic_recognition_q3.py
# (formal_series_coeffs_exact). The deposited mpmath reference is
# project-fingerprint/sectorial/vquad_stokes_resurgence/REPRODUCE_stokes_2piK.py
# lines 99-127 (riccati_coeffs / formal_series_coeffs). This script recomputes the
# a_n both ways and records the worst relative agreement, so claim PRV2-EXACT-1 is
# sourced to a committed artifact rather than a deleted scratch file.
import json
import mpmath as mp
from holonomic_recognition_q3 import formal_series_coeffs_exact

# --- deposited mpmath reference (verbatim port of REPRODUCE_stokes_2piK.py:99-127)
def riccati_coeffs(sigma, order):
    c = [mp.mpf(0)] * (order + 1)
    c[0] = sigma
    c[1] = -1 - sigma / 6
    d = [mp.mpf(0)] * (order + 1)
    d[0] = c[0] ** 2
    d[1] = 2 * c[0] * c[1]
    for k in range(2, order + 1):
        known = mp.fsum(c[i] * c[k - i] for i in range(1, k))
        rest = (3 * (known - (k - 1) * c[k - 1])
                + d[k - 1] + d[k - 2] + 6 * c[k - 1] + c[k - 2])
        c[k] = -rest / (6 * c[0])
        d[k] = 2 * c[0] * c[k] + known - (k - 1) * c[k - 1]
    return c

def formal_series_coeffs(order, dps):
    mp.mp.dps = dps
    sigma_rec = -1 / mp.sqrt(mp.mpf(3))
    rc = riccati_coeffs(sigma_rec, order=order + 10)
    f = [mp.mpf(0)] * (order + 1)
    for k in range(1, order + 1):
        if k + 1 < len(rc):
            f[k] = -rc[k + 1] / k
    a = [mp.mpf(0)] * (order + 1)
    a[0] = mp.mpf(1)
    for n in range(1, order + 1):
        a[n] = mp.fsum(k * f[k] * a[n - k] for k in range(1, n + 1)) / n
    return a

def main():
    ORDER = 150
    DPS = 120
    mp.mp.dps = DPS
    a_exact = formal_series_coeffs_exact(ORDER)
    a_ref = formal_series_coeffs(ORDER, DPS)

    def fr_to_mpf(fr):
        return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)

    relmax = mp.mpf(0)
    nmax = -1
    for n in range(1, ORDER + 1):
        xe = fr_to_mpf(a_exact[n].p) + fr_to_mpf(a_exact[n].q) * mp.sqrt(mp.mpf(3))
        xr = a_ref[n]
        if xr == 0:
            rel = abs(xe)
        else:
            rel = abs(xe - xr) / abs(xr)
        if rel > relmax:
            relmax = rel
            nmax = n

    out = {
        "order": ORDER,
        "dps": DPS,
        "field": "Q(sqrt3)",
        "reference": "REPRODUCE_stokes_2piK.py:99-127 (riccati_coeffs/formal_series_coeffs)",
        "port_vs_mpmath_relmax": mp.nstr(relmax, 6),
        "port_vs_mpmath_relmax_n": nmax,
        "a1_exact_pq": [str(a_exact[1].p), str(a_exact[1].q)],
        "a1_value": mp.nstr(fr_to_mpf(a_exact[1].p) + fr_to_mpf(a_exact[1].q) * mp.sqrt(mp.mpf(3)), 20),
        "note": "exact Q(sqrt3) port reproduces the deposited mpmath a_n to the relative "
                "tolerance below; provenance for claim PRV2-EXACT-1.",
    }
    path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
            r"\PERIOD-REP-VQUAD-002\scripts\port_crosscheck_results.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print("port_vs_mpmath_relmax =", out["port_vs_mpmath_relmax"], "at n =", nmax)
    print("wrote", path)

if __name__ == "__main__":
    main()
