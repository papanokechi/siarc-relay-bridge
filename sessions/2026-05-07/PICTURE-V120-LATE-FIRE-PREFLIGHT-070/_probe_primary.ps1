param()
$ErrorActionPreference = 'Continue'
$bridge = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"
Set-Location $bridge

$entries = @(
 @{tag="V1.a"; commit="9d6e801"; path="sessions/2026-05-06/CC-VQUAD-PIII-LITERATURE-PREFLIGHT/handoff.md"},
 @{tag="V1.b"; commit="29f0646"; path="sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP/handoff.md"},
 @{tag="V1.c"; commit="2eb9b28"; path="sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/handoff.md"},
 @{tag="V1.d"; commit="05810a2"; path="sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/handoff.md"},
 @{tag="V2.a"; commit="87f6b58"; path="sessions/2026-05-06/CMB-OQ-PASTE-W20-051-Q1Q2Q4-EXECUTION/handoff.md"},
 @{tag="V2.b"; commit="df7d6d4"; path="UNKNOWN"},
 @{tag="V2.c"; commit="0f1fdfc"; path="UNKNOWN"},
 @{tag="V2.d"; commit="dee3c01"; path="UNKNOWN"},
 @{tag="V2.e"; commit="6a150b6"; path="sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY/handoff.md"},
 @{tag="V2.f"; commit="6a150b6"; path="sessions/2026-05-06/PCF2-CF_VALUE-AUDIT-9IMPLS/handoff.md"},
 @{tag="V2.g"; commit="9261c79"; path="sessions/2026-05-07/PCF1-V13-V_QUAD-ROW-REFRAMING-066/handoff.md"},
 @{tag="V2.h"; commit="ec5eaca"; path="sessions/2026-05-07/BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/handoff.md"},
 @{tag="V3.a"; commit="e7bfe49"; path="sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE/handoff.md"}
)
foreach ($e in $entries) {
  Write-Host "=== $($e.tag) commit=$($e.commit) ==="
  if ($e.path -ne "UNKNOWN") {
    if (Test-Path $e.path) {
      $abs = (Resolve-Path $e.path).Path
      $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $abs).Hash
      $sz = (Get-Item -LiteralPath $abs).Length
      $bytes = [System.IO.File]::ReadAllBytes($abs)
      $lc = 0
      foreach ($b in $bytes) { if ($b -eq 0x0A) { $lc++ } }
      Write-Host "EXISTS sha=$($sha.Substring(0,16)).. size=$sz LF=$lc"
    } else {
      Write-Host "MISSING: $($e.path)"
    }
  } else {
    Write-Host "PATH_FROM_COMMIT_LOOKUP_NEEDED for $($e.commit)"
    git --no-pager show --name-only --pretty=format:'%H' $($e.commit) 2>&1 | Select-Object -First 5 | ForEach-Object { Write-Host "  $_" }
  }
}
