# Route probe log — ADAMS-1928-FINAL-ACQUISITION-PROBE

**Date:** 2026-05-04
**Target article:** C. R. Adams, "On the irregular cases of the linear ordinary
difference equation", Trans. Amer. Math. Soc. **30** (1928), no. 3, 507–541.
**Canonical PII:** `S0002-9947-1928-1501443-6`
**Canonical DOI:** `https://doi.org/10.1090/S0002-9947-1928-1501443-6`
**JSTOR stable:** `https://www.jstor.org/stable/1989257`
**Erratum:** Trans. Amer. Math. Soc. 30 (1928), 855 (PII `S0002-9947-1928-1500505-7`).

**Spec note (bibliographic correction).** The relay-prompt §2 Phase A.1 cites
DOI `10.1090/S0002-9947-1928-1501457-9` for Adams 1928. That PII is a different
article in the same volume (Trans. AMS 30, 1928). The actual Adams 1928 PII is
`S0002-9947-1928-1501443-6`, confirmed against the issue TOC at
<https://pubs.ams.org/journals/tran/1928-030-03>. All probes below use the
corrected PII.

---

## Routes probed (per spec §2 Phase B)

| Route | URL probed                                                                                                              | HTTP | Content-Type        | Acquisition |
|-------|-------------------------------------------------------------------------------------------------------------------------|------|---------------------|-------------|
| B.1   | `https://pubs.ams.org/journals/tran/1928-030-03/S0002-9947-1928-1501443-6/`                                             | 200  | text/html           | landing page; only `/Account/Login?returnUrl=...` link to PDF surface, no direct `<a href="*.pdf">` |
| B.1.a | `https://pubs.ams.org/journals/tran/1928-030-03/S0002-9947-1928-1501443-6/S0002-9947-1928-1501443-6.pdf`                | 200  | text/html (8.04 MB) | NOT a PDF — server returned the AMS HTML viewer wrapper (file begins `<!DOCTYPE html>`, byte-magic check fails pypdf header) |
| B.1.b | `https://pubs.ams.org/view?ProductCode=tran&directory=1928-030-03&pii=s0002-9947-1928-1501443-6`                        | 200  | text/html           | login-redirect viewer; same HTML payload as B.1.a |
| B.2   | `https://www.jstor.org/stable/1989257`                                                                                  | 200  | text/html           | JSTOR landing page; "Have library access?" gate; no Early-Journal-Content open route exposed for this issue |
| B.3   | `https://archive.org/search.php?query=Adams+1928+irregular+cases+linear+difference+equation`                            | 200  | text/html           | 0 results |
| B.4–B.7| not probed (per operator instruction "no further route probes")                                                        | n/a  | n/a                 | n/a |

## AMS open-archive policy (verbatim, ≤30 words)

From the AMS Trans. AMS journal landing page:

> Free Digital Archive: Full article PDFs in all volumes older than five years
> are available electronically free of charge.

(Source: <https://pubs.ams.org/journals/tran/1928-030-03>, fetched 2026-05-04.)

Per AMS's own policy, Adams 1928 (volume 30, age 98 years) is in scope of free
electronic availability. The agent's HTTP-only fetch did not establish whatever
JS-rendered session-state the AMS viewer requires to stream the PDF; the
landing-page download surface routes through `/Account/Login?returnUrl=...`,
which per Rule 2 is operator-side only. A browser-driven fetch would resolve
the same URL successfully under operator control.

## Operator-side AMS retrieval (recommended one-step path)

Per Rule 2 (operator handles auth / interactive flows), the recommended
operator-side action is:

1. In a browser, visit
   <https://pubs.ams.org/journals/tran/1928-030-03/S0002-9947-1928-1501443-6/>.
2. Click "Article PDF" / "View in volume". (Per AMS policy this is free for
   volumes >5 years; no AMS membership login should be required.)
3. Save the PDF as
   `tex/submitted/control center/literature/g3b_2026-05-03/12_adams_1928_TransAMS30.pdf`.
4. Append the SHA-256 to `SHA256SUMS.txt` with provenance line
   "Slot 12 acquired YYYY-MM-DDTHH:MM:SSZ via AMS Free Digital Archive
   (Trans. AMS 30 (1928) 507–541, PII S0002-9947-1928-1501443-6)."
5. Verify by `pypdf` text extraction at §§1–3 (σ-normalisation establishment).

Once the operator surfaces the PDF, Phase D (cross-validation vs. T1-A01
transitive evidence) can fire as a follow-up task in a future relay session.

## Tier-2 ILL routes (if AMS-direct surprisingly fails for the operator)

In ranked order:

1. **Yokohama City Library** (operator local) — has digital ILL with
   Tokyo University and Keio; standard turnaround for pre-1929 AMS journal
   article.
2. **AMS Member Services** — if operator holds AMS membership; per AMS Free
   Digital Archive this should not be needed, so this is fallback only.
3. **Brown University Library ILL** — Adams was at Brown 1924–1955; Brown
   maintains digital archives of Brown-affiliated researchers; external
   borrower / ILL channel may apply if operator has any such privileges.

No ILL channel is auto-submitted on behalf of the operator (per Rule 2).
