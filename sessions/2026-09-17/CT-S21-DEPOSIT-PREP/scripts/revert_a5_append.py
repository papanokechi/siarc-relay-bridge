"""Revert the bad A5 append (version DOI resolved to a dict, concept to a bare id).

Removes only the blocks this session wrote moments ago, by locating their exact
opening markers. Asserts each marker occurs exactly once before cutting.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
R1 = HERE.parent / "CT-R1-AUDIT"

cuts = [
    (R1 / "REFS-MANIFEST.md", "\n---\n\n## Own deposit: companion v1.3"),
    (R1 / "AUDIT.md", "\n\n## R34. The companion v1.3 deposit, published"),
]
for path, marker in cuts:
    t = path.read_text(encoding="utf-8")
    n = t.count(marker)
    assert n == 1, f"{path.name}: marker occurs {n} times, refusing to cut"
    path.write_text(t[: t.index(marker)].rstrip("\n") + "\n", encoding="utf-8")
    print(f"{path.name}: reverted")

claims = HERE / "claims.jsonl"
lines = [l for l in claims.read_text(encoding="utf-8").splitlines() if l.strip()]
drop = {"S21-71", "S21-72", "S21-73", "S21-74"}
kept = [l for l in lines if json.loads(l)["claim_id"] not in drop]
print(f"claims.jsonl: {len(lines)} -> {len(kept)} (dropped {len(lines) - len(kept)})")
claims.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
print(f"claims.jsonl: {len(lines)} -> {len(kept)}")
