"""Route P for sections 0-10: displays transcribed from a printed source.

Each entry records the image, its sha256, the folio READ OFF THE PAGE (not
taken from the filename), and the verdict of comparing the paper's display
against what the page shows.

The folio-from-filename distinction is not pedantry. This session found a page
image in the tree named `jimbo_p1152.png` whose printed folio is 1153, and
whose content is not the formula that cites p. 1152. Trusting the name would
have reported eq:jimbo unverifiable; reading the folio found the right file.

The DLMF entry is additionally checked MECHANICALLY against the held source
text, because for that one entry a machine-readable source exists.
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
REFS = HERE / "refs"

# (image, folio read off the page, running head read off the page, displays)
READINGS = [
    ("vdps_p2655.png", "2655",
     "MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS",
     ["section4.tex L55 A=[[a,b],[c,-a]]  -- page: A=z(z-1)(Ainf+A0/z+A1/(z-1))",
      "section4.tex L60 eq:fam-a  -- MATCHES page a(z) term for term",
      "section4.tex L60 eq:fam-b  -- MATCHES page b(z) EXCEPT the first square,"
      " where the page prints (p+1/2(q-1)q)^2 with no t; that is the misprint"
      " rem:typo declares and corrects (S16-05), and the page's second term"
      " does carry (q-1)qt, exactly as the remark states",
      "section4.tex L60 eq:fam-c  -- MATCHES page c(z) = -(z-q)/(q-1)",
      "section4.tex L95 eq:chart  -- MATCHES page U_0 = C x (C\\{0,1})"]),

    ("vdps_p2656.png", "2656",
     "Marius VAN DER PUT & Masa-Hiko SAITO",
     ["section4.tex L100 eq:omega -- MATCHES page Omega = dp^dq/(q(q-1)) - dHV^dt",
      "section4.tex L107 (4.4)    -- MATCHES page: dp/dt=q(q-1)dHV/dq,"
      " dq/dt=-q(q-1)dHV/dp",
      "section4.tex L107 (4.5) HV -- MATCHES page (4.5) term for term"]),

    ("vdps_p2635.png", "2635",
     "MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS",
     ["section1.tex L281 Katz tuple -- MATCHES Table 2.1 column order"
      " r(0), r(1), r(inf), r(t)",
      "section1.tex L289 D5~ row    -- MATCHES Table 2.1: PV, 0,0,1,-, dim 3",
      "section1.tex L289 D6~ row    -- MATCHES Table 2.1: PVdeg=PIII(D6),"
      " 0,0,1/2,-, dim 2; note Table 2.1 prints PIII(D6) WITHOUT a tilde"
      " while p.2656 prints PIII(D6~) WITH one. Section 1 follows Table 2.1,"
      " which is what it says it does. The variance is the source's own."]),

    ("jimbo_printed1152.png", "1152", "MICHIO JIMBO",
     ["section4.tex L153 eq:jimbo -- MATCHES all four parameters:"
      " alpha=1/8(th0-tht+thinf)^2, beta=-1/8(th0-tht-thinf)^2,"
      " gamma=1-th0-tht, delta=-1/2"]),

    ("jimbo_p1152.png", "1153", "BOUNDARY CONDITION FOR PAINLEVE EQUATIONS",
     ["NOT USED. Filename says 1152; the printed folio is 1153. This page"
      " carries the Stokes/connection parametrisation, not the (alpha,beta,"
      " gamma,delta) dictionary. Recorded so the misnaming is not"
      " rediscovered as a defect in the paper."]),
]

OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


say("=" * 74)
say("ROUTE P -- sections 0-10, displays transcribed from printed sources")
say("=" * 74)
say()

missing = []
for img, folio, head, displays in READINGS:
    path = REFS / img
    if not path.exists():
        missing.append(img)
        say("  MISSING IMAGE  %s" % img)
        continue
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    say("  image  %s" % img)
    say("    sha256 %s" % h)
    say("    folio read off the page : %s" % folio)
    say("    running head            : %s" % head)
    for d in displays:
        say("    - %s" % d)
    say()

# ---------------------------------------------------------------------------
# The one route-P display with a machine-readable source: DLMF 2.9.6.
say("MECHANICAL CHECK -- DLMF 2.9.6 against the held source text")
dlmf = REFS / "dlmf_2_9.txt"
if not dlmf.exists():
    sys.exit("READER FAILED: dlmf_2_9.txt not held in refs/")
text = dlmf.read_text(encoding="utf-8", errors="replace")
# DLMF's text export separates every token with spaces and uses invisible
# multiplication characters; normalise to bare symbols before comparing.
norm = re.sub(r"[\u2061\u2062\u2063\s]+", "", text)

# positive control: 2.9.5 must be found, so that "absent" cannot silently
# mean "my reader could not see it"
ctrl = "ρ2+f0ρ+g0=0"
if ctrl not in norm:
    sys.exit("READER FAILED: positive control (DLMF 2.9.5) not found; "
             "the normaliser is not reading the source")
say("  positive control DLMF 2.9.5 'rho^2+f0 rho+g0=0' found : YES")

target = "αj=(f1ρj+g1)/(f0ρj+2g0)"
found = target in norm
say("  paper's display alpha_j=(f1 rho_j+g1)/(f0 rho_j+2 g0) : %s"
    % ("MATCHES" if found else "DIFFERS"))

# negative control: a one-digit corruption of the paper's display must NOT be
# found, or the check would pass on anything
bogus = "αj=(f1ρj+g1)/(f0ρj+3g0)"
if bogus in norm:
    sys.exit("READER FAILED: a corrupted form of 2.9.6 also matches")
say("  negative control (2 g0 -> 3 g0) correctly absent      : YES")
say()

say("=" * 74)
ok = not missing and found
say("ROUTE P: %d images read, %d displays verified"
    % (len([r for r in READINGS if (REFS / r[0]).exists()]) ,
       sum(len(r[3]) for r in READINGS if not r[3][0].startswith("NOT USED"))))
say("ROUTE P: %s" % ("all transcriptions agree with their pages"
                     if ok else "UNRESOLVED -- see above"))
say("=" * 74)

(HERE / "outputs" / "route_p.out.txt").write_bytes(
    ("\n".join(OUT) + "\n").encode("utf-8"))
sys.exit(0 if ok else 1)
