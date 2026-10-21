#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verify_notice_rev2.py -- checker for NOTICE-v1.7.md at revision 2.

Revision 2 of the notice fills the v1.4/v1.5/v1.6 erratum rows from the
deposited descriptions fetched into refs/, so the rev-1 check that *declared*
those versions unreadable is retired and replaced by checks that they are now
SOURCED.

Three layers, in order:

  SECTION 0 -- READER INTEGRITY.  Before any check evaluates a known-ABSENT
      feature, the reader asserts a set of known-PRESENT features.  This closes
      the defect found at rev 1: a check reported "no fenced block containing
      the basis was found" -- verbally identical to the real defect -- because
      main() read CRLF bytes and matched '```\\n'.  Mutant controls cannot catch
      that, since a broken reader rejects the mutant too, for the same wrong
      reason.  Mutant testing verifies a check's LOGIC, not its INPUT PATH.

  SECTION 1 -- checks against the notice as written.

  SECTION 2 -- can-fail controls: every check is re-run against a mutant of the
      notice with the thing it guards removed.  A check that passes on its own
      mutant is reported BROKEN and the run fails.

  SECTION 3 -- READER CONTROLS: the file is re-read through two deliberately
      defective readers, and the SECTION 0 assertion must fire on each.  This
      is the control for SECTION 0, and it is the one control class that mutant
      testing structurally cannot provide.

Reads from disk only.  Writes nothing.
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)              # CT-S26-CTV17-DRAFT
ROOT2609 = os.path.dirname(SESSION)          # sessions/2026-09-17
REPO = os.path.dirname(os.path.dirname(ROOT2609))
NOTICE = os.path.join(SESSION, "NOTICE-v1.7.md")
REFS = os.path.join(SESSION, "refs")

failures = []
broken = []


def report(name, ok, detail=""):
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    if not ok:
        failures.append(name)


# --------------------------------------------------------- SECTION 0 machinery
class ReadError(Exception):
    pass


def assert_read(text):
    """A check that reads a file must also verify that it READ it.

    Each sentinel is a feature known to be PRESENT in the notice and known to be
    destroyed by a specific reader defect.  If any is missing, the text in hand
    is not the notice, and every downstream absence-report would be unsound.
    """
    if "\r" in text:
        raise ReadError("CR present: line endings were not normalised")
    if not text.startswith("# Channel Theory for Polynomial Continued Fractions"):
        raise ReadError("title line absent: wrong file or wrong decoding")
    if text.count("```\n") < 4:
        raise ReadError("fewer than 4 fence-plus-newline markers: fenced blocks "
                        "are unreachable by the block regex")
    for ch, why in ((u"\u03be\u2080", "xi_0"), (u"\u03b2", "beta"),
                    (u"\u0393", "Gamma"), (u"\u2264", "less-or-equal")):
        if ch not in text:
            raise ReadError("sentinel character %s (%s) absent: decoding is wrong"
                            % (repr(ch), why))
    return True


def read_notice():
    raw = open(NOTICE, "rb").read()
    text = raw.decode("utf-8").replace("\r\n", "\n")
    assert_read(text)
    return raw, text


# ------------------------------------------------------ held deposited sources
def _held_sources():
    """Every deposited text held on disk, as one dict path -> text."""
    out = {}
    v13 = os.path.normpath(os.path.join(ROOT2609, "..", "2026-05-02",
                                        "CHANNEL-THEORY-V13-RELEASE",
                                        "zenodo_description_v1.3.txt"))
    if os.path.exists(v13):
        out[v13] = open(v13, encoding="utf-8").read()
    if os.path.isdir(REFS):
        for fn in sorted(os.listdir(REFS)):
            if fn.endswith(".txt") or fn.endswith(".json"):
                fp = os.path.join(REFS, fn)
                out[fp] = open(fp, encoding="utf-8").read()
    return out


# ---------------------------------------------------------------- checks
def check_concept_doi(text):
    """Every Zenodo DOI the notice prints must occur in a held source."""
    held = _held_sources()
    if not held:
        return False, "no held deposited source found"
    blob = "\n".join(held.values())
    concept = "10.5281/zenodo.19941678"
    if concept not in blob:
        return False, "concept DOI absent from every held source"
    if concept not in text:
        return False, "concept DOI absent from the notice"
    printed = set(re.findall(r"10\.5281/zenodo\.\d+", text))
    untraced = sorted(d for d in printed if d not in blob)
    if untraced:
        return False, "DOIs printed but not in any held source: " + ", ".join(untraced)
    return True, "%d DOIs printed, all traced to %d held sources" % (len(printed), len(held))


