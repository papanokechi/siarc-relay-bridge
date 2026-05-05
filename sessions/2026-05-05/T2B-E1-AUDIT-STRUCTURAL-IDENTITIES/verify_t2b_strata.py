import json, sys, os, re
root = r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"

# +1/4 stratum check
with open(os.path.join(root, r"sessions\2026-04-29\T2B-PLUS-QUARTER-SURVEY\families.json"), "r", encoding="utf-8") as f:
    pq = json.load(f)
fams = pq["families"]
print(f"+1/4 stratum: {len(fams)} families in PLUS-QUARTER dataset")
mismatches = []
for fam in fams:
    a2, b1 = fam["a2"], fam["b1"]
    if (b1 * b1) % 4 != 0:
        mismatches.append((a2, b1, "b1^2 not divisible by 4"))
        continue
    pred = (b1 * b1) // 4
    if a2 != pred:
        mismatches.append((a2, b1, f"a2={a2} but b1^2/4={pred}"))
if not mismatches:
    print("  ALL 15 satisfy a2 = b1^2/4 (Delta = 2 b1^2). Discriminant identity VERIFIED.")
else:
    print(f"  {len(mismatches)} mismatches:")
    for m in mismatches:
        print(f"    {m}")
# Distribution by sign of a2 and by b1
from collections import Counter
signs = Counter("a2>0" if fam["a2"] > 0 else ("a2<0" if fam["a2"] < 0 else "a2=0") for fam in fams)
b1signs = Counter("b1>0" if fam["b1"] > 0 else ("b1<0" if fam["b1"] < 0 else "b1=0") for fam in fams)
print(f"  Sign distribution: {dict(signs)}")
print(f"  b1 sign distribution: {dict(b1signs)}")
b1_values = sorted({fam["b1"] for fam in fams})
print(f"  b1 values present: {b1_values}")
print()

# Today's sweep scope
with open(os.path.join(root, r"sessions\2026-05-05\T2B-RESONANCE-B67-B6-DISPATCH\t2b_b67_b6_dispatch.py"), "r", encoding="utf-8") as f:
    src = f.read()
print("TODAY's b1=6 sweep scope (key lines):")
for ln in src.split("\n"):
    if any(k in ln for k in ["A2_RANGE", "a2_range", "range(1, 31)", "A2_MIN", "A2_MAX", "for a2", "a2 in range"]):
        print(f"  {ln.strip()[:140]}")
