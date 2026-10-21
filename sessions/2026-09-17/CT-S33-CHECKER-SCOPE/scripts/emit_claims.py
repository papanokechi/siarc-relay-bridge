"""Emit CT-S33 claims. Validate in memory BEFORE writing.

The order matters and is not cosmetic. CT-S28 defect 6.3 and CT-S32 mutant arm
M6 were both emitters that refused a bad artefact only in their post-write
read-back, leaving the bad artefact on disk. Every assertion here runs against
the in-memory text; the file is opened only once the text has passed.
"""
import hashlib
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
OUT = HERE / "claims.jsonl"
NOTE = "contaminated re-derivation; prior treatment of the same operator was in context"

# The note is pinned by a hash, not only by the variable. Asserting
# c["review_note"] == NOTE alone is self-referential: edit NOTE and every
# claim still "matches". A second, independent encoding of the same constant
# is what makes the check able to fail. (Same reason a mutant drawn from a
# check's own constant list proves only that the list is consulted.)
NOTE_SHA = "88e34f289b80c5be62ab8b9e20631efb24924c8cd518ea0da6e582adc6ad7afe"
assert hashlib.sha256(NOTE.encode("utf-8")).hexdigest() == NOTE_SHA, \
    "review_note text does not match its pinned hash"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}

C = []


def claim(cid, label, ev, text, **kw):
    C.append(dict(claim_id=cid, label=label, evidence_type=ev, claim=text,
                  review="self", review_note=NOTE, session="CT-S33-CHECKER-SCOPE",
                  **kw))


claim("S33-01", "PROVEN", "source_and_measurement",
      "check_invariants.py rooted at pathlib.Path(__file__).resolve()."
      "parents[1] = sessions/2026-09-17, reaching 30 of the 446 claims.jsonl "
      "files now declared, i.e. 6.7 per cent, while its module docstring said "
      "'Per-round invariant check over the whole session corpus'. Every "
      "'INVARIANTS OK' it printed before 2026-09-19 was a statement about "
      "sessions/2026-09-17 and about nothing else.",
      evidence="refs/check_invariants.pre-S33.py (sha256 4982602cc43153f9"
               "3263bfbc7cfa0254d5520cf76f4b80cfca542df8d0e1966c) contains "
               "both the parents[1] root and the docstring phrase; "
               "outputs/verify_checker.out.txt section D measures 30 vs 443.")

claim("S33-02", "STRUCTURAL", "design",
      "Remedy adopted, per the operator's ruling: an explicit module-level "
      "ROOTS list and an EXCLUDE mapping, both printed on every run, rather "
      "than re-pointing ROOT (which widens silently) or moving folders "
      "(which rewrites paths that claims already cite). Each EXCLUDE entry "
      "carries its reason in the value and the reason is printed.",
      evidence="sessions/2026-09-17/CT-R1-AUDIT/check_invariants.py, "
               "constants ROOTS and EXCLUDE; outputs/verify_checker.out.txt "
               "section B.")

claim("S33-03", "VERIFIED", "computation",
      "The widened pass reads 4069 claims in 443 contributing files across "
      "two roots (repository 4040, C:/LocalWork/SCOPE 29). Invariants 0, "
      "1(a), 3 and 4 PASS; invariants 1(b), 2 and 5 FAIL. Exit code 1.",
      evidence="outputs/widened_pass.out.txt; independently recounted by a "
               "second implementation in outputs/recount.out.txt, 9/9 "
               "controls, agreeing on input fingerprint 8223009e06eb6256.")

claim("S33-04", "VERIFIED", "computation",
      "Invariant 2 fails on 3488 claims: 3473 carry no label field at all, "
      "14 are labelled PROCEED and 1 REFINED. These are older sessions that "
      "predate the five-label convention. This is information about the "
      "older record; the invariant was not loosened to absorb it.",
      evidence="outputs/widened_pass.out.txt FAIL 2 and the label tally; "
               "outputs/recount.out.txt derives the same 3488 from the tally "
               "rather than from the failure list.")

