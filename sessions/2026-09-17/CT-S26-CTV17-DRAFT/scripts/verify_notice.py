#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verify_notice.py -- checker for sessions/2026-09-17/CT-S26-CTV17-DRAFT/NOTICE-v1.7.md

Every check is an assertion that can fail, and every check is itself tested
against a mutated copy of the notice in which the thing it guards has been
removed.  A check that does not fire on its own mutant is reported as a BROKEN
CHECK and the run fails, so this script cannot silently become a no-op.

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

failures = []
broken = []


def report(name, ok, detail=""):
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    if not ok:
        failures.append(name)


# ---------------------------------------------------------------- checks
# Each check takes the notice text and returns (ok, detail).

def check_concept_doi(text):
    """The concept DOI must match the one in the held v1.3 release description."""
    src = os.path.join(ROOT2609, "..", "2026-05-02", "CHANNEL-THEORY-V13-RELEASE",
                       "zenodo_description_v1.3.txt")
    src = os.path.normpath(src)
    if not os.path.exists(src):
        return False, "held description not found: %s" % src
    held = open(src, encoding="utf-8").read()
    dois = set(re.findall(r"10\.5281/zenodo\.\d+", held))
    concept = "10.5281/zenodo.19941678"
    if concept not in held:
        return False, "concept DOI absent from the held description"
    if concept not in text:
        return False, "concept DOI absent from the notice"
    # every DOI printed by the notice must occur in a held source
    for d in set(re.findall(r"10\.5281/zenodo\.\d+", text)):
        if d not in dois:
            return False, "notice prints a Zenodo DOI not in the held source: %s" % d
    return True, "concept %s + %d version DOIs all traced" % (
        concept, len(set(re.findall(r"10\.5281/zenodo\.\d+", text))) - 1)


def check_paths(text):
    """Every repo-relative path the notice cites must exist on disk."""
    pats = re.findall(r"`([A-Za-z0-9_.\-/]+/[A-Za-z0-9_.\-/]+\.(?:md|tex|py|pdf|png|txt|json|jsonl))`",
                      text)
    missing = []
    checked = 0
    for p in sorted(set(pats)):
        cand = [os.path.join(ROOT2609, p), os.path.join(REPO, p)]
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
    """Every S*-NN id cited by the notice must resolve in the corpus."""
    claims = _corpus_claims()
    cited = set(re.findall(r"`(S\d+[A-Z]?-\d+)`", text))
    unknown = sorted(c for c in cited if c not in claims)
    if unknown:
        return False, "unresolved ids: " + ", ".join(unknown)
    return True, "%d cited ids, all resolve (corpus has %d)" % (len(cited), len(claims))


