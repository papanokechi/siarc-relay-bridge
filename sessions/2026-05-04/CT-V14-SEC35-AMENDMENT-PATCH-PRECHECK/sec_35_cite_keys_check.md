# CT v1.4 §3.5 amendment — cite-keys validation

**Task:** CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK
**.bib file:** `siarc-relay-bridge/sessions/2026-05-03/CT-V14-NARRATIVE-DRAFT/annotated_bibliography.bib`

---

## Cite keys introduced by the amendment

The amendment introduces **3** explicit `\cite{...}` calls
(one combined `\cite{a,b,c}` invocation) plus **3** plain-text
author-year references that may need future bibkey upgrade.

| Bibkey                                | Status                  | Action                           |
|---------------------------------------|-------------------------|----------------------------------|
| `costin2008asymptotics`               | EXISTS (line 13)        | None — ready to use              |
| `birkhofftrjitzinsky1932analytic`     | EXISTS (line 210)       | None — ready to use              |
| `jimbomiwa1981monodromy`              | EXISTS (line 152)       | None — ready to use              |

## Plain-text references (no bibkey yet — operator decision)

| Plain-text               | Anchor / source                           | Suggested bibkey                       | Action                                         |
|--------------------------|-------------------------------------------|----------------------------------------|------------------------------------------------|
| Okamoto 1987             | "Studies on the Painlevé equations IV"    | `okamoto1987studies`                   | ADD-BIB before final apply (operator)          |
| Barhoumi–Lisovyy–Miller–Prokhorov 2024 §4.1 | SIGMA, transcendence-Lax-pair §4.1 | `barhoumilisovyy2024transcendence` | ADD-BIB before final apply (operator)          |
| Birkhoff 1930 (formal-series existence) | Trans. AMS, "Generalized Riemann problem" | `birkhoff1930generalized`             | OPTIONAL ADD — currently subsumed by `birkhofftrjitzinsky1932analytic`; operator may keep plain-text  |

The patch as drafted **uses only existing bibkeys** in
`\cite{...}` calls (`costin2008asymptotics`,
`birkhofftrjitzinsky1932analytic`, `jimbomiwa1981monodromy`).
The Okamoto 1987 / BLMP 2024 / Birkhoff 1930 references are
in **plain-text author-year form only**. This is a deliberate
hygiene choice: it keeps the patch buildable as-is (no
undefined-citation warnings), and surfaces the bibkey-
addition decision as separate operator action.

## BIBKEY_COLLISION risk assessment

* `costin2008asymptotics` — single existing entry; no collision risk.
* `birkhofftrjitzinsky1932analytic` — single existing entry; no collision risk. (The bibkey says 1932 but the canonical citation year is 1933; this is a pre-existing v1.4 convention, not introduced by this amendment.)
* `jimbomiwa1981monodromy` — single existing entry; no collision risk.
* Suggested NEW bibkeys (`okamoto1987studies`, `barhoumilisovyy2024transcendence`, `birkhoff1930generalized`) — none collide with existing keys (verified via full bibkey listing, 2026-05-04). No `HALT_CTV14_BIBKEY_COLLISION` raised.

## Cross-reference to upstream artifacts

* G17-LAYER-SEPARATION-LIT-ANCHOR handoff Phase A (slot 04 Wasow image-only; slot 06 Costin 2008 ch.5; slot 03 B-T 1933) — anchors `costin2008asymptotics` and `birkhofftrjitzinsky1932analytic` at theorem-grade quotes.
* G17 handoff Phase B (slot 07 Okamoto 1987 §1; slot 08 BLMP 2024 §4.1; refs Jimbo–Miwa 1981 II) — anchors `jimbomiwa1981monodromy` plus the two suggested-NEW bibkeys.
* picture v1.17 §5 G17 row "amendment recommended" — agrees that this is documentation upgrade, not structural gap; G17 closes after operator-applied amendment.

## Verdict (cite-keys gate only)

`CITE_KEYS_GATE_PASS` — patch as drafted is buildable with
existing CT v1.4 .bib (no compile-blocking undefined
citations); operator action queued for the optional bibkey
additions before final apply.
