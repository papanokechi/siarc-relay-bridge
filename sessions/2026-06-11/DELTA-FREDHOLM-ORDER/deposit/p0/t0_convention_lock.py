#!/usr/bin/env python3
"""
DELTA-FREDHOLM-P0  --  PHASE T0  --  CONVENTION LOCK (hard gate)

Object under test:  (A,B,C)=(1,0,1), b(k)=k^2+1, u_n = 1/(b(n-1) b(n)), n>=2.
R_M(lam) = weighted independence polynomial of the path on vertices {2..M},
           vertex i carrying weight lam*u_i  (no two consecutive vertices chosen).

Conjectured finite identity (the index offset / squaring convention is what we lock):
        R(lam)^2 = det(I + lam T^2),
where T is the symmetric tridiagonal path-adjacency matrix with 0 diagonal and
off-diagonal entries sqrt(u_.).

KEY EXACT FACT used to make the determinant rational:
    det(I + lam T^2) = det(I + i sqrt(lam) T) * det(I - i sqrt(lam) T) = P_s(lam)^2,
    P_0=P_1=1,  P_k = P_{k-1} + lam * w_{k-1}^2 * P_{k-2},  w_{k-1}^2 = u_{(k-1)+off}.
So the determinant is computed EXACTLY in Fraction arithmetic via P_s, and the
identity R^2 = det reduces to the (rational) test R_M = P_s.

We brute-force R_M(lam) by INDEPENDENT subset enumeration (not the recurrence),
cross-anchor R_M(1) against the standard continuant q_M / prod b(k), then sweep
(matrix size s in {M,M+1,M+2}) x (weight offset in {0,1,2}) and find the unique
convention with residual < 1e-80 for every M in 1..12 and 5 random rationals lam.

Usage:  python t0_convention_lock.py [dps]
"""
import os, sys, json, hashlib, itertools, random
from fractions import Fraction
from mpmath import mp, mpf, sqrt as mp_sqrt, matrix, det as mp_det, log10, mpc, fabs

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 120
mp.dps = DPS
os.makedirs("out", exist_ok=True)

def b(k):
    return k*k + 1

def u(n):
    # u_n = 1/(b(n-1) b(n)); defined as a Fraction for any integer n (b(0)=1).
    return Fraction(1, b(n-1)*b(n))

# ---------------------------------------------------------------- brute force R
def R_brute(M, lam):
    """R_M(lam) by independent-set enumeration on vertices {2..M}. lam: Fraction."""
    verts = list(range(2, M+1))            # {2,...,M};  empty if M<2
    n = len(verts)
    total = Fraction(0)
    for mask in range(1 << n):
        sel = [verts[i] for i in range(n) if (mask >> i) & 1]
        ok = all(sel[t+1] != sel[t] + 1 for t in range(len(sel)-1))
        if not ok:
            continue
        prod = Fraction(1)
        for v in sel:
            prod *= lam * u(v)
        total += prod
    return total

# ----------------------------------------------------------------- continuant
def R_cont(M):
    """R_M(1) via continuant q_M / prod_{k=1..M} b(k), q_0=1,q_1=2,q_n=b(n)q_{n-1}+q_{n-2}."""
    if M <= 0:
        return Fraction(1)
    q2, q1 = Fraction(1), Fraction(2)      # q_0, q_1
    if M == 1:
        qM = q1
    else:
        for k in range(2, M+1):
            qk = b(k)*q1 + q2
            q2, q1 = q1, qk
        qM = q1
    denom = 1
    for k in range(1, M+1):
        denom *= b(k)
    return Fraction(qM, denom)

# --------------------------------------------------- exact determinant via P_s
def P_det(s, weight_offset, lam):
    """P_s(lam) = det(I + i sqrt(lam) T)  (rational), with w_{k-1}^2 = u_{(k-1)+weight_offset}.
       det(I + lam T^2) = P_s^2."""
    if s <= 0:
        return Fraction(1)
    Pp2, Pp1 = Fraction(1), Fraction(1)    # P_0, P_1
    if s == 1:
        return Pp1
    for k in range(2, s+1):
        wsq = u((k-1) + weight_offset)     # w_{k-1}^2
        Pk = Pp1 + lam * wsq * Pp2
        Pp2, Pp1 = Pp1, Pk
    return Pp1

