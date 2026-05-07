# BT 1933 §§4-6 — Internal Cross-References

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**Page span:** Acta p. 29 (PDF p. 29) — p. 51 (PDF p. 51).

This file enumerates every cross-reference inside §§4-6 to other
sections of BT 1933 (§§1-3 setup; §§7-12 consumption) and to BT
1930 ("paper (II)" / "paper (I)", Acta Math. 54, 1930).

Notation:
- "Earlier" = §§1-3 (setup; §§4-6 cite for definitions / lemmas).
- "Later" = §§7-12 (consumption; §§4-6 are cited from later sections).
- "External" = the 1930 Birkhoff paper "Formal theory of irregular
  linear difference equations" (Acta Math. 54, 1930), referred to as
  "(II)" or "(I)" in BT 1933 footnotes.

## Earlier-section dependencies (§§4-6 → §§1-3)

| Cited from | Cite text | Cite target | Subject |
| --- | --- | --- | --- |
| §4 p. 29 | "the lower boundary of F (§ 2)" | §2 (proper curves; F definition) | proper-curve framework |
| §4 p. 30 | "(Def. 1; § 1)" | §1 Definition 1 | formal s-series definition |
| §5 p. 41 | "(2; § 1)" | §1 (eq. 2) | difference-equation form L_n(y) = 0 |
| §5 p. 41 | "(cf § 1)" | §1 | coefficient-class specification |
| §5 p. 41 | "F (§ 1)" | §1 | F = (1) + (2) + ... + (η) region |
| §5 p. 41 | "(Def. 9; § 1)" | §1 Def. 9 | proper-curve definition |
| §5 p. 41 | "(Def. 4; § 1)" | §1 Def. 4 | proper fundamental set of solutions |
| §5 p. 41 | "(Def. 6; § 1)" | §1 Def. 6 | completely-proper operator |
| §5 p. 41 | "(6; § 1)", "(6 a; § 1)" | §1 (eqs. 6, 6 a) | system Y(x+1) = D(x) Y(x) |
| §5 p. 42 | "(1 a; § 1)" | §1 (eq. 1 a) | system Y(x+1) = Z(x) Y(x) generality |
| §5 p. 42 | "Lemmas 4 and 5; § 3" | §3 Lemmas 4, 5 | iteration from infinite left |
| §5 p. 42 | "Lemmas 6 and 7 (§ 3)" | §3 Lemmas 6, 7 | iteration from strip V |
| §5 p. 42 | "the notation of § 3" | §3 | notation conventions for determinant limits |
| §5 p. 46 | "(Def. 5; § 1)" | §1 Def. 5 | proper-periodic-functions definition |
| §5 p. 47 | "(Def. 9; § 1)" | §1 Def. 9 | proper-region definition (R^p) |
| §5 p. 47 | "(Def. 3; § 1)" | §1 Def. 3 | proper-functions (φ_{i j}(x_r)) |
| §5 p. 47 | "(Def. 5; § 1)" | §1 Def. 5 | proper-periodic-functions (used in (13 a)) |
| §6 p. 48 | "the kind specified in the beginning of § 1" | §1 | coefficient-class for L_n |
| §6 p. 48 | "(Def. 8; § 1)" | §1 Def. 8 | Q-factorability definition |
| §6 p. 48 | "(6; § 1)" | §1 (eq. 6) | system Y(x+1) = D(x) Y(x) |
| §6 p. 48 | "the notation of § 3" | §3 | notation for determinant limits |
| §6 p. 49 | "Lemma 5 (§ 3)" | §3 Lemma 5 | determinant-limit existence |
| §6 p. 49 | "the way asymptotic relations (2 c) were derived in § 3" | §3 | (2 c) derivation |
| §6 p. 50 | "(7 a; § 1)" | §1 (eq. 7 a) | formal-series-with-logarithms (constants γ) |

**Total earlier-section dependencies:** 24 distinct cross-references.

## §§4-6 internal dependencies (§4 → §5 → §6 chain)

| Cited from | Cite text | Cite target | Subject |
| --- | --- | --- | --- |
| §5 p. 44 | "**Lemma 8 (§ 4) is applicable** for evaluation of any of the expressions (6 c)" | §4 Lemma 8 (T1) | sum-formula application |
| §5 p. 44 | "by the methods of § 4 we evaluate (6 c)" | §4 | contour-summation methods |
| §5 p. 45 | "in applying Lemma 8" | §4 Lemma 8 (T1) | as required by the lemma |
| §5 p. 46 | "the summations in (5) being specified by § 4" | §4 | sum-formula determination |
| §6 — | (no direct §4 / §5 references inside §6 body) | — | (§6 stands on §§1-3 + (II)/(I) only) |

**§§4-6 internal chain:** §5 explicitly cites §4 Lemma 8 four times.
§6 does not directly cite §4 or §5 inside its body but uses §3 Lemma 5
for the determinant-limit existence; §6 Lemma 9 plus §5 Theorem I are
both consumed by §§7, 8, 9 downstream.

## Later-section consumption (§§7-9 → §§4-6)

(Source: section-header grep over PDF p. 51 onwards; out-of-scope for
this readthrough's verbatim extraction, but included for cross-walk
completeness.)

