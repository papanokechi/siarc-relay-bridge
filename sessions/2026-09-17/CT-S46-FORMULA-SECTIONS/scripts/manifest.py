"""Routing manifest for every display in sections 0-10.

Each display is assigned exactly one route:

  S-here    re-derived symbolically in this session by route_s_sections.py;
            the naming column gives the check tag that does it
  S-corpus  computed by a named corpus claim/script that is NOT re-run here;
            the naming column gives the claim id
  P         transcribed from a page of a source; the naming column gives the
            page, and the display must be checked against the held image
  DEF       the display IS a definition -- there is nothing to re-derive,
            because no prior quantity determines it
  UNROUTED  neither route available. This is a FINDING, not a gap to hide.

The manifest asserts it covers the census exactly: a display added, removed or
moved makes this script fail rather than drift silently out of date.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
CENSUS = HERE / "outputs" / "display_census.out.txt"

# (file, line, route, source, short description)
MANIFEST = [
    ("section0.tex", 15, "DEF", "-", "the recurrence Q_n=b(n)Q_{n-1}+Q_{n-2}"),
    ("section0.tex", 26, "S-corpus", "S1-04", "growth law, sec 0 restatement"),

    ("section1.tex", 21, "DEF", "-", "b(n)=sum beta_k n^k"),
    ("section1.tex", 29, "DEF", "-", "eq:n-rec"),
    ("section1.tex", 33, "DEF", "-", "eq:n-norm B_n, psi_n"),
    ("section1.tex", 40, "DEF", "-", "eq:n-roots nu_i"),
    ("section1.tex", 116, "S-corpus", "S1-04", "growth law restated"),
    ("section1.tex", 121, "S-corpus", "S1-04", "s = b_{d-1}/b_d+(d-1)/2"),
    ("section1.tex", 138, "S-here", "X5", "xi_0 = 2/sqrt(beta_2) at d=2"),
    ("section1.tex", 210, "S-here", "G1,R3", "R = P^2/4+P'/2-Q"),
    ("section1.tex", 281, "P", "vdPS Table 2.1", "Katz tuple (r(0),r(1),r(inf),r(t))"),
    ("section1.tex", 289, "P", "vdPS Table 2.1", "D5~/D6~ rows"),
    ("section1.tex", 312, "DEF", "-", "eq:n-traces x_1,x_2,x_3"),

    ("section2.tex", 45, "P", "DLMF 2.9.6", "alpha_j, checked in route_p.py"),
    ("section2.tex", 124, "S-here", "P1", "eq:psi-rec"),
    ("section2.tex", 149, "S-corpus", "S26-01", "psi_n upper bound, Proposition U"),
    ("section2.tex", 191, "S-corpus", "S1-04", "eq:growth-law, thm:growth"),
    ("section2.tex", 198, "S-corpus", "S1-04", "eq:K amplitude"),
    ("section2.tex", 237, "S-corpus", "S3B-02, S3B-09", "psi_infty to 48 places"),

    ("section3.tex", 20, "S-corpus", "S4-03", "eq:sysA, residual to z^38"),
    ("section3.tex", 29, "S-here", "A1", "eq:rA from eq:sysA"),
    ("section3.tex", 46, "S-here", "B0,B1", "eq:rB via z=1/x from eq:rC"),
    ("section3.tex", 52, "S-here", "C2", "eq:sysC, self-adjoint b=a'"),
    ("section3.tex", 59, "S-here", "C1", "eq:rC from eq:sysC"),
    ("section3.tex", 64, "S-here", "C3,C4,C5", "eq:spm s_pm and delta"),
    ("section3.tex", 83, "S-here", "X1,X2", "exp(-+2/sqrt3 z^-1/2), WKB at z=0"),
    ("section3.tex", 100, "S-here", "X3,X4", "exp(+-sqrt3 x/3) at infinity"),
    ("section3.tex", 127, "S-here", "R6", "eq:logcoef, rationalised"),
    ("section3.tex", 165, "DEF", "-", "eq:cover pi: w -> z=w^2"),
    ("section3.tex", 235, "S-corpus", "S6-C18", "eq:gauge x^{sqrt3/18-1}exp(...)"),

    ("section4.tex", 20, "DEF", "-", "eq:module"),
    ("section4.tex", 25, "P", "vdPS p.2655", "eq:Ainf A_inf = (t/2)diag(-1,1)"),
    ("section4.tex", 55, "DEF", "-", "A = [[a,b],[c,-a]], N = -A/D"),
    ("section4.tex", 60, "P", "vdPS p.2655", "family (4.1): a, b, c"),
    ("section4.tex", 95, "P", "vdPS p.2655", "eq:chart U_0 = C x (C-{0,1})"),
    ("section4.tex", 100, "P", "vdPS p.2656", "eq:omega symplectic form"),
    ("section4.tex", 107, "P", "vdPS p.2656", "(4.4) Hamiltonian system, H_V"),
    ("section4.tex", 153, "P", "vdPS / Jimbo-Miwa", "eq:jimbo alpha,beta,gamma,delta"),

    ("section5.tex", 26, "S-corpus", "S16-03", "t(theta_inf+1)/2, the rejected naive reading"),
    ("section5.tex", 49, "S-here", "T1,T2", "r_z expansion at infinity"),
    ("section5.tex", 53, "S-here", "T3", "t = -+2i sqrt33/9"),
    ("section5.tex", 68, "S-here", "T6,T7,T8,T9", "n = -1 -+ sqrt3/18, Riccati"),
    ("section5.tex", 117, "S-corpus", "S16-12", "theta_inf (R4 here), q exact"),
    ("section5.tex", 122, "S-corpus", "S16-12", "p exact algebraic number"),
    ("section5.tex", 127, "S-corpus", "S16-12", "theta_inf (R5 here), q,p approx"),
    ("section5.tex", 165, "S-here", "R7", "K = Q(i sqrt11)"),
    ("section5.tex", 182, "S-here", "E1,E2", "eq:eliminant"),

    ("section6.tex", 24, "DEF", "-", "L = d - 1/(2z)"),
    ("section6.tex", 58, "S-here", "G1", "R = P^2/4+P'/2-Q restated"),
    ("section6.tex", 68, "S-here", "S3,S5", "eq:PC and eq:QC"),
    ("section6.tex", 92, "S-here", "S1,S2", "3x^2+x+1 = 3 delta^2 z(z-1)"),
    ("section6.tex", 97, "S-here", "S4", "P_C = D'/D"),
    ("section6.tex", 121, "S-corpus", "S17-10", "eq:route-diff orientation"),

    ("section7.tex", 172, "DEF", "-", "eq:traces-restate"),
    ("section7.tex", 184, "S-corpus", "S22-12", "x_1,x_2,x_3 numerics"),

    ("section9.tex", 39, "S-here", "R1,R2", "P_C,Q_C reprinted"),
]

ROW = re.compile(r"^\s{2}(section\d+\.tex)\s+L(\d+)\s")


def main():
    if not CENSUS.exists():
        sys.exit("READER FAILED: census output not found at %s" % CENSUS)
    text = CENSUS.read_text(encoding="utf-8").replace("\r\n", "\n")
    census = set()
    for line in text.split("\n"):
        m = ROW.match(line)
        if m:
            census.add((m.group(1), int(m.group(2))))

    # reader-integrity floor: a census this small means the reader is broken,
    # not that the paper has no displays
    if len(census) < 10:
        sys.exit("READER FAILED: only %d displays parsed from the census"
                 % len(census))

    manifest = {(f, l) for f, l, _, _, _ in MANIFEST}
    if len(manifest) != len(MANIFEST):
        sys.exit("MANIFEST FAILED: duplicate (file, line) entries")

    missing = sorted(census - manifest)
    extra = sorted(manifest - census)

    print("=" * 74)
    print("ROUTING MANIFEST -- sections 0-10")
    print("=" * 74)
    print("  census displays   : %d" % len(census))
    print("  manifest entries  : %d" % len(manifest))
    print()

    counts = {}
    for _, _, route, _, _ in MANIFEST:
        counts[route] = counts.get(route, 0) + 1
    for route in ("S-here", "S-corpus", "P", "DEF", "UNROUTED"):
        print("  %-10s %3d" % (route, counts.get(route, 0)))
    print()

    for f, l, route, src, desc in MANIFEST:
        print("  %-14s L%-5d %-9s %-22s %s" % (f, l, route, src, desc))
    print()

    ok = True
    # P0: never invent a claim id. Every S-corpus source must resolve to a
    # claim_id actually present in some sessions/*/claims.jsonl. Absence here
    # is a citation defect, not a formatting quibble.
    corpus = set()
    sessroot = HERE.parent.parent
    own = (HERE / "claims.jsonl").resolve()
    for cj in sessroot.rglob("claims.jsonl"):
        # Exclude this session's OWN claims.jsonl (the CT-S41 precedent):
        # otherwise emitting claims changes the census that the claims cite,
        # and the gate cannot be stable within its own session. This closes
        # the staleness trap WITHIN the session only -- any later session's
        # claims.jsonl will still change this figure, so no reproducibility
        # across sessions is asserted for it.
        if cj.resolve() == own:
            continue
        try:
            for line in cj.read_text(encoding="utf-8",
                                     errors="replace").splitlines():
                m = re.search(r'"claim_id"\s*:\s*"([^"]+)"', line)
                if m:
                    corpus.add(m.group(1))
        except OSError:
            continue
    if len(corpus) < 100:
        sys.exit("READER FAILED: only %d claim ids found across the corpus; "
                 "the resolver is not reading claims.jsonl" % len(corpus))
    # positive control: an id known to exist must resolve, so that "absent"
    # cannot silently mean "my reader could not see it"
    if "S16-07" not in corpus:
        sys.exit("READER FAILED: positive control S16-07 does not resolve")
    print("  corpus claim ids read: %d (positive control S16-07 resolves)"
          % len(corpus))
    unresolved = []
    for f, l, route, src, _ in MANIFEST:
        if route != "S-corpus":
            continue
        for cid in [c.strip() for c in src.split(",")]:
            if cid and cid not in corpus:
                unresolved.append((f, l, cid))
    if unresolved:
        ok = False
        print("  UNRESOLVED claim ids cited by the manifest:")
        for f, l, cid in unresolved:
            print("     %s L%d -> %s" % (f, l, cid))
    else:
        print("  every S-corpus claim id resolves in the corpus")
    print()

    if missing:
        ok = False
        print("  UNROUTED -- in the census but not in the manifest:")
        for f, l in missing:
            print("     %s L%d" % (f, l))
    if extra:
        ok = False
        print("  STALE -- in the manifest but not in the census:")
        for f, l in extra:
            print("     %s L%d" % (f, l))
    if ok:
        print("  every census display carries exactly one route")

    print("=" * 74)
    out = HERE / "outputs" / "manifest.out.txt"
    lines = ["census=%d manifest=%d" % (len(census), len(manifest)),
             "corpus_claim_ids=%d control=S16-07" % len(corpus)]
    for route in ("S-here", "S-corpus", "P", "DEF", "UNROUTED"):
        lines.append("route %-10s count %d" % (route, counts.get(route, 0)))
    lines.append("unrouted=%d stale=%d" % (len(missing), len(extra)))
    for f, l, route, src, desc in MANIFEST:
        lines.append("  %-14s L%-5d %-9s %-22s %s" % (f, l, route, src, desc))
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
