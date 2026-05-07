# BT 1933 §4 "A Lemma on Summation" — Verbatim Extract

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**Section span:** Acta p. 29 (PDF p. 29) — Acta p. 40 (PDF p. 40).
**Section title (verbatim, TOC):** "A lemma on summation."

Page anchors `[p. NN]` mark each Acta-page break. Math symbols are
reproduced as rendered by pypdf 6.10.2 (page-by-page text extract);
isolated font-glyph drift artefacts are flagged as `[font-drift?]`
where they affect interpretation. The single uniform pypdf
substitution `w → §` is silently restored in section-headers and
body-text references to other sections (per
`bt_1933_section_index_4_6.md` "Pypdf glyph-substitution note").

The transcript below preserves the linear page-by-page reading order;
intra-paragraph line breaks introduced by the pypdf line-folding are
preserved verbatim. Display-equation labels (e.g. `(I)`, `(I a)`,
`(2)`, `(3 a)`, `(I3)`) carry their printed numbering.

---

## [p. 29] — opening (header + R-region setup)

§ 4. A Lemma on Summation.

We shall now establish a modification of the method of contour summation
used in (II).

Let R denote a region the left boundary of which is either h (the lower
boundary of F (§ 2)) or a curve, extending indefnitely upwards, with a
limiting direction at infinity. Let the right boundary of R be a curve,
extending inde- finitely upwards, with a limiting direction at infinity.
This latter boundary, if with the limiting direction of the axis of reals
will be assumed to be a curve of the form v = h u^t (h, e > o). The left
boundary of R, if extending upwards and with its limiting direction
coincident with that of the negative axis, will be of the form
v = h(−u)^e + ...(h > o; I > e > o).

The following lemma will be proved.

## [p. 30] — Lemma 8 statement + proof opening

Lemma 8. Assume that the function

(1) H(x) = e^{Q(x)} h(x)

is analytic in R while Q(x) = µx log x + γx + ... + ν x^{1/p} is proper
on and in the neighborhood of the right boundary of R and

(1 a) h(x) ∼ H̃(x)   (in R)

where H̃(x) is a formal s-series (Def. 1; § 1). Furthermore, suppose that

(1 b) ℜ Q'(x) ≦ o   (in R).

The equation

(2) y(x + 1) − y(x) = e^{Q(x)} h(x)

possesses a solution y(x), analytic in a region R' interior to R by a
distance ε(> o), for which an asymptotic relation,

(2 a) y(x) ∼ e^{Q(x)} s(x),

where s(x) is a formal s-series, is maintained in the above region.

Proof. The formal equation

y(x + 1) − y(x) = e^{Q(x)} h(x)

is formally satisfied by ỹ(x) = e^{Q(x)} s(x) where s(x) is an s-series.
This follows from a Lemma proved by Birkhoff in (I; p. 218). Let t(x)
denote s(x) with the power series factors terminated after m terms (with
m sufficiently great). Substitute in (2)

(3) y(x) = e^{Q(x)} t(x) + x^{k'} z(x)   (k' = m).

The new variable z(x) will satisfy the equation

