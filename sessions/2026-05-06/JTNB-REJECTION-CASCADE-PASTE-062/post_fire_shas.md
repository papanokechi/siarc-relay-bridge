# Post-fire SHA anchors — 062 JTNB-REJECTION-CASCADE-PASTE
# Captured: 2026-05-06 (W20), after STEP 1-5 pastes
# Bridge HEAD at deposit: dee3c01 (bridge HEAD pre-commit; will advance on session push)

## tex/submitted/CMB.txt (post-fire)
SHA-256:        0ED6291A25B3D3075C16F6436C897EE8CB1BEBB5257036732C8527B377F4DB66
Size (bytes):   91061   (delta from pre-fire: +1815)
Line count:     1999    (delta from pre-fire: +29)
Last 12 bytes:  3D 3D 3D 3D 3D 3D 3D 3D 3D 3D 3D 3D   (preserved no-trailing-newline invariant)

LC delta breakdown:
  PASTE 1 (L24 portfolio row flip):       +0
  PASTE 2 (VENUE STATUS rewrite):         +10  (spec stated +9; off-by-one in spec)
  PASTE 3 (Await verdicts amendment):     +1
  PASTE 4 (VERDICTS RECEIVED splice):     +18
  ----------------------------------------------
  Total:                                  +29  (spec stated +28; HALT_062_POST_LC triggered)

## tex/submitted/submission_log.txt (post-fire)
SHA-256:        D04B10E37BDD8874027130127D2A9DCBE5B097CF24BBE694809DEF06AC5E0530
Size (bytes):   60442   (delta from pre-fire: +415)
Line count:     1071    (unchanged; in-place inline expansion of L171 + L167 + L170)

## Post-fire CMB.txt token-count grep (STEP 6)
JTNB-2400:                    6   (was 5; +1 from PASTE 4 entry; PASTE 3 net 0; PASTE 1+2 keep)
REJECTED 2026-05-06:          2   (was 0; +1 PASTE 1 + +1 PASTE 3; PASTE 2 uses '6 May 2026', PASTE 4 uses 'REJECTED by Journal')
                                  (spec STEP 6 said =3; spec invariant projection error D3)
Await verdicts on:            1   (unchanged)
CLOSED: JTNB-2400:            1   (PASTE 3)
REJECTED by Journal de:       1   (PASTE 4)
REJECTED by JTNB 6 May:       1   (PASTE 2)
VERDICTS RECEIVED (header):   1   (## VERDICTS RECEIVED at L762; same line offset; intra-section anchor stable)

## Post-fire submission_log.txt token-count grep (STEP 6)
Verdict: <bare>:                          5   (was 6; -1 Item 22 filled in)
Verdict: Rejected (6 May 2026:            1   (NEW; Item 22)
Status: REJECTED by Journal:              1   (NEW; Item 22)
JTNB-2400:                                1   (unchanged; Item 22 Submission ID line preserved)

## Halt invariants summary
HALT_062_CMB_DRIFT:           PASS (P2 anchor matched)
HALT_062_SL_DRIFT:            PASS (P3 anchor matched)
HALT_062_PRE_FLIGHT:          PASS (STEP 0 invariants all clear)
HALT_062_HEAD_MOVED:          PASS (bridge HEAD dee3c01 stable)
HALT_062_POST_LC:             FAIL (LC = 1999, expected 1998; spec PASTE-2 +9 arithmetic was actually +10)
HALT_062_DOUBLE_SPLICE:       PASS (each NEW_STR exactly once)
HALT_062_GROUNDING_PARTIAL:   PASS (J2 corrected '101 lines' -> '133 lines' = file-system-grounded; no speculation)

## Disposition
HALT_062_POST_LC documented in halt_log.json with relay-059 precedent.
Content placement verified correct per disk inspection.
Session committed to bridge with HALT logged in handoff.md Anomalies.
