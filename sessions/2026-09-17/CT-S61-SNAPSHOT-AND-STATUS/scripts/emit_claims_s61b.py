#!/usr/bin/env python3
"""CT-S61 claims addendum (S61-12..S61-18): the SIGMA submission identifier.

Separate emitter so it cannot collide with emit_claims_s61.py, which refuses
on re-run. Validates the in-memory buffer BEFORE writing; refuses if its ids
are already present.

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
POLICY_URL = "https://sigma-journal.com/about.html#submit"
OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


def refuse(msg):
    say(f"REFUSED: {msg}")
    (OUTD / "emit_claims_s61b.refused.txt").write_text(
        "\n".join(OUT) + "\n", encoding="utf-8")
    sys.exit(2)


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    chk = OUTD / "check_sigma_id.out.txt"
    if not chk.exists():
        refuse("missing check_sigma_id.out.txt; run the check first")
    h = sha(chk)
    t = chk.read_text(encoding="utf-8")
    K = "scripts/check_sigma_id.py"
    OK = "outputs/check_sigma_id.out.txt"

    def C(cid, claim, etype="file_inspection", src=None):
        d = {"claim_id": cid, "task_id": TASK, "claim": claim,
             "label": "INSPECTED", "evidence_type": etype, "dps": None,
             "reproducible": True, "script": K, "output_hash": h,
             "output_file": OK}
        if src:
            d["external_source"] = src
            d["retrieved"] = "2026-09-21"
            d["reproducible"] = False
        return d

    c = [
        C("S61-12", "SIGMA issues no proprietary manuscript identifier: it is "
          "an arXiv overlay journal whose submission instructions direct "
          "authors to send the arXiv number, so the arXiv number is the "
          "identifier. Section-A item 37 used the non-arXiv direct email "
          "route, therefore no submission ID exists or will be assigned.",
          "web_inspection", POLICY_URL),
        C("S61-13", "No SIGMA-shaped manuscript ID occurs anywhere in "
          "submission_log.txt; item 37's Submission ID field reads 'PENDING "
          "-- email submission; no portal/manuscript ID assigned yet; "
          "awaiting editorial acknowledgement', i.e. it awaits an identifier "
          "the journal does not issue."),
        C("S61-14", "No acknowledgement of receipt of the SIGMA submission is "
          "recorded anywhere in the log; 112 days elapsed between the "
          "submission of 2026-06-01 and this check on 2026-09-21."),
        C("S61-15", "SIGMA's submission instructions state that if receipt is "
          "not acknowledged within two working days the paper should be "
          "resent to the alternative address sigmajournal@gmail.com. That "
          "remedy fell due about 2026-06-03 and has not been fired; receipt "
          "of item 37 is therefore UNCONFIRMED.",
          "web_inspection", POLICY_URL),
        C("S61-16", "SIGMA's exceptional non-arXiv route asks for the zipped "
          "paper in TeX/LaTeX format together with the PDF, and an "
          "explanation why the author prefers not to post to arXiv. Item 37 "
          "is logged as a PDF-only submission (vquad_resurgence.pdf, 612,719 "
          "B), and SIGMA_COVER_LETTER_v1.2_FINAL.md frames the direct-PDF "
          "route as a contingency ('I will follow that route if needed') "
          "rather than exercising it with a stated reason.",
          "web_inspection", POLICY_URL),
        C("S61-17", "SIGMA's stated criteria require that papers be not "
          "published previously and not under consideration for publication "
          "in any other journal or book. Given claim S61-08 (the Ramanujan "
          "withdrawal is unconfirmed and a reviewer is refereeing), the "
          "manuscript is formally under consideration at two venues, so this "
          "condition is currently breached.",
          "web_inspection", POLICY_URL),
        C("S61-18", "SIGMA states it is an authorised arXiv proxy submitter "
          "and can submit or replace an article in the arXiv on behalf of "
          "authors; stated in the context of accepted papers. Recorded "
          "because the arXiv endorsement barrier has been shaping venue "
          "selection across this portfolio.",
          "web_inspection", "https://sigma-journal.com/about.html#overlay"),
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
        # a web-sourced claim must name its source and be marked
        # non-reproducible; a local claim must not carry a source
        if x["evidence_type"] == "web_inspection":
            if not x.get("external_source") or x.get("reproducible"):
                refuse(f"{x['claim_id']}: web claim mis-marked")
        elif x.get("external_source"):
            refuse(f"{x['claim_id']}: local claim carries external_source")

    def need(cid, frag, where="check output"):
        if frag not in t:
            refuse(f"{cid}: cites {frag!r} absent from {where}")

    need("S61-13", "matches: NONE")
    need("S61-13", "PENDING")
    need("S61-14", "+112")
    need("S61-16", "PDF only (no .zip / .tex): True")
    need("S61-16", "framed as contingency ('if needed'): True")
    if "DEAD  " in t:
        refuse("a control was reported DEAD in the check output")
    if "5 finding" not in t:
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
    (OUTD / "emit_claims_s61b.out.txt").write_text(
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
