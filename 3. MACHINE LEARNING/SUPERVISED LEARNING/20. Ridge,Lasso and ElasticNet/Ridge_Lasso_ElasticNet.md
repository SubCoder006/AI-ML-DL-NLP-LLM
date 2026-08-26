# Ridge, Lasso & ElasticNet Regularization — ML Notes

> **Why Regularization?** When a model overfits (high variance), it memorizes training data but fails on new data. Regularization adds a **penalty term** to the loss function to shrink coefficients → reduces overfitting.

---

## 1. The Core Problem: Ordinary Least Squares (OLS)

Standard Linear Regression minimizes:

$$\text{Loss}_{OLS} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \|y - X\beta\|^2$$

**Problem:** No constraint on β → coefficients can blow up → overfitting.

---

## 2. Ridge Regression (L2 Regularization)

### Formula

$$\text{Loss}_{Ridge} = \underbrace{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}_{\text{RSS}} + \underbrace{\lambda \sum_{j=1}^{p}\beta_j^2}_{\text{L2 Penalty}}$$

- Closed-form solution: $\hat{\beta}_{Ridge} = (X^TX + \lambda I)^{-1}X^Ty$
- **λ (alpha):** Controls regularization strength. λ→0 = OLS; λ→∞ = all β→0

### Key Properties
- **Shrinks** coefficients toward zero but **never exactly zero**
- Works well when **many features** contribute a little (dense solution)
- Handles **multicollinearity** well (correlated features)
- Keeps all features in the model

### When to Use
- All features are potentially useful
- Features are correlated
- You want a stable model, not feature selection

### Code

```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

# IMPORTANT: Always scale features before regularization!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Fit Ridge
ridge = Ridge(alpha=1.0)   # alpha = λ
ridge.fit(X_train_scaled, y_train)

print("Coefficients:", ridge.coef_)
print("R² Score:", ridge.score(X_test_scaled, y_test))
```

```python
# Cross-validate to find best alpha
from sklearn.linear_model import RidgeCV

alphas = [0.01, 0.1, 1, 10, 100]
ridge_cv = RidgeCV(alphas=alphas, cv=5)
ridge_cv.fit(X_train_scaled, y_train)
print("Best alpha:", ridge_cv.alpha_)
```

---

## 3. Lasso Regression (L1 Regularization)

### Formula

$$\text{Loss}_{Lasso} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p}|\beta_j|$$

- No closed-form → solved via **coordinate descent**
- **λ (alpha):** Same role as Ridge; higher = more sparsity

### Key Properties
- **Shrinks some coefficients to exactly zero** → built-in **feature selection**
- Produces **sparse** models (only important features survive)
- Unstable when features are highly correlated (picks one arbitrarily)
- Prefers **few strong features**

### Why L1 Creates Sparsity (Intuition)
The L1 penalty has corners at the axes in coefficient space. The optimal solution often lands exactly at a corner → coefficient = 0. L2 has a smooth sphere → solution rarely hits an axis.

### When to Use
- Many features, but only a few are truly relevant
- You want automatic feature selection
- Interpretability matters (fewer non-zero coefficients)

### Code

```python
from sklearn.linear_model import Lasso, LassoCV

# Basic Lasso
lasso = Lasso(alpha=0.1, max_iter=10000)
lasso.fit(X_train_scaled, y_train)

# See which features were zeroed out
import pandas as pd
coef_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': lasso.coef_
})
print(coef_df[coef_df['Coefficient'] != 0])   # Surviving features
print(f"Features kept: {np.sum(lasso.coef_ != 0)} / {len(lasso.coef_)}")
```

```python
# Auto-select best alpha via cross-validation
lasso_cv = LassoCV(alphas=np.logspace(-4, 2, 50), cv=5, max_iter=10000)
lasso_cv.fit(X_train_scaled, y_train)
print("Best alpha:", lasso_cv.alpha_)
```

---

