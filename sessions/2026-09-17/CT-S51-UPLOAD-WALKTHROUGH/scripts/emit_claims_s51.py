#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CT-S51 -- emit claims.jsonl.  Validates the in-memory buffer BEFORE
writing; every output_hash is recomputed from the file on disk."""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
CHK = HERE / "outputs" / "check_upload_ready.out.txt"
SNAP = HERE / "outputs" / "zenodo_20719043.json"
DEST = HERE / "claims.jsonl"

for p in (CHK, SNAP):
    if not p.exists():
        sys.exit("REFUSED: missing evidence file %s" % p.name)

CT = CHK.read_text(encoding="utf-8")
H_CHK = hashlib.sha256(CHK.read_bytes()).hexdigest()
H_SNAP = hashlib.sha256(SNAP.read_bytes()).hexdigest()

LABELS = {"PROVEN", "VERIFIED", "INSPECTED", "STRUCTURAL", "CONJECTURED"}
SC = "sessions/2026-09-17/CT-S51-UPLOAD-WALKTHROUGH/scripts/check_upload_ready.py"


def C(cid, label, claim, script, h, **kw):
    d = {"claim_id": cid, "task_id": "CT-S51-UPLOAD-WALKTHROUGH",
         "label": label, "claim": claim,
         "evidence_type": kw.pop("ev", "file_inspection"), "dps": None,
         "reproducible": True, "script": script, "output_hash": h}
    d.update(kw)
    return d


CLAIMS = [
    C("S51-01", "INSPECTED",
      "The arXiv submission source is unchanged and still certifiable three "
      "months after it was prepared: vquad-periodrep-paper.tex is 87778 bytes "
      "with sha256 d8906249e8d0eaff681da0f21d6996e6ac824f60550be1d12a21857ae2f"
      "6a906, its companion PDF re-hashes to the layout-fixed pin 33f339ed, "
      "the build log reports 24 pages, and the file is self-contained: zero "
      "\\input, zero \\include, zero \\includegraphics, zero \\bibliography "
      "and zero \\bibliographystyle, with exactly one embedded "
      "thebibliography. It carries no occurrence of any string from the private pattern file and no venue "
      "string, so publishing the source is safe.", SC, H_CHK),
    C("S51-02", "INSPECTED",
      "The Zenodo deposit of the V_quad period-representation paper is DONE, "
      "not pending. A live API snapshot shows record 20719043 state=done, "
      "submitted=true, published 2026-06-16, licence cc-by-4.0, two files, "
      "eleven related identifiers, creator ORCID 0009-0000-6192-8273, version "
      "DOI 10.5281/zenodo.20719043 and concept DOI 10.5281/zenodo.20719042. "
      "The June handoff and operator runbook still describe the deposit as "
      "HELD and upload-ready, so following them today would attempt an "
      "already-completed irreversible action. The record is stale, not the "
      "deposit; under the append-only rule the June session is not edited and "
      "STATE.md carries the correction.", SC, H_SNAP),
    C("S51-03", "VERIFIED",
      "The abstract inside the file that would be uploaded to arXiv and the "
      "abstract the metadata package tells the operator to type are not the "
      "same text. After applying the documented macro expansions and "
      "normalising whitespace they differ, and check C2b establishes the "
      "difference is confined to one clause: deleting 'closure, whose Sakai "
      "surface type is conjectured to be' from the package text and restoring "
      "'closure on the Sakai surface' makes the two byte-identical. The "
      "package was hedge-fixed on 2026-09-13; the manuscript was not.",
      SC, H_CHK, ev="computation"),
    C("S51-04", "INSPECTED",
      "The hedge is the supported reading and the manuscript carries the "
      "unsupported one. CT-S4-FORMAL-TYPE records that the V_quad companion's "
      "v1.2 renamed object 4.1 from a theorem to 'Conjecture 4.1, Painleve V "
      "(D5^(1)) classification' (S4-01), and that this programme's own verdict "
      "on the attribution is (c) INCONCLUSIVE (S4-09). The published Zenodo "
      "description carries the unhedged wording, having been published on "
      "2026-06-16, three months before the hedge fix. Submitting the source as "
      "it stands would place the flat claim in a permanent public record; "
      "typing the hedged abstract over it would make the arXiv abstract and "
      "the arXiv-hosted paper disagree in public. This is reported as a "
      "blocking question for the operator, not resolved here.", SC, H_CHK),
    C("S51-05", "STRUCTURAL",
      "An epistemic-status defect is invisible to every instrument this "
      "programme has built. The two abstracts hash differently and always did; "
      "no digest, build, citation or reference check compares the FORCE of a "
      "claim against the label its corpus assigns. The check that found it had "
      "to be told what to compare. The general form: a gate over artefacts "
      "verifies that a document is the one intended, never that what it "
      "asserts is what the record supports.", SC, H_CHK),
    C("S51-06", "INSPECTED",
      "Pre-registered check C2 is ill-posed and is reported rather than "
      "retuned. It asked whether the two abstracts differ in exactly one "
      "region, treating a diff region as a semantic change; an adjacent "
      "replacement plus insertion is one hedge but two opcodes, so it reported "
      "2 regions with 1 carrying a hedge and failed on a correct artefact. It "
      "is replaced by C2b, which asks the decidable question -- does removing "
      "the named clause make the texts identical -- and answers yes. The "
      "ill-posed check is left in place and reported as a finding, per the "
      "PREREG rule that a threshold which proves ill-posed is itself a result.",
      SC, H_CHK),
    C("S51-07", "INSPECTED",
      "The runner kit the June Zenodo runbook drives the deposit through -- "
      "run_sandbox_draft.py, run_production_draft.py, _zenodo_uploader.py, "
      "set_prod_token.ps1, check_prod_token.ps1 -- is absent from this "
      "repository by recursive filename search. This establishes absence from "
      "the worktree only, not that the kit does not exist: prior sessions have "
      "stored material outside the tree. WALKTHROUGH-ZENODO.md is therefore "
      "written for the web UI, which needs no kit, and names the runner route "
      "as better if the operator still holds it.", SC, H_CHK),
    C("S51-08", "INSPECTED",
      "A sibling marker was written beside the stale June handoff at "
      "sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/AAA-READ-FIRST-PUBLISHED"
      ".md under P0 amendment G. It states that record 20719043 is published, "
      "gives both DOIs and the record's contents, and rules that handoff.md "
      "and operator-runbook.md are to be read as the record of how the deposit "
      "was prepared and not as live instructions. The amendment's bar is "
      "demonstrated harm rather than tidiness, and it is met: the handoff "
      "instructs the operator to perform a completed irreversible action. The "
      "marker is an addition -- it edits nothing in that folder and disturbs "
      "no digest -- the same construction as the supersedes field for claims.",
      SC, H_CHK),
]

errs, seen = [], set()
for c in CLAIMS:
    cid = c["claim_id"]
    if cid in seen:
        errs.append("%s duplicate" % cid)
    seen.add(cid)
    if c["label"] not in LABELS:
        errs.append("%s bad label %r" % (cid, c["label"]))
    if len(c["claim"]) < 60:
        errs.append("%s claim too short to be evidence" % cid)
    if not (ROOT / c["script"]).exists():
        errs.append("%s script does not resolve" % cid)
    if c["output_hash"] not in (H_CHK, H_SNAP):
        errs.append("%s output_hash is not a digest of a session output" % cid)

# anchored-figure rule (S44-17): a cited figure must sit on a line of the
# evidence that also names what it counts.
for fig, anchor in [("17", "checks"), ("2", "FINDING"), ("5", "controls"),
                    ("87778", "tex size"), ("24", "pages")]:
    if not any(fig in ln and anchor in ln for ln in CT.splitlines()):
        errs.append("figure %s is not anchored to a line naming %r"
                    % (fig, anchor))

# non-vacuity: the run must have tested something and every control must fire
if "0 controls" in CT or "FIRED" not in CT:
    errs.append("evidence records no firing control")
if "DEAD" in CT:
    errs.append("evidence records a dead control")
if "REFUSED" in CT:
    errs.append("evidence records a refusal; it is not a clean result")
# S51-03/04 depend on the finding actually being present in the evidence
for needle in ("C1    FAIL", "C2b   OK", "CONJECTURE 4.1",
               "VERDICT (c) INCONCLUSIVE"):
    if needle not in CT:
        errs.append("evidence does not carry %r" % needle)
# S51-02 depends on the record being published
if '"state": "done"' not in SNAP.read_text(encoding="utf-8"):
    errs.append("the snapshot does not show a published record")
# S51-08 depends on the marker existing and carrying the rule it claims.
MARK = (ROOT / "sessions" / "2026-06-16" / "VQUAD-ZENODO-DEPOSIT-001" /
        "AAA-READ-FIRST-PUBLISHED.md")
if not MARK.exists():
    errs.append("S51-08 cites a sibling marker that does not exist")
else:
    MT = MARK.read_text(encoding="utf-8")
    for needle in ("20719043", "10.5281/zenodo.20719042", "PUBLISHED",
                   "not as live instructions", "amendment G"):
        if needle not in MT:
            errs.append("the sibling marker does not carry %r" % needle)
    # the marker must be an ADDITION: the files it warns about stay unedited
    for sib in ("handoff.md", "operator-runbook.md"):
        if not (MARK.parent / sib).exists():
            errs.append("the marker warns about %s, which is not there" % sib)

if errs:
    print("REFUSED -- nothing written:")
    for e in errs:
        print("  " + e)
    sys.exit(2)

DEST.write_text("\n".join(json.dumps(c, ensure_ascii=False) for c in CLAIMS)
                + "\n", encoding="utf-8")
back = [json.loads(l) for l in DEST.read_text(encoding="utf-8").splitlines()]
assert len(back) == len(CLAIMS)
print("wrote %d claims" % len(back))
print("  check_upload_ready.out.txt sha256 %s" % H_CHK[:32])
print("  zenodo_20719043.json       sha256 %s" % H_SNAP[:32])
print("  claims.jsonl               sha256 %s"
      % hashlib.sha256(DEST.read_bytes()).hexdigest()[:32])
for b in back:
    print("  %-7s %-11s %s..." % (b["claim_id"], b["label"], b["claim"][:50]))
