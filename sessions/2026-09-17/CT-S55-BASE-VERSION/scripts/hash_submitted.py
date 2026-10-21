#!/usr/bin/env python3
"""CT-S55 -- hash the submitted file, in both forms Editorial Manager serves.

Two distinct artefacts, and the distinction is the whole point:

  (A) the STAMPED build EM compiles for review -- cover pages, line numbers and
      a download-link header stamped over the author's PDF. Its hash cannot
      equal any author file, so a non-match here is uninformative.

  (B) the MANUSCRIPT ITEM itself, fetched through the download link embedded in
      (A) at page 3. EM serves this as uploaded, unstamped. Its hash is
      decisive.

Exit codes: 0 clean, 2 refusal, 3 crash.
"""
import hashlib
import json
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
REFS = SESSION / "refs"
OUT = SESSION / "outputs" / "submitted_file_hash.out.txt"

STAMPED = REFS / "MATH-D-26-00523-EM.pdf"
ITEM = REFS / "EM-manuscript-item-60154-vquad-periodrep-paper-v1.2.pdf"
VERSIONS_JSON = REFS / "zenodo-20719042-versions.json"

# The link fetched to obtain (B), read back out of (A) so it is not a
# remembered string. Verified against the PDF's own annotation below.
ITEM_URI = (
    "https://www2.cloud.editorialmanager.com/math/download.aspx"
    "?id=60154&guid=68eb32f6-b9e2-4cfa-9cdf-e5ccc20ddcbf&scheme=1"
)

CANDIDATES = [
    ("1.0", 20719043, "vquad-periodrep-paper.pdf", "zenodo-v1.0-20719043.pdf"),
    ("1.1", 21410927, "vquad-periodrep-paper-v1.1.pdf", "zenodo-v1.1-21410927.pdf"),
    ("1.2", 21412469, "vquad-periodrep-paper-v1.2.pdf", "zenodo-v1.2-21412469.pdf"),
    ("1.3", 22731371, "vquad-periodrep-paper.pdf", "zenodo-v1.3-22731371.pdf"),
]

LINES: list[str] = []


def say(s: str = "") -> None:
    print(s)
    LINES.append(s)


class Refuse(Exception):
    pass


def digests(p: Path) -> tuple[int, str, str, str]:
    b = p.read_bytes()
    return (
        len(b),
        hashlib.md5(b).hexdigest(),
        hashlib.sha1(b).hexdigest(),
        hashlib.sha256(b).hexdigest(),
    )


def api_md5(blob: dict, rec_id: int, key: str) -> str:
    """Exact field path only -- never a key-name search."""
    for h in blob["hits"]["hits"]:
        if h["id"] != rec_id:
            continue
        for f in h["files"]:
            if f["key"] == key:
                ck = f["checksum"]
                if not ck.startswith("md5:"):
                    raise Refuse(f"record {rec_id} file {key}: checksum {ck!r} is not md5")
                return ck[4:]
        raise Refuse(f"record {rec_id} has no file keyed {key!r}")
    raise Refuse(f"stored API response has no record id {rec_id}")


