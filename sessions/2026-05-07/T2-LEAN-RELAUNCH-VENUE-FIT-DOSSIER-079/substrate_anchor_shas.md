# Substrate-Anchor SHAs — T2-LEAN-RELAUNCH-VENUE-FIT-DOSSIER-079

**SHA-inventory fire time:** 2026-05-07 ~15:12 JST (post-restructure
final run).
**Hash algorithm:** SHA-256 (PowerShell `Get-FileHash -Algorithm
SHA256`).
**Bridge HEAD at fire time:** 49f3423 (post-077 LANDED).

This file inventories the SHA-256 hashes of all 12 production
deliverables + 3 self-check deliverables + 4 AEAL quartet
deliverables in this envelope, plus the SHA of the
upstream-substrate input (`tex/submitted/submission_log.txt`) at
fire time.

---

## Production deliverables (12 .md)

| File | SHA-256 | Size (bytes) |
|---|---|---|
| cover_letter_framing_jfr.md | 26F1031286526200024C01C2F1C5E8695747B715CD9EC68766B020A41328DB4D | 3394 |
| cover_letter_framing_lmcs.md | 0967190679670CC7EEEE2CE0BC924322D2373899BE3E930CADF2636559AFD2C5 | 3338 |
| cover_letter_framing_mcs.md | 27BDABB8975524FA25D314BBD98975DF7546B5DCE4C124514904DFF8BE9A0657 | 3256 |
| cover_letter_framing_tcs.md | E33C42290C51DDD68CC99DA48EA13568ADBF5563AAE6542EC440EC0C0CB2B25C | 3384 |
| cross_venue_compatibility.md | 125426F33779AF8D0E18AE6FF3B7D40E7769D2B3C417A0A64D88479C69540AF5 | 5283 |
| submission_log_item26_splice_spec.md | 732ED67856165923BB41BF7BC5224C9E423F4FF8EA01B69DA2DE08A108630749 | 6370 |
| venue_profile_jfr.md | 6CA5314F601958561DD5FF92C813D2FD94F676D2C5680806146F37B5B22F0363 | 5523 |
| venue_profile_lmcs.md | 4E46D6D01059B25555B57220D81B9755975381D74BE19F85B6E964F7BBDCA7F8 | 5317 |
| venue_profile_mcs.md | CAA17EE97CE23A75922A68D178022F5E8EEBC3C1D3F937576DF91798C1764E77 | 5836 |
| venue_profile_tcs.md | 2F83B6BAAF5C1004E70903E81321AEA6F8D46D9400B16283127B03C18A8F6CFA | 6000 |
| venue_scope_fit_matrix.md | 902C3D499D481FB94C4B8B84C5FAA05E433C16BD96FAB78087D80E97A3F560A0 | 8667 |
| w21_lane1_lean_relaunch_decision_packet.md | B4980C0A98C8FFD4098F429B9F15F57C07EB11CA9199E2E9533A23E323D5B112 | 5097 |

## Self-check deliverables (3 .md)

| File | SHA-256 | Size (bytes) |
|---|---|---|
| forbidden_verb_scan.md | 7847C88E4605A6254A04414BF9F83AA7BF7D043DA935BD03121D363524D0E1C1 | 3059 |
| quote_length_scan.md | AE3C9A0D32E8A0111AFEAB77C21918097E6BEA2BB779FDEC8EF62C15F456E5FF | 3761 |
| substrate_anchor_shas.md | (this file; SHA self-referential, omitted) | (this file) |

## AEAL quartet (4 files)

| File | SHA-256 | Size (bytes) |
|---|---|---|
| claims.jsonl | C772F62B4FE50F9094035930988E7D34760B1DB9DB2859029E911C28B2E72FEC | 7104 |
| halt_log.json | 92355CC7D6BEB98282297027E5CB90D1F82D5BC022EC43F26F90F081F764041B | 5923 |
| discrepancy_log.json | 8FEE10FECD36B4A7AC0E2503670C73A9AD74894EFFE050FA6BCE84A023A5768B | 4168 |
| unexpected_finds.json | 1DF5B01DC36A56B1FA039EE1ED2C3439AA2FAA137226341822E4240C06EAFCB7 | 3304 |

## Substrate input (1 file in workspace; not in bridge dir)

| File | SHA-256 | Size (bytes) |
|---|---|---|
| tex/submitted/submission_log.txt | 2A28465AE39BADF5AB245C3114C84E3E1469BF2FA1CDD967AC017FF4C617E45A | 17030 |
| siarc-relay-bridge/sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/tunnell_afm_R2.tex | 91546B54974E25A4CF54A13CA71FA75380F0C5ED3C0EFA421C6CCAC2333D8BB9 | 46708 |

The two substrate inputs are READ-ONLY in this envelope. No edits
to either file occurred during this session.

---

**Note on post-handoff drift:** the AEAL quartet SHAs above (claims
/ halt_log / discrepancy_log / unexpected_finds) were computed
before this file (substrate_anchor_shas.md) and quote_length_scan.md
were written. They will not change during this session unless the
handoff.md write triggers an iteration that further modifies them.
The handoff.md will record any post-handoff drift in its Anomalies
section.

**Reproducibility:** these SHAs may be re-computed at any time via:

```pwsh
cd siarc-relay-bridge/sessions/2026-05-07/T2-LEAN-RELAUNCH-VENUE-FIT-DOSSIER-079
Get-ChildItem *.md, *.json, *.jsonl | Sort-Object Name |
  ForEach-Object {
    $h = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
    Write-Host "$($_.Name)|$h|$($_.Length)"
  }
```
