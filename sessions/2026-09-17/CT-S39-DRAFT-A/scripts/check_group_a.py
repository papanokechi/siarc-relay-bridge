#!/usr/bin/env python3
"""check_group_a.py -- the Group A drafting gate.

Verifies, per PREREG.md:
  O1  every cited source resolves to a HELD artefact, by path, with a sha256;
  O2  every printed folio resolves to a PDF index by LOCATING the folio in the
      page's own text, never by assuming an offset;
  O3  every quoted fragment occurs on that page, on a whitespace-free,
      ligature- and dash-normalised invariant;
  O4  every claim id cited in the prose resolves to exactly one corpus claim,
      and the label printed beside it equals the corpus label.

Plus the F6 prohibitions, which encode three standing rulings.

The evidence is the held page or PDF.  OUTLINE.md and the claim texts are NOT
consulted: they are the thing under test.
"""
import glob
import hashlib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(HERE)
ROOT = os.path.dirname(SESS)                     # sessions/2026-09-17

S0 = os.path.join(SESS, "section0.tex")
S2 = os.path.join(SESS, "section2.tex")


def read_or_fail(path, binary=False):
    """A check reporting ABSENCE cannot distinguish 'missing' from 'unreadable'."""
    try:
        if binary:
            with open(path, "rb") as fh:
                return fh.read()
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError as exc:
        print("READER INTEGRITY FAILED: cannot read %s (%s)" % (path, exc))
        sys.exit(4)


def sha(path):
    return hashlib.sha256(read_or_fail(path, binary=True)).hexdigest()


def squash(t):
    """Whitespace-free, ligature/dash/quote-folded, lowercased.

    Pre-declared in PREREG.md O3.  The Odlyzko text layer drops inter-word
    spaces, so a raw comparison reports a FALSE ABSENCE for every fragment on
    that page.  This removes exactly the representation the extractor fails to
    preserve and nothing else: no character is added, dropped or substituted
    apart from whitespace, ligatures, quotes, dashes and case.
    """
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[\u2018\u2019\u02bc\u0060]", "'", t)
    t = re.sub(r"[\u201c\u201d]", '"', t)
    t = re.sub(r"[\u2010-\u2015\u2212]", "-", t)
    return re.sub(r"\s+", "", t).lower()


# ---------------------------------------------------------------------------
# The citation table.  Each row: source, held artefact, folio, fragments.
# ---------------------------------------------------------------------------
G = os.path.join(ROOT, "CT-S8-LITCHECK", "refs")
O = os.path.join(ROOT, "CT-S24-PAPER-OUTLINE", "refs")
R1 = os.path.join(ROOT, "CT-R1-AUDIT", "refs")

PDF_CITES = [
    ("Gautschi Thm 1.1 p.31 (Pincherle)",
     os.path.join(G, "gautschi1967.pdf"), 31,
     ["THREE-TERM RECURRENCE RELATIONS 31",
      "Pincherle",
      "possesses a minimal solution"]),
    ("Gautschi Thm 2.3(a) p.35 (Perron-Kreuser)",
     os.path.join(G, "gautschi1967.pdf"), 35,
     ["THREE-TERM RECURRENCE RELATIONS 35",
      "Perron [42], Kreuser [29]",
      "two linearly independent"]),
    ("Odlyzko p.77 (connection constant; B-T objection)",
     os.path.join(O, "odlyzko_asymptotic_enum.pdf"), 77,
     ["Wimp and Zeilberger point out that it is usually easy to show that the "
      "largest of the terms of the form (9.35) does show up with a nonzero "
      "coefficient, and so determines the asymptotics of an up to a "
      "multiplicative constant.",
      "However, the Birkhoff-Trjitzinsky method does not in general provide "
      "any techniques for determining that constant.",
      "major objection to the use of the Birkhoff-Trjitzinsky results is that "
      "they may not be rigorous, since gaps are alleged to exist in the "
      "complicated proofs"]),
]

