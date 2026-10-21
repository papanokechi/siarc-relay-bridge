"""CT-S16 - append the review-#13 follow-up claims.

Append path rules (R11 lesson): abort on a duplicate id, never skip; report
counts in and out and check them.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "claims.jsonl")


def sha256(rel):
    p = os.path.join(HERE, rel)
    if not os.path.isfile(p):
        sys.exit("MISSING FILE, aborting: " + rel)
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


existing = [json.loads(l) for l in open(PATH, encoding="utf-8")]
before = len(existing)
have = {c["claim_id"] for c in existing}

NEW = []


def add(cid, task, claim, label, ev, script, out, review, note, dps=None):
    NEW.append(dict(claim_id=cid, task_id=task, claim=claim, label=label,
                    evidence_type=ev, dps=dps, reproducible=True, script=script,
                    output_hash=sha256(out), review=review, review_note=note))


add("S16-18", "S16-TYPO-RECHECK",
    "TYPO RE-VERIFIED BY LOOKING, as review #13 required. The b(z) entry of van der "
    "Put-Saito's family is on journal page 2655, confirmed from the running head, and "
    "its first term prints (p + (1/2)(q-1)q)^2 with NO t, while the second term carries "
    "(q-1)q t twice. The original transcription was correct. Also read from the same "
    "display: c(z) = -(z-q)/(q-1), hence c(0) = q/(q-1); a(z) = p + (1/2)(-2qt + t - "
    "theta_inf)(z-q) - (1/2)t(z-q)^2; 'q is the unique zero of c(z) and p = a(q)'; and "
    "'(p,q) gives canonical coordinates on an affine Zariski open set U_0 = C x "
    "(C\\{0,1}) of the moduli space M_{t,lambda}'.",
    "INSPECTED", "file_inspection", None,
    "pages/vdps_j2655_bz_LOOK.png", "self",
    "8x crop of journal p.2655 viewed alone in one message; header asserted in the "
    "rendering script before the crop was saved.")

add("S16-19", "S16-TYPO-RECHECK",
    "THE TYPO IS PRESENT IN THE AUTHORS' LATEST CORRECTED VERSION TOO. arXiv:0902.1702 "
    "v5, p.34, prints the identical first term (p + (1/2)(q-1)q)^2 with no t. The v5 "
    "comment records that 'the signs for Hamiltonian systems in Section 4 and the "
    "equations (3) (PV) and (7) (degenerate PV) are corrected', so Section 4 WAS revised "
    "and this entry was not among the corrections. A web check found no published "
    "erratum or corrigendum in Annales de l'Institut Fourier.",
    "INSPECTED", "file_inspection", None,
    "pages/arxiv_v5_p34_bz_LOOK.png", "self",
    "arXiv v5 downloaded (sha256 1d4be8e4526f6ca834506a976a6ffc999e9659acc2da08753b87e"
    "1f59d006e47) and the display viewed directly.")

add("S16-20", "S16-TYPO-RECHECK",
    "DISCRIMINATING TEST, re-run with a control. Since A(z) = z(z-1)A_inf + (z-1)A_0 + "
    "z A_1, the paper's own constraints det A_i = -theta_i^2/4 read det A(0) = "
    "-theta_0^2/4 and det A(1) = -theta_1^2/4. det A(0) holds identically for BOTH "
    "readings, so it does not discriminate. det A(1) holds IDENTICALLY for the "
    "corrected reading (p + (1/2)(q-1)q t)^2, and for the printed reading leaves the "
    "residual -(q-1)(t-1)(4p + q^2 t + q^2 - q t - q)/4, which is non-zero at the exact "
    "rational point p=2/7, q=5/3, t=11/4, theta_0=theta_1=0, theta_inf=3/5, where it "
    "equals -223/144. A deliberately bogus variant (q-1)q t^2 is REJECTED by the same "
    "test, so the test discriminates rather than accepting anything.",
    "VERIFIED", "computation", "typo_recheck.py",
    "outputs/typo_recheck.out.txt", "self",
    "control is an assertion; formulas transcribed from the two page images.", dps=0)

add("S16-21", "S16-TYPO-RECHECK",
    "CORROBORATING STRUCTURE: the printed reading's residual carries the factor (t-1) "
    "and so vanishes precisely at t = 1 - which is exactly the value at which the two "
    "readings coincide, since (q-1)q*1 = (q-1)q. A dropped factor of t produces exactly "
    "this signature. This is corroboration for the typo diagnosis, not independent "
    "proof of it.",
    "VERIFIED", "computation", "typo_recheck.py",
    "outputs/typo_recheck.out.txt", "self",
    "read off from the factored residual; labelled as corroboration, not proof.", dps=0)

add("S16-22", "S16-METHOD",
    "PAGE-OFFSET AUDIT, prompted by a naming slip in an ad-hoc crop script written this "
    "round. The correct relation is journal page = 0-based PDF index + 2610, "
    "equivalently = 1-based PDF page + 2609. render_pages.py used doc[p-1] with 1-based "
    "p and the +2609 offset, so ALL page images it produced are correctly named and "
    "every page citation in the CT-S16 claims stands. Two ad-hoc crops written this "
    "round used doc[jp-2609], indexing 0-based against a 1-based offset, and were "
    "therefore one page late; they were deleted rather than renamed. Verified by "
    "reading the printed running head of every candidate page.",
    "VERIFIED", "computation", None,
    "outputs/typo_recheck.out.txt", "self",
    "caught because the rendered header did not match the filename; the primary "
    "renderer was then audited rather than assumed correct.", dps=0)

dups = [c["claim_id"] for c in NEW if c["claim_id"] in have]
if dups:
    sys.exit("DUPLICATE IDS, ABORTING (not skipping): " + ", ".join(dups))

with open(PATH, "a", encoding="utf-8") as fh:
    for c in NEW:
        fh.write(json.dumps(c, ensure_ascii=False) + "\n")

after = sum(1 for _ in open(PATH, encoding="utf-8"))
print("claims before :", before)
print("claims to add :", len(NEW))
print("claims after  :", after)
assert after == before + len(NEW), "APPEND-PATH FAILURE: counts do not reconcile"
ids = [json.loads(l)["claim_id"] for l in open(PATH, encoding="utf-8")]
assert len(set(ids)) == len(ids), "DUPLICATE CLAIM ID IN FILE"
print("all ids unique:", True)
