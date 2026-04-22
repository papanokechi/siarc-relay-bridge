"""
Algebraic degree tester using PSLQ.
For a triggered value x, determines the minimal polynomial degree.
"""

from mpmath import mp, mpf, matrix, fabs, pslq, power


def find_algebraic_relation(x, max_degree=4, dps=100, h_max=10**8):
    """
    Run PSLQ against polynomial bases {1, x, x², ...} up to max_degree.
    Returns the minimal degree relation found, or None.
    """
    old_dps = mp.dps
    mp.dps = dps
    try:
        x = mpf(x) if not isinstance(x, mpf) else x
        # PSLQ cannot handle zero — check if x is near-zero first
        if fabs(x) < mpf("1e-40"):
            return {
                "degree": 1,
                "minimal_poly": [0, 1],
                "residual": float(fabs(x)),
            }
        for d in range(1, max_degree + 1):
            basis = [power(x, k) for k in range(d + 1)]
            rel = pslq(basis, maxcoeff=h_max)
            if rel is not None:
                # Verify residual
                residual = sum(rel[k] * power(x, k) for k in range(d + 1))
                if fabs(residual) < mpf("1e-40"):
                    # Check if this is truly degree d (leading coeff nonzero)
                    if rel[d] != 0:
                        return {
                            "degree": d,
                            "minimal_poly": list(rel),
                            "residual": float(fabs(residual)),
                        }
                    # Leading coeff is zero — relation is lower degree, already found
                    # Try to extract the actual relation
                    actual_deg = max(k for k in range(d + 1) if rel[k] != 0)
                    return {
                        "degree": actual_deg,
                        "minimal_poly": list(rel[: actual_deg + 1]),
                        "residual": float(fabs(residual)),
                    }
        return None
    finally:
        mp.dps = old_dps


def classify_algebraic(x, max_degree=4, dps=100):
    """
    Classify x as rational, algebraic, or transcendental (up to degree bound).
    Returns a dict with classification info.
    """
    result = find_algebraic_relation(x, max_degree=max_degree, dps=dps)
    if result is None:
        return {
            "algebraic_degree": None,
            "minimal_poly": None,
            "verdict": "TRANSCENDENTAL",
            "cm_discriminant": None,
        }

    degree = result["degree"]
    poly = result["minimal_poly"]

    if degree == 1:
        # Rational: poly is [a0, a1] meaning a0 + a1*x = 0, so x = -a0/a1
        verdict = "EXACT-RATIONAL"
        cm_disc = None
    elif degree == 2:
        # Quadratic: poly is [a0, a1, a2] meaning a0 + a1*x + a2*x^2 = 0
        # Discriminant = a1^2 - 4*a0*a2
        disc = poly[1] ** 2 - 4 * poly[0] * poly[2]
        cm_discs = {-3, -4, -7, -8, -11, -19, -43, -67, -163}
        cm_disc = disc if disc in cm_discs else None
        verdict = "EXACT-ALGEBRAIC"
    else:
        verdict = "EXACT-ALGEBRAIC"
        cm_disc = None

    return {
        "algebraic_degree": degree,
        "minimal_poly": poly,
        "verdict": verdict,
        "cm_discriminant": cm_disc,
        "pslq_residual": result["residual"],
    }


def check_exact_fraction(x, p, q, dps=100):
    """Check if x is exactly p/q."""
    old_dps = mp.dps
    mp.dps = dps
    try:
        x = mpf(x) if not isinstance(x, mpf) else x
        target = mpf(p) / mpf(q)
        gap = fabs(x - target)
        return float(gap) < 1e-40
    finally:
        mp.dps = old_dps
