#!/usr/bin/env python3
"""CT-S62 claims (S62-01..S62-09): the SIGMA closeout.

Validates the in-memory buffer BEFORE writing; refuses if its ids are already
present. Refusals go to their own file, never the success path's.

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
TASK = "CT-S62-SIGMA-CLOSEOUT"
OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


def refuse(msg):
    say(f"REFUSED: {msg}")
    (OUTD / "emit_claims_s62.refused.txt").write_text(
        "\n".join(OUT) + "\n", encoding="utf-8")
    sys.exit(2)


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    chk = OUTD / "check_sigma_closeout.out.txt"
    if not chk.exists():
        refuse("missing check_sigma_closeout.out.txt; run the check first")
    h = sha(chk)
    t = chk.read_text(encoding="utf-8")
    K = "scripts/check_sigma_closeout.py"
    OK = "outputs/check_sigma_closeout.out.txt"

    email = SESS / "email" / "sigma_decision_as_received.txt"
    if not email.exists():
        refuse("the verbatim decision letter is not recorded")
    eh = sha(email)

    def C(cid, claim, etype="file_inspection", script=K, ofile=OK, oh=h):
        return {"claim_id": cid, "task_id": TASK, "claim": claim,
                "label": "INSPECTED", "evidence_type": etype, "dps": None,
                "reproducible": True, "script": script, "output_hash": oh,
                "output_file": ofile}

    c = [
        C("S62-01", "SIGMA rejected the manuscript of section-A item 37 on "
          "2026-09-21, conveyed by Mrs. Vira Pobyzh, Executive Assistant, in "
          "the journal's standing screening formula: not suitable for "
          "consideration as not of the standard required. The letter states "
          "the journal is highly selective about papers for which to start "
          "the refereeing process, so no referees were assigned and no "
          "reports exist. Verbatim text recorded at "
          "email/sigma_decision_as_received.txt, sha256 " + eh + ".",
          "email_inspection"),
        C("S62-02", "The decision settles the receipt question left open at "
          "112 days: a decision letter can only exist if the 2026-06-01 "
          "direct-email submission reached the editorial office. This "
          "supersedes the receipt UNCONFIRMED reading of CT-S61 claims "
          "S61-14 and S61-15, and moots SIGMA's two-working-day resend "
          "remedy to sigmajournal@gmail.com, which must not now be fired. "
          "The earlier claims are superseded, not withdrawn: they were "
          "correct on the evidence available on 2026-09-21 before the letter "
          "arrived.", "email_inspection"),
        C("S62-03", "The letter is attributable to item 37 by elimination "
          "rather than by quotation: it names no title, no identifier and no "
          "submission date, and exactly one section-A item out of 42 names "
          "SIGMA in its Status line. The negative control confirms the search "
          "can fail. Attribution is therefore an inference, and the mailbox "
          "headers would settle it."),
        C("S62-04", "The proposed closeout wording moves the section-A active "
          "count from 4 to exactly 3, leaving items 36, 39 and 42. Measured "
          "by importing make_active_snapshot.py's own TERMINAL_V matcher and "
          "field reader and splicing the edit into an in-memory copy of the "
          "log; the file on disk was not modified, sha256 "
          "70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433 "
          "before and after."),
        C("S62-05", "The pre-registered vacuity arm fired: splicing a "
          "non-terminal verdict into the same position leaves the active "
          "count at 4, so the observable tracks the verdict text rather than "
          "the act of splicing. Without this arm a count that fell for any "
          "reason would have been read as the closeout working."),
        C("S62-06", "Both scanners that carry a TERMINAL matcher, "
          "scan_decided_not_fired.py and scan_stale_records.py, read the "
          "proposed Verdict as terminal, and both match on the word REJECTED "
          "rather than on an incidental word. This was checked explicitly "
          "because CT-S61 found that the same regex matches the bare word "
          "accepted and had silently killed a live record on the phrase "
          "'1 reviewer(s) that has accepted'."),
        C("S62-07", "The closeout is ONE-SIDED. Section-A item 36 (The "
          "Ramanujan Journal) remains non-terminal with a reviewer assigned, "
          "so the manuscript is still live at one venue. Item 36 records "
          "Submission version v.1.0 and names the superseded Stokes constant "
          "0.43770528. The SIGMA rejection therefore moots the "
          "conflict-clearing ground for the withdrawal while leaving the "
          "withdrawal necessary on a different and stronger ground: a "
          "reviewer is refereeing a build whose central constant has since "
          "been withdrawn and whose Theorem 4.1 has since been demoted to a "
          "conjecture."),
        C("S62-08", "Item 37's own text, 'Once the editorial office confirms "
          "withdrawal, the conflict is fully cleared and SIGMA becomes the "
          "sole live venue carrying the corrected v1.2', is now void in "
          "direction: the venue that survives is the one holding the "
          "superseded version, not the corrected one. Recorded as an "
          "appended supersession rather than an edit, because the flag is "
          "evidence of what was believed at the time."),
        C("S62-09", "Nothing in the letter bears on the mathematics. It gives "
          "no substantive reason, so it is neither support for nor evidence "
          "against any of the five LMP correction items, and the closeout "
          "record deliberately omits any reason beyond the quoted formula.",
          "email_inspection"),
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

    need("S62-03", "section-A items whose Status names SIGMA: [37]")
    need("S62-04", "active 4 -> 3")
    need("S62-04", "70f814b926a5fd67a761bbebe19b5474db69b440e7e3f234062"
                   "4c79029897433")
    need("S62-05", "active with a NON-terminal verdict spliced : 4")
    need("S62-06", "every scanner reads it terminal, and on the word "
                   "'REJECTED'")
    need("S62-07", "Item 36 (The Ramanujan Journal) terminal: False")
    need("S62-07", "Item 36 submission version: v.1.0")
    need("S62-07", "records the superseded constant 0.43770528: True")

    if "DID NOT FIRE" in t:
        refuse("a control did not fire in the check output")
    if "controls fired: 7/7" not in t:
        refuse("check output does not report the expected control count")

    # the email digest must be the one in S62-01, re-read from disk
    if eh not in c[0]["claim"]:
        refuse("S62-01 does not carry the digest of the letter on disk")

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
    say(f"decision letter sha256 {eh}")
    (OUTD / "emit_claims_s62.out.txt").write_text(
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
