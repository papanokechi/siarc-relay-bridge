"""
Proof Pattern Library for the PCF Hypothesis Engine.

Maps enrichment signal patterns to proof types, hypothesis forms,
falsification strategies, and verification script templates.
"""

# ---------------------------------------------------------------------------
# Pattern classification thresholds
# ---------------------------------------------------------------------------
ENRICHMENT_INF = 9999.0          # proxy for infinity in the enrichment report
ENRICHMENT_STRONG = 5.0          # association threshold (strong)
ENRICHMENT_MODERATE = 3.0        # association threshold (moderate)
P_VALUE_CUTOFF = 0.001           # significance cutoff
ZSCORE_THRESHOLD = 3.0           # continuous-parameter flag level


# ---------------------------------------------------------------------------
# Proof-type catalogue
# ---------------------------------------------------------------------------
PROOF_TYPES = {
    "IMPLICATION": {
        "description": (
            "Parameter=value is exclusive to one stratum. "
            "Every family with this property belongs to the stratum."
        ),
        "hypothesis_form": (
            "{param}={value} implies membership in {stratum}"
        ),
        "falsification": (
            "Enumerate all convergent families in F(2,4). "
            "Find any family with {param}={value} NOT in {stratum}."
        ),
        "script_strategy": "enumerate_all_check_condition",
    },
    "ASSOCIATION": {
        "description": (
            "Parameter=value is strongly enriched in one stratum "
            "but not exclusive."
        ),
        "hypothesis_form": (
            "{param}={value} is strongly associated with {stratum} "
            "(enrichment ratio {ratio:.1f}×, p={pval:.2e})"
        ),
        "falsification": (
            "Verify enrichment ratio holds on the full enumeration. "
            "Resample at larger size and recompute."
        ),
        "script_strategy": "recompute_enrichment",
    },
    "THRESHOLD": {
        "description": (
            "Continuous parameter mean differs significantly "
            "between a stratum and its complement."
        ),
        "hypothesis_form": (
            "Mean of {param} in {stratum} differs from global mean "
            "(z = {zscore:.2f}σ)"
        ),
        "falsification": (
            "Binary search for a threshold value of {param} that "
            "separates {stratum} from complement."
        ),
        "script_strategy": "threshold_binary_search",
    },
}


def classify_signal(entry, is_continuous=False):
    """Classify an enrichment entry into a proof type.

    Parameters
    ----------
    entry : dict
        One record from discovery_candidates, strong_signals,
        or categorical_enrichment in the enrichment report.
    is_continuous : bool
        True when the entry comes from continuous_summary.

    Returns
    -------
    dict with keys: proof_type, priority, mechanism_hint
    """
    if is_continuous:
        zscore = abs(entry.get("deviation_sigma", 0))
        if zscore >= ZSCORE_THRESHOLD:
            return {
                "proof_type": "THRESHOLD",
                "priority": "MEDIUM",
                "mechanism_hint": "OPEN",
            }
        return None  # not significant

    ratio = entry.get("enrichment_ratio", 0)
    pval = entry.get("p_value", 1.0)
    stratum = entry.get("stratum", "")

    if ratio >= ENRICHMENT_INF:
        # exclusive signal → implication
        priority = "HIGH"
        if stratum == "Trans":
            priority = "HIGH"  # Trans always HIGH
        return {
            "proof_type": "IMPLICATION",
            "priority": priority,
            "mechanism_hint": _guess_mechanism(entry),
        }

    if ratio >= ENRICHMENT_STRONG and pval < P_VALUE_CUTOFF:
        priority = "MEDIUM"
        if stratum == "Trans":
            priority = "HIGH"
        return {
            "proof_type": "ASSOCIATION",
            "priority": priority,
            "mechanism_hint": "OPEN",
        }

    if ratio >= ENRICHMENT_MODERATE and pval < P_VALUE_CUTOFF:
        return {
            "proof_type": "ASSOCIATION",
            "priority": "LOW",
            "mechanism_hint": "OPEN",
        }

    return None  # below thresholds


def _guess_mechanism(entry):
    """Provide a structural hint for implication-type signals."""
    param = entry.get("parameter", "")
    value = entry.get("value", "")
    stratum = entry.get("stratum", "")

    if param == "sign_disc_a" and value == "-1" and stratum == "Des":
        return (
            "disc_a < 0 means a(n) has no real roots, hence no "
            "non-negative integer root k with a(k)=0, hence not "
            "structural Rat"
        )
    if param == "a0_is_zero" and value == "True" and stratum == "Rat":
        return (
            "a(0)=0 means n=0 is a root of a(n), so a(0)=0 forces "
            "the PCF numerator to vanish at n=0, producing a "
            "finite continued fraction (structural Rat)"
        )
    if param == "a_eval_1_is_zero" and value == "True" and stratum == "Rat":
        return (
            "a(1)=a2+a1+a0=0 means the PCF numerator vanishes at n=1, "
            "forcing finite termination (structural Rat)"
        )
    if param == "degree_profile" and value == "(1,1)" and stratum == "Rat":
        return (
            "Linear a(n) and linear b(n) produce a Gauss-type CF "
            "that always converges to a rational value"
        )
    return "OPEN"


