"""make_description.py -- CT-S27-CTV17-DEPOSIT-PREP

Generates DESCRIPTION-v1.7-rev3.html from the v1.7 notice, in the HOUSE STYLE of the
deposited Channel Theory descriptions.

The house style is not invented here.  It is READ OFF the deposited v1.6
description (refs/zenodo_22782807.json):

  * tags: <p>, <strong>, <em>.  Nothing else -- no headings, no lists, no
    tables, no <code>, no <sub>.
  * non-ASCII: a NAMED HTML4 ENTITY where one exists (&beta; &radic; &minus;
    &mdash; &sect; &hellip; ...), and RAW UTF-8 where none does (the subscripts
    U+2080.., the star U+2605).  v1.6 writes "&xi;<subscript zero>" exactly
    that way.
  * paragraph separator: read from the record, not chosen.

The entity rule is VALIDATED against the deposited text by round-tripping it
(see verify_description.py control E).  If the rule were wrong, the deposited
description would not survive its own round trip.

Markdown that has no house equivalent is converted, never dropped:
  headings   -> <p><strong>...</strong></p>
  bullets    -> <p>&mdash; ...</p>
  numbered   -> <p><strong>(n)</strong> ...</p>
  tables     -> one <p> per row, cells joined by &mdash;, header row bold
  fenced     -> <p> per block, lines joined, marked as a displayed block
  blockquote -> <p><em>...</em></p>
  ---        -> dropped (a rule has no house equivalent and carries no content)
"""

import hashlib
import html.entities
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SESSIONS = os.path.dirname(SESSION)
DRAFT = os.path.join(SESSIONS, "CT-S26-CTV17-DRAFT")
NOTICE = os.path.join(SESSION, "NOTICE-v1.7-rev3.md")
RECORD = os.path.join(DRAFT, "refs", "zenodo_22782807.json")
DST = os.path.join(SESSION, "DESCRIPTION-v1.7-rev3.html")

# Known-present sentinels.  The first is NON-ASCII, per the adopted Amendment C:
# an ASCII-only sentinel set survives a wrong-codec read intact.
SENTINELS = [
    "\u03be\u2080 = d/|\u03b2_d|",                 # xi_0 = d/|beta_d|
    "# Channel Theory for Polynomial Continued Fractions",
    "## 0. Current state",
    "## 6. The Borel material",
    "the v1.6 build, unchanged",
]


def read_notice():
    with open(NOTICE, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    assert "\r" not in text, "CR survived normalisation"
    for s in SENTINELS:
        assert s in text, "known-present sentinel absent, the read is suspect: %r" % s
    assert any(ord(c) > 127 for c in SENTINELS[0]), "sentinel 0 must be non-ASCII"
    return text


def house_separator():
    """Read the paragraph separator off the deposited record."""
    with open(RECORD, encoding="utf-8") as fh:
        desc = json.load(fh)["metadata"]["description"]
    assert "<p>" in desc, "the held description carries no <p>: the read is suspect"
    seps = re.findall(r"</p>(.{0,3}?)<p>", desc, re.DOTALL)
    assert seps, "cannot find a paragraph boundary in the deposited description"
    common = max(set(seps), key=seps.count)
    return common, desc


def to_entities(s):
    """Named HTML4 entity where one exists; raw UTF-8 where none does."""
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
            continue
        name = html.entities.codepoint2name.get(ord(ch))
        out.append("&%s;" % name if name else ch)
    return "".join(out)


def esc(s):
    """Markup-escape first, then entity-encode.  Order matters."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return to_entities(s)


def inline(s):
    """Markdown inline -> <strong>/<em>.  Code spans keep their text, no tag."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s, flags=re.DOTALL)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s,
               flags=re.DOTALL)
    s = s.replace("`", "")
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", s)
    return s


