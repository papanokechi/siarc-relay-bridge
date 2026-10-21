#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CT-S50 -- emit claims.jsonl.  Validates the in-memory buffer BEFORE
writing; every output_hash is recomputed from the file on disk."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
REP = HERE / "outputs" / "check_repairs.out.txt"
SYM = HERE / "outputs" / "symbol_index.out.txt"
LOG = HERE / "paper.log"
AMD = HERE / "P0-AMENDMENT-H-UNSWEPT-SCOPE.md"
DEST = HERE / "claims.jsonl"

for p in (REP, SYM, LOG, AMD):
    if not p.exists():
        sys.exit("REFUSED: missing evidence file %s" % p.name)

RT, ST = REP.read_text(encoding="utf-8"), SYM.read_text(encoding="utf-8")
LT = LOG.read_text(encoding="utf-8", errors="replace")
AT = AMD.read_text(encoding="utf-8")
H_REP = hashlib.sha256(REP.read_bytes()).hexdigest()
H_SYM = hashlib.sha256(SYM.read_bytes()).hexdigest()
H_LOG = hashlib.sha256(LOG.read_bytes()).hexdigest()
H_AMD = hashlib.sha256(AMD.read_bytes()).hexdigest()

LABELS = {"PROVEN", "VERIFIED", "INSPECTED", "STRUCTURAL", "CONJECTURED"}
SR = "sessions/2026-09-17/CT-S50-READ-REPAIRS/scripts/check_repairs.py"
SS = "sessions/2026-09-17/CT-S50-READ-REPAIRS/scripts/symbol_index.py"
SA = "sessions/2026-09-17/CT-S50-READ-REPAIRS/P0-AMENDMENT-H-UNSWEPT-SCOPE.md"


def C(cid, label, claim, script, h, **kw):
    d = {"claim_id": cid, "task_id": "CT-S50-READ-REPAIRS", "label": label,
         "claim": claim, "evidence_type": kw.pop("ev", "file_inspection"),
         "dps": None, "reproducible": True, "script": script,
         "output_hash": h}
    d.update(kw)
    return d