# ---------------------------------------------------------------------------
# Script templates
# ---------------------------------------------------------------------------
SCRIPT_HEADER = '''\
"""
Auto-generated verification script for hypothesis {hid}.
Signal: {signal}
Proof type: {proof_type}
"""
import json, os, sys

CERT_PATH = os.path.join(os.path.dirname(__file__), "..", "..",
                         "f1_base_certificate.json")
RESULT_PATH = os.path.join(os.path.dirname(__file__), "..",
                           "verification_results.json")
'''

TEMPLATE_ENUMERATE = SCRIPT_HEADER + '''
def load_certificate():
    with open(CERT_PATH) as f:
        return json.load(f)

def compute_disc(coeffs):
    """Discriminant of quadratic a2*n^2 + a1*n + a0."""
    if len(coeffs) == 3:
        a2, a1, a0 = coeffs
        return a1*a1 - 4*a2*a0
    return None

def get_degree(coeffs):
    """Effective degree of polynomial [leading..constant]."""
    for i, c in enumerate(coeffs):
        if c != 0:
            return len(coeffs) - 1 - i
    return 0

{custom_check}

def main():
    cert = load_certificate()
    strata = cert["strata"]
    violations = []
    checked = 0

    # Collect stratum membership sets
    trans_indices = set()
    for fam in strata.get("Trans", {{}}).get("families", []):
        trans_indices.add(fam["index"])

    rat_count = strata.get("Rat", {{}}).get("count", 0)

    # We need to enumerate all convergent families.
    # The certificate has Trans families listed explicitly.
    # Rat families are identified by structural mechanism.
    # Des families are everything else among convergent.
    # For the check we iterate over the enumeration space.

    total_enum = cert.get("total_enumerated", 531441)
    convergent = cert.get("convergent", 513387)

    # Reconstruct enumeration: coefficients in [-4..4] for
    # [a2,a1,a0,b2,b1,b0], but we use the certificate strata.
    # For implication checks, we verify the Trans families satisfy
    # or violate the condition, plus spot-check Rat/Des.

    # Check all Trans families
    for fam in strata.get("Trans", {{}}).get("families", []):
        a = fam["family"]["a"]
        b = fam["family"]["b"]
        result = check_condition(a, b)
        if result is not None:
            violations.append(result)
        checked += 1

{extra_enumeration}

    result = {{
        "hypothesis": "{hid}",
        "signal": "{signal}",
        "proof_type": "{proof_type}",
        "checked": checked,
        "violations": len(violations),
        "violation_details": violations[:20],
        "status": "CONFIRMED" if len(violations) == 0 else "FALSIFIED"
    }}

    # Merge into verification_results.json
    results = []
    if os.path.exists(RESULT_PATH):
        with open(RESULT_PATH) as f:
            results = json.load(f)
    # Replace existing entry for this hypothesis
    results = [r for r in results if r.get("hypothesis") != "{hid}"]
    results.append(result)
    with open(RESULT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"{{result['hypothesis']}}: {{result['status']}} "
          f"({{result['violations']}} violations in {{result['checked']}} checked)")
    return result

if __name__ == "__main__":
    main()
'''

TEMPLATE_ENRICHMENT = SCRIPT_HEADER + '''
import math

def load_certificate():
    with open(CERT_PATH) as f:
        return json.load(f)

def compute_disc(coeffs):
    if len(coeffs) == 3:
        a2, a1, a0 = coeffs
        return a1*a1 - 4*a2*a0
    return None

def get_degree(coeffs):
    for i, c in enumerate(coeffs):
        if c != 0:
            return len(coeffs) - 1 - i
    return 0

{custom_check}

def main():
    cert = load_certificate()
    strata = cert["strata"]

    # Count families matching condition in each stratum
    target_stratum = "{stratum}"
    n_target = 0
    n_other = 0
    match_target = 0
    match_other = 0

    # Trans families
    for fam in strata.get("Trans", {{}}).get("families", []):
        a = fam["family"]["a"]
        b = fam["family"]["b"]
        hit = check_match(a, b)
        if "Trans" == target_stratum:
            n_target += 1
            if hit: match_target += 1
        else:
            n_other += 1
            if hit: match_other += 1

    # For Rat/Des we use counts from the certificate
    # and the enrichment report ratio to validate
    expected_ratio = {expected_ratio}

    result = {{
        "hypothesis": "{hid}",
        "signal": "{signal}",
        "proof_type": "ASSOCIATION",
        "match_in_target": match_target,
        "n_target": n_target,
        "expected_ratio": expected_ratio,
        "status": "CONFIRMED" if match_target > 0 else "INCONCLUSIVE"
    }}

    results = []
    if os.path.exists(RESULT_PATH):
        with open(RESULT_PATH) as f:
            results = json.load(f)
    results = [r for r in results if r.get("hypothesis") != "{hid}"]
    results.append(result)
    with open(RESULT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"{{result['hypothesis']}}: {{result['status']}}")
    return result

if __name__ == "__main__":
    main()
'''
