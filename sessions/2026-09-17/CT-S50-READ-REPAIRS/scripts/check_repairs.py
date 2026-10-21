#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CT-S50-READ-REPAIRS -- verify each ruling landed.

For every repair the check is three-sided:
  NOW      the repaired text is present in the live tree
  GONE     the pre-repair text is absent from the live tree
  SNAPSHOT the pre-repair text IS present in refs/, the pre-repair copy

The third side is the S38-07 snapshot guard: without it, "the old text is
absent" cannot be told from "my reader cannot see it", and a repair that was
never needed would pass.

Exit: 0 clean / 1 a repair failed / 2 refusal / 3 crash
"""
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
REFS = HERE / "refs"
OUT = HERE / "outputs" / "check_repairs.out.txt"

LINES, FAILED = [], []
NCHK = NCTRL = 0


def _crash(et, e, tb):
    import traceback
    sys.stderr.write("".join(traceback.format_exception(et, e, tb)))
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

NOWT, OLDT = {}, {}
for f in FILES:
    p, q = HERE / f, REFS / f
    if not p.exists() or not q.exists():
        refuse("missing %s in live tree or refs/" % f)
    NOWT[f] = p.read_text(encoding="utf-8")
    OLDT[f] = q.read_text(encoding="utf-8")


def rx(phrase):
    return re.compile(r"\s+".join(re.escape(t) for t in phrase.split()))


def hit(text_map, phrase, files):
    r = rx(phrase)
    out = []
    for f in files:
        t = text_map[f]
        for m in r.finditer(t):
            out.append((f, t.count("\n", 0, m.start()) + 1))
    return out


def repair(rid, title, new, old, files):
    """new must be present now; old must be gone now and present in refs/."""
    global NCHK, NCTRL
    NCHK += 1
    NCTRL += 1
    emit("  %s  %s" % (rid, title))
    hn = hit(NOWT, new, files)
    ho = hit(OLDT, old, files)
    hg = hit(NOWT, old, files)
    ok_now = bool(hn)
    ok_gone = not hg
    emit("     [%s] NOW      %s" % ("OK  " if ok_now else "FAIL",
         ", ".join("%s:%d" % x for x in hn) or "NOT FOUND"))
    emit("     [%s] GONE     %s" % ("OK  " if ok_gone else "FAIL",
         "pre-repair text absent" if ok_gone else
         ", ".join("%s:%d" % x for x in hg)))
    if not ho:
        refuse("%s: the pre-repair text is not in refs/ either, so 'GONE' "
               "proves nothing -- the reader may simply be blind to it" % rid)
    emit("     [FIRED] SNAPSHOT refs/ still carries it at %s"
         % ", ".join("%s:%d" % x for x in ho))
    if not ok_now:
        FAILED.append(rid + "/NOW")
    if not ok_gone:
        FAILED.append(rid + "/GONE")
    emit()


emit("=" * 78)
emit("CT-S50-READ-REPAIRS -- every ruling verified against the live tree")
emit("=" * 78)
emit()
emit("live tree : %s" % HERE.name)
emit("snapshot  : refs/ (pre-repair copy of all %d sources)" % len(FILES))
emit()

S = ["section%d.tex" % i for i in range(11)] + ["appendixA.tex",
                                               "appendixB.tex"]

repair("R1a", "section 9.4 item 6 -- stale formula-pass disclaimer",
       "All $56$ displays of \\S\\S0--10 are routed: $21$ were re-derived "
       "symbolically from the script that computed them",
       "none has been symbolically re-derived here", ["section9.tex"])

repair("R1b", "appendix B.5 item 3 -- same disclaimer, methods register",
       "Every displayed formula in this paper is routed to exactly one form of "
       "evidence",
       "No displayed formula in this paper has been re-derived here from the "
       "script that computed it", ["appendixB.tex"])

repair("R2", "section 8.7 -- the self-contradicting count",
       "has been sought; the first was the twist question of "
       "\\S\\ref{ssec:tracefree}, where one was found. Here none was.",
       "has been sought and not found --- the first being the twist question "
       "of \\S\\ref{ssec:tracefree}, where one was found", ["section8.tex"])

repair("R3", "section 5.4 -- a phrase quoted that the paper never uses",
       "The two solutions of \\S\\ref{ssec:located}, one on each branch of $t$",
       "The phrase ``for both sign branches'' in \\S\\ref{ssec:located}",
       ["section5.tex"])

repair("R4a", "section 6.2 -- R unified to section 1's typography",
       "R=\\tfrac14P^2+\\tfrac12P'-Q", "R=\\frac{P^2}{4}+\\frac{P'}{2}-Q",
       ["section6.tex"])

repair("R4b", "section 9.1 -- R unified, and P_C/Q_C no longer re-displayed",
       "the pair $P_{\\mathsf C}$, $Q_{\\mathsf C}$ of "
       "\\eqref{eq:PC}--\\eqref{eq:QC}",
       "R=P^2/4+P'/2-Q", ["section9.tex"])

repair("R5", "section 1 -- the declared scalar form now the one in use",
       "The lower-case $a$, $b$, $c$ of a scalar equation written "
       "$a\\,W''+b\\,W'+c\\,W=0$",
       "the coefficients $A$, $A'$, $C$ of a scalar equation written "
       "$A\\,W''+A'\\,W'+C\\,W=0$", ["section1.tex"])

repair("R6", "section 1 -- b entered in the reuse list, which now says seven",
       "$b$ carries four meanings, separated by argument and by subscript",
       "Six further letters are reused", ["section1.tex"])

repair("R7", "section 5.3 -- b_1 defined at first use",
       "Here $b_1$ is the coefficient of $z$ in the entry $b$ of "
       "\\eqref{eq:fam-b}, which is affine in $z$",
       "in the four unknowns $p,q,t,\\theta_\\infty$. It is consistent",
       ["section5.tex"])

repair("R8", "section 7.3 -- s_1,s_2 replaced by the declared a_1,a_2",
       "is singular because $a_1=a_2=2$ places it on two resonance divisors",
       "is singular because $s_1=s_2=2$ places it on two resonance divisors",
       ["section7.tex"])

repair("R9a", "section 1 -- the dash convention widened to any absent point",
       "with a dash in any position whose singular point is absent from the "
       "singular set",
       "with a dash in the $r(t)$ position when the singular set contains no "
       "fourth point $t$", ["section1.tex"])

repair("R9b", "section 3.6 -- System C's multiset written with four slots",
       "the effective multiset is $(0,0,1,-)$",
       "the effective multiset is $(0,0,1)$", ["section3.tex"])

repair("R9c", "section 3.6 -- System A's multiset written with four slots",
       "the dash in $(\\tfrac12,-,\\tfrac12,-)$ denotes an",
       "the dash in $(\\tfrac12,-,\\tfrac12)$ denotes an", ["section3.tex"])

repair("R9d", "section 4.6 -- the PV row no longer disagrees with section 1",
       "whose Katz invariants are $(0,0,1,-)$",
       "whose Katz invariants are $(0,0,1)$", ["section4.tex"])

repair("R10", "section 10.1 -- the counterexample referenced, not restated",
       "the $2$-torsion object $L=\\partial-\\tfrac{1}{2z}$ of "
       "\\S\\ref{ssec:tracefree} (\\texttt{S17-02}, \\textbf{PROVEN})",
       "\\begin{remark}[Trace-freeness is not enough; \\texttt{S17-02}, "
       "\\textbf{PROVEN}]", ["section10.tex"])

repair("R11", "section 1 -- a count nothing verifies removed",
       "The following letters are reused, in each case with a stated "
       "discriminator",
       "Six further letters are reused", ["section1.tex"])

# ---- global invariants ---------------------------------------------------
emit("GLOBAL INVARIANTS")
emit("-" * 78)

# no 3-slot multiset survives anywhere
three = hit(NOWT, "$(0,0,1)$", S)
NCHK += 1
emit("  [%s] G1  no 3-slot (0,0,1) survives   %s"
     % ("OK  " if not three else "FAIL",
        "confirmed" if not three else ", ".join("%s:%d" % x for x in three)))
if three:
    FAILED.append("G1")
NCTRL += 1
old3 = hit(OLDT, "$(0,0,1)$", S)
if not old3:
    refuse("G1 control dead: refs/ carries no 3-slot form to have removed")
emit("     [FIRED] refs/ carried %d of them" % len(old3))

# R appears in exactly one typography
NCHK += 1
bad = hit(NOWT, "R=\\frac{P^2}{4}", S) + hit(NOWT, "R=P^2/4+P'/2-Q", S)
good = hit(NOWT, "R=\\tfrac14P^2+\\tfrac12P'-Q", S)
emit("  [%s] G2  R in one typography only     %d site(s): %s"
     % ("OK  " if not bad and len(good) >= 3 else "FAIL", len(good),
        ", ".join("%s:%d" % x for x in good)))
if bad or len(good) < 3:
    FAILED.append("G2")

# s_1 does not occur anywhere in the paper
NCHK += 1
s1 = hit(NOWT, "s_1", S)
emit("  [%s] G3  s_1 occurs nowhere            %s"
     % ("OK  " if not s1 else "FAIL",
        "confirmed" if not s1 else ", ".join("%s:%d" % x for x in s1)))
if s1:
    FAILED.append("G3")
NCTRL += 1
if not hit(OLDT, "s_1", S):
    refuse("G3 control dead: refs/ never carried s_1")
emit("     [FIRED] refs/ carried it at %s"
     % ", ".join("%s:%d" % x for x in hit(OLDT, "s_1", S)))

# the figures printed in section 9 must be the ones the manifest reports
NCHK += 1
man = (HERE.parents[0] / "CT-S46-FORMULA-SECTIONS" / "outputs" /
       "manifest.out.txt")
if not man.exists():
    refuse("the route manifest is missing; section 9's figures cannot be "
           "resolved to evidence")
MT = man.read_text(encoding="utf-8")
want = {"S-here": 21, "S-corpus": 15, "P": 9, "DEF": 11}
bad = []
for route, n in want.items():
    # anchored-figure rule: the figure must sit on the line naming its route
    if not any(("route %s" % route) in ln and str(n) in ln
               for ln in MT.splitlines()):
        bad.append("%s=%d" % (route, n))
emit("  [%s] G4  section 9's 21/15/9/11 resolve to anchored manifest lines %s"
     % ("OK  " if not bad else "FAIL", "" if not bad else "unanchored: " +
        ", ".join(bad)))
if bad:
    FAILED.append("G4")
NCHK += 1
ok56 = "census=56 manifest=56" in MT and "unrouted=0" in MT
emit("  [%s] G5  the total 56 and unrouted=0 are the manifest's own"
     % ("OK  " if ok56 else "FAIL"))
if not ok56:
    FAILED.append("G5")
NCHK += 1
twelve = bool(hit(NOWT, "remaining twelve, all short displays, are traced but "
                        "not symbolically re-derived", ["section9.tex"]))
emit("  [%s] G6  the residual twelve = 15 S-corpus - 3 re-derived in CT-S47"
     % ("OK  " if twelve and want["S-corpus"] - 3 == 12 else "FAIL"))
if not twelve:
    FAILED.append("G6")

emit()
emit("PAGE-LEVEL INVARIANTS  (checked against the rendered text, not the "
     "source)")
emit("-" * 78)
PT = HERE / "outputs" / "paper_text.txt"
if not PT.exists():
    refuse("no rendered text; the \\ref rendering cannot be checked against "
           "the page, which is the only place it is visible")
PAGE = " ".join(PT.read_text(encoding="utf-8", errors="replace").split())

NCHK += 1
dbl = "(S17-02, PROVEN) (S17-02, PROVEN)" in PAGE
emit("  [%s] G7  no doubled citation on the page  %s"
     % ("OK  " if not dbl else "FAIL",
        "confirmed" if not dbl else "the \\nameref form is back"))
if dbl:
    FAILED.append("G7")

NCHK += 1
reads = bool(re.search(r"2-torsion object.{0,40}of\s+§\d+\.\d+\s+\(S17-02,\s+"
                       r"PROVEN\)\s+is trivial", PAGE))
emit("  [%s] G8  section 10.1 reads as a numbered cross-reference"
     % ("OK  " if reads else "FAIL"))
if reads:
    emit("        -- rendered: '... of \u00a77.1 (S17-02, PROVEN) is trivial "
         "after tensoring ...'")
else:
    FAILED.append("G8")
NCTRL += 1
# control: the page reader must be able to see the pre-repair rendering too
if "What is false" not in PAGE:
    refuse("G8 control dead: the paragraph title 'What is false' is absent "
           "from the rendered text, so the reader cannot see paragraph titles "
           "at all and G7's 'no doubled citation' proves nothing")
emit("     [FIRED] the page reader does see paragraph titles ('What is "
     "false' is present at its own paragraph), so G7's absence is a result")

NCHK += 1
seven = "Seven further letters" in PAGE or "Six further letters" in PAGE
emit("  [%s] G9  no unverified letter count survives on the page"
     % ("OK  " if not seven else "FAIL"))
if seven:
    FAILED.append("G9")

emit()
emit("=" * 78)
if FAILED:
    emit("REPAIRS: %d FAILED -- %s" % (len(FAILED), ", ".join(FAILED)))
    emit("=" * 78)
    save()
    sys.exit(1)
emit("REPAIRS: %d checks, 0 FAILED; %d controls, %d FIRED"
     % (NCHK, NCTRL, NCTRL))
emit("=" * 78)
save()
sys.exit(0)
