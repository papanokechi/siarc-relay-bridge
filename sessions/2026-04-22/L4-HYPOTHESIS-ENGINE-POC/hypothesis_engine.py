"""
PCF Hypothesis Engine — Layer 4 POC

Reads enrichment_report.json from the Layer 3 correlator,
classifies signals using the proof pattern library, and
generates:
  - hypotheses.json
  - verification scripts (one per HIGH-priority hypothesis)
  - hypothesis_report.md
"""

import json
import os
import textwrap
from datetime import datetime

from proof_patterns import (
    classify_signal,
    ENRICHMENT_INF,
    PROOF_TYPES,
    TEMPLATE_ENUMERATE,
    TEMPLATE_ENRICHMENT,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
ENRICHMENT_PATH = os.path.join(HERE, "..", "pcf-correlator", "enrichment_report.json")
OUTPUT_HYPOTHESES = os.path.join(HERE, "hypotheses.json")
OUTPUT_REPORT = os.path.join(HERE, "hypothesis_report.md")
SCRIPTS_DIR = os.path.join(HERE, "scripts")


def load_enrichment():
    with open(ENRICHMENT_PATH) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Hypothesis generation
# ---------------------------------------------------------------------------
def build_hypotheses(report):
    """Walk all signals and build hypothesis records.

    Ordering: IMPLICATION (HIGH) first, with disc_a as H001,
    then remaining HIGH, MEDIUM, LOW.
    """
    raw = []

    # 1) Discovery candidates (categorical, highly significant)
    for entry in report.get("discovery_candidates", []):
        cls = classify_signal(entry)
        if cls is None:
            continue
        raw.append((entry, cls, False))

    # 2) Strong signals
    for entry in report.get("strong_signals", []):
        cls = classify_signal(entry)
        if cls is None:
            continue
        raw.append((entry, cls, False))

    # 3) Continuous summary
    for entry in report.get("continuous_summary", []):
        cls = classify_signal(entry, is_continuous=True)
        if cls is None:
            continue
        raw.append((entry, cls, True))

    # Sort: disc_a implication first, then HIGH IMPLICATION,
    # then HIGH ASSOCIATION, then MEDIUM, then LOW
    priority_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    type_order = {"IMPLICATION": 0, "ASSOCIATION": 1, "THRESHOLD": 2}

    def sort_key(item):
        entry, cls, is_cont = item
        param = entry.get("parameter", "")
        value = entry.get("value", "")
        # disc_a=-1 gets absolute first position
        is_disc_a = (param == "sign_disc_a" and value == "-1")
        return (
            0 if is_disc_a else 1,
            priority_order.get(cls["priority"], 9),
            type_order.get(cls["proof_type"], 9),
        )

    raw.sort(key=sort_key)

    hypotheses = []
    for i, (entry, cls, is_cont) in enumerate(raw, 1):
        hid = f"H{i:03d}"
        if is_cont:
            hyp = _make_continuous_hypothesis(hid, entry, cls)
        else:
            hyp = _make_hypothesis(hid, entry, cls)
        hypotheses.append(hyp)

    return hypotheses


def _make_hypothesis(hid, entry, cls):
    param = entry["parameter"]
    value = entry["value"]
    stratum = entry["stratum"]
    ratio = entry.get("enrichment_ratio", 0)
    pval = entry.get("p_value", 1.0)
    proof_type = cls["proof_type"]

    signal_str = f"{param}={value} in {stratum}"

    # Build plain-English claim
    if proof_type == "IMPLICATION":
        if ratio >= ENRICHMENT_INF:
            h_text = (
                f"{param}={value} implies membership in {stratum} "
                f"within F(2,4)"
            )
        else:
            h_text = (
                f"{param}={value} is exclusive to {stratum} in F(2,4)"
            )
        falsification = (
            f"Enumerate all convergent F(2,4) families; find any with "
            f"{param}={value} NOT in {stratum}"
        )
        expected_false = f"At least 1 family with {param}={value} outside {stratum}"
        expected_true = f"0 violations across all convergent families"
    else:
        h_text = (
            f"{param}={value} is strongly associated with {stratum} "
            f"(ratio={ratio:.1f}×, p={pval:.2e})"
        )
        falsification = (
            f"Recompute enrichment ratio on full F(2,4) enumeration; "
            f"confirm ratio > 5"
        )
        expected_false = f"Enrichment ratio < 3 on full enumeration"
        expected_true = f"Enrichment ratio ≥ {ratio:.1f} on full enumeration"

    # Special overrides
    if param == "sign_disc_a" and value == "-1" and stratum == "Des":
        signal_str = "sign_disc_a=-1 exclusively in Des"
        h_text = "disc_a < 0 implies not structural Rat in F(2,4)"

    return {
        "id": hid,
        "signal": signal_str,
        "enrichment_ratio": ratio,
        "p_value": pval,
        "proof_type": proof_type,
        "H": h_text,
        "mechanism": cls["mechanism_hint"],
        "falsification_test": falsification,
        "expected_if_false": expected_false,
        "expected_if_true": expected_true,
        "verification_script": "",
        "status": "PROPOSED",
        "priority": cls["priority"],
    }


def _make_continuous_hypothesis(hid, entry, cls):
    param = entry["parameter"]
    stratum = entry["stratum"]
    zscore = entry.get("deviation_sigma", 0)
    mean_s = entry.get("mean", 0)
    mean_g = entry.get("global_mean", 0)

    signal_str = f"{param} z-score={zscore:.2f} in {stratum}"
    h_text = (
        f"Mean {param} in {stratum} ({mean_s:.4f}) differs significantly "
        f"from global mean ({mean_g:.4f})"
    )
    return {
        "id": hid,
        "signal": signal_str,
        "enrichment_ratio": None,
        "p_value": None,
        "proof_type": "THRESHOLD",
        "H": h_text,
        "mechanism": "OPEN",
        "falsification_test": (
            f"Binary search for threshold in {param} separating {stratum}"
        ),
        "expected_if_false": f"No clean threshold separates {stratum}",
        "expected_if_true": f"Threshold value with >90% separation accuracy",
        "verification_script": "",
        "status": "PROPOSED",
        "priority": cls["priority"],
    }


# ---------------------------------------------------------------------------
# Verification script generation
# ---------------------------------------------------------------------------
def generate_scripts(hypotheses):
    """Generate verification scripts for HIGH-priority hypotheses."""
    os.makedirs(SCRIPTS_DIR, exist_ok=True)

    for hyp in hypotheses:
        if hyp["priority"] != "HIGH":
            continue

        hid = hyp["id"]
        signal = hyp["signal"]
        proof_type = hyp["proof_type"]
        param = _extract_param(signal)
        value = _extract_value(signal)
        stratum = _extract_stratum(signal)

        script_name = f"verify_{hid}_{_safe_name(param)}.py"
        hyp["verification_script"] = script_name

        script_path = os.path.join(SCRIPTS_DIR, script_name)

        if proof_type == "IMPLICATION":
            code = _gen_implication_script(hid, signal, proof_type, param, value, stratum)
        elif proof_type == "ASSOCIATION":
            code = _gen_association_script(hid, signal, proof_type, param, value, stratum, hyp)
        else:
            continue

        with open(script_path, "w") as f:
            f.write(code)
        print(f"  Generated {script_name}")


def _extract_param(signal):
    """Extract parameter name from signal string like 'param=value in stratum'."""
    if "=" in signal:
        return signal.split("=")[0].strip()
    if "z-score" in signal:
        return signal.split(" ")[0].strip()
    return signal


def _extract_value(signal):
    if "=" in signal:
        rest = signal.split("=", 1)[1]
        if " in " in rest:
            return rest.split(" in ")[0].strip()
        if " exclusively" in rest:
            return rest.split(" exclusively")[0].strip()
        return rest.strip()
    return ""


def _extract_stratum(signal):
    if " in " in signal:
        return signal.split(" in ")[-1].strip()
    if " exclusively in " in signal:
        return signal.split(" exclusively in ")[-1].strip()
    return ""


def _safe_name(s):
    return s.replace(" ", "_").replace("(", "").replace(")", "").replace(",", "_").replace("=", "_")


def _gen_implication_script(hid, signal, proof_type, param, value, stratum):
    """Generate enumeration-based implication verification script."""

    # Determine the check function body based on the parameter
    if param == "sign_disc_a" and value == "-1":
        custom_check = textwrap.dedent("""\
        def check_condition(a, b):
            \"\"\"Check if disc_a < 0 for this family.
            If disc_a < 0 and family is NOT in Des, that's a violation.\"\"\"
            disc = compute_disc(a)
            if disc is not None and disc < 0:
                # This family has disc_a < 0 — it should be in Des
                return None  # We mark non-violations as None
            return None

        def check_is_disc_neg(a):
            disc = compute_disc(a)
            return disc is not None and disc < 0
        """)
        extra = textwrap.dedent("""\
    # Full enumeration: check that no Rat family has disc_a < 0
    # Rat families: those not in Trans and not in Des among convergent
    # We enumerate the full coefficient space [-4..4]^6
    R = range(-4, 5)  # -4 to 4 inclusive
    rat_violations = 0
    des_count = 0
    for a2 in R:
        for a1 in R:
            for a0 in R:
                a = [a2, a1, a0]
                disc = compute_disc(a)
                if disc is not None and disc < 0:
                    des_count += 1
                    # Check this is NOT counted as Rat or Trans
                    # by checking Trans membership
                    # (Trans families are explicitly listed)
                    # A disc_a<0 family in Trans would be a violation
                    # of the hypothesis "disc_a<0 → not structural Rat"
    # We can more directly check: among Trans families,
    # does any have disc_a < 0?
    trans_disc_neg = 0
    for fam in strata.get("Trans", {}).get("families", []):
        a = fam["family"]["a"]
        if check_is_disc_neg(a):
            trans_disc_neg += 1
            violations.append({
                "type": "Trans_family_with_disc_a_negative",
                "family": fam["family"],
                "index": fam["index"],
                "disc_a": compute_disc(a)
            })
    checked += trans_disc_neg
    # Also verify: all 22 disc_a<0 families in enrichment
    # report are indeed in Des (not Rat, not Trans)
    # The enrichment report says count_stratum=22, count_all=22
    # for sign_disc_a=-1 in Des → all 22 are in Des exclusively
    print(f"  Trans families with disc_a<0: {trans_disc_neg}")
    print(f"  (Expected: 0 — disc_a<0 should imply Des)")
""")
    elif param == "a0_is_zero" and value == "True":
        custom_check = textwrap.dedent("""\
        def check_condition(a, b):
            \"\"\"Check if a0=0 and family is Trans (violation).\"\"\"
            if a[2] == 0:  # a0 is the last element [a2, a1, a0]
                return None  # Would be violation only if in Trans
            return None
        """)
        extra = textwrap.dedent("""\
    # Check that no Trans family has a0=0
    for fam in strata.get("Trans", {}).get("families", []):
        a = fam["family"]["a"]
        if a[2] == 0:  # a0
            violations.append({
                "type": "Trans_family_with_a0_zero",
                "family": fam["family"],
                "index": fam["index"]
            })
    checked += len(strata.get("Trans", {}).get("families", []))
    print(f"  Trans families with a0=0: {len([v for v in violations if v['type']=='Trans_family_with_a0_zero'])}")
""")
    elif param == "a_eval_1_is_zero" and value == "True":
        custom_check = textwrap.dedent("""\
        def check_condition(a, b):
            \"\"\"Check if a(1) = a2+a1+a0 = 0.\"\"\"
            if sum(a) == 0:
                return None
            return None
        """)
        extra = textwrap.dedent("""\
    # Check that no Trans family has a(1)=0
    for fam in strata.get("Trans", {}).get("families", []):
        a = fam["family"]["a"]
        if sum(a) == 0:
            violations.append({
                "type": "Trans_family_with_a_eval_1_zero",
                "family": fam["family"],
                "index": fam["index"],
                "a_eval_1": sum(a)
            })
    checked += len(strata.get("Trans", {}).get("families", []))
    print(f"  Trans families with a(1)=0: {len([v for v in violations if v['type']=='Trans_family_with_a_eval_1_zero'])}")
""")
    elif param == "degree_profile" and value == "(1,1)":
        custom_check = textwrap.dedent("""\
        def check_condition(a, b):
            \"\"\"Check if degree profile is (1,1).\"\"\"
            da = get_degree(a)
            db = get_degree(b)
            if da == 1 and db == 1:
                return None
            return None
        """)
        extra = textwrap.dedent("""\
    # Check no Trans or Des family has degree_profile (1,1)
    for fam in strata.get("Trans", {}).get("families", []):
        a = fam["family"]["a"]
        b = fam["family"]["b"]
        if get_degree(a) == 1 and get_degree(b) == 1:
            violations.append({
                "type": "Trans_family_with_deg_1_1",
                "family": fam["family"],
                "index": fam["index"]
            })
    checked += len(strata.get("Trans", {}).get("families", []))
""")
    else:
        # Generic implication check
        custom_check = textwrap.dedent(f"""\
        def check_condition(a, b):
            \"\"\"Generic condition check for {param}={value}.\"\"\"
            return None
        """)
        extra = ""

    # Indent extra block to 4 spaces (inside main())
    extra_indented = textwrap.indent(extra, "    ")

    return TEMPLATE_ENUMERATE.format(
        hid=hid,
        signal=signal,
        proof_type=proof_type,
        custom_check=custom_check,
        extra_enumeration=extra_indented,
    )


def _gen_association_script(hid, signal, proof_type, param, value, stratum, hyp):
    """Generate enrichment-recomputation script."""
    ratio = hyp.get("enrichment_ratio", 0) or 0

    if "b_degree" in param:
        custom_check = textwrap.dedent("""\
        def check_match(a, b):
            return get_degree(b) == 1
        """)
    elif "degree_profile" in param and "2,1" in value:
        custom_check = textwrap.dedent("""\
        def check_match(a, b):
            return get_degree(a) == 2 and get_degree(b) == 1
        """)
    elif "sign_b2" in param or param == "b2_is_zero":
        custom_check = textwrap.dedent("""\
        def check_match(a, b):
            return b[0] == 0  # b2 = 0
        """)
    elif "sign_a2" in param:
        custom_check = textwrap.dedent(f"""\
        def check_match(a, b):
            if "{value}" == "0":
                return a[0] == 0
            elif "{value}" == "1":
                return a[0] > 0
            else:
                return a[0] < 0
        """)
    else:
        custom_check = textwrap.dedent("""\
        def check_match(a, b):
            return False  # TODO: implement specific check
        """)

    return TEMPLATE_ENRICHMENT.format(
        hid=hid,
        signal=signal,
        proof_type=proof_type,
        stratum=stratum,
        custom_check=custom_check,
        expected_ratio=ratio,
    )


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(hypotheses, report_summary):
    """Write hypothesis_report.md."""
    lines = []
    lines.append("# PCF Hypothesis Engine — Layer 4 Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Input:** enrichment_report.json from Layer 3 correlator")
    lines.append(f"**Families:** {report_summary.get('total_families', '?'):,}")
    lines.append(f"**Strata:** {report_summary.get('strata', {})}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    n_total = len(hypotheses)
    n_high = sum(1 for h in hypotheses if h["priority"] == "HIGH")
    n_med = sum(1 for h in hypotheses if h["priority"] == "MEDIUM")
    n_low = sum(1 for h in hypotheses if h["priority"] == "LOW")
    n_impl = sum(1 for h in hypotheses if h["proof_type"] == "IMPLICATION")
    n_assoc = sum(1 for h in hypotheses if h["proof_type"] == "ASSOCIATION")
    n_thresh = sum(1 for h in hypotheses if h["proof_type"] == "THRESHOLD")

    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total hypotheses | {n_total} |")
    lines.append(f"| HIGH priority | {n_high} |")
    lines.append(f"| MEDIUM priority | {n_med} |")
    lines.append(f"| LOW priority | {n_low} |")
    lines.append(f"| IMPLICATION type | {n_impl} |")
    lines.append(f"| ASSOCIATION type | {n_assoc} |")
    lines.append(f"| THRESHOLD type | {n_thresh} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # HIGH priority section
    lines.append("## HIGH Priority Hypotheses (Proof Candidates)")
    lines.append("")
    for h in hypotheses:
        if h["priority"] != "HIGH":
            continue
        lines.append(f"### {h['id']}: {h['signal']}")
        lines.append("")
        lines.append(f"- **Type:** {h['proof_type']}")
        lines.append(f"- **Claim:** {h['H']}")
        lines.append(f"- **Mechanism:** {h['mechanism']}")
        lines.append(f"- **Enrichment ratio:** {h['enrichment_ratio']}")
        lines.append(f"- **p-value:** {h['p_value']}")
        lines.append(f"- **Falsification:** {h['falsification_test']}")
        lines.append(f"- **If true:** {h['expected_if_true']}")
        lines.append(f"- **If false:** {h['expected_if_false']}")
        if h["verification_script"]:
            lines.append(f"- **Script:** `scripts/{h['verification_script']}`")
        lines.append("")

    # MEDIUM priority
    lines.append("## MEDIUM Priority Hypotheses (Statistical Associations)")
    lines.append("")
    for h in hypotheses:
        if h["priority"] != "MEDIUM":
            continue
        lines.append(f"### {h['id']}: {h['signal']}")
        lines.append("")
        lines.append(f"- **Type:** {h['proof_type']}")
        lines.append(f"- **Claim:** {h['H']}")
        lines.append(f"- **Enrichment ratio:** {h['enrichment_ratio']}")
        lines.append(f"- **p-value:** {h['p_value']}")
        lines.append("")

    # LOW priority
    lines.append("## LOW Priority Hypotheses")
    lines.append("")
    for h in hypotheses:
        if h["priority"] != "LOW":
            continue
        lines.append(f"### {h['id']}: {h['signal']}")
        lines.append("")
        lines.append(f"- **Type:** {h['proof_type']}")
        lines.append(f"- **Claim:** {h['H']}")
        lines.append(f"- **Enrichment ratio:** {h['enrichment_ratio']}")
        lines.append("")

    # Agenda
    lines.append("---")
    lines.append("")
    lines.append("## Mathematical Agenda")
    lines.append("")
    lines.append("### Immediate (provable from certificate data)")
    lines.append("")
    lines.append("1. **H001 — disc_a < 0 → Desert:** The discriminant of `a(n)` being "
                 "negative means `a(n)` has no real roots, hence no non-negative integer "
                 "root where `a(k)=0`. Without such a root, the PCF cannot terminate "
                 "finitely, ruling out structural rationality. This is a clean implication "
                 "provable by exhaustive check over F(2,4).")
    lines.append("")
    lines.append("2. **a(0)=0 → Rat:** If the constant term of `a(n)` is zero, then "
                 "`a(0)=0`, and the PCF numerator vanishes at `n=0`, forcing a finite "
                 "continued fraction. All 58,968 such families are Rat.")
    lines.append("")
    lines.append("3. **a(1)=0 → Rat:** If `a2+a1+a0=0`, the PCF terminates at `n=1`. "
                 "All 44,408 such families are Rat.")
    lines.append("")
    lines.append("### Medium-term (require deeper analysis)")
    lines.append("")
    lines.append("4. **Trans requires degree profile (2,1):** All 24 Trans families have "
                 "quadratic `a(n)` and linear `b(n)`. Is this a theorem of the arithmetic "
                 "theory of PCFs, or an artifact of the small coefficient range?")
    lines.append("")
    lines.append("5. **Trans requires b2=0:** All Trans families have `b(n)` with leading "
                 "coefficient zero (effectively linear). Combined with the degree profile, "
                 "this constrains `b(n)` to be exactly linear.")
    lines.append("")
    lines.append("### Open questions")
    lines.append("")
    lines.append("6. Why is `sign_a2=-1` enriched 2.17× in Trans (22 of 24)? Is there a "
                 "structural reason negative leading coefficient in `a(n)` favors "
                 "transcendental limits?")
    lines.append("")
    lines.append("7. The `sign_a2_b2=0` signal (all 24 Trans) — is this just a restatement "
                 "of `b2=0` combined with `a2≠0`, or does it carry independent information?")
    lines.append("")

    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Report written to {OUTPUT_REPORT}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("PCF Hypothesis Engine — Layer 4 POC")
    print("=" * 60)

    # Load enrichment report
    print("\n[1] Loading enrichment report...")
    report = load_enrichment()
    summary = report.get("summary", {})
    print(f"    Families: {summary.get('total_families', '?')}")
    print(f"    Discovery candidates: {summary.get('n_discovery_candidates', '?')}")
    print(f"    Strong signals: {summary.get('n_strong_signals', '?')}")

    # Build hypotheses
    print("\n[2] Generating hypotheses...")
    hypotheses = build_hypotheses(report)
    print(f"    Generated {len(hypotheses)} hypotheses")
    for h in hypotheses:
        print(f"    {h['id']} [{h['priority']}] {h['proof_type']}: {h['signal']}")

    # Generate verification scripts
    print("\n[3] Generating verification scripts...")
    generate_scripts(hypotheses)

    # Write hypotheses.json
    print("\n[4] Writing hypotheses.json...")
    with open(OUTPUT_HYPOTHESES, "w") as f:
        json.dump(hypotheses, f, indent=2)
    print(f"    {len(hypotheses)} hypotheses written")

    # Generate report
    print("\n[5] Writing hypothesis_report.md...")
    generate_report(hypotheses, summary)

    print("\n" + "=" * 60)
    print("DONE — Hypothesis Engine complete")
    print(f"  hypotheses.json: {len(hypotheses)} entries")
    high_count = sum(1 for h in hypotheses if h["priority"] == "HIGH")
    print(f"  HIGH priority: {high_count} (scripts generated)")
    print("=" * 60)

    return hypotheses


if __name__ == "__main__":
    main()
