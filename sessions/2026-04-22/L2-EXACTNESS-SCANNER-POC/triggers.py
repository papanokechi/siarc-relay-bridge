"""
Trigger conditions for the exactness scanner.
Checks numerical values for near-exact algebraic relationships.
"""

from mpmath import mpf, mpc, mp, nint, fabs, floor, log10


def check_near_integer(x, threshold=mpf("1e-20")):
    """Check if x is near an integer."""
    if isinstance(x, mpc):
        if fabs(x.imag) > threshold:
            return False, None
        x = x.real
    rounded = nint(x)
    gap = fabs(x - rounded)
    if gap < threshold:
        return True, {"type": "near-integer", "nearest_int": int(rounded), "gap": float(gap)}
    return False, None


def check_near_fraction(x, max_q=100, threshold=mpf("1e-20")):
    """Check if x is near a simple fraction p/q with |q| <= max_q."""
    if isinstance(x, mpc):
        if fabs(x.imag) > threshold:
            return False, None
        x = x.real

    # Use continued fraction convergents
    try:
        cf_terms = []
        rem = x
        for _ in range(30):
            a_i = int(floor(rem))
            cf_terms.append(a_i)
            frac = rem - a_i
            if fabs(frac) < mpf("1e-50"):
                break
            rem = 1 / frac

        # Compute convergents
        h_prev, h_curr = 0, 1
        k_prev, k_curr = 1, 0
        for a_i in cf_terms:
            h_prev, h_curr = h_curr, a_i * h_curr + h_prev
            k_prev, k_curr = k_curr, a_i * k_curr + k_prev
            if 0 < abs(k_curr) <= max_q:
                approx = mpf(h_curr) / mpf(k_curr)
                gap = fabs(x - approx)
                if gap < threshold:
                    return True, {
                        "type": "near-fraction",
                        "p": h_curr,
                        "q": k_curr,
                        "gap": float(gap),
                    }
    except (ZeroDivisionError, OverflowError):
        pass
    return False, None


def check_near_zero(x, threshold=mpf("1e-20")):
    """Check if x is near zero."""
    if isinstance(x, mpc):
        mag = fabs(x)
    else:
        mag = fabs(x)
    if mag < threshold:
        return True, {"type": "near-zero", "magnitude": float(mag)}
    return False, None


def check_sq_near_integer(x, threshold=mpf("1e-15")):
    """Check if |x|^2 is near an integer (detects quadratic irrationals)."""
    if isinstance(x, mpc):
        sq = x.real ** 2 + x.imag ** 2
    else:
        sq = x ** 2
    sq_abs = fabs(sq)
    rounded = nint(sq_abs)
    gap = fabs(sq_abs - rounded)
    if gap < threshold and int(rounded) > 0:
        return True, {
            "type": "sq-near-integer",
            "x_squared": float(sq_abs),
            "nearest_int": int(rounded),
            "gap": float(gap),
        }
    return False, None


def run_all_triggers(x):
    """Run all trigger checks on value x. Returns list of triggered conditions."""
    triggers = []

    hit, info = check_near_zero(x)
    if hit:
        triggers.append(info)
        return triggers  # near-zero implies rational (=0)

    hit, info = check_near_integer(x)
    if hit:
        triggers.append(info)

    hit, info = check_near_fraction(x)
    if hit:
        triggers.append(info)

    hit, info = check_sq_near_integer(x)
    if hit:
        triggers.append(info)

    return triggers
