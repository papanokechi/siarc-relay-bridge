"""CT-S56 -- does the revision deliver what the follow-up email promised?

The email sent to the editor on 2026-09-21 is now a COMMITMENT. It names, by
number, every place it says needs correcting. This checks the revision against
that list rather than against the session's own edit tags -- the tags are what
we believed, the email is what the editor was told.

Two of the email's numbers were checked against the paper before this ran:
  * 'the proof of Corollary 1.3' is CORRECT. CT-S52's tag said 'Cor 1.4 proof',
    and the tag is wrong; the edit itself landed in Corollary 1.3's proof.
  * 'Remark 3.4' is CORRECT, and is the number v1.2 renders. CT-S52's tag said
    'Remark 3.3', which v1.2 does not have.

Every remaining occurrence of 'apparen' and 'independen' in the rendered
revision is listed for classification. The count alone decides nothing: items
3, 4 and 5 all replace assertions with discussion, so the words necessarily
survive. What must not survive is an ASSERTION.
"""
import hashlib
import io
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REV_PDF = SESS / "revision" / "vquad-periodrep-paper.pdf"
OUT = SESS / "outputs" / "email_coverage.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def flat(p):
    d = fitz.open(p)
    t = " ".join(pg.get_text() for pg in d)
    d.close()
    return re.sub(r"\s+", " ", t)


# Assertions the email says must be gone. Each is checked as: present in the
# revision => FAIL. Phrased so that a mere mention cannot satisfy them.
MUST_BE_ABSENT = [
    ("item 4", "xi=0 called apparent (Table 1 cell)", "0 (apparent)"),
    ("item 4", "'the point 0 is apparent'", "the point 0 is apparent"),
    ("item 4", "'so the point is apparent'", "so the point is apparent"),
    ("item 4", "Prop 2.4's 'obtained twice'", "Both statements are obtained twice"),
    ("item 5", "'three structurally independent methods'",
     "three structurally independent methods"),
    ("item 5", "'three independent ways'", "three independent ways"),
    ("item 5", "Method B 'is independent of the Stokes datum'",
     "is independent of the Stokes datum"),
]

# Substance the email promises IS there.
MUST_BE_PRESENT = [
    ("item 4", "the logarithm at xi=0 is stated", "logarithm"),
    ("item 4", "unipotent local monodromy named", "unipotent"),
    ("item 4", "B-hat still holomorphic at 0", "holomorphic"),
    ("item 5", "Method B's S-free figure 3.69", "3.69"),
    ("item 5", "Method C's unaffected figure 9.31", "9.31"),
    ("item R", "the companion's v1.3 is cited", "Papanokechi"),
]

# The email's own list of objects needing correction.
EMAIL_OBJECTS = ["Proposition 2.4", "Lemma 2.7", "Table 1", "Figure 1",
                 "Remark 3.4", "Corollary 1.3"]


def main() -> int:
    t = flat(REV_PDF)

    say("=" * 76)
    say("CT-S56 -- revision checked against the follow-up email's commitments")
    say("=" * 76)
    say("")
    say(f"    revision : {REV_PDF.name}")
    say(f"    sha256   : {hashlib.sha256(REV_PDF.read_bytes()).hexdigest()}")
    say("")

    fails = 0

    say("[1] THE EMAIL'S OBJECT NUMBERS MUST EXIST IN THE REVISION")
    say("    an email that cites an object the paper does not have is the")
    say("    worst class of defect here, because the editor cannot check it")
    for o in EMAIL_OBJECTS:
        ok = o in t
        fails += (not ok)
        say(f"    [{'PASS' if ok else 'FAIL'}] {o}")
    say("")

    say("[2] ASSERTIONS THE EMAIL SAYS ARE CORRECTED -- MUST BE ABSENT")
    for item, desc, probe in MUST_BE_ABSENT:
        gone = probe not in t
        fails += (not gone)
        say(f"    [{'PASS' if gone else 'FAIL'}] {item}: {desc}")
        if not gone:
            i = t.find(probe)
            say(f"           STILL PRESENT: ...{t[max(0,i-70):i+90]}...")
    say("")

    say("[3] SUBSTANCE THE EMAIL PROMISES -- MUST BE PRESENT")
    for item, desc, probe in MUST_BE_PRESENT:
        here = probe in t
        fails += (not here)
        say(f"    [{'PASS' if here else 'FAIL'}] {item}: {desc}")
    say("")

    say("[4] CONTROL -- the absence checks must be able to fail")
    ctl = "Because bB is holonomic"
    say(f"    [{'PASS' if ctl in t else 'FAIL'}] a sentence known to be in the "
        f"revision is found by the same reader")
    fake = "this string is certainly not in the manuscript anywhere"
    say(f"    [{'PASS' if fake not in t else 'FAIL'}] a fabricated string is not "
        f"found")
    if ctl not in t or fake in t:
        fails += 1
    say("")

    say("[5] CENSUS -- every surviving 'apparen' and 'independen'")
    say("    These are NOT defects by count. Items 3, 4 and 5 replace")
    say("    assertions with discussion, so the words must survive. Each is")
    say("    listed so that an ASSERTION cannot hide among the discussion.")
    say("")
    for stem in ("apparen", "independen"):
        ms = list(re.finditer(stem, t, re.I))
        say(f"    --- {stem!r}: {len(ms)} occurrence(s) ---")
        for m in ms:
            seg = t[max(0, m.start() - 95):m.start() + 105]
            say(f"      ...{seg}...")
        say("")

    say("=" * 76)
    if fails:
        say(f"FAIL: {fails} check(s) failed. The revision does not yet deliver")
        say("what the editor has been told.")
    else:
        say("PASS: the revision delivers every commitment the email makes,")
        say("and every object it cites exists in the revision.")
    say("=" * 76)

    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
