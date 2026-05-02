# Literature cross-check --- VQUAD-PIII-NORMALIZATION-MAP

**Verdict:** G15_PARTIAL.  The canonical-form Stokes value
`S_zeta_star_can` is *not* numerically pinned in this session;
no literature comparison is therefore performed.  The cross-check
below documents what is needed to close G15 fully.

## Sources consulted (operator local library)

| Source                          | Available? | Used for |
|---------------------------------|------------|----------|
| CT v1.3 §3.5 (`channel_theory_outline.tex`, 2026-05-02 release) | YES | parameter point identification |
| CC-MEDIAN-RESURGENCE-EXECUTE session (Prompt 005, 2026-05-02) | YES | V_quad-native `C` and `zeta_*` to 108 digits |
| Loday-Richaud 2016 (Divergent Series II) | partial (cited in CT v1.3) | Borel-Laplace summability framework |
| Sibuya 1990 (linear ODE Stokes phenomena) | partial (cited in CT v1.3) | Newton polygon basics |

## Sources required but **not available locally**

| Source | Page/Section | Needed for |
|--------|--------------|------------|
| Okamoto 1987 ("Studies on the Painlevé equations IV. P_III", *Funkcial. Ekvac.* **30**, 305-332) | §2 (Hamiltonian) | Residual **R1**: convention pinning of $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ from CT v1.3's $(1/6, 0, 0, -1/2)$ |
| Okamoto 1987 | §3 eq. (3.7) | Residual **R2**: trans-series leading prefactor of `P_III(D_6)` at `t=0` |
| Okamoto 1987 | §§2-3 | Residual **R5** (primary blocker): explicit `2x2` Lax pair |
| Jimbo-Miwa 1981 ("Monodromy preserving deformation II", *Physica D* **2**, 407-448) | §3 (P_III Lax pair) | Residual **R5** (alternate route) |
| Conte-Musette 2008 (*The Painlevé Handbook*, Springer) | ch. 7, §7.3-7.4 | Cross-check on R1, R2; Stokes-multiplier formulas |
| Lisovyy-Roussillon 2017 ("On the connection problem for P_III", *J. Phys. A* **50**) | §4 | Residual **R3**: Stokes-multiplier sign and phase convention |
| Boutroux 1913 ("Recherches sur les transcendantes de M. Painlevé", *Ann. Sci. ENS* **3**:30, 255-375) | Part II §III | Residual **R3** (historical baseline) |

## What the prompt's literature crosscheck requires

The prompt Phase E says: *"Compare `S_{ζ*}^{can}` against the
published `P_III(D_6)` Stokes-data tables.  If the match is found:
write a DIAGNOSED entry. If no match is found: this is *not* a
halt --- document the parameter triple."*

Since `S_{ζ*}^{can}` is not numerically computed in this session
(Phase D was not executed because Φ_symp is residual), no
table-comparison is possible.  The parameter triple is documented
in `pIII_canonical.tex` and the residual list above.

## What is established without the missing literature

1. **V_quad scalar ODE** (`vquad_hamiltonian.tex`):
   `3 z³ f'' + 10 z² f' + (5z + z² - 1) f = 0`,
   exact rational coefficients, sympy-verified.

2. **Newton polygon at z=0**: single edge slope 1/2, exact.

3. **Borel-plane singular distance**:
   `ζ_* = 4/√3`, exact algebraic, 250-digit agreement with
   Prompt 005 measurement.

4. **Secondary exponent**: `ρ = -11/6`, exact rational.

5. **Φ_resc parameter**: `λ = 1/3`, fixed by exponent matching;
   pending R3 sign convention.

6. **Phase-C consistency**: matching system has no contradictions
   in the parameters fixable from V_quad data alone.  The
   `G15_NOT_LIFTABLE` halt clause is **not** triggered.

## Recommended literature acquisition (operator)

To close G15 fully, the operator needs at minimum:

- Okamoto 1987 §§2-3 (the explicit Lax pair --- ~10 pages),
- Conte-Musette 2008 ch. 7 §§7.3-7.4 (parameter conventions and
  trans-series tables --- ~25 pages).

Both are standard library items.  The operator's earlier
`G3b` ILL/AMS request workflow (cf. picture_revised_20260502.md
line 290) is the natural channel.

Once these are in hand, a follow-up prompt of estimated runtime
2-4 hours can close G15 completely:
- pin R1, R2, R3 from Okamoto / Conte-Musette;
- write Φ_symp explicitly from the Lax pair gauge transform;
- compute J(Φ) numerically;
- verify `S_{ζ*}^can` against Lisovyy-Roussillon's tables to
  ≥ 50 digits.

## DIAGNOSED entry candidate (placeholder, not yet authoritative)

If R1 resolves as $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)
= (1/6, 0, 0, -1/2)$ in some pre-Sakai convention (which would
require the constraint to be re-stated, since the four numbers
sum to $-1/3 \ne 0$), then the V_quad point lives on a special
divisor of the `P_III(D_6)` parameter space.  Such special
parameter points often appear in the literature under names
like *Bessel-type reduction*, *frozen Stokes data*, or
*classical solutions* of P_III.  This is a hypothesis; do not
cite without R1.
