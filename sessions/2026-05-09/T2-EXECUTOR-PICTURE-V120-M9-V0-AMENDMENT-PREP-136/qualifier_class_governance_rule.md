# Qualifier-class governance rule — UF-132-5 absorption (slot 136 §28.C)

**Excerpt for operator review and forward-pointed slot 138+ orchestration.** This file contains the full text of the new §28.C subsection inserted into the §28 Amendment Log of `picture_revised_20260507.md` per slot 136 §2.7 edit pass.

---

## §28.C — verbatim text

> ### v1.20 sub-amendment: qualifier-class governance rule (UF-132-5 absorption) (§28.C)
>
> Per cascade-132 UF-132-5 open-question (qualifier-pollution
> governance: should `(STAGING; SUBSTANTIVE-PENDING)` and similar
> qualifier classes be governed by an explicit rule), slot 136
> absorbs the qualifier-class governance rule into source-of-record
> at this sub-section.
>
> **Qualifier-class governance rule (slot 136 absorption of cascade-132
> UF-132-5):**
>
> A *qualifier* is a parenthetical annotation appended to a milestone
> or G-row identifier (e.g., `M7 V0 (SOFT-BRANCH; HARD-BRANCH-PENDING)`).
> Two classes are recognized:
>
> 1. **Substantive qualifier** — encodes a structural property of the
>    closure that affects downstream substrate (e.g., the SOFT/HARD-branch
>    split for M7 V0; the algebraic-test-scale split for M8a V0; the
>    numerical-foreclosure for M8b V0). All cascade-132 PATH_B
>    annotations are substantive.
>
> 2. **Staging qualifier** — encodes a procedural state that does NOT
>    affect downstream substrate (e.g., a hypothetical
>    `(STAGING; SUBSTANTIVE-PENDING)` marker on a partial deposit). No
>    cascade-132 PATH_B annotations are staging-class.
>
> **Rule:** substantive qualifiers MUST propagate verbatim through all
> SIARC source-of-record artefacts (umbrella, PCF papers, picture-chain).
> Staging qualifiers MAY be omitted from picture-chain headlines if they
> add no operative information (e.g., a staging marker on a substrate-prep
> deposit that is going to be Zenodo-deposited next is informational at
> the bridge level only).
>
> **Forward-pointed application:** when slot 138+ stages M11 / M12 admin
> amendments, the absorption logic should classify each new qualifier as
> substantive vs staging before propagation; staging qualifiers may be
> absorbed at the picture-chain level WITHOUT propagating to the umbrella
> or to PCF papers. The operator may further refine the rule inline at
> slot 138+ — slot 136 records the canonical default.

---

## Insertion site

- File: `tex/submitted/control center/picture_revised_20260507.md`
- Section: `## 28. Amendment Log (v1.17 → v1.20 unified)` (newly written for the FIRST TIME in slot 136 — silently fixes the v1.20 staging defect of header-references-§28-but-§28-does-not-exist)
- Subsection: §28.C (third subsection inside §28; preceded by §28.A v1.17 → v1.20 W20-Wed cascade absorption and §28.B M9 V0 closure-series absorption)
- Insertion line range: §28.C header at L2180 (post-edit); subsection spans ~40 lines

---

## Forward-pointed (slot 138+ M11/M12 admin window)

When slot 138+ stages M11 / M12 admin amendments:

1. **Classify each new qualifier** as substantive (affects downstream substrate) vs staging (procedural state only).
2. **Substantive qualifiers** propagate verbatim through all SIARC source-of-record (umbrella + PCF papers + picture-chain).
3. **Staging qualifiers** may be absorbed at the picture-chain level WITHOUT propagating to umbrella or PCF papers.
4. Refine the rule inline at slot 138+ if needed; the slot-136 default is the canonical baseline.

---

## In-fire FV remediation note

The §28.C closing sentence originally read "slot 136 establishes the canonical default" — flagged by FV scan (forbidden verb `establishes`). Remediated to "slot 136 records the canonical default" per FV discipline. Recorded in `discrepancy_log.json` as D-136-3 (INFO).

---

## Closes UF-132-5

Cascade-132 UF-132-5 (qualifier-pollution governance) is now closed in source-of-record at the picture-chain v1.20+ §28.C layer. Future cascade-class V0 closure amendments inherit this rule by default.