(3 a) q(x + 1) z(x + 1) − q(x) z(x) = x^{k'} χ(x)
              [q(x) → 1 as x → ∞]
where q(x) is rational with q(x) → 1.

## [p. 31] — formal contour-sum construction

Here

  x^{k'} χ(x) = e^{Q(x)} h(x) − Δ e^{Q(x)} t(x)

and β(x) is analytic and bounded in R. To demonstrate the truth of the
lemma we need first to show that (3 a) has a solution z(x) analytic in
R' and, if not bounded in R', infinite at x = ∞ to a finite order κ
which is such that κ − k' approaches infinity with k'.

The equation (3 a) with the second member replaced by zero is satisfied by

  z(x) = 1/q(x).

Hence

(3 b)   z(x) = (1 / q(x)) ∑_{t≡x} t^{k'} χ(t)

(3 c)   ∑_{t≡x} t^{k'} χ(t)

will be a solution of (3 a) provided the operation ∑_{t≡x} is suitably
specified.

With x in R' let L denote a contour lying interior to R and defined as
follows. When ℜ Q(x) = o along the negative axis of reals while the
lower boundary of R is h (the lower boundary of F) then L is to consist
of h and of a path L* near the right boundary of R. In all other cases
L is to consist of a path near the right boundary of R. With x not
near congruent to L (that is, if x' represents the point on L for which
ℑ x' = ℑ x we have ℜ(x − x') not an integer) let x + k_x (k_x ≥ o) be
the last one of the sequence of points x, x + 1, ... lying to the left
of L. Let l_x denote a loop which contains the points x, x + 1, ...,
x + k_x and passes between x − 1 and x and between x + k_x and L. Now,
by hypothesis, Q(x) is proper along L (and also at least within a
limited distance from L). Hence a least integer λ can be found so that

(4)   |t|^λ e^{Q(t)} → o   (ℑ t = v)

as |x| → ∞ upwards from the axis of reals along L. If µ ≠ o, L is near
the [imaginary axis of reals]. This integer λ will be unchanged if L is
shifted a finite distance in the direction of the axis of reals.

(footnote) "β(x) could be considered to be a function asymptotic in R
to a formal s-series whose power series factors begin with low powers
of x^{1/p}."

## [p. 32] — sum-formula + L-contour shift mechanics

[imaginary axis of reals]. This integer λ will be unchanged if L is
shifted a finite distance in the direction of the axis of reals.

Write, for x in R',

(5)   ∑_{t≡x} e^{Q(t)} β(t) / t^{k'}
       = ∫_{L_x} [ e^{2π√−1 λ(x−t)+Q(t)} β(t) / ((1 − e^{2π√−1(x−t)}) t^{k'}) ] dt.

Here λ will be supposed to have the value specified above. The path L_x
is to consist of L, described upwards (if L = h + L*, then h is
described from infinity to the neighborhood of the origin and L* is
described upwards), and of l_x, described in the clockwise direction.
When x approaches a position of congruency to L we shift L through a
suitable distance. The integral (5) will converge since β remains
bounded along L; moreover, it will represent a sum formula in the sense
of (3 c), and the function of x given by the second member of (5) will
be analytic in R'. It remains to show that this function is such that
z(x), as defined by (3 b), has the desired properties.

Let x' be the point on L for which ℑ x' = ℑ x. Denote the portion of L
up to that point by L_1 and from that point up by L_2. If L = h + L*,
let L*_1 denote the part of L* up to x' and let L*_2 denote the part of
L* up from x'. For t on L and for x in R' we have

(5 a)   |1 − e^{2π√−1(x−t)}|^{-1} > d > o.

The inequality

(6)   ℜ Q(x) ≧ ℜ Q(x_1)        (ℑ x = ℑ x_1; ℜ x ≦ ℜ x_1; x, x_1 in R)

will be also needed. It is seen to hold, in virtue of (1 b), since we
have ℜ Q(x_1) − ℜ Q(x) = ∫_x^{x_1} ℜ Q'(x) dx.

With these preliminaries in view consider the integral along l_x,

(footnote) "This is due to the fact that along such a path and, in
general, along a path extending upwards with its limiting direction
coinciding with that of the positive axis of imaginaries we have
[expression] behaving as a constant multiple of |x|^e (e > o)."

## [p. 33] — Birkhoff-(II) inequalities + l_x estimate

(7)   ∫_{l_x} = e^{Q(x)} β(x)/x^{k'} + e^{Q(x+1)} β(x+1)/(x+1)^{k'} + ...
                + e^{Q(x+k_x)} β(x+k_x)/(x+k_x)^{k'}.

In virtue of (6), for x in R',

(7 a)   |∫_{l_x}| ≦ e^{ℜ Q(x)} β [ 1/|x|^{k'} + 1/|x+1|^{k'} + ...
                                    + 1/|x+k_x|^{k'} ].

Now, substituting z = −x + 1 in an inequality of Birkhoff [II eq. 12],

  1/|z|^{k'-1} + ... + 1/|z+i|^{k'-1} ≦ A/|z|^{k'-1}   (ℜ z < o),
  1/|z+i|^{k'} ≦ A/|z−1|^{k'-1}                       (ℜ z > 1)

we find that (...) so that, if R extends to the right of the imaginary
axis,

(7 b)   1/|x|^{k'} + ... + 1/|x+k_x|^{k'} ≦ h_1/|x|^{k'-1}
        (ℜ x = u > o; h_1 independent of k').

Let x (|x| > q > o; u ≦ o) and x + k_x be above curves

(8)   v = h_1(−u)^{e_1}        (h_1 > o; 1 > e_1 > o),

(8 a)  v = h_2 u^{e_2}         (h_2 > o; 1 > e_2 > o).

Substituting z = −x + 1 in the inequality (13) of (II),

  1/|z+i|^{k'} ≦ ...   (ℜ z > o; ℑ z = v),

it is found that

(8 b)   1/|x|^{k'} + ... + 1/|x+k_x|^{k'} ≦ h_2'/|x|^{k'}
        (u ≦ o; ℑ x = v).

(footnote) "See formula 12 in (II)."

## [p. 34] — case split: x above curves (8) / (8 a)

Let ξ̄ (ξ̄ < o) be the value of u for the point on the curve (8) whose
ordinate is ℑ x = v. Then, from (8 b), it follows that

   h_2'/|x|^{k'-(1-e_1)} ≦ h_2''(k')/|x|^{k'-(1-e_1)} .

Now for a suitable l, independent of x (u ≦ o), |x| ≧ l |x|, whenever
x is above the curves (8), (8 a). Whence

  1/|x|^{k'} + ... + 1/|x+k_x|^{k'} ≦ h_3'(k')/|x|^{k'(1-e_1)}
  (u ≦ o; x above (8)).

Thus the inequality

(9)   1/|x|^{k'} + ... + 1/|x+k_x|^{k'} ≦ h'/|x|^{k_2}

holds, whenever x (|x| > q > o) lies above curves of form (8), (8 a).
Here k_2 can be made arbitrarily great by taking k' sufficiently great
and h' is independent of x. Hence for x in R, above curves of type (8),
(8 a), we have

(10)  |∫_{l_x}| ≦ β h' e^{ℜ Q(x)} / |x|^{k_2}.

Whenever R contains the negative axis of reals the inequality (10) will
continue to hold in the whole region R' provided that along the negative
axis of reals, for |x| sufficiently great, ℜ Q(x) ≦ o. In fact, from (7)
it follows that

(10 a)  |∫_{l_x}| ≦ e^{ℜ Q(x)} β [1/|x|^{k'} + 1/|x+1|^{k'} + ...
                                  + 1/|x+k_x|^{k'} ];

on the other hand, we have

(10 b)  ℜ(Q(x') − Q(x))    (ℑ x = ℑ x'; ℜ x < ℜ x'; x, x' in R)

## [p. 35] — Case I (negative axis: ℜQ ≦ o)

diminishing very rapidly as x' − x increases. So it is clear that the
sum of terms in (10 a), involving factors of the form (10 b), is
negligible to the extent that (10) would hold throughout R'.

The only case when the inequality (10) is not asserted is when R
contains the negative axis of reals, while x is in R' below a curve of
the form (8) and e^{ℜ Q(x)} remains bounded as x moves to the left along
a line parallel to the negative axis. In the sequel it will be seen
that it is precisely in this case that it is not necessary to consider
the integral [along l_x; cf. Case II below].

There are two cases to be considered.

Case I.   Along the negative axis of reals, for |x| sufficiently great,
ℜ Q(x) ≦ o.

In this case along any line in R, parallel to the axis of reals,
ℜ Q(x) increases not slower than a positive fractional power of |x|, as
x moves along such a line to the left. This is an immediate consequence
of the nature of the function Q(x) and of the inequality (1 b) (which
insures (5)).

Now, taking into consideration (5 a) and the integrand in (5),

  |∫_{L_1}| < (1/d) ∫_{L_1} 1/|t|^{k'} ...

By (4) the integrand in the above increases exponentially along L_1
and attains its maximum at x', the upper end point of L_1. The integral
will be of the order of magnitude of the value of this integrand at x'.
Thus

  |∫_{L_1}| ≦ e^{Q(x')} / |x'|^{k_3}       (k_3 = k' − d_3; d_3 > o;
                                            k_3 → ∞ as k' → ∞;
                                            ℑ x = ℑ x').

In the case at hand, the function

  |x'|^{k_3} g(x)

approaches zero very rapidly as x moves to the left from x' along a line
through

## [p. 36] — Case I cont. + L_2 estimate

x' parallel to the axis of reals. When x remains in a sufficiently
close neighborhood of x' and does not part from x' too rapidly as
v(:= ℑ x → ℑ x') increase, the fact can be used that
ℜ(Q(x') − Q(x)) ≦ o (ℜ x ≦ ℜ x'); we shall then have g(x) either
bounded or infinite at infinity to an order k_4 such that k_4 − k_3 → ∞
as k_3 → ∞. More precisely, this will be the case for x in any region
bounded on the left by a curve of the form

  v = h(−u)^e        (h, e > o)

where e can be taken arbitrarily small. If there is occasion to consider
a region below such a curve, for x in such a region (with e sufficiently
small) we shall have e^{ℜ(Q(x')−Q(x))} approaching zero exponentially
(i.e., as e^{−r |x|^z} (r, z > o)) as |x| → ∞ along any path to infinity
in that region. It is clear then that

(11)  |∫_{L_1}| < e^{Q(x)} / |x|^{k_4}      (k_4 → ∞ as k' → ∞; x in R').

The integral along L_2 will be written in the form

  ∫_{L_2} ( e^{2π√−1 λ(x−t) + Q(t)} β(t) / ((1 − e^{2π√−1(x−t)}) t^{k'}) ) dt.

For x in R'

  |∫_{L_2}| ≦ β |e^{2π√−1 λ(x−x')}| ∫_{L_2} e^{Q(x') − Q(t)} |dt| / |t|^{k'}.

As t moves along L_2 from x' upwards we have β(t) bounded. Therefore the
maximum of the integrand, last written, occurs at x'. The reasoning of
the type used in deriving (11) will show that

(11 a)  |∫_{L_2}| ≦ 1/|x|^{k_5}        (k_5 → ∞ as k' → ∞; x in R')

so that

(12)  |∫| ≦ β/|x|^{k_6} e^{ℜ Q(x)}     (k_6 = k' − ...; → ∞ as k' → ∞;
                                        x in R').

## [p. 37] — Case II (ℜ Q = 0 on negative axis)

Case II.   Along the negative axis of reals ℜ Q(x) = o.

If the left boundary of R is not h this boundary will be of the form

  v = h(−u)^e + ...     (h, e > o).

An inequality like (12) will continue to hold in R'. This can be shown
by the reasoning used to derive (12). If the lower boundary of R is h
the contour L will consist of

  L = h + L* = h + L* [first part] + L*_2.

The contour L_x, in (5), will then be deformed into a loop, described
in the counter clockwise direction and extending to infinity, containing
the points x − 1, x − 2, ... and not containing the points x, x + 1, ...
The formula (5) will yield the following

(13)   ∑_{t≡x} e^{Q(t)} β(t) / t^{k'}
       = e^{Q(x−1)} β(x−1)/(x−1)^{k'} + e^{Q(x−2)} β(x−2)/(x−2)^{k'} + ...

inasmuch as convergence may be asserted.

Now

(13 a)  Q(x) = µ |x| log |x| cos(τ + ρθ) + ...     (γ = γ' + √−1 γ'';
                                                    e^{√−1 ρ θ} = ε^{2π/p};
                                                    x = |x| e^{√−1 θ};
                                                    p > s ≧ 1).

Necessarily µ + γ' = 0 and, whenever a coefficient ν in Q(x) is not
zero,

(13 b)  cos(τ + ρπ) = o.

Hence Q(x) = √−1 γ'' x + ν x^{1/p} + ... (p > s ≧ 1) while

(13 c)  ℜ Q(x) = −γ'' v + |ν| |x|^{s/p} sin(s/p (θ − a)) + ...
                                    (p > s ≧ 1);

## [p. 38] — Case II cont. + Γ_H curve construction

here we may have |γ| = o. This relation is derived by noting that, in
virtue of (13 b),

(*)  cos(τ + pa) = ± sin(s/p (θ − a)).

If ℜ Q(x) = −γ'' v then

(13 d)  ℜ[Q(x − i) − Q(x)] ≦ o     (i = 1, 2, ...).

If in (13 c) |γ| ≠ o, we define a curve Γ_H in Γ, by an equation

(14)   v = h(−u)^H        (h > o; H = 1 − ν/p).

For x in R below Γ_H we have ... and ... so that

  ρ − a = tan^{-1}(v/(−u)) = π/2 + ...     (π = π + ν/p u ...).

(14 a)   ...

Thus, below Γ_H,

(14 b)   |γ| |x|^{s/p} sin(s/p (θ − a)) ≦ |γ| h^* |x|^{s/p} (1/|x|^s)
        + ... = |γ| h^*/p |x|^{s(1−H)/p} + ...
                    since |x| = −u + ...

Similarly, if x is in R below Γ_H,

(14 c)   |γ| |x − i|^{s/p} sin(s/p (θ − a)) ≦ |γ| h^* + ...
         (x − i = |x − i| e^{√−1 θ_i}; i = 1, 2, ...)

Noting that

  [Q(x − i) − Q(x)] = [± |γ| |x − i|^{s/p} sin(s/p (θ − a)) + ...
                      − ± |γ| |x|^{s/p} sin(s/p (θ − a)) + ...]

we have by (14 b) and (14 c) ...

## [p. 39] — Γ_H closure + (15)

(15)   ℜ[Q(x − i) − Q(x)] ≦ 2 |γ| h^* s^l_i + ... < q
       (q independent of x, i; x in R below Γ_H; i = 1, 2, ...).

Hence, whether ℜ Q(x) = −γ'' v or |γ| in (13 c) is not zero, the
inequalities (15) are seen to hold at least for x in R below Γ_H. Thus,
from (13) it follows that

  |∑_{t≡x}| ≦ e^q β [1/|x−1|^{k'} + 1/|x−2|^{k'} + ...]
       (x in R', below Γ_H).

Further, by formula (12) of (II),

(15 a)  ∑_{t≡x} e^{Q(t)} β(t) / t^{k'} ≦ β e^{q + ℜ Q(x)} / |x|^{k'-1}
       (x in R', below Γ_H).

If R extends above Γ_H the expression (13) does not appear useful for
purposes of demonstration, whenever x is above Γ_H. In this case we use
the relation

  ∑_{t≡x} = ∫_{L_x} = ∫_{L_1} + ∫_{L_2} + ∫_{l_x}.

The first of the last three integrals satisfies inequality (10). As to
the second one, we have the integrand (as displayed in the second
member of (5)) bounded along h (while x has a fixed value in R' (on
or above Γ_H)). We have

  ∫_{L_1} = ∫_h + ∫_{L*_1}.

Here β(t) is bounded along h and increasing exponentially along the
remaining part of L_1, i.e., along L*. Hence

  ∫_{L_1} ≦ e^{ℜ Q(x)} / |x|^c       (some c > o)

## [p. 40] — final estimate + closing of proof

With x restricted as stated, we have x having behaving in the most
unfavorable way when x is on Γ_H; we have then

(16)   ν^{1/H} = ... + ... v + h(−u)^{1/H} + ...

Thus, for x in R' on and to the right of Γ_H,

  |∫_{L_1}| ≦ 1/|x|^{k_7} ;

A similar inequality is obtained for ∫_{L_2}, valid in the same region.
In proving this inequality we again make use of (16). Hence

(17)   |∫| ≦ ... + ... + h(−u)^{1/H} + ... < h/|x|^{k_8}
       (k_8 = k_5 H → ∞ as k' → ∞; x in R' on and above Γ_H).

  |∫_{L_x}| < 1/|x|^{k_9}
  (k_9 → ∞ as k' → ∞, x in R' on and above Γ_H).

But in virtue of (15 a) an inequality like (17) is seen to hold
throughout R'. This completes the examination of Case II.

The result just mentioned, together with (10) and (12), enables us to
assert that an inequality like (17) holds, for x in R', in any case.
It follows therefore that z(x), as given by (3 b), satisfies in R' an
inequality

  |z(x)| < β'' |x|^{κ}      (κ = k − k_x).

Now κ − k = k_x − ... and approaches infinity as k approaches infinity
(see (3 a)). In (3) attach subscript to y(x), t(x), z(x). It is clear
then that (2) holds for y_k(x) to m(k) terms (m(k) → ∞ as k → ∞).

It remains to show that (y_o(x) − y_k(x)) e^{−Q(x)} (=: g_{ok}(x);
σ > k) → o in R'. If h is part of L, g_{ok}(x) = o; otherwise,
|g_{ok}(x)| ≦ h''_k e^{−ℜ Q(x)} (in R'). Application of (4) and (6)
completes the proof.

[end of § 4]

---

## Tag legend

This file is the §4 verbatim transcript only. All sentence-level
[CLAIM-B4n] tags + paraphrases + page anchors are recorded in
`bt_1933_section_4_claim_table.md`. All theorem/lemma/corollary
labels in §4 (only Lemma 8) are indexed in
`bt_1933_sections_4_6_main_theorems.md` as identifier T1.
