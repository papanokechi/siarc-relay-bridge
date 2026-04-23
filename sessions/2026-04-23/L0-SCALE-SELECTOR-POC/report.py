"""
Output formatter for scale selector reports.
"""
import json
import hashlib
import math
from datetime import datetime, timezone


def structural_check_family(a_coeffs, b_coeffs, K_str, pslq_result):
    """
    Check structural signatures for a confirmed Trans family at d=3.
    Compare with known d=2 patterns.
    """
    a = [int(c) for c in a_coeffs]
    b = [int(c) for c in b_coeffs]

    # Degree profile
    a_deg = next((3 - i for i in range(4) if a[i] != 0), 0)
    b_deg = next((3 - i for i in range(4) if b[i] != 0), 0)

    # Cubic discriminant: 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2
    a3, a2, a1, a0 = a
    disc_a = (18*a3*a2*a1*a0 - 4*a2**3*a0 + a2**2*a1**2
              - 4*a3*a1**3 - 27*a3**2*a0**2)
    abs_disc = abs(disc_a)
    sqrt_d = int(math.isqrt(abs_disc)) if abs_disc > 0 else 0
    disc_perfect_sq = (sqrt_d * sqrt_d == abs_disc)

    # Ratio a_lead / b_sublead^2
    a_lead = a[0]
    b_sub = next((c for c in b[1:] if c != 0), 0)
    ratio = float(a_lead) / (float(b_sub)**2) if b_sub != 0 else None

    # PSLQ structure
    rel = pslq_result.get('relation', [])
    c4_zero = (rel[4] == 0) if len(rel) >= 5 else None
    limit_type = 'Mobius_pi' if pslq_result.get('basis') == 'T1' else pslq_result.get('basis')

    return {
        'degree_profile': f"({a_deg},{b_deg})",
        'disc_a': disc_a,
        'disc_perfect_sq': disc_perfect_sq,
        'ratio_a_b': ratio,
        'c4_zero': c4_zero,
        'limit_type': limit_type,
    }


def build_structural_comparison(trans_families):
    """Build the d=2 vs d=3 structural comparison."""
    d2 = {
        "degree_profile": "(2,1) exclusively",
        "disc_a": "perfect square in {0, 1, 9, 25}",
        "ratio_a_lead_b_sublead_sq": "{-2/9, 1/4}",
        "pslq_c4": "always 0 (no pi^2 term)",
        "limit_type": "Mobius transform of pi",
    }

    if not trans_families:
        d3 = {
            "degree_profile": "NOT FOUND (no Trans at d=3)",
            "disc_a": "NOT FOUND",
            "ratio": "NOT FOUND",
            "pslq_c4": "NOT FOUND",
            "limit_type": "NOT FOUND",
        }
        return {"d2_signatures": d2, "d3_signatures": d3,
                "signatures_persist": False,
                "new_signatures": ["No Trans families found at d=3"]}

    profiles = set()
    discs = set()
    ratios = set()
    c4_vals = set()
    types = set()

    for fam in trans_families:
        sc = fam.get('structural', {})
        profiles.add(sc.get('degree_profile', '?'))
        discs.add(sc.get('disc_a', '?'))
        ratios.add(sc.get('ratio_a_b'))
        c4_vals.add(sc.get('c4_zero'))
        types.add(sc.get('limit_type', '?'))

    d3 = {
        "degree_profile": str(profiles),
        "disc_a": str(discs),
        "ratio": str(ratios),
        "pslq_c4": "always 0" if c4_vals == {True} else str(c4_vals),
        "limit_type": str(types),
    }

    # Check if d=2 patterns persist
    persist_checks = []
    # Profile: at d=2 it was (2,1). At d=3 with b_deg < a_deg would be similar
    all_b_lower = all('(' in p and int(p.split(',')[1].strip(')')) < int(p.split('(')[1].split(',')[0])
                       for p in profiles if '(' in p)
    persist_checks.append(all_b_lower)
    # disc_a perfect square
    all_sq = all(fam.get('structural', {}).get('disc_perfect_sq', False)
                 for fam in trans_families)
    persist_checks.append(all_sq)

    new_sigs = []
    if not all_b_lower:
        new_sigs.append("Degree profiles differ from d=2 pattern")
    if not all_sq:
        new_sigs.append("disc_a is not always a perfect square")

    return {
        "d2_signatures": d2,
        "d3_signatures": d3,
        "signatures_persist": all(persist_checks),
        "new_signatures": new_sigs if new_sigs else ["Patterns consistent with d=2"],
    }


