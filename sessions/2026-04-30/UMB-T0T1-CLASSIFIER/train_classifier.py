"""
UMB-T0T1-CLASSIFIER (P-07) — train + evaluate.

Inputs:  dataset.csv, features.json
Outputs: model.json (decision-tree rules in JSON),
         tree.svg, tree.txt (interpretable text rules),
         rules_extracted.md,
         confusion.json, roc.json,
         metrics.json, train.log
"""

import json
import csv
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_curve, roc_auc_score,
)
from sklearn.model_selection import train_test_split

HERE = Path(__file__).resolve().parent
LOG = HERE / "train.log"
log_lines: list[str] = []


def log(msg: str) -> None:
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    log_lines.append(line)


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
    log(f"Loaded {len(df)} rows.  Class counts: {df['label'].value_counts().to_dict()}")

    # Replace any nan/inf in features
    X = df[FEATURE_COLS].copy()
    X = X.replace([np.inf, -np.inf], np.nan).fillna(0.0)
    y = (df["label"] == "T1").astype(int).values  # 1 = T1, 0 = T0

    # Train/holdout split: stratified, 100 holdout per spec
    X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(
        X, y, df["idx"].values,
        test_size=100, random_state=SEED, stratify=y,
    )
    log(f"Train: {len(X_train)}  Holdout: {len(X_test)}")

    # ---- Decision Tree (interpretable) ----
    log("Training DecisionTreeClassifier(max_depth=6, criterion='gini') ...")
    dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)
    dt.fit(X_train, y_train)
    y_pred_dt = dt.predict(X_test)
    acc_dt = accuracy_score(y_test, y_pred_dt)
    cm_dt = confusion_matrix(y_test, y_pred_dt)
    proba_dt = dt.predict_proba(X_test)[:, 1]
    auc_dt = roc_auc_score(y_test, proba_dt)
    log(f"DT holdout accuracy = {acc_dt:.4f}, AUC = {auc_dt:.4f}")
    log("DT confusion matrix:\n" + str(cm_dt))

    # ---- Gradient Boosting (max accuracy) ----
    log("Training GradientBoostingClassifier(n_estimators=300, max_depth=4) ...")
    gbm = GradientBoostingClassifier(
        n_estimators=300, max_depth=4, learning_rate=0.05, random_state=SEED,
    )
    gbm.fit(X_train, y_train)
    y_pred_gbm = gbm.predict(X_test)
    acc_gbm = accuracy_score(y_test, y_pred_gbm)
    cm_gbm = confusion_matrix(y_test, y_pred_gbm)
    proba_gbm = gbm.predict_proba(X_test)[:, 1]
    auc_gbm = roc_auc_score(y_test, proba_gbm)
    log(f"GBM holdout accuracy = {acc_gbm:.4f}, AUC = {auc_gbm:.4f}")
    log("GBM confusion matrix:\n" + str(cm_gbm))

    # ---- Tree export: text + svg + json rules ----
    text_rules = export_text(dt, feature_names=FEATURE_COLS, max_depth=6)
    (HERE / "tree.txt").write_text(text_rules, encoding="utf-8")
    log("Wrote tree.txt")

    # SVG via graphviz dot if available; otherwise render via sklearn -> dot file.
    dot = export_graphviz(
        dt, out_file=None, feature_names=FEATURE_COLS,
        class_names=["T0", "T1"], filled=True, rounded=True,
        special_characters=True, impurity=False,
    )
    (HERE / "tree.dot").write_text(dot, encoding="utf-8")
    try:
        import graphviz  # type: ignore
        g = graphviz.Source(dot)
        g.format = "svg"
        out = g.render(filename=str(HERE / "tree"), cleanup=True)
        log(f"Wrote tree.svg via graphviz: {out}")
    except Exception as e:
        log(f"graphviz Python lib unavailable ({e}); attempting matplotlib fallback")
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            from sklearn.tree import plot_tree
            fig, ax = plt.subplots(figsize=(28, 14))
            plot_tree(
                dt, feature_names=FEATURE_COLS, class_names=["T0", "T1"],
                filled=True, rounded=True, ax=ax, fontsize=8,
            )
            fig.tight_layout()
            fig.savefig(HERE / "tree.svg", format="svg", bbox_inches="tight")
            plt.close(fig)
            log("Wrote tree.svg via matplotlib")
        except Exception as e2:
            log(f"matplotlib fallback failed: {e2}.  tree.dot retained as the source.")

    # ---- Extract human-readable rules per leaf with the strongest support ----
    # Walk the tree.
    tree = dt.tree_
    feature = tree.feature
    threshold = tree.threshold
    children_left = tree.children_left
    children_right = tree.children_right
    value = tree.value
    n_node_samples = tree.n_node_samples

    LEAF = -1  # sklearn uses TREE_UNDEFINED = -2 for leaves' feature indices

    def walk(node: int, conds: list[str]) -> list[dict]:
        if children_left[node] == children_right[node]:  # leaf
            v = value[node][0]
            n_total = int(n_node_samples[node])
            n_T0 = int(v[0])
            n_T1 = int(v[1])
            pred = "T1" if n_T1 >= n_T0 else "T0"
            purity = max(n_T0, n_T1) / max(n_total, 1)
            return [{
                "rule": " AND ".join(conds) if conds else "<root>",
                "n_total": n_total, "n_T0": n_T0, "n_T1": n_T1,
                "predict": pred, "purity": round(purity, 4),
            }]
        feat = FEATURE_COLS[feature[node]]
        thr = float(threshold[node])
        left = walk(children_left[node], conds + [f"{feat} <= {thr:.4g}"])
        right = walk(children_right[node], conds + [f"{feat} > {thr:.4g}"])
        return left + right

    leaf_rules = walk(0, [])
    leaf_rules.sort(key=lambda r: (-r["purity"], -r["n_total"]))
    (HERE / "leaf_rules.json").write_text(
        json.dumps(leaf_rules, indent=2), encoding="utf-8")
    log(f"Wrote leaf_rules.json ({len(leaf_rules)} leaves)")

    # ---- Misclassified holdout (for inspection) ----
    misclassified = []
    test_df = df.iloc[df.index.isin(idx_test)].reset_index(drop=True)
    test_df = df[df["idx"].isin(idx_test)].copy().sort_values("idx").reset_index(drop=True)
    test_df_sorted = test_df.set_index("idx").loc[idx_test].reset_index()
    for j, idx in enumerate(idx_test):
        true = int(y_test[j])
        pred = int(y_pred_dt[j])
        if true != pred:
            row = df[df["idx"] == idx].iloc[0]
            misclassified.append({
                "idx": int(idx),
                "true": "T1" if true == 1 else "T0",
                "predicted": "T1" if pred == 1 else "T0",
                "source": row["source"],
                "a": row["a_str"], "b": row["b_str"],
                "deg_a": int(row["deg_a"]), "deg_b": int(row["deg_b"]),
                "R_struct": float(row["R_struct"]),
                "conv_slope": float(row["conv_slope"]),
            })
    (HERE / "misclassified_holdout.json").write_text(
        json.dumps(misclassified, indent=2), encoding="utf-8")
    log(f"Wrote misclassified_holdout.json: {len(misclassified)} cases")

    # ---- Save metrics + roc ----
    fpr, tpr, _ = roc_curve(y_test, proba_dt)
    metrics = {
        "seed": SEED,
        "feature_cols": FEATURE_COLS,
        "n_train": int(len(X_train)),
        "n_holdout": int(len(X_test)),
        "decision_tree": {
            "max_depth": 6,
            "holdout_accuracy": float(acc_dt),
            "holdout_auc": float(auc_dt),
            "confusion_matrix_TN_FP_FN_TP": [int(cm_dt[0,0]), int(cm_dt[0,1]), int(cm_dt[1,0]), int(cm_dt[1,1])],
            "feature_importance": dict(zip(FEATURE_COLS, [float(v) for v in dt.feature_importances_])),
        },
        "gradient_boosting": {
            "n_estimators": 300, "max_depth": 4, "lr": 0.05,
            "holdout_accuracy": float(acc_gbm),
            "holdout_auc": float(auc_gbm),
            "confusion_matrix_TN_FP_FN_TP": [int(cm_gbm[0,0]), int(cm_gbm[0,1]), int(cm_gbm[1,0]), int(cm_gbm[1,1])],
            "feature_importance": dict(zip(FEATURE_COLS, [float(v) for v in gbm.feature_importances_])),
        },
    }
    (HERE / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    (HERE / "confusion.json").write_text(json.dumps({
        "decision_tree": {
            "labels": ["T0", "T1"],
            "matrix": cm_dt.tolist(),
            "accuracy": float(acc_dt),
        },
        "gradient_boosting": {
            "labels": ["T0", "T1"],
            "matrix": cm_gbm.tolist(),
            "accuracy": float(acc_gbm),
        },
    }, indent=2), encoding="utf-8")
    (HERE / "roc.json").write_text(json.dumps({
        "decision_tree": {"fpr": fpr.tolist(), "tpr": tpr.tolist(), "auc": float(auc_dt)},
        "gradient_boosting_auc": float(auc_gbm),
    }, indent=2), encoding="utf-8")
    log("Wrote metrics.json, confusion.json, roc.json")

    # ---- rules_extracted.md ----
    md = []
    md.append("# Extracted T0/T1 classification rules\n")
    md.append(f"_From DecisionTreeClassifier(max_depth=6); holdout {len(X_test)} families._")
    md.append(f"\n- Holdout accuracy: **{acc_dt:.4f}**")
    md.append(f"- Holdout AUC: **{auc_dt:.4f}**")
    md.append(f"- Gradient-boosted accuracy: **{acc_gbm:.4f}** (AUC {auc_gbm:.4f})\n")
    md.append("## Pure leaves (purity ≥ 0.99) ranked by support\n")
    md.append("| Rule | predicts | n_total | n_T0 | n_T1 | purity |")
    md.append("|---|---|---:|---:|---:|---:|")
    for r in leaf_rules:
        if r["purity"] >= 0.99:
            md.append(f"| `{r['rule']}` | {r['predict']} | {r['n_total']} | {r['n_T0']} | {r['n_T1']} | {r['purity']:.3f} |")
    md.append("\n## All leaves (sorted by purity)\n")
    md.append("| Rule | predicts | n_total | n_T0 | n_T1 | purity |")
    md.append("|---|---|---:|---:|---:|---:|")
    for r in leaf_rules:
        md.append(f"| `{r['rule']}` | {r['predict']} | {r['n_total']} | {r['n_T0']} | {r['n_T1']} | {r['purity']:.3f} |")
    md.append("\n## Top-3 candidate Lemmas (highest-support pure leaves)\n")
    pure = [r for r in leaf_rules if r["purity"] >= 0.99]
    pure.sort(key=lambda r: -r["n_total"])
    for i, r in enumerate(pure[:3], start=1):
        md.append(f"\n### Lemma candidate {i} — predicts {r['predict']}")
        md.append(f"- Rule: **{r['rule']}**")
        md.append(f"- Training support: n={r['n_total']}, purity={r['purity']:.3f}")
    md.append("\n## Feature importance (decision tree)\n")
    md.append("| Feature | importance |")
    md.append("|---|---:|")
    for k, v in sorted(metrics["decision_tree"]["feature_importance"].items(), key=lambda kv: -kv[1]):
        md.append(f"| `{k}` | {v:.4f} |")
    (HERE / "rules_extracted.md").write_text("\n".join(md), encoding="utf-8")
    log("Wrote rules_extracted.md")

    # ---- HALT decision ----
    halt = {
        "halt_triggered": False,
        "criterion": "Tree accuracy > 0.97 on held-out 100",
        "decision_tree_holdout_accuracy": float(acc_dt),
        "gradient_boosting_holdout_accuracy": float(acc_gbm),
        "verdict": "ESCALATE: proceed to formal verification of top-3 leaf rules"
                   if acc_dt > 0.97 else "CONTINUE: tree below threshold; iterate features",
    }
    if acc_dt > 0.97:
        halt["halt_triggered"] = True
    (HERE / "halt_log.json").write_text(json.dumps(halt, indent=2), encoding="utf-8")
    log(f"halt_log.json written — halt_triggered={halt['halt_triggered']}")

    LOG.write_text("\n".join(log_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
