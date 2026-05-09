#!/usr/bin/env pwsh
# Build dispatch_packet.txt for slot 129 (M8b V0 ratification solo-dispatch)
# Mirrors 122 / 126 structure with M7/M8a -> M8b token substitutions and 128 substrate
# Run from bridge repo root.

$ErrorActionPreference = "Stop"

$folder129 = "sessions/2026-05-09/T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129"
$substratePath128 = "sessions/2026-05-09/T2-EXECUTOR-M8B-RATIFICATION-SUBSTRATE-PREP-128/m8b_v0_ratification_template.md"
$substrateSHA128 = (Get-FileHash -Algorithm SHA256 $substratePath128).Hash
$substrateBytes128 = (Get-Item $substratePath128).Length
$substrateLines128 = (Get-Content $substratePath128).Count

$header = @"
================ CLAUDE.AI T1-SYNTH DISPATCH PACKET — M8B V0 RATIFICATION ================
Task ID: T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129
Drafted: 2026-05-09
Substrate: sessions/2026-05-09/T2-EXECUTOR-M8B-RATIFICATION-SUBSTRATE-PREP-128/m8b_v0_ratification_template.md
Substrate SHA-256: $substrateSHA128
Bridge HEAD at dispatch: beb321b (post-126-landing; 128 substrate landed at f02ab5d)
==========================================================================================

OPERATOR INSTRUCTIONS (do NOT paste this header block; start at "===PASTE FROM HERE==="):
1. Open a fresh Claude.ai conversation tab.
2. Set system / first message tone as a peer-review T1-Synth consultation.
3. Copy everything from the "===PASTE FROM HERE===" line below to the "===END PASTE===" line.
4. Submit. When Claude.ai responds, save the verbatim response to:
     sessions/2026-05-09/T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129/synth_verdict_raw.txt
5. Then run the cascade-absorption fire (130 re-fire) to structure the verdict + close the M8b chain.

==========================================================================================
===PASTE FROM HERE===

You are a T1-Synth peer reviewing a candidate M8b V0 axis-closure ratification request from
the SIARC pipeline.

Scope: SIARC paper-foundation infrastructure axis M8b (Stokes-multiplier scale; numerical
foreclosure of S_2 at d=2 stratum via Borel-Padé acceleration with d>=3 caveat carry-forward
per P-009). Refer ONLY to the substrate provided below. Do NOT speculate beyond it. If the
substrate is insufficient, return verdict label DEFER with explicit reasoning. The substrate
intentionally threads the P-009 d>=3-caveat forward; treat the d>=3 stratum as OUT OF SCOPE
for this V0 ratification (the closure target is d=2 only).

Read carefully — this is a substrate-bounded review. Treat the embedded template as the
sole evidentiary base. You may cite, paraphrase, or quote verbatim; you may NOT introduce
external claims, references, or numerical results not already present in the substrate.

Your task: answer Q1-Q5 from §3 in order. For Q4, emit one of:
  - RATIFY                  (M8b V0 closure is mathematically supported; no amendment needed)
  - RATIFY_WITH_AMENDMENT   (closure supported but requires a specific manuscript-content
                             amendment; specify the amendment in Q5)
  - DEFER                   (substrate insufficient; specify what additional substrate is
                             needed)
  - OBJECT                  (closure NOT mathematically supported; specify objection)

Return verdict in this exact format:

  M8B_V0_VERDICT: <LABEL>
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

================ SUBSTRATE BEGIN (m8b_v0_ratification_template.md) ================
"@

$footer = @"
================ SUBSTRATE END (m8b_v0_ratification_template.md) ================

End of substrate. Now answer Q1-Q5 from §3 of the substrate, emitting the verdict block in
the exact format specified above.

If you find the substrate ambiguous on any point, prefer DEFER with a specific request
for additional substrate over speculation.

If you find a mathematical objection to M8b V0 closure that is not addressed in the
substrate, emit OBJECT with the objection stated as a precise mathematical claim
(not a stylistic concern).

If you find the substrate sufficient and the closure mathematically supported, emit
RATIFY (or RATIFY_WITH_AMENDMENT if a specific manuscript-content amendment is needed
to make the closure stand cleanly). Note: the (NUMERICAL-FORECLOSURE; d>=3-CAVEAT-CARRIED-
FORWARD) annotation pattern in §1 / §4 is intentional per P-009 caveat threading; do not
treat the d>=3 carry-forward as an objection unless it materially undermines the d=2 V0
closure claim.

End of dispatch.

===END PASTE===
==========================================================================================

POST-DISPATCH OPERATOR CHECKLIST:
  [ ] Saved verbatim Claude.ai response to synth_verdict_raw.txt in this folder.
  [ ] Verified verdict label is one of {RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}.
  [ ] Verified §1-§5 reasoning sections are present.
  [ ] Ready to fire 130 cascade-absorption (re-fire post original 130-halt).

If Claude.ai response is missing one of the §1-§5 sections, re-prompt with:
  "Please re-emit your verdict in the exact format specified, including all §1-§5
   reasoning sections."

If Claude.ai emits a verdict label not in the allowed set, re-prompt with:
  "Please re-emit your verdict label as one of {RATIFY, RATIFY_WITH_AMENDMENT,
   DEFER, OBJECT}."

==========================================================================================
END DISPATCH PACKET (T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129)
==========================================================================================
"@

$headerCRLF = $header -replace "`r?`n", "`r`n"
$substrateRaw = (Get-Content $substratePath128 -Raw) -replace "`r?`n", "`r`n"
$footerCRLF = $footer -replace "`r?`n", "`r`n"

$packet = $headerCRLF + "`r`n" + $substrateRaw.TrimEnd() + "`r`n" + "`r`n" + $footerCRLF

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText((Resolve-Path $folder129).Path + "/dispatch_packet.txt", $packet, $utf8NoBom)

$packetPath = "$folder129/dispatch_packet.txt"
$packetBytes = (Get-Item $packetPath).Length
$packetLines = (Get-Content $packetPath).Count
$packetSHA = (Get-FileHash -Algorithm SHA256 $packetPath).Hash

Write-Host "=== Slot 129 dispatch packet built ==="
Write-Host "  Path:       $packetPath"
Write-Host "  Bytes:      $packetBytes"
Write-Host "  Lines:      $packetLines"
Write-Host "  SHA-256:    $packetSHA"
Write-Host ""
Write-Host "=== Substrate (128) metadata ==="
Write-Host "  SHA-256:    $substrateSHA128"
Write-Host "  Bytes:      $substrateBytes128"
Write-Host "  Lines:      $substrateLines128"
