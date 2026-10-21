"""CT-S22 - shared solver.  Analytic continuation and irregular-singularity
formal solutions for 2x2 systems

        Y'(z) = B(z) Y(z),      B(z) = Nmat(z) / Dpol(z)

with Nmat a polynomial matrix and Dpol a scalar polynomial, deg Nmat <= deg Dpol
(so B is bounded at infinity and the irregular point at infinity has Katz rank
<= 1).  Written to PREREG section 4.1; no value in this file was chosen after
seeing a result.

Conventions (PREREG section 2):
  * horizontal sections satisfy Y' = B Y with B = -A for a module d/dz + A;
  * all loops counterclockwise;
  * continuation sends a fundamental matrix Y |-> Y M, so M = Y(z*)^-1 Ycont(z*);
  * log z is tracked CONTINUOUSLY along every path, never by principal branch.

Every routine that can silently do nothing carries an assert.  This is the
direct response to CT-S16 S16-11, where a verdict was returned with no test
performed.
"""
import mpmath as mp


# ---------------------------------------------------------------- polynomials

def poly_shift(coeffs, z0):
    """coeffs[j] is the coefficient of z**j.  Return coefficients in w = z - z0."""
    n = len(coeffs)
    out = [c * 0 for c in coeffs]
    # Horner-style synthetic division, repeated
    work = list(coeffs)
    for k in range(n):
        # evaluate and deflate
        acc = work[-1] * 0
        newwork = [None] * (len(work) - 1) if len(work) > 1 else []
        for j in range(len(work) - 1, 0, -1):
            newwork[j - 1] = acc = acc * z0 + work[j]
        out[k] = (acc * z0 + work[0]) if len(work) > 1 else work[0]
        work = newwork
        if not work:
            break
    return out


def _mat_shift(nmat, z0):
    """nmat[j] is a 2x2 mp.matrix, the coefficient of z**j."""
    deg = len(nmat) - 1
    out = [mp.matrix(2, 2) for _ in range(deg + 1)]
    for r in range(2):
        for c in range(2):
            sc = poly_shift([nmat[j][r, c] for j in range(deg + 1)], z0)
            for j in range(deg + 1):
                out[j][r, c] = sc[j]
    return out


# ------------------------------------------------------- Taylor continuation

def taylor_block(nmat, dpol, z0, order):
    """Taylor coefficients of the local solution operator at z0.

    Returns a list C[0..order] of 2x2 matrices with Y(z0+w) = sum_k C[k] w^k Y(z0).
    Derived from Dpol(z) Y' = Nmat(z) Y:

        d0 (m+1) Y_{m+1} = sum_j n_j Y_{m-j} - sum_{j>=1} d_j (m-j+1) Y_{m-j+1}

    which needs d0 = Dpol(z0) != 0, i.e. steps never land on a singular point.
    """
    ns = _mat_shift(nmat, z0)
    ds = poly_shift(dpol, z0)
    d0 = ds[0]
    assert abs(d0) > mp.mpf(10) ** (-mp.mp.dps // 2), (
        f"taylor_block: Dpol({z0}) is numerically zero - step landed on a "
        f"singular point")
    C = [mp.eye(2)] + [mp.matrix(2, 2) for _ in range(order)]
    for m in range(order):
        acc = mp.matrix(2, 2)
        for j in range(len(ns)):
            if m - j >= 0:
                acc += ns[j] * C[m - j]
        for j in range(1, len(ds)):
            if m - j + 1 >= 0:
                acc -= ds[j] * (m - j + 1) * C[m - j + 1]
        C[m + 1] = acc / (d0 * (m + 1))
    return C


class Continuer:
    """Continues a fundamental matrix along an explicit path, tracking log z."""

    def __init__(self, nmat, dpol, sings, h_factor=4, guard=10):
        self.nmat, self.dpol, self.sings = nmat, dpol, list(sings)
        self.h_factor = h_factor
        # (1/h_factor)**order < 10**-(dps+guard)
        self.order = int(mp.ceil((mp.mp.dps + guard) * mp.log(10)
                                 / mp.log(h_factor))) + 2
        self.steps = 0

    def rho(self, z):
        return min(abs(z - s) for s in self.sings)

    def segment(self, Y, z, z_to, logz):
        """Continue along the straight segment z -> z_to."""
        while True:
            rem = z_to - z
            if abs(rem) == 0:
                break
            h = self.rho(z) / self.h_factor
            if h >= abs(rem):
                step = rem
            else:
                step = rem * (h / abs(rem))
            C = taylor_block(self.nmat, self.dpol, z, self.order)
            w, acc, wp = step, mp.matrix(2, 2), mp.mpf(1)
            for k in range(len(C)):
                acc += C[k] * wp
                wp = wp * w
            Y = acc * Y
            znew = z + step
            logz = logz + mp.log(znew / z)   # |step| <= |z|/4 so the ratio is near 1
            z = znew
            self.steps += 1
        return Y, z, logz

    def arc(self, Y, z, theta_delta, logz, npts=None):
        """Continue along the circular arc |z| = const through angle theta_delta."""
        r = abs(z)
        th0 = mp.arg(z)
        if npts is None:
            # must scale with h_factor, or "step halving" would not halve the
            # step along arcs and the error bar of PREREG 4.1 would be fake
            npts = max(8, int(mp.ceil(abs(theta_delta) * self.h_factor / 2)))
        for i in range(1, npts + 1):
            th = th0 + theta_delta * mp.mpf(i) / npts
            Y, z, logz = self.segment(Y, z, r * mp.expj(th), logz)
        # the chord-wise log tracking above accumulates the true continuous log
        return Y, z, logz

    def path(self, Y, z, waypoints, logz):
        for wp in waypoints:
            Y, z, logz = self.segment(Y, z, wp, logz)
        return Y, z, logz


