# Random Forest — Revision Notes

## 1. Bagging vs Boosting

| Aspect | Bagging | Boosting |
|---|---|---|
| Idea | Train models **parallel** on random subsets (bootstrap) | Train models **sequentially**, each fixing previous errors |
| Sampling | Random sampling **with replacement** | Weighted sampling — misclassified points get higher weight |
| Goal | Reduce **variance** | Reduce **bias** (and variance) |
| Combine | Majority vote / average | Weighted vote / weighted sum |
| Base learners | Independent, usually deep trees | Dependent, usually weak learners (shallow trees/stumps) |
| Overfitting risk | Lower | Higher (needs tuning: learning rate, n_estimators) |
| Examples | Random Forest | AdaBoost, Gradient Boosting, XGBoost |

**Random Forest = Bagging + Feature Randomness** (Bootstrap Aggregating on both rows and columns).

---

## 2. Random Forest — Core Idea

- Ensemble of **decision trees**, each trained on:
  - A **bootstrap sample** of rows (random sampling with replacement, ~63.2% unique samples per tree).
  - A **random subset of features** at each split (`max_features`) — decorrelates trees.
- Final prediction:
  - **Classification** → majority vote (mode) across trees.
  - **Regression** → average of tree outputs.
- Rows/features left out of a tree's bootstrap sample = **OOB (Out-of-Bag)** samples → used for OOB error estimate (free validation, no need for separate val set).

---

## 3. Random Forest Regression

- Each tree predicts a continuous value; final output = **mean of all tree predictions**.
- Splitting criterion: minimize **variance / MSE** at each node (not Gini/entropy).
- Prediction at a leaf = average target value of training samples in that leaf.
- Reduces variance of a single high-variance tree (deep trees overfit individually, averaging smooths it out).
- Loss/metric: MSE, RMSE, MAE, R².

---

## 4. Problem Classification (Regression vs Classification identification)

Key questions to decide task type:
- **Target variable type?**
  - Continuous (price, temperature, salary) → Regression
  - Discrete/categorical (yes/no, class label) → Classification
- **Output needed?**
  - A number → Regression
  - A category/probability of class → Classification
- Splitting criteria differ:
  - Classification: **Gini Impurity** or **Entropy / Information Gain**
  - Regression: **Variance Reduction (MSE)**

$$Gini = 1 - \sum_{i=1}^{c} p_i^2 \qquad Entropy = -\sum_{i=1}^{c} p_i \log_2 p_i$$

---

## 5. Feature Engineering (for Random Forest)

- **Handling categorical features**: One-Hot Encoding (low cardinality) or Label/Target Encoding (high cardinality) — trees can handle label-encoded categories reasonably well since splits are threshold-based.
- **Missing values**: RF is fairly robust; can impute with median/mode or use surrogate splits.
- **Feature scaling**: **Not required** — trees split on thresholds, not distances.
- **Feature importance**:
  - Mean Decrease in Impurity (Gini importance) — sum of impurity decrease from splits on that feature, averaged over trees.
  - Permutation importance — shuffle a feature, measure drop in performance (more reliable, avoids bias toward high-cardinality features).
- **Feature selection**: drop low-importance/correlated features to reduce noise & training time.
- **Outliers**: RF is robust to outliers (splits are rank-based, not magnitude-sensitive).

---

## 6. Model Training — Key Hyperparameters

| Parameter | Effect |
|---|---|
| `n_estimators` | Number of trees; more = more stable, diminishing returns, slower |
| `max_depth` | Controls tree depth; deeper = more variance/overfitting |
| `max_features` | Features considered per split; lower = more decorrelated trees, higher bias |
| `min_samples_split` | Min samples to split a node; higher = simpler trees |
| `min_samples_leaf` | Min samples at a leaf; higher = smoother predictions |
| `bootstrap` | Whether sampling is with replacement (True = bagging enabled) |
| `oob_score` | Use OOB samples to estimate generalization error |

**Training steps:**
1. Draw N bootstrap samples from training data (one per tree).
2. For each tree, at each node, select random subset of features → choose best split.
3. Grow tree fully (or to `max_depth`) — no pruning needed (ensemble averaging controls overfitting).
4. Repeat for `n_estimators` trees.
5. Aggregate: vote (classification) / average (regression).

---

## 7. Why Random Forest Works Well

- Individual deep trees → **low bias, high variance**.
- Averaging many **decorrelated** trees → variance drops without increasing bias much.
- Randomness sources (bootstrap rows + random feature subset) → decorrelation → better generalization than a single tree or plain bagging of trees.

---

## 8. Quick Comparison: Decision Tree vs Random Forest

| Aspect | Decision Tree | Random Forest |
|---|---|---|
| Variance | High | Low (averaged) |
| Bias | Low | Slightly higher |
| Overfitting | Prone to | Resistant |
| Interpretability | High | Lower (black-box ensemble) |
| Training speed | Fast | Slower (many trees) |
| Feature importance | Single-tree based | More robust (averaged) |