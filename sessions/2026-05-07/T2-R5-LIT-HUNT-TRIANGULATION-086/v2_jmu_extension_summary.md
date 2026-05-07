# Phase C — V2 JMU Extension Summary (arXiv:1604.03082 v4)

**Session:** 086 T2-R5-LIT-HUNT-TRIANGULATION
**Phase:** C (V2 connection-formula machinery summary + JMU
  triangulation against canonical Jimbo-Miwa-Ueno 1981)
**V2 source:** Its, Lisovyy, Prokhorov, "Monodromy dependence and
  connection formulae for isomonodromic tau functions",
  arXiv:1604.03082 v4 (29 Oct 2018) = Duke Math. J. 167:7 (2018),
  1347-1432.
**V2 PDF SHA-256:** `B63A1E2EC2E6E7A67F6BCF62C1238A5CEF834AA70983E5B2DC53AB8457461B65`
**V2 PDF size:** 714 266 B.

Substrate-inventory scope only; emits a structural summary of V2's
extension of the Jimbo-Miwa-Ueno 1-form to the full extended
monodromy data, with applicability assessment for P_III($D_6$).

---

## §C.1 — V2's central construction: the extended 1-form $\omega$

V2 §1.3 + §1 eq. (1.11) defines the extended 1-form as

$$
\omega = \sum_{\nu = 1, \dots, n, \infty} \mathrm{res}_{z = a_\nu}
   \mathrm{Tr} \bigl\{ G_{(\nu)}(z)^{-1} A(z) \, dG_{(\nu)}(z) \bigr\},
\quad d = d_T + d_M \,.
$$

Verbatim (v2_full.txt L266-273; 33 words plus formula):

> "$\omega = \sum_{\nu = 1, \ldots, n, \infty}
>  \mathrm{res}_{z = a_\nu} \mathrm{Tr}\{G_{(\nu)}(z)^{-1} A(z)
>  d G_{(\nu)}(z)\}, d = d_T + d_M.$ This expression is inspired by
>  the works of Malgrange [Mal] and Bertola [Ber]. It extends the
>  Jimbo-Miwa-Ueno form $\omega_{JMU}$"

Where:
- $T$ = isomonodromic times (positions of singular points $a_1, \dots, a_n$ in Fuchsian case; isomonodromic time $t$ in non-Fuchsian P_II/P_III case).
- $M$ = monodromy manifold.
- $G_{(\nu)}$ = local fundamental matrix solution near $z = a_\nu$.
- $A(z)$ = coefficient matrix of the linear system (1.1).

V2's $\omega$ is **not closed** in general; its exterior
differential $\Omega := d\omega$ is a 2-form on $M$ only and is
independent of isomonodromic times $T$ (V2 Proposition 2.3 for
the Fuchsian case; V2 Theorem 4.2 for the non-Fuchsian general case).

## §C.2 — V2's program: the closed form $\hat\omega$

V2 defines $\hat\omega := \omega - \omega_0$, where $\omega_0$
is a 1-form on $M$ such that $d\omega_0 = \Omega$. The form
$\hat\omega$ is closed; the **extended tau function** is then
defined by

$$
d \ln \tau_{\rm ext} = \hat\omega
$$

(V2 eq. 1.10), such that $\tau_{\rm ext}$ extends the Jimbo-Miwa-
Ueno tau function $\tau_{JMU}$ across the **full** extended phase
space $\tilde T \times M$.

The connection-formula problem is: relate the asymptotic constant
factors of $\tau$ across different critical directions in $\tilde T$
(e.g. $t \to 0, 1, \infty$ for P_VI; $t \to \pm \infty$ for P_II).
V2's $\hat\omega$ provides a path: integrate $\hat\omega$ along a
contour in $\tilde T \times M$ from one asymptotic regime to another.

## §C.3 — V2's worked applications

V2 carries the program through to two test cases:

### V2 Section 3 — Painlevé VI (Fuchsian, n = 3, 4-point system)

V2 §3 + Theorem A computes the explicit constant factor in the
P_VI tau-function asymptotics in terms of Barnes G-functions,
proving the conjectural formula of Iorgov-Lisovyy-Teschner [ILT13].

### V2 Section 4 — Painlevé II (non-Fuchsian)

V2 §4 + Theorem B computes the explicit ratio of constant factors
in the P_II tau-function asymptotics along $t \to + \infty$ and
$t \to - \infty$ rays. The non-Fuchsian construction handles
irregular singular points via Stokes-sector canonical solutions
(structurally analogous to V1's Lax-pair (4.1)+(4.3) at $\lambda
= 0, \infty$).

### V2's reference to P_III($D_8$): cited via [IP] (Its-Prokhorov)

V2 §1.4 cites Its-Prokhorov [IP] as the prior work where the
extended-1-form scheme was first realised, for P_III($D_8$) — the
"most degenerate type" of P_III. V2 itself does NOT directly
treat P_III($D_8$) or P_III($D_6$); P_VI and P_II are the V2
worked examples.

