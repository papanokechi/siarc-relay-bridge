"""Emit CT-S34 claims.

Validate in memory, encode, assert on the exact bytes destined for disk, then
write once. A post-write assertion leaves the corrupt artefact on disk; this
emitter never writes an object it has not already refused to reject.

review_note is checked against a PINNED sha256, not against the variable that
produced it. Validating a note against its own source variable is
self-referential and catches nothing.
"""
import hashlib
import io
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
ART = HERE / "claims.jsonl"
SESSION = "CT-S34-CHECKER-RULINGS"
NOTE = ("contaminated re-derivation; prior treatment of the same operator "
        "was in context")
NOTE_SHA = "88e34f289b80c5be62ab8b9e20631efb24924c8cd518ea0da6e582adc6ad7afe"
LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}

CHECKER = HERE.parent / "CT-R1-AUDIT" / "check_invariants.py"
CHK_SHA = hashlib.sha256(CHECKER.read_bytes()).hexdigest()


def H(rel):
    return hashlib.sha256((HERE / rel).read_bytes()).hexdigest()


PASS_ = H("outputs/rulings_pass.out.txt")
CTRL_ = H("outputs/verify_rulings.out.txt")
MUT_ = H("outputs/mutants.out.txt")
MEAS_ = H("outputs/measure.out.txt")
EMUT_ = H("outputs/emit_mutants.out.txt")
NOTE_ = H("NOTE-CROSS-TREE-COLLISIONS.md")
OWN_ = H("NOTE-WINDOW-OWNERSHIP.md")
PRE34 = H("refs/check_invariants.pre-S34.py")

