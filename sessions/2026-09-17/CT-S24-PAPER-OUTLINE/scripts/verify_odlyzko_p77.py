"""Verify the Odlyzko p. 77 citation against the source PDF, not the session record.

Operator ruling (CT-S24, round 3): the citation
  Odlyzko, *Asymptotic Enumeration Methods*, p. 77
originated in CT-S22-DEPENDENCE-LIT, whose record lives outside the worktree and
whose downloaded PDFs were deleted at close. It must be re-verified from a page
image of the source or dropped in favour of Nemes alone. It must NOT be cited
from the session record alone.

What is being verified (the claim as OUTLINE.md would state it):
  Birkhoff-Trjitzinsky determines the asymptotics up to a multiplicative
  constant, and does not in general supply techniques for determining that
  constant.

Page-offset rule (S16-22): the PDF page index is not the printed page number.
This script locates the printed page number on the page itself and asserts the
offset, rather than trusting index 77.

Controls, all assertions that can fail:
  C1 POSITIVE  both quoted fragments occur on the printed-p.77 page.
  C2 NEGATIVE  a fabricated near-miss fragment occurs nowhere in the document.
               Guards against a normaliser/matcher that matches anything.
  C3 NEGATIVE  the quoted fragments do not occur on a decoy page.
               Guards against a fragment so generic it appears throughout.
  C4 OFFSET    the located page's own printed folio reads 77, and the PDF index
               at which it was found is reported.
  C5 NEGATIVE  a printed folio that does not exist in the document is not
               resolved by the folio locator.
"""

import hashlib
import re
import sys
import unicodedata
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
PDF = SESSION / "refs" / "odlyzko_asymptotic_enum.pdf"
IMG_DIR = SESSION / "refs"

# Expected source identity, fixed before reading (see REPORT.md).
EXPECTED_SHA256 = "d0b58928e580ab355a6a6805846f023d5a89ebffe9fb966048beb28c1da67bff"

TARGET_FOLIO = 77

# The two fragments the citation rests on, as recorded in the CT-S22 record.
FRAGMENTS = [
    "up to a multiplicative constant",
    "does not in general provide any techniques for determining that constant",
]

# C2: fabricated, plausible-sounding, must appear nowhere.
DECOY_FRAGMENT = "provides a closed form for the multiplicative constant in all cases"

# C5: a folio beyond the document.
IMPOSSIBLE_FOLIO = 99999


def norm(s: str) -> str:
    """Whitespace- and ligature-insensitive normalisation.

    Declared up front, not added after a failure: PDF text extraction breaks
    lines mid-sentence and emits ligatures, so a raw substring test would fail
    for reasons unrelated to the claim. C2 and C3 are the arms that prove this
    normalisation has not made the test unfalsifiable.
    """
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("-\n", "")  # de-hyphenate across line breaks
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def find_folio(doc, folio: int):
    """Return PDF indices whose header/footer band carries the printed folio.

    Looks only at the top and bottom 8% of the page, so a folio number is not
    confused with an equation number or a citation in the body text.
    """
    hits = []
    want = str(folio)
    for i in range(doc.page_count):
        page = doc[i]
        h = page.rect.height
        bands = [
            fitz.Rect(0, 0, page.rect.width, h * 0.08),
            fitz.Rect(0, h * 0.92, page.rect.width, h),
        ]
        for band in bands:
            toks = page.get_textbox(band).split()
            if want in toks:
                hits.append(i)
                break
    return hits