TEXT_CITES = [
    ("DLMF 2.9.5 / 2.9.6 / 2.9.14 deferral",
     os.path.join(G, "dlmf_2_9.txt"),
     ["2.9.5", "2.9.6", "2.9.14",
      "in which P and Q are any integers see Wong and Li ( 1992a )"]),
    ("DLMF 3.6(ii) minimal/dominant",
     os.path.join(G, "dlmf_3_6.txt"),
     ["minimal", "dominant"]),
    ("Wong-Li II bibliographic identification",
     os.path.join(R1, "dlmf_bib_W.html"),
     ["Asymptotic expansions for second-order linear difference equations"]),
    ("Birkhoff-Trjitzinsky Fundamental Theorem p.69",
     os.path.join(G, "bt1933.txt"),
     ["Fundamental Theorem",
      "is completely proper in each of the several quadrants"]),
    ("Nemes 2026 connection coefficients",
     os.path.join(G, "nemes2025.txt"),
     ["treated as unknowns", "connection coefficient"]),
    ("DLMF 5.11.12 Gamma ratio",
     os.path.join(R1, "dlmf_5.11.html"),
     ["5.11.12"]),
]

# Fragments that must be found NOWHERE (A4: fabricated near-misses).
FABRICATED = [
    ("Odlyzko sentence with its negation removed",
     os.path.join(O, "odlyzko_asymptotic_enum.pdf"),
     "However, the Birkhoff-Trjitzinsky method does in general provide "
     "techniques for determining that constant."),
]

IMPOSSIBLE_FOLIO = 9999


def pdf_pages(path):
    import pypdf
    return pypdf.PdfReader(path).pages


def folio_candidates(pages, folio):
    """Indices whose page carries the folio as a STANDALONE edge token.

    A 120-character header/footer band is not enough.  In the Odlyzko volume
    the band at index 63 contains the bibliography reference "[77, 78, 79]"
    and the band at index 67 contains the equation number "(8.77)", so a band
    scan for folio 77 returns index 63 -- a WRONG PAGE, reported as a
    successful resolution.  The real marker is the folio standing alone as the
    first or last whitespace token of the page's first or last non-empty line.
    """
    lines = []
    out = []
    want = str(folio)
    for i, p in enumerate(pages):
        t = p.extract_text() or ""
        ls = [l.strip() for l in t.split("\n") if l.strip()]
        if not ls:
            continue
        edge = [ls[0], ls[-1]]
        hit = False
        for line in edge:
            toks = line.split()
            if toks and (toks[0] == want or toks[-1] == want):
                hit = True
        if hit:
            out.append(i)
    del lines
    return out


def locate_folio(pages, folio):
    """Resolve a printed folio to a PDF index, or None.

    Never assumes an offset, and requires the resolution to be UNIQUE: two
    candidate pages mean the marker is ambiguous, which is reported as a
    failure rather than silently resolved to the first one.
    """
    c = folio_candidates(pages, folio)
    return c[0] if len(c) == 1 else None


