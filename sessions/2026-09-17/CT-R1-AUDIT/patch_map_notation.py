"""R14: normalise the inversion notation to z -> 1/x (operator review #10).

B's coordinate is z, C's is x, so the map naming both coordinates is the
accurate one. Only the three claims that state the B-C equivalence are touched;
'1/z' also occurs inside Zenodo DOIs (5281/zenodo) and in earlier, unrelated
object-A material, which must not be rewritten.
"""
import json
import shutil

SRC = "claims.jsonl"
TARGETS = {"R1-82", "R1-87", "R1-89"}
OLD = "z -> 1/z"
NEW = "z -> 1/x"

shutil.copy(SRC, SRC + ".bak-r14")

rows = [json.loads(l) for l in open(SRC, encoding="utf-8") if l.strip()]
n_in = len(rows)
touched = []
for c in rows:
    if c["claim_id"] in TARGETS and OLD in c["claim"]:
        c["claim"] = c["claim"].replace(OLD, NEW)
        touched.append(c["claim_id"])

missing = TARGETS - set(touched)
if missing:
    raise SystemExit(f"ABORT: expected claims not rewritten: {sorted(missing)}")

with open(SRC, "w", encoding="utf-8") as f:
    for c in rows:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

n_out = sum(1 for l in open(SRC, encoding="utf-8") if l.strip())
print(f"in={n_in} out={n_out} rewritten={sorted(touched)}")
if n_in != n_out:
    raise SystemExit("ABORT: row count changed")
print("OK")
