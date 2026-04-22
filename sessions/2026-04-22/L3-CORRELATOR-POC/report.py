"""
Report generator: produces enrichment_report.md and enrichment_report.json.
"""

import json
import os


def _fmt_value(v):
    """Format a parameter value for display."""
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, float):
        return "%.4f" % v
    return str(v)


def _fmt_pvalue(p):
    if p < 1e-10:
        return "<1e-10"
    if p < 0.001:
        return "%.1e" % p
    return "%.4f" % p


def _interpret(r):
    """Generate plain-English interpretation of an enrichment result."""
    param = r['parameter']
    stratum = r['stratum']
    val = _fmt_value(r['value'])
    er = r['enrichment_ratio']

    # Specific interpretations for known parameters
    if param == 'b2_is_zero' and r['value'] is True:
        return (
            "%s=%s is %.1fx enriched in %s vs full space (p=%s): "
            "%s families are strongly concentrated in degree-(a,<=1) "
            "b-profiles (linear or constant b)."
            % (param, val, er, stratum, _fmt_pvalue(r['p_value']), stratum)
        )
    if param == 'a_eval_1_is_zero' and r['value'] is True:
        return (
            "%s=%s is %.1fx enriched in %s vs full space (p=%s): "
            "a(1)=0 causes the CF to terminate, yielding rational values "
            "(trivial-zero mechanism)."
            % (param, val, er, stratum, _fmt_pvalue(r['p_value']), )
        )
    if param == 'degree_profile':
        return (
            "degree_profile=%s is %.1fx enriched in %s vs full space (p=%s): "
            "%s families prefer this (a_deg, b_deg) combination."
            % (val, er, stratum, _fmt_pvalue(r['p_value']), stratum)
        )

    return (
        "%s=%s is %.1fx enriched in %s vs full space (p=%s)."
        % (param, val, er, stratum, _fmt_pvalue(r['p_value']))
    )