| Cited from | Cite text (paraphrased; verbatim quote in §§7-9 not extracted in this 073 session) | Cite target |
| --- | --- | --- |
| §7 p. 51 (Theorem II opener) | (§7 begins by invoking the §5 Theorem I "completely-proper" framework for product operators; verbatim quote DEFER to a future BT §§7-9 readthrough) | §5 T2, §6 T3 |
| §8 p. 64+ | (§8 completes the proof of §7's Theorem) | §5 T2, §7 |
| §9 p. 69 (Fundamental Existence Theorem) | (§9 quotes §5 Theorem I and §6 Lemma 9 + §7 Theorem II as ingredients of the Fundamental Existence Theorem) | §5 T2, §6 T3, §7 |

A §§7-9 verbatim readthrough is the natural follow-up substrate task
to 073; it would convert each "DEFER" line above to a verbatim
≤ 30-word quote. This is recorded in
`sectorial_upgrade_gap_status_v2_with_bt_4_6.md` §5 residual items.

**Total later-section consumption candidates:** 3 (T1 inside §5 / T2
inside §§7, 9 / T3 inside §§7, 9). Verbatim §§7-9 quotes DEFER.

## External references (§§4-6 → BT 1930 paper (I)/(II))

| Cited from | Cite text | Cite target |
| --- | --- | --- |
| §4 p. 30 | "a Lemma proved by Birkhoff in (I; p. 218)" | Birkhoff 1930 (Acta 54), p. 218 — formal-series-existence Lemma |
| §4 p. 33 | "an inequality of Birkhoff" + "formula 12 in (II)" | BT 1930 (Acta 54) eq. (12) inequality |
| §4 p. 33 | "the inequality (13) of (II)" | BT 1930 (Acta 54) eq. (13) inequality |
| §4 p. 39 | "by formula (12) of (II)" | BT 1930 (Acta 54) eq. (12) |
| §5 p. 43 | "found in (II). (The notation used in this paper is different from that of (II))" | BT 1930 (Acta 54) determinant-limit formulas |
| §5 p. 43 | "Analogous to a similar construction, in II, such a solution can be found" | BT 1930 (Acta 54) construction template |
| §5 p. 44 | "(I); in particular, (6'') on p. 213" | BT 1930 (Acta 54) p. 213 formula (6'') |
| §5 p. 44 footnote | "applied to the second member of (5 d), similar to that in (I; p. 215)" | BT 1930 (Acta 54) p. 215 |
| §5 p. 45 | "By the reasoning of (II; p. 259)" | BT 1930 (Acta 54) p. 259 |
| §6 p. 48 footnote | "Cf. (I; p. 213, l. 6)" | BT 1930 (Acta 54) p. 213 line 6 |
| §6 p. 50 | "(I); in particular, pp. 213, 215" | BT 1930 (Acta 54) pp. 213, 215 |
| §6 p. 51 | "(I; p. 213) of such series (containing logarithms)" | BT 1930 (Acta 54) p. 213 |

**Total BT 1930 cross-references:** 12 distinct cite points across §§4-6.

## Composite dependency map

```
              ┌──────────────────────────────────┐
              │  BT 1930 (Acta Math. 54)        │
              │  "Formal theory of irregular     │
              │   linear difference equations"   │
              │  cited as (I)/(II)               │
              └────────────────┬─────────────────┘
                               │  12 cross-refs
                               ▼
              ┌──────────────────────────────────┐
              │  BT 1933 §§1-3                   │
              │  setup machinery:                │
              │  - §1 Defs 1, 3, 4, 5, 6, 8, 9   │
              │  - §1 eqs 2, 6, 6 a, 7 a         │
              │  - §2 region F, B'-curves        │
              │  - §3 Lemmas 4, 5, 6, 7          │
              └────────────────┬─────────────────┘
                               │  24 cross-refs
                               ▼
              ┌──────────────────────────────────┐
              │  §4 Lemma 8 (T1)                 │
              │  "A lemma on summation"          │
              │  Acta p. 30                      │
              │                                  │
              │  contour-summation for           │
              │  y(x+1) - y(x) = e^Q(x) h(x)     │
              └────────────────┬─────────────────┘
                               │  4 cross-refs (§5 → §4)
                               ▼
              ┌──────────────────────────────────┐
              │  §5 Theorem I (T2)               │
              │  "Construction of proper         │
              │   solutions to the right of a    │
              │   proper curve"                  │
              │  Acta p. 41                      │
              │                                  │
              │  L_n completely proper in        │
              │  (m) + ... + (η);                │
              │  contains [CHART-MAP-CANDIDATE-  │
              │   B1] at p. 47 (13 a)            │
              └────────────────┬─────────────────┘
                               │  (no §6 → §5 direct cite;
                               │   parallel use of §3 Lemma 5)
                               ▼
              ┌──────────────────────────────────┐
              │  §6 Lemma 9 (T3)                 │
              │  "A lemma on factorization"      │
              │  Acta p. 48                      │
              │                                  │
              │  L_n = L_{n-Γ} · L_Γ at point    │
              │  of division                     │
              └────────────────┬─────────────────┘
                               │
                               ▼
              ┌──────────────────────────────────┐
              │  §§7-9 (out of scope for 073)    │
              │  consume T1 + T2 + T3 to build   │
              │  the Fundamental Existence       │
              │  Theorem (§9)                    │
              └──────────────────────────────────┘
```

## Summary counts

| Direction | Count |
| --- | --- |
| §§4-6 → §§1-3 (earlier-section deps) | 24 |
| §§4-6 → §§4-6 (internal §4 → §5 chain) | 4 |
| §§4-6 → BT 1930 paper (I)/(II) | 12 |
| §§4-6 ← §§7-9 (consumption; verbatim DEFER) | 3 (deferred) |
| **Grand total internal/cross cite-points** | **40 + 3 deferred** |

## Provenance

All cite locations above were verified by line-by-line scan of the
verbatim §§4-6 transcripts at:
- `bt_1933_section_4_extract.md`
- `bt_1933_section_5_extract.md`
- `bt_1933_section_6_extract.md`

Cite-target identifiers (e.g. "Def. 4", "Lemma 5", "(6 a)") are
reproduced as written in BT 1933.
