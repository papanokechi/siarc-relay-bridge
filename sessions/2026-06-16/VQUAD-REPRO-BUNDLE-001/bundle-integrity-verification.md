# Bundle integrity verification — VQUAD-REPRO-BUNDLE-001 (Stage 5.4)

**Timestamp:** 2026-06-16T07:07:57+09:00 (Asia/Tokyo)
**Bundle root:** `vquad-periodrep-bundle/`
**Harness:** `verify_bundle.py` (slot root, not shipped in bundle)
**Build transformer:** `relativize_and_copy.py` (slot root, not shipped in bundle)

This record satisfies HALT GATE 5: every essential script executes without
error and every output matches the reference data in `data/` (modulo documented
volatile fields). The paper compiles clean and reproduces the deposited PDF hash.

---

## 1. Script execution + output comparison

Each script is run **from its own bundle directory** with a fresh interpreter.
Its emitted JSON is compared byte-for-byte against the reference in `data/`,
ignoring only documented volatile fields (timestamps, wall-clock runtimes).

| # | script | dir | exit | compare to `data/` |
|---|--------|-----|------|--------------------|
| 1 | holonomic_recognition_q3.py | 01-algebraicity | ok | exact |
| 2 | extract_verify_operators.py | 01-algebraicity | ok | exact |
| 3 | indicial_analysis.py | 01-algebraicity | ok | exact |
| 4 | borel_pade_census.py | 01-algebraicity | ok | exact |
| 5 | stage2_kovacic.py | 02-galois | ok | — (stdout only) |
| 6 | stage2b_symsquare.py | 02-galois | ok | exact |
| 7 | stage3_galois_LV.py | 02-galois | ok | exact |
| 8 | stage3b_frobenius_v2.py | 02-galois | ok | exact |
| 9 | numcheck_period_rep.py | 03-verification | ok | match (modulo volatile) |
| 10 | stage4a_methodA_v2.py | 03-verification | ok | exact |
| 11 | stage4_methods.py | 03-verification | ok | exact |
| 12 | stage0_residual_check.py | 03-verification | ok | exact |
| 13 | stage1_hankel_period.py | 04-cycle | ok | exact |

**Result: ALL ESSENTIAL SCRIPTS PASS — True** (13 run, exit 0; 11 exact, 1
match-modulo-volatile, 1 stdout-only).

`q3_foundation.py` (03-verification) is a **support module** imported by
`stage0_residual_check.py`; it is byte-identical to
`01-algebraicity/holonomic_recognition_q3.py` and is exercised transitively, so
it is not run as a standalone entry.

### Volatile-field note (script 9)
`numcheck_period_rep_results.json` carries `generated_utc` (ISO timestamp) and
`runtime_seconds` (wall clock). These change on every run by construction; the
harness strips fields matching `generated|utc|runtime|seconds` before
comparison. All numerical content (the 46-digit agreements) is an exact match.

---

## 2. No-absolute-path confirmation (Stage 5.1)

