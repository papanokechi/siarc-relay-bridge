# Adams 1928 §1 — Verbatim Extract (with page anchors)

**Source PDF SHA-256:**
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`
**Section:** §1 "Formal series solutions."
**PDF pages:** 04–08. **Printed pages:** 509–513.
**Extraction tool:** pypdf 4.x (Python).

This file is a faithful pypdf rendering of §1 with explicit page-break
markers `[p. NNN]` where NNN is the printed page number. OCR artefacts
(stray punctuation, malformed subscripts, ligature misreads, dropped
spaces in formula tokens) are preserved verbatim and tagged inline with
`[sic-pypdf]` only where the artefact is severe enough to obscure
mathematical meaning. Footnotes are reproduced after the body text on
each printed page, prefixed `[fn]`.

---

## [p. 509]

**1. Formal series solutions.** We shall set forth here only a statement of
the types of series that formally satisfy (1) in various irregular cases; that
these series do satisfy (1) can be verified directly by substitution, although
the labor involved is not inconsiderable. The cases in which the only irregu-
larities are multiple roots finite and different from zero are grouped for
consideration in

**CLASS 1** (a₀₀ ≠ 0, aₙ₀ ≠ 0) [pypdf reads "aooO,0 ano z?O"]. Corresponding
to a simple root pᵢ there is one formal series of the "regular" type:*

> (4)   s(x) = pᵢˣ xʳ P(x⁻¹)

Corresponding to a root pᵢ of multiplicity m > 1, and on the assumption
that pᵢ is not a root of the secondary equation

> (5)   a₀₁ pⁿ + a₁₁ pⁿ⁻¹ + … + a_{n-1,1} p + a_{n,1} = 0,

there are m series of the following type:*

> (6)   s(x) = pᵢˣ e^{L^{(m)}(x)} xʳ P(x⁻¹/m)

where

> L^{(m)}(x) = γ^{(m-1)} x^{(m-1)/m} + γ^{(m-2)} x^{(m-2)/m} + … + γ^{(1)} x^{1/m},

the constants γ^{(m-1)}, γ^{(m-2)}, etc., being different in the different
series. The m values of γ^{(m-1)} are the m determinations of the mth root
of a constant not zero times the left-hand member of (5) after pᵢ has been
substituted for p,

[fn *] r is a constant, in this and subsequent types. P(x⁻¹) stands for a
power series in x⁻¹, namely 1 + s' x⁻¹ + s'' x⁻² + …; the constant term may
be taken as 1, since we are dealing with the homogeneous difference
equation. Similarly, P(x⁻¹/m) is used to represent a power series in x⁻¹/m,
the first term being 1. The γ's, wherever they occur, are constants. In each
type of series the constants are calculated (by formal substitution of the
series in (1)) in the order in which they appear in the series as written; for
example, in (6) the constants after p₁ are calculated in the order γ^{(m-1)},
γ^{(m-2)}, …, γ^{(1)}, r, s', s'', … . The constants thus calculated are uniquely
determined for each series of the type.

## [p. 510]

and hence are different from zero. It is easily seen that these m series are
the m determinations of a single series.*

Corresponding to a root pᵢ of multiplicity m > 2 which is a simple root of
the secondary equation (5), there is a set of m series as follows:

> 1 series,         s(x) = pᵢˣ xʳ P(x⁻¹/(m-1));
> m − 1 series,     s(x) = pᵢˣ e^{L^{(m-1)}(x)} xʳ P(x⁻¹/(m-1))

In the case m = 2, these reduce to "regular" series like (4), but in order
that the equation (1) be satisfied by two such series, further conditions
must be fulfilled.

When pᵢ is an r-fold root of the characteristic equation and a multiple
root of the secondary equation, additional complications enter the problem
of obtaining formal solutions. In general under these conditions we have
been able to obtain only part of the full quota of m series; in particular
cases the full number has been found, but the facts that the cases are
particular and that the statements of conditions are long and involved lead
us to omit their description here. Two points may deserve mention: (i)
that the presence of pᵢ as an m₁-fold root of the secondary equation tends
to reduce to m − m₁ the index of the root of x⁻¹ according to powers of
which the series proceed; and (ii) that if m₁ is sufficiently large, the
question of whether pᵢ satisfies the subsequent equations

> (7)   a_{0j} pⁿ + a_{1j} pⁿ⁻¹ + … + a_{n-1,j} p + a_{n,j} = 0   (j = 2, 3, …)

becomes of importance.

We desire to call attention to only one further case. If pᵢ is an m-fold
root of (3), a root of multiplicity ≥ m of (5), a root of multiplicity ≥ m − 1
of (7) for j = 2, a root of multiplicity ≥ m − 2 of (7) for j = 3, …, a root of
multiplicity ≥ 2 of (7) for j = m − 1, and is not a root of (7) for j = m, then
the equation (1) is satisfied by m series of the regular type (4). In the event
of all these hypotheses except the last being satisfied, and if pᵢ satisfies all
the equations (7) for j ≥ m (as it would if, for example, the coefficient
functions (2) were polynomials of degree m − 1), an analytic solution of the
equation (1) is pᵢˣ; but this function satisfies a difference equation of first
order with rational coefficients, and (1) is therefore reducible.

Secondly we consider the cases in which some or all of the irregularities
are due to the presence of zero or infinite roots or of both; these cases we
group in

[fn *] Cf. §5, in which this fact is pointed out more clearly in a particular case.

## [p. 511]

**CLASS 2** (one or both of a₀₀, aₙ₀ = 0). Let us denote by a_{i,jᵢ} the first
non-zero coefficient in aᵢ(x) (i = 0, 1, …, n), and choosing i- and j-axes,
plot the points (i, jᵢ) as in Figure 1.

Construct a broken line L, convex upward, such that both ends of each
segment of the line are points of the set (i, jᵢ) and such that all points of
the set lie upon or beneath the line. This is the form that would be
assumed by an elastic string if pegs were inserted at the points (i, jᵢ), the
ends of the string fastened one at (0, j₀) and the other at (n, jₙ), and the
string allowed to contract from above upon the pegs. At least one of the
points (i, jᵢ) will clearly be situated on the i-axis; otherwise a power of x
might be suppressed in the entire equation (1).

In this class of irregular cases the so-called "characteristic equation" (3)
is by no means completely characteristic of the difference equation (1).
In fact we would rather say that (3) is replaced by several characteristic
equations, one associated with each segment of L. The degree of the
characteristic equation associated with any segment of L is 1 less than the
number of points (i, jᵢ) that lie on or beneath that segment (inclusive of
its end points). The coefficients of this characteristic equation are the
a_{i,jᵢ} corresponding to points (i, jᵢ) actually on that segment of L; the
coefficient corresponding to a point (i, j) beneath the segment is zero.
Evidently the sum of the degrees of these several characteristic equations
is n. If one of the segments is horizontal, the characteristic equation
associated with that segment (this may be obtained from (3) by suppressing
the zero and infinite roots) picks out its quota of formal solutions
precisely as (3) distinguishes n solutions in any case of Class 1. As for a
segment not horizontal, let the slope of any such segment be −μ, a rational
number different from zero. The transformation*

> (8)   f(x) = x^{sx} e^{−μx} g(x)   [sic-pypdf rendered "xMxe-,xg(x)"]

[fn *] In making this transformation one should employ the expansion …
The factor e^{−μx} is inserted in (8) merely for convenience in annulling the
e^{iπμ} here.

## [p. 512]

then changes (1) into a new equation of exactly the same type except in
the respect that if −μ is not an integer but a fraction, q/p in lowest terms
(p positive), some of the coefficient functions will be of the form
x^{−s/p} A(x), where s is a positive integer and A(x) a power series in x⁻¹.
The effect of (8) upon the points (i, j) is to relocate them in such a way
that each segment of the new broken line L' that "roofs them over" has a
slope μ' greater than that of the corresponding segment of L. Thus, in
particular, the segment of L whose slope is −μ becomes a horizontal
segment of L'.

This analysis makes it clear that if −μ is an integer, the state of affairs
with respect to the segment of L having this slope is wholly similar to
the situation relative to a horizontal segment and hence analogous to the
cases of Class 1. The formal series associated with the segment of slope
−μ are like those enumerated above under Class 1 except for the
additional factors x^{sx} e^{−μx} preceding the power series itself. The
equation which plays the role of (5) here is the equation whose coefficients
are the a_{ij} corresponding to points (i, j) which if plotted in Figure 1
would lie upon a line parallel to this segment of slope −μ and one unit
vertically below it. The tertiary equation for a segment of slope −μ is one
whose coefficients a_{ij} are those whose corresponding points (i, j) if
plotted would lie upon a line two units vertically below the segment, and
so on for the subsequent equations.

If on the other hand −μ is a fraction, q/p in lowest terms, there
corresponds to each simple root pᵢ of the characteristic equation for this
segment of L a formal solution of the type

> (9)   s(x) = x^{sx} e^{−(q/p)x} pᵢˣ e^{L^{(p)}(x)} xʳ P(x⁻¹/p)

It is noteworthy that in this case γ^{(p-1)}, and in addition any or all of
the subsequent γ's in the exponent of e, may vanish. In fact if all the
points (i, jᵢ) not on the segment of slope −μ are situated on or beneath
a line parallel to this segment and one unit vertically below it, the γ's in
(9) will all be zero.

When, for −μ = q/p, the characteristic equation for this segment of L
has a root pᵢ of multiplicity m > 1, the situation is more complicated. Let
the segment of slope q/p be prolonged in both directions to form a line ℓ.
Of the points (i, j) corresponding to non-zero coefficients a_{ij} but not
situated on this segment there will be one or more whose distance below
ℓ, measured vertically, is least; let that distance be t/p and draw a line ℓ'
parallel to ℓ through this point (or these points). Let the constants a_{ij}
corresponding to points (i, j) on ℓ' be used as coefficients in an algebraic
equation of degree n; this is the secondary equation for the segment of
slope q/p. If the secondary equation is not satisfied by pᵢ and if t/m is 1
or a submultiple of 1, then

## [p. 513]

corresponding to the root pᵢ there are m series of type (9) with p replaced
by w, where w = t/(mp). When the secondary equation has pᵢ as a root, the
situation is analogous to that described in the corresponding case under
Class 1 above.

---

**End §1.** Continues in §2 (which begins on the same printed page p. 513
under the centred header "CASES IN WHICH THE THEORY RESEMBLES
CLOSELY THAT OF THE REGULAR CASE"). See `adams_1928_section_2_extract.md`.