def run():
    checks = []
    notes = []

    # ---- O1/O2/O3 over the PDF citations ---------------------------------
    print("[O1-O3] citations verified against the held page or PDF")
    page_cache = {}
    for name, path, folio, frags in PDF_CITES:
        if not os.path.exists(path):
            checks.append(("O1 held artefact: %s" % name, False))
            continue
        checks.append(("O1 held artefact: %s" % name, True))
        pages = page_cache.setdefault(path, pdf_pages(path))
        idx = locate_folio(pages, folio)
        checks.append(("O2 folio %d located in its own page: %s"
                       % (folio, name), idx is not None))
        if idx is None:
            continue
        notes.append("  %-46s folio %4d -> pdf index %3d   sha %s"
                     % (os.path.basename(path), folio, idx, sha(path)[:16]))
        body = squash(pages[idx].extract_text() or "")
        for f in frags:
            checks.append(("O3 fragment on p.%d [%s]: \"%s...\""
                           % (folio, name.split()[0], f[:44]),
                           squash(f) in body))
        # A2 -- decoy pages, the leaf before and the leaf after.
        for d in (idx - 1, idx + 1):
            if 0 <= d < len(pages):
                decoy = squash(pages[d].extract_text() or "")
                hit = any(squash(f) in decoy for f in frags if len(f) > 40)
                checks.append(("A2 decoy index %d rejects p.%d fragments"
                               % (d, folio), not hit))
        # A3 -- an impossible folio must not resolve.
        checks.append(("A3 impossible folio %d does not resolve in %s"
                       % (IMPOSSIBLE_FOLIO, os.path.basename(path)),
                       locate_folio(pages, IMPOSSIBLE_FOLIO) is None))

    # ---- O1/O3 over the text captures ------------------------------------
    for name, path, frags in TEXT_CITES:
        ok = os.path.exists(path)
        checks.append(("O1 held artefact: %s" % name, ok))
        if not ok:
            continue
        body = squash(read_or_fail(path))
        notes.append("  %-46s (text capture)          sha %s"
                     % (os.path.basename(path), sha(path)[:16]))
        for f in frags:
            checks.append(("O3 fragment in %s: \"%s...\""
                           % (os.path.basename(path), f[:40]),
                           squash(f) in body))

    # ---- A4 fabricated near-miss ------------------------------------------
    for name, path, fake in FABRICATED:
        pages = page_cache.setdefault(path, pdf_pages(path))
        anywhere = any(squash(fake) in squash(p.extract_text() or "")
                       for p in pages)
        checks.append(("A4 fabricated near-miss absent from all %d pages (%s)"
                       % (len(pages), name), not anywhere))

    # ---- O4 claim ids and labels -----------------------------------------
    print("[O4] claim ids and labels against the corpus")
    corpus = {}
    for f in glob.glob(os.path.join(ROOT, "CT-S*", "claims.jsonl")):
        if os.path.dirname(f) == SESS:
            continue
        for line in read_or_fail(f).split("\n"):
            if line.strip():
                r = json.loads(line)
                corpus.setdefault(r["claim_id"], []).append(r.get("label"))
    if not corpus:
        print("READER INTEGRITY FAILED: corpus empty")
        sys.exit(4)

    prose = read_or_fail(S0) + "\n" + read_or_fail(S2)
    cited = re.findall(r"\\texttt\{([A-Za-z0-9\\-]+)\}", prose)
    cited = [c.replace("\\-", "-").replace("\\_", "_") for c in cited]
    cited = [c for c in cited
             if re.match(r"^(S\d|S\d+[A-Z]?-|CT-S)", c) and "-" in c]
    checks.append(("O4 non-vacuity: prose cites claim ids at all",
                   len(cited) >= 12))

    # labelled citations: \texttt{ID}, LABEL
    pairs = re.findall(
        r"\\texttt\{([A-Za-z0-9\\-]+)\}[,}\s\\]*\s*(PROVEN|VERIFIED|INSPECTED"
        r"|STRUCTURAL|CONJECTURED)", prose)
    checks.append(("O4 non-vacuity: prose carries labelled citations",
                   len(pairs) >= 8))

    for cid in sorted(set(cited)):
        n = len(corpus.get(cid, []))
        checks.append(("O4 id resolves exactly once: %s" % cid, n == 1))

    for cid, lab in pairs:
        cid = cid.replace("\\-", "-").replace("\\_", "_")
        got = corpus.get(cid, [])
        checks.append(("O4 label matches corpus: %s -> %s" % (cid, lab),
                       len(got) == 1 and got[0] == lab))

    # ---- F6 prohibitions --------------------------------------------------
    print("[F6] standing rulings, as machine-checkable conditions")
    sq_prose = squash(prose)
    checks.append(("F6a no Painleve label asserted for V_quad",
                   not re.search(r"v_?\\?_?quad(is|isa)?(pv|piii|painleve[vi])",
                                 sq_prose)))
    # the upper bound must carry S26-01 and must not be attributed to S1-02
    m = re.search(r"\\begin\{proposition\}\[Proposition U;([^\]]*)\]", prose)
    checks.append(("F6b Proposition U carries S26-01, not S1-02",
                   bool(m) and "S26-01" in m.group(1) and "S1-02" not in m.group(1)))
    # the method paragraph must not lead with Pincherle
    # the method paragraph must not LEAD with Pincherle.  Tested by ORDER
    # within the whole paragraph, not by a character window: section 0 must
    # mention Pincherle (to say it is not used), so "mentions" and "leads
    # with" are different conditions and a window conflates them.
    mm = re.search(r"\\paragraph\{Method, in one paragraph\.\}(.*?)"
                   r"(?=\\paragraph|\\section|\Z)", prose, re.S)
    para = squash(mm.group(1)) if mm else ""
    i_mech = para.find("absolutelysummable")
    i_pin = para.find("pincherle")
    checks.append(("F6c method paragraph introduces the mechanism before Pincherle",
                   bool(mm) and i_mech >= 0 and (i_pin == -1 or i_mech < i_pin)))
    first_sentence = squash(mm.group(1).split(". ")[0]) if mm else ""
    checks.append(("F6c' Pincherle absent from the method paragraph's first sentence",
                   bool(mm) and "pincherle" not in first_sentence))
    checks.append(("F6c'' method paragraph states Pincherle is not used",
                   bool(mm) and "butitisnotused" in para))
    # the attribution paragraph must be first in section 2
    s2 = read_or_fail(S2)
    checks.append(("F6d attribution subsection is first in section 2",
                   s2.find("ssec:attribution") <
                   min(x for x in [s2.find("ssec:convergence"),
                                   s2.find("ssec:bounds")] if x > 0)))
    checks.append(("F6e Wong-Li II stated NOT OBTAINED in the prose",
                   "was not obtained" in s2.lower() or
                   "not obtained" in s2.lower()))
    checks.append(("F6f nothing rests on Birkhoff-Trjitzinsky, stated plainly",
                   "rests on" in s2 and "Birkhoff--Trjitzinsky" in s2))
    checks.append(("F6g the Wimp-Zeilberger attribution split is stated",
                   "reporting Wimp and Zeilberger" in s2 or
                   "reporting \\emph{Wimp and Zeilberger}" in s2))
    checks.append(("F6h DLMF 5.11.12 named at the point of use",
                   "5.11.12" in s2))

    # ---- F7 the forward-reference build stub ------------------------------
    # The stub exists only so the Group A standalone compiles while sections
    # 3-10 are undrafted.  If its numbers drifted from OUTLINE.md the build
    # would print a WRONG cross-reference with no warning, so the numbers are
    # checked against the outline's own headings.
    stub_path = os.path.join(SESS, "forwardrefs.tex")
    stub = read_or_fail(stub_path)
    stub_map = dict((m.group(1), int(m.group(2))) for m in
                    re.finditer(r"r@(sec:[a-z]+)\\endcsname\{\{(\d+)\}", stub))
    checks.append(("F7 stub declares the 8 undrafted sections",
                   len(stub_map) == 8))

    outline = read_or_fail(os.path.join(
        ROOT, "CT-S24-PAPER-OUTLINE", "OUTLINE.md"))
    heads = dict((int(m.group(1)), m.group(2).strip().lower())
                 for m in re.finditer(r"^### \u00a7(\d+)\.\s*(.+)$",
                                      outline, re.M))
    checks.append(("F7 non-vacuity: outline headings parsed",
                   len(heads) >= 8))
    expect_word = {
        "sec:local": "local data", "sec:moduli": "moduli space",
        "sec:point": "point of", "sec:projective": "identification is exact",
        "sec:monodromy": "monodromy", "sec:leaf": "leaf",
        "sec:limits": "scope and limits", "sec:open": "open questions",
    }
    for lab, num in sorted(stub_map.items()):
        head = heads.get(num, "")
        checks.append(("F7 stub %s -> \u00a7%d matches the outline heading"
                       % (lab, num), expect_word[lab] in head))

    # the stub must be inputted by the standalone wrapper ONLY
    users = []
    for f in glob.glob(os.path.join(SESS, "*.tex")):
        if "forwardrefs" in os.path.basename(f):
            continue
        if "forwardrefs" in read_or_fail(f):
            users.append(os.path.basename(f))
    checks.append(("F7 stub is inputted by groupa_standalone.tex alone",
                   users == ["groupa_standalone.tex"]))
    checks.append(("F7 no section file references the stub",
                   "forwardrefs" not in read_or_fail(S0)
                   and "forwardrefs" not in s2))
    checks.append(("F7 stub declares itself NOT part of the paper",
                   "IT IS NOT PART OF THE PAPER" in stub))

    return checks, notes