C = [
 ("S34-01", "PROVEN", "measurement",
  "The label convention is NOT monotone, so the cutoff for invariant 2 had "
  "to be derived rather than taken as the first labelled date. Labels appear "
  "on 2026-05-13 (6 of 89) and 2026-05-14 (9 of 18), then stand at 0 per cent "
  "on every one of the nine dates 2026-05-18, -19, -20, -22, -29, 2026-06-11, "
  "-15, -16 and -18, and are universal only from 2026-09-17 (578 of 578). A "
  "cut at the first labelled date would leave 661 unlabelled claims in scope "
  "and simply fail.",
  "outputs/measure.out.txt (sha256 %s), per-date table; control 'labelling is "
  "universal on 2026-09-17 but began earlier and lapsed' would have fired had "
  "labelling been monotone." % MEAS_),

 ("S34-02", "STRUCTURAL", "source",
  "The derivation rule applied is: the earliest date D such that EVERY claim "
  "dated on or after D carries a recognised label. On this corpus D = "
  "2026-09-17. The cutoff is PINNED in the checker as a literal, not "
  "recomputed at run time, and deliberately so: a cutoff derived from the "
  "same claims it then judges is self-fulfilling, because no claim on or "
  "after it could ever be unlabelled and invariant 2 could never fail.",
  "check_invariants.py (sha256 %s) CONVENTION_DATE with its stated rationale; "
  "the checker recomputes the derived value and REPORTS disagreement without "
  "acting on it." % CHK_SHA),

 ("S34-03", "VERIFIED", "control",
  "The scoping of invariant 2 is a scoping and not a disarming. A claim "
  "dated 2026-09-18 with no label FAILS invariant 2 (exit 1); a claim dated "
  "2026-09-16 with no label is reported OUT OF SCOPE and exits 0; a claim "
  "dated ON the cutoff, 2026-09-17, is IN scope and fails. Mutant M1, which "
  "moves the cutoff one day later, is caught by the boundary control.",
  "outputs/verify_rulings.out.txt (sha256 %s) ruling 1, three controls; "
  "outputs/mutants.out.txt (sha256 %s) arm M1 CAUGHT." % (CTRL_, MUT_)),

 ("S34-04", "VERIFIED", "measurement",
  "The pre-cutoff labelled count was reported as 0 by the checker and as 15 "
  "by measure.py. The two are reconciled and neither is wrong: measure.py "
  "counts any truthy label field, the checker counts only labels in its "
  "recognised set, and the 15 are 14 PROCEED plus 1 REFINED, values from the "
  "abandoned first attempt at the convention. The checker now prints BOTH "
  "numbers; its earlier wording asserted 0 while its own tally showed the 15.",
  "outputs/rulings_pass.out.txt (sha256 %s): '0 carry a recognised label; 15 "
  "carry a label field of any kind' and the labels tally PROCEED=14 "
  "REFINED=1." % PASS_),

 ("S34-05", "STRUCTURAL", "source",
  "Invariant 1(b) is split three ways, each reused id reported under exactly "
  "one heading. (i) global uniqueness for ordinary ids, with a deposit-mirror "
  "exemption by PATH pattern; (ii) session-local counters checked for "
  "uniqueness WITHIN a session only; (iii) idless claims given their own "
  "printed line. Every pattern used as an exemption is printed with the "
  "count it exempts.",
  "check_invariants.py (sha256 %s) section 1(b); outputs/rulings_pass.out.txt "
  "(sha256 %s) prints SESSION_LOCAL_ID, MIRROR_PATH and all three headings."
  % (CHK_SHA, PASS_)),

 ("S34-06", "PROVEN", "measurement",
  "The 84 reused ids are four kinds, not the three the ruling names: 15 "
  "deposit mirrors, 10 session-local counters, and 59 that match neither "
  "exemption. The 59 are aggregator and verifier restatements "
  "(THEORY-FLEET/AGGREGATOR restating H1..H6, a verifier restating "
  "CC-MEDIAN-RESURGENCE ids, sibling R1-ROUTE-F-* sessions).",
  "outputs/measure.out.txt (sha256 %s), reused-id classification; "
  "outputs/rulings_pass.out.txt (sha256 %s) FAIL 1(b)(i) with 59."
  % (MEAS_, PASS_)),

 ("S34-07", "PROVEN", "measurement",
  "Classified a second and differently implemented way, by claim-text "
  "identity, the 84 split 74 identical-text and 10 different-text. The two "
  "classifications cross cleanly: the 10 different-text ids ARE the "
  "session-local counters, which is exactly why per-session scoping is the "
  "right treatment for them, and all 59 unexempted ids carry identical text "
  "in every place they appear. Zero ids duplicate within a single file.",
  "outputs/measure.out.txt (sha256 %s); control 'the copy/collision split "
  "accounts for every reused id' would have fired had any id fallen outside "
  "both." % MEAS_),

 ("S34-08", "STRUCTURAL", "source_and_control",
  "Text identity was deliberately NOT made an exemption. Accepting it would "
  "absorb all 59 without a ruling, which is loosening rather than scoping. "
  "The 59 are reported in full, with the identical-text finding stated "
  "alongside them, so the convention can be ruled on. Mutant M5 injects "
  "exactly that loosening and is caught.",
  "outputs/rulings_pass.out.txt (sha256 %s): 'Text identity is NOT accepted "
  "here as an exemption: no pattern was invented to absorb them'; "
  "outputs/mutants.out.txt (sha256 %s) arm M5 CAUGHT." % (PASS_, MUT_)),

 ("S34-09", "VERIFIED", "control",
  "The exemptions do not disable the checks they sit inside. A genuine "
  "cross-session collision with DIFFERENT text still fails 1(b)(i) and is "
  "named a true collision; a counter reused WITHIN one session fails "
  "1(b)(ii); a mirror NOT at a deposit/ path is still reported. Mutants M2 "
  "(counter pattern widened to match any id), M3 (within-session threshold "
  "raised) and M4 (mirror pattern unanchored) are each caught.",
  "outputs/verify_rulings.out.txt (sha256 %s) ruling 2, six controls; "
  "outputs/mutants.out.txt (sha256 %s) arms M2, M3, M4 CAUGHT."
  % (CTRL_, MUT_)),

 ("S34-10", "STRUCTURAL", "source",
  "The 2641 idless claims are reported on their own line, worded 'This is a "
  "hole, not a pass.' They are outside every uniqueness check and the output "
  "now says so rather than leaving them silently outside 1(b). Mutant M7, "
  "which silences the line, is caught.",
  "outputs/rulings_pass.out.txt (sha256 %s) 1(b)(iii); outputs/mutants.out.txt "
  "(sha256 %s) arm M7 CAUGHT." % (PASS_, MUT_)),

 ("S34-11", "STRUCTURAL", "source_and_control",
  "The one unreadable claim is left unrepaired by ruling. It is identified by "
  "path and line, sessions/2026-04-30/SIARC-COHERENCE-AUDIT/claims.jsonl line "
  "3, a raw LaTeX \\(2,2\\) inside a JSON string, and tagged KNOWN HOLE with "
  "the ruling that left it. The known-hole list is exact, not a blanket "
  "amnesty: a DIFFERENT damaged line is reported as NEW DAMAGE. Mutant M6 "
  "turns the list into an amnesty and is caught.",
  "outputs/rulings_pass.out.txt (sha256 %s) invariant 5; "
  "outputs/verify_rulings.out.txt (sha256 %s) ruling 3, two controls; "
  "outputs/mutants.out.txt (sha256 %s) arm M6 CAUGHT."
  % (PASS_, CTRL_, MUT_)),

 ("S34-12", "STRUCTURAL", "source",
  "C:\\LocalWork\\SCOPE is removed from ROOTS and named in EXCLUDE with three "
  "printed reasons: it is written by other processes mid-run, so a verdict "
  "over it has a race in it and the checker can disagree with itself between "
  "two runs minutes apart; Window B's status is unsettled; and it collides "
  "with the repository tree by session number. The input fingerprint is kept, "
  "so a count difference is still attributed before being called a "
  "disagreement.",
  "check_invariants.py (sha256 %s) EXCLUDE; outputs/rulings_pass.out.txt "
  "(sha256 %s) prints the exclusion, the three reasons and the fingerprint; "
  "four controls in outputs/verify_rulings.out.txt (sha256 %s) ruling 4."
  % (CHK_SHA, PASS_, CTRL_)),

 ("S34-13", "INSPECTED", "source",
  "The two cross-tree collisions are recorded in a note that renames nothing: "
  "CT-S32 is CT-S32-LD2-ORDINARY-LOCUS in the repository and "
  "CT-S32-PACKET-SEALED in SCOPE; CT-S33 is CT-S33-CHECKER-SCOPE and "
  "CT-S33-COLDREAD-OUTPUT. The ambiguity reaches the claim ids, since both "
  "trees mint S<n>-<nn>. Going forward SCOPE sessions take the prefix SC-Sn.",
  "NOTE-CROSS-TREE-COLLISIONS.md (sha256 %s)." % NOTE_),

 ("S34-14", "VERIFIED", "control",
  "Every change in this session is a scoping or a reporting change and none "
  "is a loosening. Seven mutant arms, each injecting exactly the loosening "
  "one ruling forbids, are all CAUGHT by the control harness, and the checker "
  "under test is byte-identical before and after.",
  "outputs/mutants.out.txt (sha256 %s): 7/7 CAUGHT, byte-identical True; "
  "outputs/verify_rulings.out.txt (sha256 %s): 20/20 PASS." % (MUT_, CTRL_)),

 ("S34-15", "INSPECTED", "measurement",
  "Two defects in this session's own instruments were found and repaired, "
  "both by the three-condition mutant test. First, all seven arms reported "
  "MISSED because the copied control harness resolved HERE to the temporary "
  "directory and died on a missing refs/ file before judging anything; a "
  "two-condition arm testing only 'refused' would have reported CAUGHT seven "
  "times. Second, arm M1 reported MISSED because the harness PINNED the "
  "cutoff and refused the mutant structurally instead of letting the boundary "
  "control fail; the harness now derives the cutoff from the source under "
  "test.",
  "verify_rulings.py derives CUTOFF by regex from SRC; mutants.py carries the "
  "broke_script guard distinguishing an AssertionError from a harness that "
  "died; outputs/mutants.out.txt (sha256 %s) 7/7 after repair." % MUT_),

 ("S34-16", "INSPECTED", "source",
  "The predecessor checker is preserved before overwriting. "
  "check_invariants.py is untracked by git, so no version control would have "
  "retained it.",
  "refs/check_invariants.pre-S34.py (sha256 %s), hash-verified equal to the "
  "source and to the value CT-S33 cites before the original was replaced."
  % PRE34),

 ("S34-17", "STRUCTURAL", "measurement",
  "The widened, ruled pass exits 1 over 4066 claims in 442 files under one "
  "root, with two invariants failing: 1(b)(i) with 59 unexempted reused ids, "
  "and 5 with 9 non-JSONL files. Invariants 0, 1(a), 1(b)(ii), 2, 3 and 4 "
  "pass. A remaining failure is information about the record, not a defect in "
  "the checker and not something to repair by loosening it.",
  "outputs/rulings_pass.out.txt (sha256 %s), exit 1." % PASS_),

 ("S34-18", "VERIFIED", "control",
  "The claims emitter for this session validates its in-memory buffer and "
  "then the exact bytes destined for disk, and only then writes. Eight mutant "
  "arms -- altered review_note against its pinned hash, an unrecognised "
  "label, a duplicate id, a gap in the id sequence, evidence stripped of its "
  "hash, a CR injected into the bytes, review flipped away from self, and an "
  "out-of-scope phrase -- are all CAUGHT with claims.jsonl byte-identical "
  "after every arm. Byte-identity is the condition that distinguishes a "
  "pre-write check from a post-write one.",
  "outputs/emit_mutants.out.txt (sha256 %s): 8/8 CAUGHT, artefact intact=True "
  "on every arm." % EMUT_),

 ("S34-19", "INSPECTED", "control",
  "Two further instrument defects, both found by requiring the injected "
  "reason and both of the same class -- an arm refused for the WRONG reason. "
  "Arm E5 injected a substitute evidence string shorter than the emitter's "
  "length floor, so the length assertion fired instead of the hash "
  "assertion. Arm E4, renaming a claim to create a gap in the id sequence, "
  "chose an id that collided with a real one, so the uniqueness assertion "
  "fired instead of the contiguity assertion. Both were repaired; neither "
  "was a pass. Counting only 'refused' would have scored both CAUGHT.",
  "outputs/emit_mutants.out.txt (sha256 %s), arms E4 and E5 CAUGHT after "
  "repair with right_reason=True." % EMUT_),

 ("S34-20", "PROVEN", "measurement",
  "The repository tree is ALSO written concurrently, so the race that "
  "justified removing SCOPE from ROOTS is not confined to SCOPE. Two runs of "
  "the same checker this session returned different input fingerprints over "
  "different file counts: a37d6601e12fc9f0 over 445 files and 4066 claims, "
  "and a later run over 447 files. The difference is this session's own "
  "claims plus 14 that arrived in "
  "sessions/2026-09-17/CT-S35-CTV17-ITEM6/claims.jsonl, written by another "
  "process at 22:29 while this session was running. The difference was "
  "ATTRIBUTED before being called a disagreement, which is exactly what the "
  "fingerprint was added for.",
  "outputs/rulings_pass.out.txt (sha256 %s) and outputs/post_emit_pass.out.txt "
  "carry the two fingerprints and file counts; the intruding file's mtime was "
  "read directly and the file was not otherwise touched." % PASS_),

 ("S34-21", "VERIFIED", "control",
  "A citation inside this session was broken by the same liveness, and was "
  "caught only by a resolver written for the purpose. outputs/measure.out.txt "
  "is produced by WALKING the corpus, and the corpus now contains this "
  "session's own claims, so re-running measure.py after emission changed that "
  "file and left three claims citing a digest that resolved to nothing. The "
  "ordering is now fixed -- measure, then emit, then never measure again -- "
  "and a control asserts the file on disk still matches the digest the claims "
  "cite. A digest is not evidence unless something on disk answers to it.",
  "scripts/verify_claim_citations.py resolves every sha256 in claims.jsonl "
  "against a file on disk, with three controls; it reported BROKEN for "
  "17d5d74af9ce132a before the ordering was corrected."),

 ("S34-22", "VERIFIED", "control",
  "The input fingerprint is printed on EVERY completed run, not only on "
  "passing ones: it is emitted before any invariant is judged and the "
  "checker's only exit is its last statement. A failing run prints it, a run "
  "over an empty corpus prints it and states 'over 0 file(s) read', and the "
  "real run prints exactly one full 64-hex value. This is what makes two runs "
  "reconcilable; two runs cannot be compared if the one that failed printed "
  "nothing.",
  "outputs/verify_rulings.out.txt (sha256 %s), ruling 4, controls r4a, r4b "
  "and the single-full-64-hex check, 23/23 PASS." % CTRL_),

 ("S34-23", "STRUCTURAL", "source",
  "Concurrent writes have now produced a false disagreement twice, and the "
  "second was inside the git repository, which had been treated as the quiet "
  "tree. A window-ownership convention is recorded: one window owns a tree at "
  "a time, ownership is by tree rather than by folder, a non-owning window "
  "must not create a session folder, and reading is always permitted. The "
  "convention cannot be enforced; its purpose is to make concurrent writing "
  "visible and attributable rather than an unexplained number.",
  "NOTE-WINDOW-OWNERSHIP.md (sha256 %s), recording both incidents: "
  "CT-S30-PACKET-BUILD growing by three claims mid-run, and "
  "CT-S35-CTV17-ITEM6 appearing at 22:29:13." % OWN_),
]

