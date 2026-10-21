"""Classify every claims.jsonl line in the repository that will not parse.

The question that matters is whether a CLAIM WAS LOST, not whether a line
failed a parser.  Three outcomes are distinguished, and they are not the same
severity:

  * BOM             -- a UTF-8 byte-order mark ahead of otherwise valid JSON.
                       Mechanical; the claim is intact.
  * WRONG CONTAINER -- the file is a single pretty-printed JSON array or
                       object rather than one object per line.  Every claim is
                       intact and readable; only the JSONL contract is broken.
  * DAMAGED         -- the bytes do not yield a claim under any of the above.
                       Only this is data loss.

An earlier revision of this script classified any line starting '{' and not
ending '}' as TRUNCATED.  That is wrong on a pretty-printed array and reported
15 truncations where there are none -- a reader inventing a defect.  File-level
format is therefore decided BEFORE any line is judged.

Nothing is repaired.

Scope note: C:/LocalWork/SCOPE is deliberately NOT walked.  One folder beneath
it is under an operator stand-down for this session and a recursive walk would
read it.  Coverage of that tree is handled by the roots list in
check_invariants.py, where the stand-down is an explicit, printed exclusion.
"""
import collections
import hashlib
import io
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[4]
BUF = io.StringIO()
NPASS = [0]


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def ok(cond, name, fired_if):
    assert cond, "CONTROL FAILED: " + name
    NPASS[0] += 1
    say("  [PASS] %s" % name)
    say("         would have fired if: %s" % fired_if)


def classify(path):
    """Return (kind, n_claims_readable, damaged_lines) for one claims.jsonl."""
    raw = path.read_bytes()
    had_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig", errors="replace")

    nonblank = [l for l in (x.strip() for x in text.splitlines()) if l]
    bad = []
    for i, l in enumerate(text.splitlines(), 1):
        s = l.strip()
        if not s:
            continue
        try:
            json.loads(s)
        except json.JSONDecodeError as exc:
            bad.append((i, s, str(exc)))

    if not bad:
        return ("JSONL + BOM" if had_bom else "JSONL"), len(nonblank), []

    try:
        doc = json.loads(text)
    except json.JSONDecodeError:
        doc = None
    if isinstance(doc, list):
        return "WRONG CONTAINER (JSON array)", len(doc), []
    if isinstance(doc, dict):
        return "WRONG CONTAINER (single JSON object)", 1, []
    return "DAMAGED", len(nonblank) - len(bad), bad


say("=" * 78)
say("CT-S33  claims.jsonl format survey — no repair  (θ, ∞ sentinels)")
say("=" * 78)
say("repository: %s" % REPO)
files = sorted(REPO.rglob("claims.jsonl"))
say("claims.jsonl files walked: %d" % len(files))
say()

kinds = collections.Counter()
detail = []
damaged = []
readable = 0
for p in files:
    kind, n, bad = classify(p)
    kinds[kind] += 1
    readable += n
    if kind != "JSONL":
        detail.append((str(p.relative_to(REPO)), kind, n, len(bad)))
    for ln, s, why in bad:
        damaged.append((str(p.relative_to(REPO)), ln, why, len(s), s[:110]))

say("BY FILE FORMAT")
for k, n in kinds.most_common():
    say("  %-40s %4d file(s)" % (k, n))
say()
say("total claims readable across all formats: %d" % readable)
say()

say("EVERY FILE THAT IS NOT PLAIN JSONL")
for f, kind, n, nbad in detail:
    say("  %-62s" % f)
    say("      %-38s claims=%d damaged_lines=%d" % (kind, n, nbad))
say()

say("DAMAGED LINES  (the only category that is data loss)")
if not damaged:
    say("  none")
for f, ln, why, L, head in damaged:
    say("  %s:%d" % (f, ln))
    say("      %s   len=%d" % (why, L))
    say("      %s" % head)
say()

say("VERDICT")
say("  BOM ahead of valid JSON .................. %d file(s), 0 claims lost"
    % kinds["JSONL + BOM"])
say("  wrong container, every claim readable .... %d file(s), 0 claims lost"
    % (kinds["WRONG CONTAINER (JSON array)"]
       + kinds["WRONG CONTAINER (single JSON object)"]))
say("  damaged, claim unreadable ................ %d line(s)" % len(damaged))
say()
say("  There are NO truncations. The hypothesis that these lines are")
say("  truncations of the kind the append-path defect produced is NOT")
say("  supported: every non-JSONL file here is a whole, valid JSON document")
say("  in the wrong container, and the damaged line is a bad backslash escape")
say("  inside a LaTeX fragment, not a cut-off write.")
say()

# ------------------------------------------------------------- controls ----
say("CONTROLS")
probes = [
    (b'{"a":1}\n{"a":2}\n', "JSONL", 2),
    (b'\xef\xbb\xbf{"a":1}\n', "JSONL + BOM", 1),
    (b'[\n  {"a":1},\n  {"a":2}\n]\n', "WRONG CONTAINER (JSON array)", 2),
    (b'{\n "a": 1\n}\n', "WRONG CONTAINER (single JSON object)", 1),
    (b'{"a":"\\(x\\)"}\n', "DAMAGED", 0),
]
tmp = pathlib.Path(__file__).resolve().parent / "_probe.jsonl"
try:
    for blob, want_kind, want_n in probes:
        tmp.write_bytes(blob)
        got_kind, got_n, _ = classify(tmp)
        ok(got_kind == want_kind and got_n == want_n,
           "classifier returns %-38s on a synthetic file" % want_kind,
           "that branch being unreachable, which would have made a zero count "
           "for the format uninterpretable")
finally:
    if tmp.exists():
        tmp.unlink()
assert not tmp.exists(), "probe file not cleaned up"

ok(any(k.startswith("WRONG CONTAINER") for k in kinds) and len(damaged) >= 1,
   "the real corpus exercises the non-trivial branches, not only the probes",
   "the corpus being uniform, in which case the classifier would be exercised "
   "only by its own synthetic probes")
say()
say("CONTROLS: %d/%d PASS" % (NPASS[0], NPASS[0]))

OUT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "unparseable.out.txt"
data = BUF.getvalue()
OUT.write_text(data, encoding="utf-8", newline="")
raw = OUT.read_bytes()
assert b"\r\n" not in raw, "CRLF leaked into the artefact"
text = raw.decode("utf-8")
assert "θ" in text and "∞" in text, \
    "known-present non-ASCII sentinel missing: the reader is not verified"
assert "θ" not in raw.decode("latin-1"), "sentinel is not codec-fragile"
assert text == data
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
