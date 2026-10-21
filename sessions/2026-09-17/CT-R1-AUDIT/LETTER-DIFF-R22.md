# R22 — letter check before sending: operator paste vs repo draft

*The operator asked for a diff against `CT-S16-MEMBERSHIP-C/LETTER-vdPS-DRAFT.md`, which was checked against page images and is authoritative, and for both of the letter’s formulas to be verified against `TYPO-EVIDENCE.md`. Nothing has been sent.*

## Verdict

**Send the repo version.** The two differ in four places and the repo version is stronger or more exact at every one of them. No place was found where the operator’s paste is better.

## Formula checks against `TYPO-EVIDENCE.md`

| item | in repo draft | in evidence pack | agree |
|---|---|---|---|
| residual factorisation, full form | yes | yes | yes |
| corrected bracket (p + ½(q−1)q t)² | yes | yes | yes |
| printed bracket (p + ½(q−1)q)² | yes | yes | yes |
| B₁[1,2] corroboration present | yes | yes | yes |
| det A(0) does not discriminate | yes | yes | yes |
| arXiv:0902.1702v5, p. 34 | yes | yes | yes |
| no published erratum | yes | yes | yes |

Result: **every formula in the letter matches the evidence pack verbatim**.

## Unified diff

```diff
--- operator paste (review #17)
+++ repo LETTER-vdPS-DRAFT.md
@@ -4,11 +4,42 @@
 
-I have been working with your paper "Moduli spaces for linear differential equations and the Painlevé equations", Ann. Inst. Fourier 59 (2009), no. 7, 2611–2667, and I believe there is a small typographical error in the family (4.1) on p. 2655.
+I have been working with your paper "Moduli spaces for linear differential
+equations and the Painlevé equations", Ann. Inst. Fourier 59 (2009), no. 7,
+2611–2667, and I believe there is a small typographical error in the family (4.1)
+on p. 2655.
 
-The entry b(z) appears to be missing a factor of t in its first term: [FILL IN: printed form → corrected form].
+The entry b(z) appears to be missing a factor of t in its first term:
 
-My evidence is your own constraint det A(1) = −θ₁²/4. The printed form does not satisfy it; the corrected form satisfies it identically. The residual between the two readings factors as −(q−1)(t−1)(…)/4, so the two agree exactly at t = 1, which is the pattern one expects from a dropped t.
+    printed:    − z ( (p + ½(q−1)q)²  − θ₁²/4 + (q−1)(θ₀²/4 − θ₁²/4 − qθ∞²/4) ) / q  −  …
 
-The same entry appears in arXiv:0902.1702v5, p. 34, so it seems to have survived the revision of Section 4. I could not find a published erratum.
+    corrected:  − z ( (p + ½(q−1)q t)² − θ₁²/4 + (q−1)(θ₀²/4 − θ₁²/4 − qθ∞²/4) ) / q  −  …
 
-I am using the corrected form in work in preparation and would rather check with you than assume I am right.
+that is, (p + ½(q−1)q)² should read (p + ½(q−1)qt)². The second term of b(z),
+which is not in question, carries (q−1)qt in both of its factors.
+
+What persuaded me is not a constraint but your own page. The same bracket appears
+a second time on p. 2655, in the matrix B₁ of the display B = zB₀ + (1/t)B₁, and
+there it is printed **with** the t:
+
+    B₁[1,2] = − ( (p + ½(q−1)q t)² − θ₁²/4 + (q−1)(θ₀²/4 − θ₁²/4 − qθ∞²/4) ) / q
+
+Under the corrected reading, b(z)'s first term is exactly z · B₁[1,2]; under the
+printed reading it is not. So the expression appears to be written correctly a
+few lines below the place where the t is missing.
+
+This is independently confirmed by your constraint det A(1) = −θ₁²/4. The printed
+form does not satisfy it; the corrected form satisfies it identically. The
+residual between the two readings factors as
+
+    −(q−1)(t−1)(4p + q²t + q² − qt − q)/4 ,
+
+so the two agree exactly at t = 1, which is the pattern one expects from a
+dropped t — and the same factor appears in the comparison with B₁ above. (The
+companion constraint det A(0) = −θ₀²/4 holds for both readings, so it does not
+distinguish them.)
+
+The same entry appears in arXiv:0902.1702v5, p. 34, so it seems to have survived
+the revision of Section 4. I could not find a published erratum.
+
+I am using the corrected form in work in preparation and would rather check with
+you than assume I am right.
 
```

