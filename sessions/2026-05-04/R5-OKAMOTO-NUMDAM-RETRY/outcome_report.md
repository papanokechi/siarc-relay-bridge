# R5-OKAMOTO-NUMDAM-RETRY — Outcome Report

**Date:** 2026-05-04
**Task class:** Operator-side acquisition retry (NOT AEAL relay)
**Hard time cap:** 10 min — respected
**Target:** Okamoto, K. "Studies on the Painlevé equations IV. Third
Painlevé equation P_III." *Funkcialaj Ekvacioj* **30** (1987), 305–332.
**Slot:** `literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf`

---

## OUTCOME

**`OUTCOME_R5RT_NUMDAM_ACQUIRED`** ✅

Hybrid resolution: NUMDAM probe failed (the prior agent's
"NUMDAM hosts FE" recommendation was incorrect — NUMDAM is
French-math-focused and does not carry the Japanese FE
journal). Operator surfaced the actual canonical OA route —
the **Kobe University FE journal direct PDF URL** — and the
file acquired and verified cleanly.

  Source:  `http://fe.math.kobe-u.ac.jp/FE/FE_pdf_with_bookmark/FE21-30-en_KML/fe30-305-332/fe30-305-332.pdf`
  Saved to: `tex/submitted/control center/literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf`
  SHA-256:  `65294fbca97e3ce1db0ea193dcd3048d9a2942db2ae6d435c9bdfacc2b78a43f`
  Size:     6,075,525 bytes (5.79 MB), 28 pages

---

## Strengthened verification (per prior agent's lesson learned)

Title page (pypdf-extracted, verbatim):
> "Funkcialaj Ekvacioj, 30 (1987) 305-332
> Studies on the Painleve Equations IV .
> Third Painleve Equation P_{III}
> By Kazuo OKAMOTO (University of Tokyo, Japan)"

| Check                | Required             | Observed                                  | Result |
|----------------------|----------------------|-------------------------------------------|:------:|
| Series part          | "IV"                 | "Studies on the Painleve Equations IV"    | ✅ |
| Painlevé equation    | III / P_III          | "Third Painleve Equation P_{III}"         | ✅ |
| Author               | Kazuo Okamoto        | "Kazuo OKAMOTO"                           | ✅ |
| Journal              | Funkcialaj Ekvacioj  | "Funkcialaj Ekvacioj"                     | ✅ |
| Volume               | 30                   | "30"                                      | ✅ |
| Year                 | 1987                 | "(1987)"                                  | ✅ |
| Pages                | 305–332              | "305-332"                                 | ✅ |
| Page count           | ~28 (article 305–332)| 28                                        | ✅ |
| %PDF magic bytes     | `25 50 44 46`        | `25 50 44 46 2D 31 2E 33` (PDF-1.3)       | ✅ |

**All 9 verification checks PASS.** No risk of Part-I/Part-IV
confusion (the failure mode that doomed the prior R5 retry).

PDF metadata: Creator=`LaTeX with hyperref package`,
Producer=`dvipdfmx (20021230)`, CreationDate `2005-11-19 21:11:11
+09'00'` — consistent with a LaTeX-source modern typesetting of
the 1987 Okamoto article generated in Japan timezone, likely as
part of Kobe University's FE backlist digitization project.

---

## Contents (from page 1 TOC)

- §1 Painlevé system (P_{III'} and P_{III}, auxiliary Hamiltonian)
- §2 Transformation group of P_{III'} — affine Weyl group W of **B_2** root system, involution of E, parallel transformation l, realization of s_0 as canonical transformation
- §3 Toda equation and τ-function
- §4 Cylinder function and Painlevé transcendental function

The Lax-pair / canonical-Hamiltonian normalisation requested by
`CC-VQUAD-PIII-NORMALIZATION-MAP` is in §1 (Painlevé system).
**Caveat:** Okamoto 1987 uses the **W(B_2)** convention; the
slot-08 Barhoumi-Lisovyy-Miller-Prokhorov 2024 paper uses
**W(D_6)** / D_6→D_8 confluence convention. Cross-walking these
is part of the M6 closure's mapping work, not a blocker — both
conventions describe the same P_III modulo a known type
correspondence.

---

## Aggregate scenario after acquisition

**SCENARIO B confirmed** (2 of 3 acquired):

| Slot | Source                                           | Status                       |
|------|--------------------------------------------------|------------------------------|
| 07   | Okamoto FE 30 (1987) P_III — *target*            | ✅ ACQUIRED (this session)   |
| 08   | Lisovyy / Barhoumi-Lisovyy-Miller-Prokhorov 2024 | ✅ acquired (prior R5)       |
| 09   | Conte-Musette 2008 ch. 7                         | ❌ SCENARIO_C-accepted        |

Plus supplementary (preserved from prior R5 retry, not a slot):
| —    | Okamoto Part I (P_VI), Ann. Mat. CXLVI (1987)    | ✅ supplementary             |

---

## M6 status

Per task spec §2 step 6:

> **Aggregate: SCENARIO B (2 of 3 acquired)**
> **M6 status: prospects strengthened; primary Lax pair source available**

`CC-VQUAD-PIII-NORMALIZATION-MAP` can fire when M4 disposition
lands without ethics-gate framing for Okamoto. The closure
plan should include an explicit B_2 ↔ D_6 affine-Weyl
cross-walk as a sub-step (Okamoto 1987 for canonical
Hamiltonian Lax pair; Barhoumi-Lisovyy-Miller-Prokhorov 2024
for D_6 monodromy data).

The earlier "Path α / β / γ" option set from the
PROJECT-EUCLID-RETRY handoff collapses to the cleanest path:
fire M6 with full citations when M4 disposition lands.

---

## 10-minute time cap

Respected. Sequence:
1. NUMDAM specific-item URL probe → 404
2. NUMDAM fallback URL pattern probes (5 URLs) → all 404
3. NUMDAM root + journal-list scan → confirmed FE not hosted
4. Operator-supplied Kobe-U URL fetch → 5.79 MB PDF in ~3 sec
5. Strengthened verification (all 9 checks pass)
6. Slot 07 save + SHA + SHA256SUMS amendment + self-verify (PASS 11/11)
7. Bridge handoff drafting + commit

Total: well under 10-minute cap.

---

## Lesson learned for future literature acquisition

The prior R5-OKAMOTO-PROJECT-EUCLID-RETRY agent's recommendation
that NUMDAM hosts Funkcialaj Ekvacioj backlist was **incorrect**.
NUMDAM hosts primarily French math journals (full /journals/
listing has ~50 entries: AIF, BSMF, CM, PMIHES, etc.) and does
not carry Japanese math journals. Future R5-style prompts
targeting Japanese math journals (FE, J. Math. Soc. Japan,
Proc. Japan Acad., Sugaku, Hiroshima Math. J., Hokkaido Math. J.,
etc.) should try the **publishing institution's direct site
first** before generic OA aggregators:

  - Funkcialaj Ekvacioj → Kobe Univ (`http://fe.math.kobe-u.ac.jp/FE/`)
  - J. Math. Soc. Japan → Project Euclid (here Project Euclid does work)
  - Proc. Japan Acad. → Project Euclid

This finding is recorded in `unexpected_finds.json` for the
synthesizer's reference.