CLAIMS = [
    C("S50-01", "INSPECTED",
      "Section 9.4 item 6 and appendix B.5 item 3, which both disclaimed that "
      "any displayed formula had been re-derived, have been rewritten to the "
      "routed census: of 56 displays in sections 0-10, 21 re-derived "
      "symbolically, 15 traced to a recorded claim, 9 verified against the "
      "printed page, 11 definitional, 0 unrouted. Section 9.4's false clause "
      "that appendix A's formulas were transcribed rather than computed is "
      "removed; appendix A's closing note, which reports both routes exercised "
      "in CT-S45-FORMULA-A, stands unedited.", SR, H_REP),
    C("S50-02", "VERIFIED",
      "Every one of the twelve ruled repairs is verified three ways: the "
      "repaired text present in the live tree, the pre-repair text absent from "
      "it, and the pre-repair text still present in refs/, a snapshot taken "
      "before any edit. 25 checks, 0 FAILED; 19 controls, 19 FIRED. A repair "
      "whose pre-repair text is missing from refs/ causes refusal at exit 2, "
      "because 'absent' would then be indistinguishable from 'unreadable'.",
      SR, H_REP, ev="computation"),
    C("S50-03", "VERIFIED",
      "The repaired paper builds at 39 pages with 0 undefined references and "
      "0 multiply-defined labels, unchanged in page count from the pre-repair "
      "tree.", SR, H_LOG, ev="build"),
    C("S50-04", "INSPECTED",
      "section7.tex:170 states a_i = tr(B_i) = 2 identically, so the value 2 "
      "in the pre-repair 's_1=s_2=2' belongs to a_i. The symbol s_1 was a "
      "residue of an earlier draft, not a third meaning of s, and the rename "
      "to a_1=a_2=2 is a correction rather than a choice of convention.",
      SR, H_REP),
    C("S50-05", "INSPECTED",
      "section3.tex:32 states that z=0 is System A's only finite singular "
      "point (S4-05), so its singular set is {0, infinity} and both the r(1) "
      "and r(t) positions are genuinely absent. Writing its Katz multiset as "
      "(1/2,-,1/2,-) is read off the paper, not supplied to fit the "
      "convention.", SR, H_REP),
    C("S50-06", "STRUCTURAL",
      "The notation pass's claim S44-05 is literally accurate: it states that "
      "section 3's normal potential was unified to section 1's form, and it "
      "was. The defect is unswept scope, not a false claim: the pass repaired "
      "the collisions a read had noticed and never asked where else R occurs, "
      "so section 9's R=P^2/4+P'/2-Q was never in view. The same shape "
      "explains section 1's reuse list having six entries because six "
      "collisions had been noticed, not because six letters are reused.",
      SS, H_SYM),
    C("S50-07", "INSPECTED",
      "A symbol index over the final text classifies every single letter by "
      "syntactic role (CALL, SUB, BARE) across the 13 section files and finds "
      "31 letters in two or more roles across two or more sections, of which "
      "26 are named by no \\item head in section 1's reuse list. This is "
      "reported as a census of candidates, not a gate: two syntactic roles "
      "need not be two meanings, and section 1 declares some reuse in prose "
      "outside the list, which an item-head reader cannot see.", SS, H_SYM),
    C("S50-08", "VERIFIED",
      "The symbol index's item-head extractor carried two reader defects in "
      "succession, each caught by control C1 going DEAD and the script "
      "refusing at exit 2 rather than printing a census: first a regex that "
      "matched \\beta_k and returned the Latin letter b, then, with that "
      "fixed, a search that ran past the item head into the item body, where "
      "the beta entry's prose mentions $b(n)$ and again returned b. Both "
      "would have reported b as already listed before this session. A third "
      "reader defect, a case-sensitive needle for 'the remaining twelve' "
      "against section 9's 'The remaining twelve', failed check G6 on the "
      "first repair run. Three reader defects, zero paper defects.",
      SS, H_SYM, ev="computation"),
    C("S50-09", "CONJECTURED",
      "The 26 multi-role letters not named by an item head are a candidate "
      "list for a reading pass, not a defect list. Making the screen fail on "
      "them would be a threshold tuned to an answer; most are expected to be "
      "innocent.", SS, H_SYM),
    C("S50-10", "INSPECTED",
      "Section 10.1's cross-reference was written with \\nameref, which pulls "
      "the whole paragraph title; that title already carries its own citation, "
      "so the rendered page read 'set out at What is false (S17-02, PROVEN) "
      "(S17-02, PROVEN), is trivial' -- the citation printed twice. Replaced "
      "with \\ref, which renders 'of section 7.1 (S17-02, PROVEN) is trivial'. "
      "Checks G7 and G8 are run against the pdftotext rendering, with a "
      "control requiring that the page reader can see paragraph titles at all, "
      "so 'no doubled citation' cannot be satisfied by a reader blind to them. "
      "Section 1's unverifiable letter count was dropped in the same pass; G9 "
      "confirms no count survives on the page.", SR, H_REP),
    C("S50-11", "STRUCTURAL",
      "A source-level check cannot see a typesetting defect. The \\nameref "
      "doubling occurred in well-formed source, under a clean build, with "
      "every reference resolving and every source invariant satisfied; it "
      "existed only in the rendering. No check in this run before G7-G9 read "
      "the rendered page, so the whole class was outside what any instrument "
      "here could observe. The general form: a check must read the artefact "
      "the defect lives in, and must carry a control proving its reader can "
      "see that class of thing.", SR, H_REP),
    C("S50-12", "INSPECTED",
      "P0 amendment H is ADOPTED by operator ruling of 2026-09-21, with one "
      "clause added at adoption: when a repair pass is commissioned from a "
      "reported list, its first act is to sweep for the same defect elsewhere, "
      "and the sweep's result is part of the pass's output whether or not it "
      "finds anything. The ordering is load-bearing -- a sweep run after the "
      "reported items are repaired is written from inside the reported list "
      "and inherits its shape -- and so is the null result, since an empty "
      "sweep and an absent sweep are indistinguishable in a report that "
      "records only repairs. S44-05 would have failed the clause: its output "
      "named no scope, so nothing distinguished 'sections 6 and 9 were checked "
      "and are fine' from 'sections 6 and 9 were never looked at'. They were "
      "never looked at. This claim supersedes S50-06, which was written while "
      "the amendment was PROPOSED; S50-06 stands unedited.",
      SA, H_AMD, supersedes="S50-06"),
]

