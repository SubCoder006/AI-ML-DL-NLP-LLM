# PCA — Revision Notes

## Curse of Dimensionality

- As the number of **features (dimensions)** increases, the volume of the feature space grows exponentially, but data points stay sparse.
- **Effects:**
  - Distance between points becomes less meaningful (all points look "equally far").
  - Models need exponentially more data to generalize well.
  - Higher risk of **overfitting**.
  - More computation, storage, and training time.
- **Fix:** Reduce dimensions — either by *selecting* important features or *extracting* new combined features.

---

## Feature Selection vs Feature Extraction

| Aspect | Feature Selection | Feature Extraction |
|---|---|---|
| **Idea** | Pick a subset of existing features | Create new features by combining existing ones |
| **Original features** | Kept as-is | Transformed/combined |
| **Interpretability** | High (original meaning kept) | Lower (new features are combinations) |
| **Examples** | Forward/Backward selection, Chi-square, Correlation filter | PCA, LDA, t-SNE, Autoencoders |

- **Feature Selection** → removes irrelevant/redundant columns.
- **Feature Extraction** → projects data into a new, smaller space (PCA falls here).

---

## PCA — Geometric Intuition

- **Goal:** Find new axes (directions) along which the data has **maximum spread (variance)**.
- These new axes are called **Principal Components (PCs)**.
- **Key ideas:**
  - PC1 = direction of **maximum variance** in the data.
  - PC2 = direction of next-highest variance, and **perpendicular (orthogonal)** to PC1.
  - Each next PC is orthogonal to all previous ones.
- Data is then **projected** onto these new axes → fewer dimensions, minimal information loss.
- **Why maximum variance?** More spread = more information preserved. A direction with near-zero variance carries almost no useful signal.
- Geometrically: PCA **rotates** the coordinate axes to align with the directions where data varies the most.

---

## PCA — Maths Intuition

- **Step 1: Standardize the data**
  - Subtract mean, divide by standard deviation (so all features are on the same scale):
    $$ z = \frac{x - \mu}{\sigma} $$
- **Step 2: Variance and Covariance**
  - Variance measures spread of a single feature:
    $$ \text{Var}(X) = \frac{1}{n}\sum (x_i - \bar{x})^2 $$
  - Covariance measures how two features vary together:
    $$ \text{Cov}(X, Y) = \frac{1}{n}\sum (x_i - \bar{x})(y_i - \bar{y}) $$
- **Step 3: Covariance Matrix**
  - For a dataset with multiple features, build a matrix of all pairwise covariances:
    $$ \Sigma = \frac{1}{n} X^T X \quad (\text{after standardizing } X) $$
- **Goal restated mathematically:** Find a direction (unit vector) $v$ that **maximizes** the variance of the projected data $Xv$.
  - This turns into an **eigenvalue problem** on the covariance matrix.

---

## Eigen Decomposition on Covariance Matrix

- For covariance matrix $\Sigma$, solve:
  $$ \Sigma v = \lambda v $$
  where:
  - $v$ = **eigenvector** → gives the **direction** of a principal component
  - $\lambda$ = **eigenvalue** → gives the **amount of variance** captured along that direction
- **Steps:**
  1. Compute covariance matrix $\Sigma$.
  2. Find eigenvalues and eigenvectors of $\Sigma$.
  3. Sort eigenvectors by their eigenvalues in **descending order**.
  4. Top eigenvector = PC1, second = PC2, and so on.
- **Explained Variance Ratio:** tells how much information (variance) each PC holds:
  $$ \text{Explained Variance Ratio} = \frac{\lambda_i}{\sum \lambda_j} $$
- Eigenvectors are always **orthogonal** to each other (for symmetric covariance matrices) → this is why PCs are perpendicular.

---

## PCA — Implementation (Practical Steps)

1. **Standardize** the dataset (mean = 0, std = 1).
2. Compute the **covariance matrix**.
3. Compute **eigenvalues and eigenvectors**.
4. Sort eigenvectors by eigenvalues (descending) → pick top $k$ components.
5. Form a **projection matrix** $W$ using the top $k$ eigenvectors.
6. Transform data:
   $$ X_{\text{new}} = X \cdot W $$

**Using scikit-learn:**
```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Standardize
X_scaled = StandardScaler().fit_transform(X)

# Step 2: Apply PCA
pca = PCA(n_components=2)   # reduce to 2 dimensions
X_pca = pca.fit_transform(X_scaled)

# Check how much variance is explained
print(pca.explained_variance_ratio_)
```

- **Choosing number of components ($k$):** Plot cumulative explained variance vs number of components (**Scree plot**) and pick $k$ where it crosses ~90-95%.

---

## Quick Summary

- **Curse of Dimensionality** → too many features hurt model performance.
- **Feature Selection** → keep a subset of original features.
- **Feature Extraction (PCA)** → create new features (PCs) capturing max variance.
- **PCA** works by finding eigenvectors/eigenvalues of the covariance matrix.
- Top eigenvectors = directions of most variance = new reduced feature space.