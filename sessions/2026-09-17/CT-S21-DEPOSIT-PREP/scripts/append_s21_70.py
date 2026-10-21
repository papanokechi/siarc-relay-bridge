"""Append claim S21-70 (carry-over PDF staged and verified)."""

import json
import pathlib

SESSION = pathlib.Path(__file__).resolve().parents[1]
CLAIMS = SESSION / "claims.jsonl"

CLAIM = {
    "claim_id": "S21-70",
    "task_id": "CT-S21-DEPOSIT-PREP",
    "claim": (
        "The operator's v1.3 draft file list showed only the correction notice, "
        "so abort condition 4 (the carried-over v1.2 paper must be present) was "
        "not satisfied at the time of inspection. A locally held copy of the "
        "v1.2 paper was staged at upload/vquad_resurgence.pdf and verified "
        "against outputs/predeposit_20481592.json: 612719 bytes and md5 "
        "4d1e4d59072cad0db8edc86280af45a1, both equal to the live record's file "
        "entry, and the staged filename equals the published key "
        "vquad_resurgence.pdf. Uploading this file restores the paper to the "
        "record. Not established here: whether the draft is a New version or a "
        "New upload; that is resolved only by checking whether the draft's "
        "metadata fields are pre-filled from v1.2."
    ),
    "label": "VERIFIED",
    "evidence_type": "computation",
    "dps": None,
    "reproducible": True,
    "script": "scripts/stage_carryover_pdf.py",
    "output_hash": (
        "a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85"
    ),
}


def main():
    existing = [
        json.loads(line)
        for line in CLAIMS.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if any(c["claim_id"] == CLAIM["claim_id"] for c in existing):
        raise SystemExit("HALT: %s already present" % CLAIM["claim_id"])
    with CLAIMS.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(CLAIM, ensure_ascii=False) + "\n")
    print("appended %s; claims now %d" % (CLAIM["claim_id"], len(existing) + 1))


if __name__ == "__main__":
    main()
