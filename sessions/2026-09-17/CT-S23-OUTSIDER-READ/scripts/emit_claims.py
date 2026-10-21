"""CT-S23-OUTSIDER-READ - emit claims.jsonl with hashes read from disk.

Hashes are computed from the output files, never typed. The script reads back
what it wrote and re-verifies every hash against disk before exiting.
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
OUTS = HERE / "outputs"
DEST = HERE / "claims.jsonl"

IDX = "jargon_index.out.txt"
ADJ = "adjudicate.out.txt"
MAIN = "coldread_main.txt"
CTRL = "coldread_control.txt"


def sha(name):
    p = OUTS / name
    if not p.exists():
        raise SystemExit("missing output file: %s" % p)
    return hashlib.sha256(p.read_bytes()).hexdigest()


C = [
    ("S23-01", "assembly",
     "The packet named as PROVIDED in the task did not exist: there is no paper "
     "draft and no assembled packet file in the repository. All five named "
     "sources and all named page images do exist, so this is a mis-description "
     "of state rather than missing data. The packet was assembled in this "
     "session as packet/PACKET.md (30002 chars).",
     "INSPECTED", "file_inspection", None, "scripts/jargon_index.py", IDX),

    ("S23-02", "method",
     "The assembling agent holds all five source sessions in context and "
     "therefore cannot serve as the cold reader: a self-containment audit run "
     "by a reader able to supply the missing definitions from memory cannot "
     "detect the defect it is looking for. The read was dispatched to two "
     "separate contexts given only a packet path and instructed to read no "
     "other file.",
     "STRUCTURAL", "file_inspection", None, "scripts/adjudicate.py", ADJ),

    ("S23-03", "control",
     "The first-use classifier control FAILED on its initial run and halted "
     "before emitting G. The sentinel, not the classifier, was wrong: 'normal "
     "potential' is first used in packet section 2 and only explained in "
     "section 3, so UNDEFINED was the correct verdict. Replaced by four "
     "synthetic arms plus two hand-adjudicated live arms; all six pass.",
     "PROVEN", "computation", None, "scripts/jargon_index.py", IDX),

    ("S23-04", "index",
     "Mechanical first-use index over PACKET.md, with a degeneracy pre-check on "
     "the core term set itself (399 candidate alias pairs tested, none found): "
     "G = {System C, K, Katz multiset, PV, D5-tilde} used before defined; 13 "
     "terms defined; and V_quad, Channel Theory, PCF and the tr(B_i B_j) trace "
     "definition ABSENT from the packet entirely. Computed and hashed before "
     "either read was dispatched.",
     "VERIFIED", "computation", None, "scripts/jargon_index.py", IDX),

    ("S23-05", "instrument",
     "PREREG falsifier F1 did not fire: the control reader returned NOT "
     "SELF-CONTAINED with 106 task-2 items, against a threshold of 5. The "
     "instrument discriminates.",
     "VERIFIED", "computation", None, "scripts/adjudicate.py", ADJ),

    ("S23-06", "instrument",
     "PREREG falsifier F2 did not fire: the main read's task-2 list contains "
     "all 5 members of G, |T2 n G| / |G| = 5/5 = 1.00 against a threshold of "
     "0.50. The main read is not low-sensitivity and its content is admissible.",
     "VERIFIED", "computation", None, "scripts/adjudicate.py", ADJ),

    ("S23-07", "prereg-defect",
     "PREREG section 4 vacuity arm (i) FIRED: both reads returned NOT "
     "SELF-CONTAINED. The arm was written assuming the packet would return "
     "SELF-CONTAINED and encoded 'different verdicts' as the signal that the "
     "instrument reads its input; it cannot distinguish an insensitive "
     "instrument from two documents that are both genuinely not self-contained. "
     "It is ILL-POSED as written. Reported as a finding and NOT rewritten; the "
     "surviving discrimination evidence is F1 and F2.",
     "PROVEN", "computation", None, "scripts/adjudicate.py", ADJ),

    ("S23-08", "return",
     "The cold reader returned NOT SELF-CONTAINED on the assembled packet, with "
     "171 task-2 items and 31 externally-resting claims. The verdict is "
     "recorded with the qualification that PREREG arm (i) fired.",
     "INSPECTED", "file_inspection", None, "scripts/adjudicate.py", MAIN),

    ("S23-09", "return",
     "The cold reader reconstructed the main result and the nine-step method "
     "CORRECTLY from the packet alone, including the (P,Q) step as what removes "
     "the rank-1-twist ambiguity, the convention test as overdetermined, and the "
     "precision-not-proof limit. Followability and self-containment came apart: "
     "the reader could follow the argument end to end and still could not "
     "reproduce it without the cited source.",
     "INSPECTED", "file_inspection", None, "scripts/adjudicate.py", MAIN),

    ("S23-10", "assembly-defect",
     "The cold reader found a real defect introduced in assembly: the packet "
     "labels its hypotheses (A1) and (A3) with (A2) absent and never explained. "
     "The source CT-S3B-RINF/DERIVATION.md carries three, (A2) being 'no root "
     "r_i is a positive integer', which is exactly what makes Gamma(1-r_i) "
     "finite and K well-defined. The packet's (A1) silently conflates the "
     "source's (A1) and (A2) and leaves the label (A3) dangling.",
     "INSPECTED", "file_inspection", None, "scripts/adjudicate.py", MAIN),

    ("S23-11", "notation",
     "The cold reader found a notation collision present in the source material, "
     "not introduced in assembly: r_n (the normalised sequence), r_1..r_d (the "
     "roots of b) and r_inf (the limit) share a letter, and the PSLQ basis entry "
     "'r_1' is ambiguous between the first root and the first sequence term.",
     "INSPECTED", "file_inspection", None, "scripts/adjudicate.py", MAIN),
]


def main():
    lines = []
    for cid, task, claim, label, ev, dps, script, out in C:
        rec = {
            "claim_id": cid,
            "task_id": "CT-S23-OUTSIDER-READ/" + task,
            "claim": claim,
            "label": label,
            "evidence_type": ev,
            "dps": dps,
            "reproducible": True,
            "script": script,
            "output_hash": sha(out),
        }
        lines.append(json.dumps(rec, ensure_ascii=True))
    DEST.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # read back and re-verify every hash against disk
    back = [json.loads(l) for l in
            DEST.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(back) == len(C), "readback count mismatch"
    ids = [r["claim_id"] for r in back]
    assert len(set(ids)) == len(ids), "duplicate claim ids"
    want = {cid: sha(out) for cid, _, _, _, _, _, _, out in C}
    for r in back:
        assert r["output_hash"] == want[r["claim_id"]], \
            "stale hash on %s" % r["claim_id"]
        assert r["label"] in ("PROVEN", "VERIFIED", "STRUCTURAL",
                             "INSPECTED", "CONJECTURED"), \
            "bad label on %s: %r" % (r["claim_id"], r["label"])
    print("wrote %d claims to %s" % (len(back), DEST.name))
    for r in back:
        print("  %-8s %-11s %s" % (r["claim_id"], r["label"],
                                   r["claim"][:64] + "..."))
    print("\nreadback OK: %d claims, ids unique, all hashes match disk"
          % len(back))
    return 0


if __name__ == "__main__":
    sys.exit(main())
