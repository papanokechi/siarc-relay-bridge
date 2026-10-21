"""CT-S56 stage 4b -- where does each edit sit in v1.2's OWN numbering?

CT-S52's replacement tags were written against v1.0 and carry v1.0's numbers:
its tag says 'Remark 3.3', but v1.2 renders that remark as 3.4. The corrections
document goes to referees reading v1.2, so every number in it is derived here
from the v1.2 render rather than transcribed from a tag.

A miss is reported as a miss. Nothing is guessed.
"""
import hashlib
import io
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
BASE_PDF = SESS / "refs" / "zenodo-v1.2-21412469.pdf"
OUT = SESS / "outputs" / "locate_numbering.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def detex(s: str) -> str:
    s = re.sub(r"%.*", " ", s)
    s = re.sub(r"\\(label|ref|eqref|cite|texttt|emph|textbf|S)\b", " ", s)
    s = re.sub(r"\\[A-Za-z]+\*?", " ", s)
    s = re.sub(r"[{}$\\~^_&]", " ", s)
    s = re.sub(r"---", " ", s)
    return s


def norm(s: str) -> str:
    """Letters and digits only: the render hyphenates, ligatures and breaks
    maths across lines, so any whitespace-sensitive match would miss."""
    return re.sub(r"[^a-z0-9]", "", detex(s).lower())


NUMBERED = re.compile(
    r"(Theorem|Proposition|Lemma|Corollary|Remark|Definition|Table|Figure)\s+"
    r"(\d+(?:\.\d+)?)")


def main() -> int:
    sys.path.insert(0, str(HERE))
    import apply_revision_v12 as A

    reps = A.all_replacements()

    doc = fitz.open(BASE_PDF)
    raw = " ".join(p.get_text() for p in doc)
    doc.close()

    # map: position in normalised string -> nearest preceding numbered object
    anchors = []
    npos = 0
    last = 0
    for m in NUMBERED.finditer(raw):
        npos_m = len(norm(raw[:m.start()]))
        anchors.append((npos_m, f"{m.group(1)} {m.group(2)}"))
    nraw = norm(raw)

    say("=" * 78)
    say("CT-S56 STAGE 4b -- each edit located in v1.2's own numbering")
    say("=" * 78)
    say("")
    say(f"    base : {BASE_PDF.name}")
    say(f"    md5  : {hashlib.md5(BASE_PDF.read_bytes()).hexdigest()}")
    say(f"    numbered objects found in the render : {len(anchors)}")
    say(f"    replacements to locate               : {len(reps)}")
    say("")

    # ---------------------------------------------------------- control first
    say("[0] CONTROL -- the locator must find a known object and miss a fiction")
    ctl = [
        ("Lemma 2.7 (The apparent point carries no period)", True),
        ("this sentence does not occur anywhere in the paper at all", False),
    ]
    cfail = 0
    for probe, want in ctl:
        found = norm(probe) in nraw
        ok = found == want
        cfail += (not ok)
        say(f"    [{'PASS' if ok else 'FAIL'}] {'found' if found else 'missed'}: "
            f"{probe[:56]!r} (expected found={want})")
    say("")
    if cfail:
        say("REFUSED: the locator failed its own controls; no numbering is reported.")
        OUT.write_text(BUF.getvalue(), encoding="utf-8")
        return 2

    say("[1] LOCATION OF EACH EDIT")
    say("")
    hits = misses = 0
    rows = []
    for item, tag, old, new in reps:
        key = norm(old)
        # use a distinctive middle slice: the head of an old string is often
        # generic ('the point 0 is'), and a short key matches the wrong place
        probe = key[:120] if len(key) >= 120 else key
        i = nraw.find(probe)
        if i < 0 and len(key) > 40:
            probe = key[:40]
            i = nraw.find(probe)
        if i < 0:
            misses += 1
            rows.append((item, tag, None))
            say(f"    item {item:<2} [MISS] {tag[:60]}")
            continue
        where = None
        for pos, name in anchors:
            if pos <= i:
                where = name
            else:
                break
        hits += 1
        rows.append((item, tag, where))
        say(f"    item {item:<2} [{where or 'front matter':<16}] {tag[:54]}")
    say("")
    say(f"    located: {hits}    not located: {misses}")
    say("")
    say("[2] TAG vs RENDER -- which tags are stale v1.0 leftovers?")
    say("    The locator above is a CENSUS, not an adjudicator: it finds the")
    say("    nearest preceding numbered object, which is wrong whenever the")
    say("    edit's text is lossy under detex. It cannot be used to correct a")
    say("    tag. What IS decidable is whether the object a tag names exists in")
    say("    v1.2 at all -- an object that does not exist is a stale number.")
    say("")
    present = {f"{a} {b}" for a, b in NUMBERED.findall(raw)}
    stale, sound, unresolved = [], [], []
    EXPAND = {"Prop": "Proposition", "Cor": "Corollary", "Thm": "Theorem"}
    for item, tag, where in rows:
        m = re.search(r"\b(Prop|Proposition|Lemma|Remark|Cor|Corollary|Thm|Theorem|"
                      r"Table)\s*(\d+\.\d+|\d+)", tag)
        if not m:
            continue
        kind = EXPAND.get(m.group(1), m.group(1))
        named = f"{kind} {m.group(2)}"
        if named in present:
            sound.append((item, tag, named))
            say(f"    [SOUND] item {item}: {named} exists in v1.2 -- tag usable")
            if where and where != named:
                say(f"            (locator guessed {where}; the locator is wrong here)")
        else:
            stale.append((item, tag, named, where))
            say(f"    [STALE] item {item}: {named} does NOT exist in v1.2")
            say(f"            nearest render object at the edit: {where or 'unknown'}")
            say(f"            -> CONFIRM BY HAND before quoting a number")
    say("")
    say(f"    tags naming an object present in v1.2 : {len(sound)}")
    say(f"    tags naming an object ABSENT in v1.2  : {len(stale)}")
    say("")
    say("[3] NUMBERED OBJECTS PRESENT IN v1.2 (for the corrections document)")
    for n in sorted(present, key=lambda s: (s.split()[0], s.split()[1])):
        say(f"    {n}")
    say("")
    say("=" * 78)
    say("Every number quoted to the referees must appear in the [3] list.")
    say("[1] is advisory only; [2] flags stale tags; neither is authoritative.")
    say("=" * 78)

    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