def check_version_map_sourced(text):
    """The v1.3-v1.6 rows must carry the DOI and date the live records report."""
    rec = {}
    for fn, ver in (("zenodo_22782807.json", "1.6"), ("zenodo_22717792.json", "1.5")):
        fp = os.path.join(REFS, fn)
        if not os.path.exists(fp):
            return False, "missing held record %s" % fn
        d = json.load(open(fp, encoding="utf-8"))
        got = (d.get("metadata", {}) or {}).get("version")
        if got != ver:
            return False, "%s reports version %r, expected %r" % (fn, got, ver)
        rec[ver] = d
    want = [("v1.3", "10.5281/zenodo.19972394", "2026-05-02"),
            ("v1.4", "10.5281/zenodo.20585624", "2026-06-07"),
            ("v1.5", "10.5281/zenodo.22717792", "2026-09-12"),
            ("v1.6", "10.5281/zenodo.22782807", "2026-09-16")]
    for ver, doi, date in want:
        row = [l for l in text.split("\n") if l.startswith("| " + ver + " ")]
        if not row:
            return False, "no stack row for %s" % ver
        line = row[0]
        if doi not in line:
            return False, "%s row does not carry %s" % (ver, doi)
        if date not in line:
            return False, "%s row does not carry its publication date %s" % (ver, date)
    if "**unknown**" in text:
        return False, "a version row is still marked unknown"
    return True, "four rows carry DOI + date; v1.5/v1.6 versions confirmed in-record"


def check_v17_numbering_justified(text):
    """v1.7 must be justified by the concept record's CURRENT version, not assumed."""
    fp = os.path.join(REFS, "datacite_concept.json")
    if not os.path.exists(fp):
        return False, "concept record not held"
    d = json.load(open(fp, encoding="utf-8"))
    attrs = d.get("data", {}).get("attributes", d.get("attributes", {}))
    cur = attrs.get("version")
    if cur != "1.6":
        return False, "concept record reports current version %r, not '1.6'" % cur
    if "v1.7 is the correct next version number" not in text:
        return False, "the notice does not justify its own version number"
    hv = [r for r in attrs.get("relatedIdentifiers", [])
          if r.get("relationType") == "HasVersion"]
    if len(hv) != 6:
        return False, "concept record lists %d HasVersion relations, expected 6" % len(hv)
    return True, "concept record at version 1.6, 6 HasVersion relations, numbering justified"


def check_obligation_tags_are_real(text):
    """Every op:/rem: tag the notice names must occur in a held deposited text."""
    held = _held_sources()
    blob = "\n".join(held.values())
    tags = set(re.findall(r"`((?:op|rem):[A-Za-z0-9\-]+)`", text))
    if not tags:
        return False, "the notice names no obligation tag at all"
    invented = sorted(t for t in tags if t not in blob)
    if invented:
        return False, "tags not found in any held deposited text: " + ", ".join(invented)
    return True, "%d obligation tags, every one present in the deposited record" % len(tags)


def check_pdfs_not_obtained_declared(text):
    """The unfetched PDFs, and the consequence, must be declared."""
    for fp in ("ct_v_22782807.pdf", "ct_v_22717792.pdf",
               "channel_theory_outline.pdf"):
        if os.path.exists(os.path.join(REFS, fp)):
            return False, "a PDF is now held (%s) but the notice still says otherwise" % fp
    if "504" not in text:
        return False, "the HTTP 504 failure is not recorded"
    if "have not been\n> read" not in text and "has not been read" not in text \
       and "not been\n> read" not in text:
        return False, "the consequence (falsifier text unread) is not stated"
    if "does not restate\n> the falsifier" not in text and \
       "does not restate the falsifier" not in text:
        return False, "the notice does not say it declines to restate the falsifier"
    return True, "PDFs absent, 504 recorded, falsifier text explicitly not restated"