Verbatim (v2_full.txt L258-260; 35 words):

> "The program outlined above has been first realized in [IP] for
>  Painlevé III equation of the most degenerate type $D_8$, where
>  it allowed to give a proof of the connection formula for
>  $P_{III}(D_8)$ tau function earlier conjectured in [ILT14]."

## §C.4 — JMU 1981 triangulation

V2's $\omega$ extends the canonical Jimbo-Miwa-Ueno 1-form
$\omega_{JMU}$ defined in JMU 1981 (Physica D 2). The JMU 1-form
is supported on the **isomonodromic-time** part $T$ of the phase
space; V2's extension carries it across the full $\tilde T \times
M$. V2 §1.2 transcribes $\omega_{JMU}$ verbatim and the
identification $\omega|_{T} = \omega_{JMU}$ is recorded (V2
Proposition 2.3 + V2 §3's asymptotic computation).

For the P_VI case, V2 §3 derivation uses:
- The 4-point Fuchsian Lax system (eq. 1.12) with regular singular
  points at $z = 0, t, 1, \infty$.
- Stokes-Birkhoff theory at each $a_\nu$, but for Fuchsian systems
  this reduces to formal monodromy exponents $\Theta_{\nu, 0}$
  + connection matrices.

For the P_II case, V2 §4 derivation uses:
- Non-Fuchsian Lax system with one irregular singular point at
  $z = \infty$ of Poincaré rank 3/2.
- Stokes-sector canonical solutions + Stokes multipliers.

The **non-Fuchsian apparatus** in V2 §4.1 + Theorem 4.2 is
**structurally applicable** to P_III($D_6$): P_III($D_6$) has
two irregular singular points at $\lambda = 0, \infty$ (per V1
§4.1), each with formal solutions parametrised by the Stokes-
sector canonical-solution machinery.

## §C.5 — Applicability of V2's machinery to P_III($D_6$)

V2 does NOT directly compute the P_III($D_6$) connection constant.
However, V2's Theorem 4.2 (general non-Fuchsian extended 1-form
construction) IS structurally applicable to the V1 Lax pair (4.1).
The applicability rests on:

1. V1's RH problem 4.1 satisfies the V2 §4.1 hypotheses (2 × 2
   linear system with rational coefficients; irregular singular
   points $\lambda = 0, \infty$; formal-solution canonical
   factorisation per V1 (4.7)+(4.8)).
2. V2's $\omega$ = sum of residues at each singular point of
   $\mathrm{Tr}(G_{(\nu)}^{-1} A \, dG_{(\nu)})$ — directly
   constructible from V1's $\Lambda^{(6)}(\lambda, x)$ matrix
   (V1 eq. 4.2) and its formal-solution local fundamental
   matrices $\Psi_{\rm formal}^{(0)}, \Psi_{\rm formal}^{(\infty)}$
   (V1 (4.7), (4.8)).
3. The connection problem for the P_III($D_6$) tau function reduces
   to: integrate V2's $\hat\omega$ along a contour in extended
   monodromy space from one critical direction to another. This
   requires asymptotics of $\omega$ at the V_quad parameter point
   — which is the open Phase D.2 numerical residual in 058R.

V2 alone does NOT close the V_quad → P_III($D_6$) Stokes-constant
matching. V2 + V1 together provide the **methodology + Lax pair**
needed to set up the calculation, with the explicit asymptotic
analysis remaining as a separate computational task.

## §C.6 — Source / target / methodology decomposition

| Aspect           | V2 specification                                                                                                            |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Object         | Extended 1-form $\omega$ on $\tilde T \times M$ (V2 eq. 1.11) and closed form $\hat\omega$ (V2 §1.3).                      |
| Domain / target  | Extended phase space $\tilde T \times M$ → $\mathbb{C}$-valued 1-form (extends JMU 1-form $\omega_{JMU}$).                  |
| Method           | Malgrange-Bertola extension principle; residue-at-each-singular-point construction.                                         |
| Worked cases     | P_VI (V2 §3, Theorem A) + P_II (V2 §4, Theorem B). Cites [IP] for P_III($D_8$). P_III($D_6$) NOT directly treated.       |
| Applicability     | Structurally applicable to P_III($D_6$) via V1's Lax pair (4.1); explicit calculation = open computational task.           |
| JMU triangulation | V2 §1.2 + Proposition 2.3 transcribe $\omega_{JMU}$ verbatim and prove $\omega|_T = \omega_{JMU}$.                          |

## §C.7 — Discipline reassertion

V2's connection-formula machinery is DOCUMENTED at substrate-
inventory scope. The applicability assessment to P_III($D_6$) is
**structural** (V2's hypotheses match V1's Lax-pair setting); it is
not a calculation of the P_III($D_6$) tau-function connection
constant. The latter is forward-pointed as the deferred Phase D.2
numerical task per 058R substrate.

End of `v2_jmu_extension_summary.md`.
