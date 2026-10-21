#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CT-S49-FULLREAD -- emit claims.jsonl.  Validates the in-memory buffer
BEFORE writing, then recomputes every output_hash from the file on disk."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
OUTF = HERE / "outputs" / "check_read_findings.out.txt"
REPORT = HERE / "REPORT.md"
DEST = HERE / "claims.jsonl"

OUT = OUTF.read_text(encoding="utf-8")
REP = REPORT.read_text(encoding="utf-8")
SHA = hashlib.sha256(OUTF.read_bytes()).hexdigest()

LABELS = {"PROVEN", "VERIFIED", "INSPECTED", "STRUCTURAL", "CONJECTURED"}


def C(cid, label, claim, ev, script, out_hash, **kw):
    d = {"claim_id": cid, "task_id": "CT-S49-FULLREAD", "label": label,
         "claim": claim, "evidence_type": ev, "dps": None,
         "reproducible": True, "script": script, "output_hash": out_hash}
    d.update(kw)
    return d


S = "sessions/2026-09-17/CT-S49-FULLREAD/scripts/check_read_findings.py"
R = "sessions/2026-09-17/CT-S49-FULLREAD/REPORT.md"

CLAIMS = [
    C("S49-01", "INSPECTED",
      "The paper disclaims the formula re-derivation in two places while "
      "Appendix A reports it as performed: section9.tex:183-184 says 'none has "
      "been symbolically re-derived here' and names app:typo; appendixB.tex:139 "
      "says 'No displayed formula in this paper has been re-derived here'; "
      "appendixA.tex:147 says 'Both routes were exercised for this appendix in "
      "CT-S45-FORMULA-A, per equation'. CT-S45-FORMULA-A is named exactly once "
      "in the paper.", "file_inspection", S, SHA),
    C("S49-02", "INSPECTED",
      "section8.tex:210-211 contains a self-contradictory sentence: a "
      "structural argument 'has been sought and not found --- the first being "
      "the twist question of ssec:tracefree, where one was found'.",
      "file_inspection", S, SHA),
    C("S49-03", "INSPECTED",
      "section5.tex:148 quotes the phrase 'for both sign branches' and "
      "attributes it to ssec:located; the phrase occurs nowhere in the paper "
      "outside that quotation. Confirmed by counting occurrences and excluding "
      "the quoting line, not by a needle that could match itself.",
      "file_inspection", S, SHA),
    C("S49-04", "INSPECTED",
      "section1.tex:205 declares the scalar form A W'' + A' W' + C W = 0 and "
      "says it 'occurs only in that displayed form'; the paper's only equation "
      "of that shape, section3.tex:53, names its coefficients lowercase a(x), "
      "b(x), c(x) at section3.tex:55. The declared form occurs once, in its own "
      "declaration.", "file_inspection", S, SHA),
    C("S49-05", "INSPECTED",
      "The letter b carries four meanings (section1.tex:22 the recurrence "
      "polynomial; section3.tex:55 the System-C coefficient; section4.tex:56 "
      "the matrix entry; section5.tex:112 the coefficient b_1) while "
      "section1.tex:225 lists six reused letters not including b, and "
      "section1.tex:14 claims the section fixes every symbol used in the paper.",
      "file_inspection", S, SHA),
    C("S49-06", "INSPECTED",
      "b_1 is used four times in section 5 (section5.tex:112,138,207,212) with "
      "no definition; it is first tied to the matrix entry b at "
      "section6.tex:100.", "file_inspection", S, SHA),
    C("S49-07", "INSPECTED",
      "section7.tex:208 uses s_1=s_2=2; section1.tex:130-133 enumerates exactly "
      "two uses of s (bare, and s_pm) and s_1 does not occur in section1.tex. "
      "The quantity is declared in section 1 as a_i = tr(B_i).",
      "file_inspection", S, SHA),
    C("S49-08", "INSPECTED",
      "The Katz-multiset convention is not followed where it is used: "
      "section1.tex:282-284 fixes (r(0),r(1),r(inf),r(t)) with a dash only in "
      "the r(t) position and writes the PV row (0,0,1,-) at section1.tex:290; "
      "section4.tex:161 writes the same PV row as (0,0,1); section3.tex:203,210 "
      "write (0,0,1) and (1,0,0,0); section3.tex:214 puts a dash in the r(1) "
      "position. The 4-slot form occurs exactly once in the paper.",
      "file_inspection", S, SHA),
    C("S49-09", "INSPECTED",
      "R is displayed in four typographies: section1.tex:211 and "
      "section3.tex:43 as \\tfrac14P^2+\\tfrac12P'-Q, section6.tex:59 as "
      "\\frac{P^2}{4}+\\frac{P'}{2}-Q, section9.tex:36 as P^2/4+P'/2-Q. The "
      "ruling was to unify into section 1's form; sections 6 and 9 did not.",
      "file_inspection", S, SHA),
    C("S49-10", "INSPECTED",
      "S17-02's counterexample is stated at full length twice, section6.tex:25-27 "
      "and section10.tex:25-26, including the identical witness sentence; and "
      "section9.tex:40 re-displays P_C unnumbered rather than eqref-ing eq:PC at "
      "section6.tex:69.", "file_inspection", S, SHA),
    C("S49-11", "STRUCTURAL",
      "Findings S49-01 through S49-10 are cross-file inconsistencies of "
      "statement: each is invisible to a build, a page count, a citation check "
      "and the formula pass, because each requires comparing what one section "
      "promises against what another does. No instrument used in this run "
      "checked across sections.", "file_inspection", R, SHA),
    C("S49-12", "VERIFIED",
      "Two predicates failed on the first run of the confirmation script and "
      "both failures were in the reader: F3b's absence needle matched the "
      "quotation that reports the phrase, and F8e's control went DEAD because "
      "it looked for $(0,0,1,-)$ with maths delimiters where section1.tex:290 "
      "writes it inside a display. The script refused with exit 2 rather than "
      "reporting; repairing both needles gave 14 findings confirmed and 9 of 9 "
      "controls FIRED.", "computation", S, SHA),
    C("S49-13", "CONJECTURED",
      "Three observations could not be decided from the text and are reported "
      "as queries, not defects: the p.2655/p.2629 attribution conflict between "
      "section4.tex:84 and section7.tex:88; whether section10.tex:7's claim "
      "that no section sets up the machinery is contradicted by "
      "section1.tex:108,136 and section3.tex:108; and whether section 7.1's "
      "'performed' contradicts section 6.3.", "file_inspection", R, SHA),
    C("S49-14", "CONJECTURED",
      "This is an instrument-assisted read and does not substitute for the "
      "operator's own reading. It confirms findings a reader named; it cannot "
      "find what it was not looking for.", "file_inspection", R, SHA),
]

