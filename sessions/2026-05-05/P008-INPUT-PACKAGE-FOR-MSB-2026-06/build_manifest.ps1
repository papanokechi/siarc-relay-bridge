$ErrorActionPreference = "Stop"
$ws = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat"
$sd = "$ws\siarc-relay-bridge\sessions\2026-05-05\P008-INPUT-PACKAGE-FOR-MSB-2026-06"

$entries = @(
  @{ id="S1"; label="Umbrella v2.0 main.tex"; path="$ws\tex\submitted\umbrella_program_paper\main.tex" }
  @{ id="S2"; label="CT v1.3 channel_theory_outline.tex"; path="$ws\pcf-research\channel\cc_pipeline_v13_2026-05-02\channel_theory_outline.tex" }
  @{ id="S3"; label="M9 main-theorem dependency audit handoff"; path="$ws\siarc-relay-bridge\sessions\2026-05-05\M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT\handoff.md" }
  @{ id="S4"; label="T2B v3.1 bipartition manuscript"; path="$ws\siarc-relay-bridge\sessions\2026-05-07\PCF-2-V2-BIPARTITION-PROMOTION\t2b_paper_v3.1_bipartition_promotion.tex" }
  @{ id="S5"; label="Working M9 main-theorem statement (workspace search)"; path="<grep tex/submitted/**/*.tex>" }
  @{ id="S6_CMB"; label="CMB.txt (M6 status surface)"; path="$ws\tex\submitted\CMB.txt" }
  @{ id="S6_cli_log"; label="cli_log\2026-05-05.md (M6 arbitration status)"; path="$ws\cli_log\2026-05-05.md" }
  @{ id="S6_W19_wsb"; label="cli_log\2026-W19_wsb.md (M6 framing in WSB)"; path="$ws\cli_log\2026-W19_wsb.md" }
  @{ id="S7"; label="Departing-Synthesizer's three standing notes (043 inbox handoff)"; path="$ws\tex\submitted\control center\synthesizer_inbox\STRATEGYZER_HANDOFF_2026-05-08.md" }
)

$manifest = @{ compiled_utc = (Get-Date).ToUniversalTime().ToString("o"); compiler = "CLI-Tactical-Executer (relay 045)"; entries = @() }
foreach ($e in $entries) {
  $entry = @{ id = $e.id; label = $e.label; path = $e.path }
  if ($e.id -eq "S5") {
    $entry.status = "NOT_FOUND"
    $entry.reason = "workspace grep over tex/submitted/**/*.tex for thm:main|main_theorem|Main Theorem|Theorem 1.1|theorem M9|theorem:M9 returned 6 hits, NONE of which is a SIARC Master Conjecture / MASTER-V0 / Phi formal statement (matches: umbrella main.tex L194 forward-ref to companion paper #14; paper14 §Main Theorem = Ratio Universality, not Phi; pcf_rational_contamination thm:main = Trivial rational limit observation; pcf_unified_expmath_submission abstract 'two main theorems' = Logarithmic Ladder + 4/pi Casoratian)."
  } elseif (Test-Path $e.path) {
    $entry.status = "FOUND"
    $entry.size_bytes = (Get-Item $e.path).Length
    $entry.sha256 = (Get-FileHash $e.path -Algorithm SHA256).Hash
    $entry.mtime_utc = (Get-Item $e.path).LastWriteTimeUtc.ToString("o")
  } else {
    $entry.status = "NOT_FOUND"
    $entry.reason = "path absent on disk at compile time"
  }
  $manifest.entries += $entry
}
$manifest | ConvertTo-Json -Depth 5 | Out-File -FilePath "$sd\p008_substrate_manifest.json" -Encoding utf8
Write-Host "Manifest written."
Get-Content "$sd\p008_substrate_manifest.json"