def apply_exclusions(lines):
    """Declared exclusions: corpus-internal material that must not be published.

    Each rule is stated here, applied here, and VERIFIED by
    verify_description.py, which asserts the excluded string is present in the
    notice and absent from the description.  A rule that stopped matching would
    therefore be caught, not silently skipped.

    The draft banner is dropped as a WHOLE PARAGRAPH.  Dropping only the lines
    that match would leave the rest of the paragraph behind as a mangled
    fragment -- a partial exclusion is worse than none.
    """
    kept, dropped = [], []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        if ln.startswith("# "):                       # H1: Zenodo carries the title
            dropped.append(("h1-title", ln))
            i += 1
            continue
        if "**DRAFT ONLY.**" in ln:
            while i < n and lines[i].strip():
                dropped.append(("draft-banner", lines[i]))
                i += 1
            continue
        if ln.startswith("Session: `sessions/"):      # the working folder
            dropped.append(("session-path", ln))
            i += 1
            continue
        if "End of draft v1.7 notice." in ln:
            # The notice's sign-off. It is correct IN THE NOTICE, which is and
            # remains a draft document; it is false in a published description.
            while i < n and lines[i].strip():
                dropped.append(("draft-signoff", lines[i]))
                i += 1
            continue
        kept.append(ln)
        i += 1
    return kept, dropped


# Publication-stage substitutions.  Same discipline as the exclusions above:
# declared here, applied here, verified two-sidedly by verify_description.py
# (the "before" must be present in the notice, the "after" present in the
# description and the "before" absent from it).  These exist because the notice
# is a DRAFT document and describes itself as one, while the description IS the
# publication and cannot.  Nothing here changes a claim, a label or a value.
SUBSTITUTIONS = [
    ("| v1.7 | — | — | this notice, draft |",
     "| v1.7 | — | — | this notice |",
     "the v1.7 row must not call the published notice a draft"),
]


def apply_substitutions(text):
    applied = []
    for before, after, why in SUBSTITUTIONS:
        assert before in text, \
            "substitution %r matched nothing: it has stopped working" % why
        text = text.replace(before, after)
        applied.append((before, after, why))
    return text, applied


# ---------------------------------------------------------------- provenance
# OPERATOR RULING: "anything a reader can resolve stays; anything only you can
# resolve goes.  DOIs resolve.  CT-S22-STOKES/outputs/... does not."
#
# Session ids, refs/ paths and script names are internal provenance: they mean
# nothing without the tree, they promise a record that is not published, and no
# prior version of this record carries them.  What replaces them is the
# BIBLIOGRAPHIC half -- author, title, venue, DOI or URL -- plus the sha256, so
# a reader can confirm they hold the same bytes without needing the tree.
#
# Every identifier below was resolved by scripts/doi_probe_v17.py and printed
# with the RESOLVER'S OWN title.  None is written from memory: this corpus has
# already caught one hallucinated DOI (10.1007/BF02547452, offered for Birkhoff
# 1930, resolves to a 1995 chemistry paper), and that DOI is kept in the probe
# as a poison control.

