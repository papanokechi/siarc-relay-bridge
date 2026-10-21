"""Renumber the notice's sections 7, 8, 9 -> 8, 9, 10 to make room for a new §7.

WHY THIS IS A SCRIPT AND NOT A REGEX PASS
-----------------------------------------
"§9" in this notice denotes THREE different documents' section 9:

  * §9 of THIS notice        -- "Sources held and hashed"      (1 occurrence)
  * §9 of the v1.6 RECORD    -- the falsifier statements        (7 occurrences)
  * §9 of Birkhoff-Trjitzinsky 1933, p. 69 -- normal-solution shape (2)

and "§8" denotes §8 of the v1.4 EBR deposit, not of this notice. A blind
renumber would rewrite references to OTHER PEOPLE'S DOCUMENTS, silently, and
the result would still look well-formed. So every self-reference is listed
here by its exact surrounding text, each rewrite must fire exactly once, and
anything not listed is left untouched by construction.

The three headings are rewritten in DESCENDING order so that 8->9 cannot
collide with the 9->10 that has already happened.
"""

import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
SRC = SESSION / "NOTICE-v1.7-rev2.md"

# Headings, descending so renames cannot collide.
HEADINGS = [
    ("## 9. Sources held and hashed", "## 10. Sources held and hashed"),
    ("## 8. What this notice does not claim", "## 9. What this notice does not claim"),
    ("## 7. Open problems as they now stand", "## 8. Open problems as they now stand"),
]

# Self-references ONLY. Each was read in context and confirmed to point at this
# notice rather than at the v1.6 record, the v1.4 EBR deposit, or BT 1933.
SELF_REFS = [
    ("proved at every `d` (\u00a72), and the type is untouched by that proof (\u00a75, \u00a77).",
     "proved at every `d` (\u00a72), and the type is untouched by that proof (\u00a75, \u00a78).",
     "line 85 -- open-problems cross-ref"),
    ("strength of \u00a72 (\u00a77).",
     "strength of \u00a72 (\u00a78).",
     "line 301 -- open-problems cross-ref"),
    ("the analytic residual is open and is named `op:xi0-singularity-type` (\u00a72, \u00a77).",
     "the analytic residual is open and is named `op:xi0-singularity-type` (\u00a72, \u00a78).",
     "line 736 -- open-problems cross-ref"),
    ("Wong & Zhao \u00a73, which *is* held and hashed (\u00a79). Only a closed form for `K` could",
     "Wong & Zhao \u00a73, which *is* held and hashed (\u00a710). Only a closed form for `K` could",
     "line 361 -- sources-table cross-ref"),
]

# References that MUST SURVIVE UNCHANGED. These are the control: if the script
# ever starts touching them, it has become the blind regex pass it exists to
# avoid.
MUST_NOT_CHANGE = [
    ("by its own \u00a78 scope statement", "v1.4 EBR deposit, not this notice"),
    ("surviving \u00a79 cost estimates marked unverified", "v1.6 record"),
    ("it is in \u00a79 of the v1.6 PDF", "v1.6 record"),
    ("in **\u00a79 of version `10.5281/zenodo.22782807`**", "v1.6 record"),
    ("Fundamental Theorem \u00a79, p. 69", "Birkhoff-Trjitzinsky 1933"),
    ("normal-solution shape, \u00a79 p. 69", "Birkhoff-Trjitzinsky 1933"),
    ("\u00a79 falsifier text therefore unread", "v1.6 record"),
]


def main():
    raw = SRC.read_bytes()
    text = raw.decode("utf-8")

    # Amendment C: assert a known-present feature, one of them non-ASCII,
    # before concluding anything about what is or is not in this file.
    assert "# Channel Theory for Polynomial Continued Fractions" in text
    assert "\u03be\u2080" in text, "reader integrity: non-ASCII sentinel absent, wrong codec?"
    print("reader integrity: ASCII and non-ASCII sentinels present in %d bytes" % len(raw))
    print()

    before_counts = {frag: text.count(frag) for frag, _ in MUST_NOT_CHANGE}

    print("headings (descending, so 8->9 cannot collide with 9->10):")
    for old, new in HEADINGS:
        n = text.count(old)
        assert n == 1, "heading %r occurs %d times, expected 1" % (old, n)
        text = text.replace(old, new)
        print("  %-46s -> %s" % (old, new.split(" ", 1)[1]))
    print()

    print("self-references (each must fire exactly once):")
    for old, new, why in SELF_REFS:
        n = text.count(old)
        assert n == 1, "self-ref %s occurs %d times, expected 1" % (why, n)
        text = text.replace(old, new)
        print("  [ok] %s" % why)
    print()

    print("control -- references to OTHER documents must be untouched:")
    ok = True
    for frag, whose in MUST_NOT_CHANGE:
        after = text.count(frag)
        if after == before_counts[frag] and after > 0:
            print("  [PASS] %-44s (%s) x%d" % (frag[:44], whose, after))
        else:
            print("  [FAIL] %-44s (%s) %d -> %d" % (frag[:44], whose, before_counts[frag], after))
            ok = False
    assert ok, "the renumber touched a reference to another document"
    print()

    # No stale self-reference may survive.
    assert "(\u00a75, \u00a77)" not in text
    assert "(\u00a72, \u00a77)" not in text
    assert "strength of \u00a72 (\u00a77)." not in text
    assert "hashed (\u00a79)" not in text
    print("no stale self-reference to \u00a77 or \u00a79 survives")

    assert "## 7." not in text, "section 7 must be free for the new item"
    for n in (8, 9, 10):
        assert text.count("\n## %d. " % n) == 1, "section %d is not unique" % n

    SRC.write_bytes(text.encode("utf-8"))
    h = hashlib.sha256(SRC.read_bytes()).hexdigest()
    print()
    print("written: %s" % SRC.name)
    print("  bytes  : %d" % SRC.stat().st_size)
    print("  sha256 : %s  (from disk)" % h)
    return 0


if __name__ == "__main__":
    sys.exit(main())
