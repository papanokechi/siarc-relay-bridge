"""verify_artefacts.py -- CT-S36, evidence for the file-inspection claims.

check_171.py verifies section 1 against the 171 items.  It does not look at
theorem.tex at all, and it does not check the specific textual commitments
S36-01, S36-11 and S36-12 make.  Those claims need a script that actually
establishes them, so this is it.

Every assertion is stated as a required presence or a required ABSENCE, and
absences are guarded: a known-present non-ASCII-free sentinel is asserted for
each file first, so an empty or truncated read cannot report a clean absence.
"""
import hashlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TEX = HERE / "theorem.tex"
SEC1 = HERE / "section1.tex"

T = TEX.read_text(encoding="utf-8")
S = SEC1.read_text(encoding="utf-8")

CHECKS = []


def need(label, cond):
    CHECKS.append((label, bool(cond)))


# --- reader integrity: assert the files were seen, before any absence --------
need("READER theorem.tex non-empty (>20000 B)", len(T) > 20000)
need("READER theorem.tex has its title macro", r"\newcommand{\rinf}" in T)
need("READER section1.tex non-empty (>12000 B)", len(S) > 12000)
need("READER section1.tex has its section heading",
     r"\section{Notation and standing conventions}" in S)

# --- S36-01: Proposition U is present, after prop:positive, citing S26-01 ----
need("S36-01 prop:upper present", r"\label{prop:upper}" in T)
need("S36-01 (U-finite) display labelled", r"\label{eq:ufinite}" in T)
need("S36-01 (U-limit) display labelled", r"\label{eq:ulimit}" in T)
need("S36-01 prop:upper comes AFTER prop:positive",
     T.index(r"\label{prop:upper}") > T.index(r"\label{prop:positive}"))
need("S36-01 positivity stated as a hypothesis",
     "b(n)>0" in T.replace(" ", "") or r"b(k)>0" in T.replace(" ", ""))
need("S36-01 status list cites S26-01", "S26-01" in T)
need("S36-01 positivity remark present", r"\label{rem:upper-positivity}" in T)

# The drafting constraint from S26-01: S1-02 must not be offered as authority
# for the upper bound.  Checked as a proximity condition, not a bare absence.
i = T.index(r"\label{prop:upper}")
window = T[max(0, i - 200): i + 2500]
need("S36-01 ABSENCE: S1-02 not cited inside the prop:upper block",
     "S1-02" not in window)

# --- S36-11: the renaming and exactly ONE footnote ---------------------------
need("S36-11 q_n named", r"\emph{normalised denominator sequence}" in S)
need("S36-11 q_infinity named", r"q_\infty=\lim_{n\to\infty}q_n" in S)
need("S36-11 lambda roots named", r"\lambda_1,\dots,\lambda_d\in\C" in S)
need("S36-11 exactly one footnote in section 1", S.count(r"\footnote{") == 1)
need("S36-11 footnote gives the correspondence",
     "q_n\\leftrightarrow r_n" in S and
     "q_\\infty\\leftrightarrow r_\\infty" in S and
     r"\lambda_1,\dots,\lambda_d\leftrightarrow r_1,\dots,r_d" in S)
need("S36-11 ABSENCE: deposits are stated to be unaltered",
     "The deposited\nrecords are not altered" in S or
     "records are not altered" in S)

# --- S36-12: the fourth r-object is recorded ---------------------------------
need("S36-12 Katz invariant written r(c) as in van der Put-Saito",
     r"\emph{Katz invariant} $r(c)$" in S)
need("S36-12 Table 2.1 column order r(0),r(1),r(inf),r(t)",
     r"\bigl(r(0),\,r(1),\,r(\infty),\,r(t)\bigr)" in S)
need("S36-12 r(c) declared unrelated to the three r-objects",
     "is unrelated to the sequence" in S)
need("S36-12 footnote names the fourth object",
     "A fourth, unrelated object" in S)

# --- the qualification the notice-side rulings require ----------------------
need("necessary-condition qualification present",
     r"\textbf{A matching multiset is a necessary condition only.}" in S)
need("no Painleve label asserted for the operator",
     "infers a Painlev\\'e label from a multiset match alone" in S)


def main():
    print("verify_artefacts.py -- CT-S36 file-inspection evidence")
    print("  theorem.tex  sha256 %s" %
          hashlib.sha256(TEX.read_bytes()).hexdigest())
    print("  section1.tex sha256 %s" %
          hashlib.sha256(SEC1.read_bytes()).hexdigest())
    print()
    bad = 0
    for label, ok in CHECKS:
        print("  %-58s %s" % (label, "ok" if ok else "FAILED"))
        bad += not ok
    print("\n  checks run    : %d" % len(CHECKS))
    print("  checks failed : %d" % bad)
    print("\nVERDICT: %s" % ("PASSED" if bad == 0 else "FAILED"))
    sys.exit(0 if bad == 0 else 1)


if __name__ == "__main__":
    main()
