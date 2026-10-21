"""Route P of the Appendix A formula pass: the record of what was read off each
page image, with the folio read off the page itself rather than taken from the
filename.

A filename is not evidence of which page an image shows.  Each entry below
records the folio and the running head or author line that fixes it, both read
from the rendered image by eye.  That is INSPECTED evidence and is never
promoted: no verdict in this file is VERIFIED or PROVEN.

The digests let a later session confirm it read the same bytes.
"""
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
REFS = HERE / "refs"

# (image, folio read off the page, the header/footer that fixes it, what was
#  read, and the appendix claim it bears on)
READINGS = [
    ("vdps_p2655.png", "2655",
     "running head 'MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS'; "
     "footer 'TOME 59 (2009), FASCICULE 7'",
     "b(z) first squared bracket prints (p + 1/2(q-1)q)^2 -- NO t; the second "
     "term carries (q-1)qt in BOTH factors; c(z) = -(z-q)/(q-1); "
     "a(z) = p + 1/2(-2qt+t-theta_inf)(z-q) - 1/2 t(z-q)^2; "
     "A = z(z-1)(A_inf + A_0/z + A_1/(z-1)) = [[a,b],[c,-a]]",
     "S16-18 CONFIRMED"),
    ("vdps_p2655.png", "2655", "as above",
     "'The first basis vector is chosen as cyclic vector and following "
     "Subsection 4.1, q is the unique zero of c(z) and p = a(q).' -- quoted "
     "verbatim in the appendix, and it matches the page word for word",
     "S17-17 CONFIRMED"),
    ("vdps_p2655.png", "2655", "as above",
     "'The parameter (p,q) gives canonical coordinates on an affine Zariski "
     "open set U_0 CONG C x (C \\ {0,1}) of the moduli space M_{t,lambda}' -- "
     "the page prints the relation as \\cong, the appendix had transcribed it "
     "as =",
     "S16-18 DISCREPANCY, repaired"),
    ("vdps_p2655.png", "2655", "as above",
     "B = zB_0 + (1/t)B_1; the (1,2) entry of B_1 prints "
     "(p + 1/2(q-1)qt)^2 -- WITH the t, a few lines below b(z)",
     "S16-R18-01 CONFIRMED"),
    ("vdps_p2637.png", "2637",
     "running head 'MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS'; "
     "footer 'TOME 59 (2009), FASCICULE 7'",
     "'Further -theta_i^2/4 is the determinant of A_i FOR i = 0, 1 and, "
     "theta_inf is the (1,1) entry of A_0 + A_1.' The restriction to i = 0,1 "
     "is explicit on the page; A_inf is instead normalised as "
     "t/2 . diag(-1,1), so det A_inf = -t^2/4 and the unrestricted form the "
     "appendix quoted would be false at i = infinity",
     "S16-20 DISCREPANCY, repaired"),
    ("arxiv_v5_p34_bz_LOOK.png", "34",
     "author line 'MARIUS VAN DER PUT AND MASA-HIKO SAITO'",
     "b(z) first squared bracket prints (p + 1/2(q-1)q)^2 -- NO t, identical "
     "to the journal text; U_0 again printed with \\cong",
     "S16-19 CONFIRMED"),
    ("arxiv_v5_p34_B1_LOOK.png", "34 (same page, lower)",
     "continuous with the b(z) display above it",
     "B_1 (1,2) entry prints (p + 1/2(q-1)qt)^2 -- WITH the t, so the "
     "asymmetry is present in v5 exactly as in the journal",
     "S16-R18-01 CONFIRMED"),
]


def main():
    missing = [im for im, *_ in READINGS if not (REFS / im).exists()]
    if missing:
        sys.exit("READER INTEGRITY FAILED: missing image(s): %s"
                 % ", ".join(sorted(set(missing))))

    print("ROUTE P -- readings from page images, folio read off the page")
    print("=" * 74)
    seen = {}
    for im, folio, fixer, reading, bears in READINGS:
        d = seen.get(im)
        if d is None:
            d = hashlib.sha256((REFS / im).read_bytes()).hexdigest()
            seen[im] = d
        print()
        print("image  : %s" % im)
        print("sha256 : %s" % d)
        print("folio  : %s   (fixed by: %s)" % (folio, fixer))
        print("read   : %s" % reading)
        print("bears  : %s" % bears)

    print()
    print("=" * 74)
    print("%d readings over %d distinct images" % (len(READINGS), len(seen)))
    print("Label for every line above: INSPECTED. Reading a rendered image by "
          "eye is not a computation and is not promoted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
