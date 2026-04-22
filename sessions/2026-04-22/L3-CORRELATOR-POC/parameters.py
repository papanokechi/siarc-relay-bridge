"""
Parameter extractor for PCF families.
Groups A-F: degree profile, leading signs, zero structure,
coefficient ratios, discriminants, structural triggers.
"""

import math


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def extract_parameters(family):
    """Extract all 21 parameters from a PCF family dict.

    Args:
        family: dict with 'a': [a0, a1, a2], 'b': [b0, b1, b2]

    Returns:
        dict mapping parameter name -> value
    """
    a2, a1, a0 = family['a']  # certificate stores [a2, a1, a0]
    b2, b1, b0 = family['b']

    # GROUP A — Degree profile
    a_degree = 2 if a2 != 0 else (1 if a1 != 0 else 0)
    b_degree = 2 if b2 != 0 else (1 if b1 != 0 else 0)
    degree_profile = "(%d,%d)" % (a_degree, b_degree)

    # GROUP B — Leading coefficient signs
    sign_a2 = sign(a2)
    sign_b2 = sign(b2)
    sign_a2_b2 = sign(a2) * sign(b2)

    # GROUP C — Zero structure
    a0_is_zero = (a0 == 0)
    b0_is_zero = (b0 == 0)
    a1_is_zero = (a1 == 0)
    b1_is_zero = (b1 == 0)
    a2_is_zero = (a2 == 0)
    b2_is_zero = (b2 == 0)

    # GROUP D — Coefficient ratios
    a2_over_b1sq = a2 / (b1 * b1) if b1 != 0 else None
    a1_over_b1 = a1 / b1 if b1 != 0 else None
    a0_over_b0 = a0 / b0 if b0 != 0 else None

    # GROUP E — Discriminants
    disc_a = a1 * a1 - 4 * a2 * a0
    disc_b = b1 * b1 - 4 * b2 * b0
    sign_disc_a = sign(disc_a)
    sign_disc_b = sign(disc_b)

    # GROUP F — Rat-stratum structural triggers
    a_eval_1 = a2 + a1 + a0
    a_eval_1_is_zero = (a_eval_1 == 0)

    return {
        # Group A
        'a_degree': a_degree,
        'b_degree': b_degree,
        'degree_profile': degree_profile,
        # Group B
        'sign_a2': sign_a2,
        'sign_b2': sign_b2,
        'sign_a2_b2': sign_a2_b2,
        # Group C
        'a0_is_zero': a0_is_zero,
        'b0_is_zero': b0_is_zero,
        'a1_is_zero': a1_is_zero,
        'b1_is_zero': b1_is_zero,
        'a2_is_zero': a2_is_zero,
        'b2_is_zero': b2_is_zero,
        # Group D
        'a2_over_b1sq': a2_over_b1sq,
        'a1_over_b1': a1_over_b1,
        'a0_over_b0': a0_over_b0,
        # Group E
        'disc_a': disc_a,
        'disc_b': disc_b,
        'sign_disc_a': sign_disc_a,
        'sign_disc_b': sign_disc_b,
        # Group F
        'a_eval_1': a_eval_1,
        'a_eval_1_is_zero': a_eval_1_is_zero,
    }


# Classification of parameters
CATEGORICAL_PARAMS = [
    'a_degree', 'b_degree', 'degree_profile',
    'sign_a2', 'sign_b2', 'sign_a2_b2',
    'a0_is_zero', 'b0_is_zero', 'a1_is_zero', 'b1_is_zero',
    'a2_is_zero', 'b2_is_zero',
    'sign_disc_a', 'sign_disc_b',
    'a_eval_1_is_zero',
]

CONTINUOUS_PARAMS = [
    'a2_over_b1sq', 'a1_over_b1', 'a0_over_b0',
    'disc_a', 'disc_b', 'a_eval_1',
]
