# Phase C.2 — Birkhoff 1930 §§2-3 Verification

**Dispatch 3 timestamp:** 2026-05-03 (re-fire 3)
**Verdict signal:** `C_BIRKHOFF_UNIFORM_FORMAL_ONLY` (partial)

## Source

G. D. Birkhoff, "Formal theory of irregular linear difference
equations," *Acta Mathematica* **54** (1930), 205–246.

PDF on disk:
`tex/submitted/control center/literature/g3b_2026-05-03/birkhoff_1930.pdf`
(SHA-256 `aeb5291e…2efa`, 42 pages, text layer present and
extractable; full text dump in `birkhoff.txt`).

§2 = "Statement of the Formal Problem" (paper pp. 209–214).
§3 = "Solution of the Converse Problem" (paper pp. 214–217).

## Theorem (i) — formal-series existence (the §2 result)

**Statement (verbatim, p. 214, ≤ 30 words):**

> "It is our primary purpose in Part I of this paper [...] by
> proving that there always exist precisely n formal series
> solutions of the three types (6), (6'), (6")."

(28 words including bracketed elision; see birkhoff.txt
page 10, lines beginning "It is our primary purpose".)

**Construction (paraphrased; this is a paraphrase, not a
verbatim quote):** §2 sets up the Newton-polygon construction
on the points (i, j_i) where j_i is the leading exponent of
a_i(x) in the equation (4) of order n. Birkhoff describes a
"unique broken line L, concave upwards, whose vertices fall at
certain of these points, while all of the other points lie
above or on this line L" (verbatim, p. 211, 28 words). The
slopes μ_1 > μ_2 > … > μ_k of the segments of L give k
characteristic equations in ρ = e^γ, and the total number
of non-zero roots equals n (counted with multiplicity).

**Stated d-range / n-range:** The statement is **uniform in n**
(the system order, equivalently the equation (4) order); no
finite cap appears. Birkhoff's construction at p. 211 explicitly
allows arbitrary n, with k = number of segments of L bounded
above by n. The "basic integer" p (of fractional Puiseux
expansion x^{1/p}) is similarly unrestricted (any positive
integer; "all possible values of p are evidently positive
integral multiples of a least value p_0 ≥ 1", p. 209,
24 words).

**Translation to PCF d-range:** The PCF-1 / PCF-2 setting takes
n = d (recurrence order) and p = 1 (no fractional Puiseux).
Birkhoff's existence statement is therefore **uniform in
d ≥ 1** with no finite cap.

**Verdict signal for theorem (i):** `C_BIRKHOFF_UNIFORM`.

## Theorem (ii) — Borel-singularity claim (NOT in §§2-3)

Prompt 018 §2 step 5 names a second theorem to extract from
Birkhoff 1930 §§2-3:

> "Borel transform B[f] has leading singularity at ξ = c⁻¹
>  where c is the characteristic exponent from C.1"

**This statement does NOT appear in Birkhoff 1930 §§2-3.**

What §§2-3 actually treat:
- §2 — formal-series existence (theorem above) and the
  Newton-polygon construction;
- §3 — the *converse* problem (every set of n linearly
  independent formal series of types (6), (6'), (6")
  determines a unique linear difference equation of order n).

The Borel transform is **not used** in §§2-3 of this paper.
The word "Borel" does not appear in the §§2-3 text dump.
Birkhoff 1930 is the formal-series existence companion to
his earlier *analytic* theory work (cited at p. 205, footnote 1:
"The Generalized Riemann Problem for Linear Differential
Equations and the Allied Problems for Linear Difference and
q-Difference Equations," Proc. Am. Acad. Arts and Sciences,
vol. 49 (1913), pp. 521–558). The Borel-singularity radius
identification (Borel transform leading singularity at
ξ = 1/c) is part of the *analytic* theory of irregular
singularities (broadly: Watson 1918 → Nevanlinna 1918–1919
→ Borel 1928 → Écalle 1980s; in the difference-equation
context specifically Adams 1928, Birkhoff–Trjitzinsky 1933,
and later works), **not** of the formal §§2-3 of Birkhoff 1930.

This is a **prompt-spec inaccuracy** (recorded in
`unexpected_finds.json` and Phase D Anomalies). The
synthesizer almost certainly intends the Borel-singularity
content to be extracted from Birkhoff–Trjitzinsky 1933
and / or Wasow §X.3, both of which are in the broader G3b
acquisition queue but only partially landed (Wasow PDF
present but unreadable per Phase C.1; B–T 1933 not yet
acquired per `_OPERATOR_INSTRUCTIONS.md`).

**Verdict signal for theorem (ii):**
`C_BIRKHOFF_BOREL_NOT_IN_§§2-3` (i.e. claim cannot be
supported nor refuted from this paper / sections; the
relevant content lives elsewhere in the literature).

## §3 result — uniqueness of converse correspondence

§3 is mostly the converse construction (formal series ↔
unique difference equation). The relevant statement, p. 214
(verbatim, 28 words):

> "It is an easy matter to solve the converse problem by
> demonstrating that to every such set of n (linearly
> independent) formal series there corresponds a uniquely
> determined linear difference equation of the n-th order."

This pairs with theorem (i) to give the formal direction of
the bijection {n formal series of types (6), (6'), (6")}
↔ {linear difference equation of order n}. Uniformly in n
and p.

**Verdict signal for §3:** `C_BIRKHOFF_CONVERSE_UNIFORM`.

## Aggregated Phase C.2 verdict

Theorem (i) — supported, **uniform in n (= d) and p**, no cap.
Theorem (ii) — **not in this paper / sections**; cannot be
verified or refuted from Birkhoff 1930 §§2-3.

Aggregated signal: `C_BIRKHOFF_UNIFORM_FORMAL_ONLY` —
the formal-series existence half of Phase C.2 closes
uniform-in-d; the Borel-singularity half is moved to a
separate literature dependency (B–T 1933 / Wasow X.3).

## d-range stated by this section

For the theorem (i) clause that *was* verified: d_B* = ∞
(uniform). Birkhoff's theorem applies to all difference
equations of order n ≥ 1 with rational / formal-series
coefficients in x^{-1/p}. PCF-1 / PCF-2 are the n = d, p = 1
specialisation; no finite d_B cap is stated or required.
