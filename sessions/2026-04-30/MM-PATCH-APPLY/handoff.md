# MM-PATCH-APPLY — RESUME complete

**Status:** All four steps executed, three PDFs rebuilt clean, all verification greps pass.
**Pending:** papanokechi confirmation before push.

## Files modified

| File | tex sha256 | pdf size | pdf sha256 |
|---|---|---|---|
| `tex/submitted/p06_desert_ijnt_submission/pcf_desert_negative_result.tex` | `766462C5…E646D98F` | 403,905 B | `2DA49173…B9BD882E` |
| `tex/submitted/paper4_takeuchi_outline.tex` | `0864EB3D…125AFE0F` | 431,999 B | `F994525A…F87FD091` |
| `tex/submitted/umbrella_program_paper/main.tex` | `92631F7C…DC5D1D12` | 287,109 B | `D85C5260…1489B8B6` |

(MM-02 affects two of these files — UMB gets the translation remark, #14 gets the global rename.)

## Step-by-step record

### Step 1 — MM-01 (P06 line 314)

Single substitution per `patch_relay_MM01.md`:

- OLD: `case~\cite{P11}, which lie at degree profile $(2,2)$ with coefficient bound~$4$ and whose limits are M\"obius transforms of`
- NEW: `case~\cite{P11}, which lie at degree-$(2,1)$ profile (numerator quadratic, denominator linear; \cite[Prop.~prop:deg21]{P11}) inside the coefficient-bound-$4$ ambient space and whose limits are M\"obius transforms of`

Verification: `grep "degree profile.*(2,2)" pcf_desert_negative_result.tex` → **0 hits**.

### Step 2 — MM-02 (rename in #14, translation remark in UMB)

`paper4_takeuchi_outline.tex`: ordered regex replacement covering all variants — `Tier~$0..3$` (math mode), `Tier~0..3` (non-breaking space), `Tier 0..3` (regular space), `Tiers~1 and~3` (compound), and table-header `Family & Tier`. Narrative phrases such as "four-tier" (no digit) and the title "Four-Tier Obstruction Hierarchy" are preserved.

Verification: `grep '\bTier[~ ][0-3]\b' paper4_takeuchi_outline.tex` → **0 hits**.

`umbrella_program_paper/main.tex` §2 (Tiers): inserted `\begin{remark}[Translation to the obstruction hierarchy of \#14] \label{rem:tier-translation} ...` immediately after the four T0..T3 definitions, stating the inclusions $O_0 \subseteq T_0 \cup T_2$, $O_1 \subseteq T_2$, $O_2 \subseteq T_2$, $O_3 \subseteq T_3$ and that neither hierarchy refines the other. UMB's $T_0..T_3$ labels are **NOT** renamed (per resume directive).

### Step 3 — MM-03 (UMB conj:t2b two-class form)

OLD/NEW substitution in `conj:t2b` matches `patch_relay_MM03.md` content. The post-conjecture `\begin{remark}[Pre-revision form] \label{rem:t2b-prerev}` block was added immediately after the conjecture, citing UMB v1 Zenodo DOI 10.5281/zenodo.19885550.

**One additional consistency fix** (flagged separately in `unexpected_finds.json`): line 51 of UMB's abstract previously read "Trans-Stratum $-2/9$ Conjecture in precise form". Left as-is, this would create an internal contradiction with the body's now-renamed "Trans-stratum two-class conjecture" (HALT IF: "any reader path UMB → T2B → UMB still produces a contradiction after the patch"). Amended to "Trans-stratum two-class conjecture (Class A at $a_2/b_1^2 = -2/9$, Class B at $a_2/b_1^2 = +1/4$) in precise form". This is a faithful one-line update consistent with the patch's stated additive intent (no Class A claim revoked; only the title and a Class B clause added).

### Step 4 — Rebuild

All three files rebuilt with `pdflatex -interaction=nonstopmode -halt-on-error` (two passes each). No `!`-line errors, no fatal warnings on any of the three. Sizes and hashes recorded above.

## Verification grep checks

| Check | Result |
|---|---|
| `grep "degree profile.*(2,2)"` in P06 | 0 hits ✅ |
| `grep '\bTier[~ ][0-3]\b'` in #14 | 0 hits ✅ |
| `grep "T-arith"` in UMB | 0 hits ✅ (rename intentionally not applied) |
| `grep "conj:t2b"` in UMB | label present at line 242 inside new typed two-regime conjecture ✅ |

## What is preserved unchanged

- T2B v2.0 manuscript (`t2b_paper_draft_v5_withauthor_v2.tex`) — out of scope for this patch.
- UMB §6 status table (DOIs, statuses, T2B citation chain) — out of scope.
- UMB Remark 8 ("Why $-2/9$?") — out of scope; still uses the indicial-roots derivation as installed during UMB-main-fix.
- All other companion papers (P08, T2A, P11, P06 outside line 314).

## What still needs human attention before the push

1. **Reconciliation hint for T2B v3.0** (NOT done by this patch): the new UMB Conjecture explicitly cites "T2B Theorem 2 conditional on $S_{12}\neq 0$" and "T2B Theorem 3 + Cor.~classB-pi". Confirm those exact theorem numbers and corollary label exist in T2B v2.0; if T2B uses different labels, either UMB or T2B needs a one-line label fix. (This was raised but not patched.)
2. **Companion paper #14 narrative consistency**: a few bare uses of "Tier" without a digit remain in places like "first numerical audit of the Tier~0 j-distribution" (now "Obstruction Tier O0 j-distribution") — these are correct but the sentence flow is slightly clunkier. Consider a light pass on the rendered #14 PDF before submitting; not required for this patch.
3. **A second coherence audit pass restricted to UMB ∪ T2B** is mandatory before any Zenodo upload, per the MM-03 patch's HALT IF clause. Recommend running the P-10 pipeline scoped to those two files only.

## Bridge commit

Staged files in this session:
- `claims.jsonl` (6 entries)
- `halt_log.json` (from previous halt; preserved for audit trail)
- `unexpected_finds.json` (abstract line 51 consistency fix)
- `discrepancy_log.json` (empty)
- `handoff.md` (this file)

Suggested commit message: `MM-PATCH-APPLY -- MM-01/02/03 applied, P06+#14+UMB patched, verification clean`.
**No push performed.** Awaiting papanokechi confirmation.
