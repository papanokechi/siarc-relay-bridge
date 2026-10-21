"""CT-S22-STOKES Stage 5 - the degeneracy that made Stage 5A void (S22-21).

The Stage-5A PSLQ search returned, for C and for every decoy alike, the relation

    -2 log2 + 3 log3 - 3 log(pi) + 12 log Gamma(1/3) - 6 log Gamma(1/6) = 0,

with coefficient ZERO on log C.  That is not a discovery about C; it is a
classical identity among the basis constants, so the pre-registered basis was
degenerate and the search never tested C at all.

This script establishes the identity by proof and by an independent numeric
check, as PREREG section 10 requires - never by `==` on unevaluated radicals.
"""
import hashlib
import pathlib

import mpmath as mp
import sympy as sp

SESS = pathlib.Path(__file__).resolve().parent.parent
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def main():
    say("=" * 74)
    say("S22-21  Gamma(1/6) is NOT independent of {2, 3, pi, Gamma(1/3)}")
    say("=" * 74)
    say("")
    say("PROOF (two classical identities):")
    say("  Legendre duplication  Gamma(z) Gamma(z+1/2) = 2^{1-2z} sqrt(pi) Gamma(2z)")
    say("  at z = 1/6:           Gamma(1/6) Gamma(2/3) = 2^{2/3} sqrt(pi) Gamma(1/3)")
    say("  reflection at 1/3:    Gamma(1/3) Gamma(2/3) = pi / sin(pi/3) = 2 pi / sqrt3")
    say("  so                    Gamma(2/3) = 2 pi / (sqrt3 Gamma(1/3))")
    say("  substituting:         Gamma(1/6) = 2^{2/3} sqrt3 Gamma(1/3)^2 / (2 sqrt(pi))")
    say("")

    # --- arm 1: check the two input identities symbolically -----------------
    z = sp.Rational(1, 6)
    dup = sp.gammasimp(sp.simplify(sp.expand_func(
        sp.gamma(z) * sp.gamma(z + sp.Rational(1, 2))
        - 2 ** (1 - 2 * z) * sp.sqrt(sp.pi) * sp.gamma(2 * z))))
    # sympy will not apply reflection at a NUMERIC argument, so the identity is
    # proved for a symbol and then instantiated at x = 1/3.  (An earlier version
    # asked simplify() to do it at 1/3, got a non-zero expression back, and
    # would have reported a failed proof for a true identity.)
    xs = sp.Symbol("x")
    refl_sym = sp.gammasimp(sp.gamma(xs) * sp.gamma(1 - xs) - sp.pi / sp.sin(sp.pi * xs))
    refl_val = sp.simplify(sp.pi / sp.sin(sp.pi * sp.Rational(1, 3)) - 2 * sp.pi / sp.sqrt(3))
    say(f"  duplication at z=1/6, simplify-to-zero      : {dup}")
    say(f"  reflection G(x)G(1-x) - pi/sin(pi x), symbol: {refl_sym}")
    say(f"  instantiated: pi/sin(pi/3) - 2pi/sqrt3      : {refl_val}")
    assert dup == 0, f"duplication did not simplify to zero: {dup}"
    assert refl_sym == 0, f"reflection did not simplify to zero: {refl_sym}"
    assert refl_val == 0, f"instantiation did not simplify to zero: {refl_val}"

    # --- arm 2: the resulting closed form, numerically ----------------------
    mp.mp.dps = 80
    lhs = mp.gamma(mp.mpf(1) / 6)
    rhs = 2 ** (mp.mpf(2) / 3) * mp.sqrt(3) * mp.gamma(mp.mpf(1) / 3) ** 2 / (2 * mp.sqrt(mp.pi))
    say("")
    say(f"  Gamma(1/6)            = {mp.nstr(lhs, 50)}")
    say(f"  2^(2/3)V3 G(1/3)^2/2Vpi = {mp.nstr(rhs, 50)}")
    say(f"  |difference| at dps 80 = {mp.nstr(abs(lhs - rhs), 6)}")
    assert abs(lhs - rhs) < mp.mpf(10) ** -70, "the closed form does not hold"

    # --- arm 3: the exact relation PSLQ returned ----------------------------
    v = [mp.log(2), mp.log(3), mp.log(mp.pi),
         mp.log(mp.gamma(mp.mpf(1) / 3)), mp.log(mp.gamma(mp.mpf(1) / 6))]
    coef = [-2, 3, -3, 12, -6]
    resid = abs(sum(a * b for a, b in zip(coef, v)))
    say("")
    say("  the relation Stage 5A returned, evaluated directly:")
    say("    -2 log2 + 3 log3 - 3 log(pi) + 12 log G(1/3) - 6 log G(1/6)")
    say(f"    = {mp.nstr(resid, 6)}   (zero to {mp.nstr(-mp.log10(resid), 5)} digits)")
    assert resid < mp.mpf(10) ** -70, "the PSLQ relation is not the identity"
    say("")
    say("  Taking 6 x log of the closed form reproduces exactly those integers,")
    say("  so the relation PSLQ found IS this identity.  It says nothing about C.")

    # --- the consequence, stated as the finding -----------------------------
    say("")
    say("CONSEQUENCE")
    say("-" * 74)
    say("  The PREREG-STAGE5 section 3 basis was DEGENERATE.  PSLQ's smallest")
    say("  relation was a relation among the basis constants themselves, so the")
    say("  Stage 5A search never tested C.  Its 'NOT FOUND' excluded nothing and")
    say("  is WITHDRAWN.  Stage 5A is VOID, not negative.")
    say("")
    say("  The Stage-5A vacuity pre-check reported 3 decoys rejected and 1")
    say("  control accepted - the required outcome - but the decoys were")
    say("  rejected because PSLQ handed back a C-free relation, not because the")
    say("  space discriminates.  A check that passed FOR THE WRONG REASON.")
    say("  PREREG-STAGE5B section 4.1 adds the missing falsifier: PSLQ on the")
    say("  constants with log C removed must return NO relation.")
    say("")
    say("  LABEL: PROVEN (two classical identities), and VERIFIED numerically.")
    return True


if __name__ == "__main__":
    main()
    outp = SESS / "outputs" / "gamma16_identity.out.txt"
    outp.parent.mkdir(exist_ok=True)
    outp.write_text("\n".join(OUT) + "\n", encoding="utf-8")
    back = outp.read_text(encoding="utf-8")
    assert back.splitlines() == OUT, "read-back mismatch"
    print(f"\nwritten {outp}  sha256 "
          f"{hashlib.sha256(back.encode('utf-8')).hexdigest()}")
