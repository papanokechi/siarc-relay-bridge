"""Test structural prediction at b1=18 and finalize deliverables.

Predicted: (-9, 0, 0, 18, 9) -> L = 6/log(2);
           (-9, 0, 0, -18, -9) -> L = -6/log(2).
This would confirm the b1 = 6k family (k = 1, 2, 3, ...) generates
infinite Log identities L = +/- 2k/log(2) at ratio -1/36.
"""
from __future__ import annotations
import json
from pathlib import Path

import mpmath as mp_

HERE = Path(__file__).parent


def kn_mp_deg2(coeffs, N, dps):
    a2, a1, a0, b1, b0 = coeffs
    mp_.mp.dps = dps
    a2m, a1m, a0m, b1m, b0m = (mp_.mpf(c) for c in (a2, a1, a0, b1, b0))
    Pp = mp_.mpf(1); Pc = b0m
    Qp = mp_.mpf(0); Qc = mp_.mpf(1)
    K_curr = K_prev = None
    for n in range(1, N + 1):
        an = a2m * n * n + a1m * n + a0m
        bn = b1m * n + b0m
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if Qc == 0:
            return None
        K_prev = K_curr
        K_curr = Pc / Qc
        if n % 16 == 0:
            mag = max(abs(Pc), abs(Qc), mp_.mpf(1))
            Pc /= mag; Qc /= mag; Pp /= mag; Qp /= mag
    return (K_curr, K_prev)


def main():
    out = []
    mp_.mp.dps = 220
    LN2 = mp_.log(2)
    # Test k = 1, 2, 3 ; b1 = 6k
    for k in (1, 2, 3):
        b1 = 6 * k
        a2 = -k * k
        b0 = 3 * k
        for sign in (1, -1):
            coeffs = (a2, 0, 0, sign * b1, sign * b0)
            res = kn_mp_deg2(coeffs, 2000, 220)
            if res is None:
                out.append({"k": k, "coeffs": list(coeffs), "fail": "Q=0"})
                continue
            L, Lprev = res
            diff = abs(L - Lprev)
            target = mp_.mpf(sign * 2 * k) / LN2
            resid = abs(L - target)
            # PSLQ confirm
            basis = [L * LN2, mp_.mpf(1), L]
            try:
                rel = mp_.pslq(basis, maxcoeff=10**6,
                               tol=mp_.mpf(10) ** (-150))
            except Exception:
                rel = None
            rel_resid = None
            if rel is not None:
                s = sum(int(c) * x for c, x in zip(rel, basis))
                rel_resid = mp_.nstr(abs(s), 5)
            out.append({
                "k": k,
                "coeffs": list(coeffs),
                "predicted_L": f"{sign*2*k}/log(2)",
                "L_200": mp_.nstr(L, 200),
                "tail_diff": mp_.nstr(diff, 5),
                "L_minus_target_abs": mp_.nstr(resid, 5),
                "matches_prediction": bool(resid < mp_.mpf(10) ** (-150)),
                "pslq_relation_basis": ["L*log2", "1", "L"],
                "pslq_relation": [int(c) for c in rel] if rel else None,
                "pslq_residual": rel_resid,
            })
            print(f"  k={k}, coeffs={coeffs}: L={mp_.nstr(L, 40)}  "
                  f"resid={mp_.nstr(resid,3)}  pslq={rel}")
    (HERE / "structural_extrapolation.json").write_text(
        json.dumps(out, indent=2, default=str))
    print(f"\nWrote structural_extrapolation.json")


if __name__ == "__main__":
    main()