claim("S33-05", "STRUCTURAL", "computation",
      "Invariant 1(b) fails on 84 reused claim_ids of two distinct kinds, "
      "which 1(b) does not distinguish: (i) per-session local counters, ids "
      "C1..C9 reused independently by six or more sessions, a naming "
      "convention rather than a collision of distinct claims; (ii) deposit "
      "mirrors, e.g. DELTA-FREDHOLM-ORDER/deposit/p0/claims.jsonl carrying "
      "the same nine DF-* ids as DELTA-FREDHOLM-P0/claims.jsonl. A mirror is "
      "not obviously a fault. Under the old narrow root neither kind was "
      "visible.",
      evidence="outputs/widened_pass.out.txt FAIL 1(b), first 20 entries.")

claim("S33-06", "VERIFIED", "computation",
      "2641 of the 4069 claims, 64.9 per cent, carry no claim_id at all and "
      "are therefore outside invariant 1(b) entirely. The checker now prints "
      "this count on its own line rather than collapsing those claims to a "
      "None key.",
      evidence="outputs/widened_pass.out.txt, the line following FAIL 1(b); "
               "outputs/recount.out.txt.")

claim("S33-07", "PROVEN", "computation",
      "The unparseable claims.jsonl lines are NOT truncations. 51 lines "
      "across 9 files resolve as: 5 files with a UTF-8 BOM ahead of valid "
      "JSON; 3 files that are whole valid JSON arrays in the wrong container "
      "(45 lines, 17 claims, all readable); and 1 genuinely damaged line. "
      "Exactly one claim in the corpus is unreadable. The append-path "
      "truncation hypothesis is not supported.",
      evidence="outputs/unparseable.out.txt, 6/6 controls including five "
               "synthetic probes that make each zero count interpretable.")

claim("S33-08", "VERIFIED", "computation",
      "The earlier count of 46 unparseable lines and the present 51 differ "
      "because the earlier reader opened files with encoding='utf-8-sig', "
      "which silently absorbs a BOM. The five BOM files were being repaired "
      "in the reading, not counted.",
      evidence="outputs/unparseable.out.txt: 5 files classified JSONL + BOM, "
               "46 + 5 = 51.")

claim("S33-09", "INSPECTED", "file_inspection",
      "The single damaged line is sessions/2026-04-30/SIARC-COHERENCE-AUDIT/"
      "claims.jsonl line 3, 350 bytes, 'Invalid \\\\escape: line 1 column "
      "249': raw LaTeX \\\\(2,2\\\\) inside a JSON string. Not repaired; "
      "reported for the operator.",
      evidence="outputs/unparseable.out.txt, DAMAGED LINES section.")

claim("S33-10", "INSPECTED", "self_audit",
      "Defect in my own first survey: it classified any line beginning '{' "
      "and not ending '}' as TRUNCATED and reported 15 truncations that do "
      "not exist. The offending files are pretty-printed JSON arrays. Caught "
      "by parsing each file as a whole BEFORE judging any line. This is the "
      "reader-invents-a-defect class; had it been acted on it would have "
      "prompted repair of 15 intact claims.",
      evidence="scripts/survey_unparseable.py, the docstring paragraph "
               "recording the superseded revision and the classify() "
               "contract that replaced it.")

claim("S33-11", "INSPECTED", "self_audit",
      "Second instance of the same class, in a control rather than a reader: "
      "a control asserted the phrase 'the whole session corpus' was absent "
      "from the new docstring and fired on the historical quotation that "
      "documents the old defect. A control that cannot distinguish an "
      "assertion from a quotation of it reports correct prose as wrong. "
      "Narrowed to 'exactly one occurrence, inside the quotation'.",
      evidence="scripts/verify_checker.py section A, third control, whose "
               "would-have-fired text records the superseded form.")