BIBLIOGRAPHY = [
    ("W. Gautschi, *Computational aspects of three-term recurrence relations*, "
     "**SIAM Review 9**(1) (1967) 24–82",
     "DOI `10.1137/1009002`",
     "Thm 2.3(a) p. 35 (Perron–Kreuser); Thm 1.1 p. 31 (Pincherle). "
     "sha256 `47ed9dffc00a52b7cfb7f3943d7ba3f2a3d398284ec6a00926ced315ec1c5173`"),

    ("**DLMF §3.6** (Linear Difference Equations)",
     "`https://dlmf.nist.gov/3.6`",
     "Pincherle dichotomy. Capture sha256 "
     "`f6e2559307f5ac5fe7f9c909c5c71a95cdd986bd0b843e74843fc1c773a3dc86`"),

    ("**DLMF §2.9** (Difference Equations)",
     "`https://dlmf.nist.gov/2.9`",
     "(2.9.5), (2.9.6) and the (2.9.14) deferral to Wong & Li. Capture sha256 "
     "`72d6a344c2d04dc3564d95212091c40f1258f2369ec5062cc29daa6dc2c44f42`"),

    ("G. D. Birkhoff and W. J. Trjitzinsky, *Analytic theory of singular "
     "difference equations*, **Acta Mathematica 60** (1933) 1–89",
     "DOI `10.1007/bf02398269`",
     "Normal-solution shape, §9 p. 69. Cited for context only; nothing in "
     "this notice rests on it"),

    ("R. Wong and H. Li, *Asymptotic expansions for second-order linear "
     "difference equations, II*, **Stud. Appl. Math. 87**(4) (1992) 289–324",
     "DOI `10.1002/sapm1992874289`",
     "**NOT OBTAINED** — paywalled. The exponent is derived here "
     "independently and does not depend on it"),

    ("R. Wong and Y.-Q. Zhao, *Recent advances in asymptotic analysis*, "
     "**Analysis and Applications 20** (2022) 1103–1146",
     "DOI `10.1142/S0219530522400012`; preprint `arXiv:2204.09305v1`",
     "§3, the turning-point normalisation. Version pin deliberate: the read "
     "was of v1. CC-BY-4.0, 464879 B, sha256 "
     "`123ab322619c723c26f3669b248f3986c731a1969c8265d88ad65d4fddc1a50b`"),

    ("A. M. Odlyzko, *Asymptotic enumeration methods*",
     "`https://www-users.cse.umn.edu/~odlyzko/doc/asymptotic.enum.pdf`",
     "p. 77, the connection-constant statement and its attribution split. "
     "1116716 B, sha256 "
     "`d0b58928e580ab355a6a6805846f023d5a89ebffe9fb966048beb28c1da67bff`; "
     "page image sha256 "
     "`f9843a43d839ea4edb65c003264c73aca5128b39e4114a2bba0f4d8bc384558c`"),

    ("G. Nemes (2026), *Hyperasymptotics for linear difference equations with "
     "an irregular singularity*",
     "`arXiv:2508.15246v2`",
     "Abstract and §1 p. 3, connection coefficients. 618289 B, sha256 "
     "`7f848c5bc15a792559442176477d609a861d9cf78b2f37d158a265c0d5511145`"),

    ("M. van der Put and M.-H. Saito, *Moduli spaces for linear differential "
     "equations and the Painlev\u00e9 equations*, **Ann. Inst. Fourier 59**(7) "
     "(2009) 2611\u20132667",
     "`http://aif.cedram.org/item?id=AIF_2009__59_7_2611_0`",
     "Table 2.1 p. 2635 and the surrounding classification, pp. 2634\u20132637, "
     "read from page images with each folio verified by eye. No DOI is printed "
     "on the article; the identifier above is the one it carries. *Tous droits "
     "r\u00e9serv\u00e9s* \u2014 nothing from it is reproduced in this deposit. "
     "1058380 B, sha256 "
     "`1666bd6be824a99fc0b48adbe48233a9b2a520fd7e8adf187e98d22525473605`"),

    ("A. Ibrahim and B. Salvy, *Positivity certificates for linear recurrences*, "
     "**SODA 2024**, 982–994",
     "DOI `10.1137/1.9781611977912.37`; preprint `arXiv:2306.05930v2`",
     "Quoted only in its weaker printed form. CC-BY-4.0, 720492 B, sha256 "
     "`36e9d025c89b6fa042e99888513f6554a43956eb247f0e25643efec1567be627`"),

    ("Channel Theory **v1.6** record and description (the current published "
     "version)",
     "DOI `10.5281/zenodo.22782807`",
     "Record sha256 "
     "`cacfb91d913eb95385c97a9e1a56898c3ee7225e21c54aec09d97b622528a737`; "
     "description sha256 "
     "`82d51c5375754b0220475a393d517815266cdd7529433b4e2b7a1cbb0bbb596b`"),

    ("Channel Theory **v1.5** record and description",
     "DOI `10.5281/zenodo.22717792`",
     "Record sha256 "
     "`fe6ca2f17f0dbe94db5b3d69f4e0d8c92249e5854381e32e7beb0ba74361df64`; "
     "description sha256 "
     "`0898719bf793867add756a64cbacc2e621588f9a0df91eb24e82905eb6a50c20`"),

    ("Channel Theory **v1.4** record and description (via DataCite)",
     "DOI `10.5281/zenodo.20585624`",
     "Record sha256 "
     "`58ba35aa4bc8a5d58d0e5e67373ca4468f7501ea99d761b49241911f74bf060a`; "
     "description sha256 "
     "`dd37d2a8ce9dcdfa6d9e06f7ff0b98a557d80d5a9e59fd0775f0f7965dfc00ca`"),

    ("Channel Theory **v1.3** record and description (via DataCite)",
     "DOI `10.5281/zenodo.19972394`",
     "Record sha256 "
     "`0c11834472245807b98628e5b260496177ef66763f46e416c8c7396b50685cf7`; "
     "description sha256 "
     "`d278d5fa9cfaf6acf36fc0f98f4d0470c25aab8454db330c357e7c9d2e2e7921`"),

    ("Channel Theory **concept** record (DataCite)",
     "DOI `10.5281/zenodo.19941678`",
     "Current version `1.6`; six `HasVersion` relations. sha256 "
     "`22978f14678ec8f8ca9d58f3e8117ca6a12d083a5ddb7e2ae6a77905ecd1aeb3`"),

    ("Channel Theory **v1.5 and v1.6 PDFs**",
     "—",
     "**NOT HELD** — HTTP 504 on both file endpoints, retried. The §9 "
     "falsifier text is therefore unread and is pointed at, never restated"),
]


