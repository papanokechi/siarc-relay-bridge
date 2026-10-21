"""emit_claims_s37b.py -- AEAL claim records for CT-S37-DRAFT-B.

The buffer is validated BEFORE anything is written.  A post-write assertion
still leaves a corrupt artefact on disk, so every check below runs against the
in-memory list.

ORDERING NOTE.  outputs/draft_check.out.txt prints a corpus-wide file and claim
count, so writing claims.jsonl into the corpus CHANGES that output.  This
script is therefore run twice: once to place the file, and once after the
gates have been re-run, so that the digests cited here are the digests of the
final outputs on disk.  scripts/verify_claim_digests.py checks that.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "claims.jsonl"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}
EVIDENCE = {"file_inspection", "computation", "build", "proof"}


def sha(rel):
    p = HERE / rel
    if not p.exists():
        print("MISSING artefact: %s" % rel)
        sys.exit(2)
    return hashlib.sha256(p.read_bytes()).hexdigest()


C = []


def add(cid, task, claim, label, ev, script, artefact, dps=None, review="self",
        note=None):
    r = {"claim_id": cid, "task_id": task, "claim": claim, "label": label,
         "evidence_type": ev, "dps": dps, "reproducible": True,
         "script": script, "output_hash": sha(artefact), "review": review}
    if note:
        r["review_note"] = note
    C.append(r)


DC = "outputs/draft_check.out.txt"
MU = "outputs/mutants_draft_check.out.txt"

add("S37B-01", "S37B-DRAFT3",
    "Section 3 'The differential systems and their local data' is drafted as "
    "paper prose at sections/section3.tex, 7 subsections, and every numerical "
    "value in it carries the claim id it is taken from. It states System A "
    "(S4-03), its normal potential (S4-05), Systems B (S4-04) and C (S16-06), "
    "the exact formal types at 0 and infinity, the actions 2/sqrt3 and 4/sqrt3 "
    "(S4-07), the non-apparency of both finite singular points "
    "(CT-S9-PVPARAMS-C007/C008, S6-C13, S6-C14), the z = w^2 pullback with its "
    "vacuity control (S5B-C3), and the effective Katz multisets (S6-C16, "
    "S6-C7, S6-C9).",
    "STRUCTURAL", "file_inspection", "draft_check.py", "section3.tex",
    note="a drafted section is an editorial artefact; the label records that "
         "the drafting is a structural act, not that its cited results are "
         "structural. Each cited result carries its own label in the prose.")

add("S37B-02", "S37B-DRAFT4",
    "Section 4 'The moduli space and its hypotheses' is drafted at "
    "sections/section4.tex and discharges OUTLINE revision 6 repair R-(c) in "
    "full: van der Put-Saito's family (4.1) is PRINTED with all three entries "
    "a, b, c; the flow (4.4) and the Hamiltonian H_V (4.5) are PRINTED, not "
    "cited; the chart U_0 and the 2-form Omega are printed. The printed "
    "(4.5) is transcribed from CT-S16-MEMBERSHIP-C/flow_regularity.py lines "
    "9-10 and 23-24, which is the corpus record of the page-image reading "
    "S16-03; it is NOT reconstructed from memory.",
    "STRUCTURAL", "file_inspection", "draft_check.py", "section4.tex",
    note="the printed (4.5) traces to a script in the corpus that computes "
         "with it, so the transcription is executable, not only quoted.")

add("S37B-03", "S37B-CHECK",
    "The Group B draft check PASSES: 57 citations across the two drafted "
    "sections, 57 OK, 0 UNRESOLVED, 0 structurally SUPERSEDED, 0 MISMATCH. "
    "Every claim id cited in the prose resolves in the corpus and carries in "
    "the prose exactly the label its claims.jsonl record carries. The "
    "pre-registered falsifier (UNRESOLVED + SUPERSEDED + MISMATCH) > 0 did "
    "not fire.",
    "VERIFIED", "computation", "draft_check.py", DC,
    note="labels were read from the corpus at draft time and re-read by the "
         "check; no label in the prose was written from memory.")

add("S37B-04", "S37B-CONTROL",
    "The control required by the task is satisfied: 9 of 9 mutant arms are "
    "CAUGHT, each for the stated reason. Four arms insert a deliberately "
    "wrong label (M1 PROVEN->CONJECTURED on S4-03; M2 the P0-forbidden "
    "upgrade INSPECTED->PROVEN on S16-01; M3 STRUCTURAL->VERIFIED on S6-C16; "
    "M4 STRUCTURAL->INSPECTED on S16-04) and all four are rejected. M5 cites "
    "a non-existent id, M6 cites an id carrying a structured superseded_by "
    "field, M7 requires the alias form to resolve AND be reported, M8 empties "
    "a drafted file, M9 is the boundary arm for the narrowed pair bound. An "
    "arm is CAUGHT only if the exit code matches, the output names the "
    "mutated id and verdict word, and the output contains no Traceback, "
    "SyntaxError or NameError.",
    "VERIFIED", "computation", "mutants_draft_check.py", MU,
    note="the crash guard is present because a traceback echoes the source "
         "line and can otherwise satisfy a reason-string test on a checker "
         "that never ran.")

add("S37B-05", "S37B-DEFECT",
    "DEFECT FOUND IN THE CHECKER, NOT THE PROSE. The first claim-id pattern "
    "'(?:CT-)?S\\d+[A-Z]*-[A-Z]*\\d+(?:-[A-Z]+\\d+)*' requires every segment "
    "to end in digits, so the segment PVPARAMS did not match and ALL eleven "
    "CT-S9-PVPARAMS-* citations (eight in section 3, three in section 4) were "
    "silently dropped. The check would have reported PASS having examined 46 "
    "of 57 citations. Repaired to '(?:CT-)?S\\d+[A-Z]*(?:-[A-Z0-9]+)+'; the "
    "pair counts moved 37->45 and 9->12.",
    "VERIFIED", "computation", "draft_check.py", DC,
    note="found only because the reader-integrity bound fired and the pair "
         "counts were read; inspecting the regex had not found it.")

add("S37B-06", "S37B-DEFECT",
    "PRE-REGISTERED THRESHOLD PROVED ILL-POSED AND IS REPORTED AS SUCH. The "
    "reader-integrity bound required at least 15 (id,label) pairs per file; "
    "section4.tex correctly carries 12, so the bound fired on correct prose "
    "-- the fingerprint failure a non-vacuity bound exists to avoid. Narrowed "
    "post-hoc to 5 per file plus 30 across the group, with boundary mutant M9 "
    "added in the SAME edit and CAUGHT. The falsifier was not touched.",
    "STRUCTURAL", "computation", "mutants_draft_check.py", MU,
    note="disclosed in PREREG.md as an amendment rather than presented as the "
         "original design; same handling as N5/N7 in CT-S35.")

add("S37B-07", "S37B-ALIAS",
    "CITATION DEFECT IN OUTLINE.md, REPORTED NOT SILENTLY NORMALISED. "
    "OUTLINE.md cites this family as S9-PVPARAMS-C002 ... S9-PVPARAMS-C012; "
    "the corpus ids are CT-S9-PVPARAMS-C001 ... CT-S9-PVPARAMS-C014. The "
    "OUTLINE form does not literally resolve. The drafted sections use the "
    "corpus form throughout, so no citation in the drafts required the alias; "
    "the checker nevertheless implements the CT- prefix alias and REPORTS any "
    "use of it, and mutant arm M7 exercises that path.",
    "VERIFIED", "computation", "draft_check.py", DC)

add("S37B-08", "S37B-BUILD",
    "groupB_standalone.tex, which inputs the CT-S36 section 1 (sha256 "
    "39ddd724524f2a7e38febbf32cfd4d575e319b28b13bb200da022b10fa7423ca, "
    "copied unmodified to refs/section1.tex) followed by the two drafted "
    "sections, compiles under pdflatex in two passes with exit code 0, "
    "producing 10 pages with no undefined references and no LaTeX warnings. "
    "The forward reference eqref{eq:n-rec} into section 1 resolves.",
    "VERIFIED", "build", "pdflatex (two passes)", "groupB_standalone.pdf")

add("S37B-09", "S37B-SCOPE",
    "PREMISE OF THE TASK UNMET, REPORTED. The task states that sections "
    "already drafted are inputs. Group A (section 0 introduction, section 2 "
    "growth with the section 2.0 attribution paragraph) has NOT been drafted: "
    "no CT-S37-* session folder other than this one exists, and the only "
    "drafted section in the corpus is CT-S36's section1.tex. Sections 3 and 4 "
    "do not depend on Group A, so Group B was drafted as instructed, but the "
    "attribution paragraph that section 2.0 is to carry is not available to "
    "be cited from here.",
    "VERIFIED", "file_inspection", "claim_index.py", DC)

add("S37B-10", "S37B-SCOPE",
    "PRE-EXISTING CORPUS NOISE, OUT OF SCOPE, NOT REPAIRED. Indexing all "
    "claims.jsonl under sessions/ leaves 46 unparseable lines, confined to "
    "2026-04-28/AUDIT-MASTER-THEOREM-INVENTORY, "
    "2026-04-30/SIARC-COHERENCE-AUDIT and "
    "2026-05-08/T2-105-COPILOT-RESEARCHER-PROMPT-DRAFT-109, plus 84 duplicate "
    "bare claim ids (C1...C9 reused across 2026-05 sessions and "
    "CT-S15-COLDREAD-DEFERRED). All predate every CT-S* session. Reading "
    "claims.jsonl as utf-8-sig rather than utf-8 was required and removed the "
    "largest parse-failure class. None of the affected ids is cited by the "
    "drafted sections.",
    "VERIFIED", "computation", "claim_index.py", DC)

add("S37B-11", "S37B-LABELS",
    "THE CORPUS LABEL VOCABULARY IS WIDER THAN P0's FOUR. P0 names PROVEN, "
    "VERIFIED, STRUCTURAL, CONJECTURED. The corpus also uses INSPECTED for a "
    "reading of a printed page, and eight of the 57 citations in the drafted "
    "sections carry it (S6-C1, S5B-C7, S16-01 x3, S16-02, S16-03, and the "
    "three CT-S9-PVPARAMS convention claims). The prose carries INSPECTED "
    "as-is and does not promote it to VERIFIED or PROVEN; the checker's label "
    "vocabulary includes it so that such a promotion is a MISMATCH, which is "
    "what mutant arm M2 exercises.",
    "STRUCTURAL", "computation", "draft_check.py", DC)

add("S37B-12", "S37B-LABELS",
    "A RULE IN THE TASK PROMPT CONFLICTS WITH THE CORPUS, AND THE CORPUS "
    "WINS. The prompt directs that exclusions be labelled VERIFIED and row "
    "matches STRUCTURAL. In the corpus BOTH the exclusion S6-C7 (System B's "
    "effective multiset (1,0,0,0) does not match the D5/PV row) and the match "
    "S6-C16 (System C's effective multiset (0,0,1) matches it) carry "
    "STRUCTURAL. The prompt's further rule -- check each cited id's current "
    "label before writing the sentence, not from memory -- is the governing "
    "one, so the prose says STRUCTURAL for both and the conflict is reported "
    "rather than resolved by relabelling a corpus claim.",
    "STRUCTURAL", "computation", "draft_check.py", DC)

# ---------------- validate the BUFFER, before writing anything -------------
seen = set()
for r in C:
    cid = r["claim_id"]
    assert cid not in seen, "duplicate claim id in buffer: %s" % cid
    seen.add(cid)
    assert r["label"] in LABELS, "%s: bad label %r" % (cid, r["label"])
    assert r["evidence_type"] in EVIDENCE, "%s: bad evidence_type" % cid
    assert isinstance(r["claim"], str) and len(r["claim"].strip()) >= 80, \
        "%s: claim text too short or empty" % cid
    assert len(r["output_hash"]) == 64 and all(
        c in "0123456789abcdef" for c in r["output_hash"]), \
        "%s: output_hash is not a sha256" % cid
    assert r["script"], "%s: no script" % cid
    assert r["reproducible"] is True

assert len(C) == 12, "expected 12 claims, buffer has %d" % len(C)
assert any("S37B-04" == r["claim_id"] for r in C)

buf = "".join(json.dumps(r, ensure_ascii=True) + "\n" for r in C)
for line in buf.splitlines():
    json.loads(line)          # every emitted line must re-parse
assert buf.endswith("\n")

OUT.write_text(buf, encoding="utf-8", newline="\n")
print("wrote %s: %d claims, %d bytes" % (OUT.name, len(C), len(buf.encode())))
print("claims.jsonl sha256 = %s"
      % hashlib.sha256(OUT.read_bytes()).hexdigest())
