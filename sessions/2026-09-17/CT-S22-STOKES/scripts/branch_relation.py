"""CT-S22-STOKES - the relation between the two CT-S16 branches.

Two questions, both answered by proof rather than by assertion:

  S22-19  How are branch 1 (t = -2 sqrt(33) i/9) and branch 2 (t = +2 sqrt(33) i/9)
          related?  Claim: by the Galois automorphism sigma of Q(sqrt3, sqrt11)
          with sigma(sqrt3) = -sqrt3, sigma(sqrt11) = +sqrt11.  Established by
          simplifying sigma(X_1) - X_2 to zero for X in {t, theta_inf, q, p},
          AND by a numeric check - never by `==` on unevaluated radicals.

  S22-20  How do their trace coordinates compare?  Read back from the two
          Stage-2 output files, not retyped.

The point of S22-19 is NEGATIVE as much as positive: sigma is an automorphism of
a NUMBER FIELD.  The monodromy is transcendental in the matrix entries, so sigma
does not act on the analytic continuation.  The relation therefore transfers the
CT-S16 location argument and carries NO information about the Stokes data - which
is why branch 2 had to be run rather than inferred.
"""
import hashlib
import pathlib
import re

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
SESS = HERE.parent
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


S3, S11 = sp.sqrt(3), sp.sqrt(11)
S33 = sp.sqrt(33)


def branch(which):
    """The two solutions, transcribed from CT-S16-MEMBERSHIP-C/outputs/pq_solution.txt
    (the only source), with the sign of sqrt(33)/sqrt(3) flipped between them."""
    if which == 1:
        t = -2 * S33 * sp.I / 9
        th = -2 - S3 / 9
        q = sp.Rational(1, 2) - 457937 * S11 * sp.I / 122408 + 70425 * S33 * sp.I / 30602
        p = 5 * sp.I * (-28151758571 * S33 + 48874838016 * S11) / 4086468672
    else:
        t = +2 * S33 * sp.I / 9
        th = -2 + S3 / 9
        q = sp.Rational(1, 2) - 70425 * S33 * sp.I / 30602 - 457937 * S11 * sp.I / 122408
        p = 5 * sp.I * (28151758571 * S33 + 48874838016 * S11) / 4086468672
    return {"t": t, "theta_inf": th, "q": q, "p": p}


A, B = sp.symbols("A B", positive=True)


def sigma(e):
    """sqrt3 -> -sqrt3, sqrt11 -> +sqrt11, hence sqrt33 -> -sqrt33."""
    e = sp.expand(e).subs({S33: A * B, S3: A, S11: B})
    return sp.expand(e.subs({A: -S3, B: S11}))


