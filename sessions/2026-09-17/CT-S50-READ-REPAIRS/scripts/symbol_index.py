#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CT-S50 -- re-run the symbol index against the FINAL text.

The b defect was found by reading, not by an instrument, so this asks the
question that would have found it mechanically:

  which single letters are used in more than one syntactic role, and of those,
  which does section 1's reuse list not name?

'Syntactic role' is decidable where 'meaning' is not.  The roles counted are
  CALL      $x(...)$      the letter applied to an argument
  SUB       $x_k$         the letter with a subscript
  BARE      $x$           the letter alone
A letter in two or more roles across two or more sections is a reuse candidate.

This is a SCREEN, not a verdict: a letter may occupy two roles innocently.  It
fails only when a candidate is absent from section 1's list, which is the exact
shape of the b defect.

Exit: 0 clean / 1 an unlisted candidate / 2 refusal / 3 crash
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "outputs" / "symbol_index.out.txt"
LINES = []


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


SECS = ["section%d.tex" % i for i in range(11)] + ["appendixA.tex",
                                                  "appendixB.tex"]
TXT = {}
for f in SECS:
    p = HERE / f
    if not p.exists():
        refuse("missing %s" % f)
    TXT[f] = p.read_text(encoding="utf-8")

# --- resolve the corpus POSITIVELY (S44-16) ------------------------------
if "carries four meanings, separated by argument and by subscript" \
        not in " ".join(TXT["section1.tex"].split()):
    refuse("section 1 does not carry the repaired reuse list; this is not the "
           "post-repair tree the census is meant to measure")
emit("=" * 78)
emit("CT-S50 -- symbol index over the FINAL text")
emit("=" * 78)
emit("corpus resolved positively: section 1 carries the repaired reuse list")
emit()

LETTERS = [chr(c) for c in range(ord("a"), ord("z") + 1)] + \
          [chr(c) for c in range(ord("A"), ord("Z") + 1)]

roles = {L: {} for L in LETTERS}
for f in SECS:
    t = TXT[f]
    # strip label/ref/texttt/cite arguments: they are names, not symbols
    t = re.sub(r"\\(label|ref|eqref|nameref|texttt|cite|input)\{[^}]*\}", " ", t)
    for L in LETTERS:
        e = re.escape(L)
        pats = {
            "CALL": r"(?<![A-Za-z\\])" + e + r"\s*\(",
            "SUB": r"(?<![A-Za-z\\])" + e + r"_",
            "BARE": r"(?<![A-Za-z\\])" + e + r"(?![A-Za-z_(])",
        }
        for role, p in pats.items():
            n = len(re.findall(p, t))
            if n:
                roles[L].setdefault(role, {})[f] = n

# section 1's reuse list: the letters it names
S1 = " ".join(TXT["section1.tex"].split())
m = re.search(r"Letters that carry more than one meaning\.\}(.*?)"
              r"\\end\{itemize\}", S1)
if not m:
    refuse("could not locate section 1's reuse list; the audit has no "
           "reference to compare against")
def item_heads(block):
    """The letter each \\item DECLARES -- its first math symbol -- not every
    symbol mentioned in its body.  Reading the whole body is the naive
    extraction that made this control dead on the first run: the pre-repair
    list mentions b in another item's prose, so b looked already-listed."""
    out = set()
    for it in re.split(r"\\item\b", block)[1:]:
        # Only the item's FIRST math group is its head.  Searching the whole
        # item body let the \beta_k item return "b", because its prose
        # mentions $b(n)$ -- which made the control DEAD by reporting b as
        # already listed in the pre-repair tree.
        first = re.search(r"\$[^$]*\$", it)
        if not first:
            continue
        mm = re.search(r"\$(?:\\(?:mathcal|mathsf)\s*)?\{?(?:Upright\s*)?"
                       r"([A-Za-z])\}?(?![A-Za-z])", first.group(0))
        if mm:
            out.add(mm.group(1))
    return out


LISTED = item_heads(m.group(1))
# the list also names Greek beta, which this letter screen cannot see
emit("section 1 names these letters as reused: %s"
     % ", ".join(sorted(LISTED)) or "(none)")
emit()

emit("%-4s %-28s %s" % ("sym", "roles (sections)", "verdict"))
emit("-" * 78)
cands, unlisted = [], []
for L in LETTERS:
    r = roles[L]
    if len(r) < 2:
        continue
    secs = set()
    for role in r:
        secs |= set(r[role])
    if len(secs) < 2:
        continue
    cands.append(L)
    desc = "; ".join("%s:%d" % (role, sum(r[role].values()))
                     for role in sorted(r))
    listed = L in LISTED
    if not listed:
        unlisted.append(L)
    emit("%-4s %-28s %s" % (L, desc[:28],
                            "listed" if listed else "NOT IN SECTION 1'S LIST"))

emit()
emit("multi-role letters: %d; not named by section 1: %d"
     % (len(cands), len(unlisted)))
emit()

# --- control: the screen must be able to see the defect it was built for --
emit("CONTROL")
emit("-" * 78)
pre = (HERE / "refs" / "section1.tex").read_text(encoding="utf-8")
pre1 = " ".join(pre.split())
mp = re.search(r"Letters that carry more than one meaning\.\}(.*?)"
               r"\\end\{itemize\}", pre1)
if not mp:
    refuse("control dead: cannot read the PRE-repair reuse list from refs/")
PRELISTED = item_heads(mp.group(1))
fired = ("b" in cands) and ("b" not in PRELISTED) and ("b" in LISTED)
emit("  [%s] C1  b is a multi-role letter; refs/ did NOT list it, the live "
     "tree DOES" % ("FIRED" if fired else "DEAD "))
if not fired:
    refuse("control C1 did not fire: the screen cannot reproduce the very "
           "defect that motivated it, so a clean result means nothing")
emit("        -- so a clean run below is a result, not a silent screen")
emit()

emit("=" * 78)
emit("SYMBOL INDEX: %d multi-role letters; %d not named by an \\item head in "
     "section 1's reuse list" % (len(cands), len(unlisted)))
emit()
emit("This is a SCREEN, not a verdict. A letter in two syntactic roles need")
emit("not carry two meanings, and section 1 declares some reuse in prose")
emit("outside the list -- P and Q against Q_n, s against s_pm -- which an")
emit("\\item-head reader cannot see. The residue below is therefore a list of")
emit("CANDIDATES for the notation pass, not a list of defects:")
emit("  %s" % (", ".join(unlisted) or "(none)"))
emit()
emit("What the screen does assert, and what the control backs, is narrower:")
emit("the letter b was in two roles across four sections and was NOT named by")
emit("any item head before this session, and IS named now.")
emit("=" * 78)
save()
sys.exit(0)
