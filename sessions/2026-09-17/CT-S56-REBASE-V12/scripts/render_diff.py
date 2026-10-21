#!/usr/bin/env python
r"""CT-S56 Stage 4: rendered diff of the revision against the v1.2 PDF, and
attribution of every rendered change to one of the five items.

The operator's check is that the rendered diff shows ONLY the intended edits.
"Only" is the hard half: it is easy to show the intended changes are present and
much harder to show nothing else moved. So each changed block is attributed to a
replacement, and any block that cannot be attributed is reported as UNEXPLAINED
and makes the stage fail.

Pagination is deliberately ignored: the revision is longer than v1.2, so every
page boundary shifts and a page-indexed diff would report the whole document as
changed. The comparison is therefore made on the continuous text stream.

Exit codes: 0 clean / 1 finding / 2 refusal / 3 crash.
"""
import difflib
import hashlib
import importlib.util
import io
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REFS = SESS / "refs"
OUTD = SESS / "outputs"
OUT = OUTD / "render_diff.out.txt"
ROOT = SESS.parents[2]

BASE_PDF = REFS / "zenodo-v1.2-21412469.pdf"
REV_PDF = SESS / "revision" / "vquad-periodrep-paper.pdf"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


class Refuse(Exception):
    pass


def pdf_words(p: Path):
    doc = fitz.open(p)
    txt = "\n".join(pg.get_text() for pg in doc)
    npages = doc.page_count
    doc.close()
    txt = txt.replace("\u00ad", "")
    # Remove running headers and page footers before diffing. A page break
    # otherwise inserts a dozen unchanged words in the middle of an edited
    # table, which splits one edit into a delete and an insert far enough apart
    # to defeat attribution. Both patterns are CASE-SENSITIVE: the footer is the
    # all-caps running form, so the mixed-case 'Papanokechi' of the
    # bibliography -- including the new item-R entry -- is left in the stream.
    txt = re.sub(r"AN EXPONENTIAL-PERIOD REPRESENTATION OF THE V\s*quad\s*CONSTANT\s*\d*",
                 " ", txt)
    txt = re.sub(r"\d+\s+PAPANOKECHI", " ", txt)
    words = re.findall(r"\S+", txt)
    return words, npages


