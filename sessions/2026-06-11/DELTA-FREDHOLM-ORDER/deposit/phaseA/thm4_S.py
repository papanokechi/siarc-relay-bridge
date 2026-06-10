"""
Theorem-4 soft spot: S = sum_{n>=2} u_n,  u_n = 1/(b(n-1) b(n)), b(k)=A k^2+B k+C.
Plemelj-Smithies convergence is stated to rest on S < 1.

(1) S(1,0,1) high-precision value + confirm < 1 (closed form: P0 digamma form).
(2) Clean family-wide SUFFICIENT bound (telescoping):
       u_k = 1/(b(k-1)b(k)) = [1/(b(k)-b(k-1))] (1/b(k-1) - 1/b(k)),
       b(k)-b(k-1) = A(2k-1)+B >= 3A+B  for k>=2  (increasing),
    => S <= 1/((3A+B) b(1)) = 1/((3A+B)(A+B+C)).
    Sufficient condition for S<1:  (3A+B)(A+B+C) > 1.
(3) Falsification: S is NOT < 1 universally -- a degenerate triple (small A) gives S>1.
(4) Integer-regime upgrade: on the integer lattice A,C>=1, B>=0 the bound denominator
    (3A+B)(A+B+C) >= (3*1)(1+0+1) = 6, so S <= 1/6 < 1 UNCONDITIONALLY; a fast float
    grid over A,C in 1..5, B in 0..4 confirms every S <= 1/6 with the max at (1,0,1).
"""
import json, hashlib
from mpmath import mp, mpf, psi, inf, nsum

mp.dps = 80


def S_value(A, B, C, terms=300000):
    A, B, C = mpf(A), mpf(B), mpf(C)
    b = lambda k: A * k * k + B * k + C
    # direct sum with analytic tail (u_n ~ 1/(A^2 n^4); tail ~ (1/A^2) * zeta-ish)
    part = mp.fsum([1 / (b(n - 1) * b(n)) for n in range(2, terms)])
    tail = nsum(lambda n: 1 / (b(n - 1) * b(n)), [terms, inf])
    return part + tail


def bound(A, B, C):
    A, B, C = mpf(A), mpf(B), mpf(C)
    gap = 3 * A + B          # min of b(k)-b(k-1) over k>=2
    b1 = A + B + C
    return 1 / (gap * b1) if gap > 0 and b1 > 0 else None


def grid_scan_integer_family(Amax=5, Bmax=4, Cmax=5, Nmax=50000):
    """Fast float64 scan confirming S <= 1/6 uniformly on the integer lattice
    A,C in 1..Amax, B in 0..Bmax. Returns the grid summary (worst case + uniformity)."""
    one_sixth = 1.0 / 6.0
    worst_S, worst_triple = 0.0, None
    all_below = True
    count = 0
    for A in range(1, Amax + 1):
        for B in range(0, Bmax + 1):
            for C in range(1, Cmax + 1):
                bf = lambda k: A * k * k + B * k + C
                s = 0.0
                for n in range(2, Nmax):
                    s += 1.0 / (bf(n - 1) * bf(n))
                s += 1.0 / (3.0 * A * A * Nmax ** 3)   # analytic tail, u_n ~ 1/(A^2 n^4)
                count += 1
                if s > one_sixth + 1e-9:
                    all_below = False
                if s > worst_S:
                    worst_S, worst_triple = s, (A, B, C)
    return {"n_triples": count,
            "lattice": f"A,C in 1..{Amax}, B in 0..{Bmax}",
            "analytic_min_denominator": (3 * 1 + 0) * (1 + 0 + 1),  # = 6, at (1,0,1)
            "uniform_bound_1_over_6": one_sixth,
            "all_S_le_1_over_6": bool(all_below),
            "max_S": worst_S,
            "argmax_triple": worst_triple}


def closed_form_1_0_1():
    # b(k)=k^2+1 has roots {i,-i} shifted; u_n=1/(((n-1)^2+1)(n^2+1)).
    # 1/(b(n-1)b(n)) = 1/(2n-1) (1/b(n-1) - 1/b(n)); summed via digamma of the four roots
    # of the pair. Use the standard residue/digamma closed form (cross-check to direct sum).
    # S = (1/2) Re[ psi(2 - i) - psi(1 - i) ] / Im-bookkeeping is delicate; we instead
    # cross-check the high-precision direct value against P0's certified digits.
    return None


if __name__ == "__main__":
    triples = [("(1,0,1) running family", 1, 0, 1),
               ("(1,0,5)", 1, 0, 5),
               ("(1,3,2)", 1, 3, 2),
               ("(2,1,3)", 2, 1, 3),
               ("(0.01,0,1) degenerate small-A", mpf(1) / 100, 0, 1)]
    P0_S = mpf("0.13066961898743246965362031790000019617826250656153")
    res = []
    for name, A, B, C in triples:
        S = S_value(A, B, C)
        bd = bound(A, B, C)
        suff = (3 * mpf(A) + mpf(B)) * (mpf(A) + mpf(B) + mpf(C))
        ok = S < 1
        print(f"\n{name}: A={A},B={B},C={C}")
        print(f"  S            = {mp.nstr(S, 30)}")
        print(f"  bound 1/((3A+B)(A+B+C)) = {mp.nstr(bd,12) if bd else 'n/a'}"
              f"  (>=S: {bd is not None and bd >= S})")
        print(f"  sufficient (3A+B)(A+B+C) = {mp.nstr(suff,8)}  (>1 => S<1 certified: {suff>1})")
        print(f"  S < 1 : {ok}")
        if name.startswith("(1,0,1)"):
            print(f"  match P0 certified value (44 digits): |S-P0| = {mp.nstr(abs(S-P0_S),5)}")
        res.append({"name": name, "A": float(A), "B": float(B), "C": float(C),
                    "S": mp.nstr(S, 40), "bound": (mp.nstr(bd, 16) if bd else None),
                    "sufficient_prod": mp.nstr(suff, 12), "S_lt_1": bool(ok)})

    grid = grid_scan_integer_family()
    print("\nInteger-family grid scan (A,C in 1..5, B in 0..4):")
    print(f"  {grid['n_triples']} triples; all S <= 1/6 : {grid['all_S_le_1_over_6']}")
    print(f"  max S = {grid['max_S']:.10f} at {grid['argmax_triple']}"
          f"  (uniform bound 1/6 = {grid['uniform_bound_1_over_6']:.10f};"
          f" analytic min denominator = {grid['analytic_min_denominator']})")

    out = {"dps": mp.dps, "results": res,
           "integer_grid": grid,
           "sufficient_condition": "(3A+B)(A+B+C) > 1  =>  S <= 1/((3A+B)(A+B+C)) < 1",
           "integer_regime": "For A,C in Z>=1, B in Z>=0 the denominator (3A+B)(A+B+C) >= 6, "
                             "so S <= 1/6 < 1 UNCONDITIONALLY (max S on the grid is at the "
                             "running family (1,0,1)).",
           "note": "S<1 is NOT universal for real coefficients: degenerate small-A triples "
                   "give S>1 (e.g. (0.01,0,1): S=6.84). Theorem 4 is therefore stated "
                   "unconditionally on the integer family (uniform S<=1/6) and conditionally "
                   "via (3A+B)(A+B+C)>1 in general."}
    js = json.dumps(out, indent=2)
    with open("out/thm4_S_result.json", "w", newline="\n") as f:
        f.write(js)
    print("\nsha256(result json) =", hashlib.sha256(js.encode()).hexdigest())
