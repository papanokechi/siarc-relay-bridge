#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CT-S51 -- upload readiness gate.

Read-only.  Verifies the arXiv submission source and the June metadata package
against the artefacts as they stand today, and against a stored snapshot of the
live Zenodo record.  Nothing is uploaded, edited or written except this
script's own output file.

Exit codes:  0 clean | 1 finding | 2 refusal (instrument cannot see) | 3 crash
"""
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
OUT = HERE / "outputs" / "check_upload_ready.out.txt"

TEX = (ROOT / "sessions" / "2026-06-16" / "VQUAD-PAPER-LAYOUTFIX-001" /
       "latex" / "vquad-periodrep-paper.tex")
PDF = TEX.with_suffix(".pdf")
LOG = TEX.with_suffix(".log")
PKG = HERE / "refs" / "arxiv-metadata-package.md"
SNAP = HERE / "outputs" / "zenodo_20719043.json"
S4 = ROOT / "sessions" / "2026-09-17" / "CT-S4-FORMAL-TYPE" / "claims.jsonl"

LINES, FIND, CTRL = [], [], []
NCHK = [0]


def say(s=""):
    LINES.append(s)
    print(s)


def chk(tag, ok, detail):
    NCHK[0] += 1
    say("  %-5s %-4s %s" % (tag, "OK" if ok else "FAIL", detail))
    if not ok:
        FIND.append("%s: %s" % (tag, detail))
    return ok


def ctl(tag, fired, detail):
    say("  %-5s %-6s %s" % (tag, "FIRED" if fired else "DEAD", detail))
    CTRL.append((tag, fired))
    return fired


for p in (TEX, PDF, LOG, PKG, SNAP, S4):
    if not p.exists():
        sys.exit("REFUSED: missing input %s" % p)

# Strings the public source must not carry live in a private file outside
# every repository, so this script never contains them.  Fails closed: a
# missing or implausibly short file is a refusal, never an empty list that
# would let every identity check pass.  Matches are reported by index only.
PATTERNS = Path(r"C:\LocalWork\operator\private\patterns.txt")
if not PATTERNS.is_file():
    sys.exit("REFUSED: private pattern file not found; the identity check "
             "cannot see what it screens for")
FORB = [l.strip() for l in PATTERNS.read_text(encoding="utf-8").splitlines()
        if l.strip()]
if len(FORB) < 5:
    sys.exit("REFUSED: private pattern file has too few patterns (%d)"
             % len(FORB))
FORB_RX = [re.compile(r"\s+".join(re.escape(w) for w in p.split()), re.I)
           for p in FORB]


def forbidden_hits(text):
    """Indices of the private patterns present in text (never the strings)."""
    return [i for i, rx in enumerate(FORB_RX) if rx.search(text)]


def masked(text):
    """text with every private-pattern match replaced by <P index>, for echo."""
    for i, rx in enumerate(FORB_RX):
        text = rx.sub("<P%d>" % i, text)
    return text

T = TEX.read_text(encoding="utf-8")
P = PKG.read_text(encoding="utf-8")
Z = json.loads(SNAP.read_text(encoding="utf-8"))
LG = LOG.read_text(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- helpers
FORBIDDEN = (r"\input", r"\include", r"\includegraphics",
             r"\bibliography", r"\bibliographystyle")


def scan_constructs(text):
    """Count the constructs that would make a single-file upload wrong.
    \\include must not be counted for \\includegraphics."""
    n = {}
    for c in FORBIDDEN:
        if c == r"\include":
            n[c] = len(re.findall(r"\\include\b(?!graphics)", text))
        else:
            n[c] = len(re.findall(re.escape(c) + r"\b", text))
    n["thebibliography"] = text.count(r"\begin{thebibliography}")
    return n


MACROS = [(r"\Vquad", r"V_{\mathrm{quad}}"), (r"\Bhat", r"\widehat{B}"),
          (r"\Qsqrt", r"\mathbb{Q}(\sqrt3)"), (r"\Qbar", r"\overline{\mathbb{Q}}"),
          (r"\SL", r"\mathrm{SL}"), (r"\K", "K")]


def expand(s):
    for a, b in sorted(MACROS, key=lambda m: -len(m[0])):
        s = re.sub(re.escape(a) + r"(?![A-Za-z])", b.replace("\\", "\\\\"), s)
    return s


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def abstract_of_tex(text):
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    return m.group(1) if m else None


def package_abstract(text):
    """Field 3's fenced block: the one fenced block that starts 'We prove'."""
    for blk in re.findall(r"```(.*?)```", text, re.S):
        if blk.strip().startswith("We prove"):
            return blk
    return None