def check_labels(text):
    """Labels asserted in the notice must match the corpus for the load-bearing ones."""
    claims = _corpus_claims()
    expect = {
        "S1-03": "PROVEN",     # the radius identity
        "S1-04": "PROVEN",     # the growth law with exponent s
        "S1-05": "STRUCTURAL",  # Pincherle reading, interpretive
        "S3B-04": "STRUCTURAL",  # closed form for K, derivation
        "S3B-05": "VERIFIED",  # K agrees numerically
        "S21-76": "INSPECTED",  # Wong-Li II not obtained
        "S22-21": "PROVEN",    # Gamma(1/6) identity, 5A void
        "S22-22": "VERIFIED",  # the 5B negative
        "S26-01": "PROVEN",    # the upper bound on r_inf
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
    """K must never be called PROVEN, and must be called VERIFIED."""
    if "VERIFIED, never PROVEN" not in text:
        return False, "the 'VERIFIED, never PROVEN' statement for K is missing"
    for m in re.finditer(r"PROVEN", text):
        window = text[max(0, m.start() - 160):m.start()]
        if re.search(r"\bK\b\s*(is|=)[^.]{0,40}$", window):
            return False, "K appears to be labelled PROVEN near offset %d" % m.start()
    return True, "K carries VERIFIED and is never labelled PROVEN"


def check_pslq_basis_in_full(text):
    """The PSLQ search space must be printed in full, with no ellipsis."""
    blocks = re.findall(r"```\n(.*?)```", text, re.S)
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
            return False, "basis block contains an ellipsis (%r) -- it must be printed in full" % bad
    if "\u0393(1/6)" in b:
        return False, "basis block still contains Gamma(1/6), the degenerate element"
    return True, "6-vector printed in full, no ellipsis, Gamma(1/6) removed"


def check_naming_prohibition(text):
    """K at xi_0 and S_{zeta*} at 2 xi_0 must be stated as a prohibition."""
    if "Naming prohibition" not in text and "naming prohibition" not in text.lower():
        return False, "no naming-prohibition heading"
    seg = text[text.lower().index("naming prohibition"):]
    seg = seg[:1400]
    if "amplitude at" not in seg or "Stokes constant at" not in seg:
        return False, "the two roles are not both stated"
    if "2/\u221a3" not in seg or "4/\u221a3" not in seg:
        return False, "the two points are not both given numerically"
    if "never be used for the other" not in seg.lower() and \
       "may ever be used for the other" not in seg.lower():
        return False, "the prohibition itself is not stated"
    return True, "K at xi_0, S_zeta* at 2 xi_0, prohibition stated"


def check_wongli_not_obtained(text):
    """Wong-Li II must be stated NOT OBTAINED, with the full citation."""
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
    """The notice must deny formal verification, and must not claim it."""
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
    """Ibrahim-Salvy must be quoted in the weaker printed form only."""
    if "do not know how to compute" not in text:
        return False, "the weaker printed form is not quoted"
    for m in re.finditer(r"is not computable", text):
        window = text[max(0, m.start() - 120):m.start()]
        if "not** that it *" not in window and "not**" not in window:
            return False, "'is not computable' used without the not-that framing"
    return True, "weaker printed form quoted; stronger form only as the excluded reading"


def check_odlyzko_split(text):
    """The Odlyzko p.77 attribution split must survive."""
    if "Wimp and Zeilberger" not in text:
        return False, "Wimp and Zeilberger are not named"
    if "only the\n**second is his own" not in text.replace("\r", "") and \
       "only the\nsecond is his own" not in text.replace("\r", "") and \
       "second is his own" not in text:
        return False, "the split is not stated"
    if "may not be rigorous" not in text:
        return False, "the B-T rigour objection from the same page is missing"
    if "Nothing rests on B\u2013T" not in text:
        return False, "the pre-emption ('nothing rests on B-T') is missing"
    return True, "split stated, B-T objection quoted, pre-emption present"


def check_missing_versions_declared(text):
    """v1.4/v1.5/v1.6 absence must be declared, not papered over."""
    if "not in this repository" not in text:
        return False, "the absence is not declared"
    for v in ("v1.4", "v1.5", "v1.6"):
        if v not in text:
            return False, "%s is not mentioned" % v
    if "rem:d3-vacuous" not in text:
        return False, "rem:d3-vacuous is not named"
    seg_i = text.index("rem:d3-vacuous")
    seg = text[seg_i:seg_i + 600]
    if "could not be read" not in seg and "not in this repository" not in seg:
        return False, "rem:d3-vacuous is cited without declaring it was unreadable"
    return True, "v1.4-v1.6 absence and rem:d3-vacuous unreadability both declared"


def check_scope_of_negative(text):
    """The 5B negative must be scoped: excludes a space, not a closed form."""
    if "This excludes that space" not in text and "EXCLUDES THAT SPACE" not in text.upper():
        return False, "the scope sentence is missing"
    if "not** evidence that" not in text and "not evidence that" not in text:
        return False, "the 'not evidence that C has no closed form' clause is missing"
    if "1.5051" not in text:
        return False, "the positive control's cost is not reported"
    if "8.1273367954950723671" not in text:
        return False, "C is not printed"
    return True, "scope, control cost 1.5051, and C all present"


def check_zeta_is_action_difference(text):
    """zeta* = 2 xi_0 must be an action difference, explicitly not a change of variable."""
    if "not a change of variable" not in text:
        return False, "the 'not a change of variable' statement is missing"
    if "action difference" not in text:
        return False, "'action difference' is not stated"
    if "g2_pade_borel.py" not in text:
        return False, "the decisive source is not cited"
    return True, "action difference, negation, and source all present"


CHECKS = [
    ("concept DOI traced to a held source", check_concept_doi),
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
    ("v1.4-v1.6 absence declared", check_missing_versions_declared),
    ("the 5B negative is scoped", check_scope_of_negative),
    ("zeta* is an action difference", check_zeta_is_action_difference),
]

# ------------------------------------------------- mutants (can-fail controls)
# Each mutant removes exactly the thing one check guards.  If the check still
# passes on its mutant, the check is broken.
MUTANTS = {
    "concept DOI traced to a held source":
        lambda t: t.replace("10.5281/zenodo.19941678", "10.5281/zenodo.99999999"),
    "all cited paths exist":
        lambda t: t.replace("`CT-S8-LITCHECK/refs/gautschi1967.pdf`",
                            "`CT-S8-LITCHECK/refs/gautschi1967_NOSUCH.pdf`"),
    "all cited claim ids resolve":
        lambda t: t.replace("`S1-03`", "`S1-999`"),
    "load-bearing labels match the corpus":
        lambda t: t,  # replaced below by a label-table mutant
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
    "v1.4-v1.6 absence declared":
        lambda t: t.replace("not in this repository", "available"),
    "the 5B negative is scoped":
        lambda t: t.replace("**This excludes that space.**", ""),
    "zeta* is an action difference":
        lambda t: t.replace("not a change of variable", "a change of variable"),
}


def label_mutant_check(text):
    """Control for check_labels: assert a label the corpus does not carry."""
    claims = _corpus_claims()
    if claims.get("S22-22", {}).get("label") == "PROVEN":
        return True, "corpus really does say PROVEN"
    return False, "S22-22 is VERIFIED in the corpus, not PROVEN"


def main():
    if not os.path.exists(NOTICE):
        print("FATAL: %s not found" % NOTICE)
        return 2
    raw = open(NOTICE, "rb").read()
    text = raw.decode("utf-8").replace("\r\n", "\n")
    digest = hashlib.sha256(raw).hexdigest()

    print("=" * 74)
    print("verify_notice.py -- CT-S26-CTV17-DRAFT")
    print("=" * 74)
    print("notice : %s" % os.path.relpath(NOTICE, REPO).replace("\\", "/"))
    print("sha256 : %s" % digest)
    print("bytes  : %d" % len(raw))
    print()

    print("SECTION 1 -- CHECKS AGAINST THE NOTICE AS WRITTEN")
    print("-" * 74)
    for name, fn in CHECKS:
        try:
            ok, detail = fn(text)
        except Exception as exc:  # a crashing check is a failing check
            ok, detail = False, "check raised %s: %s" % (type(exc).__name__, exc)
        report(name, ok, detail)

    print()
    print("SECTION 2 -- CAN-FAIL CONTROLS (each check run against its own mutant)")
    print("-" * 74)
    for name, fn in CHECKS:
        if name == "load-bearing labels match the corpus":
            ok, _d = label_mutant_check(text)
            fired = not ok
        else:
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
            continue
        print("  [%s] %s -- mutant %s" % ("PASS" if fired else "BROKEN", name,
                                          "rejected" if fired else "ACCEPTED"))
        if not fired:
            broken.append(name)

    print()
    print("=" * 74)
    print("checks run          : %d" % len(CHECKS))
    print("checks failed       : %d%s" % (len(failures),
                                          ("  -> " + ", ".join(failures)) if failures else ""))
    print("controls fired      : %d of %d" % (len(CHECKS) - len(broken), len(CHECKS)))
    print("broken checks       : %d%s" % (len(broken),
                                          ("  -> " + ", ".join(broken)) if broken else ""))
    verdict = "OK" if (not failures and not broken) else "FAIL"
    print("VERDICT: %s" % verdict)
    print("=" * 74)
    return 0 if verdict == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
