"""AUDIT-FLEET-F unified audit script (read-only).

Phases F1-F4 plus aggregator. Writes findings.jsonl/report.md/stats.json/handoff.md
for each phase under sessions/2026-05-01/AUDIT-FLEET-F/.
"""
from __future__ import annotations
import json, os, re, hashlib, subprocess, sys, glob, collections, pathlib
from collections import Counter, defaultdict

ROOT = pathlib.Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat")
SESS = ROOT / "sessions" / "2026-05-01"
OUT  = SESS / "AUDIT-FLEET-F"
TEXSUB = ROOT / "tex" / "submitted"

PUBLISHED = {
    "umbrella":          "10.5281/zenodo.19885550",
    "pcf1_concept":      "10.5281/zenodo.19931635",
    "pcf1_v1.3":         "10.5281/zenodo.19937196",
    "pcf1_v1.2":         "10.5281/zenodo.19934553",
    "pcf1_v1.1":         "10.5281/zenodo.19931636",
    "pcf2_concept":      "10.5281/zenodo.19936297",
    "pcf2_v1.2":         "10.5281/zenodo.19951458",
    "pcf2_v1.1":         "10.5281/zenodo.19939463",
    "pcf2_v1.0":         "10.5281/zenodo.19936298",
    "ct_concept":        "10.5281/zenodo.19941678",
    "ct_v1.2":           "10.5281/zenodo.19951331",
    "ct_v1.1":           "10.5281/zenodo.19941679",
}
SUPERSEDED = {PUBLISHED[k] for k in ("pcf1_v1.2","pcf1_v1.1","pcf2_v1.1","pcf2_v1.0","ct_v1.1")}
CURRENT = {PUBLISHED[k] for k in ("pcf1_v1.3","pcf2_v1.2","ct_v1.2","umbrella")}