say("CT-S51 UPLOAD READINESS -- read-only")
say("source : %s" % TEX.relative_to(ROOT).as_posix())
say("")

# ------------------------------------------------- A: source integrity
say("A. arXiv source integrity")
h_tex = hashlib.sha256(TEX.read_bytes()).hexdigest()
h_pdf = hashlib.sha256(PDF.read_bytes()).hexdigest()
chk("A1", TEX.stat().st_size == 87778,
    "tex size %d bytes (inventory records 87778)" % TEX.stat().st_size)
say("        tex sha256 %s" % h_tex)
chk("A2", h_pdf.startswith("33f339ed"),
    "pdf re-hashes to the layout-fixed pin: %s" % h_pdf[:16])
n = scan_constructs(T)
chk("A3", all(n[c] == 0 for c in FORBIDDEN) and n["thebibliography"] == 1,
    "self-contained: " + ", ".join("%s=%d" % (k.lstrip("\\"), v)
                                   for k, v in n.items()))
chk("A4", not forbidden_hits(T) and r"\author{Papanokechi}" in T,
    "identity: 0 of %d private-pattern strings, author reads Papanokechi"
    % len(FORB))
chk("A5", "Compositio" not in T and "submitted to" not in T.lower(),
    "no venue string in the public source")
m = re.search(r"Output written on .*?\((\d+) pages", LG)
chk("A6", bool(m) and m.group(1) == "24",
    "build log reports %s pages" % (m.group(1) if m else "?"))
say("")

# ------------------------------------------------- B: live record state
say("B. Zenodo record state (stored snapshot of the live API)")
chk("B1", Z.get("state") == "done" and Z.get("submitted") is True,
    "record 20719043 state=%s submitted=%s" % (Z.get("state"), Z.get("submitted")))
chk("B2", Z.get("doi") == "10.5281/zenodo.20719043" and
    Z.get("conceptdoi") == "10.5281/zenodo.20719042",
    "version DOI %s / concept DOI %s" % (Z.get("doi"), Z.get("conceptdoi")))
chk("B3", Z["metadata"]["license"]["id"] == "cc-by-4.0",
    "license %s" % Z["metadata"]["license"]["id"])
nf = len(Z.get("files", []))
nr = len(Z["metadata"].get("related_identifiers", []))
chk("B4", nf == 2 and nr == 11,
    "%d files, %d related identifiers" % (nf, nr))
chk("B5", Z["metadata"]["creators"][0].get("orcid") == "0009-0000-6192-8273",
    "creator ORCID %s" % Z["metadata"]["creators"][0].get("orcid"))
say("        published %s" % Z["metadata"]["publication_date"])
say("")

