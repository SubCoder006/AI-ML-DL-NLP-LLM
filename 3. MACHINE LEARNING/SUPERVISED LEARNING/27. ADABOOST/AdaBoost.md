# 216–224. AdaBoost (Adaptive Boosting)

## 216. Introduction to AdaBoost

**Definition:** AdaBoost (Adaptive Boosting) is an **ensemble boosting** algorithm that combines multiple **weak learners** (typically decision stumps) sequentially, where each new learner focuses more on the samples misclassified by previous learners.

- Type: Sequential ensemble (boosting), unlike Random Forest (parallel/bagging)
- Base learner: Decision Stump (1 root + 2 leaves)
- Output: Weighted majority vote (classification) or weighted sum (regression)

$$
F(x) = \sum_{t=1}^{T} \alpha_t \, h_t(x)
$$

where $h_t(x)$ = weak learner, $\alpha_t$ = its weight (say).

---

## 217. Creating a Decision Tree Stump

**Definition:** A **stump** is a decision tree of depth 1 — one root node splitting on a single feature, producing two leaf nodes.

- Weak learner: performs only slightly better than random guessing
- Each feature is tested as a potential stump; the one minimizing weighted error is chosen

---

## 218. Performance of Decision Tree Stump

**Definition:** Performance (say/amount of say) $\alpha_t$ measures how much a stump's prediction is trusted, based on its **total error** $\varepsilon_t$ (sum of weights of misclassified samples).

$$
\alpha_t = \frac{1}{2} \ln\left(\frac{1-\varepsilon_t}{\varepsilon_t}\right)
$$

- $\varepsilon_t \to 0 \Rightarrow \alpha_t$ large (stump trusted highly)
- $\varepsilon_t = 0.5 \Rightarrow \alpha_t = 0$ (random guessing, no say)
- $\varepsilon_t \to 1 \Rightarrow \alpha_t$ large negative (predictions inverted)

---

## 219. Updating Weights

**Definition:** Sample weights are updated after each stump so **misclassified points get higher weight**, forcing the next stump to focus on them.

$$
w_{i}^{new} = w_i \cdot e^{\pm \alpha_t}
$$

- $+\alpha_t$ if misclassified (weight increases)
- $-\alpha_t$ if correctly classified (weight decreases)

---

## 220. Normalising Weights and Assigning Bins

**Definition:** After updating, weights are **normalised** to sum to 1, then cumulative weights define **bins** used for weighted resampling.

$$
w_i^{norm} = \frac{w_i^{new}}{\sum_j w_j^{new}}
$$

- Cumulative sum of normalized weights → bin boundaries $[0,1]$
- Used to select the next training subset (samples with higher weight occupy larger bins → more likely picked)

---

## 221. Selecting New Datapoints for Next Tree

**Definition:** A new dataset (same size as original) is built by **random sampling with replacement**, using the bins from Topic 220 — points with larger weight/error are more likely to be picked multiple times.

- Ensures the next stump trains more on previously misclassified samples
- After resampling, weights reset to $1/N$ for the new round

---

## 222. Final Prediction for AdaBoost

**Definition:** The final prediction is a **weighted vote/sum** of all stumps' outputs, weighted by their respective $\alpha_t$ (amount of say).

**Classification:**
$$
H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t \, h_t(x)\right)
$$

**Regression:** weighted average of stump outputs.

---

## 223. AdaBoost Model Training (Classifier)

**Definition:** `AdaBoostClassifier` (sklearn) trains stumps sequentially, each minimizing weighted classification error, combined via weighted majority voting.

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),  # stump
    n_estimators=50,
    learning_rate=1.0
)
model.fit(X_train, y_train)
```

---

## 224. AdaBoost Regressor Model Training

**Definition:** `AdaBoostRegressor` extends AdaBoost to regression using weighted median/mean of stump predictions, updating weights based on prediction error magnitude instead of misclassification.

```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

model = AdaBoostRegressor(
    estimator=DecisionTreeRegressor(max_depth=1),
    n_estimators=50,
    learning_rate=1.0
)
model.fit(X_train, y_train)
```

---

## Quick Comparison: AdaBoost vs Random Forest

| Aspect | AdaBoost | Random Forest |
|---|---|---|
| Ensemble type | Boosting (sequential) | Bagging (parallel) |
| Base learner | Stumps (depth 1) | Full-depth trees |
| Sample weighting | Adaptive (misclassified ↑) | Uniform, bootstrap |
| Tree weight in vote | $\alpha_t$ (varies) | Equal |
| Overfitting risk | Higher (sensitive to noise/outliers) | Lower |