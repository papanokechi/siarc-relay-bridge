param()
$ErrorActionPreference = 'Continue'
$bridge = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"
Set-Location $bridge

# All 27 entries with corrected paths
$entries = @(
 # PRIMARY V1.*
 @{tag="V1.a"; class="PRIMARY"; commit="9d6e801"; path="sessions/2026-05-06/CC-VQUAD-PIII-LITERATURE-PREFLIGHT/handoff.md"},
 @{tag="V1.b"; class="PRIMARY"; commit="29f0646"; path="sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP/handoff.md"},
 @{tag="V1.c"; class="PRIMARY"; commit="2eb9b28"; path="sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/handoff.md"},
 @{tag="V1.d"; class="PRIMARY"; commit="05810a2"; path="sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/handoff.md"},
 # PRIMARY V2.*
 @{tag="V2.a"; class="PRIMARY"; commit="87f6b58"; path="sessions/2026-05-06/CMB-OQ-PASTE-W20-051-Q1Q2Q4-EXECUTION/handoff.md"},
 @{tag="V2.b"; class="PRIMARY"; commit="df7d6d4"; path="sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/handoff.md"},
 @{tag="V2.c"; class="PRIMARY"; commit="0f1fdfc"; path="sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4-HALT-061-DUPLICATE-DETECTED/handoff.md"},
 @{tag="V2.d"; class="PRIMARY"; commit="dee3c01"; path="sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/handoff.md"},
 @{tag="V2.e"; class="PRIMARY"; commit="6a150b6"; path="sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/handoff.md"},
 @{tag="V2.f"; class="PRIMARY"; commit="6a150b6"; path="sessions/2026-05-06/PCF2-CF_VALUE-AUDIT-9IMPLS-065/handoff.md"},
 @{tag="V2.g"; class="PRIMARY"; commit="9261c79"; path="sessions/2026-05-07/PCF1-V13-V_QUAD-ROW-REFRAMING-066/handoff.md"},
 @{tag="V2.h"; class="PRIMARY"; commit="ec5eaca"; path="sessions/2026-05-07/BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/handoff.md"},
 # PRIMARY V3.*
 @{tag="V3.a"; class="PRIMARY"; commit="e7bfe49"; path="sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068/handoff.md"},
 # PARALLEL V4.*
 @{tag="V4.a"; class="PARALLEL"; commit="fe15737"; path="sessions/2026-05-06/T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE/handoff.md"},
 @{tag="V4.b"; class="PARALLEL"; commit="82001aa"; path="sessions/2026-05-06/T2B-TIGHTENED-SWEEP-OUTCOME-B/handoff.md"},
 @{tag="V4.c"; class="PARALLEL"; commit="7509e34"; path="sessions/2026-05-06/N3-FOURTH-LAW-ARBITRATION-SUBSTRATE/handoff.md"},
 @{tag="V4.d"; class="PARALLEL"; commit="6bbd3f0"; path="sessions/2026-05-06/W19-CLOSING-W20-WSB/handoff.md"},
 @{tag="V4.e"; class="PARALLEL"; commit="5d83797"; path="sessions/2026-05-07/PCF-2-V2-BIPARTITION-PROMOTION/handoff.md"},
 @{tag="V4.f"; class="PARALLEL"; commit="8e18465"; path="sessions/2026-05-07/T2B-BIPARTITION-B7-STRONG-NULL/handoff.md"},
 # SECONDARY V5.*
 @{tag="V5.a"; class="SECONDARY"; commit="7acfa67"; path="sessions/2026-05-06/M6-AMENDMENT-1-CMB-GLOSSARY-REFIRE/handoff.md"},
 @{tag="V5.b"; class="SECONDARY"; commit="?"; path="sessions/2026-05-06/M6-AMENDMENT-2-CAVEAT-LEG-NAMING-CONVENTION/handoff.md"},
 @{tag="V5.c"; class="SECONDARY"; commit="48c1dcb"; path="sessions/2026-05-06/JTNB-REJECTION-CASCADE-PASTE-062/handoff.md"},
 @{tag="V5.d"; class="SECONDARY"; commit="e75fd9d"; path="sessions/2026-05-06/P11-SICF-DECISION-W20-REFIRE/handoff.md"},
 @{tag="V5.e"; class="SECONDARY"; commit="?"; path="sessions/2026-05-06/P11-COVERLETTER-MATHCOMP-DEFENSIVE/handoff.md"},
 @{tag="V5.f"; class="SECONDARY"; commit="?"; path="sessions/2026-05-06/048R-EARLY-FIRE-DECISION-SUBSTRATE/handoff.md"},
 @{tag="V5.g"; class="SECONDARY"; commit="e7ce5da"; path="sessions/2026-05-06/048R-EARLY-FIRE-SUBSTRATE-PASTE-056/handoff.md"},
 @{tag="V5.h"; class="SECONDARY"; commit="?"; path="sessions/2026-05-06/P009-M8B-CAVEAT-FINAL/handoff.md"}
)

foreach ($e in $entries) {
  $exists = Test-Path -LiteralPath $e.path
  if ($exists) {
    $abs = (Resolve-Path -LiteralPath $e.path).Path
    $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $abs).Hash
    $sz = (Get-Item -LiteralPath $abs).Length
    $bytes = [System.IO.File]::ReadAllBytes($abs)
    $lc = 0
    foreach ($b in $bytes) { if ($b -eq 0x0A) { $lc++ } }
    Write-Host "$($e.tag) $($e.class) commit=$($e.commit) sha=$($sha.Substring(0,16)).. size=$sz LF=$lc path=$($e.path)"
  } else {
    Write-Host "$($e.tag) $($e.class) commit=$($e.commit) MISSING path=$($e.path)"
  }
}
