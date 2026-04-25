# SIARC Obligations — Bridge Conventions

This document records cross-session conventions and obligations that
Copilot (execution) and Claude (strategy) both rely on. Append-only.

## claims.jsonl — Session Type Convention
_Added: 2026-04-25 (TRIAGE-UNSOLVED-3 follow-up)_

### Rule: No empty claims.jsonl
Every session MUST produce at least one claims.jsonl entry.
An empty file is a malformed session — indistinguishable from a
crash or Searcher's Fatigue abort. If a session genuinely produces
zero claims, write one entry of class `near_miss` explaining why.

### session_type field

| value | meaning |
|---|---|
| _(omitted)_ | computational session (default) |
| `literature_only` | all claims from published literature |
| `null_result` | sweep returned no positive hits |
| `mixed` | computational + literature in same session |

### source field by session type

**Computational:** name of script or tool
```jsonl
{"id":"C001","evidence_class":"numerical_identity",
 "source":"bsd_ratio.py","reproduce":"python bsd_ratio.py --curve 37"}
```

**Literature-only:** Author_YEAR or doi:10.xxx/yyy;
`reproduce` uses `cite:` prefix (signals: consult reference, don't re-run)
```jsonl
{"id":"L001","evidence_class":"independently_verified",
 "source":"Kolyvagin_1989","session_type":"literature_only",
 "reproduce":"cite:doi:10.1007/BF01231195"}
```

**Null result:** sweep script name; artifact points to halt_log.json
```jsonl
{"id":"N001","evidence_class":"numerical_identity",
 "source":"cycle_search.py","session_type":"null_result",
 "artifact":"halt_log.json",
 "reproduce":"python cycle_search.py --max-length 90"}
```

### Escalation rule
`near_miss` → `numerical_identity` requires independent verification
before the next relay cycle commits to that claim. No silent escalation.