claim("S33-12", "VERIFIED", "file_inspection",
      "check_invariants.py was UNTRACKED by git (git status reported '??'), "
      "contrary to the working assumption that edits to it would be "
      "reviewable through git history. It was copied to refs/"
      "check_invariants.pre-S33.py, hash verified equal, before being "
      "overwritten.",
      evidence="git status --porcelain on the path; both copies hash "
               "4982602cc43153f93263bfbc7cfa0254d5520cf76f4b80cfca542df8d0e"
               "1966c at 4052 bytes.")

claim("S33-13", "VERIFIED", "computation",
      "C:/LocalWork/SCOPE is a live tree written by other processes during "
      "this session: CT-S30-PACKET-BUILD/claims.jsonl gained three claims "
      "between two runs minutes apart, moving the total from 4066 to 4069, "
      "which presented as a disagreement between two implementations that "
      "were in fact both correct. The checker and the recount now print a "
      "shared input fingerprint, the sha256 of the sorted path+content "
      "hashes, so that such a difference is attributed before it is called a "
      "disagreement.",
      evidence="outputs/recount.out.txt, the fingerprint control; "
               "outputs/widened_pass.out.txt, the 'input fingerprint' line.")

claim("S33-14", "STRUCTURAL", "file_inspection",
      "The session-number namespace is shared between the two roots and has "
      "collided. C:/LocalWork/SCOPE contains CT-S32-PACKET-SEALED and "
      "CT-S33-COLDREAD-OUTPUT while the repository contains "
      "CT-S32-LD2-ORDINARY-LOCUS and CT-S33-CHECKER-SCOPE. Nothing is "
      "overwritten, since the trees are disjoint, but a session cited by "
      "number alone is now ambiguous. Not resolved unilaterally.",
      evidence="directory listing of C:/LocalWork/SCOPE, 2026-09-19; no "
               "content of CT-S31-COLDREAD-ROWS was read.")

claim("S33-15", "INSPECTED", "file_inspection",
      "Three claims.jsonl files are zero bytes: sessions/2026-04-25/"
      "TRIAGE-UNSOLVED-3, sessions/2026-05-01/CHANNEL-THEORY-OUTLINE, "
      "sessions/2026-05-01/SIARC-MASTER-V0. They account exactly for the "
      "difference between 446 files walked and 443 files contributing a "
      "claim. Reported, not an invariant failure.",
      evidence="outputs/recount.out.txt; the checker prints them under the "
               "input fingerprint.")

claim("S33-16", "PROVEN", "source_and_measurement",
      "The predecessor called sys.exit(2) on the first JSONDecodeError and "
      "read with encoding='utf-8'. Under the widened roots its first error "
      "is therefore not the damaged line but a BOM: sessions/2026-04-22/"
      "H017-SIGN-A2-TRANS/claims.jsonl line 1, 'Unexpected UTF-8 BOM'. That "
      "path sorts ahead of every other offending file, so a naive widening "
      "would have aborted with exit 2 having checked no invariant at all. "
      "The rewrite reads utf-8-sig, reports the BOM under invariant 5, and "
      "collects parse failures instead of exiting on one.",
      evidence="refs/check_invariants.pre-S33.py, the read_text(encoding="
               "'utf-8') call and the except JSONDecodeError branch; the "
               "abort point was measured by replaying that exact logic over "
               "the widened file set, not inferred. An earlier draft of this "
               "claim named sessions/2026-04-30/SIARC-COHERENCE-AUDIT and "
               "was wrong: it reasoned from the damaged line and forgot that "
               "a BOM is also a parse error under plain utf-8.")

claim("S33-17", "VERIFIED", "computation",
      "20 of 20 controls on the rewritten checker pass, and they can fail: a "
      "clean synthetic corpus exits 0 with INVARIANTS OK, while nine "
      "separately injected defects (reused id, unrecognised label, review "
      "without note, unrecognised review value, PROVEN on file_inspection, "
      "BOM, JSON array, bad escape, unhonoured exclusion) each produce the "
      "corresponding named failure. The three real failures are therefore "
      "caused by the corpus, not by the checker.",
      evidence="outputs/verify_checker.out.txt, sections C and D; the real "
               "checker is asserted byte-identical after all controls.")

