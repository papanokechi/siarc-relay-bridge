# Handoff — VQUAD-REPRO-BUNDLE-002

**Status:** Deposit-target reproducibility bundle **regenerated from the
corrections-final paper, integrity-verified, and packaged**; staged and **HELD**
(no commit, no push, no Zenodo deposit) per the standing meta-rule.

**Supersedes:** VQUAD-REPRO-BUNDLE-001 (preview, PDF `359d1172…`). This is the
**deposit-target** bundle.

## What was produced

- **`vquad-periodrep-bundle/`** — the bundle tree (40 files): the corrections-final
  paper (PDF + self-contained `.tex` + `preamble.tex` + bundle `build.py`), 14
  verification scripts in 4 narrative-ordered directories, 12 reference result
  JSONs, 4 reproducibility docs, top-level README, and a CC BY 4.0 LICENSE.
- **`vquad-periodrep-bundle.zip`** — the packaged deposit-target archive.
  - SHA-256 `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb`
  - 721715 bytes, 40 entries, portable (forward-slash, single top dir, testzip OK).
- Slot records: `bundle-delta.md`, `docs-update.md`,
  `bundle-integrity-verification.md`, `bundle-archive-info.md`, `ledger.json`,
  `claims.jsonl`, this `handoff.md`.
- Auditable build tooling (kept in slot root, **not** shipped in the bundle):
  `relativize_and_copy.py` (parent→bundle transformer, retained for provenance,
  **not re-run** — scripts unchanged), `verify_bundle.py` (integrity harness),
  `_package_bundle.py` (packager).

## Paper PDF pin (the reproducible artifact)

- **Corrections-final PDF SHA-256:**
  `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe`
  (714771 bytes, 24 pp). Supersedes BUNDLE-001's `359d1172…` (698730 B, 23 pp).
- `python paper/build.py` reproduces it byte-for-byte (in-place **and** pristine
  temp dir); the PDF embedded in the zip re-hashes to the same value.

## Integrity result

- **All 13 runnable essential scripts pass** (exit 0; 11 exact match to `data/`,
  1 match-modulo-volatile, 1 stdout-only). No hardcoded absolute paths. Identical
  PASS pattern to BUNDLE-001 — corrections changed no script and no numerical
  result.
- **Paper reproduces byte-for-byte** (above).
- **Retracted DOI `20455090` absent** from the entire bundle (whole-tree scan +
  embedded PDF: NONE). Companion cited only by concept `10.5281/zenodo.20455089`.
- **HALT GATE: PASS.**

## What changed from BUNDLE-001 (preview → deposit-target)

| area | change |
|------|--------|
| `paper/` | corrections-final PDF (`4ca12a35…`, 24 pp) + corrected `.tex` + `preamble.tex`; `build.py` target SHA refreshed |
| `docs/SIARC_PROVENANCE.md` | added COLDREAD-001 (`e207b33`) + CORRECTIONS-001 (`d4fc87a`) to the chain; concept DOIs (`20455089`/`20624813`/`20694840`); `O. Marchal`; provenance note (supersedes preview) |
| `docs/CONVENTIONS.md` | `C. Marchal` → `O. Marchal`, acknowledgement cross-ref |
| `README.md` | `23 pp` → `24 pp`; companion DOI → concept `20455089` |
| `scripts/`, `data/`, `REPRODUCIBILITY.md`, `DEPENDENCIES.md`, per-dir READMEs | **UNCHANGED** (no logic / numerical change) |

Carried in from the corrections paper itself (in `paper/`): the §4.3 H-1
provenance remark, the §7.4 topological-recursion subsection + §2.2 Lax-pair
note, the bibliography repoint, the Marchal personal-communication
acknowledgement, and the M-1/M-2 terminology (Stokes constant = S; connection
coefficient = C).

## Recommended next operator actions

1. **Review the bundle** — open `vquad-periodrep-bundle/README.md`, skim `docs/`,
   spot-check a script per directory; confirm the archive opens cleanly.
2. **Release this slot** — when authorized, commit with the prepared message
   ("VQUAD-REPRO-BUNDLE-002 — deposit-target bundle regenerated from
   corrections-final paper (PDF 4CA12A35…); integrity verified; retracted DOI
   confirmed absent; supersedes BUNDLE-001 preview") + Co-authored-by trailer,
   and push.
3. **Re-run VQUAD-ZENODO-READY-001** — it will now pass Stage 1 (all 3
   prerequisites met: cold-read ✓, corrections ✓, bundle-002 ✓), perform the pin
   refresh it halted on (paper `4ca12a35…`, archive `8752d7c7…`), and **drop the
   `isSupplementTo` placeholder** (Scenario B: the bundle is part of the deposit,
   not a related work).
4. **Deposit** — run **VQUAD-ZENODO-DEPOSIT-001**: upload
   `paper/vquad-periodrep-paper.pdf` and `vquad-periodrep-bundle.zip` as **one**
   record under CC BY 4.0, mirroring the creator/ORCID/license metadata of the
   prior V_quad records (concept-linked to `10.5281/zenodo.20455089` — the
   concept DOI, **never** the retracted version `20455090`). Verify the Zenodo
   server-side **MD5** of the uploaded zip (Zenodo returns `md5:…`, not SHA-256).

## Standing-rule disposition

Slot `git add`-staged, **HELD**. No commit, no push, no deposit performed by the
agent. HEAD unchanged at `d4fc87a`. Parents (BUNDLE-001, CORRECTIONS-001,
COLDREAD-001) left pristine; the untracked `sessions/2026-06-15/EBR3-REVISION-001/`
is left untouched. COMPLETE commit message is justified — Stages 1–6 all ran and
the integrity gate PASSED.
