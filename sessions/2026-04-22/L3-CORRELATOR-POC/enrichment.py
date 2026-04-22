"""
Enrichment analysis: compare parameter distributions across strata.
Fisher exact test for categorical, z-score for continuous.
"""

from collections import Counter, defaultdict
import math
from scipy import stats


def compute_enrichment_categorical(records, param_name, strata_list):
    """Compute enrichment ratios and p-values for a categorical parameter.

    Args:
        records: list of dicts with 'stratum' and 'params' keys
        param_name: name of the parameter to analyze
        strata_list: list of stratum names

    Returns:
        list of dicts with enrichment results per (stratum, value) pair
    """
    n_all = len(records)
    # Global counts
    global_counts = Counter()
    stratum_counts = defaultdict(Counter)  # stratum -> Counter of values
    stratum_sizes = Counter()

    for rec in records:
        val = rec['params'].get(param_name)
        if val is None:
            continue
        global_counts[val] += 1
        stratum_counts[rec['stratum']][val] += 1
        stratum_sizes[rec['stratum']] += 1

    results = []
    all_values = sorted(global_counts.keys(), key=str)

    for s in strata_list:
        n_s = stratum_sizes[s]
        if n_s == 0:
            continue
        for v in all_values:
            count_s_v = stratum_counts[s][v]
            count_all_v = global_counts[v]

            # Enrichment ratio
            freq_s = count_s_v / n_s if n_s > 0 else 0
            freq_all = count_all_v / n_all if n_all > 0 else 0
            if freq_all == 0:
                enrichment = float('inf') if freq_s > 0 else 1.0
            else:
                enrichment = freq_s / freq_all

            # Fisher exact test
            # Contingency table:
            #              has_v    not_v
            #  in_S        a        b
            #  not_in_S    c        d
            a = count_s_v
            b = n_s - count_s_v
            c = count_all_v - count_s_v
            d = (n_all - n_s) - c

            try:
                _, p_value = stats.fisher_exact([[a, b], [c, d]])
            except ValueError:
                p_value = 1.0

            results.append({
                'parameter': param_name,
                'stratum': s,
                'value': v,
                'count_stratum': count_s_v,
                'count_all': count_all_v,
                'n_stratum': n_s,
                'n_all': n_all,
                'enrichment_ratio': round(enrichment, 4),
                'p_value': p_value,
            })

    return results


def compute_enrichment_continuous(records, param_name, strata_list):
    """Compute summary stats for a continuous parameter per stratum.

    Returns:
        list of dicts with mean, std, min, max, and flag if stratum
        mean deviates > 2 sigma from full-space mean.
    """
    all_vals = []
    stratum_vals = defaultdict(list)

    for rec in records:
        val = rec['params'].get(param_name)
        if val is None:
            continue
        all_vals.append(val)
        stratum_vals[rec['stratum']].append(val)

    if not all_vals:
        return []

    global_mean = sum(all_vals) / len(all_vals)
    global_var = sum((x - global_mean) ** 2 for x in all_vals) / len(all_vals)
    global_std = math.sqrt(global_var) if global_var > 0 else 0

    results = []
    for s in strata_list:
        vals = stratum_vals.get(s, [])
        if not vals:
            continue
        s_mean = sum(vals) / len(vals)
        s_var = sum((x - s_mean) ** 2 for x in vals) / len(vals) if len(vals) > 1 else 0
        s_std = math.sqrt(s_var)

        deviation = abs(s_mean - global_mean) / global_std if global_std > 0 else 0
        flagged = deviation > 2.0

        results.append({
            'parameter': param_name,
            'stratum': s,
            'n': len(vals),
            'mean': round(s_mean, 6),
            'std': round(s_std, 6),
            'min': min(vals),
            'max': max(vals),
            'global_mean': round(global_mean, 6),
            'global_std': round(global_std, 6),
            'deviation_sigma': round(deviation, 4),
            'flagged': flagged,
        })

    return results


def classify_signals(categorical_results):
    """Classify enrichment results into discovery candidates and strong signals.

    Returns:
        (discovery_candidates, strong_signals, null_results)
    """
    discovery = []
    strong = []
    # Track per-parameter: if all enrichments are 0.8-1.2, it's a null result
    param_enrichments = defaultdict(list)

    for r in categorical_results:
        er = r['enrichment_ratio']
        pv = r['p_value']
        param_enrichments[r['parameter']].append(er)

        if er > 5.0 and pv < 0.001:
            discovery.append(r)
        elif er > 3.0 and pv < 0.01:
            strong.append(r)

    null_params = []
    for param, ers in param_enrichments.items():
        if all(0.8 <= e <= 1.2 for e in ers):
            null_params.append(param)

    return discovery, strong, null_params
