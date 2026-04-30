# Extracted T0/T1 classification rules

_From DecisionTreeClassifier(max_depth=6); holdout 100 families._

- Holdout accuracy: **1.0000**
- Holdout AUC: **1.0000**
- Gradient-boosted accuracy: **1.0000** (AUC 1.0000)

## Pure leaves (purity ≥ 0.99) ranked by support

| Rule | predicts | n_total | n_T0 | n_T1 | purity |
|---|---|---:|---:|---:|---:|

## All leaves (sorted by purity)

| Rule | predicts | n_total | n_T0 | n_T1 | purity |
|---|---|---:|---:|---:|---:|
| `disc_a_psq > 0.5 AND conv_slope > 0.1475` | T1 | 17 | 0 | 1 | 0.059 |
| `disc_a_psq <= 0.5` | T1 | 143 | 0 | 1 | 0.007 |
| `disc_a_psq > 0.5 AND conv_slope <= 0.1475` | T0 | 240 | 1 | 0 | 0.004 |

## Top-3 candidate Lemmas (highest-support pure leaves)


## Feature importance (decision tree)

| Feature | importance |
|---|---:|
| `disc_a_psq` | 0.8346 |
| `conv_slope` | 0.1654 |
| `deg_a` | 0.0000 |
| `deg_b` | 0.0000 |
| `R_struct` | 0.0000 |
| `disc_a` | 0.0000 |
| `disc_a_neg` | 0.0000 |
| `BT_disc` | 0.0000 |
| `lam_ratio` | 0.0000 |
| `int_resonance` | 0.0000 |
| `stokes_idx` | 0.0000 |
| `r_final_log10` | 0.0000 |
| `finite_termination` | 0.0000 |

---

## Companion analysis: F(2,4)-only (deg_pair held constant)

Subset: 324 families (300 T0 Rat, 24 T1 Trans).  5-fold stratified CV.

- DT mean accuracy: **1.0000** (±0.0000); AUC 1.0000
- GBM mean accuracy: **1.0000** (±0.0000); AUC 1.0000
- Pooled DT CV confusion [[TN=300, FP=0], [FN=0, TP=24]]

### F(2,4)-only leaf rules (full fit)

| Rule | predicts | n | T0 | T1 | purity |
|---|---|---:|---:|---:|---:|
| `conv_slope > 0.1475` | T1 | 24 | 0 | 1 | 0.042 |
| `conv_slope <= 0.1475` | T0 | 300 | 1 | 0 | 0.003 |