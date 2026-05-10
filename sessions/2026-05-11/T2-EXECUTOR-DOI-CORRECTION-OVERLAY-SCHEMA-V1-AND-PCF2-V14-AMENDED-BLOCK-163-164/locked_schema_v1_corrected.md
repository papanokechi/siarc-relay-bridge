# Locked Zenodo Metadata Schema v1 — SIARC Anchor Deposits

**Authority:** Slot 160 verdict (LABEL=SCHEMA_LOCK_INLINE, BAND=MEDIUM-HIGH, witness=claude-opus-4-7-anthropic-2026-05-10)
**Predecessor:** Slot 157 verdict (`34563a6`); slot 159 canonical outlook (`961b828`)
**Status:** OPERATIVE (locked inline; no standalone fire)
**Citable as:** `siarc-relay-bridge sessions/2026-05-10/T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160/locked_schema_v1.md`

---

## Scope

This schema specifies how SIARC program structure (M1-M12 closure axes + cross-program relations) is expressed in Zenodo deposit metadata. It applies to **anchor deposits** (long-lived program-tier homes); single-purpose deposits cite the canonical outlook by reference.

**Anchor deposits (5):**

| Anchor | Concept-DOI | Carries axis-coverage table |
|---|---|---|
| PCF-1 | `10.5281/zenodo.19931635` | yes (next version) |
| PCF-2 | `10.5281/zenodo.19936297` | yes (v1.4 onward) |
| Umbrella | `10.5281/zenodo.19885549` | yes (v2.3 onward) |
| Channel Theory | `10.5281/zenodo.19941678` | yes (next version) |
| D2-NOTE | `10.5281/zenodo.19996689` | yes (next version) |

---

## Layer 1 — Native Related-identifier vocabulary

### Discipline

- **`IsSupplementTo` / `Cites` / `IsDocumentedBy` / `References` MUST target concept-DOIs**, not version-DOIs.
- **`IsNewVersionOf` is the documented exception**: it is by definition a version-to-version relation and MUST target the immediate predecessor's version-DOI on both sides.
- **`References` MUST target persistent identifiers** (DOI / Handle / arXiv ID / SWHID), NOT GitHub commit URLs. Bridge cascade SHAs go in the Description body as prose.

### Reference row pattern (PCF-2 v1.4 instance, 5 rows)

```
IsNewVersionOf  10.5281/zenodo.19963298    PCF-2 v1.3 (version-DOI; exception)
IsSupplementTo  10.5281/zenodo.19931635    PCF-1 concept
Cites           10.5281/zenodo.19931635    PCF-1 concept
IsSupplementTo  10.5281/zenodo.19885549    Umbrella concept
Cites           10.5281/zenodo.19885549    Umbrella concept
```

The PCF-1 pattern (paired `IsSupplementTo` + `Cites`) MUST be replicated for every paper-tier supplementary relation. This is symmetric and lossless.

### Anti-rules

- **Do NOT add `Cites` / `IsSupplementTo` rows for axis-mediated siblings** (e.g., Channel Theory, D2-NOTE, picture v1.19) in PCF-2 v1.4. Their relation is axis-tier, expressed via Layer 2.
- **Do NOT use `References` rows for bridge cascade URLs**. SHA-in-prose is the operative reference; URL is decoration.

---

## Layer 2 — Description-body axis-coverage table

### Controlled status vocabulary (LOCKED 7-term set)

```
closed (V0; primary)             -- this deposit is the canonical home
closed (V0; folded)              -- this deposit absorbs the closure; primary lives elsewhere
closed (retired into Mx)         -- axis was retired into Mx; cite Mx's primary
partial                           -- this deposit covers part; full closure pending
external                          -- axis lives elsewhere; cite that deposit
not in scope                      -- axis not addressed in this deposit
tabled (RULE 1)                   -- not yet opened
```

**Rationale for renames (verdict §Q2b):**
- Leading with closure-tier (`closed (V0; ...)` not `covered (V0-closed; ...)`) is more scannable; future V1/V2 closure tiers slot in cleanly as `closed (V1; primary)`.
- `closed (retired into Mx)` (not parallel `retired (into Mx)`) because retirement is a *form* of closure.

### Granularity rule

**List M1-M12 atomically.** Do NOT group RULE-1-tabled axes. When (e.g.) M2 opens, the migration is a status flip on a single row, not a structural edit.

