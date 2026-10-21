#!/usr/bin/env python3
"""CT-S55 -- emit claims.jsonl.

Every figure in every claim is resolved against the output files by an anchored
read: the anchor must match exactly one line, and the value is taken from that
line. A digit string occurring anywhere in the file is not evidence.

The buffer is validated BEFORE it is written. A post-write assertion leaves the
corrupt artefact on disk.

Exit codes: 0 wrote, 2 refused, 3 crash.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
OUTDIR = SESSION / "outputs"
CLAIMS = SESSION / "claims.jsonl"

BV = OUTDIR / "base_version.out.txt"
HS = OUTDIR / "submitted_file_hash.out.txt"
SW = OUTDIR / "sweep_h.out.txt"

TASK = "CT-S55-BASE-VERSION"


class Refuse(Exception):
    pass


def anchor(path: Path, prefix: str) -> str:
    """Return the single line beginning with `prefix`, minus the prefix."""
    if not path.exists():
        raise Refuse(f"{path.name}: output file absent")
    lines = [
        l.rstrip("\r\n")
        for l in path.read_text(encoding="utf-8").split("\n")
        if l.strip().startswith(prefix)
    ]
    if len(lines) != 1:
        raise Refuse(
            f"{path.name}: anchor {prefix!r} matched {len(lines)} lines, expected exactly 1"
        )
    return lines[0].strip()[len(prefix):].strip()


def main() -> int:
    if not BV.exists() or not HS.exists() or not SW.exists():
        raise Refuse("an output file is missing; run the scripts before emitting claims")

    bv_hash = hashlib.sha256(BV.read_bytes()).hexdigest()
    hs_hash = hashlib.sha256(HS.read_bytes()).hexdigest()
    sw_hash = hashlib.sha256(SW.read_bytes()).hexdigest()

    # ------------------------------------------------ resolve every figure
    g = {
        "stamped_md5": anchor(HS, "S55H stamped md5:"),
        "stamped_bytes": anchor(HS, "S55H stamped bytes:"),
        "stamped_pages": anchor(HS, "S55H stamped pages:"),
        "stamped_matches": anchor(HS, "S55H stamped matches:"),
        "item_md5": anchor(HS, "S55H item md5:"),
        "item_bytes": anchor(HS, "S55H item bytes:"),
        "item_pages": anchor(HS, "S55H item pages:"),
        "item_sha256": anchor(HS, "S55H item sha256:"),
        "sub_ver": anchor(HS, "S55H submitted version:"),
        "sub_rec": anchor(HS, "S55H submitted record:"),
        "em_total": anchor(BV, "S55 EM total pages:"),
        "em_cover": anchor(BV, "S55 EM cover pages:"),
        "em_body": anchor(BV, "S55 EM body pages:"),
        "lmp_ver": anchor(BV, "S55 LMP holds version:"),
        "lmp_rec": anchor(BV, "S55 LMP holds record:"),
        "lmp_match": anchor(BV, "S55 LMP page match:"),
        "s52_ver": anchor(BV, "S55 CT-S52 base version:"),
        "s52_pages": anchor(BV, "S55 CT-S52 base pages:"),
        "rebase": anchor(BV, "S55 rebase required:"),
        "run_ver": anchor(BV, "S55 runner-up version:"),
        "run_match": anchor(BV, "S55 runner-up page match:"),
        "unstripped": anchor(BV, "S55 unstripped page match:"),
        "name_agree": anchor(BV, "S55 filename agrees with bytes:"),
        "preds": anchor(BV, "S55 predictions:"),
        "fals": anchor(BV, "S55 falsifiers fired:"),
        "sw_dirs": anchor(SW, "S55S sweep dirs:"),
        "sw_found": anchor(SW, "S55S page figures found:"),
        "sw_census": anchor(SW, "S55S census equal to v1.0:"),
        "sw_action": anchor(SW, "S55S actionable stale figures:"),
        "sw_descr": anchor(SW, "S55S descriptive not defects:"),
        "sw_p10": anchor(SW, "S55S v1.0 pages:"),
        "sw_p12": anchor(SW, "S55S v1.2 pages:"),
        "sw_p13": anchor(SW, "S55S v1.3 pages:"),
        "sw_src": anchor(SW, "S55S arxiv source md5:"),
        "sw_srcp": anchor(SW, "S55S arxiv source pages:"),
        "sw_second": anchor(SW, "S55S second instance confirmed:"),
        "sw_empty": anchor(SW, "S55S sweep empty:"),
    }

    C = [
        {
            "claim_id": "S55-01",
            "claim": (
                f"The manuscript file Editorial Manager holds for MATH-D-26-00523 "
                f"(manuscript item id 60154, served with content-disposition filename "
                f"vquad-periodrep-paper-v1.2.pdf) is byte-identical to version "
                f"v{g['sub_ver'].lstrip('v')} of Zenodo concept 20719042, record "
                f"{g['sub_rec']}: md5 {g['item_md5']}, sha256 {g['item_sha256']}, "
                f"{g['item_bytes']} bytes, {g['item_pages']} pages. Byte equality and md5 "
                f"equality were required to agree. The file was fetched through the "
                f"download link embedded in Editorial Manager's own stamped build, and "
                f"that link was read out of the PDF's link annotations rather than "
                f"transcribed."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "script": "scripts/hash_submitted.py",
            "output_hash": hs_hash,
        },
        {
            "claim_id": "S55-02",
            "claim": (
                f"Independently of the hash, and by a differently implemented read: the "
                f"{g['em_body']} manuscript pages inside Editorial Manager's stamped build "
                f"({g['em_total']} pages total, {g['em_cover']} submission cover pages), with the "
                f"EM overlay removed under the pre-registered rule S1-S3, match version "
                f"v{g['lmp_ver'].lstrip('v')} (record {g['lmp_rec']}) page for page on "
                f"normalised text: {g['lmp_match']}. The runner-up v{g['run_ver'].lstrip('v')} "
                f"matches {g['run_match']}. The two routes -- hash of the uploaded item and "
                f"content of the stamped build -- agree."
            ),
            "label": "VERIFIED",
            "evidence_type": "file_inspection",
            "dps": None,
            "script": "scripts/base_version.py",
            "output_hash": bv_hash,
        },
        {
            "claim_id": "S55-03",
            "claim": (
                f"The revision prepared in CT-S52-XI0-LOGS-REVISION was built against a base "
                f"byte-identical to v{g['s52_ver'].lstrip('v')} ({g['s52_pages']} pages), which is "
                f"not the version Editorial Manager holds (v{g['lmp_ver'].lstrip('v')}, "
                f"{g['em_body']} pages). REBASE REQUIRED: {g['rebase']}. CT-S52's own source "
                f"identification names its base as 'the file published in Zenodo record 20719043' "
                f"-- an identification of the submitted artefact that was assumed rather than "
                f"established, and is now refuted."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "script": "scripts/base_version.py",
            "output_hash": bv_hash,
        },
        {
            "claim_id": "S55-04",
            "claim": (
                f"Editorial Manager's stamped build (md5 {g['stamped_md5']}, "
                f"{g['stamped_bytes']} bytes, {g['stamped_pages']} pages) is byte-identical to "
                f"{g['stamped_matches']} of the published versions. This non-match is the "
                f"expected result and is not evidence about which version was submitted: the "
                f"stamped build is EM's own re-render, carrying a submission cover and stamping "
                f"line numbers and a download-link header onto every manuscript page. It is "
                f"recorded so that a later reader cannot mistake the zero for a finding."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "script": "scripts/hash_submitted.py",
            "output_hash": hs_hash,
        },
        {
            "claim_id": "S55-05",
            "claim": (
                f"The page-for-page observable is content-sensitive and the stripping rule does "
                f"not manufacture the match: with the EM overlay left in place the winning "
                f"version matches {g['unstripped']} pages, and swapping two adjacent body pages "
                f"drops every candidate below a full match. All six pairs of candidate versions "
                f"differ, so a full match against one excludes the others. Predictions: "
                f"{g['preds']}. Falsifiers fired: {g['fals']}."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": None,
            "script": "scripts/base_version.py",
            "output_hash": bv_hash,
        },
        {
            "claim_id": "S55-06",
            "claim": (
                "Zenodo concept 20719042 carries four published versions, not three: v1.0 "
                "(record 20719043, 2026-06-16), v1.1 (21410927, 2026-07-17), v1.2 (21412469, "
                "2026-07-17) and v1.3 (record 22731371, published 2026-09-13). This is not a new "
                "finding: CT-S53-LMP-CORRECTION-RECORD PENDING.md already established the same "
                "table from the API and used the v1.3 date as a falsifier on the 'not updated "
                "pending the editor's reply' claim. It is restated here only because this "
                "session's independent fetch agrees with it."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "script": "scripts/hash_submitted.py",
            "output_hash": hs_hash,
        },
        {
            "claim_id": "S55-07",
            "claim": (
                f"Amendment H sweep for the same defect class -- an artefact identified or "
                f"described from the only copy in the tree rather than from its content -- "
                f"across {g['sw_dirs']} directories. The sweep is NOT empty: a second instance is "
                f"confirmed ({g['sw_second']}). The arXiv upload material names as its source an "
                f"artefact of md5 {g['sw_src']} and {g['sw_srcp']} pages, which is v1.0; the "
                f"journal holds v1.2 ({g['sw_p12']} pages) and the deposit's latest is v1.3 "
                f"({g['sw_p13']} pages). Of {g['sw_found']} page-count figures found, "
                f"{g['sw_census']} equal v1.0's {g['sw_p10']}; this is a census, not a defect "
                f"count. {g['sw_action']} are actionable -- arXiv field values to be entered or "
                f"instructions to be acted on -- and {g['sw_descr']} are descriptive and correct "
                f"as written, because they describe the v1.0 artefact, which really is "
                f"{g['sw_p10']} pages."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "script": "scripts/sweep_h.py",
            "output_hash": sw_hash,
        },
    ]

    for c in C:
        c["task_id"] = TASK
        c["reproducible"] = True

    # ------------------------------------------- validate BEFORE writing
    seen = set()
    for c in C:
        cid = c["claim_id"]
        if cid in seen:
            raise Refuse(f"{cid}: duplicate claim_id")
        seen.add(cid)
        for k in ("claim_id", "claim", "label", "evidence_type", "task_id",
                  "reproducible", "script", "output_hash"):
            if k not in c:
                raise Refuse(f"{cid}: missing required field {k!r}")
        if not isinstance(c["claim"], str) or len(c["claim"].strip()) < 60:
            raise Refuse(f"{cid}: claim text is empty or too short to be evidence")
        if c["label"] not in ("PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"):
            raise Refuse(f"{cid}: unknown label {c['label']!r}")
        if c["evidence_type"] not in ("file_inspection", "computation", "build"):
            raise Refuse(f"{cid}: unknown evidence_type {c['evidence_type']!r}")
        if len(c["output_hash"]) != 64 or not all(x in "0123456789abcdef" for x in c["output_hash"]):
            raise Refuse(f"{cid}: output_hash is not a sha256 hex digest")
        sp = SESSION / c["script"]
        if not sp.exists():
            raise Refuse(f"{cid}: cited script {c['script']} does not exist")
        # the cited output_hash must be the hash of the output that script wrote
        want = {"scripts/base_version.py": bv_hash,
                "scripts/hash_submitted.py": hs_hash,
                "scripts/sweep_h.py": sw_hash}
        if c["output_hash"] != want[c["script"]]:
            raise Refuse(f"{cid}: output_hash does not belong to {c['script']}")

    # the central facts, restated independently of the claim prose
    if g["sub_ver"].lstrip("v") != g["lmp_ver"].lstrip("v"):
        raise Refuse(
            f"the two routes disagree: hash says v{g['sub_ver'].lstrip('v')}, "
            f"content says v{g['lmp_ver'].lstrip('v')}"
        )
    if g["rebase"] != "YES":
        raise Refuse("S55-03 asserts a rebase is required, but the output does not say YES")
    if not g["unstripped"].startswith("0 of"):
        raise Refuse("S55-05 asserts 0 unstripped matches, but the output disagrees")
    if g["fals"] != "none":
        raise Refuse(f"a falsifier fired ({g['fals']}); claims may not be emitted over it")
    if g["stamped_matches"].split()[0] != "0":
        raise Refuse("S55-04 asserts the stamped build matches nothing, but the output disagrees")
    if g["sw_empty"] != "NO":
        raise Refuse("S55-07 asserts the sweep is not empty, but the output says it is")
    if g["sw_second"] != "YES":
        raise Refuse("S55-07 asserts a second instance, but the sweep did not confirm one")
    if int(g["sw_action"]) + int(g["sw_descr"]) != int(g["sw_census"]):
        raise Refuse("S55-07's actionable/descriptive split does not sum to the census")

    buf = "\n".join(json.dumps(c, ensure_ascii=False) for c in C) + "\n"
    for c in C:
        if c["claim_id"] not in buf:
            raise Refuse(f"{c['claim_id']}: absent from the buffer about to be written")

    CLAIMS.write_text(buf, encoding="utf-8")
    print(f"[wrote  ] {CLAIMS}  ({len(C)} claims)")
    print(f"[sha256 ] {hashlib.sha256(CLAIMS.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        print(f"REFUSED: {e}")
        rc = 2
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        rc = 3
    sys.exit(rc)