# --------------------------------------- mpmath determinant of explicit I+lam T^2
def det_explicit(s, weight_offset, lam):
    """det(I + lam T^2) built explicitly with sqrt(u) entries, mpmath at current dps."""
    T = matrix(s, s)
    for j in range(1, s):                  # off-diagonal index j = 1..s-1
        w = mp_sqrt(mpf(u((j) + weight_offset).numerator) / mpf(u((j)+weight_offset).denominator))
        T[j-1, j] = w
        T[j, j-1] = w
    I = matrix(s, s)
    for i in range(s):
        I[i, i] = 1
    lam_mp = mpf(lam.numerator) / mpf(lam.denominator)
    M2 = I + lam_mp * (T * T)
    return mp_det(M2)

def frac_to_mpf(fr):
    return mpf(fr.numerator) / mpf(fr.denominator)

# ----------------------------------------------------------------------- main
def main():
    report = {"task_id": "DELTA-FREDHOLM-P0", "phase": "T0", "dps": DPS}

    # (1) cross-anchor: brute R_M(1) == continuant, M=1..12, exact + 50-digit display
    anchor = []
    for M in range(1, 13):
        rb = R_brute(M, Fraction(1))
        rc = R_cont(M)
        exact_equal = (rb == rc)
        anchor.append({"M": M, "exact_equal": exact_equal,
                       "R_M_1_50dig": mp.nstr(frac_to_mpf(rb), 50)})
        assert exact_equal, f"continuant anchor FAILED at M={M}"
    report["anchor_continuant_all_exact"] = all(a["exact_equal"] for a in anchor)
    report["anchor"] = anchor

    # (2) convention sweep
    rng = random.Random(20260610)
    lams = []
    while len(lams) < 5:
        p = rng.randint(1, 19); q = rng.randint(10, 23)
        fr = Fraction(p, q)
        if 0 < fr <= 2 and fr not in lams:
            lams.append(fr)
    report["random_lambdas"] = [str(l) for l in lams]

    candidates = []
    for s_off in (0, 1, 2):
        for w_off in (0, 1, 2):
            candidates.append((s_off, w_off))

    sweep = {}
    passing = []
    for (s_off, w_off) in candidates:
        key = f"size=M+{s_off},woff={w_off}"
        worst_resid = mpf(0)
        all_exact = True
        for M in range(1, 13):
            s = M + s_off
            for lam in lams:
                Rm = R_brute(M, lam)                 # target R_M(lam)
                Pe = P_det(s, w_off, lam)            # candidate P_s(lam)  (== sqrt(det))
                if Pe != Rm:
                    all_exact = False
                # mpmath residual of the squared identity R_M^2 = det(I+lam T^2)
                det_mp = det_explicit(s, w_off, lam)
                resid = fabs(det_mp - frac_to_mpf(Rm)**2)
                if resid > worst_resid:
                    worst_resid = resid
        sweep[key] = {"all_exact_RM_eq_Ps": all_exact,
                      "worst_resid_squared_identity": mp.nstr(worst_resid, 6),
                      "worst_resid_lt_1e-80": bool(worst_resid < mpf(10)**(-80))}
        if all_exact and worst_resid < mpf(10)**(-80):
            passing.append(key)
    report["sweep"] = sweep
    report["passing_conventions"] = passing

    if len(passing) == 0:
        report["verdict"] = "HALT-T0"
    elif len(passing) > 1:
        report["verdict"] = "HALT-T0-AMBIG"
    else:
        report["verdict"] = "T0-PASS"
        report["locked_convention"] = {
            "matrix_size": "s = M  (M = upper vertex index of R_M on {2..M})",
            "off_diagonal_entry": "T[j-1,j]=T[j,j-1]=sqrt(u_{j+1}), j=1..M-1",
            "identity": "R_M(lam)^2 = det(I + lam*T^2);  equivalently R_M = det(I + i*sqrt(lam)*T)",
            "note_problem_T_M": ("problem's T_M has size M+1 (off-diagonals sqrt(u_2..u_{M+1})), "
                                 "so det(I+lam T_M^2) = R_{M+1}(lam)^2 (index +1).")}

    # hashes
    with open(__file__, "rb") as fh:
        report["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(report, indent=2)
    print(out)
    with open("out/t0_result.json", "w") as fh:
        fh.write(out)
    report_no_self = dict(report); report_no_self.pop("script_sha256", None)
    print("OUTPUT_HASH", hashlib.sha256(json.dumps(report_no_self, sort_keys=True).encode()).hexdigest())

if __name__ == "__main__":
    main()
