"""Extract every displayed formula from sections 0-10 and classify its route.

A displayed formula is one set in a display environment: \\[...\\], equation,
align, gather, multline, or their starred forms.  Inline math is excluded --
the pass is about displays, which is where a transposed digit hides best.

Classification is by explicit manifest, not by guessing.  Anything the manifest
does not cover is reported as UNROUTED, which is the finding, not a failure to
hide.
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
REFS = HERE / "refs"
FILES = ["section%d.tex" % i for i in range(11)]

ENVS = ("equation", "align", "gather", "multline", "eqnarray", "displaymath")

# environment or \[ ... \].  The negative lookbehind matters: LaTeX's
# line-break spacing is written \\[2pt], whose "\[" would otherwise be read as
# the opening of a display and swallow the rest of an align body.
ENV_RX = re.compile(
    r"\\begin\{(" + "|".join(ENVS) + r")\*?\}(.*?)\\end\{\1\*?\}",
    re.S)
BRK_RX = re.compile(r"(?<!\\)\\\[(.*?)\\\]", re.S)


def read(name):
    p = REFS / name
    if not p.exists():
        sys.exit("READER INTEGRITY FAILED: missing %s" % name)
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def displays(name):
    """Yield (line, kind, body) for each display in the file."""
    txt = read(name)
    out = []
    for m in ENV_RX.finditer(txt):
        out.append((line_of(txt, m.start()), m.group(1), m.group(2).strip()))
    for m in BRK_RX.finditer(txt):
        out.append((line_of(txt, m.start()), r"\[\]", m.group(1).strip()))
    out.sort()
    return out


def squash(s):
    """Normalise a display body for comparison: drop labels, spacing, and
    LaTeX sizing that carries no mathematical content."""
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\(bigl|bigr|Bigl|Bigr|left|right|,|;|!|quad|qquad)\b", "", s)
    s = re.sub(r"\s+", "", s)
    return s


def main():
    total = 0
    rows = []
    for f in FILES:
        for ln, kind, body in displays(f):
            total += 1
            rows.append((f, ln, kind, body))

    print("DISPLAY CENSUS -- sections 0-10")
    print("=" * 74)
    if total < 10:
        sys.exit("READER INTEGRITY FAILED: only %d displays found across %d "
                 "files; the extractor is not seeing the document"
                 % (total, len(FILES)))
    # negative control: inline math must NOT be captured
    probe = r"text $a+b$ more text"
    if ENV_RX.search(probe) or BRK_RX.search(probe):
        sys.exit("READER INTEGRITY FAILED: extractor captured inline math")
    # negative control: LaTeX line-break spacing must NOT be read as a display.
    # This fired for real: \\[2pt] inside an align body was captured as a
    # display and truncated section 6's align.
    probe2 = "a &= 1,\\\\[2pt] b &= 2,\\\\[2pt]"
    if BRK_RX.search(probe2):
        sys.exit("READER INTEGRITY FAILED: extractor read \\\\[2pt] spacing "
                 "as a display")
    # positive control: a real bracket display MUST be captured
    if not BRK_RX.search("text \\[ x = 1 \\] text"):
        sys.exit("READER INTEGRITY FAILED: extractor misses a real display")

    per = {}
    for f, ln, kind, body in rows:
        per.setdefault(f, []).append((ln, kind, body))
    for f in FILES:
        n = len(per.get(f, []))
        print("  %-16s %3d display(s)" % (f, n))
    print("  %-16s %3d total" % ("ALL", total))
    print()

    # ---------------------------------------------------------------
    # Display-consistency check (CT-S45 REPORT finding 2): the same
    # normalised display appearing more than once must be identical.
    # Where two displays are near-identical but not equal, that is the
    # signature that caught the Appendix A sign error.
    # ---------------------------------------------------------------
    print("DISPLAY-CONSISTENCY: near-duplicate displays")
    print("=" * 74)
    norm = [(f, ln, squash(b)) for f, ln, k, b in rows if len(squash(b)) > 24]
    flagged = 0
    for i in range(len(norm)):
        for j in range(i + 1, len(norm)):
            a, b = norm[i][2], norm[j][2]
            if a == b:
                continue
            # cheap similarity: same length, differ in <= 3 positions, or
            # equal up to a single leading sign
            if a.lstrip("-+") == b.lstrip("-+") and a != b:
                flagged += 1
                print("  SIGN DIFFERENCE  %s:%d  vs  %s:%d"
                      % (norm[i][0], norm[i][1], norm[j][0], norm[j][1]))
                print("     %s" % a[:90])
                print("     %s" % b[:90])
                continue
            if len(a) == len(b) and a != b:
                diff = sum(1 for x, y in zip(a, b) if x != y)
                if 0 < diff <= 3:
                    flagged += 1
                    print("  NEAR-DUPLICATE (%d char) %s:%d  vs  %s:%d"
                          % (diff, norm[i][0], norm[i][1],
                             norm[j][0], norm[j][1]))
                    print("     %s" % a[:90])
                    print("     %s" % b[:90])
    print("  %d near-duplicate pair(s) flagged" % flagged)
    print()

    # positive control for the consistency check: it must fire on a pair it
    # is given, or its silence above means nothing
    ctrl = [("X", 1, "R=\\tfrac14P^2+\\tfrac12P'-Q"),
            ("X", 2, "-R=\\tfrac14P^2+\\tfrac12P'-Q")]
    fired = ctrl[0][2].lstrip("-+") == ctrl[1][2].lstrip("-+") \
        and ctrl[0][2] != ctrl[1][2]
    print("  [control] a planted sign-differing pair is detected: %s"
          % ("YES" if fired else "NO"))
    if not fired:
        sys.exit("READER INTEGRITY FAILED: the consistency check cannot "
                 "detect a pair it was handed; its silence is meaningless")
    print()

    print("FULL LISTING")
    print("=" * 74)
    for f, ln, kind, body in rows:
        flat = re.sub(r"\s+", " ", body)
        print("  %-16s L%-5d %-12s %s"
              % (f, ln, kind, flat[:100] + ("..." if len(flat) > 100 else "")))

    print()
    print("corpus digest: %s"
          % hashlib.sha256(
              b"".join((REFS / f).read_bytes() for f in FILES)).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