claim("S33-18", "STRUCTURAL", "design",
      "The stand-down is honoured as a printed hole rather than a silent "
      "one: C:/LocalWork/SCOPE/CT-S31-COLDREAD-ROWS is listed in EXCLUDE "
      "with its reason, pruned in os.walk's dirnames so it is never listed, "
      "and named on the checker's final 'holes in that verdict' line. "
      "Removing the entry when the packet is released is a one-line edit.",
      evidence="check_invariants.py find_claim_files(); "
               "outputs/verify_checker.out.txt, the EXCLUDE control.")

claim("S33-19", "INSPECTED", "self_audit",
      "A check that cannot fire is not a check. This emitter's first form "
      "asserted `\"\\r\" not in text`, which is unreachable: json.dumps "
      "escapes a carriage return inside every string, so a stray CR cannot "
      "reach the assembled text. Replaced by a validation of the exact bytes "
      "destined for disk, `b\"\\r\" not in blob`, followed by write_bytes, "
      "which removes newline translation from outside the validated object. "
      "Mutant arm M7 exercises the replacement and is caught pre-write with "
      "the artefact byte-identical; against the original form it could not "
      "have fired at all.",
      evidence="scripts/emit_claims.py, the comment block above `blob = "
               "text.encode`; outputs/mutants.out.txt arm M7.")

claim("S33-20", "INSPECTED", "self_audit",
      "Fourth instance this run of a control passing for the wrong reason: "
      "mutant arm M6 initially mutated the emitter into invalid Python, and "
      "the resulting SyntaxError traceback echoed the source line containing "
      "the arm's own reason string, so the substring test for 'refused for "
      "the injected reason' succeeded on a script that never ran. The arm "
      "now rejects any output containing SyntaxError or NameError as a "
      "mutation that broke the script rather than the claim set.",
      evidence="scripts/mutants.py, the broke_script guard; the superseded "
               "behaviour is recorded in the comment above it.")

# ----------------------------------------------- validate BEFORE writing ---
ids = [c["claim_id"] for c in C]
assert len(ids) == len(set(ids)), "duplicate claim_id in memory"
for c in C:
    assert c["label"] in LABELS, c["claim_id"]
    assert c["review"] == "self" and c["review_note"] == NOTE, c["claim_id"]
    assert not (c["label"] == "PROVEN"
                and c["evidence_type"] == "file_inspection"), c["claim_id"]
    assert c["claim"].strip() and c["evidence"].strip(), c["claim_id"]

text = "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in C)
for line in text.splitlines():
    json.loads(line)

# Validate the EXACT BYTES that are about to reach the disk, then write those
# bytes. Two earlier forms of this block were defective:
#   - `assert "\r" not in text` can never fire: json.dumps escapes CR inside
#     every string, so a stray CR cannot reach `text` in the first place. A
#     check that cannot fire is not a check.
#   - writing via write_text(newline=...) leaves the encoding and newline
#     translation outside the validated object, so the only protection was the
#     post-write read-back -- write-then-validate, the class this emitter
#     exists to avoid.
blob = text.encode("utf-8")
assert b"\r" not in blob, "carriage return in the bytes destined for disk"
digest = hashlib.sha256(blob).hexdigest()
assert len(digest) == 64 and all(ch in "0123456789abcdef" for ch in digest)

OUT.write_bytes(blob)
raw = OUT.read_bytes()
assert raw == blob
assert raw.decode("utf-8") == text
assert hashlib.sha256(raw).hexdigest() == digest
print("claims : %d" % len(C))
print("sha256 : %s" % digest)
print("bytes  : %d" % len(raw))
for lab in sorted(LABELS):
    n = sum(1 for c in C if c["label"] == lab)
    if n:
        print("  %-12s %d" % (lab, n))