## 4. ElasticNet (L1 + L2 Combined)

### Formula

$$\text{Loss}_{EN} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda_1\sum_{j=1}^{p}|\beta_j| + \lambda_2\sum_{j=1}^{p}\beta_j^2$$

Sklearn parameterization:

$$\text{Loss}_{EN} = \frac{1}{2n}\|y - X\beta\|^2 + \alpha \cdot l1\_ratio \cdot \|\beta\|_1 + \frac{\alpha(1 - l1\_ratio)}{2}\|\beta\|_2^2$$

- `alpha`: Overall regularization strength
- `l1_ratio`: Mix between L1 and L2
  - `l1_ratio = 1` → pure Lasso
  - `l1_ratio = 0` → pure Ridge
  - `0 < l1_ratio < 1` → ElasticNet

### Key Properties
- **Best of both worlds**: Feature selection (L1) + stability with correlated features (L2)
- When correlated features exist, selects **groups** of them (unlike Lasso which picks one)
- More hyperparameters to tune (alpha + l1_ratio)

### When to Use
- Many features, some correlated
- You want feature selection but Lasso is too aggressive
- High-dimensional data (p >> n), e.g., genomics, text data

### Code

```python
from sklearn.linear_model import ElasticNet, ElasticNetCV

# Basic ElasticNet
en = ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=10000)
en.fit(X_train_scaled, y_train)

# Auto-tune both alpha and l1_ratio
l1_ratios = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 1.0]
en_cv = ElasticNetCV(l1_ratio=l1_ratios, alphas=np.logspace(-4, 1, 30), cv=5)
en_cv.fit(X_train_scaled, y_train)
print(f"Best alpha: {en_cv.alpha_}, Best l1_ratio: {en_cv.l1_ratio_}")
```

---

## 5. Comparison Table

| Property | Ridge (L2) | Lasso (L1) | ElasticNet |
|---|---|---|---|
| **Penalty** | $\sum \beta_j^2$ | $\sum \|\beta_j\|$ | L1 + L2 |
| **Feature selection** | ❌ No | ✅ Yes | ✅ Yes |
| **Coefficient = 0?** | Never | Can be exactly 0 | Can be exactly 0 |
| **Correlated features** | Handles well | Unstable | Handles well |
| **Solution type** | Dense | Sparse | Semi-sparse |
| **Hyperparameter** | alpha | alpha | alpha + l1_ratio |
| **Computation** | Closed-form | Coordinate descent | Coordinate descent |
| **Best for** | All features matter | Few features matter | Mixed scenario |

---

## 6. Types of Cross-Validation

### 6.1 K-Fold CV (Most Common)

- Splits data into **K equal folds**
- Trains on K-1 folds, validates on remaining 1
- Repeats K times → average score

```python
from sklearn.model_selection import KFold, cross_val_score

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(ridge, X_scaled, y, cv=kf, scoring='r2')
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.3f} ± {scores.std():.3f}")
```

### 6.2 Stratified K-Fold (Classification)

- Preserves **class proportions** in each fold
- Essential for imbalanced datasets

```python
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

### 6.3 Leave-One-Out (LOO)

- K = n → each sample is a validation set once
- Very expensive; use only for small datasets

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo)
```

### 6.4 Time Series Split (No Data Leakage)

- Respects temporal order; future data never trains past models

```python
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)
```

---

## 7. Real Dataset: House Price Prediction

```python
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data
housing = fetch_california_housing()
X, y = housing.data, housing.target
feature_names = housing.feature_names

# Split & Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# Train all three models
models = {
    'Ridge':      Ridge(alpha=1.0),
    'Lasso':      Lasso(alpha=0.01, max_iter=10000),
    'ElasticNet': ElasticNet(alpha=0.01, l1_ratio=0.5, max_iter=10000)
}

for name, model in models.items():
    model.fit(X_train_s, y_train)
    preds = model.predict(X_test_s)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2   = r2_score(y_test, preds)
    n_zero = np.sum(model.coef_ == 0)
    print(f"{name:12s} | RMSE: {rmse:.4f} | R²: {r2:.4f} | Zero coefs: {n_zero}/{X.shape[1]}")
```

