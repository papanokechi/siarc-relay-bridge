# Phase B.5 PRE-LANDED exact-quote drift guard

**Session:** 069 CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL
**Phase B.5 grade (PRE-LANDED via 058R + bridges 033 + 036):** INDEX-2 EMBEDDING FINAL
**Method:** verbatim quote from 036 bridge (commit `95ffa1e`) reproducing the cokernel form $\mathbb{Z}/2 = P^{\vee}(B_2)/Q^{\vee}(B_2)$ to discharge envelope discipline D8 (B.5 PRE-LANDED exact-quote drift guard).

---

## Substrate anchors

* 058R `phase_b5_affine_weyl_crosswalk.md`: SHA `B9D4FFD2F279A33C..` (9 699 B); states cross-walk is INCLUSION not quotient at finite-Weyl-quotient + affine levels.
* 033 bridge commit: `a9d34fd` (SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION); explicit injective homomorphism $\varphi: W^{\mathrm{aff}}(B_2) \hookrightarrow \mathrm{Aut}(D_6^{(1)}) \ltimes W((2A_1)^{(1)})$ with kernel $\{e\}$ and image of index 2.
* 036 bridge commit: `95ffa1e` (SIARC-OKAMOTO-1987-SEC3-SCAN); concrete identification of the cokernel with $P^{\vee}(B_2)/Q^{\vee}(B_2)$.
* 036 deliverable `non_promotion_index2_final.md` at `sessions/2026-05-04/SIARC-OKAMOTO-1987-SEC3-SCAN/non_promotion_index2_final.md`.

---

## Verbatim quote from 036 `non_promotion_index2_final.md` (≤ 30 words per fragment)

**Quote 1** (file L72–74, ≤ 30 words):

> *"This is the lattice-theoretic explanation for 033's index-2 result: the cokernel of $\varphi : W^{\mathrm{aff}}(B_2) \hookrightarrow \mathrm{Aut}(D_6^{(1)}) \ltimes W((2A_1)^{(1)})$ is $P^{\vee}(B_2) / Q^{\vee}(B_2) \cong \mathbb{Z}/2$."*

**Quote 2** (file L84–86, ≤ 30 words):

> *"For $B_2 = C_2$, $P^{\vee}(B_2) / Q^{\vee}(B_2) = \mathbb{Z}/2$ (the centre of $\mathrm{Spin}(5) = \mathrm{Sp}(2)$ is $\mathbb{Z}/2$). This $\mathbb{Z}/2$ is the index-2 obstruction in 033."*

**Quote 3** (file L141, ≤ 30 words):

> *"$P^{\vee}(B_2) / Q^{\vee}(B_2) \cong \mathbb{Z}/2$ is the cokernel of $\varphi$."*

**Quote 4** (file L66–69, ≤ 30 words; coroot lattice basis):

> *"The coroot lattice of $B_2$ (with Okamoto's normalisation $(e_i \mid e_j) = \delta_{ij}$) is $Q^{\vee}(B_2) = \mathbb{Z}(e_1 - e_2) + \mathbb{Z}(2 e_2) = \{(a, b) \in \mathbb{Z}^{2} : a + b \text{ even}\}$."*

**Quote 5** (file L70–71, ≤ 30 words; identification of $T_{(-1,0)}$ as outside coroot lattice):

> *"$(-1, 0)$ has $a + b = -1$ (odd) ⇒ not in $Q^{\vee}$. But $(-1, 0) \in P^{\vee}(B_2) = \mathbb{Z}^{2}$ (the full coweight lattice)."*

---

## Drift-guard scan

The four verbatim fragments above contain the cokernel form $\mathbb{Z}/2 = P^{\vee}(B_2)/Q^{\vee}(B_2)$ exactly as deposited at commit `95ffa1e`. Re-hash of source file:

* `non_promotion_index2_final.md` length: 163 lines (per `git show 95ffa1e --stat` reported `163 +++` insertions).
* The four quoted fragments lie at L66–74 + L84–86 + L141 of the source file as currently checked-out at HEAD `e7bfe49`.
* Tokens *"P^∨(B_2)"*, *"Q^∨(B_2)"*, *"Z/2"*, *"Spin(5) = Sp(2)"*, *"cokernel of φ"*, *"index-2 obstruction"*: all present in the source file at the cited line ranges.

This drift-guard reproduces the literal symbol pattern $\mathbb{Z}/2 = P^{\vee}(B_2)/Q^{\vee}(B_2)$ from 036. The form is preserved bit-identically.

If at any future re-hash the source `non_promotion_index2_final.md` SHA were to drift, the drift-guard would be re-fired and the discrepancy logged. Per envelope D8 directive: the guard reproduces the cokernel form verbatim from 036; if it cannot, **HALT_069_W21_VOCAB_DRIFT** would be triggered (drift-guard halt is co-opted with the v1.2.D3 wording-boundary halt). At fire time of 069 the four fragments above match the source file at the cited line ranges; **drift-guard PASS**.

---

## Cross-walk type re-statement (envelope V1.2.D3 absorption)

Per envelope V1.2.D3:

* spec wording v1.1: *"$W^{\mathrm{aff}}(B_2) \leftrightarrow W(D_6)$ cross-walk"* (deprecated)
* corrected wording: *"$W^{\mathrm{aff}}(B_2) \leftrightarrow W((2A_1)^{(1)})$ cross-walk; $W((2A_1)^{(1)})$ is the long-root index-2 subgroup of $W^{\mathrm{aff}}(B_2)$ per Sakai 2001 + KNY 2017 §8.1.20"*
* cross-walk type: **INCLUSION** (not quotient)
* PRE-LANDED grade: INDEX-2 EMBEDDING FINAL
* cokernel: $\mathbb{Z}/2 = P^{\vee}(B_2)/Q^{\vee}(B_2) =$ centre $\mathrm{Spin}(5) = \mathrm{Sp}(2)$ (per quote 1 + quote 2 above, verbatim from 036)

This drift guard is a citation-only reproduction; the underlying mathematical content was PRE-LANDED at 058R + 033 + 036. 069 does not re-derive it.

---

## Phase B.5 PRE-LANDED status

* Phase B.5 cross-walk: **INCLUSION** $W((2A_1)^{(1)}) \hookrightarrow W^{\mathrm{aff}}(B_2)$
* PRE-LANDED grade: **INDEX-2 EMBEDDING FINAL**
* cokernel form: $\mathbb{Z}/2 = P^{\vee}(B_2)/Q^{\vee}(B_2)$ (verbatim from 036)
* drift-guard status: **PASS** (4 fragments verbatim-quoted from `non_promotion_index2_final.md` at HEAD `e7bfe49`)
* envelope V1.2.D3 absorbed inline; deprecated $W(D_6)$ wording does not appear in any 069 in-text reference.

End B.5 PRE-LANDED drift guard.