A scan of every shipped `.py` (`scripts/*/*.py`, `paper/build.py`) for hardcoded
`C:\` absolute paths returns **NONE**. All output and sibling-file references
were rewritten by `relativize_and_copy.py` to
`os.path.join(os.path.dirname(os.path.abspath(__file__)), …)`. The clean harness
run above (each script finds its inputs/writes its outputs from its own dir) is
the positive confirmation that relativization is correct.

### Transformations applied to every script (auditable in `relativize_and_copy.py`)
1. **Path relativization.** Absolute `C:\…\X.json` output targets →
   `os.path.join(os.path.dirname(os.path.abspath(__file__)), "X.json")`;
   `sys.path` directory references (parent `…\scripts`) → the script's own dir
   (the cross-importing 01-algebraicity scripts are co-located, so this resolves
   correctly).
2. **UTF-8 stdout guard.** A `sys.stdout/stderr.reconfigure(encoding="utf-8")`
   shim (wrapped in try/except) is inserted before the first non-`__future__`
   import, so scripts that print mathematical glyphs (γ, ∮, ξ, …) do not crash
   under a cp1252 Windows console.
3. **stage4_methods.py convention patch** — see §3.

---

## 3. Disposition of the `stage4_methods.py` Borel-sum convention

**Finding.** The parent slot's inline Method-A inside `stage4_methods.py` used a
legacy `−1/z` Borel-sum kernel (`neg_z2Dz`, `(-1)**k` sign), which yields
`methodA_operator_duality = False` and therefore `all_three = False`. The parent
worked around this by **hand-annotating the JSON** to `True` with a human
`"note"` field rather than fixing the script.

**Correction shipped in the bundle.** The transformer rewrites that inline
Method-A to the **corrected `+1/z` kernel** (`D_ξ ↦ +1/z`, `ξ ↦ +z²D_z`;
`pos_z2Dz`, sign dropped) — the same convention already proven in the sibling
script `stage4a_methodA_v2.py` and documented in `docs/CONVENTIONS.md`.

**Effect.** With the corrected kernel:
- Method-A operator-duality residual → 0, so `methodA_operator_duality = True`
  and `all_three = True` are now produced **by the script**, not hand-edited.
- The reduced operator output is byte-identical:
  `h(z) = 27*(30*sqrt(3) + 649) / (418501*z**2*(-3 + 2*sqrt(3)))`.
- Methods B (Hankel) and C (Stokes) are **untouched**; no numerical result
  changes. Only the boolean that the legacy sign had spuriously flipped is
  corrected.

The reference `data/stage4_methods_results.json` was regenerated from the
corrected script (the human `"note"` field now lives in `docs/CONVENTIONS.md`,
§1). Harness row 11 shows the corrected script and refreshed reference agree
exactly.

---

## 4. Paper compilation + byte-reproducibility (Stage 5.3)

- **Builder:** `paper/build.py` (bundle-specific; compiles the self-contained
  `paper/vquad-periodrep-paper.tex` directly — `pdflatex` ×2, portable engine
  resolution PATH→MiKTeX fallback, `SOURCE_DATE_EPOCH=1718409600`).
- **Run from `paper/`:** `PAGES=23`, `ERRORS=0`, `PDF_EXISTS=True`.
- **SHA-256 (rebuilt):**
  `359d1172af3f867f4349cf4776a222813a855cd354bc78c0b68ccfb0026c702b`
- **Target (deposited):**
  `359D1172AF3F867F4349CF4776A222813A855CD354BC78C0B68CCFB0026C702B`
- **REPRODUCIBLE = True** (698730 bytes). Independently re-confirmed by a build
  in a pristine temp directory: identical hash.

The assembled `.tex` is fully self-contained (preamble inline, bibliography
inline as `thebibliography`; no `\input`/`\include`, no external `.bib`, no
graphics). `paper/preamble.tex` is shipped for provenance only; `build.py` does
not depend on it. The byte-identical hash is guaranteed under the environment of
record (MiKTeX 25.12 / pdfTeX 4.23); other TeX distributions yield a visually
identical PDF that may differ in byte hash (noted in `docs/DEPENDENCIES.md`).

---

## 5. Data presence (Stage 5.2)

All 12 reference JSONs are present in `data/` and are the exact comparison
targets used above. `scripts/0X-*/` ship **clean** (only `.py` + `README.md`);
running a script regenerates its result JSON next to it — that is the intended
reproduction action, and it reproduces the corresponding `data/` reference.

| data/ file | produced by |
|------------|-------------|
| holonomic_recognition_q3_results.json | holonomic_recognition_q3.py |
| operator_verification_results.json | extract_verify_operators.py |
| indicial_results.json | indicial_analysis.py |
| borel_pade_results.json | borel_pade_census.py |
| stage2_kovacic_results.json | stage2b_symsquare.py |
| stage3_galois_LV_results.json | stage3_galois_LV.py |
| stage3b_frobenius_results.json | stage3b_frobenius_v2.py |
| numcheck_period_rep_results.json | numcheck_period_rep.py |
| stage4_methodA_results.json | stage4a_methodA_v2.py |
| stage4_methods_results.json | stage4_methods.py |
| stage0_residual_results.json | stage0_residual_check.py |
| stage1_hankel_results.json | stage1_hankel_period.py |

---

## 6. Gate disposition

**HALT GATE 5: PASS.** No script failed to execute; no data file is missing or
corrupted; the paper compiles clean and reproduces the deposited PDF hash. The
bundle is internally complete and may proceed to packaging (Stage 6).

**Scope honesty (carried from `prerequisite-check.md`).** This gate certifies
*bundle integrity* — scripts run, outputs match, paper compiles
byte-reproducibly. It does **not** certify the paper as editorially final: the
prerequisite `VQUAD-PAPER-CORRECTIONS-001` slot does not exist and the cold-read
verdict is unrecorded. The bundle is assembled against the current
byte-reproducible draft and is held at ready-state pending those operator gates.
