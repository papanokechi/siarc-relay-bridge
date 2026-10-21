"""Verify every sha256 cited in claims.jsonl resolves against a file on disk.

A claim citing a digest nothing produces is unfalsifiable. This resolver is
separate from verify_report.py and runs over the claims, not the report.

It also records a hazard found the hard way: outputs/measure.out.txt is
produced by walking the corpus, and the corpus now contains this session's
own claims. Re-running measure.py AFTER emitting claims changes that file and
breaks the citation. The ordering is therefore fixed: measure, then emit,
then never measure again. This script fails if that ordering was violated,
which is the only way the violation is visible at all.
"""
import hashlib
import io
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
ART = HERE / "claims.jsonl"
raw = ART.read_bytes()
claims = [json.loads(l) for l in io.StringIO(raw.decode("utf-8"))]
assert len(claims) == 23
assert "\\(2,2\\)" in claims[10]["claim"], \
    "known-present escaped LaTeX absent: the reader is not reading this file"

pool = {}
for p in list(HERE.rglob("*")) + [HERE.parent / "CT-R1-AUDIT" /
                                  "check_invariants.py"]:
    if p.is_file():
        pool[hashlib.sha256(p.read_bytes()).hexdigest()] = p
assert len(pool) > 10

HEX = re.compile(r"\b([0-9a-f]{32,64})\b")
FP = {"a37d6601e12fc9f0": "outputs/rulings_pass.out.txt"}

bad = []
n = 0
for c in claims:
    for h in HEX.findall(c["evidence"]) + HEX.findall(c["claim"]):
        n += 1
        if any(h.startswith(k) or k.startswith(h[:16]) for k in FP):
            src = (HERE / FP[h[:16]]).read_text(encoding="utf-8",
                                                errors="replace")
            if "input fingerprint: " + h[:16] not in src:
                bad.append((c["claim_id"], h, "fingerprint not reported"))
            continue
        m = [v for k, v in pool.items() if k.startswith(h)]
        if len(m) != 1:
            bad.append((c["claim_id"], h, "matches %d files" % len(m)))

print("%d digest citation(s) across %d claims" % (n, len(claims)))
for cid, h, why in bad:
    print("  BROKEN  %s cites %s...  %s" % (cid, h[:16], why))

# --- controls --------------------------------------------------------------
print()
fake = "0" * 64
assert not [v for k, v in pool.items() if k.startswith(fake)], \
    "a digest belonging to nothing resolved"
print("  [PASS] a 64-hex digest belonging to no file does NOT resolve")
print("         would have fired if: the resolver matched loosely")

assert n >= 20, "only %d citations found; the regex may be missing them" % n
print("  [PASS] %d citations were found, so the check is not vacuous" % n)
print("         would have fired if: the regex matched nothing and every")
print("         claim passed for want of anything to check")

meas = hashlib.sha256((HERE / "outputs" / "measure.out.txt").read_bytes()
                      ).hexdigest()
cited_meas = any(meas[:32] in c["evidence"] for c in claims)
assert cited_meas, ("measure.out.txt on disk is %s, which no claim cites: "
                    "measure.py was re-run AFTER the claims were emitted"
                    % meas[:16])
print("  [PASS] measure.out.txt on disk matches the digest the claims cite")
print("         would have fired if: measure.py had been re-run after")
print("         emission, silently invalidating four claims' evidence")

assert not bad, "broken citations: %r" % bad
print()
print("ALL %d CITED DIGESTS RESOLVE." % n)
