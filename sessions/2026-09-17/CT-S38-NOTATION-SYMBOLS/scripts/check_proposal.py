#!/usr/bin/env python3
r"""check_proposal -- screen candidate letters against PREREG Part B.

The candidate letters are screened against the SAME index that symbol_index.py
reports, by importing it, so that the proposal cannot be accepted against a
second and possibly divergent reading of the corpus.

The clauses are fixed in this source BEFORE any candidate is submitted.  If a
candidate is rejected the candidate is discarded; the clause is not relaxed.

CLAUSES (PREREG Part B)
  C1  the base carries no meaning anywhere in the index
  C2  not a Painleve chart coordinate (p, q, t, theta)
  C3  not an exponent letter
  C4  not r, not \rinf, not van der Put-Saito's r(c)
  C5  not glyph-ambiguous in isolation (reads as a different letter)
  C6  its HOMOGLYPH partner does not occur in any source file in which the
      object being renamed itself occurs

On C5 and C6, the homoglyph relation used here is Greek-against-Latin
near-identity (nu/v, omega/w, chi/x, eta/n, omicron/o, iota/i, upsilon/v)
together with TeX variant glyphs of one letter (\varrho for \rho,
\varepsilon for \epsilon).  Two DISTINCT Greek letters that merely share a
stroke -- phi against psi is the case that arises here -- are not homoglyphs
and are not rejected; that risk is reported as informational instead, which is
what the residual-risk disclosure is for.  This distinction is recorded before
any candidate is run against it.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import symbol_index as SI                                    # noqa: E402

# ---------------------------------------------------------------- clauses ---
PAINLEVE = {"p", "q", "t", "\\theta", "T"}
EXPONENTS = {"\\rho", "\\varrho", "\\mu", "\\sigma", "\\lambda", "\\alpha",
             "\\kappa", "s"}
R_FAMILY = {"r", "\\rinf", "R"}
GLYPH_AMBIGUOUS = {"l", "\\omicron", "\\iota", "\\upsilon", "\\varrho",
                   "\\varepsilon", "\\varsigma", "\\varphi", "O", "I"}
HOMOGLYPH = {"\\nu": "v", "\\omega": "w", "\\chi": "x", "\\eta": "n",
             "\\omicron": "o", "\\iota": "i", "\\upsilon": "v",
             "\\varrho": "\\rho", "\\varepsilon": "\\epsilon",
             "\\Alpha": "A", "\\Beta": "B", "\\kappa": "k", "\\gamma": "y",
             "\\Sigma": "S", "\\Tau": "T", "\\Zeta": "Z", "\\Eta": "H"}

# the source files in which the two objects being re-lettered actually occur
HOME = ["theorem.tex", "section1.tex", "OUTLINE.md"]


def read_or_fail(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read().replace("\r\n", "\n")
    except Exception as exc:
        print("READER INTEGRITY FAILED: cannot read %s (%s)" % (path, exc))
        sys.exit(4)


def home_texts():
    out = {}
    for label, path, _kind, _origin in SI.SOURCES:
        if label in HOME:
            out[label] = read_or_fail(path)
    missing = [h for h in HOME if h not in out]
    if missing:
        print("READER INTEGRITY FAILED: home sources not in index: %s"
              % missing)
        sys.exit(4)
    return out


def math_text(label, text):
    """The searchable region of a source, under the SAME discipline as the
    index: math mode for .tex, backticked code spans for .md prose.

    The first version of this function searched the RAW text.  Every one of
    the 23 'v' hits it returned in OUTLINE.md and theorem.tex was a version
    string -- v1.7, v1.3.1, arXiv:0902.1702v5 -- and none was the symbol v, so
    it rejected a candidate for a collision that does not exist.  Searching
    raw prose for a single Latin letter cannot distinguish a symbol from a
    letter of English or of a version number; the index already says so and
    scans math mode only.  Using a looser rule in the screen than in the index
    it screens against was the defect.  Repaired here by reusing the index's
    own discipline, which also keeps subscripts in scope because a subscript
    lies inside the math segment.
    """
    if label.endswith(".tex"):
        return "\n".join(next(g for g in m.groups() if g is not None)
                         for m in SI.MATH.finditer(text))
    return "\n".join(m.group(1) for m in re.finditer(r"`([^`\n]+)`", text))


def partner_occurs(partner, texts):
    if partner.startswith("\\"):
        pat = re.escape(partner) + r"(?![A-Za-z])"
    else:
        pat = r"(?<![A-Za-z\\])" + re.escape(partner) + r"(?![A-Za-z0-9])"
    hits = []
    for label, text in sorted(texts.items()):
        n = len(re.findall(pat, math_text(label, text)))
        if n:
            hits.append("%s x%d" % (label, n))
    return hits


def screen(base, by_base, texts):
    """Return (ok, [(clause, verdict, detail)])."""
    rows = []

    keys = by_base.get(base, [])
    srcs = sorted({s for (_k, l) in keys for (s, _c) in l})
    ok1 = not keys
    rows.append(("C1 unused in index", ok1,
                 "no meaning in any source" if ok1 else
                 "%d keys in %s" % (len(keys), ", ".join(srcs))))

    ok2 = base not in PAINLEVE
    rows.append(("C2 not a chart coordinate", ok2,
                 "" if ok2 else "Painleve/Okamoto chart coordinate"))

    ok3 = base not in EXPONENTS
    rows.append(("C3 not an exponent letter", ok3,
                 "" if ok3 else "reserved for exponents"))

    ok4 = base not in R_FAMILY
    rows.append(("C4 not r / \\rinf / r(c)", ok4,
                 "" if ok4 else "the r-family being disambiguated"))

    ok5 = base not in GLYPH_AMBIGUOUS
    rows.append(("C5 not glyph-ambiguous", ok5,
                 "" if ok5 else "reads as a different letter in isolation"))

    partner = HOMOGLYPH.get(base)
    hits = partner_occurs(partner, texts) if partner else []
    ok6 = not hits
    rows.append(("C6 homoglyph partner absent", ok6,
                 ("no homoglyph partner" if not partner else
                  ("partner %s unused in home sources" % partner if ok6 else
                   "partner %s occurs: %s" % (partner, "; ".join(hits))))))

    return all(r[1] for r in rows), rows


def show(title, base, by_base, texts):
    ok, rows = screen(base, by_base, texts)
    print("\n  %-34s %s" % (title, "ADMISSIBLE" if ok else "REJECTED"))
    for clause, good, detail in rows:
        print("      %-30s %-6s %s" % (clause, "pass" if good else "FAIL",
                                       detail))
    return ok, rows


def main():
    by_base, _occ, _per, _srcs = SI.build_index(verbose=False)
    texts = home_texts()

    print("check_proposal -- PREREG Part B screening")
    print("index: %d distinct bases; home sources: %s"
          % (len(by_base), ", ".join(HOME)))

    # ---- controls, run BEFORE the proposal: each must be REJECTED ----------
    print("\n[controls -- each must be REJECTED, and for the named clause]")
    controls = [
        ("q  (the letter being removed)", "q", "C1 unused in index"),
        ("\\lambda (the letter being removed)", "\\lambda",
         "C1 unused in index"),
        ("r  (the r-family)", "r", "C1 unused in index"),
        ("\\rho (exponent letter)", "\\rho", "C1 unused in index"),
        ("\\varrho (variant glyph of \\rho)", "\\varrho",
         "C3 not an exponent letter"),
        ("\\mu (exponent letter)", "\\mu", "C3 not an exponent letter"),
        ("l  (reads as 1)", "l", "C5 not glyph-ambiguous"),
        ("\\omega (partner w in use)", "\\omega",
         "C6 homoglyph partner absent"),
        ("\\chi (partner x in use)", "\\chi", "C6 homoglyph partner absent"),
        ("\\eta (partner n in use)", "\\eta", "C6 homoglyph partner absent"),
    ]
    bad = []
    for title, base, want in controls:
        ok, rows = show(title, base, by_base, texts)
        if ok:
            bad.append("%s was ADMISSIBLE; the screen is not discriminating"
                       % base)
            continue
        fired = [c for c, good, _d in rows if not good]
        if want not in fired:
            bad.append("%s was rejected, but on %s, not on the expected %s"
                       % (base, fired, want))

    # ---- the proposal -----------------------------------------------------
    print("\n[proposal]")
    if len(sys.argv) > 1:
        prop = [("submitted candidate %s" % a, a) for a in sys.argv[1:]]
    else:
        prop = [("\\psi  -- normalised sequence psi_n and its limit psi_infty",
                 "\\psi"),
                ("\\nu   -- the roots nu_1..nu_d of b", "\\nu")]
    good = True
    for title, base in prop:
        ok, _rows = show(title, base, by_base, texts)
        good = good and ok

    # ---- informational residual risk (NOT a rejection clause) -------------
    print("\n[residual risk -- disclosed, not screened]")
    for base, near, why in [
            ("\\psi", "\\varphi",
             "both Greek with a vertical stroke; \\varphi occurs only as the "
             "subscript of L_\\varphi"),
            ("\\nu", "n",
             "nu sits beside the index n in b(n)=beta_d prod (n - nu_i)")]:
        hits = partner_occurs(near, texts)
        print("    %-8s near %-9s %s" % (base, near, why))
        print("             %s" % ("; ".join(hits) if hits
                                   else "partner absent from home sources"))

    print("\n[verdict]")
    if bad:
        for b in bad:
            print("  CONTROL FAILED: %s" % b)
        print("  VERDICT: the screen is not trustworthy; proposal not "
              "adjudicated.")
        sys.exit(1)
    print("  controls: %d/%d rejected for the expected clause"
          % (len(controls), len(controls)))
    if not good:
        print("  VERDICT: PROPOSAL REJECTED -- discard the candidates, do not "
              "relax the clause.")
        sys.exit(2)
    print("  VERDICT: PROPOSAL ADMISSIBLE -- \\psi_n, \\psi_\\infty and "
          "\\nu_1..\\nu_d")
    sys.exit(0)


if __name__ == "__main__":
    main()
