#!/usr/bin/env python3
"""CT-S58: locate every CT-S56 replacement on a page of the revised PDF.

Exit codes: 0 clean / 1 finding / 2 refusal / 3 crash.

The rule this script obeys, from CT-S56 finding (c): it reports UNLOCATED
rather than a guessed page. A locator that invents an answer is worse than one
that abstains, because the abstention is visible.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
S17 = SESS.parent
S56 = S17 / "CT-S56-REBASE-V12"
REV_PDF = S56 / "revision" / "vquad-periodrep-paper.pdf"
BASE_PDF = S17 / "CT-S55-BASE-VERSION" / "refs" / "zenodo-v1.2-21412469.pdf"
OUT = SESS / "outputs"

EXPECTED_REV_PAGES = 27
# The base is identified by content, not by filename. This whole run is
# meaningless if it compares against the wrong version -- which is exactly the
# defect CT-S55 existed to find.
V12_MD5 = "792107efab6317e8ae21e2ca20f092ff"


def die(msg, code=2):
    print(f"REFUSED: {msg}")
    sys.exit(code)


def norm(s: str) -> str:
    """One normalisation applied to BOTH sides of every comparison.

    The first run of this locator stripped punctuation from the anchor but not
    from the PDF text, so an anchor ending 'it Lemma' could not match the
    rendered 'it (Lemma 2.7)'. Twenty-seven 'UNLOCATED' verdicts were artefacts
    of comparing two differently-normalised strings. Both sides now go through
    here and nowhere else.
    """
    s = s.lower()
    s = re.sub(r"([a-z])- ([a-z])", r"\1\2", s)   # end-of-line hyphenation
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def pages(pdf: Path):
    """Return list of normalised page texts, 1-based via index+1."""
    doc = fitz.open(pdf)
    out = []
    for p in doc:
        t = p.get_text("text")
        t = (t.replace("\ufb01", "fi").replace("\ufb02", "fl")
              .replace("\ufb00", "ff").replace("\ufb03", "ffi")
              .replace("\ufb04", "ffl"))
        out.append(norm(t))
    doc.close()
    return out


# ---------------------------------------------------------------- anchors
# An anchor is a run of plain words that survives LaTeX rendering unchanged:
# no backslash macro, no math, no braces. We take the LONGEST such run in the
# replacement's new text, because short runs collide across pages.
TOKEN_OK = re.compile(r"^[A-Za-z][A-Za-z'\-]*$")


def plain_runs(tex: str):
    """Split LaTeX into runs of renderable plain words."""
    s = tex
    s = re.sub(r"\\[a-zA-Z]+\*?", " \x00 ", s)      # macros
    s = re.sub(r"\$[^$]*\$", " \x00 ", s)            # inline math
    s = s.replace("\\\\", " \x00 ")
    for ch in "{}[]$&%#^_~":
        s = s.replace(ch, " \x00 ")
    s = re.sub(r"\s+", " ", s)
    runs, cur = [], []
    for tok in s.split(" "):
        if tok == "\x00" or not tok:
            if cur:
                runs.append(cur)
            cur = []
            continue
        core = tok.strip(".,;:!?()")
        if TOKEN_OK.match(core):
            cur.append(core)
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs


def anchor_candidates(new_tex: str, min_words=3):
    """All contiguous word-windows of the renderable plain runs, longest first.

    Picking the *longest* run is the wrong criterion: a long run fails whenever
    the rendered text interrupts it (a \\ref, a footnote mark, a line-broken
    math atom), and a short run matches in three places. The criterion that
    matters is uniqueness, so we generate candidates and let the document
    choose.
    """
    seen, cands = set(), []
    for run in plain_runs(new_tex):
        n = len(run)
        for ln in range(n, min_words - 1, -1):
            for st in range(0, n - ln + 1):
                w = " ".join(run[st:st + ln])
                if w not in seen:
                    seen.add(w)
                    cands.append(w)
    cands.sort(key=lambda s: -len(s.split()))
    return cands


def best_anchor(new_tex: str, doc: str, spans):
    """Longest candidate that resolves to exactly one page. Never guesses."""
    for mw in (3, 2):
        cands = anchor_candidates(new_tex, min_words=mw)
        if not cands:
            continue
        ambig = None
        for c in cands[:6000]:
            pr, _ = locate(c, doc, spans)
            if len(pr) == 1:
                return c, pr, ("OK" if mw == 3 else "OK-SHORT"), (
                    "" if mw == 3 else
                    "no 3-word run available; located on a unique 2-word run")
            if len(pr) > 1 and ambig is None:
                ambig = (c, pr)
        if mw == 2:
            if ambig:
                return ambig[0], ambig[1], "AMBIG", (
                    f"no candidate is unique; best matches {len(ambig[1])} pages")
            k, n = longest_found_prefix(cands[0], doc)
            return cands[0], [], "UNLOCATED", (
                f"reader sees {k}/{n} leading words of the longest candidate")
    return None, [], "NO-ANCHOR", "no renderable plain-word run of >=2 words"


def doc_index(pdf: Path):
    """Flattened whole-document text plus an offset -> page map.

    Page-level search cannot find an anchor that straddles a page break, and a
    straddling anchor is not an absent anchor. Searching the document and
    mapping the hit offset back to a page distinguishes the two.
    """
    pgs = pages(pdf)
    buf, spans = [], []
    pos = 0
    for i, t in enumerate(pgs):
        buf.append(t)
        spans.append((pos, pos + len(t), i + 1))
        pos += len(t) + 1
    return " ".join(buf), spans, pgs


def dehyphen(s: str):
    """Undo LaTeX end-of-line hyphenation surviving as 'indepen- dence'."""
    return re.sub(r"([a-z])- ([a-z])", r"\1\2", s)


def page_of(off, spans):
    for a, b, p in spans:
        if a <= off < b:
            return p
    return spans[-1][2]


def locate(anchor: str, doc: str, spans):
    """Return (pages, mode) where mode records which normalisation matched."""
    a = norm(anchor)
    hits = [m.start() for m in re.finditer(re.escape(a), doc)]
    if hits:
        return sorted({page_of(o, spans) for o in hits}), "exact"
    return [], "none"


def longest_found_prefix(anchor: str, doc: str):
    """Diagnostic: how much of the anchor the reader CAN see.

    This is what separates 'the text is not there' from 'my anchor is too
    brittle to match text that is there'.
    """
    words = norm(anchor).split()
    best = 0
    for k in range(1, len(words) + 1):
        if " ".join(words[:k]) in doc:
            best = k
        else:
            break
    return best, len(words)


def find_pages(anchor: str, pgs):
    """Pages (1-based) whose normalised text contains the anchor."""
    a = norm(anchor)
    return [i + 1 for i, t in enumerate(pgs) if a in t]


# ---------------------------------------------------------------- main
def main():
    for p in (REV_PDF, BASE_PDF):
        if not p.exists():
            die(f"required PDF missing: {p}")

    got = hashlib.md5(BASE_PDF.read_bytes()).hexdigest()
    if got != V12_MD5:
        die(f"base PDF {BASE_PDF.name} has md5 {got}, not v1.2's {V12_MD5}; "
            "refusing to compare the revision against an unidentified base")

    rev = pages(REV_PDF)
    base = pages(BASE_PDF)
    rev_doc, rev_spans, _ = doc_index(REV_PDF)
    base_doc, base_spans, _ = doc_index(BASE_PDF)

    if len(rev) != EXPECTED_REV_PAGES:
        die(f"revised PDF has {len(rev)} pages, CT-S56 recorded "
            f"{EXPECTED_REV_PAGES}; refusing to report page numbers")

    # ---- F3 positive control: the reader can see both documents
    if not find_pages("Kovacic", rev) or not find_pages("Kovacic", base):
        die("F3 positive control failed: 'Kovacic' not found in one or both "
            "PDFs; text extraction is broken and every page number is void")

    # ---- F2 discrimination control
    GONE = "three structurally independent"
    in_rev = find_pages(GONE, rev)
    in_base = find_pages(GONE, base)
    if not in_base:
        die(f"F2 control failed: {GONE!r} absent from the v1.2 PDF too, so "
            "'absent from the revision' proves nothing about the revision")
    if in_rev:
        print(f"[FINDING] F2: {GONE!r} still present in the revision on "
              f"pages {in_rev}; item 5 did not remove it everywhere")
        f2_ok = False
    else:
        f2_ok = True

    sys.path.insert(0, str(S56 / "scripts"))
    import apply_revision_v12 as A
    reps = A.all_replacements()

    rows, unlocated, moved = [], 0, 0
    for idx, t in enumerate(reps):
        item, tag, old, new = t[0], t[1], t[2], t[3]
        anc, pr, status, diag = best_anchor(new, rev_doc, rev_spans)
        pb = locate(anc, base_doc, base_spans)[0] if anc else []
        if pr != pb:
            moved += 1
        if status not in ("OK", "OK-SHORT"):
            unlocated += 1
        rows.append((idx, item, tag, anc, pr, pb, status, diag))

    # ---- float cross-check: a check that can fail.
    # Edits 14 and 30 are inside a float (the figure, and Table 2's body). Each
    # has a sibling edit in the same float whose anchor is a full sentence. If
    # the short anchor and its sibling disagree on the page, the short anchor
    # found the wrong occurrence and its page number must not be reported.
    FLOAT_PAIRS = {
        14: (15, "figure node label vs the same figure's caption"),
        30: (31, "Table 2 body row vs the same table's caption"),
    }
    float_ok = True
    float_notes = []
    for a, (b, why) in FLOAT_PAIRS.items():
        if a >= len(rows) or b >= len(rows):
            continue
        pa, pb_ = rows[a][4], rows[b][4]
        if not pa or len(pb_) != 1:
            float_notes.append(f"  [skip] edit {a} or {b} unresolved ({why})")
            continue
        sib = pb_[0]
        if sib in pa:
            # The short anchor's candidate set contains the float's page, so
            # the edit is on that page: both are in the same float and a float
            # is typeset whole. This RESOLVES the ambiguity; it does not
            # excuse it, so the provenance is recorded in the row.
            r = list(rows[a])
            was = ",".join(map(str, pa))
            r[4] = [sib]
            r[6] = "BY-FLOAT"
            r[7] = (f"short anchor matched pages {was}; resolved to p{sib} "
                    f"because edit {b} ({why}) is in the same float")
            rows[a] = tuple(r)
            if len(pa) > 1:
                unlocated -= 1
            float_notes.append(f"  [ok] edit {a} resolved to p{sib} from "
                               f"candidates {was} ({why})")
        else:
            float_ok = False
            float_notes.append(f"  [FIRED] edit {a} matches pages "
                               f"{','.join(map(str, pa))}, none of which is "
                               f"its float sibling {b}'s page p{sib} ({why})")

    # ---- vacuity pre-check: the instrument must distinguish the two PDFs
    if moved == 0:
        die("VACUITY: every anchor resolved identically in v1.2 and the "
            "revision; the locator is not sensitive to the edits it locates")

    lines = []
    W = "=" * 78
    lines.append(W)
    lines.append("CT-S58 READ LOCATOR -- CT-S56 replacements in the revised PDF")
    lines.append(W)
    lines.append(f"revised PDF : {REV_PDF}  ({len(rev)} pages)")
    lines.append(f"v1.2 PDF    : {BASE_PDF}  ({len(base)} pages)")
    lines.append("")
    lines.append(f"controls: F3 positive PASS; F2 discrimination "
                 f"{'PASS' if f2_ok else 'FIRED'} "
                 f"(present in v1.2 p{in_base}, absent from revision)")
    lines.append(f"vacuity : {moved}/{len(reps)} anchors resolve to a "
                 f"different page-set in the revision than in v1.2")
    lines.append("float cross-check (short anchors vs their float siblings):")
    lines.extend(float_notes)
    lines.append("")
    lines.append(f"{'#':>3} {'ITEM':<5} {'REV p':<7} {'v1.2 p':<8} "
                 f"{'STATUS':<10} TAG")
    lines.append("-" * 78)
    for idx, item, tag, anc, pr, pb, status, diag in rows:
        pr_s = ",".join(map(str, pr)) or "-"
        pb_s = ",".join(map(str, pb)) or "-"
        lines.append(f"{idx:>3} {str(item):<5} {pr_s:<7} {pb_s:<8} "
                     f"{status:<10} {tag}")
        if diag:
            lines.append(f"{'':>3} {'':<5} {'':<7} {'':<8} {'':<10} "
                         f"^ {diag}")
            lines.append(f"{'':>3} {'':<5} {'':<7} {'':<8} {'':<10} "
                         f"^ anchor: {(anc or '(none)')[:90]}")
    lines.append("-" * 78)
    lines.append(f"located on exactly one page: {len(reps)-unlocated}/{len(reps)}")
    lines.append("")

    # ---- reading order: group by page
    by_page = {}
    for idx, item, tag, anc, pr, pb, status, diag in rows:
        for p in pr:
            by_page.setdefault(p, []).append((item, tag))
    lines.append(W)
    lines.append("READ ORDER -- pages of the revision carrying changed text")
    lines.append(W)
    for p in sorted(by_page):
        items = sorted({str(i) for i, _ in by_page[p]})
        lines.append(f"  p{p:<3} items {','.join(items):<12} "
                     f"{len(by_page[p])} edit(s)")
        for item, tag in by_page[p]:
            lines.append(f"        [{item}] {tag}")
    lines.append(W)

    txt = "\n".join(lines) + "\n"
    OUT.mkdir(exist_ok=True)
    (OUT / "locate_revision.out.txt").write_text(txt, encoding="utf-8")
    (OUT / "locate_revision.json").write_text(json.dumps(
        [{"idx": r[0], "item": str(r[1]), "tag": r[2], "anchor": r[3],
          "rev_pages": r[4], "base_pages": r[5], "status": r[6],
          "diagnostic": r[7]}
         for r in rows], indent=1), encoding="utf-8")
    print(txt)
    h = hashlib.sha256((OUT / "locate_revision.out.txt").read_bytes()).hexdigest()
    print(f"output sha256 {h}")

    if unlocated:
        print(f"\n[FINDING] F1: {unlocated} replacement(s) not located on "
              f"exactly one page")
        return 1
    if not f2_ok or not float_ok:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