# ---- validate the BUFFER, before anything is written --------------------
errs = []
seen = set()
for c in CLAIMS:
    cid = c["claim_id"]
    if cid in seen:
        errs.append("%s: duplicate claim_id" % cid)
    seen.add(cid)
    if c["label"] not in LABELS:
        errs.append("%s: label %r is not one of the five" % (cid, c["label"]))
    if not c["claim"].strip() or len(c["claim"]) < 40:
        errs.append("%s: claim text empty or too short to be evidence" % cid)
    if c["output_hash"] != SHA:
        errs.append("%s: output_hash is not the digest of the evidence file" % cid)
    if not (HERE.parents[2] / c["script"]).exists():
        errs.append("%s: script path does not resolve: %s" % (cid, c["script"]))

# every file:line cited must actually appear in the evidence or the report
for c in CLAIMS:
    for ref in set(re.findall(r"section\d+\.tex:\d+|appendix[AB]\.tex:\d+",
                              c["claim"])):
        f, n = ref.split(":")
        if ("%s:%s" % (f, n)) not in OUT and ref not in REP:
            errs.append("%s: cites %s, which appears in neither the evidence "
                        "file nor the report" % (c["claim_id"], ref))

# anchored-figure rule (S44-17): each figure on a line that names what it counts
for fig, anchor in [("14", "findings"), ("9", "controls")]:
    if not any(fig in ln and anchor in ln and "READ CHECK" in ln
               for ln in OUT.splitlines()):
        errs.append("figure %s/%s is not reported on an anchored summary line"
                    % (fig, anchor))

# non-vacuity: the numerator must not be zero (the 0/11 defect)
if "0 findings" in OUT or "0 FIRED" in OUT:
    errs.append("evidence file reports a zero numerator; nothing was tested")

if errs:
    print("REFUSED -- nothing written:")
    for e in errs:
        print("  " + e)
    sys.exit(2)

DEST.write_text("\n".join(json.dumps(c, ensure_ascii=False) for c in CLAIMS)
                + "\n", encoding="utf-8")

# ---- read back -----------------------------------------------------------
back = [json.loads(l) for l in DEST.read_text(encoding="utf-8").splitlines()]
assert len(back) == len(CLAIMS)
assert all(b["output_hash"] == SHA for b in back)
print("wrote %d claims to %s" % (len(back), DEST))
print("evidence  outputs/check_read_findings.out.txt  sha256 %s" % SHA)
print("claims.jsonl sha256 %s"
      % hashlib.sha256(DEST.read_bytes()).hexdigest())
for b in back:
    print("  %-7s %-11s %s..." % (b["claim_id"], b["label"], b["claim"][:58]))
