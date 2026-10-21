#!/usr/bin/env python3
"""CT-S59: emit claims.jsonl.  Validates the in-memory buffer BEFORE writing,
and appends nothing it cannot re-derive from a hashed output file on disk.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTD = SESS / "outputs"
ART = SESS / "claims.jsonl"
TASK = "CT-S59-JDE-THM61"

THM = OUTD / "check_thm61.out.txt"
LOGC = OUTD / "check_log_status.out.txt"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fail(msg):
    print(f"REFUSED: {msg}")
    sys.exit(2)


for p in (THM, LOGC):
    if not p.exists():
        fail(f"missing cited output {p.name}; run its script first")

thm_txt = THM.read_text(encoding="utf-8")
log_txt = LOGC.read_text(encoding="utf-8")
H_THM, H_LOG = sha(THM), sha(LOGC)

C = []


def add(cid, claim, out, h, evidence, script):
    C.append({
        "claim_id": cid, "task_id": TASK, "claim": claim, "label": "INSPECTED",
        "evidence_type": "file_inspection", "dps": None, "reproducible": True,
        "script": f"scripts/{script}", "output_file": f"outputs/{out}",
        "output_hash": h, "evidence": evidence,
    })


T, L = "check_thm61.py", "check_log_status.py"
O_T, O_L = THM.name, LOGC.name

add("S59-01",
    "In the as-submitted build of 'Self-Adjoint Structure of Polynomial Continued "
    "Fraction Recurrences and its Arithmetic Consequences' (PDF md5 "
    "75ee5c4fcc3dc21668794d02daa23a93; TeX sha256 bb392b76...9153), Theorem 6.1 is "
    "'Poincare-Perron, simplified form', stated for y_{n+1}=a_n y_n + b_n y_{n-1} "
    "with the explicit hypothesis a_n -> a and b_n -> b as n -> infinity.",
    O_T, H_THM, "resolved in the RENDERED PDF, not inferred from LaTeX counters", T)

add("S59-02",
    "The paper does not apply Theorem 6.1 to the PCF/Wallis recurrence. The "
    "paragraph immediately following it states that because b(n) = alpha_d n^d + ... "
    "grows polynomially, 'the Poincare-Perron theorem does not apply directly (it "
    "requires convergent coefficients)'. Present once in the TeX source and once in "
    "the render.",
    O_T, H_THM,
    "the render drops the ffi ligature ('coe cients'), so the reason was matched "
    "with a ligature-tolerant pattern carrying its own firing control",
    T)

add("S59-03",
    "thm:poincare-perron is cross-referenced 0 times anywhere in the source: no "
    "proof step invokes it. Section 6 ('Relation to Classical Asymptotic Theory') "
    "delineates what is classical from what is new; it proves nothing.",
    O_T, H_THM, "0 matches for \\Cref/\\ref/\\autoref to the label", T)

add("S59-04",
    "VERDICT on the operator's question: Theorem 6.1 is NOT a misapplied theorem. "
    "The conditional 'if Theorem 6.1 applies Poincare-Perron directly to an "
    "un-normalised PCF recurrence' does not hold, so the branch under which it "
    "would warrant telling an editor does not fire.",
    O_T, H_THM, "follows from S59-01..03 read off the same hashed output", T)

add("S59-05",
    "The Perron-Kreuser theorem is named in the paper but Kreuser has no "
    "bibliography entry: 0 \\bibitem keys match /[Kk]reuser/.",
    O_T, H_THM, "detector shown to separate present from absent on /[Pp]erron/", T)

add("S59-06",
    "The single key Perron21 = O. Perron, 'Ueber Summengleichungen und Poincaresche "
    "Differenzengleichungen', Math. Ann. 84 (1921), 1-15, is cited for BOTH the "
    "Poincare-Perron theorem and the Perron-Kreuser theorem. Perron-Kreuser proper "
    "is Perron, Acta Math. 34 (1911), plus Kreuser 1914.",
    O_T, H_THM,
    "the 1911/1914 attribution is from Gautschi 1967, Thm 2.3 (p.12) and its "
    "bibliography (p.58), read in a prior run; not re-verified here",
    T)

add("S59-07",
    "Gautschi (1967) is not cited by this paper: 0 \\bibitem keys match "
    "/[Gg]autschi/. Gautschi's Theorem 2.3(a), case sigma = d > tau = -d, gives "
    "Q_{n+1}/Q_n ~ b(n) directly and is the clean route to the sentence the paper "
    "currently sources to Perron21 + Elaydi Ch. 8.",
    O_T, H_THM, "same absent-bibitem detector as S59-05", T)

add("S59-08",
    "The paper cites Birkhoff-Trjitzinsky, 'Analytic theory of singular difference "
    "equations', as Acta Math. 60 (1932), 1-89. This matches the scan's own imprint "
    "rather than the commonly quoted 1933 and is recorded here as DELIBERATE, so "
    "that a later citation pass does not 'correct' it.",
    O_T, H_THM, "bibitem regex resolves, with a firing control", T)

add("S59-09",
    "The premise that this is a paper currently under review at the Journal of "
    "Differential Equations is FALSE. submission_log.txt records submission "
    "JDEQ26-983 as REJECTED 2026-05-27 by Qiudong Wang, Handling Editor, at initial "
    "screening before refereeing, with no referee reports.",
    O_L, H_LOG, "entry resolved by submission ID, not by item number or position", L)

add("S59-10",
    "The same submission_log.txt entry is internally inconsistent: its 'Status:' "
    "line still reads 'Submitted to Journal of Differential Equations (active "
    "review)' while its 'Verdict:' line records the 2026-05-27 rejection. A reader "
    "who stops at Status gets the wrong answer. NOT REPAIRED in this session: the "
    "log is an operator-owned record outside the session tree.",
    O_L, H_LOG, "stale-status detector shown able to report clean", L)

# ---------------------------------------------------------- validate BEFORE write
ids = [c["claim_id"] for c in C]
if len(set(ids)) != len(ids):
    fail("duplicate claim_id in buffer")
if ART.exists():
    existing = {json.loads(l)["claim_id"] for l in ART.read_text(encoding="utf-8").splitlines() if l.strip()}
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
        fail(f"{c['claim_id']}: cited output {c['output_file']} absent")
    # re-hash from disk, independently of the values computed above
    if c["output_hash"] != hashlib.sha256(src.read_bytes()).hexdigest():
        fail(f"{c['claim_id']}: output_hash does not match {c['output_file']} on disk")
    if (HERE / Path(c["script"]).name).exists() is False:
        fail(f"{c['claim_id']}: script {c['script']} absent")

# every claim must be supported by a string actually present in its cited output
support = {
    "S59-01": ("Theorem 6.1 = (Poincar", thm_txt),
    "S59-02": ("does not apply directly", thm_txt),
    "S59-03": ("thm:poincare-perron      : 0", thm_txt),
    "S59-04": ("NOT MISAPPLIED", thm_txt),
    "S59-05": ("bibitem for Kreuser            : False", thm_txt),
    "S59-06": ("Perron21", thm_txt),
    "S59-07": ("bibitem for Gautschi           : False", thm_txt),
    "S59-08": ("Acta Math. 60 (1932)", thm_txt),
    "S59-09": ("PREMISE FALSE", log_txt),
    "S59-10": ("stale relative to Verdict: True", log_txt),
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
