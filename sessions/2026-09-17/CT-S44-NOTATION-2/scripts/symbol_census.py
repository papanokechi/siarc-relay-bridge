"""Re-measure the deferred notation residue against the assembled paper.

CT-S38's symbol index was built over theorem.tex, section1.tex and OUTLINE.md
only -- sections 2-10 and both appendices did not exist.  Its deferred list is
therefore a measurement of a smaller object than the one now being repaired.
This script re-measures the six residue letters plus r over every file that
paper.tex actually inputs, and reports each occurrence with its context so the
senses can be adjudicated against printed evidence rather than recalled.

Read-only.  Writes nothing.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent

# the files paper.tex inputs, in document order
FILES = (["section%d.tex" % i for i in range(11)]
         + ["appendixA.tex", "appendixB.tex"])

# the deferred residue from CT-S38 REPORT.md L569-570, plus r
LETTERS = ["M", "A", "L", "u", "beta", "r"]

PAT = {
    "M":    r"(?<![A-Za-z\\])M(?![A-Za-z])",
    "A":    r"(?<![A-Za-z\\])A(?![A-Za-z])",
    "L":    r"(?<![A-Za-z\\])L(?![A-Za-z])",
    "u":    r"(?<![A-Za-z\\])u(?![A-Za-z])",
    "beta": r"\\beta(?![A-Za-z])",
    "r":    r"(?<![A-Za-z\\])r(?![A-Za-z])",
}


def read(name, base=None):
    p = (base or HERE) / name
    if not p.exists():
        sys.exit("READER INTEGRITY FAILED: missing %s" % name)
    t = p.read_text(encoding="utf-8", errors="strict")
    # CRLF would silently defeat every line-oriented read below
    return t.replace("\r\n", "\n").replace("\r", "\n")


# A single letter in running prose ("A reader who...") is not an occurrence of
# the symbol.  Blank every non-math character on the line, keeping offsets, so
# line numbers and context stay exact while only math spans are searchable.
MATHENV = re.compile(
    r"\\begin\{(equation\*?|align\*?|gather\*?|alignat\*?|multline\*?)\}"
    r".*?\\end\{\1\}", re.S)
DISPLAY = re.compile(r"\\\[.*?\\\]", re.S)
INLINE = re.compile(r"(?<!\\)\$(?:\\.|[^$\\])*\$", re.S)


def math_mask(text):
    """Return text with every character outside math replaced by a space."""
    keep = bytearray(b" ") * 0
    keep = [" "] * len(text)
    for rx in (MATHENV, DISPLAY, INLINE):
        for m in rx.finditer(text):
            for i in range(m.start(), m.end()):
                keep[i] = text[i]
    # newlines must survive, or every line number collapses to 1
    for i, ch in enumerate(text):
        if ch == "\n":
            keep[i] = "\n"
    return "".join(keep)


def main():
    # The corpus is named explicitly.  This census measures the DEFERRED
    # RESIDUE, which is a property of the paper as it stood BEFORE this pass
    # repaired it; running it against the repaired root measures a different
    # object.  Defaulting silently to one of the two is how a check ends up
    # reporting a number for a corpus nobody asked about.
    which = sys.argv[1] if len(sys.argv) > 1 else "prepass"
    if which not in ("prepass", "repaired"):
        sys.exit("usage: symbol_census.py [prepass|repaired]")
    base = (HERE / "refs") if which == "prepass" else HERE

    texts = {f: read(f, base) for f in FILES}
    masks = {f: math_mask(t) for f, t in texts.items()}

    # reader non-vacuity: the corpus must be large enough to be the paper
    total = sum(len(t) for t in texts.values())
    if total < 100000:
        sys.exit("READER INTEGRITY FAILED: corpus only %d chars" % total)

    # mask non-vacuity, both directions.  An all-space mask reports zero
    # occurrences of everything, which is indistinguishable from a paper that
    # uses none of these letters; an all-text mask is the prose defect the
    # mask exists to remove.
    mchars = sum(len(m.replace(" ", "").replace("\n", "")) for m in masks.values())
    if mchars < 5000:
        sys.exit("READER INTEGRITY FAILED: math mask kept only %d chars" % mchars)
    if mchars > total * 0.8:
        sys.exit("READER INTEGRITY FAILED: math mask kept %d of %d chars"
                 % (mchars, total))
    # positive control: \beta occurs only in math, so the mask must keep it
    if sum(m.count(r"\beta") for m in masks.values()) == 0:
        sys.exit("READER INTEGRITY FAILED: mask lost \\beta entirely")
    # negative control: this prose phrase must NOT survive the mask
    if any("A reader" in m for m in masks.values()):
        sys.exit("READER INTEGRITY FAILED: mask kept running prose")

    # Resolve the corpus POSITIVELY, not by path alone (the S38-07 lesson:
    # a check that names its target by path certifies whatever is at that
    # path).  Each corpus carries a marker the other does not.
    s1 = texts["section1.tex"]
    has_repair = "\\paragraph{Letters that carry more than one meaning.}" in s1
    has_prepass = "the letter $\\rho$ carries two meanings" in s1
    if which == "prepass" and not (has_prepass and not has_repair):
        sys.exit("READER INTEGRITY FAILED: refs/ does not carry the pre-repair "
                 "rho sentence; it is not the pre-pass corpus")
    if which == "repaired" and not (has_repair and not has_prepass):
        sys.exit("READER INTEGRITY FAILED: the session root does not carry the "
                 "repaired section 1; it is not the repaired corpus")

    print("[reader] corpus=%s, %d files, %d chars, %d chars in math (%.1f%%)"
          % (which, len(texts), total, mchars, 100.0 * mchars / total))
    print()

    grand = 0
    for letter in LETTERS:
        rx = re.compile(PAT[letter])
        hits = []
        for f in FILES:
            raw = texts[f].split("\n")
            for ln, mline in enumerate(masks[f].split("\n"), 1):
                n = len(rx.findall(mline))
                if n:
                    hits.append((f, ln, n, raw[ln - 1].strip()))
        grand += sum(h[2] for h in hits)
        print("=" * 72)
        print("%-6s  %d occurrence(s) on %d line(s)"
              % (letter, sum(h[2] for h in hits), len(hits)))
        print("=" * 72)
        for f, ln, n, line in hits:
            print("  %-15s %4d  x%d  %s" % (f, ln, n, line[:104]))
        print()

    print("[total] %d occurrences across %d letters" % (grand, len(LETTERS)))
    if grand == 0:
        sys.exit("READER INTEGRITY FAILED: zero occurrences is not credible")


if __name__ == "__main__":
    main()
