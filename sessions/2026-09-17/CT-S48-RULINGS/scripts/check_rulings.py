#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CT-S48-RULINGS -- checks the four record actions against the files they name.

Exit codes (the separation CT-S46/CT-S47 established):
  0  every check passed and every control fired
  1  a finding: a check failed
  2  a refusal: the instrument cannot answer (missing file, dead control)
  3  a crash
"""
import hashlib
import json
import re
import sys
from pathlib import Path

SESSIONS = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "outputs" / "check_rulings.out.txt"

LINES = []
FINDINGS = []
NCHECK = 0
NCTRL = 0


def _crash(exc_type, exc, tb):
    import traceback
    sys.stderr.write("".join(traceback.format_exception(exc_type, exc, tb)))
    sys.stderr.write("\nCRASH -- exit 3 (not a finding, not a refusal)\n")
    sys.exit(3)


sys.excepthook = _crash


def emit(s=""):
    LINES.append(s)
    print(s)


def refuse(why):
    emit("")
    emit("REFUSED: " + why)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    sys.exit(2)


def check(cid, ok, desc):
    global NCHECK
    NCHECK += 1
    emit("  [%s] %-6s %s" % ("PASS" if ok else "FAIL", cid, desc))
    if not ok:
        FINDINGS.append(cid)
    return ok


def control(cid, fired, desc):
    global NCTRL
    NCTRL += 1
    emit("  [%s] %-6s %s" % ("FIRED" if fired else "DEAD ", cid, desc))
    if not fired:
        refuse("control %s did not fire, so the check it guards is "
               "uninterpretable" % cid)
    return fired


def must_exist(p):
    if not p.exists():
        refuse("required file does not exist: %s" % p)
    return p


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def load_claim(rel, cid):
    """Resolve a claim by its exact claim_id field. Never by text search."""
    path = must_exist(SESSIONS / rel)
    found = None
    for ln, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        raw = raw.strip()
        if not raw:
            continue
        try:
            d = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if d.get("claim_id") == cid:
            if found is not None:
                refuse("claim id %s appears twice in %s" % (cid, rel))
            found = (d, ln)
    if found is None:
        refuse("claim %s not found in %s" % (cid, rel))
    return found


def line_reporting(path, figure, anchor):
    """
    S44-17's standing rule: a figure must resolve to the summary line that
    REPORTS it, not to a digit string anywhere in a file full of digits.
    Returns the line, or None.
    """
    for raw in path.read_text(encoding="utf-8").splitlines():
        if figure in raw and anchor in raw:
            return raw.strip()
    return None


# ----------------------------------------------------------------------
emit("=" * 70)
emit("CT-S48-RULINGS -- four record actions, checked against their files")
emit("=" * 70)
emit()

# ======================================================================
# R1 -- S25-01's scope: the RECORDED solutions, not the PRINTED ones
# ======================================================================
emit("R1  S25-01 is about the recorded solutions")
emit("-" * 70)

s25, s25_line = load_claim("2026-09-17/CT-S25-N1-EXHAUSTIVE/claims.jsonl", "S25-01")
s25_text = s25["claim"]
emit("  resolved S25-01 at claims.jsonl:%d, label %s" % (s25_line, s25["label"]))


def names_printed_artefact(text):
    """The detector under test. Returns the list of printed-side tokens seen."""
    seen = []
    for tok in ("section5.tex", "printed", "typeset"):
        if tok in text.lower():
            seen.append(tok)
    return seen


seen = names_printed_artefact(s25_text)
check("R1-a", "pq_solution.txt" in s25_text,
      "names the RECORDED artefact outputs/pq_solution.txt")
check("R1-b", "locate_final.py" in s25_text,
      "names the construction it re-derived from")
check("R1-c", seen == [],
      "names no printed-side artefact (found: %s)" % (seen or "none"))

fired = names_printed_artefact(s25_text + " ... and section5.tex too")
control("R1c", fired == ["section5.tex"],
        "the same detector SEES section5.tex when it is present "
        "(absence means absence, not unreadability)")
emit()

# ======================================================================
# R2 -- CT-S47 covers the printed forms
# ======================================================================
emit("R2  CT-S47 establishes the printed forms separately")
emit("-" * 70)

route = must_exist(SESSIONS / "2026-09-17/CT-S47-FORMULA-S5-QP/outputs/route_s5_qp.out.txt")
src_line = line_reporting(route, "section5.tex", "source")
sum_line = line_reporting(route, "36 checks, 0 DIFFER", "ROUTE S")

check("R2-a", src_line is not None,
      "a SOURCE line reports section5.tex: %s" % (src_line or "ABSENT"))
check("R2-b", sum_line == "ROUTE S (section 5 q,p): 36 checks, 0 DIFFER",
      "the SUMMARY line reads verbatim: %s" % (sum_line or "ABSENT"))

tex = must_exist(SESSIONS / "2026-09-17/CT-S47-FORMULA-S5-QP/refs/section5.tex")
tex_sha = sha256(tex)
check("R2-c", src_line is not None and tex_sha[:16] in src_line,
      "the source line carries the LIVE digest of section5.tex (%s...)" % tex_sha[:16])

control("R2c-1", line_reporting(route, "37 checks, 0 DIFFER", "ROUTE S") is None,
        "no summary line reports 37 checks (the figure is resolved to its "
        "reporting line, not to a digit string)")
control("R2c-2", line_reporting(route, "36 checks, 0 DIFFER", "NOT A REAL ANCHOR") is None,
        "the anchor is load-bearing: the same figure under a false anchor "
        "is not found")
emit()

# ======================================================================
# R3 -- the bar for amendment G: one filename, two pages
# ======================================================================
emit("R3  the filename jimbo_p1152.png denotes two different images")
emit("-" * 70)

wrong = must_exist(SESSIONS / "2026-09-17/CT-S21-DEPOSIT-PREP/pages/jimbo_p1152.png")
right = must_exist(SESSIONS / "2026-09-17/CT-S21-DEPOSIT-PREP/pages/jimbo_printed1152.png")
other = must_exist(SESSIONS / "2026-09-17/CT-R1-AUDIT/coldpackets/jimbo_p1152.png")
marker = must_exist(SESSIONS / "2026-09-17/CT-S21-DEPOSIT-PREP/pages/README.md")

h_wrong, h_right, h_other = sha256(wrong), sha256(right), sha256(other)
for nm, h in (("pages/jimbo_p1152.png", h_wrong),
              ("pages/jimbo_printed1152.png", h_right),
              ("coldpackets/jimbo_p1152.png", h_other)):
    emit("  live sha256  %-30s %s" % (nm, h[:16] + "..."))

check("R3-a", h_wrong != h_other,
      "the two files sharing the name jimbo_p1152.png differ")
check("R3-b", h_right != h_wrong and h_right != h_other,
      "jimbo_printed1152.png is a third, distinct image")

# PREREG section 5 predicted this: the marker records 16-hex PREFIXES.
mtext = marker.read_text(encoding="utf-8")
for cid, h, nm in (("R3-c", h_wrong, "the misnamed image"),
                   ("R3-d", h_right, "the correct folio-1152 image"),
                   ("R3-e", h_other, "the correctly-named copy elsewhere")):
    check(cid, h[:16] in mtext,
          "the marker names %s by digest (%s...)" % (nm, h[:16]))

def needle(text, phrase):
    """
    S43-12: an arm or check that matches RAW text with a single-space needle
    fails on a line-wrapped phrase. Join the tokens with \\s+ so the needle
    cannot be defeated by where the source happens to wrap.
    """
    pat = r"\s+".join(re.escape(t) for t in phrase.split())
    return re.search(pat, text) is not None


check("R3-f", needle(mtext, "Resolve these images by hash, never by filename."),
      "the marker states the rule (needle is wrap-tolerant)")

control("R3c-2", not needle(mtext, "Resolve these images by filename, never by hash."),
        "the wrap-tolerant needle does not match the rule REVERSED")

bogus = hashlib.sha256(b"no image in this tree has this content").hexdigest()
control("R3c", bogus[:16] not in mtext,
        "a digest belonging to no image in the tree is NOT found in the marker")
emit()

# ======================================================================
# R4 -- a PROVEN claim whose own text carries a formula wrong as written
# ======================================================================
emit("R4  S16-R18-02 carries PROVEN and a formula wrong as written")
emit("-" * 70)

r18, r18_line = load_claim("2026-09-17/CT-S16-MEMBERSHIP-C/claims.jsonl", "S16-R18-02")
r18_text = squash(r18["claim"])
emit("  resolved S16-R18-02 at claims.jsonl:%d" % r18_line)

UNFACT = ("z(4pqt - 4pq - 4pt + 4p + q^3 t^2 - q^3 - 2 q^2 t^2 + 2 q^2 "
          "+ q t^2 - q)/4")
FACT = "-z(q-1)(t-1)(4p + q^2 t + q^2 - qt - q)/4"

check("R4-a", r18["label"] == "PROVEN",
      "the label is PROVEN (it is: %s)" % r18["label"])
check("R4-b", UNFACT in r18_text, "the claim text carries the UNFACTORED form")
check("R4-c", FACT in r18_text, "the claim text carries the FACTORED form")

sign = must_exist(SESSIONS / "2026-09-17/CT-S47-FORMULA-S5-QP/outputs/check_r18_sign.out.txt")
verdict = line_reporting(sign, "CLAIM TEXT", "VERDICT")
agree = line_reporting(sign, "the claim's own two forms agree: False", "agree")
plus = line_reporting(sign, "PLUS one quarter of the same product reproduces it: True", "PLUS")

check("R4-d", verdict is not None,
      "CT-S47's check reports the verdict: %s" % (verdict or "ABSENT"))
check("R4-e", agree is not None,
      "and reports that the claim's two forms disagree")
check("R4-f", plus is not None,
      "and that PLUS one quarter reproduces it, so the truth is the + sign")

stripped = r18_text.replace(FACT, "")
control("R4c", FACT not in stripped,
        "with the factored form deleted, the same comparison reports it MISSING")
emit()

# ======================================================================
emit("=" * 70)
if FINDINGS:
    emit("RULINGS CHECK: %d FAILED -- %s" % (len(FINDINGS), ", ".join(FINDINGS)))
    emit("=" * 70)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    sys.exit(1)

emit("RULINGS CHECK: %d checks, 0 FAILED; %d controls, %d FIRED"
     % (NCHECK, NCTRL, NCTRL))
emit("=" * 70)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
sys.exit(0)
