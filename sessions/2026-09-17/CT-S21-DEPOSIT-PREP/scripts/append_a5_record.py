"""A5 post-publish record: REFS-MANIFEST row, AUDIT section, claims.

Every value is derived from outputs/postpublish_22831933.json (the hashed
readback of the live record) and from the bytes on disk. Nothing is retyped.
Refuses to double-append.
"""
import hashlib
import json
import pathlib
import datetime

HERE = pathlib.Path(__file__).resolve().parent.parent
R1 = HERE.parent / "CT-R1-AUDIT"
RECID = "22831933"

readback = json.loads((HERE / "outputs" / f"postpublish_{RECID}.json").read_text(encoding="utf-8"))
rights = json.loads((HERE / "outputs" / f"rights_{RECID}.json").read_text(encoding="utf-8"))


def dig(obj, *names):
    """Find the first of `names` anywhere in a nested structure."""
    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            for k, v in cur.items():
                if k in names:
                    return v
                stack.append(v)
        elif isinstance(cur, list):
            stack.extend(cur)
    return None


meta = rights["metadata"]
version_doi = rights["pids"]["doi"]["identifier"]
conceptdoi = rights["parent"]["pids"]["doi"]["identifier"]
pubdate = meta["publication_date"]
_rb = HERE / "outputs" / f"postpublish_{RECID}.json"
retrieved = datetime.datetime.fromtimestamp(
    _rb.stat().st_mtime, datetime.timezone.utc).astimezone().isoformat(timespec="seconds")
record_updated = readback["updated"]
assert retrieved.startswith("20"), f"retrieved: {retrieved!r}"
for name, val in (("version_doi", version_doi), ("conceptdoi", conceptdoi)):
    assert isinstance(val, str) and val.startswith("10.5281/zenodo."), f"{name}: {val!r}"
assert conceptdoi.endswith("20455089"), f"concept DOI moved: {conceptdoi}"
version = meta.get("version")
title = meta["title"]
licence = [r.get("id") for r in meta.get("rights", [])]
preview = rights.get("files", {}).get("default_preview")
nkw = len(meta.get("subjects", []))
creators = [(c["person_or_org"]["name"], [a["name"] for a in c.get("affiliations", [])])
            for c in meta["creators"]]
creators_str = "; ".join(f"{n} ({', '.join(a)})" for n, a in creators)
rel = meta.get("related_identifiers", [])

live_files = {f["key"]: f for f in rights["files"]["entries"].values()} \
    if isinstance(rights["files"].get("entries"), dict) else {}
assert len(live_files) == 2, f"expected 2 published files, found {sorted(live_files)}"


def local(name):
    b = (HERE / "upload" / name).read_bytes()
    return len(b), hashlib.sha256(b).hexdigest(), hashlib.md5(b).hexdigest()


files = {}
for name in ("vquad_resurgence.pdf", "vquad_resurgence_v1.3_correction_notice.md"):
    size, sha, md5 = local(name)
    entry = live_files.get(name)
    assert entry is not None, f"{name} not present in the published record"
    assert entry["checksum"] == f"md5:{md5}", f"{name}: live md5 != local md5"
    assert entry["size"] == size, f"{name}: live size != local size"
    files[name] = (size, sha, md5)

# ---------------------------------------------------------------- manifest
manifest = R1 / "REFS-MANIFEST.md"
text = manifest.read_text(encoding="utf-8")
if RECID in text:
    print("REFS-MANIFEST.md already carries the record; not appending")
else:
    rows = "\n".join(
        f"| `{n}` | `https://zenodo.org/records/{RECID}` | **{licence[0]}** | {s} | `{h}` |"
        for n, (s, h, _m) in files.items()
    )
    manifest.write_text(
        text.rstrip("\n") + f"""

---

## Own deposit: companion v1.3 (published {pubdate}, retrieved {retrieved})

Version DOI `{version_doi}` · record `{RECID}` · concept DOI `{conceptdoi}`.
This is the deposit's own CC-BY work, not a third-party reference: it is
redistributable, unlike the paywalled and all-rights-reserved entries above.
Sizes and sha256 are of the local copies in
`CT-S21-DEPOSIT-PREP/upload/`, each verified equal in size and md5 to the
published file entry of the same key.

| file | source | licence | bytes | sha256 |
|---|---|---|---|---|
{rows}
""",
        encoding="utf-8",
    )
    print("REFS-MANIFEST.md appended")