def check_painleve_target_corrected(text):
    """The stale P-III(D6) target must be corrected AND marked conjectural."""
    if "P-III(D\u2086)" not in text:
        return False, "the stale target is not named at all"
    if "D\u2085^(1)" not in text:
        return False, "the corrected Sakai surface is not named"
    if "Painlev\u00e9 V" not in text:
        return False, "the corrected Painleve type is not named"
    if "conjectural" not in text:
        return False, "the corrected identification is not marked conjectural"
    if "10.5281/zenodo.20455089" not in text:
        return False, "the companion paper grounding the conjecture is not cited"
    for m in re.finditer(r"P-III\(D\u2086\)", text):
        seg = text[max(0, m.start() - 400):m.start() + 400]
        if not re.search(r"stale|corrected|superse|must not be copied|repeating",
                         seg, re.I):
            return False, "P-III(D6) appears at offset %d without a staleness marker" % m.start()
    return True, "stale target flagged everywhere; P_V/D5 named and marked conjectural"


def check_ebr_supersession_scoped(text):
    """Retiring the EBR grounding must state EBR's scope, not just displace it."""
    if "10.5281/zenodo.20564079" not in text:
        return False, "the EBR preprint is not cited by DOI"
    i = text.find("supersedes, for this purpose, the EBR")
    if i < 0:
        return False, "the supersession sentence is missing"
    seg = text[i:i + 1200]
    for frag in ("positivity", "physical", "no positivity hypothesis"):
        if frag not in seg:
            return False, "supersession does not state EBR's scope (%s)" % frag
    if "not withdrawn" not in seg:
        return False, "the notice does not say the EBR argument itself stands"
    return True, "EBR scope stated; supersession is of the grounding, not the result"


def check_vacuity_generalises_not_replaces(text):
    """rem:d3-vacuous must be generalised with its own evidence quoted."""
    if "rem:d3-vacuous" not in text:
        return False, "rem:d3-vacuous is not named"
    i = text.find("de-empiricises `rem:d3-vacuous`")
    if i < 0:
        return False, "the generalisation sentence is missing"
    seg = text[i:i + 1800]
    if "6.85" not in seg or "1.26" not in seg:
        return False, "v1.6's own sweep numbers are not quoted"
    if "S_{\u03b6*}" not in seg or "not settled here" not in seg:
        return False, "the notice does not decline to settle the S_zeta* pre-check"
    return True, "sweep quoted, generalisation stated, S_zeta* pre-check left open"


def check_paths(text):
    pats = re.findall(r"`([A-Za-z0-9_.\-/]+/[A-Za-z0-9_.\-/]+\.(?:md|tex|py|pdf|png|txt|json|jsonl))`",
                      text)
    missing = []
    checked = 0
    for p in sorted(set(pats)):
        cand = [os.path.join(ROOT2609, p), os.path.join(REPO, p),
                os.path.join(SESSION, p)]
        checked += 1
        if not any(os.path.exists(c) for c in cand):
            missing.append(p)
    if missing:
        return False, "missing: " + ", ".join(missing)
    return True, "%d distinct cited paths all exist" % checked


def _corpus_claims():
    claims = {}
    for dirpath, _dirs, files in os.walk(ROOT2609):
        if "claims.jsonl" in files:
            fp = os.path.join(dirpath, "claims.jsonl")
            for line in open(fp, encoding="utf-8"):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                cid = rec.get("claim_id")
                if cid:
                    claims[cid] = rec
    return claims


def check_claim_ids(text):
    claims = _corpus_claims()
    cited = set(re.findall(r"`(S\d+[A-Z]?-\d+)`", text))
    unknown = sorted(c for c in cited if c not in claims)
    if unknown:
        return False, "unresolved ids: " + ", ".join(unknown)
    return True, "%d cited ids, all resolve (corpus has %d)" % (len(cited), len(claims))


def check_labels(text):
    claims = _corpus_claims()
    expect = {
        "S1-03": "PROVEN", "S1-04": "PROVEN", "S1-05": "STRUCTURAL",
        "S3B-04": "STRUCTURAL", "S3B-05": "VERIFIED", "S21-76": "INSPECTED",
        "S22-21": "PROVEN", "S22-22": "VERIFIED", "S26-01": "PROVEN",
    }
    bad = []
    for cid, lab in expect.items():
        if cid not in claims:
            bad.append("%s absent" % cid)
        elif claims[cid].get("label") != lab:
            bad.append("%s is %s not %s" % (cid, claims[cid].get("label"), lab))
    if bad:
        return False, "; ".join(bad)
    return True, "%d load-bearing labels agree with the corpus" % len(expect)


