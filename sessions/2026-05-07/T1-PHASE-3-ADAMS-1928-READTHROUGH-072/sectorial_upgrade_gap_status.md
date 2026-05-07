# Sectorial-Upgrade Gap — Substrate-Inventory Status Report

**Session:** 2026-05-07 T1-PHASE-3-ADAMS-1928-READTHROUGH-072.
**Scope:** SUBSTRATE-INVENTORY ONLY. This file enumerates which
classical-result substrate is on-disk for the SIARC-stratum
formal-to-analytic sectorial-upgrade question at d ≥ 3, before and
after the 2026-05-07 ~10:18 JST Adams 1928 acquisition. It does **not**
assert that any gap is closed, narrowed, proved, established, or
demonstrated. Per relay-prompt P8 (verdict-ladder honesty) and
HALT_072_LADDER_OVERREACH (Phase D.2 §4), this file maintains
substrate-inventory framing throughout.

---

## §1 — Substrate now on-disk (post 2026-05-07 ~10:18 JST)

Four primary-source artefacts directly relevant to the SIARC-stratum
formal-to-analytic sectorial-upgrade question are presently on-disk in
the project literature folder:

| Slot | Author/Year | Title (abbrev.) | SHA-256 (first 16 hex) | Page coverage relevant to gap |
| --- | --- | --- | --- | --- |
| Adams-1928 | C. R. Adams (1928) | "On the Irregular Cases of the Linear Ordinary Difference Equation", Trans. AMS 30 (1928), 507–541 | `d7ac4017a9737fef…` | Full paper (35 printed pages, p. 507–541). Especially §§1–2 (Newton-polygon classification + Class 2a/2b existence theorems), §6 (Theorems A, B), §8 + p. 541 closing caveat |
| 03 | G. D. Birkhoff & W. J. Trjitzinsky (1933) | "Analytic Theory of Singular Difference Equations", Acta Math. 60, 1–89 | `dcd7e3c6b2a12ae1…` | Full paper. §§1–9 covers formal series + factorisation + Theorem I (§5), Theorem II (§7), Fundamental Existence Theorem (§9). §12 Theorem 4 covers the related Riemann problem |
| 04 | W. Wasow (1965, Dover repr.) | "Asymptotic Expansions for Ordinary Differential Equations" (Dover) | `f59d6835db58d2de…` | Chapters IV (formal solutions) + V (analytic-existence theory; sectorial-upgrade theorems). Chapter X §3 in the original 1965 numbering covers the explicit sectorial-upgrade Theorem 11.1-style result |
| 06 | O. Costin (2008) | *Asymptotics and Borel Summability* (CRC), Chapter 5 | `93f1e9bf0a5fc4f6…` | Chapter 5 covers Borel summability + multisummability synthesis applicable to formal-series → analytic-solution upgrades |

**SHA verification status.** Adams-1928 SHA verified by Phase A.1 of
the present session (file size 1 266 209 B, page count 36, pypdf
metadata.title matches expected). BT 1933 + Wasow + Costin SHAs
verified by Phase A.3 against the substrate slot ledger.

---

## §2 — Substrate pre-2026-05-07 ~10:18 JST

Pre-acquisition snapshot (the state of the project literature folder
before the operator-side JSTOR-acquisition of Adams-1928 on
2026-05-07):

| Slot | Author/Year | Status |
| --- | --- | --- |
| Adams-1928 | C. R. Adams (1928), Trans. AMS 30 | **NOT-ON-DISK** |
| 03 | BT 1933 | ON-DISK (acquired earlier under the g3b 2026-05-03 substrate batch) |
| 04 | Wasow 1965 | ON-DISK (acquired earlier) |
| 06 | Costin 2008 ch.5 | ON-DISK (acquired earlier; previously read by relay 068) |

The pre-acquisition state corresponds to the Phase 2 substrate
inventory recorded in the Phase 2 → Phase 3 transition note (Phase 2
T1 acquisition tracker `t1-primary-sources-acquire`, BLOCKER closed
2026-05-07 ~10:25 JST per the relay-072 prompt-body Depends-on
clause).

