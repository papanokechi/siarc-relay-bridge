#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CT-S49-FULLREAD -- confirms every finding of the end-to-end read against the
source bytes, so that no reported defect is one the reader manufactured.

Exit codes: 0 all findings confirmed / 1 a finding failed confirmation
            2 refusal (control dead, file missing) / 3 crash
"""
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
REFS = HERE / "refs"
OUT = HERE / "outputs" / "check_read_findings.out.txt"

LINES, FAILED, NCTRL = [], [], 0


def _crash(et, e, tb):
    import traceback
    sys.stderr.write("".join(traceback.format_exception(et, e, tb)))
    sys.stderr.write("\nCRASH -- exit 3\n")
    sys.exit(3)


sys.excepthook = _crash


def emit(s=""):
    LINES.append(s)
    print(s)


def save():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")


def refuse(why):
    emit("")
    emit("REFUSED: " + why)
    save()
    sys.exit(2)


FILES = ["paper.tex", "preamble.tex", "section0.tex", "section1.tex",
         "section2.tex", "section3.tex", "section4.tex", "section5.tex",
         "section6.tex", "section7.tex", "section8.tex", "section9.tex",
         "section10.tex", "appendixA.tex", "appendixB.tex"]

TEXT = {}
for f in FILES:
    p = REFS / f
    if not p.exists():
        refuse("source file missing from refs/: %s" % f)
    TEXT[f] = p.read_text(encoding="utf-8")


def pat(phrase):
    """Wrap-tolerant needle (S43-12): tokens joined by \\s+."""
    return re.compile(r"\s+".join(re.escape(t) for t in phrase.split()))


def find_all(phrase, files=None):
    """Return [(file, lineno, line)] for every wrap-tolerant occurrence."""
    rx = pat(phrase)
    hits = []
    for f in (files or FILES):
        t = TEXT[f]
        for m in rx.finditer(t):
            hits.append((f, t.count("\n", 0, m.start()) + 1,
                         t[max(0, m.start() - 0):m.end()].replace("\n", " ")))
    return hits


def present(fid, phrase, files=None, why=""):
    hits = find_all(phrase, files)
    ok = len(hits) > 0
    loc = ", ".join("%s:%d" % (f, n) for f, n, _ in hits) or "NOWHERE"
    emit("  [%s] %-5s PRESENT %-58s  %s"
         % ("OK  " if ok else "FAIL", fid, repr(phrase[:54]), loc))
    if why:
        emit("        %s" % why)
    if not ok:
        FAILED.append(fid)
    return hits


def absent(fid, phrase, files=None, why=""):
    hits = find_all(phrase, files)
    ok = len(hits) == 0
    emit("  [%s] %-5s ABSENT  %-58s  %s"
         % ("OK  " if ok else "FAIL", fid, repr(phrase[:54]),
            "confirmed absent" if ok else
            ", ".join("%s:%d" % (f, n) for f, n, _ in hits)))
    if why:
        emit("        %s" % why)
    if not ok:
        FAILED.append(fid)
    return ok


def control(cid, fired, desc):
    global NCTRL
    NCTRL += 1
    emit("  [%s] %-5s %s" % ("FIRED" if fired else "DEAD ", cid, desc))
    if not fired:
        refuse("control %s did not fire" % cid)


emit("=" * 78)
emit("CT-S49-FULLREAD -- every finding confirmed against the source bytes")
emit("=" * 78)

# --- V3: resolve the corpus POSITIVELY, not by path (S44-16) --------------
sha5 = hashlib.sha256((REFS / "section5.tex").read_bytes()).hexdigest()
emit("")
emit("corpus: %d source files; section5.tex sha256 %s" % (len(FILES), sha5[:16]))
if sha5[:16] != "af25048b9b62a6f4":
    refuse("section5.tex is not the file CT-S47 verified; the tree moved")
control("V3", True, "section5.tex hashes to the digest CT-S47 checked, so the "
                    "tree being read is the tree that was checked")
emit()

# ==========================================================================
emit("F1  the formula-pass disclaimer is stale, and contradicts Appendix A")
emit("-" * 78)
present("F1a", "none has been symbolically re-derived here", ["section9.tex"])
present("F1b", "No displayed formula in this paper has been re-derived here "
               "from the script that computed it", ["appendixB.tex"])
present("F1c", "the formulas of Appendix~\\ref{app:typo} were transcribed from "
               "page images rather than computed", ["section9.tex"])
present("F1d", "Both routes were exercised for this appendix in "
               "\\texttt{CT-S45-FORMULA-A}, per equation", ["appendixA.tex"],
        "-- Appendix A states the re-derivation WAS performed, per equation")
control("F1c1", len(find_all("CT-S45-FORMULA-A")) == 1,
        "CT-S45-FORMULA-A is named exactly once in the paper (Appendix A), so "
        "the closure is recorded in one place and disclaimed in two")
emit()

# ==========================================================================
emit("F2  a sentence that contradicts itself")
emit("-" * 78)
present("F2a", "the second place in the paper where a structural argument for "
               "a numerically solid fact has been sought and not found",
        ["section8.tex"])
present("F2b", "the first being the twist question of "
               "\\S\\ref{ssec:tracefree}, where one was found", ["section8.tex"],
        "-- 'sought and NOT found ... where one WAS found', in one sentence")
emit()

# ==========================================================================
emit("F3  a phrase quoted from a section that does not contain it")
emit("-" * 78)
qhits = present("F3a", "The phrase ``for both sign branches'' in "
                       "\\S\\ref{ssec:located}", ["section5.tex"])
# The phrase cannot be shown absent by a needle that its own quotation
# satisfies.  The decidable question is whether it occurs ANYWHERE OTHER THAN
# inside the sentence that quotes it.
allhits = find_all("for both sign branches")
qline = qhits[0][1] if qhits else None
outside = [(f, n) for f, n, _ in allhits
           if not (f == "section5.tex" and n == qline)]
ok3b = (len(allhits) == 1 and not outside)
emit("  [%s] F3b   OUTSIDE-ITS-OWN-QUOTATION  occurrences=%d  elsewhere=%s"
     % ("OK  " if ok3b else "FAIL", len(allhits), outside or "none"))
emit("        -- the phrase exists only in the sentence that attributes it to "
     "\\S5.3; \\S5.3 does not contain it")
if not ok3b:
    FAILED.append("F3b")
control("F3c", len(find_all("On the branch")) >= 2,
        "the wording \\S5.3 actually uses is 'On the branch', twice -- so the "
        "reader can see the section, and 'absent' is not 'unreadable'")
emit()

# ==========================================================================
emit("F4  the paper declares one scalar displayed form and uses another")
emit("-" * 78)
present("F4a", "of a scalar equation written $A\\,W''+A'\\,W'+C\\,W=0$, which "
               "is a", ["section1.tex"])
present("F4b", "which is a different use of the same letters and occurs only "
               "in that displayed form", ["section1.tex"])
present("F4c", "(3x^2+x+1)\\,W''+(6x+1)\\,W'-x^2\\,W=0", ["section3.tex"],
        "-- the paper's ONLY equation of that shape")
present("F4d", "with $a(x)=3x^2+x+1$ one has $b(x)=6x+1=a'(x)$",
        ["section3.tex"], "-- named with lowercase a, b, c, not A, A', C")
control("F4e", len(find_all("A\\,W''")) == 1,
        "the declared form A W'' + A' W' + C W occurs ONCE -- in its own "
        "declaration -- and never in the body")
emit()

# ==========================================================================
emit("F5  the letter b carries four meanings; section 1's list omits it")
emit("-" * 78)
present("F5a", "b(n)=\\sum_{k=0}^{d}\\beta_k n^k", ["section1.tex"],
        "-- meaning 1: the polynomial of the recurrence")
present("F5b", "$b(x)=6x+1=a'(x)$", ["section3.tex"],
        "-- meaning 2: a coefficient of System C")
present("F5c", "A=\\begin{pmatrix} a & b\\\\ c & -a\\end{pmatrix}",
        ["section4.tex"], "-- meaning 3: an entry of the matrix A")
present("F5d", "the no-apparent-singularity condition $b_1=0$",
        ["section5.tex"], "-- meaning 4: a coefficient of that entry")
present("F5e", "Six further letters are reused, in each case with a stated "
               "discriminator", ["section1.tex"])
present("F5f", "This section fixes every symbol, name and hypothesis used in "
               "the paper", ["section1.tex"])
control("F5g", len(find_all("\\item $b_k$")) == 0
        and len(find_all("\\item $b$")) == 0,
        "section 1's reuse list has no entry for the letter b (the six are "
        "M, A, L, u, beta, r)")
emit()

# ==========================================================================
emit("F6  b_1 is used in section 5 and only explicable in section 6")
emit("-" * 78)
h5 = present("F6a", "$b_1=0$", ["section5.tex"])
h6 = present("F6b", "these coincide exactly when $b$ is constant --- that is, "
                    "when $b_1=0$", ["section6.tex"],
             "-- the first place b_1 is tied to the entry b")
control("F6c", bool(h5) and bool(h6),
        "both occurrences resolve, so the ordering claim is about real text")
emit()

# ==========================================================================
emit("F7  s_1, s_2 are used in section 7 and declared nowhere")
emit("-" * 78)
present("F7a", "is singular because $s_1=s_2=2$ places it on two resonance "
               "divisors", ["section7.tex"])
present("F7b", "The unsubscripted letter $s$ always denotes this growth "
               "exponent", ["section1.tex"])
present("F7c", "they are a different object, and the subscript is what "
               "distinguishes them", ["section1.tex"],
        "-- section 1 enumerates exactly two uses of s: bare, and s_pm")
absent("F7d", "s_1", ["section1.tex"],
       "-- s_1 is never declared in the notation section")
control("F7e", len(find_all("a_i=\\operatorname{tr}(B_i)")) >= 1,
        "the quantity section 7 calls s_i is declared as a_i in section 1, so "
        "a declared name for it does exist")
emit()

# ==========================================================================
emit("F8  the Katz-multiset convention of section 1 is not the one used")
emit("-" * 78)
present("F8a", "with a dash in the $r(t)$ position when the singular set "
               "contains no fourth point $t$", ["section1.tex"])
present("F8b", "the effective multiset is $(0,0,1)$", ["section3.tex"],
        "-- three slots, no dash")
present("F8c", "the effective multiset is $(1,0,0,0)$", ["section3.tex"],
        "-- four slots, none of which is r(1)")
present("F8d", "the dash in $(\\tfrac12,-,\\tfrac12)$ denotes an",
        ["section3.tex"], "-- a dash in the r(1) position, not r(t)")
present("F8e", "\\widetilde D_5:\\ \\mathrm{PV},\\ (0,0,1,-),\\ \\dim P=3",
        ["section1.tex"], "-- section 1 writes the PV row with FOUR slots")
present("F8f", "$\\widetilde D_5$/PV, whose Katz invariants are $(0,0,1)$",
        ["section4.tex"], "-- section 4 writes the SAME row with THREE")
control("F8g", len(find_all("(0,0,1,-)")) == 1,
        "the 4-slot form occurs exactly once in the paper -- in the table "
        "section 1 declares the convention with -- so the shapes genuinely "
        "differ across sections and are not in the reader")
emit()

# ==========================================================================
emit("F9  a cross-reference that resolves and points at the wrong subsection")
emit("-" * 78)
present("F9a", "It is recorded in the correspondence footnote of "
               "\\S\\ref{ssec:objects} and used", ["section1.tex"])
present("F9b", "\\subsection{The recurrence and its normalisation}"
               "\\label{ssec:recurrence}", ["section1.tex"])
present("F9c", "\\textbf{Correspondence with the deposited record.}",
        ["section1.tex"])
present("F9d", "\\subsection{The three objects, and their comparison}"
               "\\label{ssec:objects}", ["section1.tex"])
emit()

# ==========================================================================
emit("F10 one formula, four typographies")
emit("-" * 78)
present("F10a", "R=\\tfrac14P^2+\\tfrac12P'-Q", ["section1.tex"])
present("F10b", "R=\\tfrac14P^2+\\tfrac12P'-Q", ["section3.tex"])
present("F10c", "R=\\frac{P^2}{4}+\\frac{P'}{2}-Q", ["section6.tex"])
present("F10d", "R=P^2/4+P'/2-Q", ["section9.tex"])
emit()

# ==========================================================================
emit("F11 the same counterexample stated at full length twice")
emit("-" * 78)
present("F11a", "L=\\partial-\\frac{1}{2z}", ["section6.tex"])
present("F11b", "L=\\partial-\\tfrac{1}{2z}", ["section10.tex"])
present("F11c", "with rational witness $w=z$ satisfying $2f+w'/w=0$",
        ["section6.tex", "section10.tex"],
        "-- the identical witness sentence appears in both")
emit()

# ==========================================================================
emit("F12 one discrepancy, two page attributions")
emit("-" * 78)
present("F12a", "A second discrepancy in the same neighbourhood is recorded",
        ["section4.tex"], "-- 'the same neighbourhood' is p. 2655")
present("F12b", "the family $(4.1)$ of p.~2655 is", ["section4.tex"])
present("F12c", "der Put--Saito at p.~2629 states $\\theta_\\infty$",
        ["section7.tex"], "-- the same discrepancy, attributed to p. 2629")
control("F12d", len(find_all("p.~2629")) == 1,
        "2629 occurs exactly once in the paper, so the two attributions are "
        "not a transcription of one another")
emit()

# ==========================================================================
emit("F13 section 10 says machinery is absent that sections 1 and 3 set up")
emit("-" * 78)
present("F13a", "because stating it would require machinery that no section "
                "above sets up", ["section10.tex"])
present("F13b", "One further symbol belongs to the Borel plane of this "
                "asymptotic", ["section1.tex"])
present("F13c", "A \\emph{Stokes constant} is the coefficient with which one "
                "formal solution enters", ["section1.tex"])
present("F13d", "has single action $2/\\sqrt3=\\xi_0$ and action "
                "\\emph{difference} $4/\\sqrt3$", ["section3.tex"])
emit()

# ==========================================================================
emit("F14 two coefficients displayed twice, unnumbered the second time")
emit("-" * 78)
present("F14a", "P_{\\mathsf C}&=\\frac{2z-1}{z(z-1)},\\label{eq:PC}",
        ["section6.tex"])
present("F14b", "P_{\\mathsf C}=\\frac{2z-1}{z(z-1)},\\qquad", ["section9.tex"],
        "-- the same coefficient, re-displayed rather than \\eqref'd")
emit()

# ==========================================================================
emit("=" * 78)
if FAILED:
    emit("READ CHECK: %d PREDICATE(S) FAILED -- %s"
         % (len(FAILED), ", ".join(FAILED)))
    emit("Those findings are WITHDRAWN and must not be reported.")
    emit("=" * 78)
    save()
    sys.exit(1)
emit("READ CHECK: 14 findings, all predicates confirmed; %d controls, %d FIRED"
     % (NCTRL, NCTRL))
emit("=" * 78)
save()
sys.exit(0)
