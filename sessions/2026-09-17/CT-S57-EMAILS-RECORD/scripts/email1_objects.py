"""CT-S57 -- do the objects the FIRST email cites exist in the version LMP holds?

An email citing an object the editor's copy does not contain is the worst class
of defect available here, because the editor cannot check it and the author
cannot see the problem. The email was written against the journal's PDF, so
this is a check that can genuinely fail.

The reference is v1.2's RENDERED text -- record 21412469, md5
792107efab6317e8ae21e2ca20f092ff -- not the LaTeX source, because a \\label is
not what the editor reads.

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
EMAIL = SESS / "email" / "email_as_sent.txt"
OUT = SESS / "outputs" / "email1_objects.out.txt"

# Every numbered object the first email names, read off its text by hand.
CITED = [
    "Theorem 1.1",
    "Theorem 1.2",
    "Corollary 1.3",
    "Corollary 1.4",
    "Proposition 2.4",
    "Lemma 2.7",
    "Table 1",
    "Remark 3.4",
]
# Sections it names. Rendered as headings, so matched separately.
SECTIONS = ["1.1", "1.2", "7.1"]

# Must NOT be found: the v1.0 numbering CT-S52's tags carried. If this is
# present the check cannot discriminate v1.2 from v1.0 and says nothing.
ABSENT = ["Remark 3.3"]

L = []


def say(s=""):
    print(s)
    L.append(s)


def main():
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

    text = "\n".join(p.extract_text() or "" for p in PdfReader(str(V12_PDF)).pages)
    flat = re.sub(r"\s+", " ", text)

    say("=" * 74)
    say("CT-S57 -- the first email's objects against v1.2, the version LMP holds")
    say("=" * 74)
    say(f"    reference : v1.2 PDF, md5 {got}")
    say(f"    pages     : {len(PdfReader(str(V12_PDF)).pages)}")
    say()

    findings = 0

    say("[1] EVERY NUMBERED OBJECT THE EMAIL CITES MUST EXIST")
    for name in CITED:
        ok = name in flat
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {name}")
    say()

    say("[2] EVERY SECTION THE EMAIL NAMES MUST EXIST")
    for s in SECTIONS:
        ok = re.search(rf"\b{re.escape(s)}\b", flat) is not None
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] Section {s}")
    say()

    say("[3] DISCRIMINATION -- the v1.0 numbering must be ABSENT")
    say("    Without this the check would pass against v1.0 too, and could")
    say("    not tell the two versions apart.")
    for name in ABSENT:
        ok = name not in flat
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {name} does not occur in v1.2")
    say()

    say("[4] CONTROL -- the reader must be able to fail")
    c1 = "Proposition" in flat
    c2 = "Theorem 9.9" not in flat
    findings += 0 if (c1 and c2) else 1
    say(f"    [{'PASS' if c1 else 'FAIL'}] a word known to be present is found")
    say(f"    [{'PASS' if c2 else 'FAIL'}] a fabricated object is not found")
    say()

    say(f"email sha256 : {hashlib.sha256(EMAIL.read_bytes()).hexdigest()}")
    say()
    say("CLEAN -- every object the first email cites exists in the manuscript"
        if not findings else f"FINDINGS: {findings}")
    say("the editor is holding." if not findings else "")
    say("=" * 74)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
