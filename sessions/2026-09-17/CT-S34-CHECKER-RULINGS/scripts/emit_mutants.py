"""Mutant arms on emit_claims.py.

The standing rule is that a validating writer checks its in-memory buffer
BEFORE writing; a post-write assertion still leaves the corrupt artefact on
disk. Three instances of write-then-validate have now been found in this
corpus, so the rule is demonstrated here rather than asserted.

Each arm requires three things together: the emitter REFUSED, it refused for
the injected reason and not because the mutated source would not parse, and
claims.jsonl is BYTE-IDENTICAL afterwards. The third condition is the one
that distinguishes a pre-write check from a post-write one; the first two
alone were satisfied by CT-S28 defect 6.3 and by CT-S32 arm M6 while the
artefact on disk was already corrupt.
"""
import hashlib
import io
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
EMIT = HERE / "scripts" / "emit_claims.py"
ART = HERE / "claims.jsonl"
SRC = EMIT.read_text(encoding="utf-8")
BEFORE = hashlib.sha256(ART.read_bytes()).hexdigest()

ARMS = [
    ("E1  review_note altered -- must fail against the PINNED hash",
     'NOTE = ("contaminated re-derivation; prior treatment of the same '
     'operator "\n        "was in context")',
     'NOTE = ("clean re-derivation; nothing prior was in context")',
     "pinned hash"),
    ("E2  a claim relabelled to a value outside the recognised set",
     '("S34-01", "PROVEN", "measurement",',
     '("S34-01", "PROCEED", "measurement",',
     'r["label"] in LABELS'),
    ("E3  a duplicate claim_id",
     '("S34-07", "PROVEN", "measurement",',
     '("S34-06", "PROVEN", "measurement",',
     "len(set(ids))"),
    ("E4  a gap in the id sequence",
     '("S34-09", "VERIFIED", "control",',
     '("S34-29", "VERIFIED", "control",',
     "ids not contiguous"),
    ("E5  evidence stripped of its hash",
     'assert "sha256" in r["evidence"] or "untracked" in r["evidence"]',
     'assert "sha256" in r["evidence"] or "untracked" in r["evidence"] or True',
     "SENTINEL_E5"),
    ("E6  a CR injected into the bytes destined for disk",
     'blob = text.encode("utf-8")',
     'blob = text.replace("\\n", "\\r\\n").encode("utf-8")',
     "CR in the bytes destined for disk"),
    ("E7  review label flipped away from self",
     '"review": "self", "review_note": NOTE,',
     '"review": "independent", "review_note": NOTE,',
     'r["review"] == "self"'),
    ("E8  an out-of-scope phrase in a claim",
     "The label convention is NOT monotone",
     "The Bridge Conjecture and the label convention are NOT monotone",
     "out of scope"),
]

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


say("=" * 78)
say("CT-S34  mutant arms on the claims emitter  (θ, ∞ sentinels)")
say("=" * 78)
say("artefact under test   : claims.jsonl")
say("(its sha256 is deliberately NOT printed here: this output is cited BY")
say(" claims.jsonl, so printing the hash would make the two mutually")
say(" circular. Byte-identity across each arm is what the arms establish.)")
say()

missing = [a[0] for a in ARMS if a[1] not in SRC]
assert not missing, "mutation target absent, arm cannot fire: %r" % missing

# E5 has no natural reason string: the loosened assertion must be replaced by
# one that names itself, else the arm would test an emitter that accepts.
caught = 0
for name, old, new, reason in ARMS:
    mutated = SRC.replace(old, new, 1)
    if reason == "SENTINEL_E5":
        mutated = mutated.replace(
            'assert len(r["claim"]) > 80 and len(r["evidence"]) > 20',
            'assert len(r["claim"]) > 80 and len(r["evidence"]) > 20\n'
            '    assert "sha256" in r["evidence"], "SENTINEL_E5"')
        mutated = mutated.replace(
            'rows.append({"claim_id": cid, "label": label,',
            'evidence = ("measured directly; no digest was recorded for this '
            'line at all" if cid == "S34-17" else evidence)\n    '
            'rows.append({"claim_id": cid, "label": label,')
    assert mutated != SRC, "%s: mutation did not apply" % name
    mf = HERE / "scripts" / "_mutant_emit.py"
    mf.write_text(mutated, encoding="utf-8")
    try:
        r = subprocess.run([sys.executable, str(mf)], capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
    finally:
        mf.unlink()
    out = (r.stdout or "") + (r.stderr or "")

    refused = r.returncode != 0
    broke = ("SyntaxError" in out or "NameError" in out
             or "IndentationError" in out or "TypeError" in out)
    right = reason in out and not broke
    after = hashlib.sha256(ART.read_bytes()).hexdigest()
    intact = after == BEFORE
    verdict = "CAUGHT" if (refused and right and intact) else "MISSED"
    caught += verdict == "CAUGHT"
    say("%-6s %s" % (verdict, name))
    say("       refused=%s  right_reason=%s  broke_script=%s  artefact "
        "intact=%s" % (refused, right, broke, intact))
    if verdict == "MISSED":
        for ln in out.strip().splitlines()[-5:]:
            say("       " + ln)
    assert intact, ("%s: the artefact on disk CHANGED -- the emitter writes "
                    "before it validates" % name)

say()
say("artefact byte-identical after every arm: %s"
    % (hashlib.sha256(ART.read_bytes()).hexdigest() == BEFORE))
say("ARMS: %d/%d CAUGHT" % (caught, len(ARMS)))
assert caught == len(ARMS), "an arm was MISSED"

OUT = HERE / "outputs" / "emit_mutants.out.txt"
blob = BUF.getvalue().encode("utf-8")
assert b"\r" not in blob
OUT.write_bytes(blob)
raw = OUT.read_bytes()
assert raw == blob
assert "θ" in raw.decode("utf-8") and "∞" in raw.decode("utf-8")
assert "θ" not in raw.decode("latin-1")
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
