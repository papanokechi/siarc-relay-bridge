$base = "c:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat"
$files = @(
  "$base\cli_log\2026-W20.md",
  "$base\cli_log\2026-W21_wsb.md",
  "$base\cli_log\wsb_iso_convention.md",
  "$base\siarc-relay-bridge\sessions\2026-05-07\T1-W20-CLOSING-W21-WSB-081\w20_arc_inventory.md"
)
$verbPatterns = @('\basserts\b','\bproves\b','\bcloses\b','\bdemonstrates\b','\bestablishes\b','\bratifies\b','\bshows\b','\bconfirms\b','\bdischarges\b')
foreach ($f in $files) {
  $name = Split-Path $f -Leaf
  $content = Get-Content -LiteralPath $f -Raw
  $lines = Get-Content -LiteralPath $f
  Write-Host ""
  Write-Host "=== $name ==="
  $totalHits = 0
  foreach ($p in $verbPatterns) {
    $matches = [regex]::Matches($content, $p, 'IgnoreCase')
    if ($matches.Count -gt 0) {
      Write-Host ("  pattern: {0} -- {1} hit(s)" -f $p, $matches.Count)
      $totalHits += $matches.Count
      foreach ($m in $matches) {
        $lineNum = ($content.Substring(0, $m.Index) -split "`n").Count
        $lineText = $lines[$lineNum-1]
        if ($lineText.Length -gt 110) { $lineText = $lineText.Substring(0,110) + "..." }
        Write-Host ("    L{0}: {1}" -f $lineNum, $lineText)
      }
    }
  }
  Write-Host ("  total: {0} hits" -f $totalHits)
}
