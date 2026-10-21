#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CT-S48-RULINGS -- claims emitter.

Validates the in-memory buffer BEFORE writing (a post-write assertion still
leaves the corrupt artefact on disk), recomputes every output_hash from the
file it names, and enforces the anchored-figure rule: a figure cited in a
claim must appear on a line of its evidence file that also carries an anchor
identifying what the figure counts.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SESSIONS = Path(__file__).resolve().parents[3]
DEST = HERE / "claims.jsonl"

RULINGS = HERE / "outputs" / "check_rulings.out.txt"
ROUTE = SESSIONS / "2026-09-17/CT-S47-FORMULA-S5-QP/outputs/route_s5_qp.out.txt"

C = []


def add(cid, task, claim, label, ev, script, outfile, dps=None, supersedes=None):
    d = {
        "claim_id": cid,
        "task_id": task,
        "claim": claim,
        "label": label,
        "evidence_type": ev,
        "dps": dps,
        "reproducible": True,
        "script": script,
        "output_hash": None,
        "_outfile": outfile,
    }
    if supersedes:
        d["supersedes"] = supersedes
    C.append(d)


# ----------------------------------------------------------------------
add("S48-01", "S48/SCOPE-S25-01",
    "SCOPE ANNOTATION, superseding S25-01. S25-01's transcription controls are "
    "about the solutions RECORDED in CT-S16-MEMBERSHIP-C/outputs/pq_solution.txt: "
    "its claim text names that file and names locate_final.py, and names no "
    "printed-side artefact at all -- not section5.tex, not the word 'printed', "
    "not the word 'typeset' (check R1, three passing checks). It therefore does "
    "NOT establish anything about the forms TYPESET in the paper. The gap reads "
    "as covered until someone checks, which is why it is annotated rather than "
    "left implicit. What covers the printed forms is CT-S47-FORMULA-S5-QP, which "
    "parses every numeral and sign OUT OF section5.tex (live sha256 "
    "af25048b9b62a6f4..., reported on the source line of its own output) and "
    "reports 'ROUTE S (section 5 q,p): 36 checks, 0 DIFFER'. S25-01 is not "
    "edited and its label stands; this claim records what it does and does not "
    "cover. The control R1c fires: the same detector SEES section5.tex when the "
    "token is present, so 'names no printed-side artefact' means absence and not "
    "unreadability -- the fourth appearance of that hazard in this run.",
    "INSPECTED", "file_inspection",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt",
    supersedes="S25-01")