def main() -> int:
    say("=" * 74)
    say("CT-S55 -- HASH OF THE SUBMITTED FILE")
    say("=" * 74)

    for p in (STAMPED, ITEM, VERSIONS_JSON):
        if not p.exists():
            raise Refuse(f"required artefact missing: {p}")

    # ------------------------------------------------ provenance of the link
    say("")
    say("[0] PROVENANCE OF THE DOWNLOAD LINK")
    d = fitz.open(STAMPED)
    try:
        uris = sorted({
            l["uri"]
            for pi in range(d.page_count)
            for l in d[pi].get_links()
            if l.get("kind") == fitz.LINK_URI and "editorialmanager" in l.get("uri", "")
        })
        stamped_pages = d.page_count
    finally:
        d.close()
    say("    URIs in the stamped build pointing at Editorial Manager:")
    for u in uris:
        say(f"      {u}")
    if ITEM_URI not in uris:
        raise Refuse(
            "the URI this script records as the source of (B) is not present "
            "in the stamped build; the item's provenance is unestablished"
        )
    say("    the link used to fetch (B) is present in (A) -> provenance established")
    say("    (read out of the PDF's own link annotations, not from memory)")

    # --------------------------------------------------------------- the two
    say("")
    say("[1] (A) THE STAMPED BUILD EM COMPILES FOR REVIEW")
    n, m, s1, s2 = digests(STAMPED)
    say(f"    file   : {STAMPED.name}")
    say(f"    pages  : {stamped_pages}   (2 submission cover + 25 manuscript)")
    say(f"    bytes  : {n}")
    say(f"    md5    : {m}")
    say(f"    sha1   : {s1}")
    say(f"    sha256 : {s2}")
    stamped_md5 = m

    say("")
    say("[2] (B) THE MANUSCRIPT ITEM AS UPLOADED, FETCHED THROUGH THAT LINK")
    di = fitz.open(ITEM)
    item_pages = di.page_count
    di.close()
    n, m, s1, s2 = digests(ITEM)
    say(f"    file   : {ITEM.name}")
    say("    served : content-disposition filename=\"vquad-periodrep-paper-v1.2.pdf\"")
    say(f"    pages  : {item_pages}")
    say(f"    bytes  : {n}")
    say(f"    md5    : {m}")
    say(f"    sha1   : {s1}")
    say(f"    sha256 : {s2}")
    item_md5 = m
    item_bytes = ITEM.read_bytes()

    # -------------------------------------------------------- the comparison
    say("")
    say("[3] AGAINST THE FOUR PUBLISHED VERSIONS OF CONCEPT 20719042")
    say("    (md5 resolved by exact path hits.hits[].files[].checksum, then")
    say("     re-verified against the bytes of each downloaded file)")
    say("")
    blob = json.loads(VERSIONS_JSON.read_text(encoding="utf-8"))
    if blob["hits"]["total"] != len(CANDIDATES):
        raise Refuse(
            f"stored API response reports {blob['hits']['total']} versions; "
            f"this script knows {len(CANDIDATES)}"
        )
    hits_a: list[str] = []
    hits_b: list[str] = []
    for ver, rec, key, loc in CANDIDATES:
        want = api_md5(blob, rec, key)
        lb = (REFS / loc).read_bytes()
        got = hashlib.md5(lb).hexdigest()
        if got != want:
            raise Refuse(f"{loc}: computed md5 {got} != API md5 {want}")
        eq_b = got == item_md5
        # md5 equality and byte equality must agree; if they ever disagree the
        # comparison is not measuring what it claims to.
        if eq_b != (lb == item_bytes):
            raise Refuse(f"v{ver}: md5 equality and byte equality disagree")
        if got == stamped_md5:
            hits_a.append(ver)
        if eq_b:
            hits_b.append(ver)
        say(f"    v{ver:<4} rec {rec:<9} {len(lb):>7} bytes  md5 {got}")
        say(f"           vs (A) stamped : {'MATCH' if got == stamped_md5 else 'differs'}")
        say(f"           vs (B) item    : "
            f"{'MATCH -- byte-identical' if eq_b else 'differs'}")

    say("")
    say(f"    (A) stamped build matches : {hits_a if hits_a else 'none of the four'}")
    say(f"    (B) manuscript item matches: {hits_b if hits_b else 'none of the four'}")

    if len(hits_b) != 1:
        raise Refuse(
            f"(B) matches {len(hits_b)} published versions, not exactly one; "
            "the hash does not settle the base"
        )

    say("")
    say("[4] READING")
    say("    (A) matching nothing is the EXPECTED result, not a finding: the")
    say("        stamped build is EM's own re-render and cannot hash to an")
    say("        author file. It is reported so the non-match is not later")
    say("        mistaken for evidence about which version was submitted.")
    say("    (B) is the author PDF as uploaded. Its md5 is decisive.")

    say("")
    say("=" * 74)
    say("SUMMARY")
    say("=" * 74)
    say(f"S55H stamped md5: {stamped_md5}")
    say(f"S55H stamped bytes: {STAMPED.stat().st_size}")
    say(f"S55H stamped pages: {stamped_pages}")
    say(f"S55H stamped matches: {len(hits_a)} of 4")
    say(f"S55H item md5: {item_md5}")
    say(f"S55H item bytes: {ITEM.stat().st_size}")
    say(f"S55H item pages: {item_pages}")
    say(f"S55H item sha256: {hashlib.sha256(item_bytes).hexdigest()}")
    say(f"S55H submitted version: v{hits_b[0]}")
    say(f"S55H submitted record: {next(r for v, r, _, _ in CANDIDATES if v == hits_b[0])}")
    return 0


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        say("")
        say(f"REFUSED: {e}")
        rc = 2
    except Exception as e:  # noqa: BLE001
        say("")
        say(f"CRASH: {type(e).__name__}: {e}")
        rc = 3
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256 ] {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    print(f"[exit   ] {rc}")
    sys.exit(rc)