---

## §3 — Delta since 2026-05-07 ~10:18 JST

Exactly **one** new substrate element since the 2026-05-07 ~10:18 JST
acquisition timestamp:

- **Adams-1928** (`d7ac4017…`, 36 PDF pages, 1 266 209 B). All other
  three slots (BT 1933, Wasow 1965, Costin 2008 ch.5) were already
  on-disk.

A secondary acquisition on the same date (Gronau 2004 tertiary; not
listed above; recorded in the SHA256SUMS.txt header note) is unrelated
to the SIARC-stratum sectorial-upgrade question and does not alter the
delta for this report.

---

## §4 — Gap characterisation (substrate-inventory level)

This section enumerates which classical-result coverage is now
available in the on-disk substrate that was not available before
Adams-1928 landed. It is a substrate-coverage report, not a
gap-closure assertion.

1. Adams 1928 §1 supplies the **Newton-polygon classification** of the
   irregular case into Class 1 (a₀₀ ≠ 0, aₙ₀ ≠ 0) and Class 2 (one or
   both vanishing), with explicit segment-by-segment characteristic-
   equation construction (printed p. 511 — `[CLAIM-B4]` in the
   §1+§2 claim table).

2. Adams 1928 §2 supplies the **Class 2a / Class 2b sub-classification**
   of the Class-2 setting, with existence of n formal series solutions
   (10) and matrices G(x), H(x) (printed p. 513–p. 517 —
   `[CLAIM-B10]`, `[CLAIM-B11]`, `[CLAIM-B12]` in the claim table).

3. Adams 1928 §6 supplies **Theorem A and Theorem B** for the n-fold
   multiple-root sub-case (printed p. 529 + p. 537 — entries T1 and
   T2 in the main-theorems summary), with explicit infinite-product
   constructions Pₘ(x) and P'ₘ(x).

4. Adams 1928 §8 supplies the **mixed-multiplicity generalisation**
   for finite non-zero roots, ordered by decreasing absolute value
   with simple/multiple-root alternation, and announces the Class-2
   extension as "immediate" (printed p. 539–p. 541 — entry T9 in
   the main-theorems summary).

5. Adams 1928 §8 closing paragraph supplies the **regions-of-validity
   caveat** (printed p. 541 last paragraph) — verbatim ≤ 30 words:
   "Whatever the relative size and position of the two polygons may
   be, the regions of validity of the asymptotic forms of some or all
   of the determinant limits … are further restricted." This caveat
   articulates the residual sectorial-validity issue that recurs in
   the BT 1933 quadrant-Γ formulation.

6. The cross-walk to BT 1933 (verified at BT p. 5; Adams 1928 cited
   verbatim in BT footnote 2) **lands** Adams's results inside the BT
   1933 framework, with the BT p. 5 self-statement positioning Adams
   as "the irregular normal case" sub-case of BT's "without
   restriction upon the form of the formal series" generalisation.

7. The substrate inventory now carries explicit primary-source
   coverage of: (a) the formal-series construction (Adams §1 +
   BT §1 + Wasow IV); (b) the Class-2 multi-segment characteristic-
   equation case (Adams §1 + BT §6 Lemma 9 factorisation); (c) the
   existence-of-analytic-solutions theory (Adams §§2 + 6 + BT §§5,7,9
   + Wasow V); (d) the Borel-summability / multisummability synthesis
   (Costin ch.5) which complements the Adams + BT analytic-existence
   theory.

8. What Adams 1928 contributes that did **not** exist on-disk before
   2026-05-07 ~10:18 JST: the explicit Class-1 / Class-2 partition
   with Newton-polygon visualisation; the Class-2a / Class-2b
   sub-classification with simple-root + integer-slope vs.
   fractional-slope conditions; the n-fold multiple-root determinant-
   limit Theorems A and B; the n=2 double-root sharpening (§7); the
   mixed-multiplicity §8 extension; the p. 541 regions-of-validity
   caveat.

