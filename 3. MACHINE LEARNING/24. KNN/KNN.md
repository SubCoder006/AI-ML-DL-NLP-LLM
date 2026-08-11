# Topics 194–196: K-Nearest Neighbors (KNN)

---

## 194. KNN — Classification & Regression: Indepth Intuition

### Core Idea
KNN is a **non-parametric, instance-based (lazy)** learning algorithm. It makes no assumptions about the underlying data distribution and does not "learn" a model during training — it simply memorizes the training data and defers all computation to prediction time.

### How It Works
1. Choose a value of **K** (number of neighbors).
2. For a new query point, compute the **distance** to every point in the training set.
3. Select the **K closest points**.
4. Aggregate their labels:
   - **Classification** → majority vote among the K neighbors.
   - **Regression** → mean (or weighted mean) of the K neighbors' target values.

### Distance Metrics
- **Euclidean distance** (default, L2 norm): `sqrt(Σ(xi - yi)²)`
- **Manhattan distance** (L1 norm): `Σ|xi - yi|`
- **Minkowski distance**: generalization of Euclidean/Manhattan, parameter `p`
- **Hamming distance**: for categorical/binary features
- **Cosine similarity**: useful for high-dimensional sparse data (e.g., text)

### Choosing K
- **Small K** (e.g., K=1) → low bias, high variance → overfitting, sensitive to noise.
- **Large K** → high bias, low variance → underfitting, smoother decision boundary.
- Common practice: use **odd K** for binary classification to avoid ties.
- Optimal K is usually found via **cross-validation** (plot error vs K → "elbow" point).

### Weighted KNN
Instead of simple majority/mean, weight neighbors by inverse distance:
```
weight = 1 / distance
```
Closer neighbors influence the prediction more — helps reduce the impact of far-off points when K is large.

### Feature Scaling Matters
Since KNN relies purely on distance, unscaled features (different units/ranges) distort neighbor selection. Always apply:
- **Standardization** (z-score) or
- **Min-Max normalization**

### Curse of Dimensionality
As the number of features grows, distances between points become less meaningful (all points appear equidistant). Mitigate via:
- Dimensionality reduction (PCA)
- Feature selection

### Pros & Cons
| Pros | Cons |
|---|---|
| Simple, intuitive | Slow at prediction time (O(n) per query, naive) |
| No training phase | Memory-intensive (stores entire dataset) |
| Naturally handles multi-class | Sensitive to irrelevant features & scaling |
| Works for both classification & regression | Struggles in high dimensions |

---

## 195. Optimization of KNN — KD-Tree & Ball Tree: Indepth Intuition

### Why Optimize?
Naive KNN requires computing distance to **every** training point for each prediction → **O(n·d)** per query (n = samples, d = dimensions). This is expensive for large datasets. Spatial data structures speed up neighbor search.

### KD-Tree (K-Dimensional Tree)
- A **binary tree** that recursively partitions the feature space along axes.
- At each level, split the data on the **median** of one dimension (cycling through dimensions).
- Search becomes **O(log n)** on average (vs O(n) naive) for low-dimensional data.

**Construction:**
1. Pick a dimension to split on (often the one with highest variance, or cycle through dimensions).
2. Find the median point along that dimension → becomes the node.
3. Recursively build left/right subtrees for points less/greater than the median.

**Query (nearest neighbor search):**
1. Traverse the tree to find the region containing the query point.
2. Backtrack up the tree, checking if a closer point could exist in sibling branches (using distance to splitting hyperplane).
3. Prune branches that can't contain a closer point.

**Limitation:** Efficiency degrades in **high dimensions** (curse of dimensionality) — beyond ~20 dimensions, KD-Tree performance approaches brute force.

### Ball Tree
- Partitions data into **nested hyperspheres (balls)** instead of axis-aligned boxes.
- Each node represents a ball defined by a **centroid** and **radius** covering all points within it.
- Better suited for **higher-dimensional** data and **non-Euclidean distance metrics** than KD-Tree.

**Construction:**
1. Group points into a ball (minimum enclosing hypersphere).
2. Split the ball into two child balls (using clustering, e.g., choosing two far-apart points as centers).
3. Recurse until leaf nodes contain a small number of points.

**Query:**
- Use **triangle inequality** to prune: if the distance from the query to a ball's center minus the ball's radius is greater than the current best distance found, that entire ball can be skipped.

### KD-Tree vs Ball Tree
| Aspect | KD-Tree | Ball Tree |
|---|---|---|
| Partition shape | Axis-aligned rectangles | Hyperspheres |
| Best for | Low-dim data (< ~20 dims) | Medium-high dim data |
| Distance metrics | Mostly Euclidean | Works with many metrics |
| Build cost | Lower | Slightly higher |
| Query speed (high-dim) | Degrades | More robust |

### Other Optimization Approaches
- **Brute Force**: default fallback, O(n·d) — fine for small n.
- **Approximate Nearest Neighbors (ANN)**: e.g., LSH (Locality Sensitive Hashing), HNSW — trade exactness for speed on very large datasets.
- **Dimensionality reduction** before building the tree (PCA/UMAP) to make KD-Tree/Ball Tree viable in higher dims.

**In scikit-learn:** `algorithm` parameter in `KNeighborsClassifier`/`KNeighborsRegressor`:
```python
KNeighborsClassifier(n_neighbors=5, algorithm='auto')  # 'auto', 'ball_tree', 'kd_tree', 'brute'
```
`'auto'` lets sklearn pick the best structure based on data size/dimensionality.

---

## 196. KNN Classifier and Regressor — Classification

### KNN Classifier
- Predicts a **discrete class label**.
- Aggregation: **majority vote** among K nearest neighbors.
- Output can also be a **probability estimate** = (votes for class) / K.
- Decision boundary is **non-linear** and adapts to local data density.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5, weights='distance', metric='minkowski', p=2)
model.fit(X_train, y_train)
preds = model.predict(X_test)
probs = model.predict_proba(X_test)
```

### KNN Regressor
- Predicts a **continuous value**.
- Aggregation: **mean** (or distance-weighted mean) of K nearest neighbors' target values.

```python
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(n_neighbors=5, weights='distance')
model.fit(X_train, y_train)
preds = model.predict(X_test)
```

### Key Hyperparameters (both)
- `n_neighbors` (K): number of neighbors to consider.
- `weights`: `'uniform'` (equal vote) vs `'distance'` (closer points weigh more).
- `metric`: distance function (`minkowski`, `euclidean`, `manhattan`, etc.).
- `algorithm`: `'auto'`, `'kd_tree'`, `'ball_tree'`, `'brute'`.

### Evaluation
- **Classifier**: accuracy, precision/recall, F1, confusion matrix.
- **Regressor**: MAE, MSE, RMSE, R².
- Always validate K choice via **k-fold cross-validation**, plotting validation error against K to find the sweet spot between overfitting and underfitting.

### Quick Recap
| | Classifier | Regressor |
|---|---|---|
| Output | Class label | Continuous value |
| Aggregation | Majority vote | Mean of neighbors |
| Decision surface | Non-linear boundary | Piecewise-smooth curve |
| Sensitive to K | Yes (boundary smoothness) | Yes (curve smoothness) |

---

### Summary
KNN is simple and powerful but computationally expensive at scale — KD-Tree and Ball Tree structures make neighbor search efficient by pruning irrelevant regions of space, with Ball Tree generalizing better to higher dimensions and non-Euclidean metrics. Proper feature scaling and careful choice of K (via cross-validation) are essential for good performance in both classification and regression settings.