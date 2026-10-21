#!/usr/bin/env python3
"""CT-S61 claims addendum (S61-19..S61-23): which title to chase by.

Separate emitter so it cannot collide with the earlier two, which refuse on
re-run. Validates the in-memory buffer BEFORE writing.

Exit 0 wrote / 2 refused / 3 crash.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTD = SESS / "outputs"
CLAIMS = SESS / "claims.jsonl"
TASK = "CT-S61-SNAPSHOT-AND-STATUS"
OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


def refuse(msg):
    say(f"REFUSED: {msg}")
    (OUTD / "emit_claims_s61c.refused.txt").write_text(
        "\n".join(OUT) + "\n", encoding="utf-8")
    sys.exit(2)


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    chk = OUTD / "check_title.out.txt"
    if not chk.exists():
        refuse("missing check_title.out.txt; run the check first")
    h = sha(chk)
    t = chk.read_text(encoding="utf-8")
    K = "scripts/check_title.py"
    OK = "outputs/check_title.out.txt"

    def C(cid, claim):
        return {"claim_id": cid, "task_id": TASK, "claim": claim,
                "label": "INSPECTED", "evidence_type": "file_inspection",
                "dps": None, "reproducible": True, "script": K,
                "output_hash": h, "output_file": OK}

    c = [
        C("S61-19", "The file SIGMA received is resolved by content, not by "
          "path: vquad_resurgence.pdf in deposit-workspace\\vquad-n1-pv-d5, "
          "612,719 bytes, md5 4d1e4d59072cad0db8edc86280af45a1, matching the "
          "md5 recorded at submission_log.txt section A item 37. Three files "
          "of that same name exist in the tree with three different digests, "
          "so path alone does not identify it."),
        C("S61-20", "The title of item 37 agrees across all three independent "
          "sources: printed on page 1 of the submitted PDF, quoted once in "
          "the body of SIGMA_COVER_LETTER_v1.2_FINAL.md, and recorded in the "
          "log's Title field. The title of record is 'A non-classical "
          "Painlev\u00e9 V transcendent from a quadratic polynomial continued "
          "fraction: surface classification and resurgent Stokes data'."),
        C("S61-21", "The cover letter's Subject line is TRUNCATED. It reads "
          "'Submission: A non-classical Painlev\u00e9 V transcendent from a "
          "quadratic polynomial continued fraction' and drops the subtitle "
          "': surface classification and resurgent Stokes data'. The subject "
          "line is what an editorial office files a direct-email submission "
          "under, so a search of sent mail or of the office's records on the "
          "full title would miss this submission."),
        C("S61-22", "Consequently the search handle differs from the title of "
          "record: chase the submission by the stem 'A non-classical "
          "Painlev\u00e9 V transcendent from a quadratic polynomial continued "
          "fraction' plus the date 1 June 2026, while using the full title of "
          "record in any correspondence. With no submission ID issued by "
          "SIGMA (claim S61-12), this stem is the only handle on the "
          "submission."),
        C("S61-23", "pdftotext on this build rendered the ligatures in this "
          "PDF correctly: a probe for ligature-dropped fragments across the "
          "full extracted text returned no hits other than the unrelated "
          "'2nd ed'. The title checks were nonetheless run through a "
          "ligature-tolerant matcher whose recovery and separation controls "
          "both fired, so an absence result here cannot be confused with a "
          "reader that could not see the text."),
    ]

    # ---- validate BEFORE writing ---------------------------------------
    ids = [x["claim_id"] for x in c]
    if len(set(ids)) != len(ids):
        refuse("duplicate claim ids in buffer")
    for x in c:
        for k in ("claim_id", "task_id", "claim", "label", "script",
                  "output_hash", "output_file"):
            if not str(x.get(k, "")).strip():
                refuse(f"{x['claim_id']}: empty field {k}")
        if x["label"] != "INSPECTED":
            refuse(f"{x['claim_id']}: unexpected label")
        p = SESS / x["output_file"]
        if not p.exists() or x["output_hash"] != sha(p):
            refuse(f"{x['claim_id']}: output_hash does not match disk")
        if not (SESS / x["script"]).exists():
            refuse(f"{x['claim_id']}: cited script missing")
        if x.get("external_source"):
            refuse(f"{x['claim_id']}: local claim carries external_source")

    def need(cid, frag):
        if frag not in t:
            refuse(f"{cid}: cites {frag!r} absent from the check output")

    need("S61-19", "md5  : 4d1e4d59072cad0db8edc86280af45a1")
    need("S61-19", "bytes: 612719")
    need("S61-20", "title found on page 1: True")
    need("S61-20", "occurrences of the full title in the cover letter: 1")
    need("S61-20", "identical to the PDF's printed title: True")
    need("S61-21", "carries the stem    : True")
    need("S61-21", "carries the subtitle: False")
    need("S61-22", "Do NOT search on the full string")
    need("S61-23", "lig() recovers a ligature the literal search misses")

    if "DID NOT FIRE" in t:
        refuse("a control did not fire in the check output")
    if "controls fired: 9/9" not in t:
        refuse("check output does not report the expected control count")
    if "findings      : 1" not in t:
        refuse("check output does not report the expected finding count")

    if CLAIMS.exists():
        have = CLAIMS.read_text(encoding="utf-8")
        present = [i for i in ids if f'"{i}"' in have]
        if present:
            refuse(f"claims already recorded: {present}")

    body = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in c)
    with CLAIMS.open("a", encoding="utf-8") as f:
        f.write(body)

    say(f"appended {len(c)} claims to {CLAIMS.name}")
    say(f"claims.jsonl sha256 {sha(CLAIMS)}")
    (OUTD / "emit_claims_s61c.out.txt").write_text(
        "\n".join(OUT) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
