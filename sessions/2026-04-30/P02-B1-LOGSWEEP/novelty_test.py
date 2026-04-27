"""
P02-B1-LOGSWEEP novelty test.

Compares our PCF family (alpha(n) = -k n^2, beta(n) = (k+1)n + k,
limit = 1/ln(k/(k-1))) against the classical Euler CF for ln(1+z).

Tests:
 (i)  Empirical convergence rate of our PCF for k=2.
 (ii) Whether our PCF is the even contraction of Euler's CF for
      ln(1+z)/z evaluated at z = 1/(k-1).
"""

from fractions import Fraction
import math


def our_pcf(k, N):
    """alpha(n) = -k n^2, beta(n) = (k+1)n + k.  p_-1=1, p_0=k=beta(0)."""
    p_pp, p_p = Fraction(1), Fraction(k)
    q_pp, q_p = Fraction(0), Fraction(1)
    convs = [p_p / q_p]
    for n in range(1, N + 1):
        bn = (k + 1) * n + k
        an = -k * n * n
        p = bn * p_p + an * p_pp
        q = bn * q_p + an * q_pp
        p_pp, p_p = p_p, p
        q_pp, q_p = q_p, q
        convs.append(p / q)
    return convs


def euler_cf_ln1pz(z, N):
    """
    Standard Euler CF (Lorentzen-Waadeland eq. (2.4.2)):
        ln(1+z) = z/(1 + 1*z/(2 + 1*z/(3 + 4z/(4 + 4z/(5 + 9z/(6 + ...
    Partial numerators: a_1 = z; for m >= 1, a_{2m} = a_{2m+1} = m^2 z.
    Partial denominators: b_n = n for n >= 1 (b_0 = 0).
    Returns value as a Fraction (z must be rational).
    """
    z = Fraction(z)
    val = Fraction(0)
    for n in range(N, 0, -1):
        if n == 1:
            an = z
        else:
            m = n // 2
            an = Fraction(m * m) * z
        bn = Fraction(n)
        val = an / (bn + val)
    return val


def even_contraction_pcf(k, N):
    """
    Even contraction of Euler CF for ln(1+z)/z at z = 1/(k-1).
    Goal: see if it matches our PCF p_n/q_n exactly.

    Standard formula (Wall, Analytic Theory of CFs, Thm 21.1):
    For CF b_0 + K(a_n/b_n), the even part has convergents equal to
    even-indexed convergents of original.  We compare values directly.
    """
    # Compute Euler convergents for ln(1+z)/z, then take 1 / (z * value) ?
    # Actually our PCF -> 1/ln(k/(k-1)) and Euler CF for ln(1+z) at z=1/(k-1)
    # gives ln(k/(k-1)).  So 1 / Euler_value(N) should match our PCF for large N.
    z = Fraction(1, k - 1)
    convs = []
    # compute convergents incrementally via forward recurrence with rational
    p_pp, p_p = Fraction(1), Fraction(0)  # b_0 = 0
    q_pp, q_p = Fraction(0), Fraction(1)
    for n in range(1, 2 * N + 1):
        if n == 1:
            an = z
        else:
            m = n // 2
            an = Fraction(m * m) * z
        bn = Fraction(n)
        p = bn * p_p + an * p_pp
        q = bn * q_p + an * q_pp
        p_pp, p_p = p_p, p
        q_pp, q_p = q_p, q
        if q != 0:
            convs.append(p / q)  # this is approx ln(k/(k-1))
    return convs


def main():
    k = 2
    N = 14
    target = 1 / math.log(2)  # since k=2, target = 1/ln(2/1) = 1/ln 2

    print(f"k = {k}, target 1/ln(k/(k-1)) = {target:.15f}")
    print()

    print("Our PCF convergents:")
    ours = our_pcf(k, N)
    prev_err = None
    for i, c in enumerate(ours):
        cf = float(c)
        err = abs(cf - target)
        ratio = (err / prev_err) if (prev_err and err > 0) else float('nan')
        print(f"  n={i:2d}  C_n = {cf:.15f}  |err|={err:.3e}  ratio={ratio:.4f}")
        if err > 0:
            prev_err = err

    print()
    print("Euler CF for ln(1+z) at z = 1/(k-1) = 1, take reciprocal:")
    euler_convs = even_contraction_pcf(k, N)
    target2 = math.log(2)  # ln(1+1)
    for i, c in enumerate(euler_convs[:2 * N]):
        cf = float(c)
        err = cf - target2
        # Reciprocal -> compare to 1/ln 2
        recip = 1 / cf if cf != 0 else float('nan')
        recip_err = recip - target
        print(f"  n={i+1:2d}  E_n={cf:.12f}  err={err:+.3e}  1/E_n={recip:.12f}  err={recip_err:+.3e}")

    # Now key question: do EVEN-indexed Euler convergents match our PCF
    # under the reciprocal map?
    print()
    print("Match test: our convergent C_n  vs  1 / Euler_{2n+1} (reciprocal of odd):")
    for i in range(min(N, len(euler_convs) // 2)):
        ours_val = ours[i]
        if 2 * i + 1 < len(euler_convs):
            recip = 1 / euler_convs[2 * i + 1] if euler_convs[2 * i + 1] != 0 else None
            same = (ours_val == recip)
            print(f"  n={i:2d}  ours={float(ours_val):.10f}  1/E_{{2n+1}}={float(recip):.10f}  exact match? {same}")


if __name__ == "__main__":
    main()