def write_reports(
    discovery, strong, null_params, categorical_results,
    continuous_results, stratum_counts, output_dir
):
    """Write enrichment_report.md and enrichment_report.json."""

    md_path = os.path.join(output_dir, 'enrichment_report.md')
    json_path = os.path.join(output_dir, 'enrichment_report.json')

    lines = []
    lines.append("# PCF Cross-Family Correlator — Enrichment Report\n")

    # --- Summary ---
    lines.append("## Summary\n")
    total = sum(stratum_counts.values())
    strata_str = ", ".join(
        "%s (%d)" % (s, c) for s, c in sorted(stratum_counts.items())
    )
    lines.append("- **Strata**: %s" % strata_str)
    lines.append("- **Total families**: %d" % total)
    lines.append("- **Parameters extracted**: 21 (Groups A-F)")
    lines.append("- **Categorical parameters**: 15")
    lines.append("- **Continuous parameters**: 6")
    lines.append("- **Discovery candidates**: %d" % len(discovery))
    lines.append("- **Strong signals**: %d" % len(strong))
    lines.append("- **Null-result parameters**: %d" % len(null_params))
    lines.append("")

    # --- Discovery Candidates ---
    lines.append("## Discovery Candidates (enrichment > 5, p < 0.001)\n")
    if not discovery:
        lines.append("*None found.*\n")
    else:
        for r in sorted(discovery, key=lambda x: -x['enrichment_ratio']):
            lines.append("### %s = %s in %s" % (
                r['parameter'], _fmt_value(r['value']), r['stratum']))
            lines.append("")
            lines.append("| Metric | Value |")
            lines.append("|--------|-------|")
            lines.append("| Enrichment ratio | %.2f |" % r['enrichment_ratio'])
            lines.append("| p-value | %s |" % _fmt_pvalue(r['p_value']))
            lines.append("| Count in stratum | %d / %d |" % (
                r['count_stratum'], r['n_stratum']))
            lines.append("| Count in full space | %d / %d |" % (
                r['count_all'], r['n_all']))
            lines.append("")
            lines.append("**Interpretation**: %s" % _interpret(r))
            lines.append("")

    # --- Strong Signals ---
    lines.append("## Strong Signals (enrichment 3-5, p < 0.01)\n")
    if not strong:
        lines.append("*None found.*\n")
    else:
        for r in sorted(strong, key=lambda x: -x['enrichment_ratio']):
            lines.append("### %s = %s in %s" % (
                r['parameter'], _fmt_value(r['value']), r['stratum']))
            lines.append("")
            lines.append("| Metric | Value |")
            lines.append("|--------|-------|")
            lines.append("| Enrichment ratio | %.2f |" % r['enrichment_ratio'])
            lines.append("| p-value | %s |" % _fmt_pvalue(r['p_value']))
            lines.append("| Count in stratum | %d / %d |" % (
                r['count_stratum'], r['n_stratum']))
            lines.append("| Count in full space | %d / %d |" % (
                r['count_all'], r['n_all']))
            lines.append("")
            lines.append("**Interpretation**: %s" % _interpret(r))
            lines.append("")

    # --- Full Enrichment Table ---
    lines.append("## Full Enrichment Table\n")
    lines.append("| Parameter | Stratum | Value | Count (S) | Count (all) "
                 "| Enrichment | p-value |")
    lines.append("|-----------|---------|-------|-----------|-------------|"
                 "------------|---------|")
    for r in sorted(categorical_results,
                    key=lambda x: (x['parameter'], x['stratum'], str(x['value']))):
        lines.append("| %s | %s | %s | %d/%d | %d/%d | %.2f | %s |" % (
            r['parameter'], r['stratum'], _fmt_value(r['value']),
            r['count_stratum'], r['n_stratum'],
            r['count_all'], r['n_all'],
            r['enrichment_ratio'],
            _fmt_pvalue(r['p_value']),
        ))
    lines.append("")

    # --- Continuous Parameters ---
    if continuous_results:
        lines.append("## Continuous Parameter Summary\n")
        lines.append("| Parameter | Stratum | n | Mean | Std | Min | Max "
                     "| Global Mean | Deviation (σ) | Flagged |")
        lines.append("|-----------|---------|---|------|-----|-----|-----"
                     "|-------------|---------------|---------|")
        for r in sorted(continuous_results,
                        key=lambda x: (x['parameter'], x['stratum'])):
            lines.append(
                "| %s | %s | %d | %.4f | %.4f | %s | %s | %.4f | %.2f | %s |"
                % (
                    r['parameter'], r['stratum'], r['n'],
                    r['mean'], r['std'], r['min'], r['max'],
                    r['global_mean'], r['deviation_sigma'],
                    "**YES**" if r['flagged'] else "no",
                )
            )
        lines.append("")

    # --- Null Results ---
    lines.append("## Null Results\n")
    lines.append("Parameters with enrichment ratio 0.8–1.2 across all strata "
                 "(no differential signal):\n")
    if null_params:
        for p in sorted(null_params):
            lines.append("- `%s`" % p)
    else:
        lines.append("*All parameters show some enrichment variation.*")
    lines.append("")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    # --- JSON report ---
    report_json = {
        'summary': {
            'strata': dict(stratum_counts),
            'total_families': total,
            'n_parameters': 21,
            'n_discovery_candidates': len(discovery),
            'n_strong_signals': len(strong),
            'n_null_params': len(null_params),
        },
        'discovery_candidates': _serialize_results(discovery),
        'strong_signals': _serialize_results(strong),
        'null_result_params': sorted(null_params),
        'categorical_enrichment': _serialize_results(categorical_results),
        'continuous_summary': _serialize_continuous(continuous_results),
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report_json, f, indent=2, default=str)

    return md_path, json_path


def _serialize_results(results):
    out = []
    for r in results:
        d = dict(r)
        # Convert booleans and tuples to strings for JSON compatibility
        d['value'] = _fmt_value(d['value']) if 'value' in d else None
        out.append(d)
    return out


def _serialize_continuous(results):
    return [dict(r) for r in results]
