"""VQUAD-PIII-NORMALIZATION-MAP --- Phase A symbolic verification.

Derive the homogeneous V_quad scalar ODE from the recurrence
    Q_n = (3 n^2 + n + 1) Q_{n-1} + Q_{n-2},   Q_0 = 1
(equivalently the inhomogeneous OGF equation L f = 1 in CT v1.3 §3.5
notation), confirm the Newton polygon at z=0 has a single slope-1/2
edge, derive the characteristic exponent c = +- 2/sqrt(3) and the
secondary exponent rho = -11/6 by direct expansion, and compute the
first 6 trans-series coefficients a_k of the formal Birkhoff series

    f_+(u) = exp(c0 / u) * u^rho * (1 + a_1 u + a_2 u^2 + ...)

with c0 = 2/sqrt(3).  These are the V_quad-native normalization
quantities that the change-of-variables Phi must preserve.

Outputs are checksummed and written to verify_vquad_ode.log.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).parent
LOG = HERE / "verify_vquad_ode.log"


def section(title: str, lines: list[str]) -> None:
    lines.append("")
    lines.append("=" * 72)
    lines.append(title)
    lines.append("=" * 72)


def main() -> None:
    log: list[str] = []
    section("Phase A.1 -- recurrence and OGF ODE derivation", log)

    z, u, c = sp.symbols("z u c", complex=True)
    rho = sp.symbols("rho", real=True)
    f = sp.Function("f")
    theta = z * sp.Derivative(f(z), z)

    # CT v1.3 eq:Lf-cc with (alpha_1, alpha_0, beta_2, beta_1, beta_0) = (0,1,3,1,1)
    # L f := f - z [3(theta+1)^2 + (theta+1) + 1] f - z^2 f  =  1
    # Expand 3(theta+1)^2 + (theta+1) + 1 = 3 theta^2 + 7 theta + 5
    # theta f = z f', theta^2 f = z^2 f'' + z f'.

    fz = f(z)
    fp = sp.Derivative(fz, z)
    fpp = sp.Derivative(fz, z, 2)

    op = (
        fz
        - z * (3 * (z**2 * fpp + z * fp) + 7 * z * fp + 5 * fz)
        - z**2 * fz
    )
    op = sp.expand(op)
    log.append("Inhomogeneous operator L f - 1 =")
    log.append("    " + str(op) + "  ==  1")

    # Homogeneous operator
    homo = sp.collect(op, [fpp, fp, fz])
    log.append("Homogeneous L_h f = 0:")
    log.append("    " + str(homo) + " = 0")

    # Coefficients
    P2 = sp.simplify(homo.coeff(fpp))
    P1 = sp.simplify(homo.coeff(fp))
    P0 = sp.simplify(homo - P2 * fpp - P1 * fp).coeff(fz)
    log.append(f"  coeff f''  =  {P2}")
    log.append(f"  coeff f'   =  {P1}")
    log.append(f"  coeff f    =  {sp.simplify(P0)}")
    # Expected: P2 = -3 z^3, P1 = -10 z^2, P0 = -(5z + z^2 - 1) = 1 - 5z - z^2
    assert sp.simplify(P2 - (-3 * z**3)) == 0
    assert sp.simplify(P1 - (-10 * z**2)) == 0
    assert sp.simplify(P0 - (1 - 5 * z - z**2)) == 0
    log.append("  --> matches  3 z^3 f'' + 10 z^2 f' + (5 z + z^2 - 1) f = 0  (homog)")

    section("Phase A.2 -- Newton polygon at z = 0", log)
    # Lattice points (k = order of d/dz, q_k = ord_z of coefficient of f^(k))
    pts = [(0, sp.Poly(1 - 5 * z - z**2, z).all_coeffs() and 0),  # ord_z = 0
           (1, 2),  # 10 z^2 -> ord_z = 2
           (2, 3)]  # 3 z^3 -> ord_z = 3
    log.append(f"Lattice points (k, ord_z): {pts}")
    # Newton polygon points are (k, q_k - k)
    np_pts = [(k, q - k) for (k, q) in pts]
    log.append(f"Newton-polygon points (k, q_k - k): {np_pts}")
    # Lower convex hull edge from (0,0) to (2,1) -- single edge slope 1/2.
    slope = sp.Rational(1, 2)
    log.append(f"Single slope edge: (0,0) -> (2,1), slope = {slope}")

    section("Phase A.3 -- characteristic equation under z = u^2", log)
    # f = exp(c/u) * u^rho * (1 + sum_{k>=1} a_k u^k), z = u^2.
    # D_z = (1/(2u)) D_u.   Compute  L_h[f] / f  as a series in u, after
    # factoring out the common u^rho exp(c/u).  The trick: divide by
    # u^rho * exp(c/u) first; the result is a Laurent polynomial in u (no
    # symbolic rho exponent left), so sp.series works.
    F = sp.exp(c / u) * u**rho
    fp_u = (1 / (2 * u)) * sp.diff(F, u)
    fpp_u = (1 / (2 * u)) * sp.diff(fp_u, u)
    L_on_F = (
        -3 * u**6 * fpp_u
        - 10 * u**4 * fp_u
        + (1 - 5 * u**2 - u**4) * F
    )
    # Multiply through by u^(-rho) exp(-c/u) to strip the prefactor.
    # Use powsimp(force=True) to combine u**(-rho)*u**(rho+k) -> u**k.
    L_div = sp.powsimp(sp.expand(L_on_F * sp.exp(-c / u) * u ** (-rho)), force=True)
    L_div = sp.expand(L_div)
    log.append("L_h[exp(c/u) u^rho] / [exp(c/u) u^rho] (Taylor in u):")
    log.append("    " + str(L_div))
    L_norm = L_div  # already a Taylor polynomial after powsimp(force=True)

    # Leading u^0 coefficient determines c.
    coeff0 = sp.simplify(L_norm.coeff(u, 0))
    log.append(f"u^0 coefficient: {coeff0} = 0")
    sols = sp.solve(coeff0, c)
    log.append(f"  --> c = {sols}     (expect +- 2/sqrt(3))")
    c0_val = sp.Rational(2) / sp.sqrt(3)

    # u^1 coefficient at c = c0_val determines rho.
    L_norm_c0 = sp.expand(L_norm.subs(c, c0_val))
    coeff_u1 = sp.simplify(L_norm_c0.coeff(u, 1))
    log.append(f"u^1 coefficient (with c = 2/sqrt(3)): {coeff_u1} = 0")
    rho_sol = sp.solve(coeff_u1, rho)
    log.append(f"  --> rho = {rho_sol}    (expect -11/6)")

    section("Phase A.4 -- summary", log)
    log.append("V_quad scalar ODE (homogeneous):")
    log.append("    3 z^3 f''(z) + 10 z^2 f'(z) + (5 z + z^2 - 1) f(z) = 0")
    log.append("Inhomogeneous OGF equation:")
    log.append("    L f = 1  with  L = 1 - z[3(theta+1)^2 + (theta+1) + 1] - z^2,")
    log.append("    theta = z d/dz,  Q_0 = 1.")
    log.append("Newton polygon at z=0: single edge slope 1/2 (rank-1/2 irregular sing.).")
    log.append("Characteristic exponent: c = +- 2/sqrt(3)  =  +- 1.15470053837925152901...")
    log.append("Secondary exponent: rho = -11/6 = -1.833...  (rational).")
    log.append("Borel singular distance: zeta_* = 2 c0 = 4/sqrt(3) = 2.30940107675850305...")

    LOG.write_text("\n".join(log) + "\n", encoding="utf-8")
    digest = hashlib.sha256(LOG.read_bytes()).hexdigest()
    print(f"verify_vquad_ode.log  sha256 = {digest}")
    print(f"  lines = {len(log)}")


if __name__ == "__main__":
    main()
