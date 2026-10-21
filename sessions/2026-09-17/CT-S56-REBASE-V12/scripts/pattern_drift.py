"""CT-S56 -- the 'independent' vs 'independen' pattern question, settled from
files that still exist.

WHY THIS SCRIPT EXISTS, STATED PLAINLY: the original after-sweep output was the
only evidence that the two inline sweep runs used DIFFERENT patterns. It was
backed up, then deleted during a tidy-up in this same session, and nothing is
committed, so it is not recoverable. The claim that rested on it can no longer
be verified from disk.

What IS still decidable is the part that matters for the revision, and this
script settles it against the current files:

  * on v1.2 the two patterns are indistinguishable -- identical count, identical
    lines. An instrument choice made here looks free.
  * on the revision they are not, because item 5's new prose says "Its
    independence from B and C", which 'independent' cannot match.

That is the finding: a pattern whose inadequacy is invisible on the base and
material on the revision. The stem is adopted for both runs in sweep.py.

Exit 0 clean, 1 finding, 2 refusal.
"""
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent

BASE = SESS / "refs" / "src-v1.2" / "vquad-periodrep-paper.tex"
REV = SESS / "revision" / "vquad-periodrep-paper.tex"
OUT = SESS / "outputs" / "pattern_drift.out.txt"

NARROW = re.compile(r"independent", re.I)
STEM = re.compile(r"independen", re.I)

lines = []


def say(s=""):
    print(s)
    lines.append(s)


def read(p):
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n").split("\n")


def hits(pat, ls):
    return [(i + 1, l.strip()) for i, l in enumerate(ls) if pat.search(l)]


def main():
    for p in (BASE, REV):
        if not p.exists():
            say(f"REFUSED: {p} missing")
            return 2

    say("=" * 74)
    say("CT-S56 -- 'independent' vs the stem 'independen'")
    say("=" * 74)
    say()

    b, r = read(BASE), read(REV)
    bn, bs = hits(NARROW, b), hits(STEM, b)
    rn, rs = hits(NARROW, r), hits(STEM, r)

    say("[1] ON THE BASE THE TWO PATTERNS ARE INDISTINGUISHABLE")
    say(f"    v1.2  'independent' : {len(bn)} line(s)")
    say(f"    v1.2  'independen'  : {len(bs)} line(s)")
    same_base = [x[0] for x in bn] == [x[0] for x in bs]
    say(f"    [{'PASS' if same_base else 'FAIL'}] identical line sets on v1.2")
    say("    This is why the choice could be made carelessly and nothing")
    say("    would show. A check that cannot discriminate on the data you")
    say("    have is not thereby adequate for the data you will have.")
    say()

    say("[2] ON THE REVISION THEY ARE NOT")
    say(f"    revision  'independent' : {len(rn)} line(s)")
    say(f"    revision  'independen'  : {len(rs)} line(s)")
    extra = [x for x in rs if x[0] not in {y[0] for y in rn}]
    say(f"    lines the narrow pattern MISSES : {len(extra)}")
    for ln, t in extra:
        say(f"       L{ln:<6} {t[:96]}")
    disc = len(extra) > 0
    say(f"    [{'PASS' if disc else 'FAIL'}] the revision discriminates the two")
    say()

    say("[3] WHAT THE MISSED LINE IS")
    say("    It is Method A's independence claim -- the one the operator")
    say("    required be stated as assumed rather than measured. A sweep")
    say("    that cannot see it is a sweep that cannot audit item 5.")
    say()

    say("[4] CONTROL -- the comparison must be able to fail")
    ctrl_a = NARROW.search("this is independent of S") is not None
    ctrl_b = NARROW.search("Its independence from B and C") is None
    ctrl_c = STEM.search("Its independence from B and C") is not None
    for ok, txt in ((ctrl_a, "'independent' DOES match an adjectival use"),
                    (ctrl_b, "'independent' does NOT match 'independence'"),
                    (ctrl_c, "the stem DOES match 'independence'")):
        say(f"    [{'PASS' if ok else 'FAIL'}] {txt}")
    say()

    say("[5] WHAT IS NOT ESTABLISHED HERE")
    say("    Whether the ORIGINAL inline before- and after-sweeps used")
    say("    different patterns is no longer checkable: the original")
    say("    after-sweep output was deleted during this session's tidy-up")
    say("    and nothing is committed, so it cannot be recovered. It is")
    say("    recorded as an observation made while the file existed, not as")
    say("    a verified claim. The repair -- one pattern for both runs -- does")
    say("    not depend on it.")
    say()

    ok = same_base and disc and ctrl_a and ctrl_b and ctrl_c
    say("CLEAN" if ok else "FINDING")
    say("=" * 74)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
