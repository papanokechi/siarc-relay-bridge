"""emit_claims_s35.py -- CT-S35-CTV17-ITEM6

Writes claims.jsonl for the respecified sixth item.

Validation is on the in-memory buffer BEFORE any write: a post-write assertion
still leaves the corrupt artefact on disk.  The bytes destined for disk are the
object validated, not the pre-serialisation string, because json.dumps escapes
a carriage return into two characters and a check on the string cannot see it.
"""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
OUT = os.path.join(SESSION, "claims.jsonl")
SCOPE = r"C:\LocalWork\SCOPE"

TASK = "CT-S35-CTV17-ITEM6"


def h(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


O = lambda n: os.path.join(SESSION, "outputs", n)
PAGE_2635 = os.path.join(SESSION, "pages", "vdPS_p2635.png")
PAGE_2634 = os.path.join(SCOPE, "CT-S32-PACKET-SEALED", "packet", "pages",
                         "vdPS_p2634.png")

BY_EYE = "n/a -- printed folio read by eye from the page image; no script"

C = [
    dict(claim_id="S35-01",
         claim="Table 2.1 of van der Put-Saito (AIF 59-7, 2009) as quoted in "
               "NOTICE-v1.7-rev3.md section 7.1 agrees line for line with the "
               "printed folio 2635; the D-tilde-5 / P_V row prints r(0)=0, "
               "r(1)=0, r(inf)=1, r(t)=-, dim P=3, and the only rows whose "
               "multiset contains 1/2 are D-tilde-6, D-tilde-7 and D-tilde-8.",
         label="VERIFIED", evidence_type="file_inspection", dps=None,
         script=BY_EYE, output_hash=h(PAGE_2635)),
    dict(claim_id="S35-02",
         claim="The identification of the table's r(.) columns with Katz "
               "invariants is the source's own, stated on folio 2634 ('We will "
               "not number these ten families, but indicate them by their Katz "
               "invariants'), and the classification there is of rank-2 "
               "trace-zero connections on P^1, so the comparison is legitimate "
               "at d = 2 and must not be extended to other degrees.",
         label="VERIFIED", evidence_type="file_inspection", dps=None,
         script=BY_EYE, output_hash=h(PAGE_2634)),
    dict(claim_id="S35-03",
         claim="TIER 1. At z = 0 the Newton polygon of L_d at d = 2 gives Katz "
               "invariant 1/2 for every admissible coefficient vector, so the "
               "multiset always contains 1/2; the D-tilde-5 / P_V row contains "
               "no 1/2; therefore that row is excluded for every coefficient "
               "choice. Independently reached by an isolated reader given only "
               "the operator and the page images (CT-S34), and by this corpus.",
         label="STRUCTURAL", evidence_type="file_inspection", dps=None,
         script=BY_EYE,
         output_hash=h(os.path.join(SCOPE, "CT-S34-COLDREAD-OUTPUT",
                                    "REPORT.md"))),
    dict(claim_id="S35-04",
         claim="TIER 2. The rows reachable at d = 2, deg b = 2 are PIII(D8), "
               "PIII(D7) and degenerate P_V = PIII(D6), selected by deg a = 0, "
               "1, 2 respectively. Reproduced by the second isolated reader "
               "without being told the set; the first reader assumed "
               "deg a = deg b and so confirms the exclusion only.",
         label="STRUCTURAL", evidence_type="file_inspection", dps=None,
         review="cold",
         review_note="Re-derivable but not replayable: the second isolated "
                     "reader (CT-S34) left a prose report and no script, so "
                     "this result can be obtained again from the operator and "
                     "the page images by a reader who repeats the derivation, "
                     "but it cannot be replayed by executing anything. "
                     "Reproduction and label are different axes: a second "
                     "reading raises confidence without changing what the "
                     "claim can support, and the row matches remain necessary "
                     "conditions only, so the label stays STRUCTURAL.",
         script=BY_EYE,
         output_hash=h(os.path.join(SCOPE, "CT-S34-COLDREAD-OUTPUT",
                                    "REPORT.md"))),
    dict(claim_id="S35-05",
         claim="TIER 3. Generically the row depends only on (alpha_2, alpha_1); "
               "on the codimension-3 locus a(1) = a(2) = 0 and b(1) = 0 the "
               "point at infinity becomes ordinary and the multiset matches no "
               "row of Table 2.1. Self-derived, by a re-derivation that ran in "
               "a workspace another process was writing into and that corrected "
               "an earlier error of its own. Not independently confirmed.",
         label="STRUCTURAL", evidence_type="file_inspection", dps=None,
         script=BY_EYE,
         output_hash=h(os.path.join(SCOPE, "CT-S30-PACKET-BUILD",
                                    "claims.jsonl"))),
    dict(claim_id="S35-06",
         claim="A matching multiset is a necessary condition only: the "
               "procedure of section 7 excludes rows and assigns none, and the "
               "notice asserts no Painleve label for V_quad. Enforced by gate "
               "check N6, whose mutants append an explicit row assignment.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-07",
         claim="The record's label history is stated on both sides -- the "
               "v1.0-v1.3 P-III(D6) label inside the surviving set, the v1.4 "
               "P_V / D5^(1) label outside it -- and neither is adjudicated, "
               "because a row exclusion is not a row assignment. Enforced by "
               "gate check N7, whose mutants adjudicate in each direction.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-08",
         claim="The tier of each sentence is recoverable from the text itself: "
               "each tier carries an in-prose marker naming its level of "
               "confirmation, not only a heading. Enforced by gate check N5b, "
               "whose mutant demotes a marker to a bare heading.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-09",
         claim="DESCRIPTION-v1.7-rev3.html is 68303 chars / 68606 bytes, "
               "sha256 33a3893372dfd9dcd2c89c4202b8db5aa6d8914acf4707bfd93e744"
               "2f8c7e293, md5 cdfa63630469ee75834acd725a64415b, all read from "
               "disk after the final edit. The hashes 026e7a9e... and "
               "39903126... quoted earlier in this packet are superseded; gate "
               "check N8 fails if either is published as a current value.",
         label="VERIFIED", evidence_type="computation", dps=None,
         script="scripts/make_description.py",
         output_hash=h(O("make_description_s35.out.txt"))),
    dict(claim_id="S35-10",
         claim="The description gate runs 21 checks with 0 failures and 0 "
               "broken controls, and 3 of 3 reader-path controls caught; the "
               "deposit gate runs 11 checks, 0 failures, 3 of 3 reader "
               "controls, GATE: PASSED. S2 fired first on the stale rev2 hash, "
               "which is the behaviour it exists for.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/preflight_deposit_rev2.py",
         output_hash=h(O("preflight_deposit_s35.out.txt"))),
    dict(claim_id="S35-11",
         claim="DEFECT, repaired. Check N5's overclaim scan was sentence-scoped "
               "and reported section 7.5's correct prose -- 'a mismatch ... is "
               "VERIFIED ...; a match does not, because it leaves open whether "
               "L_d actually lies in the corresponding moduli family' -- as an "
               "overclaim. The check invented a defect. Repaired to clause "
               "scope with hedged clauses exempt, and given a boundary mutant "
               "asserting an unhedged match as VERIFIED, which is caught.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-12",
         claim="DEFECT, repaired, caught by a mutant and not by reading. The "
               "clause splitter split on the period inside 'v1.4', so check "
               "N7's v1.4 arm had no clause containing 'v1.4' and could never "
               "match; two N7 mutants were ACCEPTED and the harness reported "
               "BROKEN rather than passing. Repaired by not treating a period "
               "between digits as a clause boundary.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-13",
         claim="DEFECT, repaired. N7's pattern 'was (therefore )?correct' "
               "matched inside the notice's own phrase 'was corrected at v1.4', "
               "reporting a correct sentence as an adjudication. A missing word "
               "boundary, in the same class as S35-11: a check that invents a "
               "defect costs what missing one costs. Repaired with \\b(?!ed).",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-14",
         claim="DISCLOSURE. Checks N5 and N7 were narrowed after seeing their "
               "results. Both narrowings were accompanied in the same edit by "
               "boundary mutants drawn from outside the checks' own pattern "
               "lists (an unhedged 'A match is VERIFIED and L_d lies in that "
               "family'; 'The v1.4 correction was mistaken, though not by "
               "much'), each of which is caught, so the narrowing is bounded "
               "by tests rather than by assertion.",
         label="STRUCTURAL", evidence_type="build", dps=None,
         script="scripts/verify_description.py",
         output_hash=h(O("verify_description_s35.out.txt"))),
    dict(claim_id="S35-15",
         claim="DEFECT, repaired, found while implementing an operator ruling. "
               "This emitter projected every claim through "
               "{k: c[k] for k in REQUIRED}, so the review_note the ruling "
               "required on S35-04 would have been SILENTLY DROPPED and the "
               "claims file would have looked correct and complete without it. "
               "A projection against a fixed key list discards, without "
               "symptom, anything a later instruction adds. Repaired with an "
               "OPTIONAL carry-list, an assertion that no unrecognised key is "
               "dropped, and two pre-write assertions on S35-04's note and "
               "label; three mutants (note removed, label promoted to "
               "VERIFIED, note silent on replayability) are all caught "
               "pre-write with claims.jsonl byte-identical.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/mutants_review_note.py",
         output_hash=h(O("mutants_review_note.out.txt"))),
    dict(claim_id="S35-16",
         claim="DEFECT, repaired, found while preparing to hand over the "
               "publishing steps. The deposit packet was copied forward from "
               "CT-S27 and three places still pointed at the superseded "
               "revision: WALKTHROUGH.md sections 2 and 4 told the operator to "
               "cd into CT-S27-CTV17-DEPOSIT-PREP, and postpublish_readback.py "
               "and selftest_readback.py both read DESCRIPTION-v1.7-rev2.html. "
               "Followed literally the pre-flight would have gated the rev2 "
               "artefact while rev3 was pasted, and the post-publish readback "
               "would have compared the live v1.7 record against the revision "
               "WITHOUT the sixth item. Comparing the wrong artefact is worse "
               "than not comparing, because the result is believed. Repaired: "
               "paths corrected, and a guard added that resolves the expected "
               "digest from the gate run's own output rather than a constant "
               "and aborts before any network call. Two input-path controls "
               "(stale description, absent description) both fire.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/mutants_readback_guard.py",
         output_hash=h(O("mutants_readback_guard.out.txt"))),
    dict(claim_id="S35-17",
         claim="The post-publish readback accepts the packet and rejects all "
               "12 negative fixtures, each on its own check, with 0 broken, "
               "now reading DESCRIPTION-v1.7-rev3.html. (Ten at the time this "
               "claim was first written; two were added on 2026-09-20 with the "
               "repair recorded in S35-22, and the count is restated here "
               "rather than left to drift.) The walkthrough's S2a "
               "step was rewritten to compare the file on disk against the "
               "sha256 recorded by the passing gate run instead of against a "
               "quoted constant, and both its arms were exercised: the real "
               "file prints MATCH and a one-byte-modified copy prints STOP.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/selftest_readback.py",
         output_hash=h(O("selftest_readback_s35.out.txt"))),
    dict(claim_id="S35-18",
         claim="GOVERNANCE, ruled by the operator 2026-09-19. Two standing "
               "forms are adopted out of S35-16. (i) Before an irreversible "
               "paste, do not print an expected hash for comparison by eye: "
               "comparing a file against a quoted constant verifies the "
               "quotation, not the file. Resolve the expected digest from the "
               "passing gate run's own output, compare the file on disk, emit "
               "one word, and abort before any network call. (ii) Recorded as "
               "a CANDIDATE P0 amendment only, not ruled: an instruction "
               "document is an artefact and must be executed, not proofread. "
               "Form (i) is implemented and has exercised arms; form (ii) is "
               "recorded as a candidate and is not counted as adopted.",
         label="STRUCTURAL", evidence_type="build", dps=None,
         script="scripts/mutants_readback_guard.py",
         output_hash=h(O("mutants_readback_guard.out.txt"))),
    dict(claim_id="S35-19",
         claim="DEFECT, found and repaired 2026-09-19 by EXECUTING "
               "WALKTHROUGH.md rather than reading it -- the candidate form "
               "(ii) of S35-18 applied to itself. Five statements in the "
               "walkthrough were false at the time of the handover, all of "
               "them invisible to both gates, which verify the description "
               "and not the instructions for depositing it. (1) Section 0 "
               "reported verify_description.py as '13/13'; it runs 21 checks, "
               "so the stated count would have made a gate running FEWER "
               "checks than expected look correct. (2) Section 5's truncation "
               "row named a 54068-char description; rev3 is 68303, understating "
               "the field limit that matters by 14235 characters. (3) Section 2 "
               "instructed the operator to take a hash and compare it by eye "
               "against a constant printed in the file -- the exact form "
               "S35-18(i) exists to remove, left behind when S2a superseded "
               "it. (4) Section 6 said the publication of the section-10 "
               "source table was an unsettled operator decision and that 'the "
               "current description keeps it'; it was settled and the table "
               "was excluded -- the description contains zero occurrences of "
               "refs/, outputs/ or any CT-S session id. (5) Section 2's own "
               "command, 'Select-Object -Last 12', displays GATE: PASSED but "
               "truncates 'checks run : 11' and 'checks failed : 0', so it "
               "hides the counts the corrected text tells the reader to check; "
               "widened to -Last 16 and re-executed. Defects 1, 2 and 4 are "
               "stale-value drift of the class ruled in P0 Amendment D; defect "
               "3 is a superseded procedure surviving its replacement; defect "
               "5 could only be found by running the block.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/verify_walkthrough.py",
         output_hash=h(O("verify_walkthrough_s35.out.txt"))),
    dict(claim_id="S35-20",
         claim="INSTRUMENT, 2026-09-19. scripts/verify_walkthrough.py gates "
               "the deposit INSTRUCTIONS against the artefacts they describe: "
               "8 checks (W1 quoted check counts equal the gates' own output, "
               "W2 quoted sizes are the current revision's, W3 no eye-compared "
               "hash constant, W4 every cd targets this session, W5 every file "
               "a runnable block reads exists, W6 the stated exclusion of "
               "internal paths is true of the description, W7 the carried file "
               "agrees with DEPOSIT-FORM, W8 the display commands are EXECUTED "
               "and must not hide the counts the prose tells the reader to "
               "check), 0 failed, 0 broken, 3/3 reader-integrity controls. "
               "scripts/mutants_walkthrough.py catches 6/6 arms, each by the "
               "specific check that should catch it, with a baseline arm, a "
               "broke-the-gate guard and WALKTHROUGH.md verified unchanged. "
               "Building it produced three instrument defects, all found by "
               "running it rather than reading it: (i) the description's "
               "non-ASCII sentinel was chosen as a literal xi, which the file "
               "escapes as an entity, so the gate refused a sound file on its "
               "first run -- diagnosed as a reader defect only by a second, "
               "differently-implemented read of the raw bytes, which found 16 "
               "raw non-ASCII codepoints and 35 &xi; entities; (ii) W5 treated "
               "a redirect target as a required input and failed on an output "
               "file that cannot exist before publishing, conflating 'points "
               "at a missing input' with 'this step has not run yet'; (iii) "
               "W1's pattern required bold '**N/N**' while section 0 writes "
               "'21/21' unbolded, so the check could not see the only count in "
               "the file. Defect (iii) was exposed by mutant M1, whose anchor "
               "was taken from the packet's real history and not from W1's "
               "pattern -- P0 Amendment E doing exactly what it was ruled for.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/mutants_walkthrough.py",
         output_hash=h(O("mutants_walkthrough.out.txt"))),

    dict(claim_id="S35-21",
         claim="DEPOSIT, 2026-09-20. Channel Theory v1.7 is published as "
               "Zenodo record 22850681, DOI 10.5281/zenodo.22850681, under the "
               "unchanged concept DOI 10.5281/zenodo.19941678 read from the "
               "record's conceptdoi field and not derived from the record "
               "number. scripts/postpublish_readback.py verifies the live "
               "record against the gate-verified packet in 20 checks, 0 "
               "failed: version is 1.7; exactly one file is published, "
               "channel_theory_outline.pdf, 609300 bytes, md5 "
               "aa56a94a9354b5533b04c89461950eb1, i.e. the v1.6 build carried "
               "over unchanged with no file uploaded; the published "
               "description matches DESCRIPTION-v1.7-rev3.html on every one of "
               "45939 non-whitespace characters; the five load-bearing "
               "sentences survived; no draft-stage language is present; title, "
               "creator, affiliation, licence and all 27 keywords are "
               "unchanged from v1.6. Exactly two fields changed, description "
               "and version; publication_date 2026-09-19 is set by the "
               "platform. The deposited text is now authoritative and this "
               "repository's copy is the one that may go stale.",
         label="VERIFIED", evidence_type="file_inspection", dps=None,
         script="scripts/postpublish_readback.py",
         output_hash=h(O("postpublish_readback.out.txt"))),

    dict(claim_id="S35-22",
         claim="INSTRUMENT, 2026-09-20. The first live readback reported "
               "'VERDICT: the published record is NOT the packet that was "
               "checked' on a record that was character-for-character correct. "
               "The defect was in the checker: plain() substitutes a SPACE for "
               "every stripped tag, so an inline tag between two non-space "
               "characters manufactures a space that is not in the text; "
               "Zenodo's editor re-serialises inline markup on save, and the "
               "two sides disagreed by exactly 10 such phantom spaces, each "
               "adjacent to punctuation or inside S_{zeta}. The same check's "
               "own failure message already said 're-serialisation is "
               "expected', so it contradicted its own test. Diagnosed as a "
               "reader defect, not a record defect, by a second "
               "differently-implemented read before anything was changed: an "
               "independent renderer returned identical token streams and "
               "equal lengths, and squeezing whitespace made the two texts "
               "identical. Repaired by comparing on whitespace-squeezed text "
               "plus a non-vacuity guard, since two empty strings compare "
               "equal. The repair is two-sided (P0 Amendment E / P2): "
               "selftest_readback.py now rejects 12/12 negatives -- including "
               "two new ones, a dropped qualification and an altered value, "
               "each firing on this check alone -- and a new ARM 3 requires "
               "the re-serialised record, 862 inline tags removed, to be "
               "ACCEPTED, so the check cannot pass by rejecting everything.",
         label="VERIFIED", evidence_type="build", dps=None,
         script="scripts/selftest_readback.py",
         output_hash=h(O("selftest_readback_s35.out.txt"))),

    dict(claim_id="S35-23",
         claim="CARRY-FORWARD to v1.8, recorded 2026-09-20 from an operator "
               "ruling; changes nothing in the published v1.7. The published "
               "title of record 22850681 names the xi_0 = 2/sqrt(beta_2) "
               "identity as one of three headline contributions, while the "
               "v1.7 notice attributes that identity to Perron-Kreuser plus "
               "Pincherle (7, 7 and 10 occurrences of Perron, Kreuser and "
               "Pincherle in the published description). Title and text "
               "therefore disagree about what is new, and section 0 of v1.8 "
               "should state that the identity named in the title is classical "
               "and that the Bridge Conjecture is the record's remaining "
               "conjectural content. Observed while checking this and not "
               "previously reported: 'Bridge Conjecture' occurs 0 times in the "
               "published description, and the single case-insensitive "
               "occurrence of 'bridge' is 'the bridge tiering', not the "
               "conjecture -- so the one title item the notice does not "
               "attribute away is also the one it never names. Counts are "
               "taken from the archived published record, not the network, and "
               "are reported only after five reader-integrity assertions "
               "including two non-ASCII ones, because 'Bridge Conjecture: 0' "
               "and 'my reader could not see the file' are otherwise identical "
               "output. No claim is made that the absence is a defect.",
         label="VERIFIED", evidence_type="file_inspection", dps=None,
         script="scripts/count_title_terms.py",
         output_hash=h(O("count_title_terms.out.txt"))),

    dict(claim_id="S35-24",
         claim="GOVERNANCE, proposed and approved by the operator 2026-09-20. "
               "P0 Amendment C's symmetry bullet gains a NAMED CONSTRUCT "
               "clause: substituting a space for a stripped tag, "
               "re.sub of '<[^>]+>' to ' ' and its equivalents, manufactures a "
               "character at every tag boundary, so the rendered string is not "
               "the document's text and must not be compared, counted or "
               "pattern-matched for whitespace-adjacent features. This is a "
               "revision to C, not a sixth amendment: it adds no requirement "
               "and names a construct, so that the defect becomes greppable "
               "rather than dependent on the principle being remembered. The "
               "construct has produced a phantom twice -- 85 findings in "
               "S27-19 and a false negative verdict at the irreversible step "
               "in S35-22. Recorded in P0-AMENDMENT-C-REVISION.md in this "
               "session because P0-AMENDMENTS-ABCD.md lives in "
               "CT-S27-CTV17-DEPOSIT-PREP and earlier sessions are not edited. "
               "The first draft of that file asserted, without checking, that "
               "the construct also occurred in verify_description.py; grepping "
               "showed it is in make_description.py line 612 instead, and that "
               "verify_description.py line 93 uses the correct empty-string "
               "form. The invented assertion and its correction are recorded "
               "in the file rather than silently fixed. make_description.py is "
               "left unrepaired and carried forward: a phantom there halts a "
               "build rather than publishing anything wrong.",
         label="STRUCTURAL", evidence_type="file_inspection", dps=None,
         script="scripts/count_title_terms.py",
         output_hash=h(O("count_title_terms.out.txt"))),
]

REQUIRED = ("claim_id", "task_id", "claim", "label", "evidence_type", "dps",
            "reproducible", "script", "output_hash")
OPTIONAL = ("review", "review_note")

rows = []
for c in C:
    c = dict(c)
    c["task_id"] = TASK
    c["reproducible"] = True
    unknown = set(c) - set(REQUIRED) - set(OPTIONAL)
    assert not unknown, "unrecognised key would be silently dropped: %s" % unknown
    rows.append({k: c[k] for k in REQUIRED if k in c} |
                {k: c[k] for k in OPTIONAL if k in c})

text = "".join(json.dumps(r, ensure_ascii=True) + "\n" for r in rows)
blob = text.encode("utf-8")

# ---- validation of the exact bytes destined for disk, BEFORE writing --------
assert b"\r" not in blob, "carriage return in the bytes destined for disk"
ids = [r["claim_id"] for r in rows]
assert len(ids) == len(set(ids)), "duplicate claim_id"
assert ids == sorted(ids), "claim_ids out of order"
for r in rows:
    assert r["label"] in ("PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED"), r
    assert all(k in r for k in REQUIRED), r["claim_id"]
    assert r["claim"].strip() and len(r["claim"]) > 40, r["claim_id"]
    assert len(r["output_hash"]) == 64, r["claim_id"]
    assert r["script"], r["claim_id"]
# operator ruling, 2026-09-19: the Tier 2 claim must carry the
# re-derivable-but-not-replayable distinction on the claim itself, not only in
# REPORT.md.  Asserted here so the projection above cannot drop it silently.
_t2 = [r for r in rows if r["claim_id"] == "S35-04"]
assert len(_t2) == 1, "the Tier 2 claim S35-04 is missing"
_n = _t2[0].get("review_note", "")
assert "not replayable" in _n and "no script" in _n, \
    "S35-04 must record that the second reading is re-derivable but not replayable"
assert _t2[0]["label"] == "STRUCTURAL", "S35-04 label must stay STRUCTURAL"
# corpus invariants 3 and 4 (CT-R1-AUDIT/check_invariants.py): a `review` value
# must be one of self|cold|lean, and any claim carrying `review` must also carry
# `review_note`.  Tier 2 was reproduced by an isolated cold reader.
for _r in rows:
    if "review" in _r:
        assert _r["review"] in ("self", "cold", "lean"), _r["claim_id"]
        assert _r.get("review_note", "").strip(), \
            "%s carries review without review_note" % _r["claim_id"]
assert _t2[0].get("review") == "cold", "S35-04 records a cold-read reproduction"
for line in blob.decode("utf-8").splitlines():
    json.loads(line)
assert not any(r["label"] == "PROVEN" for r in rows), \
    "no claim in this session is a complete proof"

io.open(OUT, "wb").write(blob)
print("claims.jsonl written: %d claims" % len(rows))
print("  sha256 : %s" % h(OUT))
for r in rows:
    print("  %-8s %-11s %s" % (r["claim_id"], r["label"], r["claim"][:64]))