### Reference table (PCF-2 v1.4 axis-coverage snapshot, ≈ 2026-05-10)

| Axis | Status | Primary substrate |
|---|---|---|
| M1 | `external` | D2-NOTE concept `10.5281/zenodo.19996689` |
| M2 | `tabled (RULE 1)` | — |
| M3 | `tabled (RULE 1)` | — |
| M4 | `closed (V0; folded)` | bridge cascade `5f9db69` (cascade 106) |
| M5 | `tabled (RULE 1)` | — |
| M6.CC | `closed (retired into Channel Theory)` | Channel Theory concept `10.5281/zenodo.19941678` |
| M7 | `closed (V0; folded)` | bridge cascade `7f93b9e` (cascade 123) |
| M8a | `closed (V0; folded)` | bridge cascade `cb429e1` (cascade 127R) |
| M8b | `closed (V0; folded)` | bridge cascade `74c5630` (cascade 130R; d≥3 caveat in Appendix C iii) |
| M9 | `partial` | bridge cascade `b9aa881` (slot 136 picture v1.20+) |
| M10 | `partial` | Lean sorry discharge work-stream; SAFE phrasing in Umbrella v2.3 Appendix C ii |
| M11 | `tabled (RULE 1)` | — |
| M12 | `tabled (RULE 1)` | — |

**Per-deposit semantics:** PCF-2 v1.4 marks M7/M8a/M8b as `closed (V0; folded)` because their primary V0-closure homes are the cascade verdicts themselves; PCF-2 v1.4 *absorbs* those closures via Appendix C cross-references. A future PCF-2 V1-closure version would change `folded` → `primary` if/when the V1 mathematics lives in PCF-2 directly.

### Bridge SHA prose convention

Inline references to bridge cascade SHAs in the Description body use the pattern:

> "M7 V0 closure: bridge cascade `7f93b9e` ([siarc-relay-bridge](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-09/T1-SYNTH-M7-V0-CLOSURE-CASCADE-123/))"

The SHA is the persistent identifier; the URL is decoration that may decay if the repo is renamed (see §Migration).

---

## Layer 3 — SIARC Zenodo Community

**Status: DEFERRED.** Re-affirms `D-157-7` (slot 157 verdict §Q5d). Lift conditions:

1. RULE 1 has lifted (M1-M12 V0 closure surface observable), AND
2. A forcing function emerges (external citation requires Community URL anchor).

If lifted, Community description carries a single line: pointer to the canonical outlook bridge URL. NOT a master axis-coverage table (per §Q3b: Communities lack versioned descriptions; per-deposit snapshots are the audit trail).

---

## Migration path (when tabled axes flip post-RULE-1-lift)

1. **Authoritative status flip:** amend the canonical outlook (slot 159 source-of-record) via standard fire. The outlook is the single source of truth.
2. **Existing deposits remain frozen.** No version increment. No description edit. (Both would be governance-thrash with no scientific delta.)
3. **Next anchor deposit** (post-flip): axis-coverage table reflects the new status. The temporal sequence of anchor-deposit tables forms the deposit-tier audit trail.
4. **Community description** (when D-157-7 lifts): one-line outlook pointer; no churn.
5. **Repo identity changes:** prose-tier SHA references survive (content-addressed); URLs become stale-but-recoverable. SWHID submission to Software Heritage planned for V1 milestone.

---

## Schema versioning

- **v1 (this document):** initial lock per slot 160 verdict 2026-05-10.
- **v2 trigger conditions:** (a) RULE 1 lifts and a tabled axis enters a non-`closed` non-`partial` state requiring new vocab; (b) a 6th anchor deposit emerges; (c) DataCite vocabulary changes upstream.

Schema upgrades MUST go through a synth consultation analogous to slot 160. Existing anchor-deposit metadata is NOT retroactively upgraded; v1 tables remain valid timestamped snapshots.

---

## Consumers (tracked)

- **F6 Umbrella v2.3 substrate-prep** — embeds vocabulary + granularity rule + 5-row pattern + reference table inline.
- **Slot 137 `zenodo_v14_description_block.md` amendment-overlay** — adds 5th Layer 1 row + axis-coverage table; cites slot 160 verdict SHA.
- **Future PCF-1 / Channel Theory / D2-NOTE version increments** — apply schema at deposit time.
