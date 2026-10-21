# Draft letter to van der Put & Saito — NOT SENT

**Status: HELD.** Two operator conditions are outstanding.

| Condition | Source | Status |
|---|---|---|
| Re-verify the entry and the constraint from page images, each read alone | review #13 | **done** — `TYPO-EVIDENCE.md`; journal p. 2655 and arXiv v5 p. 34 each rendered and looked at |
| Check for a published erratum | review #13 | **done** — none found; arXiv v5 revised §4 but not this entry |
| Confirm the paper's exact title | review #14 | **done** — verified from the journal title page image, and the operator's recollection was correct; no change needed |
| Hold until `CT-S18-COLDREAD-C3` returns | review #14 | **done** — returned; task 1 **independently reproduced** the correction from the page images alone, in its own code, obtaining the same residual factorisation. The typo row is now `cold`. |
| Confirm the authors' current address from a university page, not the paper | review #14 | **operator's** — not done by this session |
| Send | — | **operator's.** This session must not send anything. |

The bracketed entry is now filled, from `TYPO-EVIDENCE.md` §2. Everything else is
the operator's text, unaltered.

---

Subject: Possible typo in family (4.1), Ann. Inst. Fourier 59 (2009), p. 2655

Dear Professors van der Put and Saito,

I have been working with your paper "Moduli spaces for linear differential
equations and the Painlevé equations", Ann. Inst. Fourier 59 (2009), no. 7,
2611–2667, and I believe there is a small typographical error in the family (4.1)
on p. 2655.

The entry b(z) appears to be missing a factor of t in its first term:

    printed:    − z ( (p + ½(q−1)q)²  − θ₁²/4 + (q−1)(θ₀²/4 − θ₁²/4 − qθ∞²/4) ) / q  −  …

    corrected:  − z ( (p + ½(q−1)q t)² − θ₁²/4 + (q−1)(θ₀²/4 − θ₁²/4 − qθ∞²/4) ) / q  −  …

that is, (p + ½(q−1)q)² should read (p + ½(q−1)qt)². The second term of b(z),
which is not in question, carries (q−1)qt in both of its factors.

What persuaded me is not a constraint but your own page. The same bracket appears
a second time on p. 2655, in the matrix B₁ of the display B = zB₀ + (1/t)B₁, and
there it is printed **with** the t:

    B₁[1,2] = − ( (p + ½(q−1)q t)² − θ₁²/4 + (q−1)(θ₀²/4 − θ₁²/4 − qθ∞²/4) ) / q

Under the corrected reading, b(z)'s first term is exactly z · B₁[1,2]; under the
printed reading it is not. So the expression appears to be written correctly a
few lines below the place where the t is missing.

This is independently confirmed by your constraint det A(1) = −θ₁²/4. The printed
form does not satisfy it; the corrected form satisfies it identically. The
residual between the two readings factors as

    −(q−1)(t−1)(4p + q²t + q² − qt − q)/4 ,

so the two agree exactly at t = 1, which is the pattern one expects from a
dropped t — and the same factor appears in the comparison with B₁ above. (The
companion constraint det A(0) = −θ₀²/4 holds for both readings, so it does not
distinguish them.)

The same entry appears in arXiv:0902.1702v5, p. 34, so it seems to have survived
the revision of Section 4. I could not find a published erratum.

I am using the corrected form in work in preparation and would rather check with
you than assume I am right.

With thanks and best regards,

Papanokechi
Independent researcher, Yokohama
ORCID 0009-0000-6192-8273

---

## Note for the operator before sending

The claim in the letter is **VERIFIED**, not PROVEN: a symbolic check that one
reading satisfies a printed constraint and matches a second printed occurrence of
the same expression, while another reading does neither. It does not establish
what the authors intended. The letter is worded accordingly ("appears to be",
"would rather check with you"), and that wording should not be strengthened.

The `B₁` corroboration was added after the letter was first drafted and is the
stronger of the two arguments, since it appeals only to the authors' own page and
not to the correctness of any constraint. It now leads the letter.
