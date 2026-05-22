"""
harness_certified/certified_constants.py — Milestone 1: certified 15-vector basis.

Authority chain
===============
- Work order: "Validated-Arithmetic Re-Run for d824d5ae Revision" (siarc relay).
- Basis predicate: lit-002 (BBC 1997) Test 1 / Test 2 outline, generalized in
  the existing empirical harness `harness/basis.py` to the 15-dim B_D(C) basis
  for D=6 with C = {pi, e, ln 2, gamma, zeta(2), zeta(3), G}.
- The certified tier here is a STRICTLY ADDITIVE re-implementation in
  python-flint / Arb ball arithmetic. The existing mpmath harness in
  ../harness/ is unchanged.

15-basis entries (same order as harness/basis.py)
================================================
   0  1            (the exact integer)
   1  K_0
   2  K_0^2
   3  K_0^3
   4  K_0^4
   5  K_0^5
   6  K_0^6
   7  log(K_0)
   8  K_0 * pi
   9  K_0 * e
  10  K_0 * ln(2)
  11  K_0 * gamma             (Euler-Mascheroni)
  12  K_0 * zeta(2)
  13  K_0 * zeta(3)
  14  K_0 * G                 (Catalan)

Every entry is an Arb ball with a CERTIFIED radius. Classical constants use
native Arb routines (the radius reflects Arb's own internal-precision
guarantee). K_0 uses the BBC 1997 eq.(1) series with an explicit closed-form
tail bound (see bbc_series.py and BBC_FORMULA_VERIFIED.md).

HONESTY NOTE: All certifications are *conditional on the load-bearing facts*
listed in the dependency ledger at the bottom of the produced JSON output:
  - python-flint / FLINT (Arb) correctness
  - BBC 1997 eq.(1) (the algebraic identity, NOT re-derived here)

Usage
=====
    python certified_constants.py 7178                # P_bits target
    python certified_constants.py 7178 --json out.json
"""

from __future__ import annotations
import json
import sys
import time
from dataclasses import dataclass, field, asdict
from typing import Any

from flint import arb, ctx

from bbc_series import (
    certified_K0,
    bbc_tail_bound,
    required_N_for_precision,
    GUARD_BITS,
)

BASIS_LABELS = (
    "1",
    "K_0",
    "K_0^2",
    "K_0^3",
    "K_0^4",
    "K_0^5",
    "K_0^6",
    "log(K_0)",
    "K_0*pi",
    "K_0*e",
    "K_0*ln2",
    "K_0*gamma",
    "K_0*zeta(2)",
    "K_0*zeta(3)",
    "K_0*G",
)
N_BASIS = 15
assert len(BASIS_LABELS) == N_BASIS


# Map from "generating constant" name to a label and a builder callable.
# A "generating constant" is one of the 9 inputs to the basis construction.
GENERATOR_LABELS = ("1", "K_0", "pi", "e", "ln2", "gamma", "zeta2", "zeta3", "catalan")


def _ball_to_dict(x: arb) -> dict[str, Any]:
    """Serialise an Arb ball as JSON-safe dict with full-precision strings."""
    return {
        "midpoint_str": str(x.mid()),
        "radius_str": str(x.rad()),
        "arb_repr": str(x),
    }


@dataclass
class CertifiedBasis:
    """The 15-vector basis, plus the 9 generators, plus audit metadata."""

    prec_bits: int
    N_truncation: int
    guard_bits: int
    generators: dict[str, arb] = field(default_factory=dict)
    basis: list[arb] = field(default_factory=list)
    K0_audit: dict[str, str] = field(default_factory=dict)
    elapsed_seconds: float = 0.0


def build_classical_constants(prec_bits: int) -> dict[str, arb]:
    """Return Arb balls for {1, pi, e, ln2, gamma, zeta2, zeta3, catalan}.

    All native Arb constants. Each ball's radius is Arb's internal certificate
    at the current working precision (set via ctx.prec).
    """
    ctx.prec = prec_bits + GUARD_BITS
    out: dict[str, arb] = {}
    out["1"] = arb(1)
    out["pi"] = arb.pi()
    out["e"] = arb(1).exp()
    out["ln2"] = arb(2).log()
    out["gamma"] = arb.const_euler()
    out["zeta2"] = arb(2).zeta()
    out["zeta3"] = arb(3).zeta()
    out["catalan"] = arb.const_catalan()
    return out