def bibliography_markdown():
    rows = ["| Source | Identifier | Note |", "|---|---|---|"]
    for src, ident, note in BIBLIOGRAPHY:
        rows.append("| %s | %s | %s |" % (src, ident, note))
    return "\n".join(rows)


# Ordered rewrites of the sentences that pointed INTO the old table by path.
# Each must fire, so a rule that stops matching fails closed rather than
# silently leaving a path in the published text.
PROVENANCE_RULES = [
    (r"Held and hashed: `CT-S8-LITCHECK/refs/gautschi1967\.pdf`, page image\s*\n"
     r"`CT-S8-LITCHECK/refs/g1967_p35_mid\.png`, `CT-S8-LITCHECK/refs/dlmf_3_6\.txt`\.",
     "Both were read from the sources themselves, including a page image of "
     "p. 35; see the bibliography in \u00a710.",
     "Gautschi and DLMF 3.6 holdings"),

    (r"present in the hashed capture `CT-S8-LITCHECK/refs/dlmf_2_9\.txt`\s*\n"
     r"\(lines 127, 143, 327, 343\)",
     "present in the hashed capture of DLMF \u00a72.9 listed in \u00a710",
     "DLMF 2.9 capture"),

    (r"`CT-R1-AUDIT/refs/wong_zhao_2022_recent_advances_arxiv-2204\.09305\.pdf`,\s*\n"
     r"464879 bytes, sha256 `123ab322619c723c\u2026`, CC-BY-4\.0\.",
     "464879 bytes, CC-BY-4.0; the full sha256 is in \u00a710.",
     "Wong-Zhao holding"),

    (r"intermediate record: `CT-S24-PAPER-OUTLINE/refs/odlyzko_asymptotic_enum\.pdf`\s*\n"
     r"\(sha256 `d0b58928\u2026`\), page image `CT-S24-PAPER-OUTLINE/refs/odlyzko_p77\.png`\s*\n"
     r"\(sha256 `f9843a43\u2026`\), checker\s*\n"
     r"`CT-S24-PAPER-OUTLINE/scripts/verify_odlyzko_p77\.py` at 5/5 controls\s*\n"
     r"\(`S24-12`, VERIFIED\)\.",
     "intermediate record. The PDF and the page image are listed with their "
     "sha256 in \u00a710, and the reading was checked at 5 of 5 controls, three "
     "of them negative.",
     "Odlyzko holding and checker"),

    (r"\(`CT-S8-LITCHECK/refs/nemes2025\.pdf`, INSPECTED\)",
     "(INSPECTED; see \u00a710)",
     "Nemes holding"),

    (r"\(SODA 2024, arXiv:2306\.05930v2, CC-BY-4\.0,\s*\n"
     r"`CT-R1-AUDIT/refs/ibrahim_salvy_2023_positivity_certificates_arxiv-2306\.05930\.pdf`,\s*\n"
     r"sha256 `36e9d025c89b6fa0\u2026`\)",
     "(SODA 2024, arXiv:2306.05930v2, CC-BY-4.0; see \u00a710)",
     "Ibrahim-Salvy holding"),

    (r"statement is in `sessions/2026-05-01/CC-PIPELINE-G2/g2_pade_borel\.py`, lines 5\u201312,\s*\n"
     r"which gives",
     "statement is in the CC-channel pipeline's Pad\u00e9\u2013Borel source, which gives",
     "CC-PIPELINE-G2 path"),

    (r"The explicit halving is at `sessions/2026-05-01/CC-PIPELINE-G/vquad_recovery\.py`,\s*\n"
     r"lines 70\u201379; its own comment",
     "The explicit halving is in the earlier recovery source; its own comment",
     "CC-PIPELINE-G path"),

    (r"recorded at\s*\n"
     r"> `sessions/2026-05-29/T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY`, with the\s*\n"
     r"> superseding disposition in\s*\n"
     r"> `sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/SUPERSEDED_BY_VQ-N1\.json`\.",
     "recorded in the project working record, with an explicit superseding "
     "disposition.",
     "V_quad reclassification paths"),

    (r"fetched on 2026-09-19 and held in `refs/`\*\*", "fetched on 2026-09-19**",
     "erratum-stack provenance"),

    (r"\(Read 2026-09-19 from\s*\n`refs/datacite_concept\.json` and `refs/zenodo_22782807\.json`; the concept DOI is",
     "(Read 2026-09-19 from the concept record and the v1.6 record, both listed "
     "in \u00a710; the concept DOI is",
     "concept and v1.6 record paths"),

    (r"> 2026-09-19 and are held in `refs/` with their bytes and hashes: v1\.5 and v1\.6",
     "> 2026-09-19 with their bytes and hashes recorded in \u00a710: v1.5 and v1.6",
     "deposited-description provenance"),

    (r"v1\.4\u2013v1\.6 comes from the deposited \*\*descriptions\*\*, held in `refs/`\. \*\*No \u00a79",
     "v1.4\u2013v1.6 comes from the deposited **descriptions**, listed in \u00a710. **No \u00a79",
     "closing-caveat provenance"),

    # The AEAL claim-id roster.  No deposited description in this record has
    # ever carried a claim id; they resolve only inside the tree.
    (r"\*AEAL claims cited by this notice:\*[^\n]*(\n[^\n]*)*?`S26-04`\.",
     "*Every numbered claim behind this notice is recorded in the project's "
     "AEAL claim ledger, which is not part of this deposit.*",
     "AEAL claim roster"),
]

