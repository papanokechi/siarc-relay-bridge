"""
Pre-screening protocol for d=3 PCF families.
Generates coefficient arrays and applies fast O(1) screens.
"""
import numpy as np
from itertools import product as iprod


def generate_families(D, b_deg_max=None):
    """
    Generate F(3,D) families with a truly degree 3.
    
    If b_deg_max is None, generate ALL families (for small D).
    If b_deg_max is 1, 2, or 3: generate only families with
    b effective degree <= b_deg_max (profile-based, for large D).
    
    Returns a_coeffs (N,4), b_coeffs (N,4) with ordering [c3,c2,c1,c0].
    """
    n = 2 * D + 1

    if b_deg_max is None:
        # Full enumeration: all (2D+1)^8 combos
        total = n ** 8
        idx = np.arange(total, dtype=np.int64)
        coeffs = np.zeros((total, 8), dtype=np.int16)
        for dim in range(7, -1, -1):
            coeffs[:, dim] = (idx % n).astype(np.int16) - D
            idx //= n
        a = coeffs[:, :4]
        b = coeffs[:, 4:]
        mask = (a[:, 0] != 0) & np.any(b != 0, axis=1)
        return a[mask].copy(), b[mask].copy()

    # Profile-based generation
    a3_vals = list(range(-D, 0)) + list(range(1, D + 1))
    a_rest = list(iprod(range(-D, D + 1), repeat=3))
    a_list = np.array([(a3,) + r for a3 in a3_vals for r in a_rest], dtype=np.int16)

    if b_deg_max <= 1:
        # b3=b2=0, (b1,b0) not both zero
        b_list = np.array([(0, 0, b1, b0)
                           for b1 in range(-D, D + 1)
                           for b0 in range(-D, D + 1)
                           if (b1, b0) != (0, 0)], dtype=np.int16)
    elif b_deg_max == 2:
        # b3=0, b2 nonzero
        b2_vals = list(range(-D, 0)) + list(range(1, D + 1))
        b_list = np.array([(0, b2, b1, b0)
                           for b2 in b2_vals
                           for b1 in range(-D, D + 1)
                           for b0 in range(-D, D + 1)], dtype=np.int16)
    else:
        # b3 nonzero
        b3_vals = list(range(-D, 0)) + list(range(1, D + 1))
        b_list = np.array([(b3, b2, b1, b0)
                           for b3 in b3_vals
                           for b2 in range(-D, D + 1)
                           for b1 in range(-D, D + 1)
                           for b0 in range(-D, D + 1)], dtype=np.int16)

    n_a, n_b = len(a_list), len(b_list)
    a_full = np.repeat(a_list, n_b, axis=0)
    b_full = np.tile(b_list, (n_a, 1))
    return a_full, b_full


def screen_rat_structural(a_coeffs, D):
    """
    Screen 1: check if a(k) = 0 for any k in {1, ..., 3D}.
    Returns boolean mask where True = Rat structural (should skip).
    """
    N = len(a_coeffs)
    rat = np.zeros(N, dtype=bool)
    a = a_coeffs.astype(np.int64)
    for k in range(1, 3 * D + 1):
        k2, k3 = k * k, k * k * k
        a_k = a[:, 0] * k3 + a[:, 1] * k2 + a[:, 2] * k + a[:, 3]
        rat |= (a_k == 0)
    return rat


def compute_degree_profiles(a_coeffs, b_coeffs):
    """Compute effective (a_degree, b_degree) for each family."""
    a_deg = np.where(a_coeffs[:, 0] != 0, 3,
            np.where(a_coeffs[:, 1] != 0, 2,
            np.where(a_coeffs[:, 2] != 0, 1, 0)))
    b_deg = np.where(b_coeffs[:, 0] != 0, 3,
            np.where(b_coeffs[:, 1] != 0, 2,
            np.where(b_coeffs[:, 2] != 0, 1, 0)))
    return a_deg, b_deg


def compute_ratio(a_coeffs, b_coeffs):
    """
    Compute a_lead / b_sublead^2 where b_sublead is first nonzero
    among {b2, b1, b0} (coefficients after the leading b3 position).
    """
    a_lead = a_coeffs[:, 0].astype(np.float64)
    b_sub = np.where(b_coeffs[:, 1] != 0, b_coeffs[:, 1],
            np.where(b_coeffs[:, 2] != 0, b_coeffs[:, 2],
                     b_coeffs[:, 3])).astype(np.float64)
    valid = b_sub != 0
    ratio = np.full(len(a_coeffs), np.nan)
    ratio[valid] = a_lead[valid] / (b_sub[valid] ** 2)
    return ratio, valid


def apply_screens(a_coeffs, b_coeffs, D, verbose=True):
    """
    Apply all pre-screens. Returns dict of boolean masks:
      valid:        basic validity (a deg 3, b nonzero)
      rat_struct:   Screen 1 fires
      candidate:    passes all screens, candidate for PSLQ
      ratio:        float array of a_lead/b_sub^2
      a_deg, b_deg: degree profiles
    """
    N = len(a_coeffs)

    # Basic validity (already filtered in generate, but double-check)
    valid = (a_coeffs[:, 0] != 0) & np.any(b_coeffs != 0, axis=1)

    # Screen 1: structural Rat
    rat_struct = screen_rat_structural(a_coeffs, D) & valid

    # Degree profiles
    a_deg, b_deg = compute_degree_profiles(a_coeffs, b_coeffs)

    # Ratio
    ratio, ratio_valid = compute_ratio(a_coeffs, b_coeffs)

    # Candidates: valid, not Rat structural
    candidate = valid & ~rat_struct

    if verbose:
        n_valid = int(valid.sum())
        n_rat = int(rat_struct.sum())
        n_cand = int(candidate.sum())
        print(f"  Screening: {N} total, {n_valid} valid, "
              f"{n_rat} Rat-structural, {n_cand} candidates")

    return {
        'valid': valid,
        'rat_struct': rat_struct,
        'candidate': candidate,
        'ratio': ratio,
        'ratio_valid': ratio_valid,
        'a_deg': a_deg,
        'b_deg': b_deg,
    }
