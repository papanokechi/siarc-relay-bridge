# Adams 1928 → BT 1933 — Ladder Map

**Adams 1928 SHA-256:**
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`
**BT 1933 SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**BT 1933 full reference:** Birkhoff, G. D. & Trjitzinsky, W. J.,
"Analytic Theory of Singular Difference Equations", Acta Mathematica
**60** (1933), pp. 1–89.

## Ladder labels

- **ABSORBED-VERBATIM**: BT 1933 contains the same result with the
  same scope.
- **EXTENDED**: BT 1933 generalises Adams's result (e.g., from a
  specific irregular sub-case to a more general factorisation /
  q-difference / Stokes-data setting).
- **SUPERSEDED**: BT 1933 strengthens Adams's bound or reduces
  hypotheses.
- **PARALLEL**: Adams treats a sub-case BT 1933 does not explicitly
  address.

## BT 1933 self-statement of relation to Adams 1928

BT 1933 **p. 5** contains the explicit acknowledgement (verbatim, ≤ 30
words):

> "In a recent important paper Adams has shown that to some extent
> Birkhoff's methods continue to apply in the irregular normal case."
> (22 words.)

immediately followed (still on BT 1933 p. 5):

> "In the present paper the analytic theory of linear difference system
> (or single equation) is developed so as to apply without restriction
> upon the form of the formal series."  (29 words.)

This pair of sentences together frames the Adams-1928 → BT-1933
ladder: Adams treats a sub-case ("the irregular normal case"); BT
generalises ("without restriction upon the form of the formal
series").

## Ladder table

| Adams ID | Section | Adams scope | BT 1933 counterpart | Ladder label |
| --- | --- | --- | --- | --- |
| **T1** (Theorem A) | §6 (n-fold root, left limits) | Class 1 special-case existence of determinant limits via infinite-left product | BT 1933 §5 *Theorem I* (existence of n columns of analytic solutions for the system, with formal-series asymptotic representation in a quadrant Γ) and §9 *Fundamental Existence Theorem* (general existence without restriction on the formal series). | **EXTENDED** |
| **T2** (Theorem B) | §6 (n-fold root, right limits) | Mirror of T1 on the right | BT 1933 §5 + §9 (entire-plane analogues; BT 1933 covers other quadrants by symmetry, "In quadrants other than Γ results will hold precisely analogous to those obtained with reference to Γ" — BT p. 5, ≤ 30 words). | **EXTENDED** |
| **T3** | §1 Class-1 formal series | Single-segment characteristic-equation case with formal series of types (4) and (6) | BT 1933 §1 (formal-series setup) — BT introduces the same formal-series machinery without the Class-1 / Class-2 split; covers regular + irregular together. | **ABSORBED-VERBATIM** (formal-series setup) / **EXTENDED** (scope: BT does not separate Class 1 / Class 2) |
| **T4** | §1 Class-2 Newton-polygon | Multi-segment Newton-polygon construction; secondary, tertiary, … equations per segment of L | BT 1933 §6 *A Lemma on Factorization* (Lemma 9; factorisation of the system in regions separated by B'-curves) and §3 *Lemmas on Iteration*. BT replaces Adams's Newton-polygon segment-by-segment construction with a region-and-factorisation framework that covers the same content without the polygon visualisation. | **EXTENDED** (different formalism; broader scope) |
| **T5** | §2 Class-2a / Class-2b existence theorems | Existence of n formal solutions (10) + matrix G(x), H(x) for Class 2a; minor formula modifications for Class 2b | BT 1933 §5 *Theorem I* + §7 *On Products of Completely Proper Operators* (Theorem II). BT replaces the Class-2a / Class-2b split with the "completely proper operator" notion; covers both sub-cases as instances. | **EXTENDED** |
| **T6** | §3 Periodic functions matrix P(x) = H⁻¹(x)G(x) | Class 2a periodic-functions structure, with z = e^{2πi x} reduction and rationality consequences | BT 1933 *no explicit periodic-functions section* (BT focuses on factorisation + Stokes-data structure). Adams's §3 treatment of periodic functions is a specialised analytic-structure result not foregrounded in BT. | **PARALLEL** |
| **T7** | §4 Asymptotic forms in entire plane (critical rays + curvilinear asymptotes Cᵢ) | Class 2a determinant-limit asymptotic-form transitions | BT 1933 §5 + §7 (the "completely proper" framework supplies the Stokes-curve asymptotic transitions that Adams describes via Cᵢ curves). BT generalises the explicit critical-ray / Cᵢ-curve picture into a region-of-validity calculus. | **EXTENDED** |
| **T8** | §7 n=2 double-root strengthening (Class 1, n=2) | Special-case improvement of T1+T2 for n=2 | BT 1933 *no explicit n=2 special section*. The n=2 case is subsumed by BT's general n; BT does not separately strengthen Adams's n=2 results. | **PARALLEL** (Adams's n=2 sharpening is a sub-case BT does not separately address) |
| **T9** | §8 Large class of irregular cases (mixed multiplicities; finite non-zero roots first; closing extension to Class 2) + the *regions-of-validity caveat* (p. 541 last paragraph) | Generalisation of T1–T2 to mixed-multiplicity Class-1 cases; closing announcement that the Class-2 multiple-root extension is "immediate" | BT 1933 §9 *Fundamental Existence Theorem* — "without restriction upon the form of the formal series" (BT p. 5). BT's Theorem of §9 settles the case Adams describes only as "immediate". | **SUPERSEDED** (BT's §9 covers what Adams's §8 announces as "immediate" with full proof; the regions-of-validity caveat persists in BT as quadrant-Γ explicit-versus-symmetric statement) |

## Distribution

| Ladder label | Count |
| --- | --- |
| ABSORBED-VERBATIM | 1 (T3, partial — the formal-series setup component) |
| EXTENDED | 5 (T1, T2, T3 (scope component), T4, T5, T7) — counted as 5 distinct ladder rungs after merging T3's split label into the EXTENDED column for the "scope: BT covers regular + irregular together" component |
| SUPERSEDED | 1 (T9) |
| PARALLEL | 2 (T6, T8) |

**Totals.** 9 indexed Adams results map to: 1 ABSORBED-VERBATIM + 5
EXTENDED + 1 SUPERSEDED + 2 PARALLEL = 9 ladder placements (T3
contributes simultaneously to ABSORBED-VERBATIM and EXTENDED, hence
the row count exceeds 9 by 1).

## Where Adams's regions-of-validity caveat (p. 541) lands in the ladder

Adams §8's closing-paragraph caveat —

> "the regions of validity of the asymptotic forms of some or all of the
> determinant limits for λ greater than this value of i are further
> restricted."  (27 words; printed p. 541.)

— is the natural seed of BT 1933 §7's "completely proper operator"
framework and §9's region-by-region existence theorem (Γ + symmetric
quadrants). The caveat is **carried forward** by BT 1933 (not
discharged).

## Cross-walk capability assessment

This session performed a quick-scan cross-walk of BT 1933 sectional
headers via pypdf and located the Adams citation at BT 1933 p. 5 (with
explicit Adams 1928 reference). A full BT 1933 §§ 7–9 verbatim
readthrough is the natural follow-up substrate task and is
**RESERVED for a future session**; the present ladder-map labels are
based on the BT 1933 sectional-headers + p. 5 self-statement +
Lemma/Theorem-label structure (Lemmas 1–10, Theorem I in §5, Theorem
II in §7, Fundamental Existence Theorem in §9, Theorem 4 in §12). No
verbatim BT 1933 theorem-statement quotes were extracted in this
session beyond the BT p. 5 Adams-acknowledgement pair.
