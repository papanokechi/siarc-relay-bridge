"""List every file_inspection claim in the corpus, for the INSPECTED relabel."""
import json, glob, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
for f in sorted(BASE.glob("CT-*/claims.jsonl")):
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        c = json.loads(line)
        if c.get("evidence_type") == "file_inspection":
            print(f'{c["claim_id"]:9} {c["label"]:12} {c["claim"][:100]}')
