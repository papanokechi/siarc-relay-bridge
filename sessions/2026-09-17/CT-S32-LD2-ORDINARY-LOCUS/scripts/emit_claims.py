"""Emit and validate CT-S32 claims.jsonl.

P0 invariants enforced BEFORE anything is written to disk (the CT-S28 defect
6.3 lesson: an emitter that writes first and asserts second leaves a corrupted
file behind on every arm that "catches" a fault).

Enforced here: unique claim_id; exactly one recognised label; review present
and in {self, cold, lean}; review_note present and non-empty; script and
output_hash present; output_hash equal to the sha256 of the artefact ON DISK;
no PROVEN claim resting on file_inspection; every `supersedes` target named
explicitly in the claim text.
"""
import hashlib
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent.parent
ART = HERE / "outputs" / "locus.out.txt"
DEST = HERE / "claims.jsonl"

H = hashlib.sha256(ART.read_bytes()).hexdigest()
S = "scripts/locus.py"
NOTE = ("contaminated re-derivation; prior treatment of the same operator "
        "was in context")

C = []


def add(cid, task, label, ev, claim, script=S, oh=H, supersedes=None,
        reproducible=True):
    o = {"claim_id": cid, "task_id": task, "claim": claim, "label": label,
         "evidence_type": ev, "dps": None, "reproducible": reproducible,
         "script": script, "output_hash": oh,
         "review": "self", "review_note": NOTE}
    if supersedes:
        o["supersedes"] = supersedes
    C.append(o)


T = "CT-S32-LD2-ORDINARY-LOCUS"

add("S32-01", T + "/locus", "PROVEN", "symbolic_computation",
    "A SINGULAR POINT OF L_2 CAN DISAPPEAR. For L_2 = z b(theta+1) + z^2 "
    "a(theta+2) - 1 with b = beta_2 n^2 + beta_1 n + beta_0 (beta_2 != 0) and "
    "a = alpha_2 n^2 + alpha_1 n + alpha_0 (alpha_2 != 0), the point at "
    "infinity is an ORDINARY point -- not a singular point at all -- exactly "
    "on the locus a(1) = a(2) = 0 AND b(1) = 0. Exhibited at b = n^2 + n - 2, "
    "a = (n-1)(n-2): in the coordinate t = 1/z the operator after removing "
    "content is (1+t) Y'' - 2 Y' - Y, whose leading coefficient at t = 0 is 1 "
    "!= 0. The singular set is then S = {0, z*} with z* = -beta_2/alpha_2, of "
    "size 2 rather than 3. Control C2, 19/19 controls PASS.")

add("S32-02", T + "/locus", "PROVEN", "symbolic_computation",
    "THE RESULTING KATZ MULTISET MATCHES NO ROW OF TABLE 2.1. On the locus of "
    "S32-01 the Katz invariants are 1/2 at z = 0 (ramification 2) and 0 at z* "
    "(regular singular), i.e. the multiset (1/2, -, 0) in the van der Put - "
    "Saito tuple notation. None of the ten rows of Table 2.1 carries that "
    "multiset. This is not a contradiction: Table 2.1 lists the families whose "
    "Riemann-Hilbert fibres have dimension one, not every rank-two connection "
    "on P1, so an operator may perfectly well be a rank-two connection and "
    "appear in no row. Both Katz readings were taken by two differently "
    "implemented methods -- the Newton polygon of the Euler-operator "
    "coefficients, and the pole order of the normal-form potential r = p^2/4 + "
    "p'/2 - q -- which agree at every point (controls C-M, nine agreements).")

add("S32-03", T + "/locus", "PROVEN", "symbolic_computation",
    "BOTH CONDITIONS ARE NEEDED: THE LOCUS IS CODIMENSION 3. a(1) = a(2) = 0 "
    "alone does NOT drop the point at infinity. At b = 3n^2 + n + 1, "
    "a = (n-1)(n-2) the exponents at infinity are {0,1} but no holomorphic "
    "solution with c_0 = 1 exists: the t^0 equation is b(1) c_0 = 5 c_0 = 0, "
    "which forces c_0 = 0 whatever the remaining coefficients, so a logarithm "
    "is forced and infinity survives as a regular singular point, multiset "
    "(0, 0, 1/2), row D6~/PVdeg = PIII(D6). The obstructing coefficient IS "
    "b(1); it is precisely its vanishing that opens the locus. Control C4.")

