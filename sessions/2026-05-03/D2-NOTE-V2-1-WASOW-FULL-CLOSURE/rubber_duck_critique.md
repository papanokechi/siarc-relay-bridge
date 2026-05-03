# Rubber-duck critique — D2-NOTE v2.1

This is the agent's self-critique of the v2.1 manuscript before the
session is committed to the bridge. It is the rubber-duck pass that
the spec calls for: the agent reads its own draft from the perspective
of an unsympathetic referee and records every weakness it can detect.
None of the weaknesses below are halt-worthy; they are recorded for
Claude's downstream review.

## Substantive

1. **The (-1)^d sign convention in the Lemma 3.1 proof step (c).**
   The proof folds the parity-dependent sign of the leading term into
   "the standard WKB convention $f \sim \exp(+c/u)$" without giving the
   convention an explicit footnote or citing where this convention is
   set. A determined referee will ask: what is the standard convention,
   and where is it stated? The honest answer is that for irregular
   singular points of order-2 linear ODEs the WKB ansatz is taken with
   a free sign on c, and the positive real root selects the formal
   solution that is asymptotic on the right half-plane sector at
   $z = 0^+$. A short citation to Wasow §5 (or to Costin 2008 ch.4)
   would close this.

2. **The q = (d+2)/2 derivation in §1.1 is sketchy.**
   The derivation moves quickly through "matching this to the
   slope-1/d read-off level $u^{-d}$ via the order-2 matrix-system
   re-scaling" without writing out the matrix-system reduction. The
   result is correct (it agrees with the SIARC Channel Theory v1.3
   Prop. 3.3.A derivation), but the sketch in §1.1 is not by itself
   a self-contained proof. A more careful version would either (a)
   write out the order-2 matrix system reduction explicitly, or (b)
   defer to CT v1.3 with a stronger pointer (the current "as derived
   in" is acceptable but minimal).

3. **The "uniformly in $n$" wording in §3.4 (Birkhoff 1930).**
   The note says Birkhoff 1930 §2 establishes formal-series existence
   "uniformly in $n$ (= the system dimension; here $n = d$ via the
   recurrence-to-ODE reduction)". This identification is correct for
   the order-2 PCF recurrence promoted to a $d \times d$ Birkhoff
   normal form, but the manuscript does not write out the
   recurrence-to-ODE-system reduction. A referee may ask for the
   reduction explicitly. Cite SIARC PCF-1 v1.3 §3 for the construction
   if pressed.

4. **The Borel-Laplace "duality variable" hand-wave in §3.5.**
   The transfer "the formal series of the recurrence solutions and the
   formal series of the ODE solution $f$ at $z = 0$ are mutually
   computable by formal Borel-Laplace transforms in the duality
   variable" is the weakest sentence in the chain. The standard
   reference is the Borel-Laplace machinery for difference operators
   (BT1933 §§4–5 supply this in difference-equation form; the
   generating-function transfer is a Cauchy-integral exercise). A
   referee may request a more detailed exposition. Costin 2008 ch.5
   §5.0a is cited as a modern restatement, but the manuscript does not
   write out the explicit Borel-Laplace pair.

5. **The SIARC bridge sessions (Appendix A) are not peer-reviewed.**
   The manuscript discloses this via the SIARC-disclosure footnotes,
   but a referee may still discount the Phase A* sweep evidence on
   grounds that the verification scripts are not independently
   replicated. Mitigating factors recorded in claims.jsonl: scripts
   are SHA-256-locked; bridge is public; Phase A* is a numerical
   verification of an already-mechanically-derived Lemma (Lemma 3.1),
   not a load-bearing primary derivation.

## Structural

6. **Page count 9 sits at the lower edge of FULL band.**
   Spec Phase E.10 sets FULL = [9, 12]. v2.1 lands at 9. If a single
   added paragraph in the rubber-duck critique items above were
   incorporated as a prose strengthening (for example, an explicit
   matrix-system reduction in §1.1, or a Borel-Laplace pair in §3.5),
   the page count would land closer to 10, more comfortably in the
   FULL band. Operator may consider these paragraphs for v2.2 if the
   classifier ever flags 9 pp as too thin.

7. **The Loday-Richaud / Mitschi pointer in §4(d).**
   The manuscript acknowledges that the Loday-Richaud volume was not
   consulted because the PDF was not on disk; this is honest and
   ETHICS-GATE-compliant, but a referee may ask why the standard
   modern reference was not consulted. The mitigating answer is that
   the Costin 2008 ch.5 §5.0a citation supplies the modern Borel-Laplace
   restatement; Loday-Richaud is a "would make even more explicit"
   pointer, not a load-bearing reference.

## Editorial

8. **Two SHA-truncations are referenced in the manuscript with form
   `b9954d12$\dots$ece66`.** These are LaTeX-compatible truncations.
   The full SHAs live in claims.jsonl and the Appendix A bridge-session
   listing. Acceptable.

9. **The forbidden-verb hygiene of CT v1.4 SOP §5 was honoured.**
   Searched the manuscript for bare "shows / confirms / proves /
   demonstrates / establishes / verifies" in conjectured contexts;
   none found in load-bearing positions. ("Verified" is used in the
   d=4 status sentence and is acceptable because d=4 has the AEAL-
   anchored measurement.) ("Proven" is used at d=2 and is correct.)
   ("Establishes" appears in the literature-attribution sentences for
   Birkhoff 1930 / Wasow / BT1933, where the sources actually
   establish the cited results; this is correct attribution, not a
   conjectured-context use.)

10. **The "Newton polygon slope-1/d edge ↔ Wasow shearing exponent
    $g_0 = 1/d$" equivalence assertion in §3.3 final paragraph.**
    The manuscript records this as "the same object in two notations".
    A referee may ask for a one-line proof. The proof is: the slope
    $h/w$ of the slope-1/d edge from $(0,0)$ to $(d,1)$ is $1/d$,
    height/width; Wasow §19.3 defines the shearing exponent as the
    multiplicity of the slope edge divided by its width, which equals
    $1/d$ for the order-2 multiplicity in the slope-1/d edge case.
    This could be added as a footnote.

## Net assessment

None of the above is halt-worthy. The manuscript closes the F1
residual that v2 admitted as open, with: (a) a mechanical Lemma
replacing the v2 black-box, (b) verbatim quoted BT1933 §§4-6 anchors,
(c) Phase A* numerical verification at d ∈ {2..10}. Items 1, 2, 4, 10
above are candidates for a future v2.2 strengthening pass; items 3, 5
are honest disclosures already made in the manuscript; items 6, 7, 8,
9 are non-issues.
