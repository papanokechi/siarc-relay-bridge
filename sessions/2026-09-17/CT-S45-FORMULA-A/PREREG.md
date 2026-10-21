# PREREG — CT-S45-FORMULA-A

Formula re-derivation pass, Appendix A. Written **before** any computation in
this session. The page images were inspected first (inspection, not
computation); the transcription that inspection produced is recorded in §3 and
is itself under test.

---

## 1. Hypothesis

Every displayed formula in `appendixA.tex` is correct, and each is verifiable by
exactly one of two routes:

- **route P (page)** — the expression is a transcription from a printed source.
  It is verified against the page image, with the folio read off the page.
- **route S (script)** — the expression is the output of a symbolic computation.
  It is re-derived from the source expressions and compared symbolically.

An equation with **neither** route available is itself the finding, and is
reported as `NO ROUTE`.

## 2. Observable

Per displayed expression, a verdict in
`{MATCHES-PAGE, MATCHES-SYMBOLIC, DIFFERS, NO ROUTE}`
together with, for route S, the symbolic residual `printed_form - rederived_form`
normalised by `sympy.simplify`, which must be exactly `0`.

## 3. Falsifiers, with thresholds

- **F1** Any route-S expression whose residual is not identically `0`.
  Threshold: exact zero over `QQ(p,q,t,theta0,theta1,thetainf)`. No tolerance —
  these are rational functions, not floating point.
- **F2** Any route-P expression differing from the page in any symbol, including
  sign, subscript, or relation (`=` versus `\cong`).
- **F3** The appendix's closing scope note asserts that *no* formula in it was
  re-derived from a computation, "because there is no such computation." If any
  displayed expression is found to be route S, that note is false. **Predicted
  to fire**: `S16-20`'s residual and `S16-R18-02`'s difference polynomial are
  plainly computational, and `S16-20` carries `evidence_type: computation`.
- **F4** The two displayed forms of the difference between readings —
  unfactored `+1/4 z(...)` and factored `-1/4 z(q-1)(t-1)(...)` — differ in
  sign. Hand expansion of the `4p` terms gives `4pqt-4pq-4pt+4p`, matching the
  unfactored form, so the factored form's leading minus is predicted wrong.
  **Recorded before computing.**

## 4. Vacuity pre-check

The instrument must move when the thing it measures moves.

- **V1 (positive)** The corrected reading `(p+1/2(q-1)q t)^2` must make
  `det A(1) + theta1^2/4` vanish identically. If it does not, the reader has
  mis-transcribed `a`, `b` or `c` and no verdict below is meaningful.
- **V2 (negative)** The printed reading `(p+1/2(q-1)q)^2` must leave a non-zero
  residual. If both readings pass, the test does not discriminate and the
  appendix's argument is void.
- **V3 (control)** The bogus variants `(q-1)q t^2`, `(q-1)q (t+1)` and
  `(q-1)q (2t)` must each be **rejected**. A test that accepts only the
  corrected reading and is silent on everything else establishes consistency,
  not discrimination. Drawn from outside the appendix's own list where possible.
- **V4 (reader)** `det A(0) + theta0^2/4` must vanish for **both** readings.
  The appendix asserts this test does not discriminate; if it does discriminate
  in my transcription, my `A(z)` is wrong.

If V1 or V2 fails, HALT: the transcription is the defect, not the appendix.

## 5. What this pass does NOT establish

- It does not check prose, only displayed mathematics.
- Route P is inspection of a rendered image by eye. It is `INSPECTED`, never
  `VERIFIED`, and never `PROVEN`.
- A route-S agreement proves the appendix's formula matches **my**
  re-derivation from **my** transcription of the page. It does not
  independently prove the source page is correct.

## 6. Standing rule adopted for this pass

Per the operator's ruling on `S44-17`: a numeric or symbolic figure is
confirmed by resolving it to the **specific display that reports it**, never by
searching an evidence file for a matching string. Every verdict below names the
expression it tested.