**Expected output (approximate):**
```
Ridge        | RMSE: 0.7256 | R²: 0.5958 | Zero coefs: 0/8
Lasso        | RMSE: 0.7301 | R²: 0.5903 | Zero coefs: 1/8
ElasticNet   | RMSE: 0.7289 | R²: 0.5917 | Zero coefs: 0/8
```

---

## 8. EDA & Feature Engineering Basics

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Check distributions
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y
print(df.describe())

# 2. Correlation heatmap (detect multicollinearity for Ridge/ElasticNet choice)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title("Feature Correlation Matrix")
plt.show()

# 3. Check for skewed features (log-transform if needed)
from scipy import stats
for col in feature_names:
    skew = stats.skew(df[col])
    if abs(skew) > 1:
        print(f"{col}: skew={skew:.2f} → consider log transform")
        df[col] = np.log1p(df[col].clip(lower=0))

# 4. Create interaction features
df['rooms_per_household'] = df['AveRooms'] / df['HouseAge']
df['bedrooms_ratio']      = df['AveBedrms'] / df['AveRooms']
```

---

## 9. Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

# Ridge: tune alpha
ridge_params = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
ridge_gs = GridSearchCV(Ridge(), ridge_params, cv=5, scoring='r2')
ridge_gs.fit(X_train_s, y_train)
print("Best Ridge alpha:", ridge_gs.best_params_)

# ElasticNet: tune both alpha and l1_ratio
en_params = {
    'alpha':     [0.001, 0.01, 0.1, 1],
    'l1_ratio':  [0.1, 0.3, 0.5, 0.7, 0.9]
}
en_gs = GridSearchCV(ElasticNet(max_iter=10000), en_params, cv=5, scoring='r2')
en_gs.fit(X_train_s, y_train)
print("Best ElasticNet params:", en_gs.best_params_)
```

---

## 10. Regularization Path (How Coefficients Change with λ)

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import lasso_path, ridge_regression

# Lasso path — shows which features survive as alpha increases
alphas, coefs, _ = lasso_path(X_train_s, y_train, alphas=np.logspace(-4, 1, 100))

plt.figure(figsize=(10, 6))
for i, name in enumerate(feature_names):
    plt.plot(-np.log10(alphas), coefs[i], label=name)

plt.xlabel('-log10(alpha) → more regularization →')
plt.ylabel('Coefficient Value')
plt.title('Lasso Regularization Path')
plt.legend(loc='upper right', fontsize=8)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
```

---

## 11. Quick Decision Guide

```
Start here:
    │
    ├── Do you have many correlated features?
    │       ├── YES → Ridge or ElasticNet
    │       └── NO  → Lasso or ElasticNet
    │
    ├── Do you want automatic feature selection?
    │       ├── YES → Lasso (few features) or ElasticNet (many features)
    │       └── NO  → Ridge
    │
    └── Is p >> n (more features than samples)?
            ├── YES → ElasticNet (most stable)
            └── NO  → Try Ridge first, compare all three via CV
```

---

## 12. Key Takeaways

- **Always scale features** before applying any regularization
- **Ridge** → use when all features contribute; handles collinearity
- **Lasso** → use for automatic feature selection; produces sparse models
- **ElasticNet** → default choice for high-dimensional / correlated data
- **Cross-validation** is essential to select optimal `alpha` (and `l1_ratio`)
- The **regularization path** visualization helps understand feature importance
- Higher `alpha` = stronger regularization = simpler model (risk: underfitting)
- Lower `alpha` = weaker regularization = closer to OLS (risk: overfitting)

---

*Section 28 | Ridge, Lasso & ElasticNet ML Algorithms*