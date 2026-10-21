# REPORT.md — CT-S8-LITCHECK

Session: `sessions/2026-09-17/CT-S8-LITCHECK/`
HEAD at start: `08aa0e2381b3dc37ee54a3200b7272755ca11d59` — verified.
HEAD at end: see §6. Nothing committed, pushed, tagged, deposited or submitted.

## 1. What was done

Literature check on the novelty of three claimed results about the Wallis/continued-fraction
denominator recurrence `Q_n = b(n)Q_{n-1} + Q_{n-2}` for polynomial `b` of degree `d >= 1`.
Deliverable: `PRIOR-ART.md`.

Work performed:
1. Verified repo HEAD; created the session folder only.
2. Fetched and text-extracted 7 open sources into `refs/` (see `PRIOR-ART.md` §3 for full
   bibliographic data, URLs, retrieval date 2026-09-17 and sha256 of every file).
3. Read DLMF §2.9 and §3.6 in full; traced DLMF's own pointer for growing-coefficient equations
   (eq. 2.9.14) to Wong & Li (1992a) via the DLMF bibliography.
4. Located and read Gautschi's 1967 SIAM Review survey (author-hosted scan). The pypdf OCR is
   lossy for Greek letters, so the critical Theorem 2.3 was re-read from a rendered **page image**
   (`refs/g1967_p35_mid.png`) before quoting, and likewise its reference list (`refs/g_p58_bot.png`).
5. Obtained Birkhoff–Trjitzinsky (1933) from Project Euclid's open archive and read §9.
6. Obtained Nemes (2026, arXiv:2508.15246) for the modern Borel/hyperasymptotic framing and for
   documentary evidence on undetermined connection coefficients.
7. Independently verified results 1–3 numerically at 60 dps for four polynomials
   (`scripts/verify_growth_law.py`), including deriving and confirming the explicit
   `K = r_inf (2π)^{(d-1)/2} / (√d ∏_i Γ(1-r_i))`.

## 2. Findings, with labels

| # | Claim | Label |
|---|---|---|
| 001 | Gautschi 1967 Thm 2.3 (Perron–Kreuser) statement, p. 35, with verbatim quote | INSPECTED |
| 002 | Our recurrence lies in case (a) of that theorem; result 1 is an immediate corollary | PROVEN (from 001 + Stirling/Cesàro) |
| 003 | DLMF §2.9 gives explicit exponents only in the bounded-coefficient case, and defers the growing case to Wong & Li (1992a) | INSPECTED |
| 004 | Identification of Wong & Li 1992a/1992b; 1992a is paywalled (HTTP 403) | INSPECTED |
| 005 | Birkhoff–Trjitzinsky 1933 Fundamental Theorem, p. 69 — existence/shape only | INSPECTED |
| 006 | Nemes 2026: connection coefficients "often treated as unknowns in other methods" | INSPECTED |
| 007 | Borel machinery for difference equations is established, but Nemes's rank-one hypothesis excludes our equation for `d >= 2` | INSPECTED |
| 008 | (H) = Pincherle-type minimality condition; classical (Gautschi Thm 1.1, p. 31; DLMF §3.6(ii)) | INSPECTED |
| 009 | Numerical verification of R1, R2 (with `s = β_{d-1}/β_d + (d-1)/2`) and R3 (closed-form `K`) | VERIFIED |
| 010 | NOT FOUND, in the stated scope and by the stated method: an explicit closed-form amplitude, or the `Σ Q_n w^n/Γ(dn+1)` radius framing | INSPECTED (absence, scoped) |
| 011 | Perron 1913 obtained but unsearchable (no OCR layer); Perron 1911 / Pincherle 1892 / Birkhoff 1930 not obtained (bot-blocked) | INSPECTED |

**Bottom line.** The operator's working hypothesis is *partly* confirmed and *partly* sharpened:

- **Result 1 IS classical.** It is a two-line corollary of the Perron–Kreuser theorem, and I can
  give chapter and verse: Gautschi, *SIAM Rev.* 9 (1967), Thm. 2.3(a), p. 35. The note should
  say so and stop claiming it.
- **Result 2's *shape* is classical** (Birkhoff–Trjitzinsky normal solutions; DLMF §2.9). Whether
  the *explicit exponent* `s = β_{d-1}/β_d + (d-1)/2` is already in print could **not** be
  settled, because the one reference DLMF names for exactly this equation class
  (Wong & Li 1992a) is paywalled.
- **Result 3 (explicit `K`) is the strongest novelty candidate.** Classical theory normalises
  formal solutions and leaves the connection coefficient free; the only modern treatment I found
  that addresses it (Nemes) computes such constants *numerically*, not in closed form.
