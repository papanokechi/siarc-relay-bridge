#!/usr/bin/env python3
"""CT-S58: emit the AEAL claims record.

validate() runs BEFORE the write, on the in-memory buffer. A post-write
assertion leaves the corrupt artefact on disk.

Every figure quoted in a claim must occur in the output file that claim cites.
Exit codes: 0 clean / 2 refusal / 3 crash.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUT = SESS / "outputs"
REC = SESS / "claims.jsonl"

TASK = "CT-S58-READ-LOCATOR"


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def C(cid, claim, label, script, outfile, evidence_type="file_inspection"):
    p = OUT / outfile
    # Do NOT hash eagerly. The control harness showed that hashing here made
    # validate()'s "cited output missing" branch unreachable: the emitter died
    # with a traceback before any validation ran. A crash is not a refusal.
    h = sha(p) if p.exists() else None
    return {"claim_id": cid, "task_id": TASK, "claim": claim, "label": label,
            "evidence_type": evidence_type, "dps": None, "reproducible": True,
            "script": f"scripts/{script}", "output": f"outputs/{outfile}",
            "output_hash": h}


def validate(claims):
    """Refuse before writing. Every check here must be able to fail."""
    errs = []
    seen = set()
    for c in claims:
        cid = c["claim_id"]
        if cid in seen:
            errs.append(f"{cid}: duplicate claim_id")
        seen.add(cid)
        if c["label"] not in ("INSPECTED", "VERIFIED", "STRUCTURAL",
                              "CONJECTURED"):
            errs.append(f"{cid}: bad label {c['label']!r}")
        if c["label"] == "PROVEN":
            errs.append(f"{cid}: PROVEN is not available to this session; "
                        "nothing here is proved, only located")
        op = SESS / c["output"]
        if not op.exists():
            errs.append(f"{cid}: cited output missing: {c['output']}")
            continue
        if c["output_hash"] is None:
            errs.append(f"{cid}: no output_hash was computed")
            continue
        if c["output_hash"] != sha(op):
            errs.append(f"{cid}: output_hash does not match {c['output']} "
                        "on disk")
        # Every integer figure in the claim must occur in the cited output AS A
        # WHOLE TOKEN. A substring test is close to vacuous: it accepts "99"
        # because the output happens to contain "199", which is how the control
        # harness's M4 arm slipped through.
        body = op.read_text(encoding="utf-8", errors="replace")
        for fig in re.findall(r"\d{1,6}", c["claim"]):
            if not re.search(rf"(?<!\d){re.escape(fig)}(?!\d)", body):
                errs.append(f"{cid}: figure {fig} does not occur as a whole "
                            f"number in {c['output']}")
        if not c["claim"].strip():
            errs.append(f"{cid}: empty claim text")
    return errs


def main():
    need = ["locate_revision.out.txt", "locate_painleve.out.txt"]
    for n in need:
        if not (OUT / n).exists():
            print(f"REFUSED: required output missing: {n}")
            return 2

    claims = [
        C("S58-01",
          "All 33 replacements CT-S56 applied to v1.2 are located on exactly "
          "one page of the revised PDF; the revised PDF has 27 pages.",
          "INSPECTED", "locate_revision.py", "locate_revision.out.txt"),
        C("S58-02",
          "Discrimination control: the phrase 'three structurally independent' "
          "is present in the v1.2 PDF and absent from the revision, so the "
          "reader can see the region it reports on.",
          "INSPECTED", "locate_revision.py", "locate_revision.out.txt"),
        C("S58-03",
          "Vacuity pre-check: 32 of 33 anchors resolve to a different page-set "
          "in the revision than in v1.2, so the locator is sensitive to the "
          "edits it locates.",
          "INSPECTED", "locate_revision.py", "locate_revision.out.txt"),
        C("S58-04",
          "Item 5's edits fall on pages 1, 3, 14, 15, 16, 17 and 18 of the "
          "revision; page 18 carries four of them, including Table 2's caption "
          "and the closing of 5.5.",
          "INSPECTED", "locate_revision.py", "locate_revision.out.txt"),
        C("S58-05",
          "The operator's ruling edit at the closing of Proposition 2.4 is on "
          "page 8 of the revision, on the same page as the other Proposition "
          "2.4 edit.",
          "INSPECTED", "locate_revision.py", "locate_revision.out.txt"),
        C("S58-06",
          "Two edits lie inside floats and have no plain-word run long enough "
          "to anchor uniquely; each was resolved to its float sibling's page "
          "by a cross-check that fires when the sibling's page is not among "
          "the candidates.",
          "INSPECTED", "locate_revision.py", "locate_revision.out.txt"),
        C("S58-07",
          "The Painleve paper source under CT-S50-READ-REPAIRS is 15 .tex "
          "files and 2780 lines; patterns in scope of the five LMP correction "
          "items return 157 line-hits in total.",
          "INSPECTED", "locate_painleve.py", "locate_painleve.out.txt"),
        C("S58-08",
          "The Painleve paper never names the LMP paper's object V_quad, nor "
          "its operators L_phi or L_V: both name patterns ran and returned "
          "zero hits. The same object appears under a different description, "
          "b(n)=3n^2+n+1, at 3 lines.",
          "INSPECTED", "locate_painleve.py", "locate_painleve.out.txt"),
        C("S58-09",
          "The Painleve paper has no Method A/B/C framing: the pattern ran and "
          "returned zero hits, so LMP item 5 has no direct counterpart there.",
          "INSPECTED", "locate_painleve.py", "locate_painleve.out.txt"),
        C("S58-10",
          "The case-sensitivity control fires: the macro pattern for the "
          "shared operators matched 3 lines case-insensitively and 0 "
          "case-sensitively, the 3 being LaTeX's own lvert and lVert.",
          "INSPECTED", "locate_painleve.py", "locate_painleve.out.txt"),
    ]

    errs = validate(claims)
    if errs:
        print("REFUSED: claims not written. Problems found before the write:")
        for e in errs:
            print(f"  - {e}")
        return 2

    REC.write_text("\n".join(json.dumps(c) for c in claims) + "\n",
                   encoding="utf-8")
    print(f"wrote {len(claims)} claims to {REC}")
    for c in claims:
        print(f"  {c['claim_id']}  {c['label']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
