# Cross-link update log -- 116 v2.1 (operator-pending)

**Status:** PREPARED_FOR_OPERATOR
**Fires:** AFTER Phase C captures the v2.1 DOI.

This file is the operator's checklist + completion log for the
A7 acceptance criterion (5 records' Zenodo metadata `Related
identifiers` updated to add `IsCitedBy` of the new umbrella v2.1
DOI).

## Pre-conditions

- v2.1 DOI assigned (Phase C complete; recorded in
  `phase_c_completion_note.md`).
- Operator has Zenodo session open with edit rights on each of the
  records below.

## Records to update

| # | Record | Latest version DOI | Status | Operator timestamp (JST) | Notes |
|---|---|---|---|---|---|
| 1 | PCF-1 v1.3 | `10.5281/zenodo.19937196` | PENDING | -- | Add `IsCitedBy` `<v2.1 DOI>` |
| 2 | PCF-2 v1.3 | `10.5281/zenodo.19963298` | PENDING | -- | Add `IsCitedBy` `<v2.1 DOI>` |
| 3 | CT v1.2 | `10.5281/zenodo.19951331` | PENDING | -- | Add `IsCitedBy` `<v2.1 DOI>` |
| 4 | T2B v3.0 | `10.5281/zenodo.19915689` | PENDING | -- | Add `IsCitedBy` `<v2.1 DOI>` |
| 5 | D2-NOTE v2.x | -- | DEFERRED | -- | No Zenodo DOI yet (drafting) -- A7 partial; see DISCREPANCY-116-D2NOTE-NO-DOI |

## Per-record procedure (Zenodo UI)

1. Open the record page (browser, logged in).
2. Click `Edit` on the latest published version.
3. Scroll to `Related/alternate identifiers`.
4. Click `Add identifier`.
5. Fill:
   - Identifier: `10.5281/zenodo.<v2.1>` (the value captured in Phase C.5)
   - Relation: `IsCitedBy`
   - Resource type: Preprint
6. Click `Save`.
7. Confirm by reopening the record metadata view; check the new row
   appears in `Related identifiers`.
8. Update this table with `DONE` + JST timestamp.

## Verification (post-fire)

After all 4 active edits are done, run from a fresh terminal (no auth
needed -- read-only DOI head):

```
$dois = '10.5281/zenodo.19937196','10.5281/zenodo.19963298','10.5281/zenodo.19951331','10.5281/zenodo.19915689'
$dois | ForEach-Object {
    Write-Host "=== $_ ==="
    Invoke-RestMethod "https://zenodo.org/api/records/$($_.Replace('10.5281/zenodo.',''))" |
        Select-Object -ExpandProperty metadata |
        Select-Object -ExpandProperty related_identifiers |
        Where-Object { $_.relation -eq 'isCitedBy' } |
        Format-Table -AutoSize
}
```

Expected: each record returns at least one row whose `identifier`
matches the v2.1 DOI.

## Completion criteria

- Records 1-4 updated and verified via the API call above.
- Record 5 (D2-NOTE) deferred and recorded in
  `discrepancy_log.json` as DISCREPANCY-116-D2NOTE-NO-DOI.
- Final state of this file: all 4 active rows status = DONE.
- Then proceed to submission_log splice (Phase D continues).
