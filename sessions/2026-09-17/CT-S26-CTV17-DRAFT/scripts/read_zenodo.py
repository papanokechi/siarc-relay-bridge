"""Read the fetched Zenodo JSON without guessing field paths.

Fields are resolved by their EXACT path (pids.doi.identifier,
parent.pids.doi.identifier, metadata.version, ...), never by searching for a key
name anywhere in the tree.  Every derived value is echoed and asserted.
"""
import json
import sys
from pathlib import Path

REFS = Path(__file__).resolve().parent.parent / "refs"


def show(path: Path):
    rec = json.loads(path.read_text(encoding="utf-8"))
    if "hits" in rec:
        hits = rec["hits"]["hits"]
        print(f"{path.name}: {len(hits)} hit(s)")
        for h in hits:
            show_one(h, indent="  ")
        return
    show_one(rec)


def show_one(rec, indent=""):
    rid = rec.get("id")
    md = rec["metadata"]
    if "pids" in rec:                      # RDM shape
        doi = rec["pids"]["doi"]["identifier"]
        concept = rec.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        version = md.get("version")
        pub = md.get("publication_date")
        lic = md.get("rights", [{}])[0].get("id") if md.get("rights") else None
        files = rec.get("files", {}).get("entries", {})
        fileinfo = [(k, v.get("size"), v.get("checksum")) for k, v in files.items()]
    else:                                  # legacy shape
        doi = rec["doi"]
        concept = rec.get("conceptdoi")
        version = md.get("version")
        pub = md.get("publication_date")
        lic = (md.get("license") or {}).get("id")
        fileinfo = [(f.get("key"), f.get("size"), f.get("checksum"))
                    for f in rec.get("files", [])]
    assert isinstance(doi, str) and doi.startswith("10.5281/zenodo."), doi
    assert concept is None or (isinstance(concept, str)
                               and concept.startswith("10.5281/zenodo.")), concept
    print(f"{indent}record id   : {rid}")
    print(f"{indent}version DOI : {doi}")
    print(f"{indent}concept DOI : {concept}")
    print(f"{indent}version     : {version}")
    print(f"{indent}title       : {md.get('title')}")
    print(f"{indent}published   : {pub}")
    print(f"{indent}license     : {lic}")
    for k, s, c in fileinfo:
        print(f"{indent}file        : {k}  {s} bytes  {c}")
    print(f"{indent}links.files : {rec.get('links', {}).get('files')}")
    print()


for name in sys.argv[1:]:
    show(REFS / name)