add("S32-04", T + "/locus", "PROVEN", "symbolic_computation",
    "SUPERSEDES S28-10. 'THE ROW DEPENDS ONLY ON (alpha_2, alpha_1)' IS TRUE "
    "GENERICALLY AND FALSE ON THE LOCUS. S28-10 asserted that, given beta_2 != "
    "0, the Table 2.1 row reached by L_2 is a function of (alpha_2, alpha_1) "
    "alone -- equivalently of deg a alone -- and does not depend on beta_2, "
    "beta_1, beta_0, alpha_0 or a(2); it recorded this as STRICTER than the "
    "pre-registration, which had allowed dependence on the vanishing of a(2). "
    "The generic statement stands. The unrestricted statement does not: "
    "holding the numerator fixed at a = (n-1)(n-2), i.e. (alpha_2, alpha_1, "
    "alpha_0) = (1, -3, 2) unchanged, and moving beta_0 alone from -2 to -1 -- "
    "that is, b(1) from 0 to 1 -- moves the answer from NO ROW to "
    "D6~/PVdeg = PIII(D6). So b(1) = beta_2 + beta_1 + beta_0 does enter, "
    "through that locus alone. The corrected statement: off the codimension-3 "
    "locus a(1) = a(2) = 0 and b(1) = 0 the row is a function of (alpha_2, "
    "alpha_1); on it the operator is not classified by Table 2.1 at all. "
    "Control C6.",
    supersedes="S28-10")

add("S32-05", T + "/locus", "PROVEN", "symbolic_computation",
    "SUPERSEDES THE 'iff deg a = 2' DIRECTION OF S28-09. S28-09 stated that "
    "D6~/PVdeg = PIII(D6) is 'reached iff deg a = 2'. The forward direction "
    "fails: deg a = 2 does not imply the row is reached, because the locus of "
    "S32-01 has deg a = 2 and reaches no row. The rest of S28-09 is "
    "unaffected: exactly three rows are reachable, and the seven exclusions "
    "stand, since they rest on Katz(0) = 1/2 and Katz(infinity) <= 1, neither "
    "of which the locus disturbs -- z = 0 keeps Katz 1/2 there (control C2). "
    "The correct form is 'reached if deg a = 2 and not (a(1) = a(2) = b(1) = "
    "0)'.",
    supersedes="S28-09")

add("S32-06", T + "/defect", "VERIFIED", "symbolic_computation",
    "THE DEFECT THAT HID IT: A CRITERION STATED BUT NOT IMPLEMENTED. The "
    "ordinary-point predicate used while first investigating this question "
    "tested only whether a holomorphic solution with c_0 = 1 exists. It did "
    "NOT require the exponents to be {0,1} -- a requirement written in the "
    "predicate's own docstring and in the surrounding prose, and simply never "
    "coded. The consequence is exhibited exactly: at b = 3n^2 + n + 1, "
    "a = (n-1)(n-2) the point z* = -3 has exponents {0, 7/3}; a holomorphic "
    "solution with c_0 = 1 does exist (the exponent-0 one), so the defective "
    "predicate calls z* ORDINARY and discards it, returning S = {0, infinity} "
    "and no row -- the right verdict class for the wrong point and the wrong "
    "reason. The correct predicate keeps z* (control C4). Running the study "
    "under both predicates side by side changes the answer, so the requirement "
    "is not decorative: control C5, which would have fired had the two "
    "predicates agreed.")

add("S32-07", T + "/defect", "STRUCTURAL", "symbolic_computation",
    "WHY {0,1} IS THE RIGHT CRITERION. A regular singular point of a "
    "second-order operator is an ordinary point exactly when its exponents are "
    "{0,1} AND no logarithm is forced. For exponents {0, m} with m >= 2 the "
    "Wronskian of the two solutions behaves as w^(m-1) and vanishes at w = 0, "
    "so two holomorphic solutions do not form a basis and the point survives; "
    "for non-integer m the second solution is not holomorphic at all. "
    "Existence of one holomorphic solution is therefore necessary and not "
    "sufficient, which is exactly the gap the defect of S32-06 fell into. "
    "Labelled STRUCTURAL: this is the standard criterion, restated here "
    "because the defect consisted in not enforcing it.")