def main() -> int:
    out = []

    def say(s=""):
        out.append(s)
        print(s)

    say("=" * 72)
    say("CT-S24 / verify_odlyzko_p77.py")
    say("=" * 72)

    if not PDF.exists():
        say(f"FAIL: source PDF absent: {PDF}")
        return 2

    digest = sha256(PDF)
    say(f"source     : {PDF.name}")
    say(f"bytes      : {PDF.stat().st_size}")
    say(f"sha256     : {digest}")
    if digest != EXPECTED_SHA256:
        say(f"FAIL: sha256 differs from the value fixed before reading")
        say(f"      expected {EXPECTED_SHA256}")
        return 2
    say("sha256 matches the value fixed before reading: OK")
    say()

    doc = fitz.open(PDF)
    say(f"pages      : {doc.page_count}")

    results = {}

    # ---- C4: resolve the printed folio, do not trust the index ----------
    hits = find_folio(doc, TARGET_FOLIO)
    say()
    say(f"[C4] printed folio {TARGET_FOLIO} found at PDF indices: {hits}")
    if len(hits) != 1:
        say(f"[C4] FAIL: expected exactly one page carrying folio {TARGET_FOLIO}")
        results["C4"] = False
        idx = None
    else:
        idx = hits[0]
        offset = idx - TARGET_FOLIO
        say(f"[C4] PDF index {idx} -> printed page {TARGET_FOLIO} (offset {offset:+d})")
        say("[C4] PASS")
        results["C4"] = True

    # ---- C5: an impossible folio must not resolve -----------------------
    bad = find_folio(doc, IMPOSSIBLE_FOLIO)
    say()
    say(f"[C5] impossible folio {IMPOSSIBLE_FOLIO} found at: {bad}")
    results["C5"] = len(bad) == 0
    say("[C5] " + ("PASS" if results["C5"] else "FAIL: locator resolved a folio that cannot exist"))

    if idx is None:
        say()
        say("VERDICT: CANNOT VERIFY (folio unresolved)")
        return 2

    page_text = norm(doc[idx].get_text())

    # ---- C1: the fragments must be on that page -------------------------
    say()
    ok1 = True
    for frag in FRAGMENTS:
        present = norm(frag) in page_text
        say(f"[C1] on printed p.{TARGET_FOLIO}: {present}  <- {frag!r}")
        ok1 = ok1 and present
    results["C1"] = ok1
    say("[C1] " + ("PASS" if ok1 else "FAIL: quoted fragment not on the cited page"))

    # ---- C2: decoy must appear nowhere in the document -------------------
    say()
    whole = norm("\n".join(doc[i].get_text() for i in range(doc.page_count)))
    decoy_present = norm(DECOY_FRAGMENT) in whole
    say(f"[C2] fabricated fragment present anywhere: {decoy_present}")
    say(f"     {DECOY_FRAGMENT!r}")
    results["C2"] = not decoy_present
    say("[C2] " + ("PASS" if results["C2"] else "FAIL: matcher matches fabricated text"))

    # ---- C3: fragments must not be on a decoy page ----------------------
    say()
    decoy_idx = idx + 7
    decoy_text = norm(doc[decoy_idx].get_text())
    any_there = any(norm(f) in decoy_text for f in FRAGMENTS)
    say(f"[C3] fragments present on decoy PDF index {decoy_idx}: {any_there}")
    results["C3"] = not any_there
    say("[C3] " + ("PASS" if results["C3"] else "FAIL: fragments are not specific to the cited page"))

    # ---- page image -----------------------------------------------------
    say()
    img = IMG_DIR / f"odlyzko_p{TARGET_FOLIO}.png"
    pix = doc[idx].get_pixmap(dpi=200)
    pix.save(img)
    say(f"page image : {img.name}  ({img.stat().st_size} bytes, sha256 {sha256(img)})")

    # ---- context for the report ----------------------------------------
    say()
    say("-" * 72)
    say(f"CONTEXT on printed p.{TARGET_FOLIO} (raw extraction, verbatim):")
    say("-" * 72)
    raw = doc[idx].get_text()
    key = "Birkhoff"
    pos = raw.find(key)
    if pos >= 0:
        say(raw[max(0, pos - 700): pos + 1200])
    else:
        say("(no 'Birkhoff' token on this page; printing head of page)")
        say(raw[:1200])

    doc.close()

    say()
    say("=" * 72)
    npass = sum(1 for v in results.values() if v)
    for k in sorted(results):
        say(f"  {k}: {'PASS' if results[k] else 'FAIL'}")
    say(f"CONTROLS: {npass}/{len(results)}")
    verdict = "VERIFIED" if npass == len(results) else "NOT VERIFIED"
    say(f"VERDICT: p.{TARGET_FOLIO} citation {verdict}")
    say("=" * 72)

    Path(sys.argv[1]).write_text("\n".join(out) + "\n", encoding="utf-8") if len(sys.argv) > 1 else None
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