add("S48-02", "S48/AMENDMENT-G",
    "P0 amendment G ADOPTED by operator ruling: when a stored file's NAME "
    "misleads about its CONTENT and the file is cited by content digest so that "
    "renaming would strand those citations, add a sibling MARKER FILE beside it "
    "naming the discrepancy, the correct file and the citing rule. The bar is "
    "demonstrated harm, not tidiness -- a marker is written only where the name "
    "has caused a wrong citation or been shown capable of causing one, because a "
    "marker beside every imperfect name decays into noise the next reader learns "
    "to skip. jimbo_p1152.png cleared the bar twice: CT-S15 attributed folio-1153 "
    "transcriptions to 1152, and CT-S46 route P would have reported the paper's "
    "eq:jimbo UNVERIFIABLE against its cited page had it trusted the filename -- "
    "a false finding against correct prose. The instance, "
    "CT-S21-DEPOSIT-PREP/pages/README.md, is verified against LIVE-computed "
    "digests: 05fecc96632ca6d4... (folio 1153, misnamed), 42fffb7b09ff60b5... "
    "(folio 1152, correctly named) and 84f548ceadd8d4a0... (a DIFFERENT image, "
    "also called jimbo_p1152.png, correctly named, folio 1152). Six checks pass; "
    "two controls fire, including one requiring that the rule stated BACKWARDS "
    "is not matched.",
    "INSPECTED", "file_inspection",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt")

add("S48-03", "S48/LABEL-VS-BYTES",
    "A PROVEN claim in this corpus contains a formula that is WRONG AS WRITTEN. "
    "S16-R18-02 carries label PROVEN (read from its label field, at "
    "CT-S16-MEMBERSHIP-C/claims.jsonl line 24) and its claim text states one "
    "quantity twice: the unfactored z(4pqt - 4pq - 4pt + 4p + q^3 t^2 - q^3 - "
    "2 q^2 t^2 + 2 q^2 + q t^2 - q)/4, which is correct, and the factored "
    "-z(q-1)(t-1)(4p + q^2 t + q^2 - qt - q)/4, which is not: the two differ by "
    "exactly a sign, and CT-S47's check_r18_sign.py reports 'the claim's own two "
    "forms agree: False' and 'PLUS one quarter of the same product reproduces "
    "it: True'. Both forms are present in the claim text and both were read from "
    "it (checks R4-b, R4-c), so this is a defect in the RECORD, not only in "
    "appendixA.tex's typeset display. The control R4c fires.",
    "INSPECTED", "file_inspection",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt")

add("S48-04", "S48/LABEL-SCOPE",
    "RULING, recorded: the label on S16-R18-02 stays PROVEN, and the reasoning "
    "is the substance. A label grades whether the RESULT is proved, not whether "
    "every transcription of it is typographically correct. S16-R18-02's "
    "unfactored form is right and its factored form wrong, so the proof stands "
    "and the artefact was defective; downgrading would assert that the "
    "mathematics was in doubt, which it was not. The general statement, which "
    "this pass is what found: A LABEL IS A VERDICT ON A RESULT; IT HAS NEVER "
    "BEEN A GUARANTEE ABOUT THE BYTES OF ITS STATEMENT. The correct instrument "
    "is therefore supersession, not relabelling -- S47-12 records the corrected "
    "display under supersedes: S16-R18-02 with the original standing unedited. "
    "This bears on how much a label can be asked to carry, and is the argument "
    "for the formula pass having existed at all: no label, at any strength, "
    "would have caught it.",
    "STRUCTURAL", "source",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt")

add("S48-05", "S48/FORMULA-PASS-CLOSED",
    "RULING, recorded: the formula pass is CLOSED. Twelve short route-S displays "
    "remain un-re-derived, each with a resolving corpus claim, in a paper whose "
    "two highest-risk displays -- eq:QC's 22/22/54/5 and section 5's exact q and "
    "p -- were both re-derived with the prediction made in advance of the "
    "instrument (PREREG F5 in CT-S46, PREREG section 5 in CT-S47). The residual "
    "risk is a reader-visible slip in a short expression, which an end-to-end "
    "human read covers better than a further instalment would. The scope of what "
    "is closed is stated exactly so that closure cannot later be read as a claim "
    "that every display was re-derived: 56 of 56 displays were ROUTED, 38 "
    "symbolic identities were checked at residual 0, and 12 displays were "
    "accepted on a resolving corpus claim without independent re-derivation.",
    "STRUCTURAL", "source",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt")

add("S48-06", "S48/NEEDLE-WRAP",
    "INSTRUMENT DEFECT, found and repaired in this session. Check R3-f -- 'the "
    "marker states the rule' -- FAILED on its first run against a marker that "
    "states the rule perfectly well. Cause: the needle was a literal "
    "single-space string, and the sentence 'Resolve these images by hash, never "
    "by filename.' is LINE-WRAPPED in the README between 'hash,' and 'never'. "
    "This is S43-12 recurring: a check that matches raw text with a "
    "single-space needle cannot see a phrase broken at a line end, and reports "
    "absence identical to the absence it exists to detect. Diagnosed against the "
    "raw file before anything was edited, so a correct marker was not 'repaired'. "
    "Fixed in the READER, by compiling each needle to a regex joining its "
    "whitespace-separated tokens with \\\\s+, and given a control requiring that "
    "the same wrap-tolerant needle does NOT match the rule stated BACKWARDS -- "
    "without which a needle loose enough to cross line breaks might be loose "
    "enough to match anything. Final state: 18 checks, 0 FAILED; 6 controls, 6 "
    "FIRED.",
    "VERIFIED", "control",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt")

add("S48-07", "S48/PREREG-PREDICTION",
    "The PREREG advance prediction was right in its location and wrong in its "
    "mechanism, and is recorded as such rather than quietly reconciled. PREREG "
    "section 5 predicted a clean run and named R3 as the most likely place to "
    "fail, because the marker records digests as 16-hex PREFIXES followed by an "
    "ellipsis and a reader comparing full 64-hex digests would report absence "
    "for a file the marker names. R3 is indeed where the run failed -- but at "
    "R3-f, on line wrapping, not at R3-c/d/e on digest width; the prefix "
    "comparison had been built as the PREREG said it would be and passed. A "
    "prediction that names the right block for the wrong reason is a partial "
    "hit, and calling it a hit would overstate what foresight bought.",
    "STRUCTURAL", "source",
    "scripts/check_rulings.py", "outputs/check_rulings.out.txt")

# ----------------------------------------------------------------------
# Validate the BUFFER, before anything is written.
# ----------------------------------------------------------------------
LABELS = {"PROVEN", "VERIFIED", "INSPECTED", "STRUCTURAL", "CONJECTURED"}
problems = []


def bad(cid, why):
    problems.append("%s: %s" % (cid, why))


seen = set()
for d in C:
    cid = d["claim_id"]
    if cid in seen:
        bad(cid, "duplicate claim id")
    seen.add(cid)
    if d["label"] not in LABELS:
        bad(cid, "label %r is not one of the five" % d["label"])
    if not d["claim"].strip():
        bad(cid, "empty claim text")
    if len(d["claim"].strip()) < 80:
        bad(cid, "claim text is too short to carry evidence")
    p = HERE / d["_outfile"]
    if not p.exists():
        bad(cid, "evidence file does not exist: %s" % d["_outfile"])
    if not (HERE / d["script"]).exists():
        bad(cid, "script does not exist: %s" % d["script"])

if problems:
    print("REFUSED before writing:")
    for s in problems:
        print("  " + s)
    sys.exit(2)

# ---- anchored figures: number AND anchor must share a line -----------
ANCHORED = [
    ("S48-01", ROUTE, "36 checks, 0 DIFFER", "ROUTE S"),
    ("S48-01", ROUTE, "af25048b9b62a6f4", "section5.tex"),
    ("S48-02", RULINGS, "05fecc96632ca6d4", "jimbo_p1152.png"),
    ("S48-02", RULINGS, "42fffb7b09ff60b5", "jimbo_printed1152.png"),
    ("S48-02", RULINGS, "84f548ceadd8d4a0", "coldpackets"),
    ("S48-03", RULINGS, "PROVEN", "R4-a"),
    ("S48-06", RULINGS, "18 checks, 0 FAILED", "RULINGS CHECK"),
    ("S48-06", RULINGS, "6 controls, 6 FIRED", "RULINGS CHECK"),
]
for cid, path, fig, anchor in ANCHORED:
    if not path.exists():
        bad(cid, "anchored-figure evidence file missing: %s" % path)
        continue
    hit = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if fig in raw and anchor in raw:
            hit = raw.strip()
            break
    if hit is None:
        bad(cid, "figure %r does not appear on any line of %s carrying the "
                 "anchor %r" % (fig, path.name, anchor))

# ---- positive control on the anchored-figure rule itself -------------
ctrl_hit = any(("99 checks, 0 FAILED" in raw and "RULINGS CHECK" in raw)
               for raw in RULINGS.read_text(encoding="utf-8").splitlines())
if ctrl_hit:
    bad("CONTROL", "the anchored-figure reader matched a figure that is not "
                   "in the file; it is not discriminating")

if problems:
    print("REFUSED before writing:")
    for s in problems:
        print("  " + s)
    sys.exit(2)

# ---- output hashes, recomputed from the files ------------------------
for d in C:
    d["output_hash"] = hashlib.sha256(
        (HERE / d["_outfile"]).read_bytes()).hexdigest()
    if not re.fullmatch(r"[0-9a-f]{64}", d["output_hash"]):
        bad(d["claim_id"], "output_hash is not 64 hex")

if problems:
    print("REFUSED before writing:")
    for s in problems:
        print("  " + s)
    sys.exit(2)

buf = "\n".join(
    json.dumps({k: v for k, v in d.items() if k != "_outfile"},
               ensure_ascii=False) for d in C) + "\n"

# the buffer itself must parse, one claim per line, before it reaches disk
for i, ln in enumerate(buf.strip().splitlines(), 1):
    obj = json.loads(ln)
    if obj["claim_id"] != C[i - 1]["claim_id"]:
        print("REFUSED: buffer line %d is not the claim it should be" % i)
        sys.exit(2)

DEST.write_text(buf, encoding="utf-8")
print("wrote claims.jsonl: %d claims, sha256 %s"
      % (len(C), hashlib.sha256(DEST.read_bytes()).hexdigest()))
for d in C:
    print("  %-7s %-11s %-22s%s"
          % (d["claim_id"], d["label"], d["task_id"].split("/")[-1],
             "  supersedes " + d["supersedes"] if "supersedes" in d else ""))
