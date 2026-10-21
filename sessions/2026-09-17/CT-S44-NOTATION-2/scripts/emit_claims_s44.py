"""Emit CT-S44's claims, validating the buffer BEFORE writing it.

Every check below runs against the in-memory list.  A post-write assertion
still leaves a corrupt artefact on disk (S28-14, S32-12), so the file is not
opened until the buffer has passed.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / "claims.jsonl"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"}

# numbers that appear in prose for reasons the evidence file need not contain
WHITELIST = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
             "0", "44", "38", "43", "23"}

C = []


def add(cid, task, claim, label, ev_type, script, output, dps=None,
        supersedes=None, also=None):
    rec = {
        "claim_id": cid,
        "task_id": task,
        "claim": claim,
        "label": label,
        "evidence_type": ev_type,
        "dps": dps,
        "reproducible": True,
        "script": script,
        "output_file": output,
    }
    # A claim whose numbers span several runs must cite them all.  Widening
    # the whitelist instead would have hidden the mismatch this check found.
    if also:
        rec["also_output_file"] = list(also) if isinstance(also, (list, tuple)) \
            else [also]
    if supersedes:
        rec["supersedes"] = supersedes
    C.append(rec)


S = "scripts/"
O = "outputs/"
DIFF = O + "rendered_diff.out.txt"
ARMS = O + "rendered_diff_arms.out.txt"
CENS = O + "symbol_census.out.txt"
CENSP = O + "symbol_census_prepass.out.txt"
CENSM = O + "mutants_census.out.txt"
ASM = O + "check_assembly.out.txt"
MUT = O + "mutants_assembly.out.txt"

add("S44-01", "CT-S44-NOTATION-2",
    "The unsubscripted rho of the deposited record -- the exponent of the "
    "leading Borel-plane singularity, an indicial exponent in the uniformiser "
    "u = sqrt z -- has been removed from section 1 as a symbol of this paper. "
    "It is named only in the correspondence footnote, as the deposited "
    "convention, because the paper states no result about it and its relation "
    "to the growth exponent s was anchored only at d = 2.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-02", "CT-S44-NOTATION-2",
    "Section 1's sentence stating that rho carries two meanings was false "
    "about the paper. rho occurs in three senses, none of which is the "
    "Borel-plane exponent that sentence called its primary meaning: rho_j for "
    "the characteristic roots of the homogeneous recurrence in section 2, rho "
    "as the growth base in the normal-solution form in section 2, and rho_pm "
    "for the finite singular points of System B in section 3. The sentence had "
    "already been repaired once, at CT-S38, from a stronger false claim; the "
    "repair replaced it with a weaker false claim.",
    "VERIFIED", "computation", S + "symbol_census.py", CENS)

add("S44-03", "CT-S44-NOTATION-2",
    "Section 7 used rho as an undefined step-size scale, writing the error bar "
    "as obtained from step halving at h = rho/4 against h = rho/8. No "
    "definition of that rho exists anywhere in the paper or in the cited "
    "claim. It was removed in favour of the step counts the claim does "
    "record, so that the sentence asserts only what its evidence supports; no "
    "value was invented to fill the gap.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-04", "CT-S44-NOTATION-2",
    "Section 2's Newton--Puiseux diagram has been unified to Newton polygon, "
    "the name section 1 defines and the name used by van der Put--Saito and "
    "the Katz-invariant literature. The paper previously defined one name and "
    "used another, which no citation check and no build can detect.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-05", "CT-S44-NOTATION-2",
    "Section 3's normal potential, written R = 1/4 a^2 + 1/2 a' - b, has been "
    "unified to the general form R = 1/4 P^2 + 1/2 P' - Q already stated in "
    "section 1, with section 3's case recorded as the specialisation (P, Q) = "
    "(a, b). The two were the same construction at different specialisations, "
    "so the repair unifies rather than separates them.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-06", "CT-S44-NOTATION-2",
    "The ruled separation of P as a determinant from P as the first-order "
    "coefficient of a scalar operator required no edit: the paper nowhere "
    "writes a bare P for the determinant a^2 + bc. Section 8 already writes "
    "-det A and names it. Every bare P in the 13 assembled files is the "
    "scalar operator's coefficient, a quotation, or a subscripted variant. "
    "The item is discharged by verification, not by repair.",
    "VERIFIED", "computation", S + "symbol_census.py", CENS)

add("S44-07", "CT-S44-NOTATION-2",
    "The moduli space was written three ways -- upright M with subscript in "
    "section 0, bare calligraphic M in section 9, and calligraphic M with "
    "subscript in the appendix A passage quoted verbatim from van der "
    "Put--Saito. The quoted form is the source's own and is authoritative, so "
    "sections 0 and 9 were unified to it. The section 0 change has no "
    "rendered-text signature, since pdftotext maps both glyphs to M; the "
    "section 9 change does, and the gate caught the author's initial "
    "misdeclaration of both as invisible.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-08", "CT-S44-NOTATION-2",
    "Section 5 reintroduced r_1, in a fifth sense -- the coefficient of 1/x in "
    "the expansion of the normal potential -- after section 1's correspondence "
    "footnote names the deposited record's r_1 as ambiguous and the roots were "
    "renamed to nu_i precisely to retire it. The symbol was retired by writing "
    "its value inline. The displayed consequence is unchanged and was checked "
    "arithmetically: with c_0^2 = 1/3 the display reads -1 -+ sqrt3/18 before "
    "and after.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-09", "CT-S44-NOTATION-2",
    "Section 5 used a bare A for the scalar residue of a Riccati solution, "
    "while a bare A denotes a two-by-two matrix everywhere else in the paper, "
    "including nineteen lines later in the same section. It was renamed to "
    "kappa, which the census confirms was unused. This is the only residue "
    "item resolved by renaming rather than by stating a convention.",
    "INSPECTED", "file_inspection", S + "symbol_census.py", CENS)

add("S44-10", "CT-S44-NOTATION-2",
    "Section 1 gains a paragraph stating the convention for each of the six "
    "deferred letters M, A, L, u, beta and r, each with its discriminator -- "
    "font, subscript, or locality to one computation -- following section 1's "
    "own precedent of resolving a collision by stating the convention where "
    "the objects are already distinguishable.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)

add("S44-11", "CT-S44-NOTATION-2",
    "The deferred residue was re-measured against the assembled paper rather "
    "than inherited from CT-S38, whose symbol index was built over theorem.tex "
    "and section 1 alone, before sections 2 to 10 and the appendices existed. "
    "Over the pre-pass corpus -- 13 files, 138537 characters -- the census "
    "returns 185 occurrences of the six letters across 6 letters, of which 61 "
    "are A. Restricting to math spans is what makes that number mean "
    "anything: unrestricted, the reader counts the English article, a defect "
    "caught by the mask's negative control before any figure was reported.",
    "VERIFIED", "computation", S + "symbol_census.py", CENSP)

add("S44-12", "CT-S44-NOTATION-2",
    "The rendered-text gate compares the token SEQUENCE of the pre-pass and "
    "post-pass documents, not the whitespace-stripped character multiset used "
    "at CT-S38, which is anagram-blind and cannot distinguish a rename from "
    "its reverse. It passes with 20 differing regions, every one accounted "
    "for, and all 8 control arms CAUGHT -- including the arm that transposes "
    "two symbols into an anagram of the same characters.",
    "VERIFIED", "computation", S + "rendered_diff.py", ARMS, None, None, DIFF)

add("S44-13", "CT-S44-NOTATION-2",
    "The repaired paper builds at 39 pages with 0 errors, 0 undefined "
    "references and 0 multiply-defined labels, converged over four passes. "
    "The assembly gate passes over the repaired files at 13 sections, 124 "
    "labels and 76 referenced targets, and its 7 mutant arms are all CAUGHT. "
    "The gate was repointed from the pre-pass copies before it was run; left "
    "as staged it would have certified the unrepaired document.",
    "VERIFIED", "build", S + "check_assembly.py", ASM, None, None,
    (MUT, "paper.log"))

add("S44-14", "CT-S44-NOTATION-2",
    "CT-S43's recorded page count of 37 is not reproducible from CT-S43's own "
    "inputs. Rebuilding that session's exact layout, jobname and files -- "
    "verified byte-identical, preamble included -- converges at 38 pages over "
    "three passes. CT-S43's paper.log therefore records a build of an earlier "
    "state of the files than the ones it shipped, and the gate did not see it "
    "because it read the log rather than rebuilding. No file of CT-S43 is "
    "altered; this claim supersedes the page count only.",
    "VERIFIED", "build", S + "rendered_diff.py", O + "scratch_s43/paper.log",
    None, "S43-07")

add("S44-15", "CT-S44-NOTATION-2",
    "The gate's declaration of intended changes was completed iteratively "
    "against the diff it certifies, so it is not a blind pre-registration and "
    "its authority rests on its control arms rather than on the declaration. "
    "Two declarations were found wrong by the gate itself: the moduli-space "
    "repair was declared invisible when half of it is visible, and section 5's "
    "numeric delta was declared without being computed and was simply wrong. "
    "Both were corrected against the measurement, not the expectation.",
    "INSPECTED", "file_inspection", S + "rendered_diff.py", DIFF)


add("S44-16", "CT-S44-NOTATION-2",
    "This session's first symbol census was run mid-pass, against a tree that "
    "some repairs had already reached and others had not. It reported figures "
    "that match neither the pre-pass corpus nor the repaired one, and that "
    "state no longer exists, so the measurement is not reproducible. The "
    "defect was invisible while the census defaulted to the session root: it "
    "surfaced only when the script was re-run and its own output changed "
    "underneath a claim that quoted it. The census now names its corpus "
    "explicitly, prepass or repaired, and resolves it POSITIVELY by a marker "
    "each tree carries and the other does not -- refs/section1.tex must still "
    "carry the pre-repair rho sentence, and the session root must carry the "
    "repaired conventions paragraph -- so that a census cannot report a number "
    "for a corpus nobody asked about. Three control arms, including a negative "
    "arm in which a semantically neutral edit must NOT fire the guard, all "
    "CAUGHT.",
    "VERIFIED", "computation", S + "mutants_census.py", CENSM)

add("S44-17", "CT-S44-NOTATION-2",
    "The emitter's own numeric check is weaker than it appears, and this is "
    "recorded as a limit rather than repaired. It confirms a number by "
    "searching the cited evidence file for the digit string anywhere in the "
    "file, so a line number, a context quotation or an unrelated figure "
    "satisfies it. The superseded text of S44-11 cited a count for the letter "
    "A that the check accepted solely because the same digits occur as a line "
    "number in the census listing -- the check passed for the wrong reason, on "
    "a figure that was in fact unreproducible. The general form is the one "
    "already recorded for textual proximity: presence of a numeral in a file "
    "does not establish that the file evidences that quantity. A sound version "
    "would resolve each figure to the summary line that reports it.",
    "INSPECTED", "file_inspection", S + "emit_claims_s44.py", CENSP)


# --------------------------------------------------------------------------
# Pre-write validation.  Nothing below opens the output file.
# --------------------------------------------------------------------------
def fail(msg):
    print("REFUSING TO WRITE: %s" % msg)
    sys.exit(1)


checks = 0
ID_TOKEN = re.compile(r"\bS[0-9]+[A-Z]*-[0-9A-Za-z-]+")
NUM = re.compile(r"\d+")

seen = set()
for r in C:
    cid = r["claim_id"]
    checks += 1
    if cid in seen:
        fail("duplicate claim id %s" % cid)
    seen.add(cid)

    checks += 1
    if r["label"] not in LABELS:
        fail("%s: label %r is not one of the five" % (cid, r["label"]))

    checks += 1
    if len(r["claim"]) < 80:
        fail("%s: claim text is too short to carry evidence" % cid)

    checks += 1
    if not r["claim"].endswith("."):
        fail("%s: claim text is not a complete sentence" % cid)

    # the evidence file must exist and be non-empty
    checks += 1
    p = HERE / r["output_file"]
    if not p.exists():
        fail("%s: evidence file %s does not exist" % (cid, r["output_file"]))
    checks += 1
    if p.stat().st_size == 0:
        fail("%s: evidence file %s is empty" % (cid, r["output_file"]))

    checks += 1
    sp = HERE / r["script"]
    if not sp.exists():
        fail("%s: script %s does not exist" % (cid, r["script"]))

    # every number the claim reports must appear in its own evidence file,
    # with claim-id tokens stripped first so that S44-15 cannot contribute a
    # spurious 15
    body = p.read_text(encoding="utf-8", errors="replace")
    if r.get("also_output_file"):
        for extra in r["also_output_file"]:
            ap = HERE / extra
            checks += 1
            if not ap.exists() or ap.stat().st_size == 0:
                fail("%s: second evidence file %s missing or empty"
                     % (cid, extra))
            body += ap.read_text(encoding="utf-8", errors="replace")
    text = ID_TOKEN.sub(" ", r["claim"])
    for n in NUM.findall(text):
        if n in WHITELIST:
            continue
        checks += 1
        if n not in body:
            fail("%s: reports %s, which does not appear in %s"
                 % (cid, n, r["output_file"]))

# the emitter must not be able to pass by having nothing to check
if len(C) < 10:
    fail("only %d claims staged; that is not this session's output" % len(C))
if checks < 100:
    fail("only %d pre-write checks ran" % checks)

# a claim that supersedes must name a real, differently-numbered claim
for r in C:
    if "supersedes" in r:
        checks += 1
        if not re.fullmatch(r"S[0-9]+[A-Z]*-[0-9]+", r["supersedes"]):
            fail("%s: malformed supersedes %r" % (r["claim_id"],
                                                  r["supersedes"]))
        if r["supersedes"].startswith("S44-"):
            fail("%s: supersedes a claim of its own session" % r["claim_id"])

buf = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in C)

# the buffer must parse back to exactly what was staged
checks += 1
back = [json.loads(ln) for ln in buf.strip().split("\n")]
if back != C:
    fail("buffer does not round-trip to the staged records")

digest = hashlib.sha256(buf.encode("utf-8")).hexdigest()
OUT.write_text(buf, encoding="utf-8", newline="\n")

# read-back, after the buffer was already proved good
if hashlib.sha256(OUT.read_bytes()).hexdigest() != digest:
    fail("written file does not match the validated buffer")

print("%d claims, %d pre-write checks, sha256 %s"
      % (len(C), checks, digest))
for r in C:
    print("  %-8s %-12s %s" % (r["claim_id"], r["label"],
                               r["claim"][:64].replace("\n", " ")))
