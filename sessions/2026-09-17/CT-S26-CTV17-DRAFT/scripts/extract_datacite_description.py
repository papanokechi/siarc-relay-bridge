"""Extract descriptions from a DataCite DOI record (Zenodo fallback route).

Used when zenodo.org returns 504.  Fields are read by exact path
(data.attributes.descriptions[i].description), never by key search.
"""
import html
import json
import re
import sys
from pathlib import Path

REFS = Path(__file__).resolve().parent.parent / "refs"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_description import to_text  # noqa: E402

for name in sys.argv[1:]:
    p = REFS / name
    attrs = json.loads(p.read_text(encoding="utf-8"))["data"]["attributes"]
    doi = attrs["doi"]
    ver = attrs.get("version")
    descs = attrs["descriptions"]
    assert descs, f"{doi}: no descriptions"
    body = "\n\n".join(d["description"] for d in descs
                       if d.get("descriptionType") in (None, "Abstract", "Other"))
    assert body.strip(), f"{doi}: empty description body"
    txt = to_text(body)
    out = p.with_suffix(".description.txt")
    out.write_text(txt, encoding="utf-8", newline="\n")
    assert out.read_text(encoding="utf-8") == txt, "read-back mismatch"
    print(f"{p.name}: doi {doi}  version {ver!r}  {len(descs)} description(s)  "
          f"text {len(txt)} B -> {out.name}")
