"""emit_claims_s40.py -- AEAL claim records for CT-S40-DRAFT-B-RERUN.

Validation runs on the IN-MEMORY buffer BEFORE anything is written, so a
refusal never leaves a corrupt claims.jsonl on disk (S28-14 / S32-12).

Two-pass note.  draft_check.py prints a different [self-exclusion] line
depending on whether this session's claims.jsonl exists, so its output digest
changes the first time claims are emitted.  The procedure is therefore:

    1. run this emitter (claims.jsonl comes into existence)
    2. re-run draft_check.py (its output settles; the line is now non-vacuous)
    3. run this emitter again (digests resolve against the settled output)

Step 3's output is stable under further re-runs, because draft_check's line
depends only on the EXISTENCE of claims.jsonl and the file count of the walk,
never on its contents.  That invariance is asserted by re-running the gate
after emission and comparing digests, not assumed.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "outputs"
ART = HERE / "claims.jsonl"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}

DRAFT = "draft_check.out.txt"
MUT = "mutants_draft_check.out.txt"
ASM = "check_assembly.out.txt"
AMUT = "mutants_assembly.out.txt"


def sha_file(name):
    p = OUT / name
    if not p.exists():
        print("MISSING OUTPUT: %s" % p)
        sys.exit(2)
    return hashlib.sha256(p.read_bytes()).hexdigest()


def row(cid, label, claim, script, out, **extra):
    r = {"claim_id": cid, "task_id": "CT-S40-DRAFT-B-RERUN", "claim": claim,
         "label": label, "evidence_type": "build" if "build" in out else
         "file_inspection", "dps": None, "reproducible": True,
         "script": script, "output_hash": sha_file(out)}
    r.update(extra)
    return r


ROWS = [
    row("S40-01", "VERIFIED",
        "Group B (sections 3 and 4) re-checked against the REPAIRED section 1 "
        "and with section 2 present. All 57 (claim id, label) pairs resolve "
        "and every asserted label matches the label the corpus record carries "
        "today: 0 UNRESOLVED, 0 SUPERSEDED, 0 MISMATCH. The CT- prefix alias "
        "is REMOVED per the operator ruling recorded as S39-08; a bare short "
        "form is now UNRESOLVED and fails, and where the retired alias would "
        "have resolved it that is printed as a diagnostic on the failing row "
        "rather than silently normalised. The removal is a no-op on this "
        "prose: no citation in sections 3 or 4 needed the alias, so it was "
        "already dead code when CT-S37 retained it. Mutant M7 is INVERTED "
        "accordingly and is the boundary mutant for the removal; 12/12 arms "
        "CAUGHT, including three new ones.",
        "scripts/draft_check.py", DRAFT),

    row("S40-02", "VERIFIED",
        "A cross-section label mismatch invisible to BOTH prior gates: "
        "sections 0 and 2 reference sec:local at three places, while section "
        "3 defines itself as sec:systems and section 4 already references "
        "sec:systems. Group A's build reported 0 undefined references because "
        "its stub forwardrefs.tex DECLARED sec:local -- the stub manufactured "
        "a target that no section defines. Group B's build never referenced "
        "section 3 from outside, so it had no symptom there either. The "
        "defect has no external symptom in page count, rendered diff or "
        "either build, and appears only on assembly with the stub forbidden "
        "from standing in for a section that exists. Confirmed by building "
        "sections 0-4 together before repair: exactly 3 undefined references, "
        "all to sec:local, and nothing else. Repaired in this session's "
        "copies by renaming the three references to sec:systems (the definer "
        "wins, and section 4 already agreed); the combined build then gives "
        "15 pages, 0 errors, 0 undefined and 0 multiply-defined references. "
        "check_assembly.py encodes the rule that produced it -- a stub may "
        "declare ONLY labels for sections that do not exist -- and 7/7 arms "
        "are CAUGHT, A1 reinstating this exact defect and A2 its cause.",
        "scripts/check_assembly.py", ASM),

    row("S40-03", "VERIFIED",
        "CT-S37 checked Group B against a section 1 that no longer exists: "
        "its refs/section1.tex is the pre-CT-S38 copy (13660 B) and the "
        "repaired file is 14325 B, differing in the psi/nu re-lettering, the "
        "rewritten rho sentence, and the new s/s_pm and P,Q/Q_n "
        "disambiguation paragraphs. The re-run asserts the correct input "
        "POSITIVELY and TWO-SIDED, per the form adopted at S38-07: three "
        "pre-repair markers must be present in the retained CT-S37 snapshot "
        "and absent from the live file, and five repair markers the reverse. "
        "All eight resolve. The first attempt at this guard was itself "
        "defective in two ways, both repaired before the result was reported: "
        "it was one-sided, and its needle spanned a line break in the source "
        "so a raw containment test reported a FALSE ABSENCE on correct text "
        "-- the same failure as CT-S39's F6c. Matching is now done on "
        "whitespace-squashed text. Arm M12 stages the stale copy and is "
        "CAUGHT.",
        "scripts/draft_check.py", DRAFT),

    row("S40-04", "INSPECTED",
        "SCOPE FINDING on P0 amendment F, reported and NOT repaired. S38-17 "
        "measured 649 claim lines in 35 files and concluded that the five "
        "labels PARTITION the corpus, 'so there is no sixth label'. The "
        "census script prints its root honestly as sessions/2026-09-17, but "
        "draft_check.py's corpus index walks ALL of sessions/ -- 451 "
        "claims.jsonl files, 4195 claim lines, 1411 unique claim ids. The "
        "word 'corpus' therefore denotes two different sets in two checks of "
        "the same run. Over the full tree the five do NOT partition: PROCEED "
        "(14) and REFINED (1) occur in 2026-05-13 and 2026-05-14, and 3458 "
        "claim lines carry no label field at all. Confirmed by two "
        "differently-implemented readers (pathlib.rglob + json.loads, and "
        "os.walk + a raw-bytes regex), which agree on 451 files, 4195 lines "
        "and every label count, and resolve to named file:line locations; the "
        "raw line at 2026-05-13/T1-SYNTH-VERDICT-212-.../claims.jsonl:1 "
        "carries \"label\": \"PROCEED\" beside lock/band/confidence fields, "
        "i.e. a different claim schema from a different workstream. The "
        "amendment's substance holds for the Channel Theory working corpus; "
        "what is wrong is the unqualified word 'corpus'. OPERATOR RULING "
        "REQUESTED on the wording. Not repaired here because amending S38-17 "
        "would strand the digests later claims cite.",
        "scripts/draft_check.py", DRAFT,
        review_note="Scope defect in an adopted P0 amendment, not a "
                    "measurement error: the census figures are correct for "
                    "the root the script prints. Re-derivable from the two "
                    "reader scripts quoted in REPORT.md section 3; those were "
                    "run inline and are not retained as files, so this is "
                    "re-derivable but not replayable."),

    row("S40-05", "INSPECTED",
        "CORRECTION to the stated reason for this re-run, recorded rather "
        "than the conclusion. The re-run was commissioned because sections 3 "
        "and 4 'cite a section that isn't there'. Measured, they do not: 0 "
        "labels borrowed from section 2 and 0 references to sec:growth. The "
        "single label they borrow from outside themselves is eq:n-rec, from "
        "section 1, and it resolved throughout. That premise was therefore "
        "wrong, and the operator has recorded the correction. Drafting Group "
        "A first was nonetheless the right order, for a different reason: "
        "section 2.0 is the paper's most citation-dense paragraph and had to "
        "be drafted before anything leaned on its attribution. The re-run's "
        "value lies in the repaired section 1 and in the assembly check, "
        "neither of which was the reason it was commissioned.",
        "scripts/draft_check.py", DRAFT,
        review_note="The correction is the claim; the conclusion (that the "
                    "re-run was worth doing) is unchanged but now rests on "
                    "citation density rather than on an unresolved "
                    "cross-reference that never existed."),

    row("S40-06", "VERIFIED",
        "First combined build of the drafted paper: sections 0, 1, 2, 3, 4 "
        "with a stub for sections 5-10 only. 15 pages, 0 errors, 0 undefined "
        "references, 0 multiply-defined labels; 69 distinct labels defined "
        "and 46 distinct targets referenced, all resolving. The wrapper must "
        "load hyperref, which Group B's did and Group A's did not: sections 3 "
        "and 4 use \\\\texorpdfstring, and the first combined build aborted on "
        "an undefined control sequence for want of it. That is a second "
        "assembly-only defect, invisible to either standalone build.",
        "scripts/check_assembly.py", ASM),

    row("S40-07", "INSPECTED",
        "CT-S39-DRAFT-A's section0.tex and section2.tex still carry the three "
        "sec:local references; only this session's copies are repaired. They "
        "are deliberately NOT edited: CT-S39's claims cite the digest of "
        "check_group_a.out.txt, which is produced by reading those two files, "
        "so a one-word change there would strand all eight S39 digests. This "
        "is the same reasoning that left draft_check.py's alias alone until "
        "the operator ruled. OPERATOR RULING REQUESTED: repair CT-S39 in "
        "place and re-emit its claims, or carry the repair forward at "
        "assembly. The same question governs S1-04's stale claim text "
        "(S39-03) and the three pre-upgrade rows in CT-S1-THEOREM/REPORT.md.",
        "scripts/check_assembly.py", ASM),

    row("S40-08", "VERIFIED",
        "Control coverage for this session: 12/12 arms CAUGHT on "
        "draft_check.py and 7/7 on check_assembly.py, each scored on three "
        "conditions -- expected exit code, the output naming both the rule "
        "and the mutated object, and no Traceback/SyntaxError/NameError, so "
        "that a checker which merely crashed is never counted as having "
        "caught anything. The staged tree pins claim_index.ROOT to the real "
        "sessions directory and now also stages OUTLINE.md at the path "
        "draft_check resolves, without which every arm would die on reader "
        "integrity before judging anything (the CT-S34 copied-harness "
        "defect). Two arms exist solely to stop a rule passing vacuously: A6 "
        "empties the stub so R2 cannot pass on an empty set, and A7 empties "
        "every section so the integrity bounds are shown to be bounds.",
        "scripts/mutants_assembly.py", AMUT),

    row("S40-09", "VERIFIED",
        "SUPERSEDES S39-07. S39-07 recorded the Group A build as 9 pages with "
        "0 undefined references and described forwardrefs.tex as guarded by "
        "F7 against drift from OUTLINE.md. Both halves are true as stated and "
        "neither is retracted. What S39-07 could not know is that the stub "
        "DECLARED sec:local, a label no section defines: sections 0 and 2 "
        "reference it, section 3 defines sec:systems. The 0-undefined result "
        "was therefore achieved in part by the stub manufacturing its own "
        "target, and F7 could not detect it because F7 checks the stub's "
        "NUMBERS against the outline's headings, which is all it could check "
        "while section 3 did not exist. Per operator ruling of 2026-09-20, "
        "CT-S39-DRAFT-A is NOT edited: its section0.tex and section2.tex "
        "still carry the three sec:local references and its claim digests "
        "stand. The repaired files live in CT-S40-DRAFT-B-RERUN/refs/ and the "
        "assembly builds from there. The general rule is now carried by "
        "check_assembly.py R2 -- a stub may declare ONLY labels for sections "
        "that do not exist -- with arms A1 and A2 reinstating the defect and "
        "its cause.",
        "scripts/check_assembly.py", ASM,
        supersedes="S39-07"),

    row("S40-10", "INSPECTED",
        "SUPERSEDES S1-04 as to its CLAIM TEXT ONLY; the label PROVEN is "
        "correct and is not disturbed. S1-04's record still ends 'Steps 3,4 "
        "rest on Gap G1 ... Hence STRUCTURAL, not PROVEN', which was true "
        "when written and was made false by the R1 audit: theorem.tex lines "
        "427-436 record the closure of Gap G1 and CT-S1-THEOREM/REPORT.md "
        "line 8 records the upgrade STRUCTURAL -> PROVEN explicitly. The "
        "growth law is PROVEN. The one classical input the closure leaves "
        "imported is the normalisation h_infinity = 1, DLMF (5.11.12), "
        "Gamma(z+a)/Gamma(z+b) ~ z^(a-b), verified in the held capture "
        "CT-R1-AUDIT/refs/dlmf_5.11.html and named at the point of use in "
        "section 2. Per operator ruling of 2026-09-20 the original record "
        "stands and is amended by this claim rather than rewritten, the R20 "
        "precedent. The same applies to the three pre-upgrade STRUCTURAL rows "
        "at CT-S1-THEOREM/REPORT.md lines 44, 61 and 239, which are "
        "superseded by this claim and left in place.",
        "scripts/check_assembly.py", ASM,
        supersedes="S1-04",
        review_note="Supersedes the claim TEXT, not the label. A future "
                    "reader taking S1-04's closing sentence at face value "
                    "would understate a proved theorem; one taking the label "
                    "without reading the text would miss the h_infinity = 1 "
                    "import. This claim is what stops both."),

    row("S40-11", "INSPECTED",
        "P0 AMENDMENT F's SCOPE CLAUSE IS REWRITTEN, by operator ruling of "
        "2026-09-20 on the finding S40-04. F is a standing rule, not a claim, "
        "so it is amended in place rather than superseded; its digest is "
        "cited by no claim, which was checked before editing. The word "
        "'corpus' in F now means the Channel Theory corpus, the sessions "
        "under sessions/2026-09-17/, which is the root label_census.py walks "
        "and prints. A new scope section records that draft_check.py's index "
        "walks all of sessions/ -- 451 files, 4195 claim lines -- of which "
        "3458 carry no label field and 15 carry PROCEED or REFINED from a "
        "different workstream's schema, where 'label' sits beside lock, band "
        "and confidence fields that the AEAL schema does not have. Check C4 "
        "is restated as partitioning the Channel Theory corpus rather than "
        "'anywhere'. F's substance is unchanged and nothing is relabelled: "
        "the five still partition the set that was measured, and the "
        "out-of-five values are a different vocabulary in a different system, "
        "not a sixth epistemic label.",
        "scripts/check_assembly.py", ASM,
        review_note="Amends a standing rule in place, which is permitted "
                    "here only because no claim cites the file's digest; that "
                    "was verified before the edit, not assumed."),
]


def validate(rows):
    checks, fails = [], []

    def chk(desc, ok, why=""):
        checks.append((desc, ok, why))
        if not ok:
            fails.append("%s -- %s" % (desc, why))

    buf = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n"

    ok = True
    for line in buf.splitlines():
        try:
            json.loads(line)
        except json.JSONDecodeError as e:
            ok = False
            chk("every line parses as JSON", False, str(e))
            break
    if ok:
        chk("every line parses as JSON", True)

    ids = [r["claim_id"] for r in rows]
    chk("claim ids unique", len(ids) == len(set(ids)))
    bad = [r["claim_id"] for r in rows if r["label"] not in LABELS]
    chk("every label is one of the five (P0 amendment F)", not bad, str(bad))
    thin = [r["claim_id"] for r in rows if len(r["claim"]) < 120]
    chk("every claim text is substantive", not thin, str(thin))
    badh = [r["claim_id"] for r in rows
            if len(r["output_hash"]) != 64
            or any(c not in "0123456789abcdef" for c in r["output_hash"])]
    chk("every output_hash is 64 hex", not badh, str(badh))

    idx = {}
    for p in HERE.rglob("*"):
        if p.is_file():
            idx.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(),
                           []).append(p)
    unres = [r["claim_id"] for r in rows if r["output_hash"] not in idx]
    chk("every output_hash resolves to a file on disk", not unres, str(unres))

    miss = [r["claim_id"] for r in rows if not (HERE / r["script"]).exists()]
    chk("every script exists", not miss, str(miss))

    # content assertions -- a claim that lost its substance must not be written
    byid = {r["claim_id"]: r for r in rows}
    chk("S40-02 names both colliding labels",
        "sec:local" in byid["S40-02"]["claim"]
        and "sec:systems" in byid["S40-02"]["claim"])
    chk("S40-04 states the two roots it distinguishes",
        "sessions/2026-09-17" in byid["S40-04"]["claim"]
        and "451" in byid["S40-04"]["claim"])
    chk("S40-04 and S40-07 request a ruling and carry a note or say so",
        "RULING REQUESTED" in byid["S40-04"]["claim"]
        and "RULING REQUESTED" in byid["S40-07"]["claim"])
    chk("S40-04 carries the review_note recording replayability",
        "replayable" in str(byid["S40-04"].get("review_note", "")))
    chk("no claim upgrades a label in prose",
        not any("therefore PROVEN" in r["claim"] for r in rows))

    # Supersession, per the operator ruling of 2026-09-20: amend by a new
    # claim, never by editing a record whose digest is cited.  A supersedes
    # field that the claim text does not also name is a silent retraction.
    sup = [r for r in rows if r.get("supersedes")]
    chk("at least one supersession is recorded", len(sup) >= 2,
        "%d found" % len(sup))
    unnamed = [r["claim_id"] for r in sup
               if r["supersedes"] not in r["claim"]]
    chk("every supersedes field is named in its own claim text",
        not unnamed, str(unnamed))
    notled = [r["claim_id"] for r in sup
              if not r["claim"].startswith("SUPERSEDES")]
    chk("every superseding claim leads with SUPERSEDES", not notled,
        str(notled))

    # The superseded ids must EXIST, or the supersession points at nothing.
    corpus = set()
    root = HERE.parents[1]
    for p in root.rglob("claims.jsonl"):
        if p.resolve() == ART.resolve():
            continue
        for line in p.read_text(encoding="utf-8-sig",
                                errors="replace").splitlines():
            m = line.find('"claim_id"')
            if m >= 0:
                try:
                    corpus.add(json.loads(line)["claim_id"])
                except Exception:
                    pass
    ghost = [r["supersedes"] for r in sup if r["supersedes"] not in corpus]
    chk("every superseded claim id resolves in the corpus", not ghost,
        str(ghost))

    chk("S40-10 does not disturb S1-04's label",
        "label PROVEN is correct and is not disturbed"
        in byid["S40-10"]["claim"])
    chk("S40-11 records that F's digest was checked before editing",
        "cited by no claim, which was checked before editing"
        in byid["S40-11"]["claim"])
    chk("S40-05 records the correction, not the conclusion",
        byid["S40-05"]["claim"].startswith("CORRECTION"))

    return buf, checks, fails


def main():
    buf, checks, fails = validate(ROWS)
    print("emit_claims_s40 -- pre-write validation")
    for desc, ok, why in checks:
        print("  %-56s %s" % (desc, "ok" if ok else "FAILED: " + why))
    if fails:
        print("\nREFUSED: %d check(s) failed; nothing written." % len(fails))
        sys.exit(1)
    ART.write_text(buf, encoding="utf-8")
    h = hashlib.sha256(ART.read_bytes()).hexdigest()
    print("\n  claims written : %d" % len(ROWS))
    print("  checks run     : %d" % len(checks))
    print("  checks failed  : 0")
    print("  claims.jsonl   : %d B  sha256 %s" % (ART.stat().st_size, h))
    print("VERDICT: CLAIMS EMITTED")


if __name__ == "__main__":
    main()
