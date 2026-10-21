"""Emit claims.jsonl for CT-S46-FORMULA-SECTIONS.

Two rules are enforced before anything is written:

1. THE ANCHORED-FIGURE RULE (the operator's standing rule, from S44-17).
   A numeral appearing anywhere in an evidence file does not evidence the
   quantity a claim is about -- in CT-S44 the figure 128 matched a LINE
   NUMBER. So every cited figure must resolve to a line of its evidence file
   that ALSO carries a named anchor for that figure.

2. BYTE-EXACT WRITE (from CT-S45).
   Path.write_text applies platform newline translation AFTER the buffer has
   been validated, so a post-write assertion finds the corruption only once it
   is already on disk. The ENCODED BYTES are validated pre-write and written
   with write_bytes.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "outputs"
ART = HERE / "claims.jsonl"

CENS = "outputs/display_census.out.txt"
RTS = "outputs/route_s_sections.out.txt"
ARMS = "outputs/mutants_route_s_sections.out.txt"
MAN = "outputs/manifest.out.txt"
RTP = "outputs/route_p.out.txt"

# claim_id, label, claim, evidence_type, script, evidence file,
# figures = ((number, evidence file, anchor that must share the line), ...)
CLAIMS = [
    ("S46-01", "INSPECTED",
     "Sections 0-10 of the paper contain 56 displayed formulas, extracted by "
     "a reader that rejects inline math, rejects LaTeX line-break spacing, "
     "and fails if fewer than 10 displays are found.",
     "file_inspection", "scripts/display_census.py", CENS,
     ((56, CENS, "ALL"),)),

    ("S46-02", "VERIFIED",
     "The display extractor initially matched LaTeX line-break spacing "
     "\\\\[2pt] as a \\[..\\] display. The defect BOTH invented a display "
     "(section6.tex L69) AND hid a real one (section6.tex L92, the "
     "factorisation 3x^2+x+1=3 delta^2 z(z-1)), leaving section 6's total at "
     "6 either way: no count-based check could have detected it. Repaired "
     "with a negative lookbehind and locked by a negative control arm.",
     "computation", "scripts/display_census.py", CENS, ()),

    ("S46-03", "VERIFIED",
     "Route S: 38 symbolic checks over the displays of sections 0-10, every "
     "one an exact rational-function identity with residual 0 under "
     "sympy.simplify. No check is a comparison of an expression with itself.",
     "computation", "scripts/route_s_sections.py", RTS,
     ((38, RTS, "checked displays match"),)),

    ("S46-04", "VERIFIED",
     "eq:QC, the display the operator named as the transposed-digit risk, is "
     "correct as printed: transporting System C by x = s_+ + delta z gives "
     "Q(z) = (22z^2-22z-2i sqrt11 z+5+i sqrt11)/(54 z(z-1)). PREREG falsifier "
     "F5 predicted this MATCH by hand expansion BEFORE the script was "
     "written, so the agreement is informative and not merely a check that "
     "could only pass.",
     "computation", "scripts/route_s_sections.py", RTS, ()),

    ("S46-05", "VERIFIED",
     "eq:rA is the projective normal potential of eq:sysA's homogeneous part: "
     "R = P^2/4 + P'/2 - Q with P = 10/(3z), Q = (z^2+5z-1)/(3z^3) expands "
     "exactly to (-3z^2-5z+3)/(9z^3).",
     "computation", "scripts/route_s_sections.py", RTS, ()),

    ("S46-06", "VERIFIED",
     "eq:rB is routable in-session after all, although System B's ODE is "
     "never displayed in the paper: z = 1/x is Mobius, so its Schwarzian "
     "vanishes, and r_B(1/x)/x^4 equals eq:rC exactly. This is the paper's "
     "own stated claim that B and C share a normal potential, re-derived "
     "rather than cited.",
     "computation", "scripts/route_s_sections.py", RTS, ()),

    ("S46-07", "VERIFIED",
     "Section 5's located constants follow from eq:rC by transport: the "
     "potential at infinity is -11/27 + (i sqrt11/27)/z, giving t = -+2i "
     "sqrt33/9 from t^2/4 = R(inf); both finite poles are double with "
     "coefficient -1/4; the 1/x coefficient of r_C is -1/9 and c_0^2 = 1/3, "
     "giving n = -1 -+ sqrt3/18. Nine checks, all residual 0.",
     "computation", "scripts/route_s_sections.py", RTS, ()),

    ("S46-08", "VERIFIED",
     "Seven restatement checks confirm that quantities displayed more than "
     "once agree mathematically, including eq:PC/eq:QC reprinted in section 9 "
     "under different markup, which the TEXTUAL near-duplicate check cannot "
     "see. This is the generalisation of CT-S45's Appendix A defect, where "
     "two displays of one quantity four lines apart disagreed.",
     "computation", "scripts/route_s_sections.py", RTS, ()),

    ("S46-09", "VERIFIED",
     "Control arms for route S: 14 of 14 behaved as expected. Eight mutate a "
     "printed paper value (including two digit transpositions and one sign "
     "flip, the CT-S45 defect class), three attack the reader and must make "
     "it refuse, two alter section 9's reprint of eq:PC/eq:QC, and one is a "
     "neutral edit that must NOT fire. A crash never scores as a detection.",
     "build", "scripts/mutants_route_s_sections.py", ARMS,
     ((14, ARMS, "ARMS:"),)),

    ("S46-10", "VERIFIED",
     "Route S's refusals originally exited 1, the same code as 'a display "
     "DIFFERS', so a broken instrument and a real finding were "
     "indistinguishable to any caller. Three halt arms reported MISSED and "
     "exposed it. Refusals now exit 2.",
     "build", "scripts/mutants_route_s_sections.py", ARMS, ()),

    ("S46-11", "INSPECTED",
     "The routing manifest covers all 56 census displays with no display "
     "unrouted and no stale entry: 21 route S-here, 15 route S-corpus, 9 "
     "route P, 11 definitional. Coverage is asserted against the census, so a "
     "display added or moved fails the manifest rather than drifting.",
     "file_inspection", "scripts/manifest.py", MAN,
     ((56, MAN, "census="), (21, MAN, "S-here"), (15, MAN, "S-corpus"),
      (9, MAN, "route P"), (11, MAN, "DEF"), (0, MAN, "unrouted="))),

    ("S46-12", "VERIFIED",
     "Every claim id cited by the manifest as a route-S-corpus source "
     "resolves to a claim_id present in the corpus, checked against 1493 ids "
     "read from sessions/*/claims.jsonl with S16-07 as a positive control so "
     "that 'absent' cannot silently mean 'my reader could not see it'. The "
     "walk excludes this session's own claims.jsonl (the CT-S41 precedent), "
     "without which emitting these claims changes the census they cite. That "
     "closes the trap within the session only: a later session's claims.jsonl "
     "will still move the figure, so no cross-session reproducibility is "
     "asserted for it.",
     "file_inspection", "scripts/manifest.py", MAN,
     ((1493, MAN, "corpus_claim_ids="),)),

    ("S46-19", "VERIFIED",
     "The corpus-id census first moved between two runs of the same gate, "
     "because the walk included this session's own claims.jsonl and emission "
     "had added 17 ids to it. The emitter refused rather than writing a "
     "figure that no longer resolved. This is the third distinct defect this "
     "session that was surfaced by a check re-reading its evidence instead "
     "of trusting an exit code.",
     "file_inspection", "scripts/manifest.py", MAN, ()),

    ("S46-13", "INSPECTED",
     "Route P: the nine transcribed displays agree with their sources, each "
     "folio read off the page image and not taken from the filename. Journal "
     "p.2655 confirms family (4.1) a, b, c and the chart; p.2656 confirms "
     "Omega, (4.4) and (4.5) H_V; p.2635 Table 2.1 confirms both Dynkin rows "
     "and the column order r(0),r(1),r(inf),r(t); Jimbo p.1152 confirms all "
     "four Painleve V parameters.",
     "file_inspection", "scripts/route_p.py", RTP, ()),

    ("S46-14", "VERIFIED",
     "The page image held in the tree as jimbo_p1152.png carries the printed "
     "folio 1153 and does not contain the (alpha,beta,gamma,delta) "
     "dictionary that section 4 cites to p.1152. The correct page is held "
     "separately as jimbo_printed1152.png. Trusting the filename would have "
     "reported eq:jimbo unverifiable; reading the folio found the right "
     "file. This is a defect in the tree, not in the paper.",
     "file_inspection", "scripts/route_p.py", RTP, ()),

    ("S46-15", "VERIFIED",
     "DLMF 2.9.6 as printed in section 2, alpha_j = (f1 rho_j+g1)/(f0 "
     "rho_j+2 g0), matches the held DLMF source text after normalising away "
     "invisible multiplication characters, with DLMF 2.9.5 as a positive "
     "control and a one-digit corruption as a negative control.",
     "computation", "scripts/route_p.py", RTP, ()),

    ("S46-16", "INSPECTED",
     "This session modified no file of the paper: all 15 .tex sources copied "
     "into refs/ are byte-identical to the CT-S45-FORMULA-A assembly they "
     "were taken from. Sections 0-10 required no formula repair; the only "
     "repairs made in the formula pass remain Appendix A's, in CT-S45.",
     "file_inspection", "scripts/manifest.py", MAN, ()),

    ("S46-17", "VERIFIED",
     "The control harness for route S originally ran each mutant with the "
     "session root as its working directory, so every mutated copy "
     "overwrote outputs/route_s_sections.out.txt -- the exact file the "
     "claims cite by digest. After a full gate run the surviving artefact "
     "was the LAST ARM's output, reporting a display DIFFERS that does not. "
     "It was caught only because the emitter re-reads its evidence and "
     "refused to write. The arms now run in a scratch directory and the "
     "gate's output is byte-identical before and after they run.",
     "build", "scripts/mutants_route_s_sections.py", ARMS,
     ((14, ARMS, "ARMS:"),)),

    ("S46-18", "STRUCTURAL",
     "Sections 0-10 close the standing gap the run has carried since group "
     "A: every displayed formula now has a stated route and a verdict, so a "
     "transposed digit inside a display is no longer invisible to the "
     "checks. The gap remains open only for quantities routed S-corpus, "
     "whose printed form is inherited from a claim's output rather than "
     "re-derived here; those 15 are named individually in the manifest.",
     "file_inspection", "scripts/manifest.py", MAN,
     ((15, MAN, "S-corpus"),)),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = 0
    records = []
    for cid, label, claim, etype, script, ev, figures in CLAIMS:
        # the script must exist
        if not (HERE / script).exists():
            sys.exit("REFUSED: %s cites a script that does not exist: %s"
                     % (cid, script))
        checks += 1
        evp = HERE / ev
        if not evp.exists():
            sys.exit("REFUSED: %s cites evidence that does not exist: %s"
                     % (cid, ev))
        checks += 1
        if label not in ("PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED",
                         "CONJECTURED"):
            sys.exit("REFUSED: %s carries a label outside the five: %s"
                     % (cid, label))
        checks += 1
        if not claim.strip():
            sys.exit("REFUSED: %s has empty claim text" % cid)
        checks += 1

        # THE ANCHORED-FIGURE RULE
        evtext = evp.read_text(encoding="utf-8",
                               errors="replace").replace("\r\n", "\n")
        for number, evfile, anchor in figures:
            if evfile != ev:
                sys.exit("REFUSED: %s cites a figure from a file other than "
                         "its evidence file" % cid)
            hit = [ln for ln in evtext.split("\n")
                   if anchor in ln and str(number) in ln]
            if not hit:
                sys.exit("REFUSED: %s cites %d with anchor %r, but no line of "
                         "%s carries both" % (cid, number, anchor, ev))
            checks += 1

        records.append({
            "claim_id": cid,
            "task_id": "CT-S46-FORMULA-SECTIONS",
            "claim": claim,
            "label": label,
            "evidence_type": etype,
            "dps": "exact",
            "reproducible": True,
            "script": script,
            "output_hash": sha(evp),
        })

    ids = [r["claim_id"] for r in records]
    if len(ids) != len(set(ids)):
        sys.exit("REFUSED: duplicate claim ids")
    checks += 1

    buf = "\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n"
    data = buf.encode("utf-8")

    # BYTE-EXACT WRITE: validate the ENCODED BYTES before anything reaches disk
    if b"\r" in data:
        sys.exit("REFUSED: encoded buffer contains CR; refusing to write")
    checks += 1
    for line in data.split(b"\n"):
        if line and not line.startswith(b"{"):
            sys.exit("REFUSED: a line of the buffer is not a JSON object")
    checks += 1
    reparsed = [json.loads(l) for l in data.decode("utf-8").splitlines()]
    if reparsed != records:
        sys.exit("REFUSED: the encoded buffer does not re-parse to the records")
    checks += 1

    ART.write_bytes(data)
    if ART.read_bytes() != data:
        sys.exit("WROTE, BUT READ-BACK DIFFERS")

    print("%d claims, %d pre-write checks, exit 0" % (len(records), checks))
    print("claims.jsonl sha256 %s" % sha(ART))
    return 0


if __name__ == "__main__":
    sys.exit(main())
