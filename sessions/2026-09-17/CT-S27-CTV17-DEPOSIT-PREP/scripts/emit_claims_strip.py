"""Emit the claims for the internal-provenance strip round.

Hashes are taken FROM DISK, after each artefact is final.  A hash of an
in-memory string is not evidence about a file, and re-running a checker
invalidates every hash that points at its output -- which is why each revision
here writes a NEW output filename and never overwrites one already cited.
"""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
CLAIMS = os.path.join(SESSION, "claims.jsonl")


def sha(relpath):
    with open(os.path.join(SESSION, relpath), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


CLAIMS_TO_ADD = [
    dict(
        claim_id="S27-13",
        label="INSPECTED",
        claim=(
            "THE PUBLISHED DESCRIPTION CARRIES NO INTERNAL PROVENANCE A READER "
            "CANNOT RESOLVE. No uncommitted session id, no refs/, scripts/ or "
            "outputs/ path, no working file name, and no AEAL claim id survives: "
            "residue 0 against six patterns. 21 inline claim ids were removed and "
            "27 references outside the sources table were reworded. The epistemic "
            "labels those ids carried (PROVEN/VERIFIED/STRUCTURAL/INSPECTED) were "
            "KEPT: a label is content, only the identifier is provenance."),
        evidence_type="file_inspection",
        script="scripts/make_description.py",
        output="outputs/make_description_r4.out.txt",
    ),
    dict(
        claim_id="S27-14",
        label="INSPECTED",
        claim=(
            "THE STRIP IS GUARANTEED ON BOTH SIDES, IN THE VERIFIER AND NOT ONLY "
            "IN THE GENERATOR'S ASSERTS. P1 rejects unresolvable internal "
            "provenance; P2 asserts that 11 named resolvable identifiers and at "
            "least 8 sha256 values are still present. P1 alone is insufficient, "
            "because a strip that deleted the citations along with the paths "
            "would satisfy it perfectly. Both now re-test on every run rather "
            "than at generation time only, the same move that put T5 in the "
            "verifier. 16/16, 0 broken, 3/3 reader controls."),
        evidence_type="build",
        script="scripts/verify_description.py",
        output="outputs/verify_description_r6.out.txt",
    ),
    dict(
        claim_id="S27-15",
        label="INSPECTED",
        claim=(
            "P1 AND P2 TAKE THEIR MUTANTS FROM OUTSIDE THEIR OWN PATTERN LISTS. "
            "Each P1 mutant is a verbatim string that stood in the pre-strip "
            "notice, drawn from the source text rather than composed from the "
            "patterns P1 matches on; 3 P1 and 2 P2 mutants were all rejected. "
            "This applies the principle flagged as a candidate fifth P0 "
            "amendment BEFORE it is ruled on: a mutant drawn from a check's own "
            "list proves only that the list is consulted, never that it is "
            "adequate. Written up as PROPOSED in P0-AMENDMENT-E.md; NOT adopted."),
        evidence_type="build",
        script="scripts/verify_description.py",
        output="outputs/verify_description_r6.out.txt",
    ),
    dict(
        claim_id="S27-16",
        label="VERIFIED",
        claim=(
            "NO IDENTIFIER IN THE PUBLISHED BIBLIOGRAPHY IS FROM MEMORY: EACH WAS "
            "RESOLVED AND PRINTED WITH THE RESOLVER'S OWN TITLE. Gautschi "
            "10.1137/1009002 (SIAM Review 9(1) 24-82) was DISCOVERED BY TITLE "
            "QUERY and was not previously recorded anywhere in the corpus; "
            "Birkhoff-Trjitzinsky 10.1007/bf02398269 (Acta Math. 60, 1-89); Wong "
            "& Li II 10.1002/sapm1992874289, which remains NOT OBTAINED and is "
            "labelled so; Wong & Zhao 10.1142/S0219530522400012; Ibrahim & Salvy "
            "10.1137/1.9781611977912.37; Nemes arXiv:2508.15246; DLMF 3.6 and "
            "2.9; Odlyzko, whose held PDF is byte-identical (1116716 B) to the "
            "file on the author's site. 10 rows probed, 0 not fit to publish."),
        evidence_type="computation",
        script="scripts/doi_probe_v17.py",
        output="outputs/doi_probe_v17.out.txt",
    ),
    dict(
        claim_id="S27-17",
        label="VERIFIED",
        claim=(
            "THE IDENTIFIER PROBE RETAINS A POISON CONTROL AND PASSES IT BY "
            "REPORTING WHAT THE DOI ACTUALLY IS. 10.1007/BF02547452, which the "
            "corpus had already caught being offered for Birkhoff 1930, resolves "
            "to a 1995 chemistry paper. The probe's correct behaviour is to "
            "resolve it and print that title, since a probe that merely rejected "
            "it could not distinguish a wrong identifier from a dead one. This "
            "is why the bibliography's identifiers are evidence rather than "
            "recall."),
        evidence_type="computation",
        script="scripts/doi_probe_v17.py",
        output="outputs/doi_probe_v17.out.txt",
    ),
    dict(
        claim_id="S27-18",
        label="INSPECTED",
        claim=(
            "THE DECISION TO REMOVE CLAIM IDS FOLLOWS THE RECORD, NOT PREFERENCE: "
            "THE DEPOSITED v1.6 DESCRIPTION CARRIES ZERO AEAL CLAIM IDS. The "
            "operator's consistency argument therefore reaches them. The same "
            "reading sharpens the rule in the other direction: v1.6 DOES carry a "
            "github.com URL into a committed sessions/2026-05-02/ path, so the "
            "line is not 'sessions/ is internal' but committed-and-public versus "
            "uncommitted. The 2026-09-17 session paths resolve for nobody."),
        evidence_type="file_inspection",
        script="scripts/make_description.py",
        output="outputs/make_description_r4.out.txt",
    ),
    dict(
        claim_id="S27-19",
        label="INSPECTED",
        claim=(
            "AN AUDIT REPORTED 85 SPACE-BEFORE-PUNCTUATION DEFECTS THAT DO NOT "
            "EXIST: THE RAW HTML CONTAINS ZERO. All 85 are '</strong>.' or "
            "'</em>.', and the audit's own tag-stripping substitutes a SPACE for "
            "each tag, manufacturing ' .'. Recorded because it is the "
            "reader-integrity class IN REVERSE: adopted Amendment C covers a "
            "reader that cannot see a defect, this is a reader that invents one. "
            "The corrective is the same, a second differently-implemented read, "
            "which is why it cost minutes instead of a round of edits to prose "
            "that was already correct."),
        evidence_type="file_inspection",
        script="scripts/verify_description.py",
        output="outputs/verify_description_r6.out.txt",
    ),
    dict(
        claim_id="S27-20",
        label="INSPECTED",
        claim=(
            "BOTH GATES WERE RE-RUN AFTER THE STRIP AND ARE MUTUALLY CONSISTENT. "
            "verify_description 16/16, 0 failed, 0 broken, 3/3 reader controls, "
            "entity round trip 28/28; preflight_deposit_rev2 11/11, 3/3, GATE "
            "PASSED, against description sha256 026e7a9e..., 54068 chars, 54256 "
            "bytes, 156 paragraphs. The first post-strip gate run correctly "
            "BLOCKED on S2 and S3, the declared hash pointing at bytes that no "
            "longer existed. One further repair: S3 reported 'passed 14/14' from "
            "a HARD-CODED string while reading a 16-check output, so the count is "
            "now parsed from the output it read."),
        evidence_type="build",
        script="scripts/preflight_deposit_rev2.py",
        output="outputs/preflight_deposit_rev2_r7.out.txt",
    ),
]

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"}


def main():
    for c in CLAIMS_TO_ADD:
        assert c["label"] in LABELS, "%s: unrecognised label %r" % (
            c["claim_id"], c.get("label"))
        head = c["claim"].split(".")[0]
        assert not any(head.startswith(lab) for lab in LABELS), (
            "%s: the label belongs in the 'label' FIELD, not as a prefix in the "
            "claim text -- this is the house shape the corpus checker enforces"
            % c["claim_id"])

    existing = set()
    if os.path.exists(CLAIMS):
        with io.open(CLAIMS, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    existing.add(json.loads(line)["claim_id"])

    written = []
    with io.open(CLAIMS, "a", encoding="utf-8", newline="\n") as fh:
        for c in CLAIMS_TO_ADD:
            if c["claim_id"] in existing:
                print("  skip %s (already present)" % c["claim_id"])
                continue
            rec = {
                "claim_id": c["claim_id"],
                "task_id": "CT-S27-CTV17-DEPOSIT-PREP/strip",
                "claim": c["claim"],
                "label": c["label"],
                "evidence_type": c["evidence_type"],
                "dps": None,
                "reproducible": True,
                "script": c["script"],
                "output_hash": sha(c["output"]),
            }
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            written.append((c["claim_id"], c["output"], rec["output_hash"]))

    print("appended %d claim(s) to claims.jsonl" % len(written))
    for cid, out, h in written:
        print("  %-8s %-46s %s" % (cid, out, h[:16]))

    with io.open(CLAIMS, encoding="utf-8") as fh:
        total = sum(1 for line in fh if line.strip())
    print("claims.jsonl now holds %d claim(s)" % total)


if __name__ == "__main__":
    main()