# ------------------------------------------------- C: epistemic agreement
say("C. Does the uploaded source say what the typed abstract says?")
at, ap = abstract_of_tex(T), package_abstract(P)
if at is None or ap is None:
    say("  REFUSED: could not locate one of the two abstracts")
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    sys.exit(2)
ea, eb = norm(expand(at)), norm(ap)
same = ea == eb
chk("C1", same, "macro-expanded tex abstract == package abstract")
if not same:
    sm = difflib.SequenceMatcher(None, ea.split(), eb.split())
    diffs = [(" ".join(ea.split()[i1:i2]), " ".join(eb.split()[j1:j2]))
             for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    say("        %d differing region(s):" % len(diffs))
    for a, b in diffs:
        say("          SOURCE : %r" % masked(a))
        say("          PACKAGE: %r" % masked(b))
    hedged = [d for d in diffs if "conjectur" in d[1].lower()]
    # C2 AS PRE-REGISTERED.  It asks whether there is exactly ONE differing
    # region.  That is not the same question as "one semantic change": an
    # adjacent replacement plus insertion is one hedge but two opcodes, so the
    # predicate cannot distinguish a single hedge from two edits.  It is
    # recorded as ill-posed rather than retuned (PREREG F4), and replaced by
    # C2b, which is decidable.
    chk("C2", len(diffs) == len(hedged) and len(hedged) == 1,
        "PRE-REGISTERED, ILL-POSED: counts diff REGIONS, not semantic "
        "changes; %d regions, %d carrying a hedge" % (len(diffs), len(hedged)))
    # C2b: undo the documented hedge on the package side.  If the two texts
    # are then byte-equal, the hedge is provably the ONLY difference.
    unhedged = eb.replace("closure, whose Sakai surface type is conjectured "
                          "to be", "closure on the Sakai surface")
    chk("C2b", unhedged == ea,
        "removing the hedge clause from the package text makes it identical "
        "to the source abstract: the hedge is the only difference")
zd = Z["metadata"]["description"]
chk("C3", "closure on the Sakai surface" in zd and "conjectur" not in
    zd.split("admits an explicit")[0],
    "the PUBLISHED record carries the unhedged wording")
say("")

# ------------------------------------------------- D: corpus support
say("D. What label does the corpus give the D_5^(1) attribution?")
s4 = S4.read_text(encoding="utf-8")
chk("D1", "CONJECTURE 4.1" in s4,
    "CT-S4 records the companion's v1.2 as carrying 'CONJECTURE 4.1'")
chk("D2", "VERDICT (c) INCONCLUSIVE" in s4,
    "CT-S4's own verdict on the attribution is 'VERDICT (c) INCONCLUSIVE'")
# Echo the matched text rather than asserting a verdict about it: a check that
# reports OK without showing what it matched cannot be audited downstream.
for cid, needle in (("S4-01", "CONJECTURE 4.1"),
                    ("S4-09", "VERDICT (c) INCONCLUSIVE")):
    for row in s4.splitlines():
        if needle in row and '"claim_id": "%s"' % cid in row:
            i = row.index(needle)
            say("        %s quotes: ...%s..."
                % (cid, row[max(0, i - 60):i + len(needle) + 40]))
            break
say("")

# ------------------------------------------------- vacuity, AFTER the above
say("Vacuity pre-checks (run after the observables, per the CT-S47 ordering)")
probe = r"text \input{x} more \includegraphics[w]{y} and \bibliography{z}"
pn = scan_constructs(probe)
ctl("V1", pn[r"\input"] == 1 and pn[r"\includegraphics"] == 1 and
    pn[r"\bibliography"] == 1 and pn[r"\include"] == 0,
    "construct reader finds planted constructs and does not count "
    "\\includegraphics as \\include")
raw = r"the \Vquad series and \Bhat of it"
ctl("V2a", norm(expand(raw)) == norm(r"the V_{\mathrm{quad}} series and "
                                     r"\widehat{B} of it"),
    "comparator reports equality for a text and its expansion")
ctl("V2b", norm(expand(raw)) != norm(r"the V_{\mathrm{quad}} series and "
                                     r"\widehat{B} of that"),
    "comparator reports difference when one word changes")
ctl("V3", Z["metadata"].get("__absent__") is None and
    "publication_date" in Z["metadata"],
    "snapshot reader distinguishes an absent field from an unread one")
ctl("V4",
    all(i in forbidden_hits("zz %s zz" % p) for i, p in enumerate(FORB))
    and forbidden_hits(T + "\n" + FORB[0]) != []
    and "Papanokechi" in T,
    "identity reader fires on each planted private pattern, the A4 test "
    "fails on the source plus a planted one, and the benign name is present")
say("")

nf_ = len(FIND)
dead = [t for t, f in CTRL if not f]
say("RESULT: %d checks, %d FINDING(S); %d controls, %d FIRED"
    % (NCHK[0], nf_, len(CTRL), len(CTRL) - len(dead)))
for f in FIND:
    say("  FINDING %s" % f)
OUT.parent.mkdir(exist_ok=True)
OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")

if dead:
    print("REFUSED: dead controls %s" % dead)
    sys.exit(2)
sys.exit(1 if FIND else 0)
