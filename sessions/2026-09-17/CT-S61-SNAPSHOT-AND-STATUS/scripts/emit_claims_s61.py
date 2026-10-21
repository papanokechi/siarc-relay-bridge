#!/usr/bin/env python3
"""CT-S61 claims emitter. Validates the in-memory buffer BEFORE writing, and
refuses to append if its claim IDs are already present.

Exit 0 wrote / 2 refused / 3 crash.
"""
import hashlib
import json
import re
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
    (OUTD / "emit_claims_s61.refused.txt").write_text(
        "\n".join(OUT) + "\n", encoding="utf-8")
    sys.exit(2)


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    OUTD.mkdir(parents=True, exist_ok=True)
    snap = OUTD / "active_snapshot.txt"
    snapout = OUTD / "make_active_snapshot.out.txt"
    chk = OUTD / "check_item36_windows.out.txt"
    for p in (snap, snapout, chk):
        if not p.exists():
            refuse(f"missing evidence file {p.name}; run the scripts first")

    h_snap, h_chk = sha(snap), sha(chk)
    chk_txt = chk.read_text(encoding="utf-8")
    snap_txt = snap.read_text(encoding="utf-8")

    def C(cid, claim, script, out, h):
        return {"claim_id": cid, "task_id": TASK, "claim": claim,
                "label": "INSPECTED", "evidence_type": "file_inspection",
                "dps": None, "reproducible": True, "script": script,
                "output_hash": h, "output_file": out}

    S = "scripts/make_active_snapshot.py"
    K = "scripts/check_item36_windows.py"
    OS_ = "outputs/active_snapshot.txt"
    OK = "outputs/check_item36_windows.out.txt"

    c = [
        C("S61-01", "SUPERSEDES CT-S60 claim in REPORT.md section 5: "
          "scan_decided_not_fired.py WAS located, at "
          "C:\\LocalWork\\deposit-A076227\\out\\, together with three siblings "
          "scan_stale_records.py, scan_fired_not_landed.py and "
          "scan_submission_substrates.py.", K, OK, h_chk),
        C("S61-02", "The 2026-08-29 rewrite of scan_decided_not_fired.py is "
          "verifiable: v1 backup run against the current log reports 13 flat "
          "windows with no record attribution; the current version reports 1 "
          "live and 12 moot, correctly suppressing the JDE nudge window.",
          K, OK, h_chk),
        C("S61-03", "scan_decided_not_fired.py computes liveness as "
          "dead = TERMINAL(Verdict) or TERMINAL(Status); because it is an OR "
          "it is structurally blind to Status/Verdict disagreement, so "
          "CT-S60's sweep is complementary and not duplicative.",
          K, OK, h_chk),
        C("S61-04", "scan_stale_records.py independently names section-A items "
          "13, 26 and 35 as its calibration true positives, corroborating "
          "CT-S60 claim S60-11 that JMP26-AR-01521 is Item 35, not Item 34.",
          K, OK, h_chk),
        C("S61-05", "scan_stale_records.py currently exits 2 with CALIBRATION "
          "FAILED because the master-log patch it anchors on has landed; its "
          "anchor requires updating per its own printed instruction.",
          K, OK, h_chk),
        C("S61-06", "Generated active-submissions snapshot: section A holds 42 "
          "items of which 4 are active (Verdict not terminal), namely items "
          "36, 37, 39 and 42. 5/5 controls fired. The count independently "
          "matches scan_stale_records.py's 'non-terminal records 4'.",
          S, OS_, h_snap),
        C("S61-07", "Section-A items 36 and 37 carry an identical Title and "
          "are both non-terminal, at The Ramanujan Journal and at SIGMA "
          "respectively.", K, OK, h_chk),
        C("S61-08", "A withdrawal of item 36 was requested from The Ramanujan "
          "Journal on 2026-06-01 and remains unconfirmed 112 days later; the "
          "portal check of 2026-08-29 recorded that one reviewer had accepted "
          "the invitation and was refereeing.", K, OK, h_chk),
        C("S61-09", "scan_decided_not_fired.py suppresses item 36 as 'moot "
          "(record now terminal)' because its TERMINAL regex matches the word "
          "'accepted' inside the sentence 'There is 1 reviewer(s) that has "
          "accepted.' -- a phrase asserting the manuscript is live.",
          K, OK, h_chk),
        C("S61-10", "Item 36's own escalation dates WATCH-1 2026-09-01 and "
          "WATCH-2 2026-09-12 are overdue by 20 and 9 days and are matched by "
          "neither the scanner's PAT regex nor any other check: PAT lists "
          "'escalation' while the text says 'escalate', and WATCH-2 carries no "
          "trigger keyword.", K, OK, h_chk),
        C("S61-11", "This session did not modify submission_log.txt; its "
          "sha256 remains "
          "70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433. "
          "Status-line replacements for items 13 and 26 are proposed in "
          "STATUS-EDITS.md and left for the operator to apply.",
          K, OK, h_chk),
    ]

    # ---- validate the in-memory buffer BEFORE writing -------------------
    ids = [x["claim_id"] for x in c]
    if len(set(ids)) != len(ids):
        refuse("duplicate claim ids in buffer")
    for x in c:
        for k in ("claim_id", "task_id", "claim", "label", "script",
                  "output_hash", "output_file"):
            if not str(x.get(k, "")).strip():
                refuse(f"{x['claim_id']}: empty field {k}")
        if x["label"] != "INSPECTED":
            refuse(f"{x['claim_id']}: unexpected label {x['label']}")
        p = SESS / x["output_file"]
        if not p.exists():
            refuse(f"{x['claim_id']}: cited output {x['output_file']} missing")
        if x["output_hash"] != sha(p):
            refuse(f"{x['claim_id']}: output_hash does not match "
                   f"{x['output_file']} on disk")
        if not (HERE.parent / x["script"]).exists():
            refuse(f"{x['claim_id']}: cited script {x['script']} missing")

    # substantive cross-checks against the evidence text
    def need(cid, frag, hay, where):
        if frag not in hay:
            refuse(f"{cid}: cites {frag!r} absent from {where}")

    need("S61-06", "Section-A items: 42", snap_txt, "active_snapshot.txt")
    need("S61-06", "Active: 4", snap_txt, "active_snapshot.txt")
    need("S61-07", "titles identical: True", chk_txt, "check output")
    need("S61-08", "(+112d)", chk_txt, "check output")
    need("S61-09", "'accepted'", chk_txt, "check output")
    need("S61-10", "overdue:+20d", chk_txt, "check output")
    need("S61-10", "overdue:+9d", chk_txt, "check output")
    if "DEAD  " in chk_txt:
        refuse("a control was reported DEAD in the check output")
    if "7 finding" not in chk_txt and "4 finding" not in chk_txt:
        refuse("check output does not report the expected finding count")

    # idempotency: refuse rather than append twice
    if CLAIMS.exists():
        have = CLAIMS.read_text(encoding="utf-8")
        present = [i for i in ids if f'"{i}"' in have]
        if present:
            refuse(f"claims already recorded: {present}")

    body = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in c)
    with CLAIMS.open("a", encoding="utf-8") as f:
        f.write(body)

    say(f"wrote {len(c)} claims to {CLAIMS.name}")
    say(f"claims.jsonl sha256 {sha(CLAIMS)}")
    (OUTD / "emit_claims_s61.out.txt").write_text(
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
