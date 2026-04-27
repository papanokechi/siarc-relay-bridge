"""
SPRINT-W3-SUBLEADING-BALANCE -- Part C
======================================
Direct algebraic test on the CF limits L for Trans families.

C1. PSLQ on  [1, L, L^2, L^3, L^4]  with maxcoeff=10000 -> must reject
    phantom hits (L-coeff = 0).
C2. Pairwise PSLQ on  [1, L_i, L_j, L_i*L_j]  for Trans pairs.
C3. Exploratory: PSLQ on [1, L, sqrt(17), pi, log(2)].
"""

import json
import mpmath
from mpmath import mp, mpf, sqrt, log, pi as mpi, exp as mexp

mp.dps = 300


def trans_families():
    fams = []
    for b1 in (3, 6, 9, 12, 15):
        a2 = -2 * (b1 // 3) ** 2  # = -2 b1^2 / 9 (b1 multiple of 3)
        fams.append((0, 0, a2, 0, b1))
        fams.append((1, 0, a2, 1, b1))
    return fams[:10]


def cf_limit(a0, a1, a2, b0, b1, N=500):
    p_prev, p_curr = mpf(1), mpf(0)
    q_prev, q_curr = mpf(0), mpf(1)
    for n in range(1, N + 1):
        bn = mpf(b1) * n + mpf(b0)
        an = mpf(a2) * n * n + mpf(a1) * n + mpf(a0)
        p_nxt = bn * p_curr - an * p_prev
        q_nxt = bn * q_curr - an * q_prev
        p_prev, p_curr = p_curr, p_nxt
        q_prev, q_curr = q_curr, q_nxt
    if q_curr == 0:
        return None
    return p_curr / q_curr


def phantom_hit(rel, target_index):
    """rel is a list of integer coefficients in same order as basis.
    target_index is the index of the target value (the thing we wanted
    to express).  Phantom hit: rel[target_index] = 0."""
    if rel is None:
        return False
    return rel[target_index] == 0


def main():
    print("="*84)
    print("Part C -- direct algebraic identification of CF limits L")
    print(f"          mp.dps = {mp.dps},   N (iterations) = 500")
    print("="*84)

    fams = trans_families()
    Ls = []
    for i, fam in enumerate(fams, 1):
        L = cf_limit(*fam)
        Ls.append(L)
        print(f"  T{i:02d}  fam={fam}    L = {mpmath.nstr(L, 30)}")
    print()

    # ----- C1.  PSLQ against {1, L, L^2, L^3, L^4} with maxcoeff=10000 -----
    print("="*84)
    print("C1.  PSLQ on  [1, L, L^2, L^3, L^4]  with maxcoeff=10000")
    print("     Phantom hit rule:  reject relations with L-coeff = 0.")
    print("="*84)
    c1_results = []
    for i, L in enumerate(Ls, 1):
        basis = [mpf(1), L, L*L, L**3, L**4]
        try:
            rel = mpmath.pslq(basis, tol=mpf(10)**(-40), maxcoeff=10000)
        except Exception as e:
            rel = None
        # target index: we are testing whether L is algebraic; phantom hit
        # if all of [L, L^2, L^3, L^4] coefficients are zero.
        if rel is not None and all(rel[k] == 0 for k in (1, 2, 3, 4)):
            tag = "PHANTOM_HIT_REJECTED"
        elif rel is None:
            tag = "no relation found"
        else:
            tag = "**ALGEBRAIC HIT**"
        c1_results.append((i, rel, tag))
        print(f"  T{i:02d}  PSLQ = {rel}    -> {tag}")
    print()

    # ----- C2.  Pairwise PSLQ on (L_i, L_j) for Trans pairs ---------------
    print("="*84)
    print("C2.  Pairwise PSLQ on  [1, L_i, L_j, L_i*L_j, L_i^2, L_j^2]   (maxcoeff=10000)")
    print("="*84)
    c2_results = []
    for i in range(len(Ls)):
        for j in range(i + 1, len(Ls)):
            Li, Lj = Ls[i], Ls[j]
            basis = [mpf(1), Li, Lj, Li * Lj, Li * Li, Lj * Lj]
            try:
                rel = mpmath.pslq(basis, tol=mpf(10)**(-40), maxcoeff=10000)
            except Exception:
                rel = None
            # Phantom hit: all "non-constant" coefs zero
            if rel is not None and all(rel[k] == 0 for k in range(1, 6)):
                tag = "PHANTOM"
            elif rel is None:
                tag = "none"
            else:
                tag = "HIT"
                c2_results.append((i + 1, j + 1, rel))
            if tag == "HIT":
                print(f"  T{i+1:02d} - T{j+1:02d}:  PSLQ = {rel}  -> {tag}")
    if not c2_results:
        print("  (no non-phantom relations found)")
    print()

    # ----- C3.  Exploratory: PSLQ on [1, L, sqrt(17), pi, log(2)] ---------
    print("="*84)
    print("C3.  Exploratory PSLQ on  [1, L, sqrt(17), pi, log(2)]")
    print("="*84)
    c3_results = []
    s17 = sqrt(mpf(17))
    pi_ = mpi
    ln2 = log(mpf(2))
    for i, L in enumerate(Ls, 1):
        basis = [mpf(1), L, s17, pi_, ln2]
        try:
            rel = mpmath.pslq(basis, tol=mpf(10)**(-40), maxcoeff=10000)
        except Exception:
            rel = None
        if rel is not None and rel[1] == 0:
            tag = "PHANTOM (L-coeff = 0)"
        elif rel is None:
            tag = "none"
        else:
            tag = "**HIT**"
        c3_results.append((i, rel, tag))
        print(f"  T{i:02d}  PSLQ = {rel}    -> {tag}")
    print()

    # ----- save -----
    out = {
        "L_values": [str(L) for L in Ls],
        "C1": [{"i": i, "rel": rel, "tag": tag} for (i, rel, tag) in c1_results],
        "C2": [{"i": i, "j": j, "rel": rel} for (i, j, rel) in c2_results],
        "C3": [{"i": i, "rel": rel, "tag": tag} for (i, rel, tag) in c3_results],
    }
    with open("direct_algebraic.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print("Wrote direct_algebraic.json")

    # ----- summary verdict -----
    any_C1_hit = any(tag == "**ALGEBRAIC HIT**" for (_, _, tag) in c1_results)
    any_C2_hit = bool(c2_results)
    any_C3_hit = any(tag == "**HIT**" for (_, _, tag) in c3_results)
    print()
    print("="*84)
    print("Part C verdict")
    print("="*84)
    print(f"  C1 (algebraic, single L):  {'POSITIVE' if any_C1_hit else 'NEGATIVE'}")
    print(f"  C2 (pairwise):             {'POSITIVE' if any_C2_hit else 'NEGATIVE'}")
    print(f"  C3 (mixed transcendental): {'POSITIVE' if any_C3_hit else 'NEGATIVE'}")


if __name__ == "__main__":
    main()
