"""Cycle 3b (R1-ROUTE-F-K-PERP-QUOTIENT-LATTICE) verification tests.

Pre-registered AEAL discipline: the synthesizer's expected verdict
is declared at the TOP of this file BEFORE any computation runs.
The test `test_pre_registered_verdict_alignment` records whether
the actual verdict matches; falsification of the pre-registered
verdict is NOT a test failure (it's a legitimate verdict-branch
resolution to a different allowed branch) but IS reported via
the test parametrisation and the cycle's `unexpected_finds.json`.

The actual hard assertions enforced here are the synthesizer's
defensive-flag and signature-envelope constraints:

  - Quotient has rank 2 (torsion-free abelian).
  - The Z-basis lifts to K_X^perp (each pairing with -K_X is zero).
  - The Z-basis is PRIMITIVE in Z^9 (saturated lift).
  - -K_X projects to zero in the quotient.
  - Gram(Q) is symmetric and integer.
  - Signature (p, n, z) satisfies p in {0, 1} and n in {0, 1, 2}.
  - Verdict is one of the five enumerated branches.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from sakai_d6.surface import (
    DIM_PIC,
    GRAM_PIC,
    anti_canonical,
    intersect,
)
from sakai_d6.saturation import (
    K_PERP_BASIS,
    RANK_K_PERP,
    RANK_KNY,
    kny_in_k_perp_coords,
)
from sakai_d6.quotient import (
    EXPECTED_DIVISORS_FROM_CYCLE2,
    RANK_L_DELTA,
    RANK_Q,
    k_perp_quotient_basis,
    quotient_basis_in_pic_coords,
    quotient_classification,
    quotient_discriminant,
    quotient_gram_matrix,
    quotient_signature,
    verify_elementary_divisors_match_cycle2,
    verify_gram_is_symmetric,
    verify_minus_K_X_projects_to_zero,
    verify_quotient_basis_is_in_k_perp,
    verify_quotient_basis_is_primitive,
    verify_report,
    verify_signature_within_pic_envelope,
    verify_snf_decomp_holds,
    _snf_decomposition,
    _write_artefacts,
)


# ---------------------------------------------------------------------------
# Pre-registered expectations (declared BEFORE computing)
# ---------------------------------------------------------------------------
#
# Per the synthesizer's cycle-3b brief, the pre-registered verdict is:
#
#     Q_LORENTZIAN  (signature (1, 1, 0), discriminant in {-1, -4})
#
# This pre-registration is based on the synthesizer's signature
# accounting:
#
#     Pic signature (1, 9)
#     -> K_X^perp / <-K_X>  (synthesizer claimed (1, 7))
#     -> Q = quotient by L_delta / <-K_X>  (negative-definite rank 6)
#     -> Q signature (1, 7) - (0, 6) = (1, 1)
#
# These are declared here for the cycle-3b record. If the actual
# computed verdict differs, it is recorded in
# `unexpected_finds.json` and the AEAL claim file's `actual_*`
# block, but the test suite still PASSES because the actual
# verdict is one of the five allowed branches and the defensive
# flags hold.

PREREGISTERED_VERDICT = "Q_LORENTZIAN"
PREREGISTERED_SIGNATURE = (1, 1, 0)
PREREGISTERED_DISCRIMINANT_CANDIDATES = (-1, -4)

ALLOWED_VERDICTS = (
    "Q_DEFINITE_NEGATIVE",
    "Q_DEFINITE_POSITIVE",
    "Q_LORENTZIAN",
    "Q_DEGENERATE_WITH_ISOTROPIC_LINE",
    "Q_TOTALLY_ISOTROPIC",
)


# ---------------------------------------------------------------------------
# Substrate sanity (cycle-1 and cycle-2 contracts)
# ---------------------------------------------------------------------------


def test_predecessor_kny_in_k_perp_shape() -> None:
    M = kny_in_k_perp_coords()
    assert M.shape == (RANK_KNY, RANK_K_PERP) == (7, 9)


def test_predecessor_k_perp_basis_shape() -> None:
    assert K_PERP_BASIS.shape == (RANK_K_PERP, DIM_PIC) == (9, 10)


def test_predecessor_cycle2_elementary_divisors() -> None:
    """All seven elementary divisors of A = M^T must equal 1."""
    assert verify_elementary_divisors_match_cycle2() is True


def test_snf_decomp_unimodular_identity() -> None:
    """U @ A @ V == D and det(U), det(V) in {-1, +1}."""
    D, U, V, U_inv = _snf_decomposition()
    M_np = kny_in_k_perp_coords()
    from sympy import Matrix
    A = Matrix(M_np.T.tolist())
    assert U * A * V == D
    assert int(U.det()) in (-1, 1)
    assert int(V.det()) in (-1, 1)
    # U_inv * U should be the identity 9x9.
    I9 = (U_inv * U).tolist()
    for i in range(RANK_K_PERP):
        for j in range(RANK_K_PERP):
            expected = 1 if i == j else 0
            assert int(I9[i][j]) == expected, f"U_inv * U mismatch at ({i},{j})"


def test_snf_decomp_holds_flag() -> None:
    assert verify_snf_decomp_holds() is True


# ---------------------------------------------------------------------------
# Quotient rank, basis, and primitivity
# ---------------------------------------------------------------------------


def test_quotient_rank_is_two() -> None:
    """The quotient Q has rank 9 - 7 = 2."""
    assert RANK_Q == 2
    assert RANK_L_DELTA == 7
    assert RANK_K_PERP - RANK_L_DELTA == RANK_Q
    Q_kperp = k_perp_quotient_basis()
    assert Q_kperp.shape == (RANK_Q, RANK_K_PERP) == (2, 9)
    # Z-rank of the 2x9 matrix is exactly 2.
    rank = int(np.linalg.matrix_rank(Q_kperp.astype(np.float64)))
    assert rank == RANK_Q


def test_quotient_basis_is_in_k_perp() -> None:
    """Each q_k is orthogonal to -K_X under the Pic form."""
    assert verify_quotient_basis_is_in_k_perp() is True
    Q_pic = quotient_basis_in_pic_coords()
    k_anti = anti_canonical()
    for v in Q_pic:
        assert intersect(v.astype(np.int64), k_anti) == 0


def test_quotient_basis_in_pic_shape() -> None:
    Q_pic = quotient_basis_in_pic_coords()
    assert Q_pic.shape == (RANK_Q, DIM_PIC) == (2, 10)


def test_quotient_basis_is_primitive() -> None:
    """The lift (q_1, q_2) generates a SATURATED rank-2 sublattice of Z^9."""
    assert verify_quotient_basis_is_primitive() is True


def test_quotient_basis_reconstructs_via_K_perp() -> None:
    """Q_pic == Q_kperp @ K_PERP_BASIS (definitional sanity)."""
    Q_kperp = k_perp_quotient_basis()
    Q_pic = quotient_basis_in_pic_coords()
    assert np.array_equal(Q_kperp @ K_PERP_BASIS, Q_pic)


# ---------------------------------------------------------------------------
# -K_X projects to zero in Q
# ---------------------------------------------------------------------------


def test_minus_K_projects_to_zero() -> None:
    """-K_X, lifted to K_X^perp coords, has zero image in Q."""
    assert verify_minus_K_X_projects_to_zero() is True


def test_minus_K_is_in_L_delta_explicitly() -> None:
    """Cross-check: there exist integers c_0..c_6 with
    sum c_i delta_i = -K_X in K_X^perp coords.

    Solve the 9-dim linear system over Q (will be exact because
    the predecessor cycle proved the saturation).
    """
    M = kny_in_k_perp_coords()  # 7 x 9
    free_idx = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    kfree = anti_canonical()[free_idx].astype(np.int64)
    # Solve c @ M == kfree, i.e. M^T @ c^T == kfree.
    from sympy import Matrix
    A = Matrix(M.T.tolist())  # 9 x 7
    rhs = Matrix(kfree.tolist())
    # Sympy solve.
    aug = A.row_join(rhs)
    rref, pivots = aug.rref()
    # The last column of the RREF (restricted to the leading rows)
    # gives c. Since the system is consistent (cycle-2 saturation),
    # there must be no inconsistent row.
    for r in range(rref.rows):
        row = rref.row(r)
        if all(row[c] == 0 for c in range(7)) and row[7] != 0:
            pytest.fail(
                f"System -K_X = sum c_i delta_i is inconsistent in row {r}: "
                f"{[int(x) for x in row]}"
            )


# ---------------------------------------------------------------------------
# Gram matrix
# ---------------------------------------------------------------------------


def test_quotient_gram_is_symmetric() -> None:
    G = quotient_gram_matrix()
    assert G.shape == (RANK_Q, RANK_Q) == (2, 2)
    assert int(G[0, 1]) == int(G[1, 0])
    assert verify_gram_is_symmetric() is True


def test_quotient_gram_is_integer() -> None:
    G = quotient_gram_matrix()
    for i in range(2):
        for j in range(2):
            v = G[i, j]
            assert isinstance(v, (int, np.integer)), f"Gram[{i},{j}] = {v} ({type(v)})"


def test_quotient_gram_matches_pic_form_directly() -> None:
    """Cross-check: G[i,j] = <q_i, q_j>_Pic by direct intersect()."""
    G = quotient_gram_matrix()
    Q_pic = quotient_basis_in_pic_coords()
    for i in range(2):
        for j in range(2):
            expected = intersect(
                Q_pic[i].astype(np.int64),
                Q_pic[j].astype(np.int64),
            )
            assert int(G[i, j]) == expected, (
                f"Gram[{i},{j}] = {int(G[i, j])} but direct intersect = {expected}"
            )


# ---------------------------------------------------------------------------
# Discriminant and signature
# ---------------------------------------------------------------------------


def test_quotient_discriminant_matches_det() -> None:
    G = quotient_gram_matrix()
    expected = int(G[0, 0]) * int(G[1, 1]) - int(G[0, 1]) ** 2
    assert quotient_discriminant() == expected


def test_quotient_signature_consistent_with_pic_signature() -> None:
    """Pic signature (1, 9): the rank-2 quotient must have p in {0, 1}
    and n in {0, 1, 2}.
    """
    p, n, z = quotient_signature()
    assert p in (0, 1), f"Signature p={p} outside Pic envelope {{0, 1}}"
    assert n in (0, 1, 2), f"Signature n={n} outside Pic envelope {{0, 1, 2}}"
    assert p + n + z == RANK_Q
    assert verify_signature_within_pic_envelope() is True


def test_quotient_classification_matches_verdict_branch() -> None:
    """The verdict resolves to exactly one of the five enumerated branches."""
    verdict = quotient_classification()
    assert verdict in ALLOWED_VERDICTS, (
        f"Verdict {verdict!r} not in allowed branches {ALLOWED_VERDICTS!r}"
    )


def test_signature_and_verdict_internally_consistent() -> None:
    """The (p, n, z) tuple and the verdict label must agree."""
    p, n, z = quotient_signature()
    verdict = quotient_classification()
    if verdict == "Q_DEFINITE_NEGATIVE":
        assert (p, n, z) == (0, 2, 0)
    elif verdict == "Q_DEFINITE_POSITIVE":
        assert (p, n, z) == (2, 0, 0)
    elif verdict == "Q_LORENTZIAN":
        assert (p, n, z) == (1, 1, 0)
    elif verdict == "Q_DEGENERATE_WITH_ISOTROPIC_LINE":
        assert z == 1 and p + n == 1
    elif verdict == "Q_TOTALLY_ISOTROPIC":
        assert (p, n, z) == (0, 0, 2)
    else:
        pytest.fail(f"Unhandled verdict {verdict!r}")


# ---------------------------------------------------------------------------
# Pre-registration record (does NOT fail the suite if falsified)
# ---------------------------------------------------------------------------


def test_pre_registered_verdict_alignment_recorded() -> None:
    """Record alignment with the synthesizer's pre-registered verdict.

    Per the cycle-3b brief: "If the verdict is anything other than
    `Q_LORENTZIAN`, that's a finding worth recording prominently."
    This test ALWAYS PASSES; it merely captures the comparison for
    the cycle's `unexpected_finds.json` record. The actual
    pre-registration vs. actual gap is enforced as a soft
    diagnostic, not a hard assertion.
    """
    actual_verdict = quotient_classification()
    actual_signature = quotient_signature()
    actual_disc = quotient_discriminant()
    # Soft logging: print to stdout (captured by pytest -s).
    if actual_verdict != PREREGISTERED_VERDICT:
        print(
            f"\n[cycle-3b verdict-branch resolution] "
            f"PRE-REGISTERED={PREREGISTERED_VERDICT} (sig {PREREGISTERED_SIGNATURE}, "
            f"disc in {PREREGISTERED_DISCRIMINANT_CANDIDATES}); "
            f"ACTUAL={actual_verdict} (sig {actual_signature}, disc {actual_disc})."
        )
    # The test passes regardless: the cycle records the resolution
    # in the AEAL claim and unexpected_finds artefacts.
    assert actual_verdict in ALLOWED_VERDICTS


# ---------------------------------------------------------------------------
# Aggregate report and artefact emission
# ---------------------------------------------------------------------------


def test_verify_report_all_flags_true() -> None:
    rep = verify_report()
    flag_keys = (
        "snf_decomp_holds",
        "elementary_divisors_match_cycle2",
        "quotient_basis_is_in_k_perp",
        "quotient_basis_is_primitive",
        "minus_K_X_projects_to_zero",
        "gram_is_symmetric",
        "signature_within_pic_envelope",
    )
    for k in flag_keys:
        assert rep[k] is True, f"verify_report() flag {k!r} is not True: {rep[k]}"
    assert rep["verdict"] in ALLOWED_VERDICTS


def test_artefact_emission(tmp_path: Path) -> None:
    """`_write_artefacts` produces well-formed verdict and provenance JSON."""
    rep = verify_report()
    _write_artefacts(rep, tmp_path)

    verdict_path = tmp_path / "quotient_verdict.json"
    provenance_path = tmp_path / "quotient_basis_provenance.json"
    assert verdict_path.exists()
    assert provenance_path.exists()

    verdict_data = json.loads(verdict_path.read_text())
    assert verdict_data["verdict"] in ALLOWED_VERDICTS
    assert verdict_data["rank_q"] == RANK_Q
    assert verdict_data["all_flags_ok"] is True
    assert isinstance(verdict_data["discriminant"], int)
    assert isinstance(verdict_data["signature_p_n_z"], list)
    assert len(verdict_data["signature_p_n_z"]) == 3

    provenance_data = json.loads(provenance_path.read_text())
    assert provenance_data["A_shape"] == [RANK_K_PERP, RANK_KNY]
    assert provenance_data["elementary_divisors_of_A"] == list(EXPECTED_DIVISORS_FROM_CYCLE2)
    assert provenance_data["predecessor_cycle2_commit"] == "139fa8b"
    assert provenance_data["predecessor_cycle3a_commit"] == "baf650a"
    assert len(provenance_data["quotient_basis_in_k_perp_coords"]) == RANK_Q
    assert len(provenance_data["quotient_basis_in_pic_coords"]) == RANK_Q
