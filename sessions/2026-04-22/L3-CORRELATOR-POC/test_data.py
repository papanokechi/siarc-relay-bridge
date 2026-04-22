"""
Minimal test fixture for the correlator pipeline.
Generates synthetic families with known enrichment patterns.
"""


def make_test_data():
    """Return a list of (family, stratum) records for testing.

    Known enrichments baked in:
    - All Trans families have b2=0 (b2_is_zero enriched in Trans)
    - All Rat families have a_eval_1=0 (a_eval_1_is_zero enriched in Rat)
    - Trans families all have degree_profile (2,1)
    """
    records = []

    # 10 Rat families: a(1)=a2+a1+a0=sum(a)=0, b2!=0
    # Coefficient order: [a2, a1, a0] — a(n)=a2*n^2+a1*n+a0
    rat_families = [
        {'a': [1, -2, 1], 'b': [3, 2, 1]},   # 1-2+1=0
        {'a': [1, -3, 2], 'b': [4, 1, 2]},   # 1-3+2=0
        {'a': [1, 0, -1], 'b': [1, 2, 3]},   # 1+0-1=0
        {'a': [-1, 1, 0], 'b': [2, 3, 1]},   # -1+1+0=0
        {'a': [1, -4, 3], 'b': [2, 2, 2]},   # 1-4+3=0
        {'a': [1, 1, -2], 'b': [1, 1, 1]},   # 1+1-2=0
        {'a': [-1, -3, 4], 'b': [3, 3, 3]},  # -1-3+4=0
        {'a': [1, 2, -3], 'b': [2, 1, 4]},   # 1+2-3=0
        {'a': [-2, 1, 1], 'b': [1, 4, 2]},   # -2+1+1=0
        {'a': [-3, 1, 2], 'b': [1, 2, 1]},   # -3+1+2=0
    ]
    for fam in rat_families:
        records.append({'family': fam, 'stratum': 'Rat'})

    # 5 Trans families: b2=b[0]=0, a2!=0, degree_profile (2,1)
    # Coefficient order: [b2, b1, b0]
    trans_families = [
        {'a': [-1, -3, -2], 'b': [0, -3, -4]},
        {'a': [3, 2, 1], 'b': [0, 4, 1]},
        {'a': [-2, 3, -1], 'b': [0, 2, 1]},
        {'a': [4, -1, 2], 'b': [0, -1, 3]},
        {'a': [2, 1, -3], 'b': [0, 3, 2]},
    ]
    for fam in trans_families:
        records.append({'family': fam, 'stratum': 'Trans'})

    # 20 Des families: generic, b2(=b[0])!=0, a_eval_1 != 0
    des_families = [
        {'a': [3, 2, 1], 'b': [3, 2, 1]},
        {'a': [4, 3, 2], 'b': [4, 3, 2]},
        {'a': [-3, 2, -1], 'b': [3, -2, 1]},
        {'a': [2, 1, 3], 'b': [1, 2, 4]},
        {'a': [1, 4, -2], 'b': [2, 1, 3]},
        {'a': [3, -1, 4], 'b': [1, 4, 2]},
        {'a': [-2, 3, 1], 'b': [4, 1, 1]},
        {'a': [4, 2, -3], 'b': [1, 3, 2]},
        {'a': [3, -4, 2], 'b': [4, 2, 1]},
        {'a': [-1, 2, 3], 'b': [3, 1, 4]},
        {'a': [2, 1, -4], 'b': [2, 4, 3]},
        {'a': [4, -3, 1], 'b': [3, 1, 2]},
        {'a': [-3, 2, 4], 'b': [4, 3, 1]},
        {'a': [2, 4, -1], 'b': [3, 2, 4]},
        {'a': [-4, 1, 2], 'b': [1, 4, 3]},
        {'a': [4, -2, 3], 'b': [2, 3, 1]},
        {'a': [1, 3, -4], 'b': [4, 1, 2]},
        {'a': [-3, 4, 1], 'b': [3, 2, 4]},
        {'a': [2, -3, 4], 'b': [4, 2, 3]},
        {'a': [-4, 3, -2], 'b': [3, 4, 1]},
    ]
    for fam in des_families:
        records.append({'family': fam, 'stratum': 'Des'})

    return records


if __name__ == '__main__':
    data = make_test_data()
    from collections import Counter
    strata = Counter(r['stratum'] for r in data)
    print("Test data: %d families" % len(data))
    for s, c in sorted(strata.items()):
        print("  %s: %d" % (s, c))