# Inline claim ids, removed in order.  The label a citation carries (PROVEN,
# VERIFIED, STRUCTURAL, INSPECTED) is EPISTEMIC CONTENT and is kept; only the
# unresolvable identifier goes.  The residue assertion in main() is what
# actually guarantees this list is complete -- these rules are the attempt, the
# assertion is the proof.
CID = r"`S\d+[A-Z]?-(?:\d\d|\*)`"

CLAIM_ID_RULES = [
    (r"(?m)^\*Claims:\*[^\n]*\n", ""),
    (r"\(" + CID + r"\s*[\u2013-]\s*" + CID + r",\s*", "("),
    (r"\(" + CID + r",\s*", "("),
    (r"\s*\(" + CID + r"(?:,\s*" + CID + r")*\)", ""),
    (r";\s*" + CID + r",\s*", "; "),
    (r"\s*" + CID + r",\s*", " "),
    (r"\s*" + CID, ""),
]


def strip_claim_ids(text):
    total = 0
    for pat, repl in CLAIM_ID_RULES:
        text, n = re.subn(pat, repl, text)
        total += n
    text = re.sub(r"\(\s*,\s*", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r" +([.,;])", r"\1", text)
    return text, total


def strip_internal_provenance(text):
    """Replace the held-artefact table with a bibliography, then reword every
    sentence that pointed into it by path.  Returns the text and a log."""
    log = []

    start = text.find("| Source | Location | Note |")
    assert start != -1, "the sources table is not where it was: rule stopped working"
    end = text.find("\n\n", text.find("V_quad` reclassification", start))
    assert end > start, "could not find the end of the sources table"
    text = text[:start] + bibliography_markdown() + text[end:]
    log.append(("sources-table", "replaced by a %d-row bibliography" % len(BIBLIOGRAPHY)))

    for pat, repl, why in PROVENANCE_RULES:
        new, n = re.subn(pat, repl, text)
        assert n > 0, "provenance rule %r matched nothing: it has stopped working" % why
        text = new
        log.append((why, "%d occurrence(s)" % n))
    text, n_cid = strip_claim_ids(text)
    log.append(("inline claim ids", "%d removed, labels kept" % n_cid))
    return text, log


