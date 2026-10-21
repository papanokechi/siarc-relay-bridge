#!/usr/bin/env python3
"""CT-S60: emit claims.jsonl.  Validates in memory before writing; appends only."""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTD = SESS / "outputs"
ART = SESS / "claims.jsonl"
TASK = "CT-S60-LOG-STATUS-SWEEP"

SW = OUTD / "sweep_status_verdict.out.txt"
AC = OUTD / "check_active_counts.out.txt"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fail(msg):
    print(f"REFUSED: {msg}")
    sys.exit(2)


for p in (SW, AC):
    if not p.exists():
        fail(f"missing cited output {p.name}; run its script first")

sw_txt, ac_txt = SW.read_text(encoding="utf-8"), AC.read_text(encoding="utf-8")
H_SW, H_AC = sha(SW), sha(AC)

C = []


def add(cid, claim, out, h, evidence, script):
    C.append({
        "claim_id": cid, "task_id": TASK, "claim": claim, "label": "INSPECTED",
        "evidence_type": "file_inspection", "dps": None, "reproducible": True,
        "script": f"scripts/{script}", "output_file": f"outputs/{out}",
        "output_hash": h, "evidence": evidence,
    })


S, A = "sweep_status_verdict.py", "check_active_counts.py"

add("S60-01",
    "Section A of submission_log.txt (sha256 70f814b9...29897433) contains 42 "
    "items, numbered 1..42, each bounded at the next item's start and at the "
    "section separator.",
    SW.name, H_SW,
    "span bounding follows the log's own 2026-08-29 note; controls confirm no "
    "item absorbs the next and the final item does not absorb the trailing block",
    S)

add("S60-02",
    "EXACTLY TWO section-A items assert liveness in their Status line while "
    "carrying a terminal Verdict: Item 13 (JDEQ26-983, Journal of Differential "
    "Equations) and Item 26 (JSCO-D-26-00112, Journal of Symbolic Computation). "
    "These are the full extent of the Status/Verdict contradiction class.",
    SW.name, H_SW,
    "Item 13 served as a positive control with ground truth established in "
    "CT-S59; Item 26 was found, not assumed",
    S)

add("S60-03",
    "Item 26's Status reads 'With Editor at Journal of Symbolic Computation "
    "(Elsevier; double-blind; active review) - Editor-in-Chief Dr. Josef Schicho "
    "assigned as handling editor 2026-05-19' while its Verdict records 'REJECTED "
    "2026-06-15 by Josef Schicho, Editor-in-Chief, after peer review'. Unlike "
    "Item 13 this one WAS refereed, so the rejection carries scientific signal.",
    SW.name, H_SW, "read off the same hashed sweep output", S)

add("S60-04",
    "Neither Item 34 nor Item 35 is in the contradiction class. Item 34 (The "
    "(4,3)-(5,3) Desert Conjecture) classifies TERMINAL x TERMINAL; Item 35 "
    "(JMP26-AR-01521, The WKB Geometry of Newton Polygons) classifies VENUE x "
    "TERMINAL. The conjecture that the JMP entry 'has the same shape' as Item 13 "
    "is not borne out.",
    SW.name, H_SW,
    "a negative result about specifically named items, reported because it was "
    "specifically predicted",
    S)

add("S60-11",
    "CORRECTION, superseding CT-S60's own draft and CT-S59/REPORT.md section 6 "
    "item 1: the JMP submission is section-A Item 35, NOT Item 34. Item 34 is the "
    "Desert Conjecture paper. CT-S59 asserted 'Item 34 (JMP)' because it read a "
    "grep hit by line proximity rather than resolving the entry's own span. Same "
    "class as the defect this session exists to find: a record identified by "
    "location rather than by content.",
    SW.name, H_SW,
    "the sweep resolves each item by its own '<n>. Filename:' span; Item 35 "
    "carries Submission ID JMP26-AR-01521. CT-S59's REPORT.md is left unedited "
    "per append-only discipline; this claim supersedes it.",
    S)

add("S60-05",
    "16 further section-A items pair a venue-naming Status ('Submitted to <venue>') "
    "with a terminal Verdict. These are NOT contradictions: Status there names the "
    "venue, not the liveness. Flagging them would have produced 16 false positives "
    "and buried the 2 real ones.",
    SW.name, H_SW,
    "the three-valued Status classification exists precisely to separate these "
    "two cells; both cells are reported so the judgement is visible",
    S)

