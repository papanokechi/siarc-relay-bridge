#!/usr/bin/env python3
"""
P06-DESERT-VALIDATION Step 1: Positive control at degree profile (2,1)

Re-evaluates the 24 F(2,4) Trans-stratum families from the P11 base-case
paper using the desert paper's pipeline (forward Wallis recurrence at
130 dps, PSLQ at maxcoeff=10000) and confirms recovery of their known
pi-rational relations.

Design note (basis): the desert paper's 12-element basis B contains
pi^2 but NOT pi.  The F(2,4) Trans families lie in Q(pi) (relations of
shape c0 + c1*K + c2*pi + c3*K*pi = 0), so they cannot be recovered
against the literal desert basis -- by construction the desert search
purposefully excludes Q(pi) targets, which is precisely the
"Trans-stratum" the (4,3)/(5,3) sweep is testing for.  For the positive
control to be meaningful, we therefore extend B with pi
(EXTENDED_BASIS = B U {pi}) and run PSLQ on the 14-vector
(K, 1, pi, zeta3, pi^2, ln^2(2), G, pi*ln(2), zeta(5), pi^4/90,
 pi^2*ln(2), zeta(3)*pi^2, zeta(3)*ln(2), zeta(2)*ln(2)^2).

A "recovered" hit is any non-zero PSLQ relation involving K with
|c_i| <= 10,000 whose support is contained in {1, K, pi, K*pi}; the
F(2,4) Trans relations are bilinear (Mobius transforms of pi), so we
also include K*pi in the extended basis.  This matches the "T1 basis"
[1, K, pi, K*pi, K^2] used by P11 (Theorem T1 of the F(2,4) base
case).

Outputs: step1_positive_control_result.json  (per-family record)
"""
import json
import time
from pathlib import Path
from mpmath import mp, mpf, pi as mp_pi, zeta, log, catalan, pslq

HERE = Path(__file__).resolve().parent
TRANS_PATH = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\trans_families.json")

DPS = 130
N_TERMS = 600  # generous for degree-2 PCFs (all converge by ~100)
MAXCOEFF = 10000


def eval_pcf(a_coeffs, b_coeffs, N, dps):
    """Forward Wallis recurrence; a_coeffs, b_coeffs are [a2,a1,a0]."""
    mp.dps = dps + 50
    a2, a1, a0 = mpf(a_coeffs[0]), mpf(a_coeffs[1]), mpf(a_coeffs[2])
    b2, b1, b0 = mpf(b_coeffs[0]), mpf(b_coeffs[1]), mpf(b_coeffs[2])
    Pp, Pc = mpf(1), b0
    Qp, Qc = mpf(0), mpf(1)
    for n in range(1, N + 1):
        nn = mpf(n)
        an = a2 * nn * nn + a1 * nn + a0
        bn = b2 * nn * nn + b1 * nn + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 60 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10) ** 20:
                Pp /= s; Pc /= s; Qp /= s; Qc /= s
    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)


def main():
    t_start = time.time()
    families = json.loads(TRANS_PATH.read_text())
    assert len(families) == 24, f"expected 24, got {len(families)}"

    # Pre-compute extended basis at high precision
    mp.dps = DPS + 50
    PI = mp_pi
    z3 = zeta(3)
    pi2 = PI ** 2
    ln2 = log(2)
    ln2sq = ln2 ** 2
    cat = catalan
    piln2 = PI * ln2
    z5 = zeta(5)
    pi4_90 = PI ** 4 / 90
    pi2ln2 = pi2 * ln2
    z3pi2 = z3 * pi2
    z3ln2 = z3 * ln2
    z2ln2sq = (pi2 / 6) * ln2sq

    BNAMES = ["V", "1", "pi", "Vpi", "zeta3", "pi2", "ln2sq", "Cat",
              "piln2", "zeta5", "pi4_90", "pi2ln2", "z3pi2",
              "z3ln2", "z2ln2sq"]

    def basis(V):
        return [V, mpf(1), PI, V * PI, z3, pi2, ln2sq, cat, piln2, z5,
                pi4_90, pi2ln2, z3pi2, z3ln2, z2ln2sq]

    results = []
    recovered = 0
    for tf in families:
        idx = tf["index"]
        a = tf["family"]["a"]
        b = tf["family"]["b"]
        K = eval_pcf(a, b, N_TERMS, DPS)
        if K is None:
            results.append({"index": idx, "a": a, "b": b,
                            "value": None, "status": "diverged"})
            continue
        mp.dps = DPS
        bv = basis(K)
        try:
            rel = pslq(bv, maxcoeff=MAXCOEFF, maxsteps=5000)
        except Exception as e:
            rel = None
        if rel is None or (rel[0] == 0 and rel[3] == 0):
            results.append({
                "index": idx, "a": a, "b": b,
                "value_str": str(K)[:60],
                "status": "no_relation_with_K",
                "relation": rel,
            })
            continue
        # Compute residual
        resid = abs(sum(c * x for c, x in zip(rel, bv)))
        # "Recovered" iff support is within the pi-affine subspace
        # spanned by {V, 1, pi, V*pi, pi^2}.  PSLQ may multiply the
        # canonical T1 relation 0 = c0 + c1*V + c2*pi + c3*V*pi by pi,
        # producing a pi^2 term; both forms are equivalent.
        # BNAMES: V(0) 1(1) pi(2) Vpi(3) zeta3(4) pi2(5) ln2sq(6) ...
        forbidden = [4] + list(range(6, len(rel)))
        support_pi_only = all(rel[i] == 0 for i in forbidden)
        rec = bool(support_pi_only)
        if rec:
            recovered += 1
        results.append({
            "index": idx, "a": a, "b": b,
            "value_str": str(K)[:60],
            "status": "recovered" if rec else "relation_outside_pi_subspace",
            "relation": [int(c) for c in rel],
            "basis_names": BNAMES,
            "residual_log10": float(mp.log10(resid)) if resid > 0 else -999.0,
        })

    out = {
        "task": "P06-DESERT-VALIDATION-STEP1",
        "description": "Positive control: PSLQ recovery of F(2,4) Trans families using desert pipeline + extended basis (B U {pi}).",
        "dps": DPS, "n_terms": N_TERMS, "maxcoeff": MAXCOEFF,
        "n_families": len(families),
        "n_recovered_pi_only_subspace": recovered,
        "wall_clock_s": time.time() - t_start,
        "results": results,
    }
    out_path = HERE / "step1_positive_control_result.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"DONE: {recovered}/{len(families)} F(2,4) Trans families recovered in pi-only subspace")
    print(f"Output: {out_path}")
    print(f"Wall clock: {out['wall_clock_s']:.1f} s")


if __name__ == "__main__":
    main()