def detex(s: str) -> str:
    """Crude LaTeX -> comparison tokens. Lossy on purpose: used only to decide
    whether a rendered block overlaps a replacement, never to assert equality."""
    s = re.sub(r"%.*", " ", s)
    s = re.sub(r"\\(label|ref|eqref|cite|texttt|emph|textbf|S)\b", " ", s)
    s = re.sub(r"\\[A-Za-z]+\*?", " ", s)
    s = re.sub(r"[{}$\\~^_&]", " ", s)
    s = re.sub(r"---", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def tokens(s: str):
    return [w for w in re.findall(r"[a-z]{4,}", detex(s))]


RUNHEAD = r"an exponential-period representation of the vquad constant\s*\d*"
FOOTHEAD = r"(?:\d+\s*)?papanokechi"


def reflow_key(s: str) -> str:
    """Normalise away pagination artefacts ONLY.

    Running headers, their page numbers and end-of-line hyphenation are removed;
    digits elsewhere are deliberately KEPT. Stripping all digits would make
    '8.84' and '3.69' compare equal and would report the single most important
    edit of item 5 as mere reflow.
    """
    t = s.lower()
    t = re.sub(RUNHEAD, " ", t)
    t = re.sub(FOOTHEAD, " ", t)
    t = t.replace("\u00ad", "")
    t = re.sub(r"-\s+", "", t)
    t = re.sub(r"\s+", "", t)
    return t


def load_reps():
    """CT-S52's 19 (imported) plus this session's item-5 list (imported from our
    own apply script, so the two can never disagree)."""
    def imp(path, name):
        spec = importlib.util.spec_from_file_location(name, path)
        m = importlib.util.module_from_spec(spec)
        sys.modules[name] = m
        spec.loader.exec_module(m)
        return m

    mine = imp(HERE / "apply_revision_v12.py", "s56_rd")
    # One source of truth: see apply_revision_v12.all_replacements(). This
    # file previously rebuilt the list as s52.R + FIVE, omitting the L455
    # item-4 edit, and still reported CLEAN -- an attributor missing a
    # replacement cannot say so; it can only attribute that change to
    # something else or fail to see it at all.
    reps = [(i, t, o.replace("\r\n", "\n"), n.replace("\r\n", "\n"))
            for i, t, o, n in mine.all_replacements()]
    return reps


def main():
    say("=" * 78)
    say("CT-S56 STAGE 4 -- rendered diff, revision vs the v1.2 PDF LMP holds")
    say("=" * 78)
    say("")

    for p in (BASE_PDF, REV_PDF):
        if not p.exists():
            raise Refuse(f"missing PDF: {p}")

    bw, bp = pdf_words(BASE_PDF)
    rw, rp = pdf_words(REV_PDF)
    # Header/footer stripping must not remove the bibliography's own author
    # entries, which are mixed case. Item R adds one, so if this ever fired the
    # single edit most likely to be hidden would be the new reference.
    nbib = sum(1 for w in rw if "Papanokechi" in w)
    if nbib < 2:
        say(f"REFUSED: header/footer stripping left only {nbib} mixed-case")
        say("'Papanokechi' tokens in the revision stream; the bibliography")
        say("entries, including item R's, may have been stripped.")
        return 2
    say(f"    footer strip control : {nbib} mixed-case 'Papanokechi' bibliography")
    say("                           tokens survive in the revision stream")
    say(f"    base     v1.2 : {bp} pages, {len(bw)} words, "
        f"md5={hashlib.md5(BASE_PDF.read_bytes()).hexdigest()}")
    say(f"    revision      : {rp} pages, {len(rw)} words, "
        f"sha256={hashlib.sha256(REV_PDF.read_bytes()).hexdigest()[:16]}")
    say(f"    net           : {rp-bp:+d} pages, {len(rw)-len(bw):+d} words")
    say("")

    reps = load_reps()
    say(f"    replacements to attribute against: {len(reps)}")
    say("")

    # -------------------------------------------------------- the stream diff
    sm = difflib.SequenceMatcher(None, bw, rw, autojunk=False)
    raw_blocks = [op for op in sm.get_opcodes() if op[0] != "equal"]

    # Merge blocks separated by only a few equal words. A word-level differ
    # splits one edit into several fragments whenever the edited text shares
    # short runs with the original ("of", "T =", ")"), and a fragment too short
    # to contain any 4-letter token scores 0% against every replacement -- which
    # is indistinguishable from a genuinely unexplained change. Merging first
    # makes the block long enough to be decided.
    GAP = 40
    merged = []
    for tag, i1, i2, j1, j2 in raw_blocks:
        if merged and i1 - merged[-1][2] <= GAP and j1 - merged[-1][4] <= GAP:
            p = merged[-1]
            merged[-1] = ("merged", p[1], i2, p[3], j2)
        else:
            merged.append((tag, i1, i2, j1, j2))
    blocks = merged
    say(f"[1] RENDERED CHANGED BLOCKS: {len(raw_blocks)} raw, {len(blocks)} after")
    say(f"    merging fragments separated by <= {GAP} unchanged words")
    say("")

    full = OUTD / "render-diff-v1.2-to-revision.txt"
    with full.open("w", encoding="utf-8") as fh:
        for tag, i1, i2, j1, j2 in blocks:
            fh.write(f"\n=== {tag} base[{i1}:{i2}] rev[{j1}:{j2}]\n")
            fh.write("--- base: " + " ".join(bw[i1:i2]) + "\n")
            fh.write("+++ rev : " + " ".join(rw[j1:j2]) + "\n")
    say(f"    full rendered diff -> {full.name}")
    say("")

    # ------------------------------------------------------------ attribution
    rep_tok = []
    for item, tag, old, new in reps:
        rep_tok.append((item, tag, set(tokens(old)) | set(tokens(new))))

    unexplained = []
    reflow = 0
    say("[2] ATTRIBUTION OF EACH RENDERED BLOCK")
    say("")
    for k, (tag, i1, i2, j1, j2) in enumerate(blocks, 1):
        bseg = " ".join(bw[i1:i2])
        rseg = " ".join(rw[j1:j2])
        shown = (rseg or bseg)[:88]

        # decidable first: did any text actually change, or is this pagination?
        if reflow_key(bseg) == reflow_key(rseg):
            reflow += 1
            say(f"    {k:>2}. [{tag:^7}] REFLOW ONLY (text identical after de-hyphenation")
            say(f"        and header removal; digits preserved)  {shown[:60]}")
            continue

        seg = bseg + " " + rseg
        st = set(tokens(seg))
        best, bestscore = None, 0.0
        for item, rtag, rt in rep_tok:
            if not st:
                continue
            ov = len(st & rt) / max(1, len(st))
            if ov > bestscore:
                best, bestscore = (item, rtag), ov
        if best and bestscore >= 0.30:
            say(f"    {k:>2}. [{tag:^7}] item {best[0]:<2} ({bestscore:.0%})  {best[1][:46]}")
            say(f"        {shown}")
        else:
            unexplained.append((k, tag, shown, bestscore))
            say(f"    {k:>2}. [{tag:^7}] UNEXPLAINED (best overlap {bestscore:.0%})")
            say(f"        base: {bseg[:80]}")
            say(f"        rev : {rseg[:80]}")
    say("")
    say(f"    reflow-only blocks : {reflow}")
    say(f"    attributed blocks  : {len(blocks) - reflow - len(unexplained)}")
    say(f"    unexplained blocks : {len(unexplained)}")
    say("")

    # ------------------------------------------- exact account of Table 1
    # The Table 1 block is symbol-heavy: item 4 changes one cell, while the
    # surrounding rows are unchanged, so token overlap is legitimately ~29%.
    # Lowering the threshold to admit it would be tuning a threshold to an
    # answer. Instead the block is settled exactly: applying item 4's single
    # cell substitution to the base table must reproduce the revision's table
    # character for character.
    say("[2b] EXACT ACCOUNT OF THE TABLE 1 BLOCK")
    OLD_CELL = "0 (apparent)"
    NEW_CELL = "0 (reg. sing., logarithmic; bB holomorphic there)"

    def region(s):
        i = s.find("finite singularities")
        if i < 0:
            return None
        j = s.find("Galois group", i)
        return re.sub(r"\s+", " ", s[i:j]).strip() if j > i else None

    breg, rreg = region(" ".join(bw)), region(" ".join(rw))
    t1_ok = False
    if breg is None or rreg is None:
        say("    [FAIL] could not locate the Table 1 region in both renders")
    else:
        subbed = re.sub(r"\s+", " ", breg.replace(OLD_CELL, NEW_CELL))
        t1_ok = subbed == rreg
        say(f"    base cell present   : {OLD_CELL in breg}")
        say(f"    revision cell present: {NEW_CELL in rreg}")
        say(f"    [{'PASS' if t1_ok else 'FAIL'}] base table + item-4 cell substitution "
            f"== revision table")
        if not t1_ok:
            say(f"      base+sub: {subbed[:150]}")
            say(f"      revision: {rreg[:150]}")
    # control: the substitution must be what makes them equal, not a no-op
    t1_ctl = (breg is not None and rreg is not None
              and re.sub(r"\s+", " ", breg) != rreg)
    say(f"    [{'PASS' if t1_ctl else 'FAIL'}] control: the tables DIFFER without "
        f"the substitution")
    say("")

    accounted = []
    if t1_ok and t1_ctl:
        for u in list(unexplained):
            if "finite singularities" in u[2] or "order / degree" in u[2]:
                accounted.append(u)
                unexplained.remove(u)
                say(f"    block {u[0]} accounted to item 4 by the exact Table 1 test")
        say("")

    # ------------------------------------------------- presence / absence test
    say("[3] EVERY REPLACEMENT'S NEW TEXT MUST BE RENDERED")
    revjoin = " ".join(rw).lower()
    basejoin = " ".join(bw).lower()
    missing = []
    for item, tag, old, new in reps:
        nt = tokens(new)
        if len(nt) < 6:
            say(f"    item {item:<2} [skipped: too few prose tokens] {tag[:50]}")
            continue
        probe = " ".join(nt[:6])
        hit = probe in re.sub(r"[^a-z ]", " ", revjoin)
        # fall back to a token-overlap test for maths-heavy strings
        if not hit:
            hit = len(set(nt) & set(re.findall(r"[a-z]{4,}", revjoin))) / len(set(nt)) > 0.8
        say(f"    item {item:<2} [{'rendered' if hit else 'MISSING':^9}] {tag[:50]}")
        if not hit:
            missing.append((item, tag))
    say("")

    say("[4] KEY SUBSTANTIVE CHECKS")
    checks = [
        ("v1.2 said 'three structurally independent methods'",
         "three structurally independent methods", basejoin, True),
        ("revision must not say it", "three structurally independent methods", revjoin, False),
        ("v1.2 said B 'is independent of the Stokes datum'",
         "independent of the stokes datum", basejoin, True),
        ("revision must not say it", "independent of the stokes datum", revjoin, False),
        ("v1.2 carried 8.84 as Method B's figure in Table 2", "8.84", basejoin, True),
        ("revision reports 3.69 for Method B", "3.69", revjoin, True),
        ("v1.2 said 'completes part (ii)(a)'", "completes part (ii)(a)", basejoin, True),
        ("revision must not", "completes part (ii)(a)", revjoin, False),
        ("v1.2 said 'proved twice'", "proved twice", basejoin, True),
        ("revision must not", "proved twice", revjoin, False),
        ("revision cites the companion's v1.3", "20455089", revjoin, True),
    ]
    failed = 0
    for desc, needle, hay, want in checks:
        got = needle.lower() in re.sub(r"\s+", " ", hay)
        ok = got == want
        if not ok:
            failed += 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {desc}: found={got} expected={want}")
    say("")

    say("[5] CONTROL ON THE REFLOW TEST")
    say("    a reflow test that collapses real edits would hide exactly the")
    say("    change item 5 exists to make, so it is exercised both ways.")
    ctl = [
        ("hyphenation must collapse", "discontinu- ity", "discontinuity", True),
        ("running header must collapse",
         "AN EXPONENTIAL-PERIOD REPRESENTATION OF THE Vquad CONSTANT 7 foo", "foo", True),
        ("page footer must collapse", "24 PAPANOKECHI bar", "bar", True),
        ("a CHANGED FIGURE must NOT collapse",
         "rel. err. = 8.84 10-46", "rel. err. = 3.69 10-46", False),
        ("a changed word must NOT collapse", "independent of", "dependent on", False),
    ]
    cfail = 0
    for desc, a, b, want in ctl:
        got = reflow_key(a) == reflow_key(b)
        ok = got == want
        if not ok:
            cfail += 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {desc}: collapsed={got} expected={want}")
    say("")

    say("=" * 78)
    rc = 0
    if cfail:
        say(f"REFUSED: the reflow test failed {cfail} of its own controls;")
        say("the block classification above cannot be trusted.")
        return 2
    if unexplained:
        say(f"FINDING: {len(unexplained)} rendered block(s) not attributable to an item.")
        rc = 1
    if missing:
        say(f"FINDING: {len(missing)} replacement(s) not visible in the render.")
        rc = 1
    if failed:
        say(f"FINDING: {failed} substantive check(s) failed.")
        rc = 1
    if rc == 0:
        say("STAGE 4 CLEAN -- every rendered change is attributable to items 1-5,")
        say("every replacement is visible in the render, all substantive checks pass.")
    say("=" * 78)
    return rc


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        say("")
        say(f"REFUSED: {e}")
        rc = 2
    except Exception:
        import traceback
        say("")
        say("CRASH:")
        say(traceback.format_exc())
        rc = 3
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    sys.exit(rc)