add("S60-06",
    "Item 42 (MATH-D-26-00523, the live LMP submission) classifies LIVE x OPEN, "
    "i.e. consistent. The one entry that SHOULD read as live does.",
    SW.name, H_SW, "sanity check on the sweep, not a finding", S)

add("S60-07",
    "Three 'Active journal submissions' counts exist, at lines 1507, 2005 and "
    "2553. The two that enumerate items (lines 2005 and 2553) list items now "
    "carrying terminal verdicts: 5 of 5, and 3 of 3 respectively.",
    AC.name, H_AC, "counts located by regex with a separates-present-from-absent control", A)

add("S60-08",
    "Those counts are NOT defects. Each is a DATED SNAPSHOT (nearest dates "
    "2026-05-25 and 2026-05-26 respectively) and was true when written. The "
    "genuine hazard is different and weaker: no snapshot NEWER than 2026-05-26 "
    "exists, so a reader seeking the current active set finds a four-month-old "
    "one whose three entries have all since been rejected.",
    AC.name, H_AC,
    "the script's own section [2] date check is what prevents this being "
    "reported as a third contradiction; without it these would have been "
    "two invented defects",
    A)

add("S60-09",
    "Both contradictions share one origin: each Verdict line records "
    "'[CORRECTION RECORDED 2026-08-29 ...]', i.e. both were part of the same "
    "landed-but-not-recorded batch, and in both the correction was appended to "
    "Verdict without touching Status. This is one process gap, not two accidents.",
    SW.name, H_SW, "both Verdict lines carry the same 2026-08-29 correction marker", S)

add("S60-10",
    "NOT REPAIRED: no write of any kind was made to submission_log.txt. Both "
    "scripts are read-only and the file's sha256 is unchanged from the value "
    "read by CT-S59 (70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433).",
    SW.name, H_SW, "same digest observed by two sessions' scripts on separate runs", S)

# ---------------------------------------------------------- validate BEFORE write
ids = [c["claim_id"] for c in C]
if len(set(ids)) != len(ids):
    fail("duplicate claim_id in buffer")
if ART.exists():
    existing = {json.loads(l)["claim_id"]
                for l in ART.read_text(encoding="utf-8").splitlines() if l.strip()}
    clash = existing & set(ids)
    if clash:
        fail(f"claim_id(s) already recorded, refusing to rewrite: {sorted(clash)}")

for c in C:
    if c["label"] != "INSPECTED":
        fail(f"{c['claim_id']}: label must be INSPECTED")
    for k in ("claim", "evidence", "script", "output_file", "output_hash"):
        if not str(c[k]).strip():
            fail(f"{c['claim_id']}: empty {k}")
    src = OUTD / Path(c["output_file"]).name
    if not src.exists():
        fail(f"{c['claim_id']}: cited output absent")
    if c["output_hash"] != hashlib.sha256(src.read_bytes()).hexdigest():
        fail(f"{c['claim_id']}: output_hash does not match {c['output_file']} on disk")
    if not (HERE / Path(c["script"]).name).exists():
        fail(f"{c['claim_id']}: script {c['script']} absent")

support = {
    "S60-01": ("42 items, numbered 1..42", sw_txt),
    "S60-02": ("CONTRADICTIONS: 2", sw_txt),
    "S60-03": ("JSCO-D-26-00112", sw_txt),
    "S60-04": ("34  TERMINAL TERMINAL", sw_txt),
    "S60-05": ("VENUE x TERMINAL  =  16", sw_txt),
    "S60-06": ("42  LIVE     OPEN", sw_txt),
    "S60-07": ("line 2553: count = 3", ac_txt),
    "S60-08": ("2026-05-26", ac_txt),
    "S60-09": ("CORRECTION RECORDED 2026-08-29", sw_txt),
    "S60-10": ("NOT REPAIRED", sw_txt),
    "S60-11": ("35  VENUE    TERMINAL  JMP26-AR-01521", sw_txt),
}
for cid, (needle, hay) in support.items():
    if needle not in hay:
        fail(f"{cid}: supporting string {needle!r} not present in its cited output")
if set(support) != set(ids):
    fail("support table and claim set disagree")

with ART.open("a", encoding="utf-8", newline="\n") as fh:
    for c in C:
        fh.write(json.dumps(c, ensure_ascii=False) + "\n")

print(f"wrote {len(C)} claims -> {ART}")
print(f"claims.jsonl sha256 {sha(ART)}")