# ------------------------------------------------------------------- audit
audit = R1 / "AUDIT.md"
atext = audit.read_text(encoding="utf-8")
if f"zenodo.{RECID}" in atext:
    print("AUDIT.md already carries the record; not appending")
else:
    audit.write_text(
        atext.rstrip("\n") + f"""

## R34. The companion v1.3 deposit, published

Published {pubdate} as a **new version** of record `20481592`, not a new
upload: version DOI `{version_doi}`, record `{RECID}`, concept DOI
`{conceptdoi}` unchanged. Version `{version}`. Licence `{licence[0]}`.
Title byte-identical to v1.2. Creators: {creators_str}. {nkw} keywords: the nine
carried over in their stored order plus `correction notice` and
`isomonodromic deformation`. Exactly one related identifier, unchanged from
v1.2: `{rel[0]['identifier']}`, relation `{rel[0]['relation_type']['id']}`. No
row was added for the v1.2 record, because Zenodo carries version lineage in
`metadata.relations.version`, outside `related_identifiers`, and DataCite has
no `corrects` relation.

Two files. The correction notice, and the v1.2 paper retained unchanged --- the
ruling of R31, taken because a concept DOI that resolves to an erratum with no
paper strands every reader following a citation. `default_preview` is
`{preview}`, so the landing page shows the manuscript and the erratum is read
as the description. Both files were verified after publication against the
bytes on disk, and the paper additionally against the v1.2 record's own stored
file entry, so the manuscript in the new version is byte-identical to the one
already cited.

**The last defect caught was in a filename, again.** The paper was first
uploaded from `CT-R1-AUDIT/refs/`, where it is stored under the descriptive
name `vquad_resurgence_v1.2_zenodo-20481592.pdf`. That name embeds record
`20481592` in a file published on record `{RECID}`, and Zenodo publishes the
filename it is given and freezes the file set at publish. No content scan could
reach it: the bytes were correct and the label was on the outside. This is the
third instance of the class this round, after the `DRAFT-` prefix and the Jimbo
packet mislabel, and it is the reason the staged copy carries the v1.2 record's
own published file key rather than a name chosen for the shelf it sat on
(S21-71, S21-72).

The whole round's defect class, stated once: **true when written, wrong at
deposit.** A stale checklist header, a self-addressed instruction, a stale hash,
a `DRAFT` H1, a `DRAFT-` filename, a stale upload-target line, a count reused
with a changed referent, a mis-named file, and an abstract whose refuted claims
sit four paragraphs below the correction that overturns them. Every one is a
duplicate drifting from the thing it describes. The countermeasure that held was
not a better checker but a rule about authorship: `FORM-VALUES.md` derives its
values from the record JSON instead of retyping them, and `UPLOAD-SCREENS.md`
quotes no field value at all.
""",
        encoding="utf-8",
    )
    print("AUDIT.md appended")

# ------------------------------------------------------------------ claims
claims = HERE / "claims.jsonl"
ctext = claims.read_text(encoding="utf-8")
out_hash = hashlib.sha256(
    (HERE / "outputs" / f"postpublish_{RECID}.json").read_bytes()).hexdigest()

