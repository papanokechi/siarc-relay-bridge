"""R13: adopt CT-S15 claim by claim, promote the two cleared claims to cold,
and record the rejected transcriptions. Aborts on claim_id collision.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CJ = HERE / "claims.jsonl"


def sha(p):
    p = pathlib.Path(p)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


V15 = sha(HERE / "VERIFY-S15.md")

NEW = [
    dict(claim_id="R1-92", task_id="R13-S15",
         claim="van der Put-Saito p.2635, immediately after Table 2.1, reads verbatim: 'We will also "
               "describe the corresponding one-dimensional families of differential modules M(t).' "
               "Read directly from the page image vdps_p2635.png. This is DIRECT textual evidence that "
               "dim P = 0 does not negate a one-dimensional deformation direction, replacing the "
               "inference R1-56 previously rested on.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script=None, output_hash=sha(HERE / "coldpackets" / "vdps_p2635.png"),
         review="cold", review_note="located by CT-S15-COLDREAD-DEFERRED under isolation; re-read here "
                                    "directly from the page image, not from OCR."),
    dict(claim_id="R1-93", task_id="R13-S15",
         claim="WORDING REFINEMENT to R1-56, adopted from CT-S15: P should not be called simply 'the "
               "parameter space of the family'. Per p.2634 it is 'a space of parameters P (related to "
               "the parameters spaces of the Painleve equations) consisting of traces or eigenvalues of "
               "the matrices involved in the construction of R', and per p.2635 'R -> P is a family of "
               "affine cubic surfaces'. P is the base of a cubic-surface fibration on the MONODROMY side.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script=None, output_hash=sha(HERE / "coldpackets" / "vdps_p2634.png"),
         review="cold", review_note="both quotes re-read directly from the page images."),
    dict(claim_id="R1-94", task_id="R13-S15",
         claim="Table 2.1's r(t) column is a KATZ-INVARIANT column for a singular point named t, present "
               "only when the singular set contains one: the PVI row (0,0,0,0) has r(t)=0 with "
               "S={0,1,inf,t}, whereas the PIII(D8) row has r(t)='-'. The letter t does two different "
               "jobs on p.2635, which is the confusion R1-56 exists to prevent.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script=None, output_hash=sha(HERE / "coldpackets" / "vdps_p2635.png"),
         review="cold", review_note="read directly from the page image."),
    dict(claim_id="R1-95", task_id="R13-S15",
         claim="REJECTED TRANSCRIPTION from CT-S15: it rendered the constant matrix in Jimbo's (3.1) as "
               "'(1/2) sigma_3' = diag(1/2,-1/2). The printed page carries diag(1,0). These differ by "
               "the trace shift (1/2)I and are different matrices. Caused by OCR. Not adopted; the "
               "notice does not quote (3.1), so it did not propagate.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script=None, output_hash=sha(HERE / "coldpackets" / "jimbo_p1152.png"),
         review="self", review_note="rejection based on direct reading of jimbo_p1152.png."),
    dict(claim_id="R1-96", task_id="R13-S15",
         claim="REJECTED TRANSCRIPTION from CT-S15: it reported (A1)_PV as non-integrality of "
               "theta_infinity, theta_0 and theta_t. The printed line is exactly 'theta_0, theta_t not "
               "in Z'; theta_infinity does NOT appear. This is a LOAD-BEARING hypothesis for C2. Caused "
               "by OCR. Not adopted. The notice's own line 116 states it correctly and was verified "
               "earlier by direct reading, so it did not propagate.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script=None, output_hash=sha(HERE / "coldpackets" / "jimbo_p1152.png"),
         review="self", review_note="rejection based on direct reading of jimbo_p1152.png."),
    dict(claim_id="R1-97", task_id="R13-METHOD",
         claim="P0 AMENDMENT: a load-bearing statement is read by LOOKING at the rendered page. Machine "
               "transcription of a page image, OCR included, is a text layer and does not satisfy the "
               "citation rule. An agent that cannot view an image must HALT and report that rather than "
               "OCR the page and proceed. Evidence: CT-S15 was given page images, ran OCR, and produced "
               "two transcription errors, one of them on a load-bearing hypothesis - the Gautschi (2.8) "
               "near-miss repeating one review after that lesson was recorded.",
         label="STRUCTURAL", evidence_type="proof", dps=None, reproducible=True,
         script=None, output_hash=V15,
         review="self", review_note="method finding; reasoning in VERIFY-S15.md and P0-CITATION-RULE.md."),
    dict(claim_id="R1-98", task_id="R13-S15",
         claim="Statement 2 verdict ADOPTED (CT-S15: CORRECT). To be an instance of Jimbo (3.1) an "
               "object must supply A_0(t) and A_t(t) as explicit t-dependent matrices, the singular "
               "points x=0 and x=t, eigenvalue data +/- theta_nu/2, and crucially the SECOND equation "
               "dY/dt = -A_t(t)/(x-t) Y. Scalar local data - singular points, exponents, formal type - "
               "supply none of these. The reasoning is independent of the two rejected transcriptions.",
         label="STRUCTURAL", evidence_type="proof", dps=None, reproducible=True,
         script=None, output_hash=V15,
         review="cold", review_note="CT-S15 reached this under isolation; the argument does not depend "
                                    "on its two OCR defects."),
]

rec, lines = {}, []
for line in CJ.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    c = json.loads(line)
    rec[c["claim_id"]] = c
    lines.append(c)

collide = [c["claim_id"] for c in NEW if c["claim_id"] in rec]
if collide:
    sys.exit(f"ABORT: claim_id collision, nothing written: {collide}")

# --- promote R1-56, now cold-read ------------------------------------------
promoted = 0
for c in lines:
    if c["claim_id"] == "R1-56" and c.get("review") != "cold":
        c["review"] = "cold"
        c["review_note"] = ("cold-read by CT-S15-COLDREAD-DEFERRED, verdict CORRECT WITH WORDING "
                            "CHANGE; the wording refinement is adopted as R1-93 and the claim now rests "
                            "on the direct textual support of R1-92 rather than on an inference.")
        promoted += 1

out = [json.dumps(c, ensure_ascii=False) for c in lines]
out += [json.dumps(c, ensure_ascii=False) for c in NEW]
CJ.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"appended {len(NEW)} claims: {[c['claim_id'] for c in NEW]}")
print(f"promoted {promoted} claim(s) in this file to review=cold")
print(f"in: {len(lines)}   out: {len(out)}   (delta {len(out) - len(lines)}, expected {len(NEW)})")
assert len(out) - len(lines) == len(NEW), "count mismatch"

# --- promote CT-S9-PVPARAMS-C014 in its own session file -------------------
S9 = ROOT / "CT-S9-PVPARAMS" / "claims.jsonl"
s9_lines, s9_promoted = [], 0
for line in S9.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    c = json.loads(line)
    if c["claim_id"] == "CT-S9-PVPARAMS-C014" and c.get("review") != "cold":
        c["review"] = "cold"
        c["review_note"] = ("cold-read by CT-S15-COLDREAD-DEFERRED as statement 2, verdict CORRECT; "
                            "that reader had no access to this session's reasoning.")
        s9_promoted += 1
    s9_lines.append(json.dumps(c, ensure_ascii=False))
S9.write_text("\n".join(s9_lines) + "\n", encoding="utf-8")
print(f"promoted {s9_promoted} claim(s) in CT-S9-PVPARAMS/claims.jsonl to review=cold")