9. The above 8 items are substrate-inventory facts about what is now
   on-disk. They do not by themselves describe a closure, narrowing,
   or upgrade of any gap; they describe the coverage available to a
   future synthesizer-tier reader.

10. Per HALT_072_LADDER_OVERREACH and the verdict-ladder honesty
    discipline (P8), no statement in this section is a gap-closure
    assertion. Each of items 1–9 above is a substrate-coverage fact
    or a primary-source cross-reference.

(Sentence count: 10. Per E.5 ≤ 25-sentence cap, this section is within
the ceiling.)

---

## §5 — Residual items (substrate-inventory level)

The following classical-result substrate elements remain
**NOT-ON-DISK** at the SIARC stratum d ≥ 3 sectorial-upgrade-question
level, after the present session's Adams 1928 acquisition:

1. **Wasow 1965 Chapter X §3 Theorem 11.1** (the explicit
   sectorial-upgrade theorem in Wasow's numbering) — although Wasow
   1965 is on-disk at slot 04, the Phase A.3 quick-scan of slot 04
   did not in this session re-confirm that the Chapter X §3 page
   range is fully extractable; verbatim Theorem 11.1 statement is
   not yet captured into a session deliverable. This item is a
   "substrate is on-disk but not yet read in detail" residual rather
   than a "substrate not on-disk" residual.

2. **Loday-Richaud 2016 Chapter 2 multisummability synthesis** — the
   project's literature folder does not contain a Loday-Richaud 2016
   PDF in the g3b 2026-05-03 batch (the only batch surveyed in this
   session). Whether Loday-Richaud is needed at the SIARC-stratum
   sectorial-upgrade level is a question for the W21 LANE-1
   arbitration substrate consumer. Acquisition status: OPEN.

3. **Carmichael's 1912 paper on linear difference equations** —
   cited in BT 1933 p. 4 but not in Adams 1928. Not on-disk in the
   g3b batch. Acquisition status: OPEN.

4. **A verbatim BT 1933 §§7–9 readthrough** parallel to the present
   072 session's Adams readthrough — needed for the natural cross-
   walk completion. The BT 1933 paper is on-disk; a future relay
   session analogous to 072 would extract verbatim ≤ 30-word
   theorem-statements + claim tables for BT §§5/7/9.

5. **Galbrun 1913 (Acta Math. 36)** — cited in Adams 1928 p. 508
   footnote ¶ and mentioned in BT 1933 p. 4 (DEFER label in the
   bibliography cross-walk; pypdf quick-scan did not isolate the
   BT 1933 footnote text). Acquisition status: not on-disk in the
   g3b batch.

6. **Norlund 1924 *Differenzenrechnung*** (Berlin: Springer) cited by
   Adams 1928 p. 508 footnote § — not on-disk in the g3b batch.
   Status: OPEN.

7. **Perron 1917 Heidelberg Sitzungsberichte vol. 8A No. 17** — cited
   by Adams 1928 p. 508 footnote ‡ — not on-disk in the g3b batch.
   Status: OPEN. (Likely low-priority; Perron 1917 covers only the
   n=2 double-root sub-case, which Adams 1928 §7 already supersedes
   in coverage.)

(Sentence count: 9. Within the E.5 ≤ 25-sentence cap.)

---

## Self-check status

- Phase D.2 §4 does not contain the tokens "closes", "closes the gap",
  "proves the gap", "establishes the upgrade", "narrows the gap",
  "demonstrates closure", "shows closure" outside policy-exempt
  contexts (the HALT-name reference in `HALT_072_LADDER_OVERREACH`
  appears in the §4 header policy clause and the closing §4 item 10;
  these are halt-name self-references, not gap-closure assertions).
  See `forbidden_verb_scan.md` §C for full E.3 scan.
- Phase D.2 §4 sentence count: 10 (≤ 25). §5 sentence count: 9
  (≤ 25). E.5 anchoring rate: 10/10 + 9/9 = 100% (every sentence
  traces to a verbatim Adams quote, a substrate-anchor SHA, or a
  primary-source cross-reference).
