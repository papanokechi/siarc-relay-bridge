"""
CT-S23-OUTSIDER-READ - mechanical first-use index over packet/PACKET.md.

Computes G, the subset of the PREREG core term set that is USED BEFORE DEFINED
in the packet. G is the ground truth against which the cold reader's task-2
list is scored (PREREG F2). It is computed BEFORE the read is dispatched and
its output file is hashed, so it cannot be adjusted after the return.

Definition, fixed here and not changed afterwards:

  A core term is USED-BEFORE-DEFINED if its first USE occurrence in the packet
  is not preceded anywhere in the packet by a DEFINITIONAL occurrence.

  USE occurrences are matched by the term's `use` regex.
  DEFINITIONAL occurrences are matched by the term's `defn` regex.
  A term with NO definitional occurrence anywhere is used-before-defined by
  this rule (its first use is preceded by nothing).

DEGENERACY PRE-CHECK on the term set itself, per the clause proposed in
CT-S22-STOKES/P0-AMENDMENT.md: before the set is used, it is tested for
INTERNAL relations independently of the packet. No term's `use` regex may be
implied by another's, i.e. no string may exist that matches two terms' use
patterns where one is a substring alias of the other. An aliasing pair would
inflate |G| with a term that cannot be independently missed. Aliasing pairs
are collapsed and the collapse is reported. If the pre-check cannot fail --
if no candidate aliasing pair is even tested -- that is reported too.

CONTROL (an assertion that can fail): two sentinel terms are added to the run.
  - a term that IS defined early and used late        -> must NOT be in G
  - a term that appears nowhere in the packet at all  -> must NOT be scored
If either sentinel misbehaves the classifier is wrong and the script halts
rather than emitting a G that nothing checked.
"""

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
PACKET = HERE / "packet" / "PACKET.md"
OUT = HERE / "outputs" / "jargon_index.out.txt"

# (key, use-regex, defn-regex or None)
# Declared before running. `defn` is None where the packet is expected to
# carry no definition; the classifier does not depend on that expectation.
TERMS = [
    ("V_quad",          r"V_quad|V\\_quad",                       None),
    ("Channel Theory",  r"Channel Theory",                        None),
    ("System A",        r"\bSystem A\b|\*\*A\*\*",                r"\|\s*\*\*A\*\*\s*\|"),
    ("System B",        r"\bSystem B\b|\*\*B\*\*",                r"\|\s*\*\*B\*\*\s*\|"),
    ("System C",        r"\bSystem C\b",                          r"\*\*System C\*\* is the scalar equation"),
    ("PCF",             r"\bPCF\b",                               None),
    ("xi_0",            r"ξ₀",                                    r"ξ₀ = d / \|β_d\|"),
    ("rho",             r"\bρ\b|ρ_d",                             r"candidate Borel-plane exponent\*\* is `ρ_d"),
    ("K",               r"(?<![A-Za-z_])K(?![A-Za-z_])",          r"K = r_∞ · \(2π\)"),
    ("r_inf",           r"r_∞",                                   r"r_∞ := lim|r_n = Q_n / ∏"),
    ("S_zeta_star",     r"S_\{ζ\*\}",                             r"`S_\{ζ\*\}` is the Stokes constant"),
    ("zeta_star",       r"(?<!S_\{)ζ\*",                          r"ζ\* = \|c₊ − c₋\|"),
    ("B1B2B3",          r"\bB₁\b|\bB1\b|tr\(B",                   r"x₁ = tr\(B"),
    ("Q_n",             r"Q_n|Qₙ",                                r"Q_n = b\(n\) Q_\{n-1\}"),
    ("theta_infty",     r"θ_∞",                                   r"det A_i = −θ_i²/4"),
    ("U_0",             r"U₀",                                    r"chart is `U₀ ≅"),
    ("row_001",         r"\(0,0,1\)",                             r"\(0,0,1\)`\s*\|\s*PV"),
    ("Katz multiset",   r"Katz multiset",                         None),
    ("PV",              r"Painlevé V|\bPV\b|\bP-V\b",             r"Painlevé V is the isomonodromy foliation"),
    ("D5tilde",         r"D̃₅",                                    None),
    ("Stokes constant", r"Stokes constant",                       r"`S_\{ζ\*\}` is the Stokes constant"),
    ("trace coords",    r"trace coordinates|comparison quantities", r"comparison quantities are `x₁, x₂, x₃`"),
]

# --- classifier control -----------------------------------------------------
# Three synthetic arms exercise the three branches against the DEFINITION.
# Two LIVE arms, hand-adjudicated against the packet by reading it, exercise
# the definition against the WORLD. A constructed rehearsal alone checks only
# the code against the definition, never the definition against the material.
#
# First attempt at this control used ("normal potential", defined in §3) as a
# defined-early sentinel and FAILED. The classifier was right and the sentinel
# was wrong: "normal potential" is first USED in §2 (Proposition 5) and only
# explained in §3, so UNDEFINED was the correct verdict. Recorded rather than
# quietly re-tuned, and the arm was replaced.

SYNTHETIC = [
    # (name, text, use, defn, expected)
    ("syn-defined-then-used",
     "We define FOO := 1. Later we use FOO again.",
     r"\bFOO\b", r"define FOO :=", False),
    ("syn-used-then-defined",
     "We use BAR here. Much later: we define BAR := 1.",
     r"\bBAR\b", r"define BAR :=", True),
    ("syn-never-defined",
     "We use BAZ here and never say what it is.",
     r"\bBAZ\b", None, True),
    ("syn-absent",
     "Nothing relevant here.",
     r"\bQUX\b", None, None),
]

