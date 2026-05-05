import json, os
from collections import Counter
root = r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"

# DELTA2-VERIFICATION: check -2/9 stratum identity
candidates = [
    r"sessions\2026-04-29\T2B-DELTA2-VERIFICATION\dataset_verification.json",
    r"sessions\2026-04-29\T2B-DELTA2-VERIFICATION\k3_families.json",
]
for cand in candidates:
    p = os.path.join(root, cand)
    if not os.path.exists(p):
        continue
    print(f"=== {cand} ===")
    with open(p, "r", encoding="utf-8") as f:
        try:
            d = json.load(f)
        except Exception as e:
            print(f"  LOAD-ERR {e}"); continue
    if isinstance(d, dict):
        keys = list(d.keys())[:30]
        print(f"  keys[:30]: {keys}")
        for k in ("families", "k3_families", "verified", "data", "trans"):
            if k in d and isinstance(d[k], list):
                fams = d[k]
                print(f"  {k}: {len(fams)} entries; sample: {fams[0] if fams else None}")
                # Try to verify a2 = -2 b1^2 / 9
                ratio_29 = []
                ratio_other = []
                for fam in fams:
                    if not isinstance(fam, dict):
                        continue
                    a2 = fam.get("a2")
                    b1 = fam.get("b1")
                    if a2 is None or b1 is None:
                        continue
                    pred_29 = -2 * b1 * b1 / 9
                    pred_quarter = b1 * b1 / 4
                    is_29 = abs(a2 - pred_29) < 1e-9
                    is_q = abs(a2 - pred_quarter) < 1e-9
                    if is_29:
                        ratio_29.append((a2, b1))
                    elif is_q:
                        ratio_other.append(("+1/4", a2, b1))
                    else:
                        ratio_other.append(("OTHER", a2, b1))
                print(f"    on -2/9 locus (a2 = -2 b1^2/9): {len(ratio_29)}")
                print(f"    on +1/4 locus (a2 = b1^2/4): {sum(1 for r in ratio_other if r[0]=='+1/4')}")
                print(f"    on neither: {sum(1 for r in ratio_other if r[0]=='OTHER')}")
                if any(r[0]=='OTHER' for r in ratio_other):
                    print(f"    OTHER sample: {[r for r in ratio_other if r[0]=='OTHER'][:5]}")
    elif isinstance(d, list):
        print(f"  list length {len(d)}; sample: {d[0] if d else None}")
