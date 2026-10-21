"""Per-round invariant check over the whole session corpus.

Run at the end of every round, before appending a new AUDIT.md section.
Exit code is nonzero if any invariant fails.

Invariants
  1(a)  no `file_inspection` claim carries the label PROVEN
  1(b)  every claim_id is unique across the corpus
  2     every claim carries exactly one recognised label
  3     every claim with a `review` field also carries a `review_note`
  4     `review` is one of self | cold | lean
"""
import json
import pathlib
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}
REVIEWS = {"self", "cold", "lean"}

claims = []
for path in sorted(ROOT.rglob("claims.jsonl")):
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            print(f"FAIL parse  {path.relative_to(ROOT)}:{lineno}: {exc}")
            sys.exit(2)
        claims.append((path.relative_to(ROOT), lineno, obj))

print(f"corpus: {len(claims)} claims in {len({p for p, _, _ in claims})} files\n")

fails = 0

# --- 1(b) duplicate claim_id ------------------------------------------------
seen = defaultdict(list)
for path, lineno, c in claims:
    cid = c.get("claim_id")
    if cid:
        seen[cid].append(f"{path}:{lineno}")
dups = {k: v for k, v in seen.items() if len(v) > 1}
if dups:
    fails += 1
    print(f"FAIL 1(b): {len(dups)} duplicate claim_id(s)")
    for k, v in sorted(dups.items()):
        print(f"   {k}: {v}")
else:
    print(f"ok   1(b): all {len(seen)} claim_ids unique")

# --- 1(a) PROVEN must not rest on file inspection ---------------------------
bad = [f"{p}:{n} {c.get('claim_id')}" for p, n, c in claims
       if c.get("label") == "PROVEN" and c.get("evidence_type") == "file_inspection"]
if bad:
    fails += 1
    print(f"FAIL 1(a): {len(bad)} PROVEN claims with evidence_type=file_inspection")
    for b in bad:
        print("  ", b)
else:
    print("ok   1(a): no PROVEN claim rests on file_inspection")

# --- 2 exactly one recognised label ----------------------------------------
bad = [f"{p}:{n} {c.get('claim_id')} -> {c.get('label')!r}" for p, n, c in claims
       if c.get("label") not in LABELS]
if bad:
    fails += 1
    print(f"FAIL 2: {len(bad)} claim(s) with an unrecognised or missing label")
    for b in bad[:20]:
        print("  ", b)
else:
    print("ok   2: every claim carries exactly one recognised label")

# --- 3/4 review field well-formed ------------------------------------------
missing_note = [f"{p}:{n} {c.get('claim_id')}" for p, n, c in claims
                if c.get("review") and not c.get("review_note")]
bad_val = [f"{p}:{n} {c.get('claim_id')} -> {c.get('review')!r}" for p, n, c in claims
           if c.get("review") and c.get("review") not in REVIEWS]
if missing_note:
    fails += 1
    print(f"FAIL 3: {len(missing_note)} reviewed claim(s) with no review_note")
    for b in missing_note[:20]:
        print("  ", b)
else:
    print("ok   3: every reviewed claim carries a review_note")
if bad_val:
    fails += 1
    print(f"FAIL 4: {len(bad_val)} claim(s) with an unrecognised review value")
    for b in bad_val:
        print("  ", b)
else:
    print("ok   4: every review value is one of self|cold|lean")

# --- summary ----------------------------------------------------------------
tally = defaultdict(int)
rev = defaultdict(int)
for _, _, c in claims:
    tally[c.get("label")] += 1
    rev[c.get("review", "(none)")] += 1
print("\nlabels: " + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
print("review: " + "  ".join(f"{k}={v}" for k, v in sorted(rev.items())))
print("\n" + ("INVARIANTS OK" if not fails else f"{fails} INVARIANT(S) FAILED"))
sys.exit(1 if fails else 0)
