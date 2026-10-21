"""CT-S56 -- verify claims.jsonl against the files on disk.

Why this exists. The emitter computes each output_hash from the file at build
time, so its internal 'output_hash == sha(file)' check compares a value with
itself and cannot fail in normal operation. It caught mutant M1 only because
that arm overwrote the value after it was computed. A check that cannot fail in
normal operation is not evidence.

This verifier re-reads claims.jsonl FROM DISK and re-hashes each cited output
FROM DISK. The two values now have independent provenance, so disagreement is
detectable -- which matters because any later re-run of a script silently
invalidates every claim citing its output.
"""
import hashlib
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTD = SESS / "outputs"
CLAIMS = SESS / "claims.jsonl"
OUT = OUTD / "verify_claims.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def main() -> int:
    rows = [json.loads(l) for l in CLAIMS.read_text(encoding="utf-8").splitlines() if l.strip()]

    say("=" * 74)
    say("CT-S56 -- claims.jsonl verified against the files on disk")
    say("=" * 74)
    say("")
    say(f"    claims.jsonl : {CLAIMS.stat().st_size} B, {len(rows)} claims")
    say(f"    sha256       : {hashlib.sha256(CLAIMS.read_bytes()).hexdigest()}")
    say("")
    say("    Both sides are read from disk, so this check has independent")
    say("    provenance and can actually fail -- unlike the emitter's own")
    say("    build-time comparison of a computed hash with itself.")
    say("")

    bad = 0
    for c in rows:
        cid = c["claim_id"]
        of = c.get("output_file")
        if not of:
            say(f"    [ ---- ] {cid}: cites no output file")
            continue
        p = OUTD / of
        if not p.exists():
            say(f"    [ FAIL ] {cid}: cited output missing: {of}")
            bad += 1
            continue
        got = hashlib.sha256(p.read_bytes()).hexdigest()
        if got != c["output_hash"]:
            say(f"    [ FAIL ] {cid}: {of}")
            say(f"             recorded {c['output_hash'][:32]}")
            say(f"             on disk  {got[:32]}")
            say(f"             the output was regenerated after the claim was written")
            bad += 1
        else:
            say(f"    [  ok  ] {cid}: {of}")
        sp = SESS / c["script"]
        if not sp.exists():
            say(f"    [ FAIL ] {cid}: script missing: {c['script']}")
            bad += 1
    say("")

    say("[control] the comparison must be able to fail")
    probe = hashlib.sha256(b"not any real output").hexdigest()
    real = hashlib.sha256((OUTD / rows[0]["output_file"]).read_bytes()).hexdigest()
    say(f"    [{'PASS' if probe != real else 'FAIL'}] a synthetic hash does not "
        f"match a real output")
    say("")

    say("=" * 74)
    if bad:
        say(f"FAIL: {bad} claim(s) no longer match the files they cite.")
        say("Re-run scripts/emit_claims_s56.py LAST, after every other script.")
    else:
        say("PASS: every claim's cited output hashes to the recorded value.")
    say("=" * 74)

    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