# Live arms, verdicts fixed by hand-reading packet/PACKET.md before running:
#   U_0  - §4 states "The chart is `U₀ ≅ C × (C∖{0,1})`" at its first mention
#          -> defined (False)
#   Katz multiset - used in the §2 table, never defined anywhere in the packet
#          -> undefined (True)
LIVE = [
    ("live-U_0", r"U₀", r"chart is `U₀ ≅", False),
    ("live-Katz", r"Katz multiset", None, True),
]


def degeneracy_precheck(terms):
    """Test the term set for INTERNAL relations, independently of the packet.

    Returns (aliases, n_pairs_tested). An alias pair is one where every string
    matching term i's use-regex also matches term j's use-regex, probed over
    the literal alternatives appearing in the patterns themselves.
    """
    def literals(pat):
        # crude but sufficient: the alternation branches, minus regex syntax
        out = []
        for br in pat.split("|"):
            s = re.sub(r"\(\?<!.*?\)|\(\?!.*?\)|\\b|\\\\", "", br)
            s = s.replace("\\", "")
            if s and not any(c in s for c in "()[]{}*+?^$"):
                out.append(s)
        return out

    aliases = []
    pairs = 0
    for i, (ki, ui, _) in enumerate(terms):
        for j, (kj, uj, _) in enumerate(terms):
            if i == j:
                continue
            li = literals(ui)
            if not li:
                continue
            pairs += 1
            if all(re.search(uj, s) for s in li):
                aliases.append((ki, kj))
    return aliases, pairs


def classify(text, use_pat, defn_pat):
    m_use = re.search(use_pat, text)
    if m_use is None:
        return None  # absent from packet
    if defn_pat is None:
        return True  # no definition anywhere -> used before defined
    m_def = re.search(defn_pat, text)
    if m_def is None:
        return True
    return m_def.start() > m_use.start()


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def main():
    text = PACKET.read_text(encoding="utf-8")
    lines = []
    lines.append("CT-S23-OUTSIDER-READ - mechanical first-use index")
    lines.append("packet: %s (%d chars)" % (PACKET.name, len(text)))
    lines.append("packet sha256: %s" % hashlib.sha256(
        PACKET.read_bytes()).hexdigest())
    lines.append("")

    # --- degeneracy pre-check on the term set itself -----------------------
    aliases, pairs = degeneracy_precheck(TERMS)
    lines.append("DEGENERACY PRE-CHECK on the core term set")
    lines.append("  candidate pairs tested : %d" % pairs)
    assert pairs > 0, "degeneracy pre-check tested nothing - it cannot fail"
    if aliases:
        lines.append("  ALIASING PAIRS FOUND   : %s" % aliases)
    else:
        lines.append("  aliasing pairs found   : none")
    collapsed = {a for a, b in aliases}
    lines.append("  terms collapsed        : %s" % (sorted(collapsed) or "none"))
    lines.append("")

    # --- classifier control ------------------------------------------------
    lines.append("CLASSIFIER CONTROL")
    bad = 0
    for name, txt, use, defn, exp in SYNTHETIC:
        got = classify(txt, use, defn)
        ok = got is exp
        bad += 0 if ok else 1
        lines.append("  %-22s -> %-5s expected %-5s  %s"
                     % (name, got, exp, "ok" if ok else "MISMATCH"))
    for name, use, defn, exp in LIVE:
        got = classify(text, use, defn)
        ok = got is exp
        bad += 0 if ok else 1
        lines.append("  %-22s -> %-5s expected %-5s  %s"
                     % (name, got, exp, "ok" if ok else "MISMATCH"))
    if bad:
        lines.append("")
        lines.append("  CONTROL FAILED (%d arm(s)) - G not emitted." % bad)
        OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("\n".join(lines))
        return 2
    lines.append("  all %d arms ok (4 synthetic, 2 live hand-adjudicated)"
                 % (len(SYNTHETIC) + len(LIVE)))
    lines.append("")

    # --- the index ---------------------------------------------------------
    G, defined, absent = [], [], []
    lines.append("%-18s %-8s %-10s %s" % ("term", "1st use", "verdict", "note"))
    lines.append("-" * 64)
    for key, use, defn in TERMS:
        if key in collapsed:
            lines.append("%-18s %-8s %-10s %s" % (key, "-", "COLLAPSED",
                                                  "alias of another term"))
            continue
        v = classify(text, use, defn)
        m = re.search(use, text)
        ln = line_of(text, m.start()) if m else "-"
        if v is None:
            absent.append(key)
            lines.append("%-18s %-8s %-10s %s" % (key, "-", "ABSENT",
                                                  "not used in packet"))
        elif v:
            G.append(key)
            note = "no definition in packet" if defn is None else \
                   "first use precedes definition"
            lines.append("%-18s %-8s %-10s %s" % (key, ln, "UNDEFINED", note))
        else:
            defined.append(key)
            lines.append("%-18s %-8s %-10s %s" % (key, ln, "defined", ""))

    lines.append("")
    lines.append("G (used before defined), |G| = %d:" % len(G))
    for k in G:
        lines.append("  - %s" % k)
    lines.append("")
    lines.append("defined in packet, %d: %s" % (len(defined), defined))
    lines.append("absent from packet, %d: %s" % (len(absent), absent))
    lines.append("")
    lines.append("PREREG F2: the cold read is recorded as LOW-SENSITIVITY if")
    lines.append("  |T2 n G| / |G| < 0.5, i.e. fewer than %d of the %d above."
                 % (-(-len(G) // 2), len(G)))

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))

    # read back what was written
    back = OUT.read_text(encoding="utf-8")
    assert "G (used before defined)" in back, "readback failed"
    print("\nreadback OK; sha256 %s" %
          hashlib.sha256(OUT.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
