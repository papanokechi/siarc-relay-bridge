$bases = @{
  "074" = "sessions/2026-05-07/T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074"
  "075" = "sessions/2026-05-07/T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK-075"
  "077" = "sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077"
  "078" = "sessions/2026-05-07/T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078"
  "079" = "sessions/2026-05-07/T2-LEAN-RELAUNCH-VENUE-FIT-DOSSIER-079"
}

$results = @()
foreach ($key in $bases.Keys | Sort-Object) {
  $dir = $bases[$key]
  Get-ChildItem -Path $dir -File | ForEach-Object {
    $h = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
    $lc = (Get-Content $_.FullName | Measure-Object -Line).Lines
    $results += [pscustomobject]@{
      Dossier = $key
      File    = $_.Name
      SHA16   = $h.Substring(0,16)
      Bytes   = $_.Length
      Lines   = $lc
    }
  }
}

# Also anchor 076 GATED preflight
$envFile = "../tex/submitted/control center/prompt/076_t3_path_delta_literature_recon.txt"
if (Test-Path $envFile) {
  $h = (Get-FileHash -Algorithm SHA256 -LiteralPath $envFile).Hash
  $lc = (Get-Content $envFile | Measure-Object -Line).Lines
  $sz = (Get-Item $envFile).Length
  $results += [pscustomobject]@{
    Dossier = "076_GATED"
    File    = "076_t3_path_delta_literature_recon.txt"
    SHA16   = $h.Substring(0,16)
    Bytes   = $sz
    Lines   = $lc
  }
}

$results | Sort-Object Dossier, File | Format-Table -AutoSize | Out-String -Width 200
$results | Export-Csv -NoTypeInformation -Path "sessions/2026-05-07/T2-LANE1-CROSS-DOSSIER-COUPLING-ANALYSIS-080/_phase_a_sha_inventory.csv"
Write-Host "BRIDGE_HEAD: $((git rev-parse --short HEAD))"
Write-Host "TOTAL_FILES: $($results.Count)"
