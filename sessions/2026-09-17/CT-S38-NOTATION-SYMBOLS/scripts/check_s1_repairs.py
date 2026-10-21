#!/usr/bin/env python3
r"""check_s1_repairs -- the three authorised section-1 repairs.

Ruling: fix section 1, not section 3.  The false exclusivity claim about rho
is replaced by a statement of rho's two meanings; the collisions that sit
INSIDE section 1 -- Q against Q_n, and s against s_pm -- are separated the way
section 1 already separates sans-serif A,B,C from the coefficients A,A',C, by
naming the distinction rather than renaming the letter.

The re-lettering and the prose repair are separate changes and are kept
separately auditable:
    refs/section1-pre-S38.tex       before the rename
    refs/section1-symbols-only.tex  after the rename, before this repair
    section1.tex                    after both

Each check carries a mutant arm; an arm that is not rejected means the check
cannot fail and the repair is unverified.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(HERE)
CUR = os.path.join(SESS, "section1.tex")
SNAP = os.path.join(SESS, "refs", "section1-symbols-only.tex")
THM = os.path.join(SESS, "theorem.tex")
THM_OLD = os.path.join(SESS, "refs", "theorem-pre-S38.tex")

FALSE_CLAIM = r"never\s+used\s+for\s+anything\s+else"


def read_or_fail(p):
    try:
        with open(p, "r", encoding="utf-8") as fh:
            return fh.read().replace("\r\n", "\n")
    except Exception as exc:
        print("READER INTEGRITY FAILED: cannot read %s (%s)" % (p, exc))
        sys.exit(4)


def flat(t):
    return re.sub(r"\s+", " ", t)


def nsub(t, sym):
    """Occurrences of a subscripted symbol, e.g. \\psi_1, \\nu_d."""
    return len(re.findall(re.escape(sym) + r"(?![A-Za-z0-9])", t))


def thm_checks(new, old):
    r"""The r_1 ambiguity inside theorem.tex.

    The pre-rename file used r_1 for TWO objects: the first root of b, in
    'r_1,...,r_d are the roots', and the first term of the normalised
    sequence, in 'psi_0 = 1 and psi_1 = Q_1/b(1)'.  A rename that sent both to
    nu_1, or both to psi_1, would leave the file compiling, the page count
    unchanged and the rendered multiset equal under the map -- and the
    ambiguity intact.  Neither the build nor the rendered diff can see this.
    """
    fn, fo = flat(new), flat(old)
    root_new = "\\nu_1,\\dots,\\nu_d" in fn
    root_old = "r_1,\\dots,r_d" in fo
    # the root phrase must not have been given the sequence letter
    root_as_psi = "\\psi_1,\\dots,\\psi_d" in fn
    return [
        ("R8 theorem.tex: the roots are nu_1..nu_d, not psi",
         root_new and not root_as_psi),
        ("R9 theorem.tex: exactly 1 nu_1 and 1 nu_d (the root sentence)",
         nsub(new, "\\nu_1") == 1 and nsub(new, "\\nu_d") == 1),
        ("R10 theorem.tex: the 5 sequence sites became psi_1",
         nsub(new, "\\psi_1") == 5),
        ("R11 theorem.tex: no r_1 or r_d survives",
         nsub(new, "r_1") == 0 and nsub(new, "r_d") == 0),
        ("R12 non-vacuity: the old file really did overload r_1",
         root_old and nsub(old, "r_1") == 6),
    ]


def checks(t):
    f = flat(t)
    refs = set(re.findall(r"\\(?:eq)?ref\{([^}]+)\}", t))
    labels = set(re.findall(r"\\label\{([^}]+)\}", t))
    return [
        ("R1 the false rho exclusivity claim is gone",
         not re.search(FALSE_CLAIM, f)),
        ("R2 rho's two meanings are stated, with the subscript rule",
         "the letter $\\rho$ carries two meanings" in f
         and "\\rho_\\pm=(-1\\pm i\\sqrt{11})/2" in f
         and "separated by the presence of a subscript" in f),
        ("R3 Q is separated from the denominators Q_n",
         "a different object from the denominators $Q_n$" in f
         and "P$ and $Q$ never do" in f),
        ("R4 s is separated from s_pm",
         "The unsubscripted letter $s$ always denotes this growth exponent"
         in f and "subscripted $s_\\pm$" in f),
        ("R5 every \\ref target has a \\label in this file",
         refs <= labels),
        ("R6 the re-lettering survived the repair",
         not re.search(r"(?<![A-Za-z\\])q_", t)
         and not re.search(r"\\lambda(?![A-Za-z])", t)
         and "\\psi_n\\leftrightarrow r_n" in t
         and "10.5281/zenodo.19941678" in t),
        ("R7 the deposit footnote still names the deposited symbols",
         all(re.search(r"(?<![A-Za-z\\])" + re.escape(p) + r"(?![A-Za-z])", t)
             for p in [r"r_n", r"r_\infty", r"r_1", r"r_d"])),
    ]


def main():
    cur = read_or_fail(CUR)
    snap = read_or_fail(SNAP)
    print("check_s1_repairs -- the three authorised section-1 repairs")
    print("  section1.tex                   %6d B" % len(cur))
    print("  refs/section1-symbols-only.tex %6d B" % len(snap))

    print("\n[non-vacuity: the repair is a real change]")
    nv = [
        ("the snapshot still carries the false claim",
         bool(re.search(FALSE_CLAIM, flat(snap)))),
        ("the current file does not", not re.search(FALSE_CLAIM, flat(cur))),
        ("the repair added text", len(cur) > len(snap)),
    ]
    for label, good in nv:
        print("  %-52s %s" % (label, "ok" if good else "FAILED"))
    if not all(g for _l, g in nv):
        print("HALT: the repair is not distinguishable from doing nothing.")
        sys.exit(1)

    print("\n[checks]")
    rows = checks(cur)
    thm = read_or_fail(THM)
    thm_old = read_or_fail(THM_OLD)
    rows = rows + thm_checks(thm, thm_old)
    bad = 0
    for label, good in rows:
        print("  %-52s %s" % (label, "ok" if good else "FAILED"))
        bad += 0 if good else 1

    print("\n[arms -- each mutation must be REJECTED, by the named check]")
    arms = [
        ("A1 the false claim restored", "R1",
         lambda t: t.replace(
             "In this paper the letter $\\rho$ carries two meanings",
             "The letter $\\rho$ is never used for anything else. "
             "In this paper the letter $\\rho$ carries two meanings", 1)),
        ("A2 the Q paragraph deleted", "R3",
         lambda t: re.sub(
             r"The coefficients \$P\$ and \$Q\$ of an equation.*?"
             r"equation \$\\mathsf C\$\.", "", t, flags=re.S)),
        ("A3 the s paragraph deleted", "R4",
         lambda t: re.sub(
             r"The unsubscripted letter \$s\$.*?distinguishes\s+them\.",
             "", t, flags=re.S)),
        ("A4 a dangling reference introduced", "R5",
         lambda t: t.replace("\\eqref{eq:n-rec}",
                             "\\eqref{eq:does-not-exist}", 1)),
        ("A5 the rename undone", "R6",
         lambda t: t.replace("\\psi_n", "q_n")),
    ]
    nmiss = 0
    for name, want, mut in arms:
        mrows = dict(((l.split()[0], g) for l, g in checks(mut(cur))))
        fired = [k for k, g in mrows.items() if not g]
        ok = want in fired
        print("  %-46s %s  (fired: %s)"
              % (name, "CAUGHT" if ok else "MISSED",
                 ", ".join(sorted(fired)) or "nothing"))
        nmiss += 0 if ok else 1

    print("\n[arms -- theorem.tex's r_1 ambiguity]")
    tarms = [
        ("A6 both roles collapsed onto psi_1", "R8",
         lambda t: t.replace("\\nu_1,\\dots,\\nu_d", "\\psi_1,\\dots,\\psi_d")),
        ("A7 one sequence site left un-renamed", "R10",
         lambda t: t.replace("\\psi_1", "r_1", 1)),
        ("A8 both roles collapsed onto nu_1", "R10",
         lambda t: t.replace("\\psi_1", "\\nu_1")),
    ]
    for name, want, mut in tarms:
        mrows = dict(((l.split()[0], g)
                      for l, g in thm_checks(mut(thm), thm_old)))
        fired = [k for k, g in mrows.items() if not g]
        ok = want in fired
        print("  %-46s %s  (fired: %s)"
              % (name, "CAUGHT" if ok else "MISSED",
                 ", ".join(sorted(fired)) or "nothing"))
        nmiss += 0 if ok else 1
    arms = arms + tarms

    print("\n[verdict]")
    print("  checks run    : %d" % len(rows))
    print("  checks failed : %d" % bad)
    print("  arms CAUGHT   : %d/%d" % (len(arms) - nmiss, len(arms)))
    if bad or nmiss:
        print("  VERDICT: SECTION-1 REPAIRS NOT VERIFIED")
        sys.exit(1)
    print("  VERDICT: SECTION-1 REPAIRS VERIFIED")
    sys.exit(0)


if __name__ == "__main__":
    main()
