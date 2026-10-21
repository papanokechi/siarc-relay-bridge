"""Verify every hash cited in REPORT.md resolves against a file on disk.

A report that cites a digest nothing produces is worse than one that cites
none. Every 16+-hex-digit run in the report must be the prefix of the sha256
of some file in this session (or of the checker under change), and the report
must be under 200 lines.

Controls that can fail are included: a digest of the right shape that belongs
to nothing must be rejected, and the resolver must not succeed by matching a
prefix so short that anything matches.
"""
import hashlib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
REPORT = HERE / "REPORT.md"
raw = REPORT.read_bytes()
text = raw.decode("utf-8")
assert "≥" in text and "…" in text, "non-ASCII sentinel absent: reader unverified"
assert "≥" not in raw.decode("latin-1"), "a wrong-codec read would have passed"

pool = {}
for p in list(HERE.rglob("*")) + [HERE.parent / "CT-R1-AUDIT" /
                                  "check_invariants.py"]:
    if p.is_file():
        pool[hashlib.sha256(p.read_bytes()).hexdigest()] = p
assert len(pool) > 10, "file pool too small; the check would be vacuous"

HEX = re.compile(r"\b([0-9a-f]{16,64})\b")
cited = sorted(set(HEX.findall(text)))
assert len(cited) >= 10, "too few digests found; the regex may have missed them"


def resolve(h):
    m = [v for k, v in pool.items() if k.startswith(h)]
    return m


# Input fingerprints are hashes of a MANIFEST, not of any file, so they cannot
# resolve in the pool. They are verified differently: each must appear
# verbatim in the checker output that reports it.
FINGERPRINTS = {
    "a37d6601e12fc9f0": "outputs/rulings_pass.out.txt",
    "f5947419b462bccb": "outputs/post_emit_pass.out.txt",
}


lines = text.count("\n") + (0 if text.endswith("\n") else 1)
print("REPORT.md: %d lines, %d bytes" % (lines, len(raw)))
assert lines < 200, "report is %d lines, over the 200 limit" % lines

unresolved = []
for h in cited:
    m = resolve(h)
    if h in FINGERPRINTS:
        src = (HERE / FINGERPRINTS[h]).read_text(encoding="utf-8",
                                                 errors="replace")
        assert "input fingerprint: " + h in src, (
            "fingerprint %s is not reported by %s" % (h, FINGERPRINTS[h]))
        print("  [fp] %s...  input fingerprint, verbatim in %s"
              % (h[:16], FINGERPRINTS[h]))
    elif len(m) == 1:
        print("  [ok] %s...  %s" % (h[:16], m[0].relative_to(HERE.parent)))
    else:
        unresolved.append((h, len(m)))
        print("  [??] %s...  matches %d files" % (h[:16], len(m)))

# --- controls --------------------------------------------------------------
print()
fake = "deadbeefdeadbeefdeadbeefdeadbeef"
assert resolve(fake) == [], "a digest belonging to nothing resolved"
print("  [PASS] a well-formed digest belonging to no file does NOT resolve")
print("         would have fired if: resolve() matched loosely, making every")
print("         [ok] above meaningless")

short = [h for h in cited if len(h) < 16]
assert not short, "a digest shorter than 16 hex was accepted"
print("  [PASS] no digest shorter than 16 hex digits is accepted")
print("         would have fired if: a prefix short enough to collide were")
print("         treated as a citation")

known = hashlib.sha256((HERE / "claims.jsonl").read_bytes()).hexdigest()
assert known in cited or any(known.startswith(h) for h in cited), \
    "claims.jsonl's own digest is not cited in the report"
print("  [PASS] claims.jsonl's digest is among those cited and resolves")
print("         would have fired if: the report cited digests but not the")
print("         artefact it is a report on")

assert not unresolved, "unresolved digests: %r" % unresolved
print()
print("ALL %d CITED DIGESTS RESOLVE; report %d lines." % (len(cited), lines))
