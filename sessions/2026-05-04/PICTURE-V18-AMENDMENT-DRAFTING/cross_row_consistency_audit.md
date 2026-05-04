# Cross-row consistency audit — v1.18 (PICTURE-V18 §C)

## C.1 Zenodo ID consistency — ✅ PASS

**Check:** No row in v1.18 cites the wrong PCF-1 v1.3 Zenodo concept DOI.

| Token | Count v1.18 | Context |
|-------|-------------|---------|
| `19937196` | 10 | PCF-1 v1.3 concept DOI — correct (rows L415 + L1767 of cumulative file + new v1.18 mentions in superblock + §28) |
| `19941678` | 4 | Channel Theory v1.3 concept DOI — correct (row L418 + cross-references) |
| `19963298` | 5 | PCF-2 v1.3 concept DOI — correct (row L417 + cross-references) |

No instances of the wrong-PCF-1 IDs being attached to PCF-1 rows.
Cheat-sheet operator-side artifacts (separate from this picture file)
remain on operator's plate per `cheat-sheet-pcf1-zenodo-id-correction`
todo (see PICTURE-V18 §B.5 + §4 HALT_CHEAT_SHEET_NOT_CORRECTED hedge).

## C.2 M6 Phase B.5 / G18 / methodology consistency — ✅ PASS

All three rows agree on Case 3 outcome of PICTURE-V18 §B.10:

- **M6 Phase B.5 (delta #9):** STILL_PARTIAL_PENDING_PIVOT_DECISION; literature
  path exhausted at OA budget; SIARC primary-derivation Path B (033) deferred
  at operator.
- **G18 anchor (delta #8):** CLOSED_TRIANGULATED_3_SOURCE — note this is the
  Birkhoff–Trjitzinsky 1933 anchor closure, **separate** from the M6 Phase B.5
  W cross-walk; G18 closure does NOT discharge M6 Phase B.5.
- **Methodology footnote (delta #11):** explicitly states the W homomorphism is
  not stated as a theorem in any post-Sakai PIII OA paper surveyed (NY 2004 TOC,
  KNY 2017, NY 1998, NY 2000, FW 2005); bridge is folklore-Lie-theory; M6 Phase
  B.5 final state is STILL_PARTIAL_PENDING_PIVOT_DECISION.

`STILL_PARTIAL_PENDING_PIVOT_DECISION` count in v1.18: 8 (consistent across
top-revision header + Updates superblock + §28 cascade table + methodology
footnote + cycle status + cross-references).

## C.3 G3b grammar — ✅ PASS

All three G3b residuals use `CLOSED_VIA_<route>_<...>` status grammar:

- (i) `CLOSED_VIA_OPERATOR_GATED_OA_ROUTES`
- (ii) `CLOSED_VIA_TRANSITIVE_T1_A01`
- (iii) `CLOSED_VIA_COSTIN_SUBSTITUTE`

## C.4 G17 / CT v1.4 §3.5 reading-decision consistency — ✅ PASS

G17 row + existing operator todo `ct-v14-sec35-reading-decision` are mutually
consistent. Both reference the Reading A vs Reading B Section-numbering ambiguity
surfaced by prompt 023 (`CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK`) and cross-checked
by prompt 026 (`G17-LAYER-SEPARATION-LIT-ANCHOR`). G17 status `AMENDMENT_PENDING_
READING_DECISION`; verdict label `UPGRADE_CTV14_SEC35_PATCH_PARTIAL_SECTION_
NUMBERING_AMBIGUITY`. Operator + Claude pivot-decision pending.

## C.5 §11 arxiv-mirror state consistency — ✅ PASS

4/4 PASS for non-PCF-1 records (umbrella v2.0 / PCF-2 v1.3 / CT v1.3 / T2B v3.0).
PCF-1 v1.3 pack hazard documented (21pp post-edit re-pack vs canonical 16pp v1.3;
operative-truth via bridge snapshot `58dfa9e`). `034` re-fire status hedged.
Cosmetic CT v1.3 `00README` Title-field-blank flag carried forward.

## C.6 PII typo correction — ✅ PASS WITH DOCUMENTED EXCEPTION

**Strict reading:** PII-1501443-6 should appear (correction landed); PII-1501457-9
should NOT appear (typo gone).

**v1.18 actual:**
- `PII-1501443-6` count: 6 (correction recorded across header + Updates row + §28 row + methodology references)
- `1501457-9` literal-token count: 7 (all in `was X → now Y` correction-record language)
- v1.17 `1501457-9` count: 0 (typo never landed in this picture file)

**Documented exception:** The literal typo token `1501457-9` appears 7× in v1.18
**only** as part of `was X → now Y` correction-record language (e.g., "PII typo
corrected (was `PII-1501457-9` → now `PII-1501443-6`)"). No active reference uses
the typo number. The strict-reading intent of C.6 — "the typo isn't being carried
forward as an active reference" — is satisfied. Operator-side cheat-sheet
artifacts that may reference the old PII number should be patched separately
(out of scope per PICTURE-V18 §6).

If strict zero-token compliance is required for v1.18 deposit, post-process
sed/replace the 7 informational mentions with descriptive language (e.g.,
"prior typo'd PII number" / "the corrected PII") — purely cosmetic, no
semantic change.

## Audit verdict

✅ **5 of 6 checks PASS unconditionally** (C.1 / C.2 / C.3 / C.4 / C.5).
✅ **C.6 PASS with documented exception** (literal typo token appears in
correction-record language only; no active references; v1.17 had 0 occurrences).

**Aggregate:** PICTURE-V18 §3 AEAL claim 3 satisfied — "Cross-row consistency
audit pass (C.1-C.6 all ✓ OR documented exceptions)."