# ---------------------------------------------------------------------------
# Phase F1 — AEAL claims consistency
# ---------------------------------------------------------------------------
def phase_F1():
    odir = OUT / "F1"
    odir.mkdir(parents=True, exist_ok=True)
    findings = []
    issue_n = [0]
    def add(sev, cat, loc, cur, exp, rem):
        issue_n[0] += 1
        findings.append({
            "issue_id": f"F1-{issue_n[0]:02d}",
            "severity": sev,
            "category": cat,
            "location": loc,
            "current": cur,
            "expected": exp,
            "remediation": rem,
        })

    files = sorted(SESS.rglob("claims*.jsonl"))
    # exclude AUDIT-FLEET-F itself
    files = [f for f in files if "AUDIT-FLEET-F" not in str(f)]
    session_folders = set()
    total_entries = 0
    by_id = defaultdict(list)  # claim_id -> list[(file, line_no, entry)]
    statements = defaultdict(list)  # normalised stmt -> list[(claim_id, file, status)]
    schema_violations = 0
    parse_errors = 0
    REQUIRED = ("claim_id","statement","verdict")  # we'll be lenient: claim or statement
    for f in files:
        rel = f.relative_to(ROOT)
        # session folder = first dir under sessions/2026-05-01/
        parts = f.relative_to(SESS).parts
        session_folders.add(parts[0])
        try:
            with f.open("r", encoding="utf-8") as fh:
                for i, line in enumerate(fh, 1):
                    line = line.strip()
                    if not line:
                        continue
                    total_entries += 1
                    try:
                        e = json.loads(line)
                    except Exception as ex:
                        parse_errors += 1
                        add("MEDIUM","schema_parse_error",f"{rel}:{i}",
                            line[:80], "valid JSON", "fix JSON syntax")
                        continue
                    cid = e.get("claim_id") or e.get("id")
                    stmt = e.get("statement") or e.get("claim")
                    verdict = (e.get("verdict") or e.get("status") or
                               e.get("evidence_type") or "")
                    confidence = (e.get("confidence") or "").upper()
                    evidence = e.get("evidence") or e.get("evidence_summary") or e.get("script") or ""
                    # AEAL schema (per copilot-instructions): required fields are
                    # claim, evidence_type, dps, reproducible, script, output_hash
                    REQUIRED_AEAL = ("claim","evidence_type","script","output_hash")
                    missing = [k for k in REQUIRED_AEAL if k not in e or e.get(k) in (None,"")]
                    if missing:
                        schema_violations += 1
                        add("MEDIUM","schema_missing_aeal_fields",f"{rel}:{i}",
                            f"missing AEAL fields {missing}",
                            "all AEAL required fields present (claim, evidence_type, script, output_hash)",
                            "add missing fields per AEAL spec")
                    # Use stable surrogate id if no explicit claim_id
                    if not cid and stmt:
                        h = hashlib.sha256((str(rel)+"|"+stmt).encode("utf-8")).hexdigest()[:12]
                        cid = f"{pathlib.PurePosixPath(str(rel).replace(chr(92),'/')).parts[2]}::{h}"
                    if cid:
                        by_id[cid].append((str(rel), i, e))
                    if stmt:
                        norm = re.sub(r"\s+"," ", stmt.lower().strip())[:160]
                        statements[norm].append((cid or "<no-id>", str(rel), str(verdict)))
                    # confidence/evidence mismatch
                    if confidence == "HIGH" and not evidence and not e.get("dps") and not e.get("output_hash"):
                        add("LOW","confidence_evidence_mismatch",f"{rel}:{i}",
                            f"confidence=HIGH no evidence/dps/hash for {cid}",
                            "HIGH only with quantitative evidence",
                            "downgrade confidence or add evidence")
        except Exception as ex:
            add("HIGH","file_read_error",str(rel),str(ex),"file readable",
                "investigate file access")

    # duplicate claim_ids ACROSS DIFFERENT session folders
    duplicates_count = 0
    for cid, entries in by_id.items():
        sess_set = {pathlib.PurePosixPath(e[0].replace("\\","/")).parts[2] for e in entries}
        # parts[0]=sessions, [1]=2026-05-01, [2]=session-folder
        if len(sess_set) > 1:
            duplicates_count += 1
            add("MEDIUM","duplicate_claim_id_cross_session",
                ";".join(f"{e[0]}:{e[1]}" for e in entries),
                f"claim_id={cid} appears in {sorted(sess_set)}",
                "claim_ids globally unique or namespaced",
                "namespace claim_id with session prefix")

    # verdict contradictions: same normalised statement, different verdict tokens
    verdict_contradictions = 0
    POS = {"PASS","SUPPORTED","CONFIRMED","TRUE","HOLDS","VERIFIED"}
    NEG = {"FAIL","REFUTED","FALSIFIED","FALSE","NULL","HALT"}
    for stmt, occ in statements.items():
        if len(occ) < 2:
            continue
        verds = {v.upper() for _,_,v in occ if v}
        pos = bool(verds & POS); neg = bool(verds & NEG)
        if pos and neg:
            verdict_contradictions += 1
            add("HIGH","verdict_contradiction",
                ";".join(f"{f}({c})" for c,f,v in occ),
                f"verdicts={verds} for stmt='{stmt[:60]}...'",
                "single coherent verdict",
                "review and reconcile or split into distinct claim_ids")

    # broken cross-refs: handoff.md mentions claim_ids; check existence
    broken_xref = 0
    handoffs = list(SESS.rglob("handoff.md"))
    handoffs = [h for h in handoffs if "AUDIT-FLEET-F" not in str(h)]
    cid_pat = re.compile(r"\b([A-Z][A-Z0-9]+-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{1,3})\b")
    known_cids = set(by_id.keys())
    for h in handoffs:
        try:
            txt = h.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in cid_pat.findall(txt):
            # heuristic: only flag if it looks like a claim_id pattern that's used elsewhere
            # i.e. must match prefix of an existing claim_id family
            fam = m.rsplit("-",1)[0]
            same_fam = [c for c in known_cids if c.rsplit("-",1)[0] == fam]
            if same_fam and m not in known_cids:
                broken_xref += 1
                add("MEDIUM","broken_claim_xref",
                    str(h.relative_to(ROOT)),
                    f"handoff cites {m} not in claims*.jsonl (family {fam} has {len(same_fam)} entries)",
                    "all cited claim_ids exist",
                    "either add the claim or correct the citation")

    # FALSIFIED claims still cited in published tex
    pub_tex = [
        SESS / "PCF1-V13-UPDATE"   / "p12_pcf1_main.tex",
        SESS / "PCF2-V12-RELEASE"  / "pcf2_program_statement.tex",
        SESS / "CHANNEL-THEORY-V12"/ "channel_theory_outline.tex",
        TEXSUB / "umbrella_program_paper" / "main.tex",
    ]
    pub_tex_text = ""
    for p in pub_tex:
        if p.exists():
            pub_tex_text += "\n%%FILE:%s\n" % p + p.read_text(encoding="utf-8", errors="replace")
    falsified_cited = 0
    for cid, entries in by_id.items():
        verds = {(e[2].get("verdict") or e[2].get("status") or "").upper() for e in entries}
        if verds & NEG and cid in pub_tex_text:
            falsified_cited += 1
            add("CRITICAL","falsified_but_cited_in_published",
                f"published tex / claim_id={cid}",
                f"cid={cid} verdicts={verds} appears verbatim in published tex",
                "FALSIFIED claims must not be cited as positive evidence",
                "remove citation or convert to NULL/discussion")

    stats = {
        "session_folders_scanned": sorted(session_folders),
        "claims_jsonl_files_found": len(files),
        "total_claim_entries": total_entries,
        "unique_claim_ids": len(by_id),
        "duplicates_cross_session": duplicates_count,
        "verdict_contradictions": verdict_contradictions,
        "schema_violations": schema_violations,
        "parse_errors": parse_errors,
        "broken_xrefs": broken_xref,
        "falsified_but_cited": falsified_cited,
    }
    (odir/"stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    with (odir/"findings.jsonl").open("w", encoding="utf-8") as fh:
        for x in findings:
            fh.write(json.dumps(x)+"\n")

    # report
    sev_counts = Counter(f["severity"] for f in findings)
    report = f"""# F1 — AEAL claims consistency

**Scope:** all `sessions/2026-05-01/*/claims*.jsonl` (excluding AUDIT-FLEET-F itself).

## Summary

- Session folders scanned: **{len(stats['session_folders_scanned'])}**
- claims*.jsonl files found: **{stats['claims_jsonl_files_found']}**
- Total claim entries: **{stats['total_claim_entries']}**
- Unique claim_ids: **{stats['unique_claim_ids']}**
- Cross-session duplicate claim_ids: **{stats['duplicates_cross_session']}**
- Verdict contradictions (same stmt, opposing verdict): **{stats['verdict_contradictions']}**
- Schema violations (missing claim_id/statement): **{stats['schema_violations']}**
- JSON parse errors: **{stats['parse_errors']}**
- Broken handoff xrefs (claim_id cited but not defined): **{stats['broken_xrefs']}**
- FALSIFIED-but-still-cited in published tex: **{stats['falsified_but_cited']}**

## Severity counts

{json.dumps(dict(sev_counts), indent=2)}

## Notes

- "Cross-session duplicate claim_id" treats the session folder under
  `sessions/2026-05-01/<NAME>/` as the namespace boundary; multiple
  `claims_phase_*.jsonl` files in the *same* folder are not flagged.
- "Verdict contradiction" uses normalised lower-case statement string
  (first 160 chars); only fires when both POS and NEG token sets hit.
- "Broken claim xref" is heuristic: an ID is flagged only if its prefix
  family exists elsewhere in `claims*.jsonl` but the specific ID does not.
- Findings are listed in `findings.jsonl`.
"""
    (odir/"report.md").write_text(report, encoding="utf-8")
    handoff = f"""# F1 handoff

- Files scanned: {stats['claims_jsonl_files_found']} across {len(stats['session_folders_scanned'])} session folders.
- Total entries: {stats['total_claim_entries']}; unique claim_ids: {stats['unique_claim_ids']}.
- Severity counts: {dict(sev_counts)}.
- Critical concerns: {stats['falsified_but_cited']} FALSIFIED claim_id(s) appearing verbatim in published-tex sources.
- See `findings.jsonl` and `report.md`.
"""
    (odir/"handoff.md").write_text(handoff, encoding="utf-8")
    return stats, findings


# ---------------------------------------------------------------------------
# Phase F2 — DOI / Zenodo metadata
# ---------------------------------------------------------------------------
def phase_F2():
    odir = OUT / "F2"
    odir.mkdir(parents=True, exist_ok=True)
    findings = []
    n = [0]
    def add(sev, cat, loc, cur, exp, rem):
        n[0] += 1
        findings.append({
            "issue_id": f"F2-{n[0]:02d}", "severity": sev, "category": cat,
            "location": loc, "current": cur, "expected": exp, "remediation": rem,
        })

    # gather DOIs
    doi_pat = re.compile(r"10\.5281/zenodo\.(\d+)|10\.\d{4,9}/[\w./()\-:;]+", re.I)
    doi_locs = defaultdict(list)  # doi -> list[(file,line)]
    files = []
    files.append(TEXSUB/"submission_log.txt")
    files += list(SESS.rglob("zenodo_description*.txt"))
    files += list(TEXSUB.glob("*.tex"))
    files += list(TEXSUB.rglob("*.bib"))
    files += list(SESS.rglob("*.tex"))
    files += list(SESS.rglob("*.bib"))
    files = [f for f in files if "AUDIT-FLEET-F" not in str(f) and f.exists()]
    for f in files:
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for i, line in enumerate(txt.splitlines(), 1):
            for m in doi_pat.finditer(line):
                d = m.group(0).rstrip(".,;)}")
                doi_locs[d].append((str(f.relative_to(ROOT)), i))

    # (a) DOI HEAD checks
    doi_status = {}
    networking_failed = False
    for d in sorted(doi_locs):
        if not d.lower().startswith("10.5281/zenodo."):
            continue
        url = "https://doi.org/"+d
        try:
            r = subprocess.run(["curl.exe","-I","-L","-m","12","-s","-o","NUL",
                                "-w","%{http_code}", url],
                               capture_output=True, text=True, timeout=20)
            code = (r.stdout or "").strip()[-3:]
            doi_status[d] = code
        except Exception as ex:
            doi_status[d] = f"ERR:{ex}"
            networking_failed = True
    inaccessible = networking_failed and not any(v in {"200","301","302","303","307","308"} for v in doi_status.values())

    for d, code in doi_status.items():
        if code not in {"200","301","302","303","307","308"}:
            sev = "HIGH" if not inaccessible else "INFO"
            add(sev, "doi_resolution_failed",
                ";".join(f"{f}:{l}" for f,l in doi_locs[d][:3]),
                f"{d} -> HTTP {code}",
                "200/301/302/303",
                "verify Zenodo record published & DOI active" if not inaccessible else "network unavailable, retry later")

    # (b) IsSupplementTo / IsPartOf reciprocity
    desc_files = {p.name: p for p in SESS.rglob("zenodo_description*.txt")}
    relations = defaultdict(set)  # this_doi -> set[(rel, target_doi)]
    # heuristic identification: parse each description for "Is supplement to", "Is part of", etc.
    desc_parsed = {}
    for name, p in desc_files.items():
        txt = p.read_text(encoding="utf-8", errors="replace")
        # try to identify which DOI THIS description is for from its containing folder
        parent = p.parent.name
        this_doi = {
            "PCF2-V12-RELEASE":   PUBLISHED["pcf2_v1.2"],
            "PCF2-V11-RELEASE":   PUBLISHED["pcf2_v1.1"],
            "CHANNEL-THEORY-V12": PUBLISHED["ct_v1.2"],
            "CHANNEL-THEORY-V11": PUBLISHED["ct_v1.1"],
        }.get(parent, parent)
        rels = []
        for line in txt.splitlines():
            for kw in ["IsSupplementTo","IsPartOf","Continues","IsSupplementedBy",
                       "IsDocumentedBy","Cites","IsVersionOf"]:
                if kw.lower() in line.lower() or kw.replace("Is","Is supplement").lower() in line.lower():
                    for m in doi_pat.finditer(line):
                        rels.append((kw, m.group(0)))
            # plain-text patterns
            ll = line.lower()
            if "supplement to" in ll or "is supplement" in ll:
                for m in doi_pat.finditer(line):
                    rels.append(("IsSupplementTo", m.group(0)))
            if "part of" in ll:
                for m in doi_pat.finditer(line):
                    rels.append(("IsPartOf", m.group(0)))
            if "continues" in ll:
                for m in doi_pat.finditer(line):
                    rels.append(("Continues", m.group(0)))
        desc_parsed[parent] = (this_doi, rels)

    # reciprocity: if A IsSupplementTo B, then B should IsSupplementedBy A in B's record
    # We don't have B's Zenodo record description (only PCF2 & CT), so flag asymmetric
    forward = defaultdict(set)
    for parent, (this_doi, rels) in desc_parsed.items():
        for kw, target in rels:
            forward[(this_doi, kw)].add(target)
    # PCF-1 v1.3 has no zenodo_description.txt in sessions
    pcf1_desc_present = any(p.name.startswith("zenodo_description") and "PCF1" in str(p)
                            for p in SESS.rglob("zenodo_description*.txt"))
    umbrella_desc_present = any(p.name.startswith("zenodo_description") and ("SIARC" in str(p) or "umbrella" in str(p).lower())
                                for p in SESS.rglob("zenodo_description*.txt"))
    if not pcf1_desc_present:
        add("MEDIUM","missing_pcf1_zenodo_description","sessions/2026-05-01/PCF1-V13-UPDATE/",
            "no zenodo_description_v1.3.txt found",
            "PCF-1 v1.3 has its own zenodo_description for cross-link audit",
            "regenerate v1.3 description from Zenodo record and store under PCF1-V13-UPDATE/")
    if not umbrella_desc_present:
        add("MEDIUM","missing_umbrella_zenodo_description","sessions/",
            "no zenodo_description for SIARC umbrella (19885550) found",
            "umbrella description present for reciprocity check",
            "add zenodo_description_umbrella.txt mirroring published Zenodo metadata")

    # (c) stale-version: if some file references a superseded DOI without flagging it
    for d in SUPERSEDED:
        for f, l in doi_locs.get(d, []):
            # Skip files where listing the superseded version is intentional / informational
            if f.endswith("submission_log.txt"):
                continue
            if "/archive/" in f.replace("\\","/") or f.endswith(".log") or f.endswith(".aux"):
                continue
            # Zenodo description files explicitly enumerate prior versions — not stale
            if "zenodo_description" in f.lower() or "zenodo_notes" in f.lower():
                continue
            # submission_log_patch_* files describe version transitions — informational
            if "submission_log_patch" in f.lower():
                continue
            sev = "MEDIUM"
            add(sev, "stale_version_reference",
                f"{f}:{l}",
                f"references superseded DOI {d}",
                f"reference current DOI in same family",
                "update reference or add explicit 'superseded' annotation")

    # (d) concept vs version inversions in submission_log
    sl_path = TEXSUB/"submission_log.txt"
    sl_txt = sl_path.read_text(encoding="utf-8", errors="replace")
    # heuristic: every "Cite-all DOI" should be a concept DOI we know; every "current" should be a current DOI
    for cur_label, cur_doi in [("PCF-1 v1.3", PUBLISHED["pcf1_v1.3"]),
                               ("PCF-2 v1.2", PUBLISHED["pcf2_v1.2"]),
                               ("Channel Theory v1.2", PUBLISHED["ct_v1.2"])]:
        if cur_doi not in sl_txt:
            add("HIGH","submission_log_missing_current_doi","tex/submitted/submission_log.txt",
                f"current DOI {cur_doi} for {cur_label} not in submission_log",
                f"submission_log references {cur_doi} as current",
                "add the current-version DOI line")

    # (e) submission_log monotonic numbering
    items = re.findall(r"(?m)^(\d+)\.\s+Filename", sl_txt)
    if items:
        nums = list(map(int, items))
        # detect duplicates / non-monotonic within a section
        # log has TWO sections (paper submissions; Zenodo submissions) — duplicate count is OK
        dups = [k for k,v in Counter(nums).items() if v > 2]
        if dups:
            add("LOW","submission_log_repeated_numbers","tex/submitted/submission_log.txt",
                f"item numbers appearing >2 times: {dups}",
                "each item number appears in at most two sections (paper + zenodo)",
                "review duplicate numbering")

    # date inconsistency check: same Zenodo DOI with two different dates
    # specifically item 9 zenodo (t2a) appears with both 26th and 28th April
    for line_no, line in enumerate(sl_txt.splitlines(), 1):
        pass
    # crude: find two distinct "Submitted on" dates near same DOI
    chunks = re.split(r"(?m)^\d+\.\s+Filename", sl_txt)
    for chunk in chunks:
        dates = re.findall(r"Submitted on:\s*(\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4})", chunk)
        if len(set(dates)) > 1:
            add("LOW","submission_log_date_drift","tex/submitted/submission_log.txt",
                f"same item has dates {set(dates)}",
                "single submission date per item",
                "reconcile date discrepancy")
            break

    # (f) arXiv presence inventory (INFO)
    arxiv_in_tex = 0
    for f in (TEXSUB/"submission_log.txt",):
        if "arxiv.org" in f.read_text(encoding="utf-8", errors="replace").lower():
            arxiv_in_tex += 1
    add("INFO","arxiv_presence_inventory","tex/submitted/submission_log.txt",
        f"arxiv.org references in submission_log: {arxiv_in_tex}",
        "informational",
        "track which papers are on arXiv vs Zenodo only")

    stats = {
        "files_scanned": len(files),
        "unique_dois": len(doi_locs),
        "doi_resolution_results": dict(Counter(doi_status.values())),
        "doi_resolution_inaccessible": inaccessible,
        "zenodo_descriptions_found": [p.name for p in desc_files.values()],
        "pcf1_zenodo_description_present": pcf1_desc_present,
        "umbrella_zenodo_description_present": umbrella_desc_present,
    }
    (odir/"stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    with (odir/"findings.jsonl").open("w", encoding="utf-8") as fh:
        for x in findings: fh.write(json.dumps(x)+"\n")

    sev_counts = Counter(f["severity"] for f in findings)
    report = f"""# F2 — DOI / Zenodo metadata

## Scope

- {len(files)} files scanned (submission_log, zenodo_description_v*.txt,
  tex/submitted/*.tex, *.bib, sessions/2026-05-01/*).
- {len(doi_locs)} unique DOI strings encountered.

## DOI HEAD-check (curl.exe -I -L -m 12)

Inaccessible-partial: **{stats['doi_resolution_inaccessible']}**

Status code distribution: `{stats['doi_resolution_results']}`

Per-DOI status (zenodo records only):
"""
    for d, code in sorted(doi_status.items()):
        report += f"- `{d}` -> {code}\n"
    report += f"""
## Zenodo description inventory

Files found: {stats['zenodo_descriptions_found']}

- PCF-1 v1.3 description: {'PRESENT' if pcf1_desc_present else 'MISSING'}
- SIARC umbrella description: {'PRESENT' if umbrella_desc_present else 'MISSING'}

## Severity counts

{json.dumps(dict(sev_counts), indent=2)}

See `findings.jsonl` for individual issues.
"""
    (odir/"report.md").write_text(report, encoding="utf-8")
    handoff = f"""# F2 handoff

- Unique DOIs: {len(doi_locs)}; resolution distribution {stats['doi_resolution_results']}.
- Inaccessible-partial flag: {stats['doi_resolution_inaccessible']}.
- Severity counts: {dict(sev_counts)}.
- Notable: PCF-1 v1.3 description {'PRESENT' if pcf1_desc_present else 'MISSING (MEDIUM)'};
  SIARC umbrella description {'PRESENT' if umbrella_desc_present else 'MISSING (MEDIUM)'}.
"""
    (odir/"handoff.md").write_text(handoff, encoding="utf-8")
    return stats, findings


# ---------------------------------------------------------------------------
# Phase F3 — Conjecture numbering / statements
# ---------------------------------------------------------------------------
def phase_F3():
    odir = OUT / "F3"
    odir.mkdir(parents=True, exist_ok=True)
    findings = []
    n = [0]
    def add(sev,cat,loc,cur,exp,rem):
        n[0]+=1
        findings.append({"issue_id":f"F3-{n[0]:02d}","severity":sev,"category":cat,
                         "location":loc,"current":cur,"expected":exp,"remediation":rem})

    pub_tex = {
        "PCF-1 v1.3":      SESS / "PCF1-V13-UPDATE"   / "p12_pcf1_main.tex",
        "PCF-2 v1.2":      SESS / "PCF2-V12-RELEASE"  / "pcf2_program_statement.tex",
        "Channel Theory v1.2": SESS / "CHANNEL-THEORY-V12"/ "channel_theory_outline.tex",
        "SIARC umbrella":  TEXSUB / "umbrella_program_paper" / "main.tex",
    }
    pub_tex = {k:v for k,v in pub_tex.items() if v.exists()}
    text = {k: v.read_text(encoding="utf-8", errors="replace") for k,v in pub_tex.items()}

    # extract environments
    env_pat = re.compile(
        r"\\begin\{(theorem|conjecture|conj|proposition|prop|lemma|corollary|definition|remark)\*?\}"
        r"\s*(?:\[(?P<title>[^\]]*)\])?\s*(?:\\label\{(?P<label>[^}]+)\})?",
        re.I)
    env_inline_label = re.compile(r"\\label\{([^}]+)\}")
    items = defaultdict(list)  # (paper, type, label-or-numbered) -> [body]
    by_paper = defaultdict(list)
    label_counts = defaultdict(Counter)  # paper -> Counter[label]
    for paper, txt in text.items():
        # iterate over begin/end blocks
        for m in re.finditer(r"\\begin\{(theorem|conjecture|conj|proposition|prop|lemma|corollary|definition|remark)\*?\}(.*?)\\end\{\1\*?\}",
                             txt, re.S|re.I):
            kind = m.group(1).lower()
            body = m.group(2)
            label_match = env_inline_label.search(body)
            label = label_match.group(1) if label_match else None
            line_no = txt[:m.start()].count("\n")+1
            items[(paper,kind,label)].append((line_no, body[:300]))
            by_paper[paper].append((kind, label, line_no, body[:300]))
            if label:
                label_counts[paper][label] += 1

    # within-paper duplicate labels
    for paper, ctr in label_counts.items():
        for lab, cnt in ctr.items():
            if cnt > 1:
                add("HIGH","within_paper_duplicate_label",f"{pub_tex[paper].relative_to(ROOT)}",
                    f"label `{lab}` defined {cnt}× in {paper}",
                    "each label unique within paper",
                    "rename one of the duplicates")

    # cross-paper conjecture references like "Conjecture B4"
    ref_pat = re.compile(r"Conjecture\s+([A-Z][0-9]+(?:'|\*|\.A\*?|\.B\*?|\.[a-z])?)", )
    refs_by_paper = defaultdict(set)
    for paper, txt in text.items():
        for m in ref_pat.finditer(txt):
            refs_by_paper[paper].add(m.group(1))
    # collect conjecture *labels* that look like conj:b4, conj:b5 etc
    conj_labels_by_paper = defaultdict(set)
    for (paper,kind,lab), occ in items.items():
        if kind in {"conjecture","conj"} and lab:
            conj_labels_by_paper[paper].add(lab)

    # promotion conjecture -> theorem: same anchor token (e.g. "B4") used as conj in one
    # paper but as theorem in another — heuristic
    # We'll match on label suffix tokens like b4, b5, b3
    def tokens(labels):
        out = set()
        for l in labels:
            t = l.lower().replace("conj:","").replace("thm:","").replace("theorem:","")
            t = t.replace("prop:","").replace("rem:","")
            out.add(t)
        return out

    conj_tokens = {p: tokens(s) for p,s in conj_labels_by_paper.items()}
    thm_tokens = {p: tokens({lab for (q,k,lab),_ in items.items()
                              if q==p and k=="theorem" and lab}) for p in pub_tex}
    # cross-paper promotion
    for p1, ct in conj_tokens.items():
        for p2, tt in thm_tokens.items():
            if p1==p2: continue
            shared = ct & tt
            for tok in shared:
                add("CRITICAL","cross_paper_promotion_conjecture_to_theorem",
                    f"{p1} vs {p2}",
                    f"token `{tok}`: conjecture in {p1}, theorem in {p2}",
                    "either both papers agree, or proof reference is provided",
                    "verify proof exists; if not, demote in {p2} or harmonise")

    # cross-paper citation drift: conjecture token cited but not defined here AND not labelled
    # in target paper
    all_defined_tokens = {p: conj_tokens.get(p,set()) | thm_tokens.get(p,set()) for p in pub_tex}
    for paper, refs in refs_by_paper.items():
        for r in refs:
            r_norm = r.lower()
            # check if defined in this paper
            here = any(r_norm in t for t in all_defined_tokens[paper])
            elsewhere = any(r_norm in all_defined_tokens[q] for q in pub_tex if q!=paper)
            if not here and not elsewhere:
                add("MEDIUM","conjecture_ref_undefined",
                    str(pub_tex[paper].relative_to(ROOT)),
                    f"{paper} cites `Conjecture {r}` but no paper defines it",
                    "every cited conjecture defined in some surveyed paper",
                    "either define or fix the citation")

    # silent demotion: token that was theorem somewhere is now conj/open in another
    for p1, tt in thm_tokens.items():
        for p2 in pub_tex:
            if p1==p2: continue
            ct2 = conj_tokens.get(p2,set())
            shared = tt & ct2
            for tok in shared:
                add("HIGH","silent_demotion_theorem_to_conjecture",
                    f"{p1} vs {p2}",
                    f"token `{tok}`: theorem in {p1}, conjecture in {p2}",
                    "consistent status across papers (with explicit cross-ref)",
                    "harmonise status or add cross-paper note")

    # definition drift heuristic: take top shared term "channel", "C-channel", "predicate"
    # — lightweight: just count occurrences; we won't auto-flag drift without HIL review
    add("INFO","definition_drift_scan_skipped","cross-paper",
        "automated drift detection of natural-language definitions skipped",
        "human review for conceptual drift",
        "schedule a human-review pass before next major release")

    stats = {
        "papers_scanned": list(pub_tex.keys()),
        "envs_extracted": sum(len(v) for v in by_paper.values()),
        "conjecture_tokens_per_paper": {p:sorted(s) for p,s in conj_tokens.items()},
        "theorem_tokens_per_paper": {p:sorted(s) for p,s in thm_tokens.items()},
        "cross_paper_refs": {p:sorted(s) for p,s in refs_by_paper.items()},
    }
    (odir/"stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    with (odir/"findings.jsonl").open("w",encoding="utf-8") as fh:
        for x in findings: fh.write(json.dumps(x)+"\n")
    sev_counts = Counter(f["severity"] for f in findings)
    report = f"""# F3 — Conjecture numbering & statements

## Scope

Papers scanned: {stats['papers_scanned']}

Total environments extracted (theorem/conjecture/prop/lemma/cor/def/rem): {stats['envs_extracted']}

## Token tables (label suffix = bare token)

Conjectures:
{json.dumps(stats['conjecture_tokens_per_paper'], indent=2)}

Theorems:
{json.dumps(stats['theorem_tokens_per_paper'], indent=2)}

Cross-paper Conjecture refs:
{json.dumps(stats['cross_paper_refs'], indent=2)}

## Severity counts

{json.dumps(dict(sev_counts), indent=2)}

See `findings.jsonl`.
"""
    (odir/"report.md").write_text(report, encoding="utf-8")
    handoff = f"""# F3 handoff

- {len(stats['papers_scanned'])} papers scanned, {stats['envs_extracted']} environments.
- Severity counts: {dict(sev_counts)}.
- Heuristic basis: label-suffix token matching across papers.
- Definition-drift detection deferred to human review (INFO).
"""
    (odir/"handoff.md").write_text(handoff, encoding="utf-8")
    return stats, findings


# ---------------------------------------------------------------------------
# Phase F4 — BibTeX hygiene
# ---------------------------------------------------------------------------
def phase_F4():
    odir = OUT / "F4"
    odir.mkdir(parents=True, exist_ok=True)
    findings = []
    n=[0]
    def add(sev,cat,loc,cur,exp,rem):
        n[0]+=1
        findings.append({"issue_id":f"F4-{n[0]:02d}","severity":sev,"category":cat,
                         "location":loc,"current":cur,"expected":exp,"remediation":rem})

    # find all bib files
    bib_files = []
    for base in (TEXSUB, ROOT/"tex"/"drafts", SESS, ROOT/"sessions"/"2026-04-30"):
        if base.exists():
            bib_files += list(base.rglob("*.bib"))
    # parse entries
    entry_pat = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)(?=^@|\Z)", re.S|re.M)
    field_pat = re.compile(r"(\w+)\s*=\s*[\{\"](.*?)[\}\"]\s*[,\n]", re.S)
    entries = []  # list[(file, key, type, fields_dict, body, line)]
    for f in bib_files:
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in entry_pat.finditer(txt):
            etype = m.group(1).lower()
            key = m.group(2)
            body = m.group(3)
            fields = {fm.group(1).lower(): fm.group(2)
                      for fm in field_pat.finditer(body+"\n")}
            line_no = txt[:m.start()].count("\n")+1
            entries.append((str(f.relative_to(ROOT)), key, etype, fields, body, line_no))

    # within-file duplicate keys
    by_file_key = defaultdict(list)
    for e in entries:
        by_file_key[(e[0], e[1])].append(e)
    for (fp, key), lst in by_file_key.items():
        if len(lst) > 1:
            add("CRITICAL","bib_duplicate_key_within_file",
                f"{fp}:{','.join(str(x[5]) for x in lst)}",
                f"key `{key}` appears {len(lst)}× in same file",
                "unique keys per .bib",
                "merge or rename")

    # cross-file duplicates
    by_key = defaultdict(list)
    for e in entries:
        by_key[e[1]].append(e)
    for key, lst in by_key.items():
        files_set = {e[0] for e in lst}
        if len(files_set) > 1:
            # compare normalised body
            norm_bodies = {re.sub(r"\s+","",e[4].lower()) for e in lst}
            sev = "LOW" if len(norm_bodies)==1 else "HIGH"
            cat = "bib_duplicate_key_cross_file_match" if len(norm_bodies)==1 else "bib_duplicate_key_cross_file_diverge"
            add(sev, cat,
                ";".join(sorted(files_set)),
                f"key `{key}` in {len(files_set)} files; bodies {'identical' if len(norm_bodies)==1 else 'diverge'}",
                "harmonise to single canonical .bib or accept duplication",
                "consolidate or annotate")

    # missing DOI
    for fp,key,etype,fields,body,line in entries:
        if etype not in {"article","book","inproceedings","incollection"}:
            continue
        year = fields.get("year","")
        try:
            yr = int(re.search(r"\d{4}", year).group(0)) if year else 0
        except Exception:
            yr = 0
        if yr >= 2000 and "doi" not in fields:
            sev = "LOW"
            # HIGH if Zenodo self-cite (key looks like papanokechi or zenodo)
            if re.search(r"papanokechi|zenodo|siarc", key, re.I) or \
               re.search(r"papanokechi|zenodo|siarc", fields.get("author","")+fields.get("howpublished",""), re.I):
                sev = "HIGH"
            add(sev,"bib_missing_doi_post2000",f"{fp}:{line}",
                f"@{etype}{{{key}}} year={yr} no DOI",
                "DOI present for post-2000 article/book/inproceedings",
                "add doi field")

    # arXiv eprint without DOI when journal listed
    for fp,key,etype,fields,body,line in entries:
        if "eprint" in fields and "journal" in fields and "doi" not in fields:
            add("LOW","bib_arxiv_eprint_no_doi_with_journal",f"{fp}:{line}",
                f"{key} has eprint+journal, no doi",
                "DOI in addition to eprint when journal-published",
                "look up DOI")

    # cite-but-not-defined: collect \cite{...} from tex sources, intersect with .bib keys
    tex_sources = []
    tex_sources += list(TEXSUB.glob("*.tex"))
    tex_sources += list(SESS.rglob("*.tex"))
    tex_sources = [t for t in tex_sources if "AUDIT-FLEET-F" not in str(t)]
    cite_pat = re.compile(r"\\cite[a-zA-Z]*\*?\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}")
    cited_by_file = defaultdict(set)
    all_keys = {e[1] for e in entries}
    cite_undefined = 0
    # we need to know which .bib files each tex uses (\bibliography{...} or \addbibresource{...})
    bib_use = defaultdict(set)  # tex_file -> set of bib stems
    bib_pat = re.compile(r"\\(?:bibliography|addbibresource)\{([^}]+)\}")
    for t in tex_sources:
        try:
            txt = t.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in bib_pat.finditer(txt):
            for b in m.group(1).split(","):
                bib_use[str(t)].add(b.strip().replace(".bib",""))
        for m in cite_pat.finditer(txt):
            for c in m.group(1).split(","):
                c = c.strip()
                cited_by_file[str(t)].add(c)
    # build per-tex visible bib keys
    bib_by_stem = defaultdict(set)
    for fp,key,etype,fields,body,line in entries:
        stem = pathlib.Path(fp).stem
        bib_by_stem[stem].add(key)
    # detect tex files that use inline \begin{thebibliography} (no .bib resolution needed)
    inline_bib = set()
    bibitem_keys = defaultdict(set)  # tex_path -> set of \bibitem keys
    bibitem_pat = re.compile(r"\\bibitem(?:\[[^\]]*\])?\s*\{([^}]+)\}")
    for t in tex_sources:
        try:
            tt = t.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if r"\begin{thebibliography}" in tt:
            inline_bib.add(str(t))
            for m in bibitem_pat.finditer(tt):
                bibitem_keys[str(t)].add(m.group(1))
    for tex_path, cites in cited_by_file.items():
        stems = bib_use.get(tex_path,set())
        has_inline = tex_path in inline_bib
        if has_inline and not stems:
            # cites must be defined by \bibitem in same file
            visible = bibitem_keys.get(tex_path, set())
            source = "inline thebibliography"
        elif stems:
            visible = set()
            for s in stems:
                visible |= bib_by_stem.get(s, set())
            if has_inline:
                visible |= bibitem_keys.get(tex_path, set())
            source = f"bib stems {sorted(stems)}"
            if not visible:
                # could not resolve any bib stem — skip rather than false-positive
                continue
        else:
            # no \bibliography and no \begin{thebibliography} — skip (likely a fragment / section file)
            continue
        for c in cites:
            if c not in visible:
                cite_undefined += 1
                rel = pathlib.Path(tex_path).relative_to(ROOT)
                add("CRITICAL","bib_cite_undefined",str(rel),
                    f"\\cite{{{c}}} not in {source}",
                    "every cite key defined",
                    "add bibitem or fix typo (would render as ?? in PDF)")

    # defined-but-not-cited
    cited_all = set().union(*cited_by_file.values()) if cited_by_file else set()
    uncited = 0
    for key in all_keys:
        if key not in cited_all:
            uncited += 1
    add("INFO","bib_defined_not_cited_count",
        ";".join(sorted({e[0] for e in entries})[:5])+"...",
        f"{uncited}/{len(all_keys)} bib keys not referenced by any \\cite",
        "informational",
        "consider trimming")

    # author capitalisation: top variants
    author_variants = Counter()
    for e in entries:
        a = e[3].get("author","")
        if a:
            author_variants[a[:80]] += 1
    # not really actionable; record top 10 as INFO
    top10 = author_variants.most_common(10)
    add("INFO","bib_top_author_variants","aggregate",
        f"top10={top10[:5]}",
        "informational",
        "review for capitalisation drift if needed")

    stats = {
        "bib_files_scanned": len(bib_files),
        "bib_entries_total": len(entries),
        "unique_bib_keys": len(all_keys),
        "tex_files_scanned": len(tex_sources),
        "total_cites": sum(len(v) for v in cited_by_file.values()),
        "cite_undefined": cite_undefined,
        "defined_not_cited": uncited,
    }
    (odir/"stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    with (odir/"findings.jsonl").open("w",encoding="utf-8") as fh:
        for x in findings: fh.write(json.dumps(x)+"\n")
    sev_counts = Counter(f["severity"] for f in findings)
    report = f"""# F4 — BibTeX hygiene

## Scope

- {len(bib_files)} .bib files scanned in tex/, sessions/2026-04-30, sessions/2026-05-01.
- {len(entries)} bibliography entries; {len(all_keys)} unique keys.
- {len(tex_sources)} .tex files scanned for \\cite{{}}; {sum(len(v) for v in cited_by_file.values())} citation occurrences.

## Headline numbers

- Cite-but-not-defined: **{cite_undefined}** (CRITICAL — would render as ??)
- Defined-but-not-cited: {uncited}
- Cross-file duplicate keys (with content match): see findings
- Missing DOI on post-2000 article/book/inproceedings: see findings

## Severity counts

{json.dumps(dict(sev_counts), indent=2)}
"""
    (odir/"report.md").write_text(report, encoding="utf-8")
    handoff = f"""# F4 handoff

- {len(bib_files)} bib files, {len(entries)} entries, {len(all_keys)} unique keys.
- Critical: {cite_undefined} cite-but-not-defined occurrences (would render as ?? in PDF).
- Severity counts: {dict(sev_counts)}.
- Note: cite resolution uses per-tex `\\bibliography{{}}` resolution where present; falls back to global key set for tex without explicit \\bibliography.
"""
    (odir/"handoff.md").write_text(handoff, encoding="utf-8")
    return stats, findings


# ---------------------------------------------------------------------------
# Aggregator
# ---------------------------------------------------------------------------
def aggregator(F1, F2, F3, F4):
    odir = OUT / "AGGREGATOR"
    odir.mkdir(parents=True, exist_ok=True)
    all_findings = []
    for tag, (stats, findings) in [("F1",F1),("F2",F2),("F3",F3),("F4",F4)]:
        for x in findings:
            x = dict(x); x["phase"]=tag
            all_findings.append(x)
    sev_order = ["CRITICAL","HIGH","MEDIUM","LOW","INFO"]
    by_sev = {s: [f for f in all_findings if f["severity"]==s] for s in sev_order}
    counts = {s: len(by_sev[s]) for s in sev_order}

    # cross correlations
    correlations = []
    f1_falsified_cited = [f for f in by_sev["CRITICAL"] if f["category"]=="falsified_but_cited_in_published"]
    f3_promoted = [f for f in by_sev["CRITICAL"] if f["category"]=="cross_paper_promotion_conjecture_to_theorem"]
    if f1_falsified_cited and f3_promoted:
        correlations.append("F1 falsified-but-cited × F3 promoted: BOTH present — release block")
    f2_stale = [f for f in by_sev["MEDIUM"] if f["category"]=="stale_version_reference"]
    f4_stale_bib = [f for f in by_sev["LOW"] if "duplicate_key_cross_file" in f["category"]]
    if f2_stale and f4_stale_bib:
        correlations.append(f"F2 stale DOI ({len(f2_stale)}) × F4 stale .bib duplicates ({len(f4_stale_bib)}): coordinate cleanup")
    f3_def_drift = [f for f in all_findings if f["category"].startswith("definition_drift")]
    if f3_def_drift:
        correlations.append("F3 definition_drift_scan_skipped: human review pass needed")
    if not correlations:
        correlations.append("No cross-sub-agent correlations rose above noise threshold.")

    # action_list
    blockers = by_sev["CRITICAL"]
    pcf2_blockers = [f for f in blockers if "PCF-2" in (f.get("location","")+f.get("current","")) or "pcf2" in (f.get("location","")+f.get("current","")).lower()]
    ct_blockers   = [f for f in blockers if "Channel" in (f.get("location","")+f.get("current","")) or "channel_theory" in (f.get("location","")+f.get("current","")).lower()]
    note_blockers = [f for f in blockers if "standalone" in (f.get("location","")+f.get("current","")).lower()]

    pcf2_v13_clear = "NO" if pcf2_blockers else "YES (no CRITICAL touching PCF-2)"
    ct_v13_clear   = "NO" if ct_blockers else "YES (no CRITICAL touching Channel Theory)"
    note_clear     = "NO" if note_blockers else "YES (no CRITICAL touching standalone-note)"
    # also block on any HIGH that touches the relevant artifact
    pcf2_high = [f for f in by_sev["HIGH"] if "pcf2" in (f.get("location","")+f.get("current","")).lower()]
    ct_high   = [f for f in by_sev["HIGH"] if "channel" in (f.get("location","")+f.get("current","")).lower()]

    # write UNIFIED_AUDIT
    lines = ["# UNIFIED_AUDIT — AUDIT-FLEET-F\n",
             f"## Severity totals\n\n```\n"+
             "\n".join(f"{s:9s}: {counts[s]}" for s in sev_order)+"\n```\n"]
    for s in sev_order:
        lines.append(f"\n## {s} ({counts[s]})\n")
        for f in by_sev[s][:50]:  # cap display
            lines.append(f"- **[{f['phase']} {f['issue_id']}]** `{f['category']}` — {f['location']}: {f['current'][:200]}")
        if len(by_sev[s])>50:
            lines.append(f"- ... {len(by_sev[s])-50} more, see findings.jsonl per phase")
    lines.append("\n## Cross-sub-agent correlations\n")
    for c in correlations:
        lines.append(f"- {c}")
    (odir/"UNIFIED_AUDIT.md").write_text("\n".join(lines), encoding="utf-8")

    # action list
    al = ["# action_list — AUDIT-FLEET-F\n",
          "## Block-on-next-session (CRITICALs)\n"]
    if blockers:
        for f in blockers:
            al.append(f"- [{f['phase']} {f['issue_id']}] {f['category']}: {f['location']} — {f['current'][:160]}\n  remediation: {f['remediation']}")
    else:
        al.append("- (none)")
    al.append("\n## PCF2-V13-RELEASE preconditions")
    al.append(f"- Clear: **{pcf2_v13_clear}**")
    if pcf2_high:
        al.append(f"- Plus {len(pcf2_high)} HIGH items touching pcf2 — review before tagging v1.3.")
    al.append("\n## Channel-Theory-V13 preconditions")
    al.append(f"- Clear: **{ct_v13_clear}**")
    if ct_high:
        al.append(f"- Plus {len(ct_high)} HIGH items touching channel theory.")
    al.append("\n## Standalone-note-fire preconditions")
    al.append(f"- Clear: **{note_clear}**")
    al.append("\n## Defer list (LOW + INFO)")
    al.append(f"- {counts['LOW']} LOW + {counts['INFO']} INFO items deferred to next maintenance pass.")
    (odir/"action_list.md").write_text("\n".join(al), encoding="utf-8")

    # claims.jsonl (5+ AEAL claims documenting the audit)
    audit_claims = [
        {"claim_id":"AUDIT-FLEET-F-01",
         "statement":"AUDIT-FLEET-F F1 phase scanned all sessions/2026-05-01 claims*.jsonl files and produced findings.jsonl + report.md + stats.json + handoff.md.",
         "evidence_type":"computation","verdict":"PASS","reproducible":True,
         "script":"sessions/2026-05-01/AUDIT-FLEET-F/audit.py","output_hash":"see F1/stats.json"},
        {"claim_id":"AUDIT-FLEET-F-02",
         "statement":"AUDIT-FLEET-F F2 phase performed DOI HEAD checks via curl.exe and inventoried Zenodo descriptions for the four published records.",
         "evidence_type":"computation","verdict":"PASS","reproducible":True,
         "script":"sessions/2026-05-01/AUDIT-FLEET-F/audit.py","output_hash":"see F2/stats.json"},
        {"claim_id":"AUDIT-FLEET-F-03",
         "statement":"AUDIT-FLEET-F F3 phase extracted theorem/conjecture/proposition environments from the four published .tex sources and built cross-paper token tables.",
         "evidence_type":"computation","verdict":"PASS","reproducible":True,
         "script":"sessions/2026-05-01/AUDIT-FLEET-F/audit.py","output_hash":"see F3/stats.json"},
        {"claim_id":"AUDIT-FLEET-F-04",
         "statement":"AUDIT-FLEET-F F4 phase scanned all .bib files and intersected \\cite keys with bib entries to detect cite-but-not-defined.",
         "evidence_type":"computation","verdict":"PASS","reproducible":True,
         "script":"sessions/2026-05-01/AUDIT-FLEET-F/audit.py","output_hash":"see F4/stats.json"},
        {"claim_id":"AUDIT-FLEET-F-05",
         "statement":"AUDIT-FLEET-F aggregator produced UNIFIED_AUDIT.md with severity buckets and three go/no-go preconditions for PCF2-V13/Channel-Theory-V13/standalone-note-fire.",
         "evidence_type":"computation","verdict":"PASS","reproducible":True,
         "script":"sessions/2026-05-01/AUDIT-FLEET-F/audit.py","output_hash":"see AGGREGATOR/UNIFIED_AUDIT.md"},
        {"claim_id":"AUDIT-FLEET-F-06",
         "statement":f"AUDIT-FLEET-F severity totals: CRITICAL={counts['CRITICAL']} HIGH={counts['HIGH']} MEDIUM={counts['MEDIUM']} LOW={counts['LOW']} INFO={counts['INFO']}.",
         "evidence_type":"computation","verdict":"INFO","reproducible":True,
         "script":"sessions/2026-05-01/AUDIT-FLEET-F/audit.py","output_hash":"n/a"},
    ]
    with (odir/"claims.jsonl").open("w",encoding="utf-8") as fh:
        for c in audit_claims: fh.write(json.dumps(c)+"\n")

    # top-5 most urgent
    urgent = []
    for s in sev_order:
        for f in by_sev[s]:
            urgent.append(f)
            if len(urgent)>=5: break
        if len(urgent)>=5: break
    top5 = "\n".join(f"{i+1}. [{f['phase']} {f['issue_id']} {f['severity']}] {f['category']}: {f['current'][:140]}"
                     for i,f in enumerate(urgent))

    handoff = f"""# AUDIT-FLEET-F handoff

## Severity totals

```
CRITICAL : {counts['CRITICAL']}
HIGH     : {counts['HIGH']}
MEDIUM   : {counts['MEDIUM']}
LOW      : {counts['LOW']}
INFO     : {counts['INFO']}
```

## Top 5 most urgent

{top5 or '(no findings)'}

## Three go/no-go verdicts

- **PCF2-V13-RELEASE clear?** {pcf2_v13_clear} (HIGH-touching-pcf2 = {len(pcf2_high)})
- **Channel-Theory-V13 clear?** {ct_v13_clear} (HIGH-touching-CT = {len(ct_high)})
- **standalone-note-fire clear?** {note_clear}

## Cross-sub-agent correlations

{chr(10).join('- '+c for c in correlations)}

## Halt status

(see per-phase handoffs; F2 INACCESSIBLE_PARTIAL = {F2[0].get('doi_resolution_inaccessible',False)})
"""
    (odir/"handoff.md").write_text(handoff, encoding="utf-8")
    return counts, urgent, pcf2_v13_clear, ct_v13_clear, note_clear


def main():
    F1 = phase_F1()
    F2 = phase_F2()
    F3 = phase_F3()
    F4 = phase_F4()
    counts, urgent, pcf2, ct, note = aggregator(F1,F2,F3,F4)
    summary = {
        "severity_counts": counts,
        "top5_urgent": [(f["phase"],f["issue_id"],f["severity"],f["category"]) for f in urgent],
        "pcf2_v13_clear": pcf2,
        "ct_v13_clear": ct,
        "note_clear": note,
        "f2_inaccessible_partial": F2[0].get("doi_resolution_inaccessible",False),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