new = [
    {
        "claim_id": "S21-71",
        "task_id": "CT-S21-DEPOSIT-PREP",
        "claim": (
            f"Companion v1.3 is published at version DOI {version_doi} (record {RECID}, "
            f"published {pubdate}) as a new version of record 20481592; concept DOI is still "
            f"{conceptdoi}. Ten post-publish checks passed: concept DOI unchanged, version "
            f"{version}, title byte-identical to v1.2, paper present with md5 unchanged, notice "
            "present under its publishable name with md5 and size equal to the local file, no "
            "filename containing DRAFT, and exactly one related identifier "
            f"({rel[0]['identifier']}, {rel[0]['relation_type']['id']}) unchanged from v1.2. "
            f"Licence {licence[0]}; default_preview {preview}; {nkw} keywords; creator "
            f"{creators[0][0]} with affiliation {creators[0][1][0]}."
        ),
        "label": "VERIFIED",
        "evidence_type": "computation",
        "dps": None,
        "reproducible": True,
        "script": "scripts/postpublish_readback.py",
        "output_hash": out_hash,
    },
    {
        "claim_id": "S21-72",
        "task_id": "CT-S21-DEPOSIT-PREP",
        "claim": (
            "DEFECT CAUGHT AT THE BOUNDARY: the v1.2 paper was first uploaded to the v1.3 draft "
            "from CT-R1-AUDIT/refs/, carrying the shelf name "
            "vquad_resurgence_v1.2_zenodo-20481592.pdf, which embeds record 20481592 in a file "
            f"published on record {RECID}. Zenodo publishes the filename it is given and forbids "
            "file addition, removal or modification after publish, so the wrong label would have "
            "frozen permanently. The bytes were correct throughout, so no content scan could "
            "reach it. The row was replaced before publish with the staged copy carrying the "
            "v1.2 record's published file key vquad_resurgence.pdf, and the published record was "
            "read back to confirm the key. Third instance this round of a wrong label baked into "
            "a name, after the DRAFT- prefix and the Jimbo packet mislabel."
        ),
        "label": "VERIFIED",
        "evidence_type": "computation",
        "dps": None,
        "reproducible": True,
        "script": "scripts/postpublish_readback.py",
        "output_hash": out_hash,
    },
    {
        "claim_id": "S21-73",
        "task_id": "CT-S21-DEPOSIT-PREP",
        "claim": (
            "NOT ESTABLISHED at deposit, recorded so it is not mistaken for settled: the v1.2 "
            "abstract is carried unchanged in the v1.3 description, four paragraphs below the "
            "correction notice, and still states that the exact-ODE structure forces both finite "
            "singularities to be apparent (refuted by C1) and that beta = gamma = 0 by the stated "
            "derivation (refuted by C2, gamma = 1 on the companion's own data). Keeping the "
            "abstract is deliberate, since it describes the paper file that is in the record, but "
            "no separator paragraph marking the boundary was confirmed present at publish. The "
            "description is editable after publication; the file set is not."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/postpublish_readback.py",
        "output_hash": out_hash,
    },
    {
        "claim_id": "S21-74",
        "task_id": "CT-S21-DEPOSIT-PREP",
        "claim": (
            "SELF-CAUGHT DEFECT in the A5 recording script, first pass: version_doi and "
            "conceptdoi were resolved by a recursive search for any key named 'doi', which found "
            "the pids.doi OBJECT rather than its identifier string, so the first append wrote the "
            "Python repr {'identifier': ..., 'provider': 'datacite', ...} into AUDIT.md and the "
            "manifest, and wrote the parent RECORD ID 20455089 where the concept DOI "
            "10.5281/zenodo.20455089 belonged. Caught by reading the script's echoed values "
            "rather than its exit code, which was 0. The three appended blocks were reverted by "
            "scripts/revert_a5_append.py and the derivation was repaired to read "
            "pids.doi.identifier and parent.pids.doi.identifier explicitly, with assertions that "
            "both are strings beginning 10.5281/zenodo. and that the concept DOI still ends "
            "20455089. Same class as the stored memory that a record's concept DOI is not its "
            "record number, and the same shape as the round's own defect: a value retyped or "
            "guessed at instead of derived from the field that holds it."
        ),
        "label": "INSPECTED",
        "evidence_type": "computation",
        "dps": None,
        "reproducible": True,
        "script": "scripts/append_a5_record.py",
        "output_hash": out_hash,
    },
]

existing = {json.loads(l)["claim_id"] for l in ctext.splitlines() if l.strip()}
added = 0
with claims.open("a", encoding="utf-8", newline="\n") as fh:
    for c in new:
        if c["claim_id"] in existing:
            print(f"{c['claim_id']} already present; skipped")
            continue
        fh.write(json.dumps(c, ensure_ascii=True) + "\n")
        added += 1
print(f"claims appended: {added}")
print(f"version_doi {version_doi} | concept {conceptdoi} | licence {licence} | preview {preview}")