def build_report(task_id, D_searched, D_min, trans_families,
                 families_enumerated, families_screened, families_pslq,
                 structural_comparison, runtime):
    """Build the main JSON report."""
    screening_total = sum(families_enumerated.values())
    screening_removed = sum(families_enumerated.values()) - sum(families_pslq.values())
    eff = f"{100*screening_removed/max(screening_total,1):.1f}%"

    trans_list = []
    for fam in trans_families:
        trans_list.append({
            "D": fam['D'],
            "a": fam['a'],
            "b": fam['b'],
            "K_approx": fam['K_approx'],
            "pslq_relation": fam.get('pslq_relation'),
            "residual": fam.get('residual'),
            "degree_profile": fam.get('structural', {}).get('degree_profile'),
            "disc_a": fam.get('structural', {}).get('disc_a'),
            "ratio_a_b": fam.get('structural', {}).get('ratio_a_b'),
        })

    key_finding = ""
    if trans_families:
        key_finding = (f"D_min = {D_min}: found {len(trans_families)} Trans families "
                       f"at d=3, D={D_min}.")
    else:
        key_finding = (f"No Trans families found at d=3 for D in {D_searched}. "
                       f"D_min > {max(D_searched)}.")

    return {
        "task_id": task_id,
        "date": datetime.now(timezone.utc).isoformat(),
        "target_phenomenon": "Trans-stratum families",
        "fixed_degree": 3,
        "D_values_searched": D_searched,
        "D_min": D_min,
        "trans_families_found": trans_list,
        "structural_comparison": structural_comparison,
        "families_enumerated": families_enumerated,
        "families_screened": families_screened,
        "families_pslq_tested": families_pslq,
        "screening_efficiency": eff,
        "runtime_seconds": round(runtime, 1),
        "key_finding": key_finding,
    }


def format_markdown(report):
    """Format report as markdown."""
    lines = []
    lines.append("# Scale Selector Report: F(3,D) Trans Search")
    lines.append(f"**Task:** {report['task_id']}")
    lines.append(f"**Date:** {report['date']}")
    lines.append(f"**Runtime:** {report['runtime_seconds']}s")
    lines.append("")

    lines.append("## 1. Search Summary")
    lines.append(f"- **Fixed degree:** d={report['fixed_degree']}")
    lines.append(f"- **D values searched:** {report['D_values_searched']}")
    lines.append(f"- **D_min:** {report['D_min'] or 'NOT FOUND'}")
    lines.append(f"- **Screening efficiency:** {report['screening_efficiency']}")
    lines.append("")

    for D_str, count in report['families_enumerated'].items():
        pslq_count = report['families_pslq_tested'].get(D_str, 0)
        lines.append(f"  - {D_str}: {count:,} enumerated, "
                     f"{pslq_count:,} PSLQ-tested")
    lines.append("")

    lines.append("## 2. Trans Families Found")
    if report['trans_families_found']:
        for fam in report['trans_families_found']:
            lines.append(f"\n### Family at D={fam['D']}")
            lines.append(f"- a = {fam['a']}, b = {fam['b']}")
            lines.append(f"- K = {fam['K_approx']}")
            lines.append(f"- PSLQ relation: {fam['pslq_relation']}")
            lines.append(f"- Residual: {fam['residual']}")
            lines.append(f"- Degree profile: {fam['degree_profile']}")
            lines.append(f"- disc_a: {fam['disc_a']}")
            lines.append(f"- a_lead/b_sub^2: {fam['ratio_a_b']}")
    else:
        lines.append("**No Trans families found.**")
    lines.append("")

    lines.append("## 3. Structural Comparison: d=2 vs d=3")
    sc = report.get('structural_comparison', {})
    lines.append(f"- **Signatures persist:** {sc.get('signatures_persist', 'N/A')}")
    if sc.get('new_signatures'):
        for s in sc['new_signatures']:
            lines.append(f"  - {s}")
    lines.append("")

    lines.append("## 4. Key Finding")
    lines.append(f"> {report['key_finding']}")
    lines.append("")

    if not report['trans_families_found']:
        lines.append("## 5. Recommended Next D")
        max_D = max(report['D_values_searched']) if report['D_values_searched'] else 0
        lines.append(f"Search D={max_D+1} with aggressive pre-screening, "
                     f"or expand to d=3 with targeted coefficient ranges.")
    lines.append("")

    return "\n".join(lines)


def write_claims(report, filepath):
    """Write AEAL claims."""
    report_json = json.dumps(report, indent=2)
    output_hash = hashlib.sha256(report_json.encode()).hexdigest()

    claims = []
    for fam in report.get('trans_families_found', []):
        claims.append({
            "claim": (f"Trans family at d=3 D={fam['D']}: "
                      f"a={fam['a']}, b={fam['b']}, K~{fam['K_approx'][:20]}"),
            "evidence_type": "computation",
            "dps": 150,
            "reproducible": True,
            "script": "scale_selector.py",
            "output_hash": output_hash,
        })

    D_min = report.get('D_min')
    if D_min is not None:
        claims.append({
            "claim": f"D_min = {D_min} for Trans-stratum at d=3",
            "evidence_type": "computation",
            "dps": 150,
            "reproducible": True,
            "script": "scale_selector.py",
            "output_hash": output_hash,
        })

    for D in report.get('D_values_searched', []):
        D_str = f"D={D}"
        n_pslq = report['families_pslq_tested'].get(D_str, 0)
        n_trans = sum(1 for f in report.get('trans_families_found', []) if f['D'] == D)
        if n_trans == 0:
            claims.append({
                "claim": (f"No Trans found at d=3 D={D}: "
                          f"{n_pslq} families PSLQ-tested"),
                "evidence_type": "computation",
                "dps": 150,
                "reproducible": True,
                "script": "scale_selector.py",
                "output_hash": output_hash,
            })

    if not claims:
        claims.append({
            "claim": "Scale selector search completed; see report",
            "evidence_type": "computation",
            "dps": 150,
            "reproducible": True,
            "script": "scale_selector.py",
            "output_hash": output_hash,
        })

    with open(filepath, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c) + "\n")

    return claims