def build_basis(prec_bits: int) -> CertifiedBasis:
    """Construct the 15-vector certified basis at the given working precision."""
    t0 = time.time()
    N = required_N_for_precision(prec_bits, safety_bits=64)
    classical = build_classical_constants(prec_bits)
    K0, logK0, K0_audit = certified_K0(N, prec_bits)

    # 15 basis entries in canonical order (see BASIS_LABELS).
    K_pow = [arb(1)]  # K_0^0
    for _ in range(6):
        K_pow.append(K_pow[-1] * K0)
    # K_pow now has K_0^0, K_0^1, ..., K_0^6.

    basis: list[arb] = []
    basis.append(K_pow[0])                   # 0  1
    basis.append(K_pow[1])                   # 1  K_0
    basis.append(K_pow[2])                   # 2  K_0^2
    basis.append(K_pow[3])                   # 3  K_0^3
    basis.append(K_pow[4])                   # 4  K_0^4
    basis.append(K_pow[5])                   # 5  K_0^5
    basis.append(K_pow[6])                   # 6  K_0^6
    basis.append(logK0)                      # 7  log K_0
    basis.append(K0 * classical["pi"])       # 8  K_0 * pi
    basis.append(K0 * classical["e"])        # 9  K_0 * e
    basis.append(K0 * classical["ln2"])      # 10 K_0 * ln2
    basis.append(K0 * classical["gamma"])    # 11 K_0 * gamma
    basis.append(K0 * classical["zeta2"])    # 12 K_0 * zeta(2)
    basis.append(K0 * classical["zeta3"])    # 13 K_0 * zeta(3)
    basis.append(K0 * classical["catalan"])  # 14 K_0 * G

    # Store K_0 as a "generator" too (it's both index 1 of the basis and a generator)
    classical["K_0"] = K0

    t1 = time.time()
    return CertifiedBasis(
        prec_bits=prec_bits,
        N_truncation=N,
        guard_bits=GUARD_BITS,
        generators=classical,
        basis=basis,
        K0_audit=K0_audit,
        elapsed_seconds=t1 - t0,
    )


def basis_to_json(cb: CertifiedBasis) -> dict[str, Any]:
    """Serialise a CertifiedBasis to a JSON-safe dict."""
    return {
        "prec_bits": cb.prec_bits,
        "prec_dps_approx": int(cb.prec_bits / 3.32192809489),  # log_10(2) reciprocal
        "N_truncation": cb.N_truncation,
        "guard_bits": cb.guard_bits,
        "elapsed_seconds": round(cb.elapsed_seconds, 4),
        "generators": {
            name: _ball_to_dict(val) for name, val in cb.generators.items()
        },
        "basis": [
            {"index": i, "label": BASIS_LABELS[i], **_ball_to_dict(cb.basis[i])}
            for i in range(N_BASIS)
        ],
        "K0_audit": cb.K0_audit,
        "dependency_ledger": {
            "computation_engine": "python-flint backed by FLINT (Arb)",
            "load_bearing_identities": [
                {
                    "identity": "BBC 1997 eq. (1), p.2; A_s from Lemma 1(a) p.3",
                    "form": "log(K_0)*log(2) = sum_{s>=1} (zeta(2s)-1)/s * A_s",
                    "citation": "Bailey, Borwein, Crandall (1997). On the Khintchine Constant. Math. Comp. 66(217), 417-431. DOI 10.1090/S0025-5718-97-00800-4",
                    "local_cache_sha256": "7DD18D84B93A36B85F4F94D23671A202258CB6517CCBAA5794EDEADD0E793793",
                    "local_cache_path": "_lit_cache/khinchin.pdf",
                    "verification_doc": "BBC_FORMULA_VERIFIED.md",
                }
            ],
            "tail_bound_formula": "|tail_logK0_x_log2| <= (4*(zeta(2)-1)/(3*(N+1)))*4^{-N}; proved in BBC_FORMULA_VERIFIED.md §3",
            "honesty_note": "K_0 enclosure is rigorous conditional on BBC 1997 eq.(1); we certify the arithmetic, not the identity",
        },
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    P = int(argv[1])
    out_path = None
    if "--json" in argv:
        out_path = argv[argv.index("--json") + 1]
    cb = build_basis(P)
    payload = basis_to_json(cb)
    text = json.dumps(payload, indent=2)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"WROTE {out_path}  (P_bits={P}, N={cb.N_truncation}, t={cb.elapsed_seconds:.3f}s)")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
