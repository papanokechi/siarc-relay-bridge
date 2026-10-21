"""CT-S57 -- do the objects the FOLLOW-UP email cites exist in the version LMP holds?

Same question as email1_objects.py, asked of the second email. An email citing
an object the editor's copy does not contain is the worst class of defect
available here: the editor cannot check it and the author cannot see it.

The follow-up was written against the journal's PDF -- the operator said so
explicitly ("it cites the journal copy's numbering ... which I read off the PDF
Editorial Manager holds, not off CT-S52's base") -- so this check can genuinely
fail, and the revision's own 27-page numbering must NOT be used here.

One addition over email1_objects.py: the list of cited objects below is
hand-read off the email, so it could be wrong in the direction that matters
least visibly -- by naming something the email never cites. Step [0] therefore
checks every entry against the email text itself before any of it is looked
for in the PDF. A citation list that cannot be found in its own email is not
evidence about the PDF.

Exit 0 clean, 1 finding, 2 refusal.
"""
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
ROOT = SESS.parents[2]

V12_PDF = (ROOT / "sessions/2026-09-17/CT-S56-REBASE-V12"
           / "refs/src-v1.2/vquad-periodrep-paper.pdf")
V12_MD5 = "792107efab6317e8ae21e2ca20f092ff"
EMAIL = SESS / "email" / "followup_as_sent.txt"
OUT = SESS / "outputs" / "email2_objects.out.txt"

# Numbered objects the follow-up names, hand-read off its text.
# (email_pattern, pdf_name)
CITED = [
    (r"Proposition 2\.4", "Proposition 2.4"),
    (r"Lemma 2\.7", "Lemma 2.7"),
    (r"Table 1\b", "Table 1"),
    (r"Table 2\b", "Table 2"),
    (r"Figure 1\b", "Figure 1"),
    (r"Remark 3\.4", "Remark 3.4"),
    (r"Corollary 1\.3", "Corollary 1.3"),
]
# Sections it names, and the equation it says still stands.
# Anchored to the section TITLE as rendered, not to the bare numeral: "5"
# alone occurs on nearly every page of a 25-page paper, so a bare-numeral
# check passes whatever the PDF contains and is no evidence at all.
# Rendered without a space after the dot in the extracted text.
SECTIONS = [(r"Section 1\.3", "1.3", "1.3.Main results"),
            (r"Section 5\b", "5", "5.Three verifications")]
EQUATIONS = [(r"identity \(17\)", "(17)")]

# Must NOT be found: v1.0's numbering. Without this the check would pass
# against v1.0 too and could not tell the versions apart.
ABSENT = ["Remark 3.3"]

L = []


def say(s=""):
    print(s)
    L.append(s)


def main():
    if not EMAIL.exists():
        say(f"REFUSED: {EMAIL} missing")
        return 2
    etext = EMAIL.read_text(encoding="utf-8", errors="replace")
    if not V12_PDF.exists():
        say(f"REFUSED: {V12_PDF} missing")
        return 2
    got = hashlib.md5(V12_PDF.read_bytes()).hexdigest()
    if got != V12_MD5:
        say(f"REFUSED: reference PDF is not v1.2 (md5 {got})")
        return 2
    try:
        from pypdf import PdfReader
    except ImportError:
        say("REFUSED: pypdf not available; cannot read the rendered text")
        return 2

    pages = PdfReader(str(V12_PDF)).pages
    flat = re.sub(r"\s+", " ",
                  "\n".join(p.extract_text() or "" for p in pages))

    say("=" * 74)
    say("CT-S57 -- the follow-up's objects against v1.2, the version LMP holds")
    say("=" * 74)
    say(f"    reference : v1.2 PDF, md5 {got}, {len(pages)} pages")
    say(f"    email     : {EMAIL.name}, {EMAIL.stat().st_size} bytes")
    say()

    findings = 0

    say("[0] THE CITATION LIST MUST ITSELF BE READABLE OFF THE EMAIL")
    say("    Guards against this script naming an object the email never")
    say("    cites -- an error that would otherwise pass silently.")
    for pat, name in CITED + [(p, n) for p, n, _t in SECTIONS] + EQUATIONS:
        ok = re.search(pat, etext) is not None
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] the email cites {name}")
    say()

    say("[1] EVERY NUMBERED OBJECT THE FOLLOW-UP CITES MUST EXIST IN v1.2")
    for _pat, name in CITED:
        ok = name in flat
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {name}")
    say()

    say("[2] SECTIONS AND EQUATIONS")
    say("    Sections are matched on their rendered TITLE. A bare numeral")
    say("    check would pass against any document and prove nothing.")
    for _pat, s, title in SECTIONS:
        ok = title in flat
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] Section {s} = {title!r}")
    for _pat, e in EQUATIONS:
        ok = e in flat
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] equation {e}")
    say()

    say("[3] DISCRIMINATION -- the v1.0 numbering must be ABSENT")
    for name in ABSENT:
        ok = name not in flat
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {name} does not occur in v1.2")
    say()

    say("[4] CONTROL -- the reader must be able to fail")
    c1 = "Proposition" in flat
    c2 = "Theorem 9.9" not in flat
    c3 = re.search(r"Proposition 9\.9", etext) is None
    c4 = "5.Nonexistent section title" not in flat
    findings += 0 if (c1 and c2 and c3 and c4) else 1
    say(f"    [{'PASS' if c1 else 'FAIL'}] a word known to be present is found")
    say(f"    [{'PASS' if c2 else 'FAIL'}] a fabricated object is absent from "
        "the PDF")
    say(f"    [{'PASS' if c3 else 'FAIL'}] a fabricated object is absent from "
        "the email (step [0] can fail)")
    say(f"    [{'PASS' if c4 else 'FAIL'}] a fabricated section title is "
        "absent (step [2] can fail)")
    say()

    say(f"email sha256 : {hashlib.sha256(EMAIL.read_bytes()).hexdigest()}")
    say()
    if findings:
        say(f"FINDINGS: {findings}")
    else:
        say("CLEAN -- every object the follow-up cites exists in the "
            "manuscript")
        say("the editor is holding, and every object named here is cited by "
            "the email.")
    say("=" * 74)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
