# Zenodo v2.1 deposit log -- 116 (PARTIAL: agent-side prep + operator-side fire)

**Status (agent-side):** READY_FOR_OPERATOR
**Status (deposit):** PENDING_OPERATOR_FIRE
**Reason for partial:** the agent's persistent PowerShell terminal cannot
authenticate to the Zenodo web UI (same class of limitation as the
`gh-auth-agent-terminal-limitation-2026-04-29` repo memory entry: no
TTY for OAuth device-code flow; no Zenodo API token present in the
agent's process scope). Agent has produced the PDF, the source diff,
the metadata package, and the AEAL artefact bundle below, all
deposit-ready. The operator (papanokechi) fires Phase C from a fresh
browser session.

---

## 1. Deposit-ready artefacts (this session folder)

| Artefact | Path | SHA256 | Size |
|---|---|---|---|
| Umbrella v2.1 PDF | `umbrella_v21.pdf` | `436962F093A95DB12AF6FD84B99515BE802A274C14B3EFE182EDACA3DF87A35D` | 495254 bytes (15 pages) |
| Umbrella v2.1 TeX source | `umbrella_v21.tex` | (compiled from same tree as PDF) | 1019 lines |
| v2.0 -> v2.1 diff | `b_amendment.diff` | -- | 255 lines |
| AEAL claims (audit-only) | `claims.jsonl` | -- | 7 entries (0 new numerical claims) |
| Bridge SHA list | `bridge_sha_list.md` | -- | 4 substrate SHAs |

The PDF pdflatex baseline is documented in
`b_pdflatex_compile_log.md`: pass-1 W=127 + 84 undef-msgs (label-shift,
expected); pass-2 W=43 + 0 errors + 0 undefined refs; 15 pages.

## 2. Zenodo cascade target

- **Concept DOI (umbrella, all-versions):**
  `10.5281/zenodo.19885550` -- *canonical per `tex/submitted/umbrella_program_paper/main.tex`
  L853 (existing v1 / v2.0 source); per picture cross-walks
  `tex/submitted/control center/picture_revised_2026050{2,3,4}.md`
  the concept DOI is recorded as `19885549` (off-by-one from the tex
  source). The 077 portfolio bundling audit
  (`sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/portfolio_substrate_anchor_shas.md`
  L78) flagged a third reading of `19965040` as concept (audit verdict:
  concept x). See `discrepancy_log.json` DISCREPANCY-116-CONCEPT-DOI for
  the resolution: agent uses the tex-source value `19885550` as
  canonical; operator should verify against the Zenodo record's actual
  concept-DOI on the deposit page during Phase C.
- **Previous version DOI (v2.0):** `10.5281/zenodo.19965041`
- **New version DOI (v2.1):** ASSIGNED AT DEPOSIT TIME (operator captures
  + reports back for Phase D submission_log splice).

## 3. Operator runbook -- Phase C (Zenodo deposit)

Estimated time: ~30-45 min.

### C.1 Open + start new version

1. Browse to <https://doi.org/10.5281/zenodo.19965041> (umbrella v2.0
   record).
2. Verify the concept DOI on the record header (right-hand sidebar
   "Versions" widget) and update `discrepancy_log.json` DISCREPANCY-116-CONCEPT-DOI
   with the actual value.
3. Click `New version` (top-right); Zenodo creates a draft inheriting
   metadata.

### C.2 Upload artefacts

1. Replace the v2.0 PDF with `umbrella_v21.pdf` from this session
   folder.
2. Optionally also upload as supporting files:
   - `umbrella_v21.tex` (TeX source; for reproducibility)
   - `b_amendment.diff` (v2.0 -> v2.1 diff)
   - `claims.jsonl` (AEAL audit bundle for v2.1)
   - `bridge_sha_list.md` (substrate SHA manifest)

### C.3 Update metadata

