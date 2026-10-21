"""Append S21-75: the unresolvable pointer caught in the drafted description edit.

Derives the paragraph evidence from the published record JSON rather than
restating it. Refuses to double-append.
"""
import hashlib
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RECID = "22831933"
CLAIM_ID = "S21-75"

rights = json.loads((HERE / "outputs" / f"rights_{RECID}.json").read_text(encoding="utf-8"))
desc = rights["metadata"]["description"]
paras = [html.unescape(re.sub(r"<.*?>", "", p)).strip()
         for p in re.findall(r"<p>(.*?)</p>", desc, re.S)]

# Evidence the pointer is unresolvable: "five items" is announced, but no
# paragraph of the notice block is labelled with a numeral.
notice = paras[:5]
assert "five items" in notice[0], notice[0][:80]
numbered = [p for p in notice if re.match(r"^\(?\s*(1|2|3|i|I)\b[.)]", p)]

# Evidence C1 is contradicted twice in the retained abstract.
abstract = paras[5:8]
hits = [i + 5 for i, p in enumerate(abstract)
        if "forces both finite singularities to be apparent" in p
        or "apparent singularity positions are the roots" in p]

# Evidence the version-history blocks carry bold labels and the v1.3 block does not.
labelled = re.findall(r"<strong>(Version 1\.[0-9][^<]*)</strong>", desc)

claim = {
    "claim_id": CLAIM_ID,
    "task_id": "CT-S21-DEPOSIT-PREP",
    "claim": (
        "Two presentation defects in the published v1.3 description, and one defect in the "
        "wording drafted to fix them. (a) The v1.3 correction notice occupies paragraphs 0-4 "
        f"with no bolded label, while the version history carries {len(labelled)} labelled "
        f"blocks ({'; '.join(labelled)}), so the newest notice was the only unlabelled one. "
        "(b) The retained v1.2 abstract contradicts correction C1 in TWO paragraphs, not one: "
        f"indices {hits} of the description, the second generalising the refuted claim to every "
        "polynomial continued fraction and standing as the abstract's final sentence. (c) The "
        "drafted boundary sentence pointed the reader to 'item 1 above', but although paragraph "
        "0 announces five items, the notice block is prose and "
        f"{len(numbered)} of its 5 paragraphs carry a leading numeral, so the pointer resolves "
        "to nothing on the rendered page; it was replaced with 'the first correction above', "
        "which names its target instead of indexing it. Edits staged in DESCRIPTION-EDIT.md and "
        "gated on the operator; they are metadata edits on the published record, which leave the "
        "frozen file set and the DOI untouched."
    ),
    "label": "INSPECTED",
    "evidence_type": "file_inspection",
    "dps": None,
    "reproducible": True,
    "script": "scripts/append_s21_75.py",
    "output_hash": hashlib.sha256(
        (HERE / "outputs" / f"rights_{RECID}.json").read_bytes()).hexdigest(),
}

claims = HERE / "claims.jsonl"
existing = {json.loads(l)["claim_id"] for l in claims.read_text(encoding="utf-8").splitlines() if l.strip()}
if CLAIM_ID in existing:
    print(f"{CLAIM_ID} already present; nothing appended")
else:
    with claims.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(claim, ensure_ascii=True) + "\n")
    print(f"{CLAIM_ID} appended")

print(f"labelled version blocks : {labelled}")
print(f"numbered notice paras   : {len(numbered)} of {len(notice)}")
print(f"C1 contradicted at paras: {hits}")
