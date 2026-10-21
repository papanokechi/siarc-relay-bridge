"""R12: apply operator review #9's wording ruling to the claim record, and add
the claims arising from this round. Aborts on claim_id collision (R1-85).
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
CJ = HERE / "claims.jsonl"


def sha(p):
    p = pathlib.Path(p)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


NUM = sha(HERE / "verify_s14_numeric.out.txt")

# --- 1. wording correction: "same object" is too strong ---------------------
OLD = "Objects B and C are therefore the same object in different presentations."
NEW_TXT = ("Objects B and C are therefore PROJECTIVELY EQUIVALENT under z -> 1/z: related by that "
           "change of variable together with a scalar (rank-1) gauge transformation. They are NOT "
           "the same operator - their printed forms differ by the twist A^(-1/2), which alters the "
           "trace. The phrase 'the same object' was too strong and has been withdrawn.")

lines, patched = [], 0
rec = {}
for line in CJ.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    c = json.loads(line)
    if c["claim_id"] == "R1-82" and OLD in c["claim"]:
        c["claim"] = c["claim"].replace(OLD, NEW_TXT)
        patched += 1
    rec[c["claim_id"]] = c
    lines.append(c)

print(f"patched {patched} claim(s) for the projective-equivalence wording")

NEW = [
    dict(claim_id="R1-86", task_id="R12-NUMERIC",
         claim="Numeric confirmation of the B-C normal-form identity at dps=60 over 8 sample points "
               "(real and complex, including x=1/1000 and x=7): worst relative residual 1.5558e-61, "
               "threshold 1e-50, PASS. The root correspondence under x=1/z has |diff| exactly 0.0 at "
               "50 digits. This supplies the numeric half required by the P0 symbolic-equality rule.",
         label="VERIFIED", evidence_type="computation", dps=60, reproducible=True,
         script="verify_s14_numeric.py", output_hash=NUM,
         review="self", review_note="numeric half of a claim whose symbolic half is cold (R1-82)."),
    dict(claim_id="R1-87", task_id="R12-WORDING",
         claim="WORDING CORRECTION under operator review #9: 'B and C are the same object' is too "
               "strong for a notice about loose identity claims. What was shown is identical "
               "trace-free normal forms under z -> 1/z, i.e. PROJECTIVE EQUIVALENCE (change of "
               "variable plus rank-1 gauge). The printed operators differ by a trace-altering twist, "
               "so they are not the same operator. Notice and claim text updated.",
         label="STRUCTURAL", evidence_type="proof", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=sha(HERE / "verify_s14.out.txt"),
         review="self", review_note="operator-supplied correction, adopted; it tightens a label rather "
                                    "than changing a computation."),
    dict(claim_id="R1-88", task_id="R12-WORDING",
         claim="The three object names form TWO equivalence classes, not three unrelated objects: "
               "object A (what Channel Theory computes on) and the class {B, C}. The conflation C4 "
               "corrects is precisely between A and the {B,C} class, which is the one the Dtilde5 "
               "label fits. This sharpens C4 rather than weakening it.",
         label="STRUCTURAL", evidence_type="proof", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=sha(HERE / "verify_s14.out.txt"),
         review="self", review_note="follows from R1-82 (cold) plus the distinctness of A's Katz type."),
    dict(claim_id="R1-89", task_id="R12-OPENQ",
         claim="RECORDED AS FUTURE PROBLEM, NOT A RESULT: because B and C are projectively equivalent "
               "under z -> 1/z, the isomonodromic embedding question need be posed only once; a "
               "deformation built for either, transported by the equivalence, settles the other. This "
               "reduces two open questions to one but does not make the remaining one easier, since a "
               "deformation must still be written down. Anyone attempting the transport must check "
               "that z -> 1/z carries C's time t = -+2i*sqrt(33)/9 to a consistent time for B. That "
               "check has NOT been performed.",
         label="CONJECTURED", evidence_type="proof", dps=None, reproducible=True,
         script=None, output_hash=None,
         review="self", review_note="recorded as an open problem; no weight rests on it."),
    dict(claim_id="R1-90", task_id="R12-LOADBEARING",
         claim="LOAD-BEARING TEST applied to the three deferred claims (operator ruling, review #9). "
               "R1-56 is LOAD-BEARING: C4 point 7 exists only to state it, and no other notice content "
               "supplies it, so it was sent for cold read. CT-S9-PVPARAMS-C014 is CORROBORATING ONLY: "
               "the notice asserts OPENNESS, which its falsity would not contradict, and C3's "
               "fixed-time sentence rests on the separately-cold affine computation. R1-57 is "
               "CORROBORATING ONLY: it is CONJECTURED on the face of the notice.",
         label="STRUCTURAL", evidence_type="proof", dps=None, reproducible=True,
         script="LOADBEARING-TEST.md", output_hash=sha(HERE / "LOADBEARING-TEST.md"),
         review="self", review_note="reasoning recorded in full in LOADBEARING-TEST.md for checking."),
    dict(claim_id="R1-91", task_id="R12-PACKET",
         claim="PACKET-E-deferred.md dispatched as CT-S15-COLDREAD-DEFERRED, carrying both R1-56 "
               "(statement 1) and CT-S9-PVPARAMS-C014 (statement 2) per the operator's ruling that if "
               "either needs a cold read, both go in one packet. Sources provided: vdps p2634/p2635, "
               "jimbo p1152, companion v1.2 p2/p3, all as page images. R1-57 was not sent.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script=None, output_hash=sha(HERE / "coldpackets" / "PACKET-E-deferred.md"),
         review="self", review_note="dispatch record."),
]

collide = [c["claim_id"] for c in NEW if c["claim_id"] in rec]
if collide:
    sys.exit(f"ABORT: claim_id collision, nothing written: {collide}")

out = [json.dumps(c, ensure_ascii=False) for c in lines]
out += [json.dumps(c, ensure_ascii=False) for c in NEW]
CJ.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"appended {len(NEW)} claims: {[c['claim_id'] for c in NEW]}")
print(f"in: {len(lines)}   out: {len(out)}   (delta {len(out) - len(lines)}, expected {len(NEW)})")
assert len(out) - len(lines) == len(NEW), "count mismatch"
