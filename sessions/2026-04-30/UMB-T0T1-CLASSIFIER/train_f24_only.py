"""
UMB-T0T1-CLASSIFIER — companion analysis: F(2,4)-only stratified.

Restricts to the 324 F(2,4) records (300 Rat + 24 Trans) so that the
deg_pair shape feature is held constant, exposing the genuine internal
T0 vs T1 effective criterion.
"""

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import StratifiedKFold

HERE = Path(__file__).resolve().parent
SEED = 20260430

FEATURE_COLS = [
    "deg_a", "deg_b",
    "R_struct",
    "disc_a", "disc_a_neg", "disc_a_psq",
    "BT_disc", "lam_ratio", "int_resonance",
    "stokes_idx",
    "conv_slope", "r_final_log10", "finite_termination",
]


def main():
    df = pd.read_csv(HERE / "dataset.csv")
    f24 = df[df["source"].str.startswith("F24_")].copy().reset_index(drop=True)
    print(f"F(2,4)-only subset: {len(f24)} rows  "
          f"({(f24['label']=='T0').sum()} T0 / {(f24['label']=='T1').sum()} T1)")

    X = f24[FEATURE_COLS].replace([np.inf, -np.inf], np.nan).fillna(0.0)
    y = (f24["label"] == "T1").astype(int).values

    # 5-fold stratified CV (small T1 class -> avoid 1-shot holdout)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    fold_acc_dt: list[float] = []
    fold_acc_gbm: list[float] = []
    fold_auc_dt: list[float] = []
    fold_auc_gbm: list[float] = []
    fold_cm = np.zeros((2, 2), dtype=int)
    for k, (tr, te) in enumerate(skf.split(X, y)):
        dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)
        dt.fit(X.iloc[tr], y[tr])
        p = dt.predict(X.iloc[te])
        fold_acc_dt.append(accuracy_score(y[te], p))
        if y[te].sum() > 0 and y[te].sum() < len(y[te]):
            fold_auc_dt.append(roc_auc_score(y[te], dt.predict_proba(X.iloc[te])[:, 1]))
        fold_cm += confusion_matrix(y[te], p, labels=[0, 1])

        gbm = GradientBoostingClassifier(
            n_estimators=300, max_depth=4, learning_rate=0.05, random_state=SEED,
        )
        gbm.fit(X.iloc[tr], y[tr])
        pg = gbm.predict(X.iloc[te])
        fold_acc_gbm.append(accuracy_score(y[te], pg))
        if y[te].sum() > 0 and y[te].sum() < len(y[te]):
            fold_auc_gbm.append(roc_auc_score(y[te], gbm.predict_proba(X.iloc[te])[:, 1]))

    print(f"DT  5-fold acc = {np.mean(fold_acc_dt):.4f} +/- {np.std(fold_acc_dt):.4f}; AUC = {np.mean(fold_auc_dt):.4f}")
    print(f"GBM 5-fold acc = {np.mean(fold_acc_gbm):.4f} +/- {np.std(fold_acc_gbm):.4f}; AUC = {np.mean(fold_auc_gbm):.4f}")
    print("DT pooled CV confusion matrix [[TN, FP],[FN, TP]] =\n", fold_cm)

    # Final fit on full F(2,4) subset for rule extraction
    dt_full = DecisionTreeClassifier(max_depth=6, random_state=SEED)
    dt_full.fit(X, y)
    print("\nFull-fit decision tree on F(2,4) (depth=6):")
    print(export_text(dt_full, feature_names=FEATURE_COLS, max_depth=6))

    # Walk leaves
    tree = dt_full.tree_
    feature = tree.feature
    threshold = tree.threshold
    children_left = tree.children_left
    children_right = tree.children_right
    value = tree.value
    n_node_samples = tree.n_node_samples

    def walk(node: int, conds: list[str]) -> list[dict]:
        if children_left[node] == children_right[node]:
            v = value[node][0]
            n_total = int(n_node_samples[node])
            n_T0 = int(v[0]); n_T1 = int(v[1])
            pred = "T1" if n_T1 >= n_T0 else "T0"
            purity = max(n_T0, n_T1) / max(n_total, 1)
            return [{
                "rule": " AND ".join(conds) if conds else "<root>",
                "n_total": n_total, "n_T0": n_T0, "n_T1": n_T1,
                "predict": pred, "purity": round(purity, 4),
            }]
        feat = FEATURE_COLS[feature[node]]
        thr = float(threshold[node])
        return walk(children_left[node], conds + [f"{feat} <= {thr:.4g}"]) + \
               walk(children_right[node], conds + [f"{feat} > {thr:.4g}"])

    leaves = walk(0, [])
    leaves.sort(key=lambda r: (-r["purity"], -r["n_total"]))

    out = {
        "n_records": int(len(f24)),
        "n_T0": int((f24["label"]=="T0").sum()),
        "n_T1": int((f24["label"]=="T1").sum()),
        "cv_decision_tree": {
            "fold_accuracies": fold_acc_dt,
            "mean_accuracy": float(np.mean(fold_acc_dt)),
            "std_accuracy": float(np.std(fold_acc_dt)),
            "mean_auc": float(np.mean(fold_auc_dt)) if fold_auc_dt else None,
            "pooled_confusion_matrix": fold_cm.tolist(),
            "feature_importance_full_fit": dict(zip(FEATURE_COLS, [float(v) for v in dt_full.feature_importances_])),
        },
        "cv_gradient_boosting": {
            "fold_accuracies": fold_acc_gbm,
            "mean_accuracy": float(np.mean(fold_acc_gbm)),
            "std_accuracy": float(np.std(fold_acc_gbm)),
            "mean_auc": float(np.mean(fold_auc_gbm)) if fold_auc_gbm else None,
        },
        "leaf_rules_full_fit": leaves,
    }
    (HERE / "f24_only_metrics.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("Wrote f24_only_metrics.json")

    # Append to rules_extracted.md
    md = ["\n\n---\n\n## Companion analysis: F(2,4)-only (deg_pair held constant)\n",
          f"Subset: {len(f24)} families ({(f24['label']=='T0').sum()} T0 Rat, "
          f"{(f24['label']=='T1').sum()} T1 Trans).  5-fold stratified CV.\n",
          f"- DT mean accuracy: **{np.mean(fold_acc_dt):.4f}** "
          f"(±{np.std(fold_acc_dt):.4f}); AUC {np.mean(fold_auc_dt):.4f}",
          f"- GBM mean accuracy: **{np.mean(fold_acc_gbm):.4f}** "
          f"(±{np.std(fold_acc_gbm):.4f}); AUC {np.mean(fold_auc_gbm):.4f}",
          f"- Pooled DT CV confusion [[TN={fold_cm[0,0]}, FP={fold_cm[0,1]}], "
          f"[FN={fold_cm[1,0]}, TP={fold_cm[1,1]}]]\n",
          "### F(2,4)-only leaf rules (full fit)\n",
          "| Rule | predicts | n | T0 | T1 | purity |",
          "|---|---|---:|---:|---:|---:|",
          ]
    for r in leaves:
        md.append(f"| `{r['rule']}` | {r['predict']} | {r['n_total']} | "
                  f"{r['n_T0']} | {r['n_T1']} | {r['purity']:.3f} |")
    with (HERE / "rules_extracted.md").open("a", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("Appended F(2,4)-only section to rules_extracted.md")


if __name__ == "__main__":
    main()
