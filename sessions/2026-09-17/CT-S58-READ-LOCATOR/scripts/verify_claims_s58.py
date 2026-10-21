#!/usr/bin/env python3
"""CT-S58: re-read claims.jsonl and every cited output FROM DISK.

The emitter's own hash check compares a value it computed moments earlier from
the same file, so it cannot fail on a record that was correct when written and
stale afterwards. This runs last and re-derives both sides.

Exit codes: 0 all claims verify / 1 a claim does not / 2 refusal / 3 crash.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REC = SESS / "claims.jsonl"


def main():
    if not REC.exists():
        print(f"REFUSED: no claims record at {REC}")
        return 2
    lines = [l for l in REC.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not lines:
        print("REFUSED: claims record is empty")
        return 2

    bad = 0
    for l in lines:
        c = json.loads(l)
        cid = c["claim_id"]
        op = SESS / c["output"]
        sp = SESS / c["script"]
        if not sp.exists():
            print(f"[FAIL] {cid}: script missing: {c['script']}")
            bad += 1
        if not op.exists():
            print(f"[FAIL] {cid}: output missing: {c['output']}")
            bad += 1
            continue
        h = hashlib.sha256(op.read_bytes()).hexdigest()
        if h != c["output_hash"]:
            print(f"[FAIL] {cid}: recorded {c['output_hash'][:16]} but "
                  f"on-disk {h[:16]} for {c['output']}")
            bad += 1
            continue
        body = op.read_text(encoding="utf-8", errors="replace")
        for fig in re.findall(r"\d{1,6}", c["claim"]):
            if not re.search(rf"(?<!\d){re.escape(fig)}(?!\d)", body):
                print(f"[FAIL] {cid}: figure {fig} absent from {c['output']}")
                bad += 1
        if c["label"] not in ("INSPECTED", "VERIFIED", "STRUCTURAL",
                              "CONJECTURED"):
            print(f"[FAIL] {cid}: bad label {c['label']!r}")
            bad += 1

    print(f"{len(lines)} claim(s) re-verified from disk, {bad} failure(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