# ------------------------------------------- formal solution at infinity

def series_div(num, den, order):
    """Power-series division: num/den as a series to given order.

    num[k] 2x2 matrices, den[k] scalars, den[0] != 0.
    """
    assert abs(den[0]) > 0, "series_div: den[0] == 0"
    out = []
    for k in range(order + 1):
        acc = num[k] if k < len(num) else mp.matrix(2, 2)
        acc = mp.matrix(acc)
        for j in range(1, min(k, len(den) - 1) + 1):
            acc -= den[j] * out[k - j]
        out.append(acc / den[0])
    return out


def b_series_at_infinity(nmat, dpol, order):
    """B(z) = sum_{k>=0} Bk z^-k  (requires deg Nmat <= deg Dpol)."""
    m = len(dpol) - 1
    assert len(nmat) - 1 <= m, "deg Nmat > deg Dpol: B unbounded at infinity"
    num = [mp.matrix(2, 2) for _ in range(m + 1)]
    for j in range(len(nmat)):
        num[m - j] = mp.matrix(nmat[j])
    den = [dpol[m - j] if m - j >= 0 else mp.mpf(0) for j in range(m + 1)]
    return series_div(num, den, order)


def formal_at_infinity(nmat, dpol, order, lam_first=None):
    """Formal fundamental solution  Y_f = T F(z) z^L exp(Lam z)  at z = infinity.

    lam_first: if given, the eigenvalue of B_inf that must be placed FIRST, i.e.
    that labels e_1.  PREREG 2.1 fixes e_1 by its exponential factor, and the
    sign of a discriminant is not allowed to decide it.

    Returns (T, Lam, L, F) with F a list of 2x2 matrices, F[0] = I, and
    B_inf = T Lam T^-1 diagonalised with DISTINCT eigenvalues.

    Recurrence (derived in PREREG 4.1):
        [F_m, Lam] = RHS_m,
        RHS_m = sum_{j=1..m} Bt_j F_{m-j} + (m-1) F_{m-1} - F_{m-1} L ,
    off-diagonal entries from RHS_m, and diag(F_{m-1}) fixed by diag(RHS_m) = 0.
    """
    B = b_series_at_infinity(nmat, dpol, order + 1)
    Binf = B[0]
    tr, det = Binf[0, 0] + Binf[1, 1], Binf[0, 0] * Binf[1, 1] - Binf[0, 1] * Binf[1, 0]
    disc = mp.sqrt(tr ** 2 - 4 * det)
    lam1, lam2 = (tr + disc) / 2, (tr - disc) / 2
    if lam_first is not None:
        d1, d2 = abs(lam1 - lam_first), abs(lam2 - lam_first)
        assert min(d1, d2) < abs(lam1 - lam2) / 4, (
            f"formal_at_infinity: lam_first={lam_first} matches neither "
            f"eigenvalue {lam1}, {lam2}")
        if d2 < d1:
            lam1, lam2 = lam2, lam1
    assert abs(lam1 - lam2) > mp.mpf(10) ** (-mp.mp.dps // 3), (
        "formal_at_infinity: B_inf has (numerically) equal eigenvalues - the "
        "irregular type is not of the assumed unramified rank-1 form")

    def eigvec(lam):
        # (Binf - lam I) v = 0
        a, b = Binf[0, 0] - lam, Binf[0, 1]
        c, d = Binf[1, 0], Binf[1, 1] - lam
        v = mp.matrix([b, -a]) if abs(b) + abs(a) >= abs(c) + abs(d) else mp.matrix([-d, c])
        n = mp.sqrt(v[0] ** 2 + v[1] ** 2)
        assert abs(n) > 0, "formal_at_infinity: null eigenvector"
        return v / n

    v1, v2 = eigvec(lam1), eigvec(lam2)
    T = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
    assert abs(mp.det(T)) > mp.mpf(10) ** (-mp.mp.dps // 3), "T singular"
    Ti = T ** -1
    Lam = mp.matrix([[lam1, 0], [0, lam2]])
    resid = Ti * Binf * T - Lam
    assert max(abs(resid[i, j]) for i in range(2) for j in range(2)) < \
        mp.mpf(10) ** (-mp.mp.dps + 20), "diagonalisation of B_inf failed"

    Bt = [Ti * Bk * T for Bk in B]
    L = mp.matrix([[Bt[1][0, 0], 0], [0, Bt[1][1, 1]]])

    F = [mp.eye(2)]
    dl = [lam1, lam2]
    for m in range(1, order + 1):
        # RHS_m with diag(F_{m-1}) temporarily zeroed, to solve for it
        Fprev = mp.matrix(F[m - 1])
        diag_prev = [Fprev[0, 0], Fprev[1, 1]]
        if m >= 2:
            Fprev[0, 0] = Fprev[1, 1] = 0
            # diag(RHS_m) = 0 determines diag(F_{m-1}).  The coefficient of
            # (F_{m-1})_{pp} there is exactly (m-1): the L_pp contributions from
            # Bt_1 F_{m-1} and -F_{m-1} L cancel.
            base = mp.matrix(2, 2)
            for j in range(2, m + 1):
                base += Bt[j] * F[m - j]
            lin = Bt[1] * Fprev + (m - 1) * Fprev - Fprev * L
            for p in range(2):
                # coefficient of diag(F_{m-1})_{pp} in diag(RHS_m)_{pp} is (m-1)
                val = base[p, p] + lin[p, p]
                diag_prev[p] = -val / (m - 1)
            Fprev[0, 0], Fprev[1, 1] = diag_prev[0], diag_prev[1]
            F[m - 1] = Fprev
        acc = mp.matrix(2, 2)
        for j in range(1, m + 1):
            acc += Bt[j] * F[m - j]
        acc += (m - 1) * F[m - 1] - F[m - 1] * L
        Fm = mp.matrix(2, 2)
        for p in range(2):
            for qq in range(2):
                if p != qq:
                    Fm[p, qq] = acc[p, qq] / (dl[qq] - dl[p])
        if m == 1:
            assert abs(acc[0, 0]) < mp.mpf(10) ** (-mp.mp.dps + 20) and \
                abs(acc[1, 1]) < mp.mpf(10) ** (-mp.mp.dps + 20), \
                "formal_at_infinity: L was not diag(Bt_1) after all"
        F.append(Fm)
    return T, Lam, L, F


def formal_value(T, Lam, L, F, z, logz, nterms):
    """T F_N(z) z^L exp(Lam z), optimally truncated at nterms, with a CONTINUOUS
    log z supplied by the caller (never the principal branch)."""
    S = mp.matrix(2, 2)
    zi = mp.mpf(1)
    for k in range(nterms + 1):
        S += F[k] * zi
        zi = zi / z
    zL = mp.matrix([[mp.e ** (L[0, 0] * logz), 0], [0, mp.e ** (L[1, 1] * logz)]])
    eQ = mp.matrix([[mp.e ** (Lam[0, 0] * z), 0], [0, mp.e ** (Lam[1, 1] * z)]])
    return T * S * zL * eQ


def formal_residual(nmat, dpol, T, Lam, L, F, z, nterms):
    """Control C-0: substitute the truncated formal solution back into the ODE.

    Returns the max relative residual of  Y' - B Y  at z, column-normalised.
    The derivative is EXACT, not a finite difference:
        Y = T S z^L e^{Lam z},  Y' = T [S' + S L/z + S Lam] z^L e^{Lam z}.
    """
    logz = mp.log(z)
    S = mp.matrix(2, 2)
    Sp = mp.matrix(2, 2)
    for k in range(nterms + 1):
        S += F[k] * z ** (-k)
        if k >= 1:
            Sp += F[k] * (-k) * z ** (-k - 1)
    zL = mp.matrix([[mp.e ** (L[0, 0] * logz), 0], [0, mp.e ** (L[1, 1] * logz)]])
    eQ = mp.matrix([[mp.e ** (Lam[0, 0] * z), 0], [0, mp.e ** (Lam[1, 1] * z)]])
    Y = T * S * zL * eQ
    dY = T * (Sp + S * L / z + S * Lam) * zL * eQ
    Nz = mp.matrix(2, 2)
    zp = mp.mpf(1)
    for j in range(len(nmat)):
        Nz += nmat[j] * zp
        zp = zp * z
    Dz = mp.mpf(0)
    zp = mp.mpf(1)
    for j in range(len(dpol)):
        Dz += dpol[j] * zp
        zp = zp * z
    R = dY - (Nz / Dz) * Y
    worst = mp.mpf(0)
    for c in range(2):
        scale = max(abs(Y[0, c]), abs(Y[1, c]))
        for r in range(2):
            worst = max(worst, abs(R[r, c]) / scale)
    return worst


# ------------------------------------------------------------------ helpers

def mnorm(M):
    return max(abs(M[i, j]) for i in range(2) for j in range(2))


def normalise_columns(Y):
    """Scale each column to max-modulus 1.  The comparison quantities x1,x2,x3
    are invariant under conjugation by a diagonal matrix (PREREG 2.1, G_m), so
    this is free, and it removes the exp(|tz|) dynamic range entirely."""
    Yn = mp.matrix(Y)
    sc = []
    for c in range(2):
        s = max(abs(Y[0, c]), abs(Y[1, c]))
        assert s > 0, "normalise_columns: null column"
        sc.append(s)
        Yn[0, c] /= s
        Yn[1, c] /= s
    return Yn, sc
