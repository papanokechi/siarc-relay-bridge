"""
K computation and PSLQ classification for d=3 PCFs.
Uses Euler-Wallis recurrence: P_n = b(n)*P_{n-1} + a(n)*P_{n-2}
Convention: a = partial numerator poly, b = partial denominator poly.
Coefficients [c3, c2, c1, c0], leading first.
"""
import numpy as np
from mpmath import mp, mpf, pi as mp_pi, pslq, fabs


# ---------------------------------------------------------------------------
# Float64 batch computation (Lentz algorithm)
# ---------------------------------------------------------------------------

def compute_K_batch_lentz(a_coeffs, b_coeffs, N=200):
    """
    Batch K computation using modified Lentz algorithm at float64.
    Returns (K_values, converged_mask).
    """
    M = len(a_coeffs)
    if M == 0:
        return np.array([]), np.array([], dtype=bool)

    tiny = 1e-300
    a = a_coeffs.astype(np.float64)
    b = b_coeffs.astype(np.float64)

    # f_0 = b(0) = b0
    b0 = b[:, 3]
    f = np.where(b0 != 0, b0, tiny)
    C = f.copy()
    D = np.zeros(M, dtype=np.float64)

    K_mid = None

    for n in range(1, N + 1):
        n2, n3 = n * n, n * n * n
        a_n = a[:, 0] * n3 + a[:, 1] * n2 + a[:, 2] * n + a[:, 3]
        b_n = b[:, 0] * n3 + b[:, 1] * n2 + b[:, 2] * n + b[:, 3]

        D = b_n + a_n * D
        D = np.where(D == 0, tiny, D)
        D = 1.0 / D

        C = b_n + a_n / C
        C = np.where(C == 0, tiny, C)

        delta = C * D
        f = f * delta

        if n == N // 2:
            K_mid = f.copy()

    K = f
    converged = np.isfinite(K)
    if K_mid is not None:
        converged &= np.isfinite(K_mid)
        denom = np.maximum(np.abs(K), 1e-10)
        converged &= (np.abs(K - K_mid) < 1e-4 * denom)

    return K, converged


def rat_prescreen_float(K_values, max_q=300, tol=1e-4):
    """
    Float64 rationality pre-screen.
    Returns mask where True = likely rational (skip PSLQ).
    """
    likely_rat = np.zeros(len(K_values), dtype=bool)
    finite = np.isfinite(K_values)
    for q in range(1, max_q + 1):
        prod = K_values * q
        residual = np.abs(prod - np.round(prod))
        likely_rat |= (residual < tol) & finite
    return likely_rat


# ---------------------------------------------------------------------------
# mpmath high-precision computation
# ---------------------------------------------------------------------------

def compute_K_mpmath(a_coeffs, b_coeffs, N=500, dps=150):
    """
    Compute K for a single family using mpmath Euler-Wallis recurrence.
    a_coeffs, b_coeffs: array-like of 4 ints [c3,c2,c1,c0].
    Returns K (mpf) or None if divergent.
    """
    mp.dps = dps + 50
    a3, a2, a1, a0 = [mpf(int(c)) for c in a_coeffs]
    b3, b2, b1, b0 = [mpf(int(c)) for c in b_coeffs]

    Pp, Pc = mpf(1), b0          # P(-1)=1, P(0)=b(0)
    Qp, Qc = mpf(0), mpf(1)     # Q(-1)=0, Q(0)=1

    for n in range(1, N + 1):
        nn = mpf(n)
        an = a3 * nn**3 + a2 * nn**2 + a1 * nn + a0
        bn = b3 * nn**3 + b2 * nn**2 + b1 * nn + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 50 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10)**20:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s

    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)


# ---------------------------------------------------------------------------
# PSLQ classification
# ---------------------------------------------------------------------------

def classify_single(K, dps=150):
    """
    Run PSLQ cascade on a single K value.
    Returns dict with stratum, basis, relation, residual.
    """
    mp.dps = dps

    # Rational check: {1, K}
    try:
        rel = pslq([mpf(1), K], maxcoeff=10**6)
    except Exception:
        rel = None
    if rel is not None:
        residual = fabs(rel[0] + rel[1] * K)
        if residual < mpf(10)**(-40):
            return {'stratum': 'Rat', 'basis': 'R',
                    'relation': list(rel), 'residual': float(residual)}

    # Trans T1: {1, K, pi, K*pi, pi^2}
    try:
        basis_vals = [mpf(1), K, mp_pi, K * mp_pi, mp_pi**2]
        rel = pslq(basis_vals, maxcoeff=10**8)
    except Exception:
        rel = None
    if rel is not None:
        residual = fabs(sum(r * v for r, v in zip(rel, basis_vals)))
        if residual < mpf(10)**(-30):
            # Contamination check: make sure it's not secretly rational
            rat_check = pslq([mpf(1), K], maxcoeff=10**6)
            if rat_check is not None:
                rat_res = fabs(rat_check[0] + rat_check[1] * K)
                if rat_res < mpf(10)**(-40):
                    return {'stratum': 'Rat', 'basis': 'R',
                            'relation': list(rat_check), 'residual': float(rat_res)}
            return {'stratum': 'Trans', 'basis': 'T1',
                    'relation': list(rel), 'residual': float(residual)}

    # Log L1: {1, K, ln2, K*ln2}  (quick check for unexpected finds)
    from mpmath import log
    try:
        ln2 = log(2)
        basis_vals = [mpf(1), K, ln2, K * ln2]
        rel = pslq(basis_vals, maxcoeff=10**8)
    except Exception:
        rel = None
    if rel is not None:
        residual = fabs(sum(r * v for r, v in zip(rel, basis_vals)))
        if residual < mpf(10)**(-30):
            return {'stratum': 'Log', 'basis': 'L1',
                    'relation': list(rel), 'residual': float(residual)}

    return {'stratum': 'Desert', 'basis': None,
            'relation': None, 'residual': None}


def confirm_classification(a_coeffs, b_coeffs, classification, dps=300, N=500):
    """Confirm a Trans/Log hit at higher precision."""
    K = compute_K_mpmath(a_coeffs, b_coeffs, N=N, dps=dps)
    if K is None:
        return None
    result = classify_single(K, dps=dps)
    return result