def main():
    say("=" * 74)
    say("CT-S22-STOKES  -  the relation between the two CT-S16 branches")
    say("=" * 74)
    b1, b2 = branch(1), branch(2)

    say("")
    say("S22-19  sigma: sqrt3 -> -sqrt3, sqrt11 -> +sqrt11  (so sqrt33 -> -sqrt33)")
    say("-" * 74)
    ok = True
    for k in ("t", "theta_inf", "q", "p"):
        d = sp.simplify(sp.radsimp(sp.expand(sigma(b1[k]) - b2[k])))
        # symbolic arm
        sym0 = (d == 0)
        # independent numeric arm, per PREREG section 10
        num = mp.mpmathify(complex(sp.N(sigma(b1[k]) - b2[k], 40)))
        say(f"  sigma({k:9s})_1 - {k:9s}_2 :  simplify -> {d}   "
            f"|numeric| = {mp.nstr(abs(num), 6)}")
        ok = ok and sym0 and abs(num) < mp.mpf(10) ** -30
    say(f"  [{'PASS' if ok else 'FAIL'}] sigma maps branch 1 to branch 2 term by term.")
    assert ok, "the Galois relation does not hold"

    say("")
    say("  Are they complex conjugates?  (they are widely assumed to be)")
    for k in ("q", "p", "t", "theta_inf"):
        d = sp.simplify(sp.expand(sp.conjugate(b1[k]) - b2[k]))
        say(f"    conj({k:9s})_1 - {k:9s}_2 = {d}")
    say("  -> q and p are NOT conjugate pairs; conjugation flips the sqrt(11)")
    say("     term as well, which sigma does not.  The branches are Galois")
    say("     conjugates over Q(sqrt3, sqrt11), not complex conjugates.")

    say("")
    say("  SCOPE, and the reason branch 2 was RUN and not inferred:")
    say("  sigma is an automorphism of a NUMBER FIELD.  The monodromy and Stokes")
    say("  data are transcendental functions of the matrix entries, and sigma")
    say("  does not act on analytic continuation.  The relation transfers the")
    say("  CT-S16 location argument; it carries NO information about the Stokes")
    say("  data.  LABEL for the relation: PROVEN.  LABEL for any transfer of")
    say("  monodromy through it: NOT CLAIMED.")

    # ---- S22-20: compare the two Stage-2 outputs, read back from disk ------
    say("")
    say("S22-20  the two branches' trace coordinates, read back from the")
    say("        Stage-2 output files (not retyped)")
    say("-" * 74)
    vals = {}
    for tag, fn in (("branch 1", "stage2_systemC.out.txt"),
                    ("branch 2", "stage2_systemC_b2.out.txt")):
        path = SESS / "outputs" / fn
        if not path.exists():
            say(f"  {tag}: MISSING {fn} - cannot compare")
            return False
        txt = path.read_text(encoding="utf-8")
        d = {}
        for key in ("x1", "x2", "x3", "alpha"):
            m = re.search(rf"^\s*{key}\s*=\s*\S*\s*=?\s*\(([^)]*)\)\s*$", txt, re.M)
            if m is None:
                m = re.search(rf"^\s*{key}\b.*?\(([^)]*)\)\s*$", txt, re.M)
            d[key] = m.group(1) if m else "?"
        u = re.search(r"UNIQUE:\s*(\S+)", txt)
        d["convention"] = u.group(1) if u else "?"
        vals[tag] = d
        say(f"  {tag}: convention {d['convention']}")
        for key in ("x1", "x2", "x3", "alpha"):
            say(f"      {key:5s} = {d[key][:70]}")

    if "?" not in str(vals):
        def realpart(s):
            return s.split("+")[0].split("-")[0].strip() if not s.strip().startswith("-") \
                else "-" + s.strip()[1:].split("+")[0].split("-")[0].strip()
        swap = (realpart(vals["branch 1"]["x1"]) == realpart(vals["branch 2"]["x2"]) and
                realpart(vals["branch 1"]["x2"]) == realpart(vals["branch 2"]["x1"]))
        # x3's imaginary parts are ~1e-170, i.e. zero to precision; compare the
        # REAL parts.  An earlier version compared the raw strings including
        # those 1e-170 tails and reported False while printing the conclusion
        # anyway - a check that could not fail.
        same3 = realpart(vals["branch 1"]["x3"]) == realpart(vals["branch 2"]["x3"])
        samea = vals["branch 1"]["alpha"] == vals["branch 2"]["alpha"]
        mirror = vals["branch 1"]["convention"] != vals["branch 2"]["convention"]
        say("")
        say(f"  x1 <-> x2 interchanged between branches : {swap}")
        say(f"  x3 real parts identical                 : {same3}")
        say(f"  alpha identical                         : {samea}")
        say(f"  conventions differ (mirrored)           : {mirror}  "
            f"{vals['branch 1']['convention']} vs {vals['branch 2']['convention']}")
        all_ok = swap and same3 and samea and mirror
        say("")
        if all_ok:
            say("  [PASS] -> the two branches sit at the SAME point of the")
            say("  character variety, up to the relabelling induced by the")
            say("  mirrored convention.  LABEL: VERIFIED.")
        else:
            say("  [FAIL] the branches do NOT agree in the way described; the")
            say("  claim that they give one point is NOT established.")
        assert all_ok, "branch comparison failed"
    return True


if __name__ == "__main__":
    ok = main()
    outp = SESS / "outputs" / "branch_relation.out.txt"
    outp.parent.mkdir(exist_ok=True)
    outp.write_text("\n".join(OUT) + "\n", encoding="utf-8")
    back = outp.read_text(encoding="utf-8")
    assert back.splitlines() == OUT, "read-back mismatch"
    print(f"\nwritten {outp}  sha256 "
          f"{hashlib.sha256(back.encode('utf-8')).hexdigest()}")