def check_k_never_proven(text):
    if "VERIFIED, never PROVEN" not in text:
        return False, "the 'VERIFIED, never PROVEN' statement for K is missing"
    for m in re.finditer(r"PROVEN", text):
        window = text[max(0, m.start() - 160):m.start()]
        if re.search(r"\bK\b\s*(is|=)[^.]{0,40}$", window):
            return False, "K appears to be labelled PROVEN near offset %d" % m.start()
    return True, "K carries VERIFIED and is never labelled PROVEN"


def check_pslq_basis_in_full(text):
    blocks = re.findall(r"```\n(.*?)```", text, re.S)
    if not blocks:
        return False, "READER: no fenced block found at all -- refusing to report absence"
    cand = [b for b in blocks if "log C" in b and "PSLQ" not in b]
    if not cand:
        return False, "no fenced block containing the basis was found"
    b = max(cand, key=len)
    need = ["log C", "log 2", "log 3", "log \u03c0", "log \u0393(1/3)",
            "10^6", "|m| \u2264 12", "dps 120", "D_trust = 100",
            "0.40 \u00b7 D_trust = 40"]
    miss = [n for n in need if n not in b]
    if miss:
        return False, "basis block missing: " + ", ".join(miss)
    for bad in ("\u2026", "...", "etc."):
        if bad in b:
            return False, "basis block contains an ellipsis (%r)" % bad
    if "\u0393(1/6)" in b:
        return False, "basis block still contains Gamma(1/6), the degenerate element"
    return True, "6-vector printed in full, no ellipsis, Gamma(1/6) removed"


def check_naming_prohibition(text):
    if "naming prohibition" not in text.lower():
        return False, "no naming-prohibition heading"
    seg = text[text.lower().index("naming prohibition"):][:1400]
    if "amplitude at" not in seg or "Stokes constant at" not in seg:
        return False, "the two roles are not both stated"
    if "2/\u221a3" not in seg or "4/\u221a3" not in seg:
        return False, "the two points are not both given numerically"
    if "never be used for the other" not in seg.lower() and \
       "may ever be used for the other" not in seg.lower():
        return False, "the prohibition itself is not stated"
    return True, "K at xi_0, S_zeta* at 2 xi_0, prohibition stated"


def check_wongli_not_obtained(text):
    if "NOT OBTAINED" not in text:
        return False, "'NOT OBTAINED' does not appear"
    for frag in ("Second-Order Linear Difference Equations, II",
                 "10.1002/sapm1992874289", "289\u2013324", "403"):
        if frag not in text:
            return False, "citation fragment missing: %s" % frag
    if "1992b" not in text or "65\u201394" not in text:
        return False, "the 1992a/1992b suffix trap is not disambiguated"
    return True, "full citation, HTTP 403, and the suffix trap all present"


def check_no_formal_verification_claim(text):
    if "seven `sorry`s" not in text and "seven `sorry`" not in text:
        return False, "the seven sorries are not stated"
    if "does not claim formal verification" not in text:
        return False, "the denial of formal verification is missing"
    for m in re.finditer(r"machine-checked", text):
        window = text[max(0, m.start() - 60):m.start()]
        if not re.search(r"(no|not|nothing|never)\b[^.]*$", window, re.I):
            return False, "'machine-checked' used without negation at offset %d" % m.start()
    return True, "seven sorries stated; every 'machine-checked' is negated"


def check_ibrahim_salvy_weak_form(text):
    if "do not know how to compute" not in text:
        return False, "the weaker printed form is not quoted"
    for m in re.finditer(r"is not computable", text):
        window = text[max(0, m.start() - 120):m.start()]
        if "not**" not in window:
            return False, "'is not computable' used without the not-that framing"
    return True, "weaker printed form quoted; stronger form only as the excluded reading"


