$L = [System.IO.File]::ReadAllLines("tex\submitted\CMB.txt")
$h4Hits = @()
$ccHits = @()
for ($i = 0; $i -lt 1643; $i++) {
    if ($L[$i] -match 'M6\.H4 = ') { $h4Hits += ($i + 1) }
    if ($L[$i] -match 'M6\.CC = ') { $ccHits += ($i + 1) }
}
Write-Host "P6: pre-1644 (lines 1..1643)"
Write-Host "  M6.H4 = hits: $($h4Hits.Count)"
Write-Host "  M6.CC = hits: $($ccHits.Count)"
if ($h4Hits.Count -gt 0) { Write-Host "  H4 lines: $($h4Hits -join ',')" }
if ($ccHits.Count -gt 0) { Write-Host "  CC lines: $($ccHits -join ',')" }

# Also enumerate the file header structure so we can pick the insertion point
Write-Host '---first 50 lines of CMB.txt---'
for ($i = 0; $i -lt [Math]::Min(50, $L.Length); $i++) {
    Write-Host ("{0,4}: {1}" -f ($i + 1), $L[$i])
}