add("S32-08", T + "/controls", "VERIFIED", "symbolic_computation",
    "CONTROL REPORT: 19 of 19 PASS, and the discriminating arms could all have "
    "fired. C1 generic deg a = 2 gives three singular points and the row "
    "PVdeg=PIII(D6) (would have fired on any other row). C2 on the locus "
    "infinity is ordinary, #S = 2, no row (would have fired had infinity "
    "stayed singular, or had the two-point multiset matched some row). C3 the "
    "sharp arm: moving beta_0 by 1, so b(1): 0 -> 1, restores infinity and the "
    "row (would have fired had the classifier been blind to b(1), in which "
    "case C2 would have been uninterpretable). C4 a(1) = a(2) = 0 alone does "
    "not drop infinity (would have fired had the locus been codimension 2). "
    "C5 the defective predicate changes the answer (would have fired had the "
    "two predicates agreed, showing the defect harmless). C6 with (alpha_2, "
    "alpha_1) held fixed, beta_0 alone moves the answer (would have fired had "
    "the multiset been unchanged, leaving S28-10 intact). Nine C-M arms compare "
    "the Newton-polygon and normal-form-potential readings at every point of "
    "every case (would have fired on any disagreement). The artefact is read "
    "back from disk, CRLF is asserted absent, and a known-present non-ASCII "
    "sentinel is asserted present AND asserted destroyed by a latin-1 read "
    "before any absence is evaluated.")

add("S32-09", T + "/coverage", "INSPECTED", "file_inspection",
    "check_invariants.py DOES NOT REACH C:/LocalWork/SCOPE, AND REACHES LESS "
    "OF THIS REPOSITORY THAN ITS DOCSTRING CLAIMS. The checker at "
    "sessions/2026-09-17/CT-R1-AUDIT/check_invariants.py sets ROOT = "
    "pathlib.Path(__file__).resolve().parents[1], which is "
    "sessions/2026-09-17, and then rglobs claims.jsonl beneath it. Two "
    "consequences, both measured today. (i) C:/LocalWork/SCOPE is outside this "
    "repository entirely and is not reached, confirming S30-08; the CT-S28, "
    "CT-S29 and CT-S31 claim material there is outside the corpus checker. "
    "(ii) The docstring says 'over the whole session corpus', but the "
    "repository holds 443 claims.jsonl files of which only 29 lie under "
    "sessions/2026-09-17; 414 are never examined. The checker reports 'corpus: "
    "540 claims in 29 files', and that count is the honest measure of what it "
    "covers. No files were moved to change this; see S32-10.",
    script="(none -- direct inspection of check_invariants.py)",
    reproducible=False)

add("S32-10", T + "/coverage", "STRUCTURAL", "file_inspection",
    "WHAT IT WOULD TAKE, AND WHY IT WAS NOT DONE UNILATERALLY. Three options, "
    "in increasing order of disturbance. (1) Re-point ROOT: change parents[1] "
    "to the repository root so the checker sees all 443 claims files. Cost: "
    "414 previously unchecked files enter the invariant set at once and any "
    "legacy violation becomes a hard failure of every future round; it must be "
    "a deliberate, staged decision, not a side effect. (2) Give the checker an "
    "explicit roots list, including C:/LocalWork/SCOPE, so out-of-tree session "
    "folders are checked in place without being moved. Cost: the corpus "
    "acquires a dependency on an absolute path outside version control, and "
    "'the corpus' stops being 'what is in the repository'. (3) Move the SCOPE "
    "session folders into sessions/ so they are reached by construction. Cost: "
    "this is a provenance-bearing relocation of deposited-adjacent records and "
    "at least one of those folders -- CT-S31-COLDREAD-ROWS -- is an input "
    "packet being assembled for a different, uncontaminated process, from "
    "which this session has been stood down. Moving files to satisfy a checker "
    "is exactly the unilateral act that was ruled out, so nothing was moved "
    "and no path was rewritten. The decision is left to the operator. This "
    "session was placed under sessions/2026-09-17/ so that its own claims are "
    "reached by the existing checker with no change to it at all.",
    script="(none -- design note)",
    reproducible=False)

add("S32-11", T + "/scope", "STRUCTURAL", "symbolic_computation",
    "SCOPE LIMIT, BINDING, AND A CONTAMINATION DISCLOSURE. (i) A matching Katz "
    "multiset is NECESSARY, NOT SUFFICIENT: nothing in S32-01..S32-05 asserts "
    "that any specialisation of L_2 IS a member of any van der Put - Saito "
    "family, and no membership, isomonodromy or surface-type claim is made. "
    "(ii) Conversely, and this is the content of S32-02, failure to match is "
    "not a pathology: Table 2.1 is not a classification of all rank-two "
    "connections. (iii) Every claim in this session is labelled review 'self' "
    "with the note 'contaminated re-derivation; prior treatment of the same "
    "operator was in context'. The computation in scripts/locus.py was written "
    "and run in this repository from the operator's definition and reproduces "
    "the finding independently, but the earlier treatment of the same operator "
    "was in context throughout, so no arm of this session is a cold read and "
    "none should be counted as independent confirmation of the earlier work.")

