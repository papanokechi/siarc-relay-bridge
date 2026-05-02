"""Symbolic derivation of the Birkhoff formal series recurrence
for d=2 PCF families.

ODE for OGF f(z) = sum_n Q_n z^n:
    alpha z^3 f''
    + [(3 alpha + beta) z^2 + delta z^3] f'
    + [(alpha + beta + gamma) z + (2 delta + epsilon) z^2 - 1] f
    + Q0 = 0

Substitute z = u^2 and the formal Birkhoff ansatz
    f(u) = exp(c/u) * u^rho * S(u),  S(u) = 1 + a_1 u + a_2 u^2 + ...

The leading u^0 vanishing gives c^2 = 4/alpha (so c = +/- 2/sqrt(alpha))
and the u^1 vanishing gives rho = -3/2 - beta/alpha.

Goal: extract polynomial-in-k coefficients C_diag(k), C_1(k), C_2(k),
C_3(k) such that the recurrence reads

    C_diag(k) * a_k
       = C_1(k) * a_{k-1}
       + C_2(k) * a_{k-2}
       + C_3(k) * a_{k-3}.

Validation: for V_quad (alpha=3, beta=1, gamma=1, delta=0, epsilon=1)
the existing CC-MEDIAN-RESURGENCE-EXECUTE recurrence is

    (3 c / 2) k * a_k = (-coeff_km1) a_{k-1} + a_{k-3},
    coeff_km1 = -5 - 7 p / 2 - 3 p^2 / 4,   p = rho + k - 1.

We must reproduce that.
"""
from __future__ import annotations

import sympy as sp


def derive():
    u, k = sp.symbols("u k", real=True)
    a = sp.Function("a")
    alpha, beta, gamma, delta, epsilon = sp.symbols(
        "alpha beta gamma delta epsilon", real=True
    )
    c, rho = sp.symbols("c rho", real=True)

    # f(u) = exp(c/u) u^rho S(u). Build operator acting on S only by
    # working with the OGF ODE expressed in u via z = u^2.
    z = u ** 2
    # Differentials wrt z in terms of u.
    # df/dz = (1/(2u)) df/du
    # d2f/dz2 = (1/(4u^2)) (d2f/du2 - df/du / u)

    P2 = alpha * z ** 3
    P1 = (3 * alpha + beta) * z ** 2 + delta * z ** 3
    P0 = (alpha + beta + gamma) * z + (2 * delta + epsilon) * z ** 2 - 1

    # Build f(u) = exp(c/u) u^rho S(u) symbolically; compute f, f' (wrt z),
    # f'' (wrt z), substitute, divide by exp(c/u) u^rho, expand in u.

    # We keep S as a generic symbol-function; we'll truncate as a series.
    # To handle arbitrary order recursively, we expand in u to order
    # high enough to extract the coefficient relations.
    N = 8  # truncation order for derivation; the recurrence coefficients
           # become stable after order ~5 due to the 4-term stencil.

    # S = 1 + sum_{j=1..N} a_j u^j
    a_syms = [sp.Symbol(f"a{j}") for j in range(N + 1)]
    a_syms[0] = sp.Integer(1)
    S = sum(a_syms[j] * u ** j for j in range(N + 1))

    # f(u) = E(u) * G(u) * S(u), with E=exp(c/u), G = u^rho.
    # Compute f' and f'' wrt z via chain rule using u-derivatives.
    G = sp.exp(c / u) * u ** rho * S

    Gu = sp.diff(G, u)
    Guu = sp.diff(Gu, u)

    # f'_z = Gu / (2 u)
    fz = Gu / (2 * u)
    # f''_z = (Guu - Gu / u) / (4 u^2)
    fzz = (Guu - Gu / u) / (4 * u ** 2)

    LHS = P2 * fzz + P1 * fz + P0 * G
    # Divide by exp(c/u) * u^rho (no zeros for u != 0).
    LHS = sp.simplify(LHS / (sp.exp(c / u) * u ** rho))
    # Now LHS depends on u and the a_j; expand as Laurent series in u
    # and extract coefficient of each u^n.

    LHS = sp.expand(LHS)

    # Apply leading-term conditions: c^2 = 4/alpha, rho = -3/2 - beta/alpha.
    # This kills u^{-?} singularities in LHS at the symbolic level if we
    # substitute c symbolically? Actually LHS has powers like u^0, u^1, ...
    # (after dividing by u^rho the radial factor becomes u^0). The small-u
    # expansion still has singular powers from the exp factor differentiation.
    # Let's just substitute the leading-condition relations later when
    # collecting.

    # Collect coefficients of u^n.
    LHS_series = sp.series(LHS, u, 0, N + 4).removeO()

    coeffs = {}
    for n in range(-2, N + 1):
        coeffs[n] = sp.expand(LHS_series.coeff(u, n))

    print("Raw coefficient of u^n (un-substituted):")
    for n in sorted(coeffs):
        if coeffs[n] != 0:
            print(f"  [u^{n}]:", sp.simplify(coeffs[n]))

    # Apply c^2 -> 4/alpha (i.e., alpha*c^2 -> 4) and rho -> -3/2 - beta/alpha.
    # Then constant term and u^1 term should vanish.
    rho_val = sp.Rational(-3, 2) - beta / alpha
    print()
    print("Substituting rho = -3/2 - beta/alpha and alpha*c^2 = 4:")
    for n in sorted(coeffs):
        e = coeffs[n].subs(rho, rho_val)
        # Replace alpha*c^2 with 4 (Groebner-style by hand)
        # Substitute c**2 = 4/alpha; but to keep recurrence clean we keep c.
        e = e.subs(c ** 2, 4 / alpha)
        e = sp.simplify(sp.expand(e))
        coeffs[n] = e
        print(f"  [u^{n}] =", e)

    # Now for n>=2, the equation [u^n] = 0 expresses a relation among
    # a_{n-1}, a_{n-2}, a_{n-3}, a_{n-4} (the "diagonal" being a_{n-1}
    # because the stencil shifts as derived in the manual analysis).
    # Print in the form: linear in a_j.
    print()
    print("Recurrence form (coeff on each a_j at order [u^n]):")
    for n in range(2, N + 1):
        e = coeffs[n]
        row = {}
        for j in range(0, N + 1):
            cf = sp.expand(e.coeff(a_syms[j])) if isinstance(a_syms[j], sp.Symbol) else sp.Integer(0)
            if cf != 0:
                row[j] = cf
        print(f"  [u^{n}] :")
        for j, cf in sorted(row.items()):
            print(f"      a_{j} : {sp.simplify(cf)}")

    # V_quad sanity: alpha=3, beta=1, gamma=1, delta=0, epsilon=1.
    print()
    print("V_quad numerical check:")
    subs_vq = {alpha: 3, beta: 1, gamma: 1, delta: 0, epsilon: 1,
               c: 2 / sp.sqrt(3)}
    for n in range(2, 6):
        e = coeffs[n].subs(subs_vq)
        e = sp.simplify(e)
        print(f"  [u^{n}] (V_quad) =", e)


if __name__ == "__main__":
    derive()