def check_odlyzko_split(text):
    if "Wimp and Zeilberger" not in text:
        return False, "Wimp and Zeilberger are not named"
    if "second is his own" not in text:
        return False, "the split is not stated"
    if "may not be rigorous" not in text:
        return False, "the B-T rigour objection from the same page is missing"
    if "Nothing rests on B\u2013T" not in text:
        return False, "the pre-emption ('nothing rests on B-T') is missing"
    return True, "split stated, B-T objection quoted, pre-emption present"


def check_scope_of_negative(text):
    if "This excludes that space" not in text:
        return False, "the scope sentence is missing"
    if "not** evidence that" not in text and "not evidence that" not in text:
        return False, "the 'not evidence that C has no closed form' clause is missing"
    if "1.5051" not in text:
        return False, "the positive control's cost is not reported"
    if "8.1273367954950723671" not in text:
        return False, "C is not printed"
    return True, "scope, control cost 1.5051, and C all present"


def check_zeta_is_action_difference(text):
    if "not a change of variable" not in text:
        return False, "the 'not a change of variable' statement is missing"
    if "action difference" not in text:
        return False, "'action difference' is not stated"
    if "g2_pade_borel.py" not in text:
        return False, "the decisive source is not cited"
    return True, "action difference, negation, and source all present"


def check_repo_absence_correction(text):
    """The rev-1 'zero occurrences' finding must be corrected, not quietly dropped."""
    if "op:xi0-singularity-type" not in text:
        return False, "the tag is still not cited"
    i = text.find("zero occurrences")
    if i < 0:
        return False, "the earlier finding is not restated in order to be corrected"
    seg = text[max(0, i - 400):i + 900]
    # Blockquote-and-whitespace normalisation: this passage is inside a '> '
    # block, so line breaks insert '\n> ' mid-phrase.  Recorded in REPORT.md
    # section 4 as a post-hoc loosening, with a third mutant added in the same
    # edit to show the check can still fail.
    flat = re.sub(r"\s+", " ", seg.replace("\n>", " "))
    if not re.search(r"true\W{0,4}of the repository", flat):
        return False, "the scope of the earlier finding is not corrected"
    if "false of the corpus" not in flat:
        return False, "the notice does not say the finding was false of the corpus"
    if "absence from the repo" not in flat:
        return False, "the general lesson is not stated"
    return True, "rev-1 finding corrected in place, with its scope named"


CHECKS = [
    ("all printed DOIs trace to a held source", check_concept_doi),
    ("version map rows carry DOI + date from the records", check_version_map_sourced),
    ("v1.7 numbering justified by the concept record", check_v17_numbering_justified),
    ("every op:/rem: tag exists in the deposited record", check_obligation_tags_are_real),
    ("unfetched PDFs and their consequence declared", check_pdfs_not_obtained_declared),
    ("Painleve target corrected and marked conjectural", check_painleve_target_corrected),
    ("EBR supersession states EBR's scope", check_ebr_supersession_scoped),
    ("vacuity generalises rem:d3-vacuous with its numbers", check_vacuity_generalises_not_replaces),
    ("rev-1 repo-absence finding corrected", check_repo_absence_correction),
    ("all cited paths exist", check_paths),
    ("all cited claim ids resolve", check_claim_ids),
    ("load-bearing labels match the corpus", check_labels),
    ("K is VERIFIED and never PROVEN", check_k_never_proven),
    ("PSLQ basis printed in full", check_pslq_basis_in_full),
    ("naming prohibition present", check_naming_prohibition),
    ("Wong-Li II stated NOT OBTAINED", check_wongli_not_obtained),
    ("no formal-verification claim", check_no_formal_verification_claim),
    ("Ibrahim-Salvy in the weaker form", check_ibrahim_salvy_weak_form),
    ("Odlyzko attribution split survives", check_odlyzko_split),
    ("the 5B negative is scoped", check_scope_of_negative),
    ("zeta* is an action difference", check_zeta_is_action_difference),
]

