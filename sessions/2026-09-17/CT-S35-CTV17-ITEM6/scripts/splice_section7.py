"""Replace section 7 of NOTICE-v1.7-rev3.md with the CT-S35 three-tier version.

The splice is bounded by two anchors that must each occur exactly once, and the
result is validated as a WHOLE BUFFER before any byte is written: a post-write
check would leave a corrupt notice on disk even when it refuses.
"""

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
NOTICE = SESSION / "NOTICE-v1.7-rev3.md"
NEW = SESSION / "NEW-SECTION-7.md"

START = "## 7. The formal type of the generating-function operator"
END = "\n---\n\n## 8. Open problems as they now stand"


def main():
    raw = NOTICE.read_bytes()
    text = raw.decode("utf-8")

    # Amendment C: assert known-present features, one non-ASCII, before
    # concluding anything about absence.
    assert "# Channel Theory for Polynomial Continued Fractions" in text
    assert "\u03be\u2080" in text, "reader integrity: non-ASCII sentinel absent"
    # Normalise line endings in ONE place, after decoding, so that every
    # anchor and every assertion below sees the same convention.
    crlf = "\r\n" in text
    text = text.replace("\r\n", "\n")
    print("reader integrity: sentinels present in %d bytes, source endings %s"
          % (len(raw), "CRLF (normalised to LF)" if crlf else "LF"))

    assert text.count(START) == 1, "start anchor is not unique"
    assert text.count(END) == 1, "end anchor is not unique"
    i = text.index(START)
    j = text.index(END)
    assert j > i, "the anchors are in the wrong order"
    old = text[i:j]
    print("replacing %d bytes of section 7 (%d subsections)"
          % (len(old), old.count("\n### ")))

    new = NEW.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n")
    assert new.startswith(START), "the replacement does not open with section 7"
    text = text[:i] + new + text[j:]

    # ---- whole-buffer validation, BEFORE writing -------------------------
    # Content assertions are made against a whitespace-flattened view: the
    # notice is hard-wrapped, so a literal multi-word string is as likely to
    # be defeated by a line break as by absence, and a check that cannot tell
    # those apart is not a check.
    flat = re.sub(r"\s+", " ", re.sub(r"(?m)^>[ \t]?", "", text))
    checks = []

    def need(label, cond):
        checks.append((label, bool(cond)))

    need("section 7 heading unique", text.count(START) == 1)
    need("section 8 follows", text.count("## 8. Open problems as they now stand") == 1)
    for n in range(0, 11):
        need("heading %d present once" % n, text.count("\n## %d. " % n) == 1)

    # The four qualifications, in the NOTICE source (the description is checked
    # separately by the gate; this is the earlier of the two chances to fail).
    need("Q4 tier markers in prose", all(
        s in flat for s in ("**This paragraph is Tier 1",
                            "**This paragraph is Tier 2",
                            "**This paragraph is Tier 3")))
    need("Q1 necessary not sufficient", "**necessary, not sufficient**" in flat)
    need("Q1 excludes rows and assigns none",
         "excludes rows and assigns none" in flat)
    need("Q2 no Painlevé label asserted",
         "asserts no Painlev\u00e9 label for `V_quad`" in flat)
    need("Q3 history: D6 inside", "lies **inside** the surviving" in flat)
    need("Q3 history: D5 outside", "lies **outside** the surviving" in flat)
    need("Q3 history not adjudicated", "neither is adjudicated" in flat)
    need("tier 1 exclusion stated for ALL coefficient vectors",
         "for any admissible coefficient vector" in flat)
    need("tier 3 locus named", "a(1) = a(2) = 0` and `b(1) = 0" in flat)
    need("tier 3 contamination disclosed",
         "another process was writing into" in flat)
    need("rank-2 scope stated", "the operator has rank 2" in flat)
    need("folio 2634 quoted", "Katz invariant `r(p)`" in flat)
    need("folio 2635 table quoted", "Classification of Families" in flat)

    bad = [lab for lab, ok in checks if not ok]
    for lab, ok in checks:
        print("  [%s] %s" % ("ok" if ok else "FAIL", lab))
    assert not bad, "pre-write validation failed: %s" % bad

    blob = text.encode("utf-8")
    assert b"\r" not in blob, "a CR reached the buffer destined for disk"
    NOTICE.write_bytes(blob)

    h = hashlib.sha256(NOTICE.read_bytes()).hexdigest()
    print()
    print("written: %s" % NOTICE.name)
    print("  bytes  : %d" % NOTICE.stat().st_size)
    print("  sha256 : %s  (from disk)" % h)
    return 0


if __name__ == "__main__":
    sys.exit(main())