- **The Borel framing is the weakest novelty claim.** Borel transforms are standard in this
  field; the `Σ Q_n w^n/Γ(dn+1)` statement is a repackaging of result 1 and should be presented
  as expository.

## 3. What was NOT established

- Whether Wong & Li (1992a) already prints `s` explicitly in terms of the coefficients. **Open.**
- Whether Perron (1911) went beyond a ratio asymptotic. **Open** (source not obtained).
- Whether Perron's *Kettenbrüche* contains a `Q_n / ∏b(k) → r_inf` statement. **Open** (scan
  obtained but not machine-searchable).
- Whether Elaydi / Kooman / Van der Cruyssen / Wimp App. B contain anything sharper. **Open.**
- No claim is made that results 2/3 or the Borel framing are absent from the literature at large;
  all absence statements in `PRIOR-ART.md` are scoped to the named files and methods.

## 4. Open questions for the operator

1. **Can you obtain Wong & Li, *Stud. Appl. Math.* 87 (1992) 289–324 through an institutional
   subscription or interlibrary loan?** This is the single blocking item for a defensible novelty
   claim on result 2. I could not fetch it without bypassing a paywall, which governance forbids.
2. Same for Wimp, *Computation with Recurrence Relations* (1984), Appendix B, and Elaydi ch. 8.
3. Would you like a retry window for Project Euclid (Perron 1911, Pincherle 1892, Birkhoff 1930)?
   The host IP-throttled this session after one successful download; a later session from the same
   machine will probably succeed.
4. Do you want OCR run over `refs/perron1913.pdf` (541 pp., JBIG2/JP2 images, needs `jbig2dec` +
   a Fraktur-capable OCR engine)? That is a non-trivial job and I did not attempt it.
5. Recommendation for the note: demote result 1 to "recalled, classical (Perron–Kreuser)", present
   result 2 as "the classical expansion made explicit", and foreground result 3 + the vacuity
   explanation as the contribution — subject to item 1.

## 5. Uncommitted files created (all inside the session folder; nothing outside was touched)

```
sessions/2026-09-17/CT-S8-LITCHECK/PRIOR-ART.md
sessions/2026-09-17/CT-S8-LITCHECK/REPORT.md
sessions/2026-09-17/CT-S8-LITCHECK/claims.jsonl
sessions/2026-09-17/CT-S8-LITCHECK/scripts/verify_growth_law.py
sessions/2026-09-17/CT-S8-LITCHECK/scripts/verify_growth_law.out
sessions/2026-09-17/CT-S8-LITCHECK/refs/bt1933.pdf
sessions/2026-09-17/CT-S8-LITCHECK/refs/bt1933.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/dlmf_2_9.html
sessions/2026-09-17/CT-S8-LITCHECK/refs/dlmf_2_9.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/dlmf_3_6.html
sessions/2026-09-17/CT-S8-LITCHECK/refs/dlmf_3_6.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/g1967_p35_mid.png
sessions/2026-09-17/CT-S8-LITCHECK/refs/g_p58_bot.png
sessions/2026-09-17/CT-S8-LITCHECK/refs/g_p58_top.png
sessions/2026-09-17/CT-S8-LITCHECK/refs/gautschi1967.pdf
sessions/2026-09-17/CT-S8-LITCHECK/refs/gautschi1967.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/nemes2025.pdf
sessions/2026-09-17/CT-S8-LITCHECK/refs/nemes2025.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/p1913_4.png
sessions/2026-09-17/CT-S8-LITCHECK/refs/p1913_title.png
sessions/2026-09-17/CT-S8-LITCHECK/refs/perron1913.pdf
sessions/2026-09-17/CT-S8-LITCHECK/refs/perron1913.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/polycf.pdf
sessions/2026-09-17/CT-S8-LITCHECK/refs/polycf.txt
sessions/2026-09-17/CT-S8-LITCHECK/refs/wang_jat2014.pdf
sessions/2026-09-17/CT-S8-LITCHECK/refs/wang_jat2014.txt
```

(`refs/perron1913.txt` is an empty-of-content extraction artefact: the scan has no text layer.)

## 6. Governance

- No `git add`, `commit`, `push`, `tag`, PR, deposit or submission was performed.
- No file outside `sessions/2026-09-17/CT-S8-LITCHECK/` was created or modified.
- Only open-access / freely-hosted sources were fetched. Search engines surfaced sci-hub mirrors
  for Wong & Li and for Birkhoff–Trjitzinsky; these were **not** used.
- HEAD re-verified at end of session: see the final `git --no-pager rev-parse HEAD` output
  recorded in the session transcript (`08aa0e2381b3dc37ee54a3200b7272755ca11d59`).
