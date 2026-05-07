# Adams 1928 §2 — Verbatim Extract (with page anchors)

**Source PDF SHA-256:**
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`
**Section:** §2 "Existence theorems."
**PDF pages:** 08–12. **Printed pages:** 513–517.
**Section header:** introduced by centred banner "CASES IN WHICH THE
THEORY RESEMBLES CLOSELY THAT OF THE REGULAR CASE" appearing on the
same printed page (513) immediately before the §2 numbered header.
**Extraction tool:** pypdf 4.x (Python).

This file is a faithful pypdf rendering of §2 with page-break markers.
OCR artefacts are tagged inline only where they obscure mathematical
meaning. Footnotes are reproduced after each printed page text.

---

## [p. 513 — banner + §2 opening]

**CASES IN WHICH THE THEORY RESEMBLES CLOSELY THAT OF THE REGULAR CASE**

**2. Existence theorems.** In certain of the irregular cases the theory of
equation (1) is much like that of the regular case; these cases fall under
the following classes.

**CLASS 2a.** The slope of each segment of L is an integer and the
characteristic equation associated with each segment has only simple
roots.

**CLASS 2b.** The slopes of some or all of the segments of L are fractional;
the characteristic equation associated with a segment of L whose slope is
an integer has only simple roots; the characteristic equation associated
with a segment of L whose slope is fractional has only simple roots and
either (a) no two of these roots are of equal absolute value, or (b) if two
or more of these roots have the same absolute value, no exponential
factor e^{L^{(p)}(x)} occurs in the formal series corresponding to them
(conditions under which the situation (b) would obtain are described
in §1).

We point out briefly in this section the dissimilarities between the
existence theorems in the cases of Class 2a and in the regular case; the
discussion requires only slight modifications, chiefly in respect to the
formulas, to adapt it to the cases of Class 2b.

In each case of Class 2a the equation (1) possesses n formal series
solutions which we denote by

> (10)   sᵢ(x) = x^{sᵢ x} e^{−μᵢ x} pᵢˣ x^{rᵢ} (1 + s'ᵢ x⁻¹ + s''ᵢ x⁻² + …)
>        (i = 1, 2, …, n).

All the μ for the set of solutions associated with a particular segment of
L then have the same value. To gain the simplicity of the matrix notation
and to make our work parallel that of Birkhoff, we write our single
equation (1) of the nth order in the form of a system of n linear equations
of the first order; the n formal solutions (10) then provide us with n sets
of formal solutions for the system.* These sets we arrange in a matrix, of
which each set constitutes a column; the elements of the first row are the
n series (10).

The order of the columns in the matrix is of importance. Let them be
arranged first according to descending values of μ; secondly, let those for
which μᵢ is the same be ordered according to descending values of |pᵢ|.

[fn *] The details of this frequently employed device are shown fully in
a particular case in §5.

## [p. 514]

Then (x/e)^{μᵢ x} pᵢˣ plays the role that pᵢˣ does in the regular case, and
since we have

> (11)   |(x/e)^{μᵢ x} pᵢˣ| > |(x/e)^{μⱼ x} pⱼˣ|       (i > j)

for large values of |x| when μᵢ is > μⱼ and for all values of x when μᵢ is = μⱼ,
no difficulty is experienced in establishing the existence of determinant
limits,* of solutions associated with them, and of intermediate solutions.

In seeking solutions by the aid of contour integrals, however, we
[need to] in some instances make a different choice of the λ_{ik} in
Birkhoff's formula (40) in order to insure that g_{lk}(x) be asymptotically
represented by s_{lk}(x) in as large a region as possible. For x above A₁∞
we have, as in the regular case,†

> (12)   g_{lk}(x) ~ s_{1k}(x) e^{2π λ_{1k} (-1)^{1/2} x} q_{1k}(x) + …
>                + s_{k-1,k}(x) e^{2π λ_{k-1,k} (-1)^{1/2} x} q_{k-1,k}(x)
>                + s_{lk}(x),

and we desire the last term on the right to be the dominant one in the
left half-plane. The governing influences in the terms are the exponential
factors, which are

> (x/e)^{μ₁ x} p₁ˣ e^{2π λ_{1k} (-1)^{1/2} x}, …,
> (x/e)^{μ_{k-1} x} p_{k-1}ˣ e^{2π λ_{k-1,k} (-1)^{1/2} x},
> (x/e)^{μ_k x} p_kˣ.

Writing all these as exponentials to the base e and dividing through by
the last, we may express the exponents in the following form:

> (13)   2π(-1)^{1/2} ( λ_{1k} − [(μ₁ − μ_k)/{2π(-1)^{1/2}}] {log[(x/e)^{1/2}]}
>                       + [logp₁ − logp_k]/{2π(-1)^{1/2}}
>                       − (μ₁ − μ_k) logx /{2π(-1)^{1/2}} ),
>        … (analogous for indices i = 2, …, k−1) …

[Eq. (13) is multi-line; pypdf rendering severely garbled — see PDF p. 9
direct for the canonical typeset form. The verbatim three-line form
above is a plain-text reconstruction; raw pypdf token shown for
faithfulness in the trailing block of this file.]

We propose to select the λ's so that these exponents, save the last, will
have real parts that become negatively infinite as x becomes infinite in
the second quadrant. If the μᵢ (i = 1, 2, …, k) in (13) are all equal, these
exponents are identical with the corresponding exponents in the regular
case. This makes it clear that the λ's may be chosen so that those
solutions on the left,

[fn *] We employ the terminology of Birkhoff, loc. cit.

[fn †] It should be observed that, to be consistent with the definition of
asymptotic representation of a function g(x) (cf. Birkhoff, loc. cit.,
p. 248), the relation (12) should, until the question of dominance is
settled, be interpreted as meaning "g_{lk}(x) is the sum of k functions
which have for asymptotic forms the several terms on the right." For
simplicity, however, we shall continue to write such relations in the form
of (12).

## [p. 515]

obtained by contour integrals, which are associated with the segment of
L farthest to the left will have the same properties as do all the principal
solutions in the regular case. When μᵢ is thus equal to μ_k, we choose
λ_{ik} as the least integer exceeding*

> (14)   (arg p_k − arg pᵢ)/(2π).

When μᵢ is greater than μ_k, the ith exponent in (13) clearly has a real
part that becomes negatively infinite as x recedes to infinity in the sector
π/2 + ε ≤ arg x < π, ε being an arbitrarily small positive number, whatever
choice of λ_{ik} be made; this is owing to the presence of log x within the
parentheses. If, however, we choose λ_{ik} to be any integer (and we take
it to be the least integer) greater than

> (15)   α_{ik} = [arg p_k − arg pᵢ − (μᵢ − μ_k) π/2]/(2π),

the asymptotic form of g_{lk}(x) will be given by s_{lk}(x) for x above A₁∞ and
on or to the left of the imaginary axis, or likewise on or to the left of
any parallel to it.

For x in the strip bounded by A₁∞ and B₁∞ the asymptotic form of
g_{lk}(x) is given by s_{lk}(x) as in the regular case, by virtue of the ordering
of the formal series according to μ's and p's.

When x is below B₁∞ we have

> (16)   g_{lk}(x) ~ s_{l1}(x) e^{2π(λ_{1k} − 1)(-1)^{1/2} x} q'_{1k}(x) + …
>                  + s_{l,k-1}(x) e^{2π(λ_{k-1,k} − 1)(-1)^{1/2} x} q'_{k-1,k}(x)
>                  + s_{lk}(x).

The dominance depends upon the real part of the exponents

> (17)   2π(-1)^{1/2}( λ_{ik} − 1 − μᵢ + μ_k + [logp_k − logpᵢ
>                     − (μᵢ − μ_k) log x]/{2π(-1)^{1/2}} ),
>         … (for i = 1, …, k−1) …

For μᵢ = μ_k (i = 1, 2, …, k − 1) the asymptotic form of g_{lk}(x) in any
sector π ≤ arg x ≤ 3π/2 − ε for which ε is positive is s_{lk}(x). If none of the
quantities

[fn *] This choice is the same as Birkhoff's in the regular case when the
quantity (14) is not an integer; if (14) is an integer, our λ_{ik} exceeds
his by 1. We make this choice in order to insure that g_{lk}(x) always be
represented asymptotically by s_{lk}(x) in the direction of the positive axis
of imaginaries; with Birkhoff's choice and (14) an integer for one or
more values of i, the asymptotic form of g_{lk}(x) in that direction is given
by the sum of two or more terms of (12), one of which is the last.

## [p. 516]

(14) is an integer, we have g_{lk}(x) ~ s_{lk}(x) for π < arg x < 3π/2; if on the
other hand one or more of the quantities (14) is an integer, the
asymptotic form of g_{lk}(x) in the direction of the negative axis of
imaginaries is given by the sum of two or more terms of (16), one of
which is the last.

When μᵢ is greater than μ_k for some or all of the values of i (= 1, 2, …,
k − 1), the ith exponent in (17) has a real part that becomes negatively
infinite as x recedes to infinity in the sector π < arg x < 3π/2 − ε, due to
the presence of the term log x, so that we have g_{lk}(x) ~ s_{lk}(x) in that
sector. In the direction of the negative axis of imaginaries, however, the
asymptotic form of g_{lk}(x) is given by s_{lk}(x) only when all of the
following conditions are fulfilled: (a) μᵢ − μ_k is ≤ 1 for i = 1, 2, …, k − 1;
(b) when μᵢ − μ_k = 1, λ_{ik} − α_{ik} is < 1; (c) when μᵢ − μ_k = 0, the
quantity (14) is not an integer.

If among these conditions (c) alone fails to be satisfied, the asymptotic
form of s_{lk}(x) [pypdf typo for g_{lk}(x)] in the direction of the negative
axis of imaginaries is given by the sum of two or more terms of (16); one
of these terms is the last, while the others correspond to values of i for
which pᵢ = p_k and (14) is an integer. If either or both of conditions (a)
and (b) fail, the asymptotic form of g_{lk}(x) in the direction in question
is given by the term (or sum of terms) of (16) corresponding to the
value (or values) of i for which

> λ_{ik} − 1 − α_{ik} + (μᵢ − μ_k)/2

is largest.

The functions g_{ij}(x) are analytic except for poles throughout the entire
finite plane; we denote the matrix (g_{ij}(x)) by **G(x)**.

The freedom that we have in the choice of λ_{ik} when μᵢ is > μ_k makes it
clear that the solutions on the left associated with segments of L other
than that farthest to the left are not in general characterized uniquely by
the properties we have proved for them. Exceptions can occur only when
the solutions in question are associated with the second segment from the
left and when the slope of that segment is only 1 greater than the slope
of the first segment. We therefore hesitate to apply to these solutions the
term "principal solutions" except in the case in which L consists of but a
single segment; this case is, however, essentially regular.

There exists a similar set of solutions "on the right," in obtaining which
we choose λ_{ik} (i > k) as the least integer exceeding α_{ik} (cf. (15); the
fact that in α_{ik}, i is now > k should not be overlooked). From the
relation α_{ik} = − α_{ki} it follows that λ_{ki} = 2 − λ_{ik} or 1 − λ_{ik}
according as α_{ik} is or is not an integer. In this set of solutions only
those associated with the segment of L farthest to the right can in general
be said to be characterized by the properties we prove them to possess.
We denote the matrix of these functions by **H(x)**;

## [p. 517]

its elements are analytic except for poles throughout the finite plane.

---

**End §2.** Continues in §3 ("Periodic functions.") on the same printed
page p. 517.