rows = []
for cid, label, ev_type, text, evidence in C:
    rows.append({"claim_id": cid, "label": label, "evidence_type": ev_type,
                 "claim": text, "review": "self", "review_note": NOTE,
                 "session": SESSION, "evidence": evidence})

# ---- validate the objects, then the exact bytes, BEFORE writing -----------
assert hashlib.sha256(NOTE.encode("utf-8")).hexdigest() == NOTE_SHA, \
    "review_note does not match its pinned hash"
ids = [r["claim_id"] for r in rows]
assert len(set(ids)) == len(ids) == 23
assert ids == ["S34-%02d" % i for i in range(1, 24)], "ids not contiguous"
for r in rows:
    assert r["label"] in LABELS
    assert r["review"] == "self" and r["review_note"] == NOTE
    assert r["session"] == SESSION
    assert len(r["claim"]) > 80 and len(r["evidence"]) > 20
    assert "sha256" in r["evidence"] or "untracked" in r["evidence"]
    for bad in ("Bridge Conjecture", "membership", "isomonodromic"):
        assert bad not in r["claim"], "out of scope: %s" % bad

text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
blob = text.encode("utf-8")
assert b"\r" not in blob, "CR in the bytes destined for disk"
assert blob.endswith(b"\n") and not blob.startswith(b"\xef\xbb\xbf")
H_OUT = hashlib.sha256(blob).hexdigest()
ART.write_bytes(blob)

raw = ART.read_bytes()
assert raw == blob and hashlib.sha256(raw).hexdigest() == H_OUT
back = [json.loads(l) for l in io.StringIO(raw.decode("utf-8"))]
assert len(back) == 23 and [b["claim_id"] for b in back] == ids
assert "\\(2,2\\)" in back[10]["claim"], "escaped LaTeX did not survive"
print("wrote %d claims  sha256 = %s  bytes = %d" % (len(back), H_OUT, len(raw)))
