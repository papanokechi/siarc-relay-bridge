"""Verify the Appendix A repairs by parsing the repaired LaTeX and comparing
the displayed expressions against sympy's own factorisation.

The control that makes this evidence is the pre-repair file: refs/appendixA.tex
must FAIL exactly the check that the repaired file passes.  A checker that
passes the repaired text proves only that it can read; one that also rejects
the text it was built to catch has been shown to discriminate.

Nothing here trusts a string comparison against an expected literal.  The
LaTeX is parsed into a sympy expression and compared mathematically, so an
equivalent rewriting would also pass and a transposed digit would not.
"""
import pathlib
import re
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent.parent
p, q, t, z = sp.symbols("p q t z")

# The true factorisation, re-derived independently in route_s.py.
TRUE = sp.Rational(1, 4) * z * (q - 1) * (t - 1) * (
    4 * p + q ** 2 * t + q ** 2 - q * t - q)

# The displayed factored form, located by the sentence that introduces it.
SENT = r"The difference between the two readings factors as\s*(.+?),"


def latex_to_expr(s):
    """Convert the narrow subset of LaTeX used in this display to sympy."""
    s = s.strip().strip("$")
    s = s.replace(r"\tfrac14", "(1/4)").replace(r"\tfrac12", "(1/2)")
    s = s.replace(r"\bigl", "").replace(r"\bigr", "")
    # implicit multiplication is also written as a space in LaTeX ("z(q-1)"
    # versus "\tfrac14 z"); removing whitespace lets one rule cover both
    s = re.sub(r"\s+", "", s)
    s = s.replace("^{2}", "**2").replace("^{3}", "**3")
    s = re.sub(r"\^\{(\d+)\}", r"**\1", s)
    # implicit multiplication: 4p -> 4*p, z( -> z*(, )( -> )*(, qt -> q*t
    s = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", s)
    s = re.sub(r"([a-zA-Z0-9\)])\(", r"\1*(", s)
    s = re.sub(r"\)([a-zA-Z0-9])", r")*\1", s)
    s = re.sub(r"([pqtz])([pqtz])", r"\1*\2", s)
    s = s.replace(")*=", ")=")
    return sp.sympify(s, locals={"p": p, "q": q, "t": t, "z": z})


def check(path, label):
    txt = pathlib.Path(path).read_text(encoding="utf-8")
    txt_flat = re.sub(r"\s+", " ", txt)

    m = re.search(SENT, txt_flat)
    if not m:
        print("  %-10s READER FAILED: the introducing sentence is absent; "
              "this check cannot see its target" % label)
        return None

    raw = m.group(1)
    try:
        expr = latex_to_expr(raw)
    except Exception as exc:                                   # noqa: BLE001
        print("  %-10s READER FAILED: cannot parse %r (%s)" % (label, raw, exc))
        return None

    resid = sp.simplify(sp.expand(expr - TRUE))
    ok = resid == 0
    print("  %-10s %s" % (label, "MATCHES the true factorisation"
                          if ok else "DIFFERS from the true factorisation"))
    print("             parsed: %s" % sp.factor(expr))
    if not ok:
        print("             residual: %s" % sp.factor(resid))
    return ok


def main():
    print("verify_repair: the factored difference in Appendix A")
    print("  true value: %s" % sp.factor(TRUE))
    print()

    repaired = check(HERE / "appendixA.tex", "repaired")
    prepair = check(HERE / "refs" / "appendixA.tex", "pre-repair")

    print()
    if repaired is None or prepair is None:
        print("VERDICT: FAIL -- a reader failed; no conclusion is available")
        return 1
    if not repaired:
        print("VERDICT: FAIL -- the repaired appendix still differs")
        return 1
    if prepair:
        print("VERDICT: FAIL -- the CONTROL passed. The pre-repair file was "
              "accepted by a check built to reject it, so the check does not "
              "discriminate and the 'repaired' verdict means nothing.")
        return 1
    print("VERDICT: PASS -- repaired matches, and the control (pre-repair) is "
          "rejected by the same check, so it discriminates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
