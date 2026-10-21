#!/usr/bin/env python3
"""CT-S57: split the two emails apart, without losing or altering a byte.

The operator pasted the follow-up into email_as_sent.txt, which already held
the first email. That file is cited by five claims with a sha256 recorded when
it held the first email alone, so the record went stale the moment the paste
landed -- and nothing in this session would have noticed, because CT-S57 has
no post-hoc verifier.

This script refuses unless the first part reproduces the RECORDED hash exactly.
Reconstructing either email is not an option; if the split does not reproduce
the recorded bytes, the right outcome is a refusal and a report.

Exit codes: 0 split and verified / 2 refusal / 3 crash.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
EMAIL = SESS / "email"
COMBINED = EMAIL / "email_as_sent.txt"
FIRST = EMAIL / "email_as_sent.txt"
FOLLOWUP = EMAIL / "followup_as_sent.txt"
REC = SESS / "claims.jsonl"

# The hash recorded by record_correction.py when the file held email 1 alone.
RECORDED_SHA = "9bdcd347505999fdfb269ca0b632b23d83c25245e55fac066f565cd29a0572a0"
RECORDED_BYTES = 2862

SUBJ1 = "Subject: MATH-D-26-00523: author's corrections to four statements"
SUBJ2 = "Subject: MATH-D-26-00523: item 4 resolved, and one further correction"


def die(m, c=2):
    print(f"REFUSED: {m}")
    sys.exit(c)


def sha(b: bytes):
    return hashlib.sha256(b).hexdigest()


def main():
    if not COMBINED.exists():
        die(f"missing {COMBINED}")
    if FOLLOWUP.exists():
        die(f"{FOLLOWUP.name} already exists; refusing to overwrite a record")

    raw = COMBINED.read_bytes()
    print(f"combined file: {len(raw)} bytes, sha256 {sha(raw)}")

    if sha(raw) == RECORDED_SHA:
        die("the file still hashes to the recorded value, so it holds only "
            "the first email; the follow-up has not been pasted in")

    # Locate the second subject line. Byte-level, so nothing is re-encoded.
    marker = SUBJ2.encode("utf-8")
    idx = raw.find(marker)
    if idx < 0:
        die(f"could not find the follow-up's subject line in {COMBINED.name}; "
            "refusing to guess where one email ends and the other begins")
    if raw.find(marker, idx + 1) >= 0:
        die("the follow-up's subject line occurs more than once; the split "
            "point is ambiguous")
    if not raw.startswith(SUBJ1.encode("utf-8")):
        die("the file does not begin with the first email's subject line")

    head, tail = raw[:idx], raw[idx:]
    stripped = head.rstrip(b"\r\n")

    # The record, not a guess, defines where the first email ends. The paste
    # inserted separator blank lines that belong to neither email, so try the
    # candidate endings and accept only the one whose hash the five existing
    # claims already cite. If none matches, refuse: that means the first email
    # on disk is not the text those claims rest on.
    candidates = [
        ("as stripped", stripped),
        ("+ one CRLF", stripped + b"\r\n"),
        ("+ one LF", stripped + b"\n"),
        ("+ two CRLF", stripped + b"\r\n\r\n"),
        ("unstripped head", head),
    ]
    print(f"split at byte {idx}")
    chosen = None
    for name, cand in candidates:
        h = sha(cand)
        mark = ""
        if h == RECORDED_SHA and chosen is None:
            chosen = (name, cand)
            mark = "  <- matches the recorded hash"
        print(f"  part 1 {name:<16}{len(cand):<6}{h[:16]}{mark}")
    print(f"  part 2 {'':<16}{len(tail):<6}{sha(tail)[:16]}")

    if chosen is None:
        die("no candidate ending for part 1 reproduces the recorded "
            f"{RECORDED_SHA}. The first email as it now sits on disk is not "
            "the one the five existing claims cite. Report this; do not "
            "reconstruct it.")
    name, first = chosen
    dropped = len(head) - len(first)
    print(f"[PASS] part 1 = {name}, {len(first)} bytes, byte-identical to the "
          f"text the existing claims cite; {dropped} separator byte(s) "
          "introduced by the paste belong to neither email and are discarded")

    if len(first) != RECORDED_BYTES:
        die(f"part 1 is {len(first)} bytes, not the recorded {RECORDED_BYTES}")

    FOLLOWUP.write_bytes(tail)
    FIRST.write_bytes(first)
    print(f"wrote {FOLLOWUP}")
    print(f"restored {FIRST} to its recorded bytes")

    # Re-verify from disk, both sides re-read.
    back = FIRST.read_bytes()
    if sha(back) != RECORDED_SHA:
        die("post-write read-back of part 1 does not match the recorded hash")
    fu = FOLLOWUP.read_bytes()
    print(f"\nfollow-up on disk: {len(fu)} bytes, sha256 {sha(fu)}")

    # Confirm every existing claim citing the email file still verifies.
    if REC.exists():
        bad = 0
        for line in REC.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            c = json.loads(line)
            out = c.get("output") or c.get("file") or ""
            p = SESS / out if out else None
            if p and p.exists() and c.get("output_hash"):
                if sha(p.read_bytes()) != c["output_hash"]:
                    print(f"[FAIL] {c['claim_id']}: {out} no longer matches "
                          "its recorded hash")
                    bad += 1
        print(f"existing claims re-checked from disk: "
              f"{'all consistent' if not bad else f'{bad} inconsistent'}")
        if bad:
            return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
