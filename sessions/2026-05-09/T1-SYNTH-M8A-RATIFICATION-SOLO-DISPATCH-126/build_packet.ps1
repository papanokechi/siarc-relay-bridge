#!/usr/bin/env pwsh
# Build dispatch_packet.txt for slot 126 (M8a V0 ratification solo-dispatch)
# Mirrors 122 structure with M7 -> M8a token substitutions and 125 substrate
# Run from bridge repo root.

$ErrorActionPreference = "Stop"

$folder126 = "sessions/2026-05-09/T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126"
$substratePath125 = "sessions/2026-05-09/T2-EXECUTOR-M8A-RATIFICATION-SUBSTRATE-PREP-125/m8a_v0_ratification_template.md"
$substrateSHA125 = (Get-FileHash -Algorithm SHA256 $substratePath125).Hash
$substrateBytes125 = (Get-Item $substratePath125).Length
$substrateLines125 = (Get-Content $substratePath125).Count

# Header (lines 1-58 in 122 pattern; M8a tokens baked in)
$header = @"
================ CLAUDE.AI T1-SYNTH DISPATCH PACKET — M8A V0 RATIFICATION ================
Task ID: T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126
Drafted: 2026-05-09
Substrate: sessions/2026-05-09/T2-EXECUTOR-M8A-RATIFICATION-SUBSTRATE-PREP-125/m8a_v0_ratification_template.md
Substrate SHA-256: $substrateSHA125
Bridge HEAD at dispatch: 3a86cc9 (post-127-halt addendum; substrate 125 landed at 4f15411)
==========================================================================================

OPERATOR INSTRUCTIONS (do NOT paste this header block; start at "===PASTE FROM HERE==="):
1. Open a fresh Claude.ai conversation tab.
2. Set system / first message tone as a peer-review T1-Synth consultation.
3. Copy everything from the "===PASTE FROM HERE===" line below to the "===END PASTE===" line.
4. Submit. When Claude.ai responds, save the verbatim response to:
     sessions/2026-05-09/T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126/synth_verdict_raw.txt
5. Then run the cascade-absorption fire (127) to structure the verdict + close the M8a chain.

==========================================================================================
===PASTE FROM HERE===

You are a T1-Synth peer reviewing a candidate M8a V0 axis-closure ratification request from
the SIARC pipeline.

Scope: SIARC paper-foundation infrastructure axis M8a (d=2 PCF-1 §3 sign-of-Delta_b dichotomy
+ Painlevé classification full coverage). Refer ONLY to the substrate provided below. Do NOT
speculate beyond it. If the substrate is insufficient, return verdict label DEFER with
explicit reasoning.

Read carefully — this is a substrate-bounded review. Treat the embedded template as the
sole evidentiary base. You may cite, paraphrase, or quote verbatim; you may NOT introduce
external claims, references, or numerical results not already present in the substrate.

Your task: answer Q1-Q5 from §3 in order. For Q4, emit one of:
  - RATIFY                  (M8a V0 closure is mathematically supported; no amendment needed)
  - RATIFY_WITH_AMENDMENT   (closure supported but requires a specific manuscript-content
                             amendment; specify the amendment in Q5)
  - DEFER                   (substrate insufficient; specify what additional substrate is
                             needed)
  - OBJECT                  (closure NOT mathematically supported; specify objection)

Return verdict in this exact format:

  M8A_V0_VERDICT: <LABEL>
  Confidence band: <HIGH/MEDIUM/LOW>

  ## §1 reasoning
  ...

  ## §2 reasoning
  ...

  ## §3 reasoning
  ...

  ## §4 verdict label + reasoning
  ...

  ## §5 amendment specification (if RATIFY_WITH_AMENDMENT)
  ...

================ SUBSTRATE BEGIN (m8a_v0_ratification_template.md) ================
"@

# Footer (lines 513-550 in 122 pattern; M8a tokens baked in)
$footer = @"
================ SUBSTRATE END (m8a_v0_ratification_template.md) ================

End of substrate. Now answer Q1-Q5 from §3 of the substrate, emitting the verdict block in
the exact format specified above.

If you find the substrate ambiguous on any point, prefer DEFER with a specific request
for additional substrate over speculation.

If you find a mathematical objection to M8a V0 closure that is not addressed in the
substrate, emit OBJECT with the objection stated as a precise mathematical claim
(not a stylistic concern).

If you find the substrate sufficient and the closure mathematically supported, emit
RATIFY (or RATIFY_WITH_AMENDMENT if a specific manuscript-content amendment is needed
to make the closure stand cleanly).

End of dispatch.

===END PASTE===
==========================================================================================

POST-DISPATCH OPERATOR CHECKLIST:
  [ ] Saved verbatim Claude.ai response to synth_verdict_raw.txt in this folder.
  [ ] Verified verdict label is one of {RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}.
  [ ] Verified §1-§5 reasoning sections are present.
  [ ] Ready to fire 127 cascade-absorption.

If Claude.ai response is missing one of the §1-§5 sections, re-prompt with:
  "Please re-emit your verdict in the exact format specified, including all §1-§5
   reasoning sections."

If Claude.ai emits a verdict label not in the allowed set, re-prompt with:
  "Please re-emit your verdict label as one of {RATIFY, RATIFY_WITH_AMENDMENT,
   DEFER, OBJECT}."

==========================================================================================
END DISPATCH PACKET (T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126)
==========================================================================================
"@

# Normalize all to CRLF (Windows convention; matches 122)
$headerCRLF = $header -replace "`r?`n", "`r`n"
$substrateRaw = (Get-Content $substratePath125 -Raw) -replace "`r?`n", "`r`n"
$footerCRLF = $footer -replace "`r?`n", "`r`n"

# Compose: header + CRLF + substrate (already includes its own trailing newline) + CRLF + footer
# Match 122 layout: header ends with SUBSTRATE BEGIN marker; then a CRLF; then substrate body;
# then CRLF; then SUBSTRATE END marker (which is the first line of footer); then footer.
$packet = $headerCRLF + "`r`n" + $substrateRaw.TrimEnd() + "`r`n" + "`r`n" + $footerCRLF

# Write packet atomically (UTF-8 no BOM; matches 122)
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$packetPath = "$folder126/dispatch_packet.txt"
[System.IO.File]::WriteAllText((Resolve-Path $folder126).Path + "/dispatch_packet.txt", $packet, $utf8NoBom)

# Stats
$packetBytes = (Get-Item $packetPath).Length
$packetLines = (Get-Content $packetPath).Count
$packetSHA = (Get-FileHash -Algorithm SHA256 $packetPath).Hash

Write-Host "=== Slot 126 dispatch packet built ==="
Write-Host "  Path:       $packetPath"
Write-Host "  Bytes:      $packetBytes"
Write-Host "  Lines:      $packetLines"
Write-Host "  SHA-256:    $packetSHA"
Write-Host ""
Write-Host "=== Substrate (125) metadata ==="
Write-Host "  SHA-256:    $substrateSHA125"
Write-Host "  Bytes:      $substrateBytes125"
Write-Host "  Lines:      $substrateLines125"
