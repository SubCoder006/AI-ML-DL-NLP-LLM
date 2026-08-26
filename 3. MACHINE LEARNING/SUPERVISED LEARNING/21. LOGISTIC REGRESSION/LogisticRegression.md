# Logistic Regression — Complete Reference Notes
---

## Table of Contents
- [Logistic Regression — Complete Reference Notes](#logistic-regression--complete-reference-notes)
  - [Table of Contents](#table-of-contents)
  - [1. Why Linear Regression Fails as a Classifier (Topic 172)](#1-why-linear-regression-fails-as-a-classifier-topic-172)
  - [2. Logistic Regression — Math Intuition (Topic 173)](#2-logistic-regression--math-intuition-topic-173)
    - [2.1 Sigmoid (Logistic) Function](#21-sigmoid-logistic-function)
    - [2.2 Odds and Log-Odds (Logit)](#22-odds-and-log-odds-logit)
    - [2.3 Hypothesis Function](#23-hypothesis-function)
    - [2.4 Cost Function — Why Not MSE?](#24-cost-function--why-not-mse)
    - [2.5 Maximum Likelihood Derivation](#25-maximum-likelihood-derivation)
    - [2.6 Gradient Descent Update Rule](#26-gradient-descent-update-rule)
    - [2.7 Regularization (L1 / L2)](#27-regularization-l1--l2)
  - [3. Performance Metrics (Topic 174)](#3-performance-metrics-topic-174)
    - [3.1 Confusion Matrix](#31-confusion-matrix)
    - [3.2 Core Metrics](#32-core-metrics)
    - [3.3 When to Use What](#33-when-to-use-what)
    - [3.4 Log Loss (Cross-Entropy as a metric)](#34-log-loss-cross-entropy-as-a-metric)
  - [4. One-vs-Rest / OVR (Topics 175, 179)](#4-one-vs-rest--ovr-topics-175-179)
  - [5. Logistic Regression Implementation (Topic 176)](#5-logistic-regression-implementation-topic-176)
  - [6. Hyperparameter Tuning (Topics 177, 178)](#6-hyperparameter-tuning-topics-177-178)
    - [6.1 Grid Search CV](#61-grid-search-cv)
    - [6.2 Randomized Search CV](#62-randomized-search-cv)
  - [7. Handling Imbalanced Datasets (Topic 180)](#7-handling-imbalanced-datasets-topic-180)
    - [7.1 Detection](#71-detection)
    - [7.2 Techniques](#72-techniques)
  - [8. ROC Curve (Topic 181)](#8-roc-curve-topic-181)
    - [8.1 AUC (Area Under Curve)](#81-auc-area-under-curve)
    - [8.2 Code](#82-code)
  - [Quick Formula Cheat Sheet](#quick-formula-cheat-sheet)

---

## 1. Why Linear Regression Fails as a Classifier (Topic 172)

Linear Regression fits:

$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
$$

Problems when used for binary classification ($y \in \{0, 1\}$):

| Issue | Explanation |
|---|---|
| **Unbounded output** | $\hat{y}$ can be $< 0$ or $> 1$, but probabilities must lie in $[0, 1]$ |
| **Sensitive to outliers** | A single extreme point shifts the regression line and the decision threshold drastically |
| **Wrong loss function** | OLS minimizes squared error, assuming Gaussian residuals — invalid for categorical targets |
| **Unstable decision boundary** | The 0.5 cut-off on a straight line separates classes poorly once data is skewed |
| **Heteroscedasticity** | Residual variance isn't constant for classification targets, violating linear regression assumptions |

**Conclusion:** We need a function that squashes any real-valued input into $(0, 1)$ — the **sigmoid (logistic) function** — the foundation of Logistic Regression.

---

## 2. Logistic Regression — Math Intuition (Topic 173)

### 2.1 Sigmoid (Logistic) Function

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

where:

$$
z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n = \mathbf{w}^T \mathbf{x} + b
$$

**Properties:**
- $\sigma(z) \in (0, 1)$ for all real $z$
- $\sigma(0) = 0.5$
- $\sigma(-z) = 1 - \sigma(z)$
- Derivative: $\sigma'(z) = \sigma(z)\,(1 - \sigma(z))$

### 2.2 Odds and Log-Odds (Logit)

$$
\text{Odds} = \frac{P(y=1\mid x)}{1 - P(y=1\mid x)}
$$

$$
\text{logit}(p) = \ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n
$$

This is why Logistic Regression is a **Generalized Linear Model (GLM)** — it models the log-odds as a linear function of the inputs.

### 2.3 Hypothesis Function

$$
h_\theta(x) = P(y = 1 \mid x;\theta) = \sigma(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}}
$$

Prediction rule:

$$
\hat{y} =
\begin{cases}
1 & \text{if } h_\theta(x) \geq 0.5 \\
0 & \text{if } h_\theta(x) < 0.5
\end{cases}
$$

### 2.4 Cost Function — Why Not MSE?

Using Mean Squared Error with a sigmoid hypothesis produces a **non-convex** cost surface (multiple local minima), so Gradient Descent isn't guaranteed to converge. Instead, Logistic Regression uses **Log Loss / Binary Cross-Entropy**, derived from **Maximum Likelihood Estimation (MLE)**.

### 2.5 Maximum Likelihood Derivation

For a single training example:

$$
P(y \mid x; \theta) = h_\theta(x)^y \, (1 - h_\theta(x))^{1-y}
$$

Likelihood over $m$ examples:

$$
L(\theta) = \prod_{i=1}^{m} h_\theta(x^{(i)})^{y^{(i)}} \, \left(1 - h_\theta(x^{(i)})\right)^{1-y^{(i)}}
$$

Taking the log (Log-Likelihood):

$$
\ell(\theta) = \sum_{i=1}^{m} \left[ y^{(i)} \log h_\theta(x^{(i)}) + (1-y^{(i)}) \log\left(1 - h_\theta(x^{(i)})\right) \right]
$$

Maximizing log-likelihood $\equiv$ minimizing **negative log-likelihood**, giving the cost function:

$$
J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log h_\theta(x^{(i)}) + (1-y^{(i)}) \log\left(1 - h_\theta(x^{(i)})\right) \right]
$$

This function is **convex**, guaranteeing a global minimum.

### 2.6 Gradient Descent Update Rule

Partial derivative of $J(\theta)$ w.r.t. $\theta_j$:

$$
\frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)}
$$

Update rule (applied simultaneously for all $j$):

$$
\theta_j := \theta_j - \alpha \, \frac{\partial J(\theta)}{\partial \theta_j}
$$

where $\alpha$ is the **learning rate**.

### 2.7 Regularization (L1 / L2)

To prevent overfitting:

**L2 (Ridge):**

$$
J(\theta) = -\frac{1}{m}\sum_{i=1}^{m}\Big[y^{(i)}\log h_\theta(x^{(i)}) + (1-y^{(i)})\log(1-h_\theta(x^{(i)}))\Big] + \frac{\lambda}{2m}\sum_{j=1}^{n}\theta_j^2
$$

**L1 (Lasso):**

$$
J(\theta) = -\frac{1}{m}\sum_{i=1}^{m}\Big[y^{(i)}\log h_\theta(x^{(i)}) + (1-y^{(i)})\log(1-h_\theta(x^{(i)}))\Big] + \frac{\lambda}{m}\sum_{j=1}^{n}|\theta_j|
$$

In `sklearn`, this is controlled by `penalty` (`'l1'`, `'l2'`, `'elasticnet'`, `'none'`) and inverse regularization strength `C` (note: $C = \frac{1}{\lambda}$ — smaller `C` means stronger regularization).

---

## 3. Performance Metrics (Topic 174)

### 3.1 Confusion Matrix

| | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

### 3.2 Core Metrics

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

$$
\text{Recall (Sensitivity / TPR)} = \frac{TP}{TP + FN}
$$

$$
\text{Specificity (TNR)} = \frac{TN}{TN + FP}
$$

$$
F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

**Generalized $F_\beta$ score** (weights recall $\beta$ times more than precision):

$$
F_\beta = (1+\beta^2) \cdot \frac{\text{Precision} \cdot \text{Recall}}{\beta^2 \cdot \text{Precision} + \text{Recall}}
$$

### 3.3 When to Use What

| Scenario | Preferred Metric |
|---|---|
| Balanced classes | Accuracy |
| Cost of False Positive is high (e.g. spam detection) | Precision |
| Cost of False Negative is high (e.g. cancer detection) | Recall |
| Need balance between Precision & Recall | F1-Score |
| Imbalanced classes / ranking quality | ROC-AUC, PR-AUC |

### 3.4 Log Loss (Cross-Entropy as a metric)

$$
\text{LogLoss} = -\frac{1}{m}\sum_{i=1}^{m}\Big[y^{(i)}\log(\hat{p}^{(i)}) + (1-y^{(i)})\log(1-\hat{p}^{(i)})\Big]
$$

Lower log loss means better-calibrated probability predictions.

---

## 4. One-vs-Rest / OVR (Topics 175, 179)

For multiclass classification with $K$ classes, OVR trains **$K$ independent binary classifiers**:

$$
h_\theta^{(k)}(x) = P(y = k \mid x; \theta), \quad k = 1, 2, \dots, K
$$

Each classifier $k$ is trained to distinguish **class $k$** vs **all other classes combined**.

**Final prediction:**

$$
\hat{y} = \arg\max_{k} \; h_\theta^{(k)}(x)
$$

| Pros | Cons |
|---|---|
| Simple, interpretable | Each sub-classifier may face class imbalance (1 vs rest) |
| Works with any binary classifier | $K$ models to train — more compute |
| Easy to add new classes | Probabilities across classifiers aren't always well-calibrated/comparable |

**Alternative:** Softmax / Multinomial Logistic Regression (`multi_class='multinomial'` in sklearn) trains one unified model using the **softmax function**:

$$
P(y=k\mid x) = \frac{e^{\theta_k^T x}}{\sum_{j=1}^{K} e^{\theta_j^T x}}
$$

---

## 5. Logistic Regression Implementation (Topic 176)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# 1. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Feature scaling (important for gradient-based solvers)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Model
model = LogisticRegression(
    penalty='l2',
    C=1.0,
    solver='lbfgs',       # 'liblinear', 'saga', 'newton-cg', 'sag'
    multi_class='auto',   # 'ovr' or 'multinomial'
    max_iter=1000
)
model.fit(X_train_scaled, y_train)

# 4. Predict
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# 5. Evaluate
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

**Solver guide:**

| Solver | Penalty Support | Best For |
|---|---|---|
| `liblinear` | L1, L2 | Small datasets, binary classification |
| `lbfgs` | L2, none | Default, multinomial, medium datasets |
| `saga` | L1, L2, elasticnet | Large datasets, sparse data |
| `newton-cg` | L2, none | Multinomial, medium datasets |
| `sag` | L2, none | Large datasets |

---

## 6. Hyperparameter Tuning (Topics 177, 178)

### 6.1 Grid Search CV

Exhaustively tries **every combination** of specified hyperparameter values using k-fold cross-validation.

$$
\text{Total fits} = (\text{number of param combinations}) \times (\text{number of CV folds})
$$

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear']
}

grid_search = GridSearchCV(
    estimator=LogisticRegression(max_iter=1000),
    param_grid=param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)
grid_search.fit(X_train_scaled, y_train)

print(grid_search.best_params_)
print(grid_search.best_score_)
```

### 6.2 Randomized Search CV

Samples a **fixed number** (`n_iter`) of random combinations from the parameter distributions — far cheaper than Grid Search for large search spaces.

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

param_dist = {
    'C': uniform(loc=0.01, scale=100),
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear']
}

random_search = RandomizedSearchCV(
    estimator=LogisticRegression(max_iter=1000),
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring='f1',
    random_state=42,
    n_jobs=-1
)
random_search.fit(X_train_scaled, y_train)
```

| | Grid Search | Randomized Search |
|---|---|---|
| Coverage | Exhaustive | Sampled subset |
| Cost | High (exponential in params) | Controlled by `n_iter` |
| Best for | Small search space | Large / continuous search space |
| Guarantee | Finds best combo *within grid* | Probabilistic — may miss optimum |

---

## 7. Handling Imbalanced Datasets (Topic 180)

When one class dominates (e.g. 95% negative, 5% positive), accuracy becomes misleading.

### 7.1 Detection

$$
\text{Imbalance Ratio} = \frac{\text{majority class count}}{\text{minority class count}}
$$

### 7.2 Techniques

**A. Resampling**
- **Oversampling minority class:** Random Oversampling, **SMOTE** (Synthetic Minority Oversampling Technique)
- **Undersampling majority class:** Random Undersampling, Tomek Links, NearMiss

**B. Class Weights** — penalize misclassifying the minority class more heavily:

$$
J(\theta) = -\frac{1}{m}\sum_{i=1}^{m} w_{y^{(i)}} \Big[y^{(i)}\log h_\theta(x^{(i)}) + (1-y^{(i)})\log(1-h_\theta(x^{(i)}))\Big]
$$

```python
model = LogisticRegression(class_weight='balanced')
```

`'balanced'` mode sets weights as:

$$
w_k = \frac{n_{\text{samples}}}{K \cdot n_k}
$$

where $n_k$ is the number of samples in class $k$, and $K$ is the number of classes.

**C. SMOTE example**

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train_scaled, y_train)
```

**D. Better evaluation metrics for imbalance**
- Precision, Recall, F1 (avoid plain accuracy)
- ROC-AUC, **PR-AUC** (more informative than ROC-AUC under heavy imbalance)
- Confusion matrix inspection per class

---

## 8. ROC Curve (Topic 181)

The **Receiver Operating Characteristic (ROC)** curve plots:

$$
\text{TPR (Recall)} = \frac{TP}{TP+FN} \quad \text{vs.} \quad \text{FPR} = \frac{FP}{FP+TN}
$$

at every possible classification threshold $t \in [0, 1]$.

### 8.1 AUC (Area Under Curve)

$$
\text{AUC} = \int_0^1 \text{TPR}(\text{FPR}) \, d(\text{FPR})
$$

Interpretation:

| AUC | Meaning |
|---|---|
| 1.0 | Perfect classifier |
| 0.9 – 1.0 | Excellent |
| 0.8 – 0.9 | Good |
| 0.7 – 0.8 | Fair |
| 0.5 | No better than random guessing |
| < 0.5 | Worse than random (inverted predictions) |

AUC equals the probability that a randomly chosen positive sample is ranked higher than a randomly chosen negative sample:

$$
\text{AUC} = P\big(\hat{p}(x^+) > \hat{p}(x^-)\big)
$$

### 8.2 Code

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc:.3f})')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')  # baseline
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

## Quick Formula Cheat Sheet

| Concept | Formula |
|---|---|
| Sigmoid | $\sigma(z) = \dfrac{1}{1+e^{-z}}$ |
| Log-odds | $\ln\left(\dfrac{p}{1-p}\right) = \theta^T x$ |
| Cost (Log Loss) | $J(\theta) = -\dfrac{1}{m}\sum \big[y\log h_\theta(x) + (1-y)\log(1-h_\theta(x))\big]$ |
| Gradient | $\dfrac{\partial J}{\partial \theta_j} = \dfrac{1}{m}\sum (h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)}$ |
| Accuracy | $\dfrac{TP+TN}{TP+TN+FP+FN}$ |
| Precision | $\dfrac{TP}{TP+FP}$ |
| Recall | $\dfrac{TP}{TP+FN}$ |
| F1 Score | $2 \cdot \dfrac{P \cdot R}{P+R}$ |
| Softmax | $\dfrac{e^{\theta_k^Tx}}{\sum_j e^{\theta_j^Tx}}$ |
| Class weight (balanced) | $w_k = \dfrac{n_{samples}}{K \cdot n_k}$ |

---

*Notes generated for Section 30: Logistic Regression — topics 172–181.*