MUTANTS = {
    "all printed DOIs trace to a held source":
        lambda t: t.replace("10.5281/zenodo.19941678", "10.5281/zenodo.99999999"),
    "version map rows carry DOI + date from the records": [
        lambda t: t.replace("| v1.4 | `10.5281/zenodo.20585624` | 2026-06-07 |",
                            "| v1.4 | **unknown** | **unknown** |"),
        lambda t: t.replace("| v1.6 | `10.5281/zenodo.22782807` | 2026-09-16 |",
                            "| v1.6 | `10.5281/zenodo.22782807` | 2026-09-99 |"),
    ],
    "v1.7 numbering justified by the concept record":
        lambda t: t.replace("v1.7 is the correct next version number",
                            "v1.7 follows v1.6"),
    "every op:/rem: tag exists in the deposited record":
        lambda t: t.replace("`op:xi0-singularity-type`", "`op:xi0-type-of-singularity`"),
    "unfetched PDFs and their consequence declared":
        lambda t: t.replace("504", "200"),
    "Painleve target corrected and marked conjectural":
        lambda t: t.replace("D\u2085^(1)", "D\u2086^(1)"),
    "EBR supersession states EBR's scope":
        lambda t: t.replace("not withdrawn", "withdrawn"),
    "vacuity generalises rem:d3-vacuous with its numbers":
        lambda t: t.replace("6.85 \u00d7 10\u207b\u00b9\u2078", "a negligible amount"),
    "rev-1 repo-absence finding corrected": [
        lambda t: t.replace("zero occurrences", "no mention"),
        lambda t: t.replace("true **of the repository** and false of the corpus",
                            "an oversight"),
        lambda t: t.replace("> from the repo, not absence from the published record.",
                            "> generally."),
    ],
    "all cited paths exist":
        lambda t: t.replace("`CT-S8-LITCHECK/refs/gautschi1967.pdf`",
                            "`CT-S8-LITCHECK/refs/gautschi1967_NOSUCH.pdf`"),
    "all cited claim ids resolve":
        lambda t: t.replace("`S1-03`", "`S1-999`"),
    "load-bearing labels match the corpus": None,   # handled by label_mutant_check
    "K is VERIFIED and never PROVEN":
        lambda t: t.replace("**Label: VERIFIED, never PROVEN.**", "**Label: PROVEN.**"),
    "PSLQ basis printed in full": [
        lambda t: t.replace("m\u00b7log C + a\u00b7log 2 + b\u00b7log 3 + c\u00b7log \u03c0 + d\u00b7log \u0393(1/3) + f = 0",
                            "m\u00b7log C + a\u00b7log 2 + \u2026 + f = 0"),
        lambda t: t.replace("          cost = n_nonzero \u00b7 log10(max|coeff|) \u2264 0.40 \u00b7 D_trust = 40\n", ""),
        lambda t: t.replace("v = [ log C , log 2 , log 3 , log \u03c0 , log \u0393(1/3) , 1 ]",
                            "v = [ log C , log 2 , log 3 , log \u03c0 , log \u0393(1/3) , log \u0393(1/6) , 1 ]"),
    ],
    "naming prohibition present":
        lambda t: t.replace("Neither name may ever be used for the other", "They differ"),
    "Wong-Li II stated NOT OBTAINED":
        lambda t: t.replace("NOT OBTAINED", "consulted"),
    "no formal-verification claim":
        lambda t: t.replace("does not claim formal verification",
                            "reports the formal verification"),
    "Ibrahim-Salvy in the weaker form":
        lambda t: t.replace("do not know how to compute", "cannot in principle compute"),
    "Odlyzko attribution split survives":
        lambda t: t.replace("Wimp and Zeilberger", "Odlyzko"),
    "the 5B negative is scoped":
        lambda t: t.replace("**This excludes that space.**", ""),
    "zeta* is an action difference":
        lambda t: t.replace("not a change of variable", "a change of variable"),
}


def label_mutant_check(text):
    claims = _corpus_claims()
    if claims.get("S22-22", {}).get("label") == "PROVEN":
        return True, "corpus really does say PROVEN"
    return False, "S22-22 is VERIFIED in the corpus, not PROVEN"


# ------------------------------------------------- SECTION 3 reader controls
def reader_binary_no_normalise():
    """The rev-1 defect, reproduced exactly: decode without CRLF normalisation."""
    return open(NOTICE, "rb").read().decode("utf-8")


def reader_wrong_codec():
    """A plausible wrong codec: latin-1 mangles every non-ASCII sentinel."""
    return open(NOTICE, "rb").read().decode("latin-1").replace("\r\n", "\n")


def reader_truncating():
    """A reader that silently returns only the first 2 KB."""
    return open(NOTICE, "rb").read()[:2048].decode("utf-8", "ignore").replace("\r\n", "\n")