add("S32-12", T + "/emitter", "VERIFIED", "symbolic_computation",
    "THE EMITTER'S OWN VALIDATION WAS TESTED, AND ONE ARM CAUGHT A REAL "
    "DEFECT IN IT. scripts/mutants.py injects seven faults into "
    "scripts/emit_claims.py one at a time -- duplicate claim_id, unrecognised "
    "label, empty review_note, a PROVEN claim resting on file_inspection, a "
    "`supersedes` target not named in the claim text, an output_hash that is "
    "not the sha256 of the artefact on disk, and a review value outside "
    "self|cold|lean -- and requires of each arm THREE things: the emitter "
    "refuses, it refuses for the injected reason, and claims.jsonl on disk is "
    "byte-identical afterwards. On the first run arm M6 reported MISSED on the "
    "third of those: the emitter refused, but only in its post-write read-back "
    "section, so the bad output_hash had already reached disk. That is the "
    "same class as CT-S28 defect 6.3. Repaired by moving the artefact-hash "
    "assertion into the pre-write validation block; all seven arms then "
    "reported CAUGHT with claims.jsonl byte-identical throughout, and a clean "
    "re-run reproduces the file byte-for-byte. Every anchor string is asserted "
    "present before its arm runs, so no arm can pass vacuously by failing to "
    "apply.",
    script="scripts/mutants.py")

# ----------------------------------------------- VALIDATE, THEN write ------
LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}
REVIEWS = {"self", "cold", "lean"}

ids = [c["claim_id"] for c in C]
assert len(ids) == len(set(ids)), "duplicate claim_id within this session"
assert H == hashlib.sha256(ART.read_bytes()).hexdigest(), \
    "artefact changed under the emitter"
for c in C:
    cid = c["claim_id"]
    assert c["label"] in LABELS, (cid, c["label"])
    assert c["review"] in REVIEWS, cid
    assert c["review_note"] and c["review_note"].strip(), cid
    assert c["script"] and c["output_hash"], cid
    assert not (c["label"] == "PROVEN"
                and c["evidence_type"] == "file_inspection"), cid
    if "supersedes" in c:
        assert c["supersedes"] in c["claim"], \
            "%s: supersedes target not named in the claim text" % cid

# no collision with the rest of the corpus
repo = pathlib.Path(__file__).resolve().parents[4]
other = set()
unparsed = 0
for p in repo.rglob("claims.jsonl"):
    if p.resolve() == DEST.resolve():
        continue
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            other.add(json.loads(line).get("claim_id"))
        except json.JSONDecodeError:
            unparsed += 1
clash = sorted(set(ids) & other)
assert not clash, "claim_id collision with the corpus: %s" % clash

payload = "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in C)
assert payload.count("\n") == len(C)

DEST.write_text(payload, encoding="utf-8", newline="")

# ----------------------------------------------------------- read back -----
raw = DEST.read_bytes()
assert b"\r\n" not in raw, "CRLF leaked into claims.jsonl"
back = [json.loads(l) for l in raw.decode("utf-8").splitlines() if l.strip()]
assert len(back) == len(C), "read-back count differs from what was written"
assert back == C, "read-back content differs from what was written"
assert all(c["output_hash"] == H for c in back if c["script"] == S)
assert H == hashlib.sha256(ART.read_bytes()).hexdigest(), \
    "artefact changed under the emitter"

print("claims: %d" % len(back))
print("artefact %s sha256 %s" % (ART.name, H))
print("claims.jsonl sha256 %s bytes %d"
      % (hashlib.sha256(raw).hexdigest(), len(raw)))
print("labels: " + "  ".join(
    "%s=%d" % (k, sum(1 for c in back if c["label"] == k))
    for k in sorted({c["label"] for c in back})))
print("supersedes: " + ", ".join(
    "%s->%s" % (c["claim_id"], c["supersedes"]) for c in back
    if "supersedes" in c))
print("checked %d claim_ids elsewhere in the corpus for collision "
      "(%d line(s) unparseable)" % (len(other), unparsed))
