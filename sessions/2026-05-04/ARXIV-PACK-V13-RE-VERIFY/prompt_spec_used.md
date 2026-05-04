# prompt_spec_used.md

This session executed Prompt 030 (TASK ID:
**ARXIV-PACK-V13-RE-VERIFY**) as composed 2026-05-04 ~15:05 JST
by Copilot CLI (Claude Opus 4.7 xhigh).

The full prompt body is preserved in the relay log; key gates +
constraints honoured this session:

- Phase A SHA-triple-check (commit reachability, tex SHA, pdf SHA,
  page count, 027 cross-check)
- Phase B git-archive extract from `58dfa9e` to a fresh working
  directory (no overlay onto bridge working tree)
- Phase C tarball rebuild at `pcf1_v1.3.tar.gz`, single subdir
  prefix matching existing convention
- Phase D manifest.txt + 00README.txt + abstract.txt + hash_match.json
- Phase E handoff + AEAL claims
- Phase F deployment to `arxiv_pack_pcf1_v1.3_REBUILT/` with
  redirect notice in original `arxiv_pack_pcf1_v1.3/`
- §4 halt-condition coverage: PDF SHA drift (not triggered),
  Zenodo hash mismatch (not triggered), page-count !=16 (not
  triggered)
- §5 forbidden-verb hygiene: no overclaim language
- §6 out-of-scope: no .tex modification, no arXiv submission, no
  Zenodo modification, no work on other 4 records
- §7 outcome ladder: targeting UPGRADE_ARXIV_PACK_V13_REBUILT_CLEAN_
  READY_002_REFIRE (one minor caveat: spec Zenodo IDs were wrong;
  real ID is 19937196 -- see unexpected_finds.json)

No changes were made to:
- the canonical source at sessions/2026-05-01/PCF1-V13-UPDATE/
- the existing sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/
  arxiv_pack_pcf1_v1.3/ contents (only added a REDIRECT_TO_REBUILT.txt
  notice file alongside the contaminated 21pp materials)
- the existing RUNBOOK_pcf1.md (per spec)

No web modifications were attempted (Zenodo API GET is read-only,
no auth, public record).