errs, seen = [], set()
for c in CLAIMS:
    cid = c["claim_id"]
    if cid in seen:
        errs.append("%s duplicate" % cid)
    seen.add(cid)
    if c["label"] not in LABELS:
        errs.append("%s bad label %r" % (cid, c["label"]))
    if len(c["claim"]) < 60:
        errs.append("%s claim too short to be evidence" % cid)
    if not (ROOT / c["script"]).exists():
        errs.append("%s script does not resolve" % cid)
    if c["output_hash"] not in (H_REP, H_SYM, H_LOG, H_AMD):
        errs.append("%s output_hash is not a digest of a session output" % cid)
    if "supersedes" in c and c["supersedes"] not in seen:
        errs.append("%s supersedes %s, which is not an earlier claim here"
                    % (cid, c["supersedes"]))

# anchored-figure rule: each cited figure on a line naming what it counts
for fig, anchor, txt in [("25", "checks", RT), ("19", "controls", RT),
                         ("39", "pages", LT), ("31", "multi-role", ST),
                         ("26", "not named", ST)]:
    if not any(fig in ln and anchor in ln for ln in txt.splitlines()):
        errs.append("figure %s is not anchored to a line naming %r"
                    % (fig, anchor))

# non-vacuity: a zero numerator is a count of nothing tested
if re.search(r"\b0 checks\b|\b0 controls\b|0 FIRED", RT):
    errs.append("evidence reports a zero numerator")
if "0 FAILED" not in RT:
    errs.append("the repair check did not report a clean run")
# the two new claims cite page-level checks by name; they must be in evidence
for g in ("G7", "G8", "G9"):
    if not any(g in ln and "OK" in ln for ln in RT.splitlines()):
        errs.append("page-level check %s is not reported OK in the evidence" % g)
if "page reader does see paragraph titles" not in RT:
    errs.append("the page reader's control is not recorded as fired")
# S50-12 asserts the amendment is ADOPTED and carries the commissioning clause.
# Read the status off the document's own head, not off a search of the body,
# which quotes the word PROPOSED historically.
_head = AT.splitlines()[:4]
if not any(ln.startswith("**Status: ADOPTED") for ln in _head):
    errs.append("the amendment's head does not declare it ADOPTED")
if any("PROPOSED" in ln for ln in _head):
    errs.append("the amendment's head still carries PROPOSED")
for needle in ("COMMISSIONED FROM A REPORTED LIST",
               "whether or not it finds anything",
               "## The clause added on adoption"):
    if needle not in AT:
        errs.append("the amendment does not carry %r" % needle)
if "supersedes" not in AT:
    errs.append("the amendment does not record the superseding claim")
if "REFUSED" in RT or "REFUSED" in ST:
    errs.append("an evidence file records a refusal; it is not a clean result")

if errs:
    print("REFUSED -- nothing written:")
    for e in errs:
        print("  " + e)
    sys.exit(2)

DEST.write_text("\n".join(json.dumps(c, ensure_ascii=False) for c in CLAIMS)
                + "\n", encoding="utf-8")
back = [json.loads(l) for l in DEST.read_text(encoding="utf-8").splitlines()]
assert len(back) == len(CLAIMS)
print("wrote %d claims" % len(back))
print("  check_repairs.out.txt sha256 %s" % H_REP[:32])
print("  symbol_index.out.txt  sha256 %s" % H_SYM[:32])
print("  paper.log             sha256 %s" % H_LOG[:32])
print("  amendment H           sha256 %s" % H_AMD[:32])
print("  claims.jsonl          sha256 %s"
      % hashlib.sha256(DEST.read_bytes()).hexdigest()[:32])
for b in back:
    print("  %-7s %-11s %s..." % (b["claim_id"], b["label"], b["claim"][:52]))