| Field | New value |
|---|---|
| Title | An Arithmetic Stratification of Polynomial Continued Fractions: Program Statement of the SIARC Series (v2.1: Closure Cascade Amendment) |
| Authors | papanokechi (ORCID 0009-0000-6192-8273) |
| Description | Append (or replace) with the changelog block in `zenodo_v21_description_block.md` |
| Version | 2.1 |
| Publication date | 2026-05-09 (or operator's actual deposit date) |
| Resource type | Preprint |
| Subjects/keywords | (carry-over from v2.0) + `M4 V0 closure`, `M6.CC R1 closure`, `Route F D_7 sector`, `SIARC closure cascade` |
| Related identifiers | See section C.4 below |

### C.4 Related identifiers (Zenodo metadata, "Related/alternate identifiers" block)

Set on the v2.1 record's metadata:

| Relation | Identifier | Resource type | Note |
|---|---|---|---|
| `IsVersionOf` | `10.5281/zenodo.19885550` (concept; verify per C.1.2) | Preprint | Umbrella concept record |
| `IsNewVersionOf` | `10.5281/zenodo.19965041` | Preprint | Umbrella v2.0 |
| `Cites` | `10.5281/zenodo.19937196` | Preprint | PCF-1 v1.3 |
| `Cites` | `10.5281/zenodo.19963298` | Preprint | PCF-2 v1.3 |
| `Cites` | `10.5281/zenodo.19951331` | Preprint | CT v1.2 |
| `Cites` | `10.5281/zenodo.19915689` | Preprint | T2B v3.0 |

(D2-NOTE v2.x has no Zenodo DOI yet per the v2.0 companion table
`Drafting / forthcoming` row; skip until D2-NOTE deposits.)

### C.5 Publish + capture DOI

1. Click `Publish`.
2. Capture the assigned v2.1 version DOI from the record header.
3. Verify resolution:
   ```
   curl -sI https://doi.org/10.5281/zenodo.<NEW> | grep -i ^location
   ```
   Expected: `location: https://zenodo.org/records/<NEW>`.
4. Record the new DOI in `phase_c_completion_note.md` (operator
   creates) and report the value back to the agent for Phase D
   submission_log splice.

### C.6 If deposit fails

- Save the draft (do NOT discard) and copy the error message verbatim
  into `phase_c_completion_note.md` under "DEPOSIT_FAILURE".
- Do NOT click `Publish` more than once.
- The Zenodo support address is `info@zenodo.org`; the GitHub Zenodo
  helpdesk is <https://help.zenodo.org/>.

## 4. Operator runbook -- Phase D (cross-link metadata edits)

Estimated time: ~10-15 min (5 records, ~2-3 min each).

For each of the records below, on Zenodo (logged in):

1. Open the record page.
2. Click `Edit` on the latest published version.
3. In `Related/alternate identifiers`, add a row:
   `IsCitedBy` / `<v2.1 DOI from C.5>` / Preprint.
4. Save (no PDF re-upload required).

| Record | Latest version DOI | Concept DOI |
|---|---|---|
| PCF-1 v1.3 | `10.5281/zenodo.19937196` | `10.5281/zenodo.19931635` |
| PCF-2 v1.3 | `10.5281/zenodo.19963298` | `10.5281/zenodo.19936297` |
| CT v1.2 | `10.5281/zenodo.19951331` | `10.5281/zenodo.19941678` |
| T2B v3.0 | `10.5281/zenodo.19915689` | `10.5281/zenodo.19783311` |
| D2-NOTE v2.x | DEFERRED -- no Zenodo DOI yet (drafting) | -- |

A7 acceptance lists 5 records but D2-NOTE has not deposited; operator
fires only 4 cross-link edits and records the D2-NOTE deferral in
`cross_link_update_log.md` post-fire. This is logged as
DISCREPANCY-116-D2NOTE-NO-DOI in `discrepancy_log.json`.

## 5. Operator runbook -- Phase D (submission_log splice)

After Phase C captures the v2.1 DOI:

1. Replace `<DOI-PENDING-PHASE-C>` placeholders in
   `submission_log_item11_splice.diff` with the actual v2.1 DOI.
2. Apply the diff to `tex/submitted/submission_log.txt`:
   ```
   cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat"
   git apply siarc-relay-bridge/sessions/2026-05-09/T1-EXECUTOR-116-UMBRELLA-V21-M9-V0-DEPOSIT-133/submission_log_item11_splice.diff
   ```
   (Note: prompt 116 spec said "Item 22 series 2"; actual current series
   2 last item is Item 10 not Item 21, so the splice is Item 11 not
   Item 22. See DISCREPANCY-116-SUBLOG-NUMBERING.)
3. Run the post-splice grep invariants from the prompt's D.4:
   ```
   Select-String -Path submission_log.txt -Pattern '^11\.' | Measure-Object | Select-Object -ExpandProperty Count
   # expected: 1 (the new Item 11 in series 2)
   Select-String -Path submission_log.txt -Pattern 'umbrella' | Measure-Object | Select-Object -ExpandProperty Count
   # expected: increment +1 vs pre-splice (the new Item 11 reference)
   Select-String -Path submission_log.txt -Pattern '<TBD>|<TODO>|<DOI-PENDING'
   # expected: empty
   ```

## 6. Hand-back protocol

When Phase C + D are complete, the operator pastes the v2.1 DOI into a
fresh agent chat with `116-FOLLOWUP-DOI` as the task ID and the agent
fires the Phase D submission_log splice + Phase E standing-final-step
under that follow-up task. Alternatively the operator self-applies the
diff per section 5 above; either path closes the M9 V0 deposit.

## 7. Forbidden-verb scan on this file

Run during agent's Phase E:

```
Select-String -Path zenodo_v21_deposit_log.md -Pattern 'confirms|proves|demonstrates|validates|corroborates|certifies|settles|discharges' -CaseSensitive:$false
```

Expected: only quoted occurrences inside audit-trail blocks (e.g. the
v2.0 -> v2.1 paragraph quoting Q4 v2 verdict text). Bare predictive
prose hits are flagged for mitigation pre-commit.