READER_CONTROLS = [
    ("binary read, CRLF not normalised (the rev-1 defect)", reader_binary_no_normalise),
    ("wrong codec (latin-1)", reader_wrong_codec),
    ("silently truncated read", reader_truncating),
]


def main():
    if not os.path.exists(NOTICE):
        print("FATAL: %s not found" % NOTICE)
        return 2

    print("=" * 74)
    print("verify_notice_rev2.py -- CT-S26-CTV17-DRAFT")
    print("=" * 74)

    print("SECTION 0 -- READER INTEGRITY")
    print("-" * 74)
    try:
        raw, text = read_notice()
    except ReadError as exc:
        print("  [FAIL] reader integrity -- %s" % exc)
        print("VERDICT: FAIL")
        return 1
    digest = hashlib.sha256(raw).hexdigest()
    print("  [PASS] reader integrity -- title, 4+ fence markers, 4 unicode "
          "sentinels, no CR")
    print("notice : %s" % os.path.relpath(NOTICE, REPO).replace("\\", "/"))
    print("sha256 : %s" % digest)
    print("bytes  : %d" % len(raw))
    print()

    print("SECTION 1 -- CHECKS AGAINST THE NOTICE AS WRITTEN")
    print("-" * 74)
    for name, fn in CHECKS:
        try:
            ok, detail = fn(text)
        except Exception as exc:
            ok, detail = False, "check raised %s: %s" % (type(exc).__name__, exc)
        report(name, ok, detail)

    print()
    print("SECTION 2 -- CAN-FAIL CONTROLS (each check run against its own mutant)")
    print("-" * 74)
    for name, fn in CHECKS:
        if name == "load-bearing labels match the corpus":
            ok, _d = label_mutant_check(text)
            fired = not ok
            print("  [%s] %s -- mutant %s" % ("PASS" if fired else "BROKEN", name,
                                              "rejected" if fired else "ACCEPTED"))
            if not fired:
                broken.append(name)
            continue
        muts = MUTANTS[name]
        if not isinstance(muts, list):
            muts = [muts]
        fired = True
        for i, mf in enumerate(muts):
            mut = mf(text)
            if mut == text:
                print("  [BROKEN] %s -- mutant %d is identical to the original"
                      % (name, i + 1))
                fired = False
                continue
            try:
                ok, _d = fn(mut)
            except Exception:
                ok = False
            if ok:
                print("  [BROKEN] %s -- mutant %d ACCEPTED" % (name, i + 1))
                fired = False
        if fired:
            print("  [PASS] %s -- %d mutant(s) rejected" % (name, len(muts)))
        else:
            broken.append(name)

    print()
    print("SECTION 3 -- READER CONTROLS (mutate the INPUT PATH, not the text)")
    print("-" * 74)
    print("  Each defective reader must be caught by SECTION 0.  Mutant testing")
    print("  cannot supply this: a broken reader rejects the mutant too, for the")
    print("  same wrong reason, so the can-fail control fires and the check looks")
    print("  healthy while reporting a false absence.")
    reader_fail = 0
    for name, rf in READER_CONTROLS:
        try:
            bad = rf()
            assert_read(bad)
            print("  [BROKEN] %s -- NOT caught by assert_read" % name)
            reader_fail += 1
        except ReadError as exc:
            print("  [PASS] %s -- caught: %s" % (name, exc))
        except Exception as exc:
            print("  [PASS] %s -- caught by decoding: %s" % (name, type(exc).__name__))

    print()
    print("=" * 74)
    print("checks run          : %d" % len(CHECKS))
    print("checks failed       : %d%s" % (len(failures),
                                          ("  -> " + ", ".join(failures)) if failures else ""))
    print("controls fired      : %d of %d" % (len(CHECKS) - len(broken), len(CHECKS)))
    print("broken checks       : %d%s" % (len(broken),
                                          ("  -> " + ", ".join(broken)) if broken else ""))
    print("reader controls     : %d of %d caught" % (len(READER_CONTROLS) - reader_fail,
                                                     len(READER_CONTROLS)))
    verdict = "OK" if (not failures and not broken and not reader_fail) else "FAIL"
    print("VERDICT: %s" % verdict)
    print("=" * 74)
    return 0 if verdict == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