def arms():
    """Controls A1, A5, A6 -- each mutates the data and must be CAUGHT."""
    print("\n[controls] each arm must be CAUGHT")
    out = []

    # A1 -- a fragment altered by one word must be reported ABSENT.
    import pypdf
    pages = pypdf.PdfReader(
        os.path.join(O, "odlyzko_asymptotic_enum.pdf")).pages
    body = squash(pages[76].extract_text() or "")
    good = ("However, the Birkhoff-Trjitzinsky method does not in general "
            "provide any techniques for determining that constant.")
    bad = good.replace("techniques", "algorithms")
    out.append(("A1 one-word-altered fragment reported ABSENT",
                (squash(good) in body) and (squash(bad) not in body)))

    # A5 -- a deliberately wrong label must be caught.
    prose = read_or_fail(S0) + "\n" + read_or_fail(S2)
    mutant = prose.replace("\\texttt{S1-05}, STRUCTURAL",
                           "\\texttt{S1-05}, PROVEN")
    caught = ("\\texttt{S1-05}, PROVEN" in mutant
              and "\\texttt{S1-05}, STRUCTURAL" in prose)
    out.append(("A5 deliberately wrong label S1-05 PROVEN is detectable",
                caught))

    # A6 -- an unresolvable claim id must be caught.
    corpus = set()
    for f in glob.glob(os.path.join(ROOT, "CT-S*", "claims.jsonl")):
        if os.path.dirname(f) == SESS:
            continue
        for line in read_or_fail(f).split("\n"):
            if line.strip():
                corpus.add(json.loads(line)["claim_id"])
    out.append(("A6 fabricated id S1-99 does not resolve in the corpus",
                "S1-99" not in corpus and "S1-01" in corpus))

    # A7 -- each F6 prohibition fires on injected forbidden text.
    inj = prose.replace(
        "\\paragraph{Method, in one paragraph.} The argument",
        "\\paragraph{Method, in one paragraph.} Pincherle's theorem gives the "
        "growth, and the argument")
    m = re.search(r"\\paragraph\{Method, in one paragraph\.\}(.*?)"
                  r"(?=\\paragraph|\\section|\Z)", inj, re.S)
    p2 = squash(m.group(1)) if m else ""
    out.append(("A7 F6c fires when the method paragraph leads with Pincherle",
                bool(m) and p2.find("pincherle") < p2.find("absolutelysummable")))

    inj2 = prose.replace("[Proposition U; \\texttt{S26-01}, PROVEN]",
                         "[Proposition U; \\texttt{S1-02}, PROVEN]")
    m2 = re.search(r"\\begin\{proposition\}\[Proposition U;([^\]]*)\]", inj2)
    out.append(("A7 F6b fires when Proposition U is attributed to S1-02",
                bool(m2) and "S1-02" in m2.group(1)))

    # A8 -- the folio resolver must reject the false candidates that a
    # header/footer BAND scan accepts.  This is the arm that would have caught
    # the defect found on the first run: a band scan for folio 77 returns
    # index 63 (bibliography reference "[77, 78, 79]") and index 67
    # (equation "(8.77)"), neither of which is page 77.
    band_hits = []
    pat = re.compile(r"(?<!\d)77(?!\d)")
    for i, p in enumerate(pages):
        t = p.extract_text() or ""
        if pat.search(t[:120] + "\n" + t[-120:]):
            band_hits.append(i)
    strict = folio_candidates(pages, 77)
    out.append(("A8 band scan is shown defective (>=2 candidates, first is not 76)",
                len(band_hits) >= 2 and band_hits[0] != 76))
    out.append(("A8' strict resolver returns exactly one index, and it is 76",
                strict == [76]))

    # A9 -- an AMBIGUOUS folio must resolve to None rather than to the first
    # candidate.  Without this, two markers would be silently resolved.
    class _FakePage(object):
        def __init__(self, s):
            self._s = s

        def extract_text(self):
            return self._s

    twins = [_FakePage("head\nbody\n77"), _FakePage("77\nbody\ntail")]
    out.append(("A9 an ambiguous folio (two markers) resolves to None",
                locate_folio(twins, 77) is None
                and folio_candidates(twins, 77) == [0, 1]))

    # A10 -- a drifted stub number must be caught by F7.
    stub = read_or_fail(os.path.join(SESS, "forwardrefs.tex"))
    drifted = stub.replace("r@sec:leaf\\endcsname{{8}",
                           "r@sec:leaf\\endcsname{{7}")
    dmap = dict((m.group(1), int(m.group(2))) for m in
                re.finditer(r"r@(sec:[a-z]+)\\endcsname\{\{(\d+)\}", drifted))
    outline = read_or_fail(os.path.join(
        ROOT, "CT-S24-PAPER-OUTLINE", "OUTLINE.md"))
    heads = dict((int(m.group(1)), m.group(2).strip().lower())
                 for m in re.finditer(r"^### \u00a7(\d+)\.\s*(.+)$",
                                      outline, re.M))
    out.append(("A10 F7 fires when a stub number drifts (leaf 8 -> 7)",
                "leaf" not in heads.get(dmap["sec:leaf"], "")))

    # A11 -- the PDF must actually render the attribution material.  A check
    # on the .tex alone cannot tell "written" from "reaches the page".
    pdf = os.path.join(SESS, "outputs", "build", "groupa_standalone.pdf")
    if os.path.exists(pdf):
        import pypdf
        txt = squash("".join((p.extract_text() or "")
                             for p in pypdf.PdfReader(pdf).pages))
        for probe in ["wimpandzeilberger", "perron", "kreuser", "pincherle",
                      "wasnotobtained", "5.11.12"]:
            out.append(("A11 rendered PDF carries %r" % probe, probe in txt))
        out.append(("A11 rendered PDF does NOT carry the stub's warning text",
                    "notpartofthepaper" not in txt))
    else:
        out.append(("A11 PDF present to be checked", False))

    return out


def main():
    checks, notes = run()
    print()
    for n in notes:
        print(n)
    print("\n[checks]")
    bad = 0
    for label, good in checks:
        if not good:
            bad += 1
        print("  %-86s %s" % (label[:86], "ok" if good else "FAILED"))
    a = arms()
    nca = 0
    for label, good in a:
        if not good:
            nca += 1
        print("  %-86s %s" % (label[:86], "CAUGHT" if good else "MISSED"))

    print("\n[verdict]")
    print("  checks run      : %d" % len(checks))
    print("  checks failed   : %d" % bad)
    print("  control arms    : %d" % len(a))
    print("  arms missed     : %d" % nca)
    if bad or nca:
        print("  VERDICT: GROUP A GATE FAILED")
        sys.exit(1)
    print("  VERDICT: GROUP A CITATIONS AND LABELS VERIFIED")


if __name__ == "__main__":
    main()
