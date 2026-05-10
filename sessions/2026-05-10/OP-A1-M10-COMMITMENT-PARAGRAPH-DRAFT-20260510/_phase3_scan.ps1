$root = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-10\OP-A1-M10-COMMITMENT-PARAGRAPH-DRAFT-20260510"
$f = Join-Path $root "op_a1_phase2_candidates.md"

"==================== WHOLE-FILE SCANS ===================="

"---- RULE 1 leakage (Zenodo|endorsement|arXiv|Compositio|Ramanujan|AFM|venue|journal) ----"
$rule1 = Select-String -Path $f -Pattern '\b(Zenodo|endorsement|arXiv|Compositio|Ramanujan|AFM|venue|journal)\b' -CaseSensitive:$false -AllMatches
"hit count: " + ($rule1 | Measure-Object).Count
$rule1 | Select-Object LineNumber, Line | Format-Table -AutoSize

"---- FV scan strict 7-verb 3p-singular (closes|discharges|proves|establishes|ratifies|demonstrates|shows) ----"
$fv = Select-String -Path $f -Pattern '\b(closes|discharges|proves|establishes|ratifies|demonstrates|shows)\b' -CaseSensitive:$false -AllMatches
"hit count: " + ($fv | Measure-Object).Count
$fv | Select-Object LineNumber, Line | Format-Table -AutoSize

"---- non-ASCII byte count ----"
$bytes = [System.IO.File]::ReadAllBytes($f)
($bytes | Where-Object { $_ -gt 127 } | Measure-Object).Count

"==================== PER-CANDIDATE BLOCK SCANS ===================="

$content = Get-Content -Raw -Path $f
$blockA = (($content -split '## Candidate A')[1] -split '## Candidate B')[0]
$blockB = (($content -split '## Candidate B')[1] -split '## Candidate C')[0]
$blockC = (($content -split '## Candidate C')[1] -split '## Notes on drafting choices')[0]

function ScanBlock {
    param([string]$Name, [string]$Body)
    "==== Candidate $Name ===="
    $r1 = [regex]::Matches($Body, '(?i)\b(Zenodo|endorsement|arXiv|Compositio|Ramanujan|AFM|venue|journal)\b').Count
    $r2 = [regex]::Matches($Body, '(?i)\b(closes|discharges|proves|establishes|ratifies|demonstrates|shows)\b').Count
    "  RULE 1 leakage hits     : $r1"
    "  FV strict 7-verb hits   : $r2"
    "  block char length       : " + $Body.Length
    "  block line count        : " + ($Body -split "`n").Count
    "  has 'cascade-132 sec 5'   : " + ($Body -match 'cascade-132 sec 5')
    "  has 'BUNDLED-DEFERRED-NOTE': " + ($Body -match 'BUNDLED-DEFERRED-NOTE')
    "  has 'COMMITTED-2026-05-10': " + ($Body -match 'COMMITTED-2026-05-10')
    # Aggressive past/gerund inflection scan
    $aggr = [regex]::Matches($Body, '(?i)\b(close[ds]?|closing|discharg(e[ds]?|ing)|prov(e[ds]?|ing)|establish(es|ed|ing)?|ratif(y|ies|ied|ying)|demonstrat(e[ds]?|ing)|show(s|ed|ing|n)?)\b')
    "  aggressive inflection hits (informational): " + $aggr.Count
    foreach ($m in $aggr) { "    -> token: " + $m.Value }
}

ScanBlock -Name 'A' -Body $blockA
ScanBlock -Name 'B' -Body $blockB
ScanBlock -Name 'C' -Body $blockC
