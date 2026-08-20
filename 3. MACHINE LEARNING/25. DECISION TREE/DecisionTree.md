# Decision Tree — Short Notes

## 1. Introduction to Decision Tree

- A **Decision Tree** is a supervised ML algorithm used for both **classification** and **regression**.
- It splits data into subsets based on feature values, forming a **tree structure**:
  - **Root Node** → entire dataset
  - **Internal Node** → decision on a feature
  - **Leaf Node** → final output (class label or value)
- Works by asking a series of **yes/no or threshold-based questions** to split data until it becomes "pure" or a stopping condition is met.
- Easy to interpret (white-box model), but prone to **overfitting**.

---

## 2. Entropy and Gini Impurity

Both measure **impurity/disorder** in a node — lower value = purer node.

### Entropy
$$
Entropy(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)
$$
- $p_i$ = proportion of class $i$ in set $S$
- Range: 0 (pure) to 1 (max impurity, for binary class)

### Gini Impurity
$$
Gini(S) = 1 - \sum_{i=1}^{c} p_i^2
$$
- Range: 0 (pure) to 0.5 (max impurity, for binary class)
- Measures probability of misclassifying a randomly chosen element.

---

## 3. Information Gain

- Measures **reduction in entropy** after a dataset is split on an attribute.
$$
IG(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} \cdot Entropy(S_v)
$$
- Higher Information Gain → better feature to split on.
- Used in **ID3 algorithm** to choose the best splitting attribute.

---

## 4. Entropy vs Gini Impurity

| Aspect | Entropy | Gini Impurity |
|---|---|---|
| Formula | $-\sum p_i \log_2 p_i$ | $1 - \sum p_i^2$ |
| Computation | Slower (log calculation) | Faster (no log) |
| Max value (binary) | 1 | 0.5 |
| Sensitivity | Slightly more sensitive to class imbalance | Less sensitive |
| Used in | ID3, C4.5 | CART |
| Practical difference | Usually gives similar trees; Gini is default in sklearn (faster) |

---

## 5. Decision Tree Split for Numerical Features

- For continuous/numerical features, the algorithm:
  1. Sorts the feature values.
  2. Considers **midpoints** between consecutive values as candidate thresholds.
  3. For each threshold $t$, splits data into $x \le t$ and $x > t$.
  4. Calculates Gini/Entropy/Information Gain for each split.
  5. Selects the threshold with **best impurity reduction**.
- This makes splitting numerical features computationally expensive (many candidate thresholds).

---

## 6. Post Pruning & Pre Pruning

Pruning reduces **overfitting** by simplifying the tree.

### Pre-Pruning (Early Stopping)
- Stop tree growth early using constraints:
  - `max_depth`
  - `min_samples_split`
  - `min_samples_leaf`
  - `max_leaf_nodes`
- Faster, but risk of **underfitting**.

### Post-Pruning
- Grow the full tree first, then **remove/collapse branches** that don't improve validation performance.
- Common method: **Cost Complexity Pruning (CCP)** — controlled by parameter $\alpha$ in sklearn (`ccp_alpha`).
- Usually gives better generalization than pre-pruning but computationally costlier.

---

## 7. Decision Tree Regression

- Used when target variable is **continuous**.
- Instead of Gini/Entropy, splitting is based on minimizing **variance** or **MSE (Mean Squared Error)**:
$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \bar{y})^2
$$
- Leaf node value = **mean of target values** in that region.
- Predicts a constant value for each region (step-function-like output, not smooth).

---

## 8. Decision Tree Implementation (sklearn)

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

# Classification
clf = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Regression
reg = DecisionTreeRegressor(max_depth=5, random_state=42)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
```

Key hyperparameters:
- `criterion`: `'gini'`, `'entropy'` (classification) / `'squared_error'` (regression)
- `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features`, `ccp_alpha`

---

## 9. Decision Tree Preprocessing / Pruning Notes

- Decision Trees **don't require feature scaling** (no distance metric involved).
- Handle both numerical and categorical features (categorical need encoding in sklearn).
- Sensitive to **noisy data** and **small variations** → high variance model.
- Preprune using `max_depth`/`min_samples_leaf`, or postprune using `ccp_alpha` (cost complexity pruning path via `cost_complexity_pruning_path()`).

---

## 10. Example — Diabetes Prediction Using Decision Tree Regressor

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg = DecisionTreeRegressor(max_depth=4, random_state=42)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
```
- Predicts disease progression (continuous value) based on patient features (BMI, blood pressure, etc.).
- `max_depth` tuning important — too deep → overfits; too shallow → underfits.

---

## Quick Revision Table

| Concept | Key Idea |
|---|---|
| Entropy/Gini | Measure node impurity |
| Information Gain | Choose best split (max IG) |
| Numerical Split | Try midpoints as thresholds |
| Pre-Pruning | Stop early (depth, min samples) |
| Post-Pruning | Grow full tree, then trim (ccp_alpha) |
| Regression Tree | Splits minimize MSE/variance, leaf = mean |