def lead_paragraph():
    """The opener, in the house shape, with both DOIs read from the record."""
    with open(RECORD, encoding="utf-8") as fh:
        rec = json.load(fh)
    cdoi, vdoi = rec.get("conceptdoi"), rec.get("doi")
    assert cdoi and vdoi and cdoi != vdoi, "concept and version DOI not both present"
    assert rec["metadata"]["version"] == "1.6", "the held record is not v1.6"
    return ("<strong>Version notice (v1.7).</strong> This version corrects and "
            "attributes; it alters no theorem, proposition or numerical value of "
            "v1.6. Concept DOI is preserved (%s); v1.6 (%s) is superseded. It is a "
            "<em>description-only</em> version; the paragraph immediately below "
            "states what that means for the attached file." % (esc(cdoi), esc(vdoi)))


def convert(md):
    paras = []
    md, subs = apply_substitutions(md)
    md, prov = strip_internal_provenance(md)
    lines = md.split("\n")
    lines, dropped = apply_exclusions(lines)
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        if line.startswith("```"):
            block = []
            i += 1
            while i < n and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            body = " ".join(x.strip() for x in block if x.strip())
            if body:
                paras.append("<em>Displayed:</em> " + esc(body))
            continue

        if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            paras.append("<strong>" + inline(m.group(2).strip()) + "</strong>")
            i += 1
            continue

        if line.lstrip().startswith("|") and i + 1 < n and \
                re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            # Each cell is inlined SEPARATELY and only then joined by the
            # entity.  Joining first and inlining after sent the "&" of
            # "&mdash;" through esc(), producing "&amp;mdash;" -- which
            # publishes as the literal text "&mdash;".  That defect stood in
            # 77 places and no check saw it.
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            paras.append("<strong>" + " &mdash; ".join(
                inline(c) for c in head if c) + "</strong>")
            while i < n and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                row = " &mdash; ".join(inline(c) for c in cells if c)
                if row:
                    paras.append(row)
                i += 1
            continue

        m = re.match(r"^\s*>\s?(.*)$", line)
        if m:
            buf = [m.group(1)]
            i += 1
            while i < n and re.match(r"^\s*>", lines[i]):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            body = " ".join(x.strip() for x in buf if x.strip())
            if body:
                paras.append("<em>" + inline(body) + "</em>")
            continue

        m = re.match(r"^\s*([*+-]|\d+\.)\s+(.*)$", line)
        if m:
            marker, first = m.group(1), m.group(2)
            buf = [first]
            i += 1
            while i < n and lines[i].strip() and \
                    not re.match(r"^\s*([*+-]|\d+\.)\s+", lines[i]) and \
                    not lines[i].startswith("#") and \
                    not lines[i].lstrip().startswith("|") and \
                    not lines[i].startswith("```") and \
                    not re.match(r"^\s*>", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            body = " ".join(x.strip() for x in buf if x.strip())
            if marker[0].isdigit():
                paras.append("<strong>(" + marker.rstrip(".") + ")</strong> " +
                             inline(body))
            else:
                paras.append("&mdash; " + inline(body))
            continue

        if not line.strip():
            i += 1
            continue

        buf = [line]
        i += 1
        while i < n and lines[i].strip() and \
                not lines[i].startswith("#") and \
                not lines[i].startswith("```") and \
                not lines[i].lstrip().startswith("|") and \
                not re.match(r"^\s*>", lines[i]) and \
                not re.match(r"^\s*([*+-]|\d+\.)\s+", lines[i]) and \
                not re.match(r"^\s*(-{3,})\s*$", lines[i]):
            buf.append(lines[i])
            i += 1
        body = " ".join(x.strip() for x in buf)
        if body.strip():
            paras.append(inline(body))

    return paras, dropped, subs, prov


def main():
    md = read_notice()
    sep, v16 = house_separator()
    paras, dropped, subs, prov = convert(md)
    paras.insert(0, lead_paragraph())
    doc = sep.join("<p>" + p + "</p>" for p in paras)

    with open(DST, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(doc)

    with open(DST, "rb") as fh:
        back_raw = fh.read()
    back = back_raw.decode("utf-8")
    assert back == doc, "read-back differs from what was written"
    h = hashlib.sha256(back_raw).hexdigest()

    tags = sorted(set(t.lower() for t in re.findall(r"</?([a-zA-Z0-9]+)", back)))
    nonascii = sorted(set(c for c in back if ord(c) > 127))

    print("DESCRIPTION-v1.7-rev3.html written and read back")
    print("  source     : NOTICE-v1.7-rev3.md  (%d bytes)"
          % os.path.getsize(NOTICE))
    print("  paragraphs : %d" % len(paras))
    print("  chars      : %d   (v1.6 deposited description: %d)" % (len(back), len(v16)))
    print("  bytes      : %d" % len(back_raw))
    print("  sha256     : %s   (from disk)" % h)
    print("  separator  : %r  (read from the deposited record, not chosen)" % sep)
    print("  tags       : %s" % ", ".join(tags))
    print("  raw non-ASCII kept (no HTML4 name): %s"
          % " ".join("U+%04X %s" % (ord(c), c) for c in nonascii))
    print()
    import collections
    kinds = collections.Counter(k for k, _ in dropped)
    print("  declared exclusions applied (corpus-internal, not published):")
    for k, cnt in sorted(kinds.items()):
        print("    %-14s %d line(s)" % (k, cnt))
    for k in ("h1-title", "draft-banner", "session-path", "draft-signoff"):
        assert k in kinds, "exclusion rule %r matched nothing: it has stopped working" % k
    print()
    print("  declared publication-stage substitutions:")
    for before, after, why in subs:
        print("    %s" % why)
        print("      before: %s" % before)
        print("      after : %s" % after)
    assert subs, "the substitution list is empty: the rule set has been lost"

    # Amendment C: assert a known-present feature, including a non-ASCII one,
    # before trusting any absence reported below.
    assert "&xi;" in back and "₀" in back, "reader integrity: the file did not read"
    print()
    print("  post-generation absence checks (gated on the assertion above):")
    dbl = re.findall(r"&amp;[a-zA-Z]+;", back)
    print("    double-escaped entities        : %d %s"
          % (len(dbl), sorted(set(dbl)) if dbl else "(none)"))
    assert not dbl, "double-escaped entities would publish as literal text: %s" % sorted(set(dbl))
    plain = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", back)))
    stray = []
    for m in re.finditer(r"(?i)\bdraft\b|\bno deposit\b|\bnot deposited\b", plain):
        ctx = plain[max(0, m.start() - 90):m.start() + 90]
        if '"' in ctx or "watermark" in ctx or "build" in ctx:
            continue                      # a QUOTATION of v1.6's watermark
        stray.append(ctx.strip())
    print("    unquoted draft-stage language  : %d" % len(stray))
    for s in stray:
        print("      ...%s..." % s)
    assert not stray, "draft-stage language would be published"

    print()
    print("  internal provenance stripped (operator ruling: anything a reader")
    print("  can resolve stays; anything only the author can resolve goes):")
    for why, detail in prov:
        print("    %-34s %s" % (why, detail))

    residue = sorted(set(re.findall(
        r"CT-S\d+[A-Z0-9-]*|CT-R\d+[A-Z0-9-]*|refs/[^\s,;)<]+|scripts/[^\s,;)<]+"
        r"|sessions/[^\s,;)<]+|\b[A-Za-z0-9_]+\.(?:py|json|tex|txt|png)\b"
        r"|\bS\d+[A-Z]?-\d\d\b", plain)))
    print("    %-34s %d %s" % ("residual internal identifiers", len(residue),
                               residue if residue else "(none)"))
    assert not residue, ("internal provenance would be published: %s" % residue)

    # The other half of the ruling: what a reader CAN resolve must still be
    # there.  A strip that also removed the citations would pass the check
    # above and leave the attribution in section 2-4 unsupported.
    must_resolve = ["10.1137/1009002", "10.1007/bf02398269", "10.1002/sapm1992874289",
                    "10.1142/S0219530522400012", "10.1137/1.9781611977912.37",
                    "dlmf.nist.gov/3.6", "dlmf.nist.gov/2.9", "arXiv:2508.15246",
                    "odlyzko/doc/asymptotic.enum.pdf",
                    "10.5281/zenodo.19941678", "10.5281/zenodo.22782807"]
    lost = [s for s in must_resolve if s not in plain]
    print("    %-34s %d of %d present"
          % ("resolvable identifiers", len(must_resolve) - len(lost), len(must_resolve)))
    assert not lost, "the strip removed resolvable citations: %s" % lost


if __name__ == "__main__":
    main()
