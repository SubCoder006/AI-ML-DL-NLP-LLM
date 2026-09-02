# 🎓 Machine Learning — Complete Exam Revision Notes

> Compiled and organized from your notes, mapped to your syllabus (Module I, II, IV, V — a Module III on Bayesian/Instance-based/SVM classifiers is included separately since it's standard in this sequence). Topics **not present in your uploaded notes** (Design of a Learning System, Concept Learning, GMM, LDA) have been added in full since they're classic exam topics for this syllabus.

---

## 📑 Contents

- [MODULE I — Introduction to ML](#module-i--introduction-to-ml)
- [MODULE II — Regression](#module-ii--regression)
- [MODULE III — Classification: Bayesian & Instance-Based Learning](#module-iii--classification-bayesian--instance-based-learning)
- [MODULE IV — Trees and Unsupervised Learning](#module-iv--trees-and-unsupervised-learning)
- [MODULE V — Dimensionality Reduction](#module-v--dimensionality-reduction)
- [Appendix A — Math Foundations](#appendix-a--math-foundations)
- [Appendix B — Probability & Statistics](#appendix-b--probability--statistics)
- [Final Exam Cheat Sheet](#-final-exam-cheat-sheet)

---
---

# MODULE I — Introduction to ML

## 1.1 What is Machine Learning?

> **Definition:** ML is the field of study that gives computers the ability to learn from data/experience without being explicitly programmed — a program **learns** if its **performance (P)** at some **task (T)** improves with **experience (E)** (Tom Mitchell's formal definition).

**Well-posed learning problem = (T, P, E)**

| Symbol | Meaning | Example (Spam filter) |
|---|---|---|
| T (Task) | What the system does | Classify emails as spam/not spam |
| P (Performance) | How success is measured | % of emails correctly classified |
| E (Experience) | Data used to learn | Labeled emails (past spam/ham) |

### Big picture pipeline
```
Math & Stats → Python → Data → ML Algorithms → Deep Learning → Deployment
```

## 1.2 Types of Learning

| Type | Data | Goal | Examples |
|---|---|---|---|
| **Supervised Learning** | Labeled (X, y) | Learn mapping f(X) → y | Linear/Logistic Regression, Decision Trees, SVM |
| **Unsupervised Learning** | Unlabeled (X only) | Find structure/patterns | K-Means, PCA, Hierarchical Clustering |
| **Reinforcement Learning (RL)** | Agent + environment + reward | Learn a policy that maximizes cumulative reward | Game AI, Robotics |

**Reinforcement Learning loop:**
```
Agent → takes Action → Environment changes → Agent gets Reward
       ←←←←←← learns to maximize reward ←←←←←←
```
Key RL terms: **State, Action, Reward, Policy, Q-value.**

**Supervised** further splits into:
- **Regression** — predict a continuous value (house price)
- **Classification** — predict a discrete category (spam/not spam)

## 1.3 Design of a Learning System (classic exam topic)

Steps to design a learning system (e.g., a checkers-playing program):

1. **Choosing the Training Experience (E)** — direct vs indirect feedback; is a teacher present; is the training data representative of the distribution the system will be tested on?
2. **Choosing the Target Function** — what exactly should be learned? e.g., `ChooseMove: Board → Move`, or an evaluation function `V: Board → ℝ` that scores how good a board state is.
3. **Choosing a Representation for the Target Function** — e.g., represent V̂ as a linear combination of board features:
   $$\hat{V}(b) = w_0 + w_1x_1 + w_2x_2 + \cdots + w_nx_n$$
   (trade-off between expressiveness and size of hypothesis space)
4. **Choosing a Function Approximation Algorithm**
   - Generate training examples (estimate training values, e.g. using successor board's value)
   - Adjust weights to best fit training examples — usually via a **gradient-descent/LMS (least mean squares) weight-update rule**
5. **The Final Design** — four modules that interact:
   - **Performance System** — uses the learned target function to solve the task
   - **Critic** — generates training examples from the trace (labels states with training values)
   - **Generalizer** — outputs a hypothesis (estimate of target function) from training examples
   - **Experiment Generator** — proposes new problems for the Performance System to explore

```
        ┌────────────────────┐
        │  Experiment         │
        │  Generator           │
        └─────────┬───────────┘
                   │ new problem
        ┌──────────▼──────────┐        ┌──────────────┐
        │  Performance System  │───────▶│    Critic     │
        └──────────┬───────────┘  trace └──────┬────────┘
                   │ hypothesis                │ training examples
        ┌──────────▼──────────┐◀──────────────┘
        │    Generalizer        │
        └────────────────────────┘
```

## 1.4 Perspectives and Issues in Machine Learning

**Perspective:** ML can be viewed as searching a very large **hypothesis space** (defined by the representation chosen) to find the hypothesis that best fits training examples plus prior knowledge/constraints.

**Key Issues in ML:**
| Issue | Description |
|---|---|
| **Which algorithm to use?** | No single algorithm works best for all problems (No Free Lunch theorem) |
| **How much training data is enough?** | Relates to sample complexity; more complex hypothesis space → more data needed |
| **When/how can prior knowledge held by the learner guide the process?** | Prior knowledge can reduce the effective hypothesis space |
| **What's the best strategy for choosing the next training experience?** | Active learning, experiment design |
| **How to reduce the learning task to function approximation problems?** | Choosing the right target function representation |
| **How can the learner automatically alter its representation?** | Adapting hypothesis space during learning (meta-learning) |
| **Overfitting vs Underfitting** | Model too complex vs too simple (see Module II) |
| **Bias–Variance tradeoff** | Balancing systematic error vs sensitivity to training data |
| **Computational complexity** | Time/memory cost of training & inference |

## 1.5 Concept Learning

> **Definition:** Concept Learning is the task of inferring a **boolean-valued function** (a *concept*, e.g., "EnjoySport = Yes/No") from training examples of its input/output.

- A **hypothesis h** is a conjunction of constraints on instance attributes.
- Each attribute constraint can be: a specific value, `?` (any value accepted), or `∅` (no value accepted / never true).
- **Hypothesis space H** = set of all possible hypotheses.
- **Instance space X** = set of all possible instances.

### General-to-Specific Ordering
A hypothesis $h_1$ is **more general than or equal to** $h_2$ ($h_1 \geq_g h_2$) if every instance satisfying $h_2$ also satisfies $h_1$.
- Most general hypothesis: `<?, ?, ?, ?, ?, ?>` (accepts everything)
- Most specific hypothesis: `<∅, ∅, ∅, ∅, ∅, ∅>` (accepts nothing)

### FIND-S Algorithm (finds the maximally specific hypothesis)
```
1. Initialize h to the most specific hypothesis in H
2. For each positive training example x:
     For each attribute constraint aᵢ in h:
         If x satisfies aᵢ → do nothing
         Else → replace aᵢ with the next more general constraint satisfied by x
3. Output hypothesis h
```
- **Ignores negative examples** entirely.
- Guaranteed to output the most specific hypothesis consistent with positive examples (assuming target concept is in H, no noise).
- **Limitation:** can't tell if it has learned the *only* correct hypothesis, can't detect inconsistent training data, and ignores negative examples.

### Candidate Elimination Algorithm
Maintains the **Version Space** — the set of *all* hypotheses consistent with all training examples seen so far — using two boundary sets:
- **S (Specific boundary):** most specific hypotheses consistent with data
- **G (General boundary):** most general hypotheses consistent with data

```
Initialize G to the set of maximally general hypotheses
Initialize S to the set of maximally specific hypotheses

For each training example d:
  If d is POSITIVE:
      Remove from G any hypothesis inconsistent with d
      For each hypothesis s in S inconsistent with d:
          Remove s; add minimal generalizations of s consistent with d
          (and having some more general member of G)
          Remove from S any hypothesis more general than another in S
  If d is NEGATIVE:
      Remove from S any hypothesis inconsistent with d
      For each hypothesis g in G inconsistent with d:
          Remove g; add minimal specializations of g consistent with d
          (and having some more specific member of S)
          Remove from G any hypothesis less general than another in G
```
The **Version Space** = all hypotheses between S and G boundaries (inclusive). Converges to the target concept as more examples arrive (if it's in H and data is noise-free).

### Inductive Bias
The set of assumptions a learner uses to predict outputs for unseen inputs, beyond the training data (needed because pure induction from finite data is otherwise underdetermined). E.g., FIND-S's bias = target concept can be represented as a conjunction of attribute constraints.

## 1.6 Model-Based vs Instance-Based Learning

| Aspect | Model-Based (Eager) | Instance-Based (Lazy) |
|---|---|---|
| Learning type | Eager — builds explicit model | Lazy — no explicit training |
| Key idea | Learn function f(X) → Y | Store instances, compare via similarity |
| Training time | High | Low (~none) |
| Prediction time | Low | High (search dataset) |
| Memory usage | Low | High (stores entire dataset) |
| Examples | Linear/Logistic Regression, Decision Trees, NN | KNN, Case-Based Reasoning |
| One-liner | "Learn the formula" | "Remember the examples" |

---
---

# MODULE II — Regression

## 2.1 Simple & Multiple Linear Regression

$$\hat{y} = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p$$

- **OLS closed form (simple LR):**
$$\beta_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}, \qquad \beta_0 = \bar{y}-\beta_1\bar{x}$$
- **Normal Equation (multiple LR):**
$$\hat{\boldsymbol\beta} = (X^\top X)^{-1}X^\top y$$
- Fails when $X^\top X$ is singular → multicollinearity or p > n → fix with **Ridge**.

**Assumptions of Linear Regression (exam favorite):**
1. Linearity 2. Independence of errors 3. Homoscedasticity (constant variance) 4. Normality of residuals 5. No multicollinearity

### Cost Function & Gradient Descent
$$J(\beta) = \frac{1}{2n}\sum(\hat{y}_i - y_i)^2 \qquad \beta_j \leftarrow \beta_j - \alpha\frac{\partial J}{\partial \beta_j}$$

| Variant | Data/step | Notes |
|---|---|---|
| Batch GD | All N | Stable, slow |
| Stochastic GD | 1 | Fast, noisy |
| Mini-batch GD | k (32–256) | **Standard in practice** |

### Performance Metrics (Regression)
| Metric | Formula | Notes |
|---|---|---|
| MAE | $\frac1n\sum\|y_i-\hat y_i\|$ | Robust to outliers |
| MSE | $\frac1n\sum(y_i-\hat y_i)^2$ | Used as training loss (differentiable) |
| RMSE | $\sqrt{MSE}$ | Same unit as target, penalizes large errors |
| R² | $1-\frac{SS_{res}}{SS_{tot}}$ | Variance explained |
| Adjusted R² | $1-(1-R^2)\frac{n-1}{n-p-1}$ | Penalizes useless features |

### Polynomial Regression
$$\hat y = \beta_0+\beta_1x+\beta_2x^2+\cdots+\beta_dx^d$$
Non-linear in x, **linear in β** → still solvable by OLS. Higher degree → lower bias, higher variance (risk of overfitting). Use `PolynomialFeatures` + `Pipeline` (prevents data leakage in CV).

## 2.2 Overfitting, Underfitting & Bias-Variance

$$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \sigma^2(\text{irreducible noise})$$

| | Underfitting (High Bias) | Overfitting (High Variance) |
|---|---|---|
| Train error | High | Very low |
| Test error | High | High |
| Fix | More features, complex model, less regularization | Regularization, more data, feature selection, CV, early stopping |

## 2.3 Regularization: Ridge, Lasso, ElasticNet

| | Ridge (L2) | Lasso (L1) | ElasticNet |
|---|---|---|---|
| Penalty | $\lambda\sum\beta_j^2$ | $\lambda\sum\|\beta_j\|$ | both, weighted by `l1_ratio` |
| Coefficients → 0? | Never (shrinks only) | Yes → feature selection | Yes |
| Correlated features | Handled well | Unstable (picks one) | Handled well (selects groups) |
| Solution | Closed-form | Coordinate descent | Coordinate descent |
| Best for | All features matter | Few features matter, p>>n | Mixed/high-dim, correlated + sparse |

> **Why L1 gives sparsity:** L1's constraint region has corners on the axes → optimum often lands exactly on an axis (coefficient = 0). L2's constraint region is a smooth sphere → rarely lands exactly on an axis.

`sklearn`: `Ridge(alpha=λ)`, `Lasso(alpha=λ)`, `ElasticNet(alpha, l1_ratio)`. **Always scale features before regularizing.**

### Cross-Validation types
| Type | Idea |
|---|---|
| K-Fold | Split into K folds, rotate validation fold |
| Stratified K-Fold | Preserves class proportions (classification) |
| Leave-One-Out | K = n, expensive |
| Time Series Split | Respects temporal order, no leakage |

---
---

# MODULE III — Classification: Bayesian & Instance-Based Learning

## 3.1 Logistic Regression

Used for **classification** (despite the name). Squashes linear output into (0,1) via **sigmoid**:
$$\sigma(z)=\frac1{1+e^{-z}}, \quad z = w^\top x+b$$

- **Log-odds (logit):** $\ln\frac{p}{1-p} = \theta^\top x$ → this is why LR is a **Generalized Linear Model**.
- **Cost function (Log Loss / Binary Cross-Entropy)**, derived via Maximum Likelihood (MSE would be non-convex here):
$$J(\theta) = -\frac1m\sum\left[y\log h_\theta(x) + (1-y)\log(1-h_\theta(x))\right]$$
- Regularized with L1/L2 same as linear regression; sklearn parameter `C = 1/λ` (**smaller C = stronger regularization**).
- **Multiclass:** One-vs-Rest (OVR, train K binary classifiers) or **Softmax/Multinomial** 
$$
P(y=k \mid x)
=
\frac{e^{\theta_k^T x}}
{\sum_j e^{\theta_j^T x}}
$$

### Classification Metrics (also apply to SVM, NB, KNN, Trees)
| | Predicted + | Predicted − |
|---|---|---|
| Actual + | TP | FN |
| Actual − | FP | TN |

$$Accuracy=\frac{TP+TN}{All} \quad Precision=\frac{TP}{TP+FP} \quad Recall=\frac{TP}{TP+FN} \quad F_1=2\cdot\frac{P\cdot R}{P+R}$$

| Scenario | Preferred metric |
|---|---|
| Balanced classes | Accuracy |
| FP costly (spam) | Precision |
| FN costly (cancer) | Recall |
| Need balance | F1 |
| Imbalanced / ranking | ROC-AUC, PR-AUC |

**ROC Curve:** TPR (Recall) vs FPR at all thresholds. **AUC** = P(random positive ranks higher than random negative). AUC 0.5 = random guessing, 1.0 = perfect.

**Handling imbalanced data:** resampling (SMOTE, oversampling/undersampling), `class_weight='balanced'`, use F1/ROC-AUC/PR-AUC instead of accuracy.

## 3.2 Naive Bayes

> Based on **Bayes' Theorem**, assumes all features are **conditionally independent** given the class ("naive" assumption).

$$P(\text{class}\mid\text{data}) = \frac{P(\text{data}\mid\text{class})\cdot P(\text{class})}{P(\text{data})}$$

Predict class = argmax of posterior probability.

| Variant | Data type |
|---|---|
| Gaussian NB | Continuous (assumes normal distribution) |
| Multinomial NB | Discrete counts (text/word frequency) |
| Bernoulli NB | Binary (present/absent) |

**Pros:** fast, works with small data, handles high dimensions (text) well. **Con:** independence assumption rarely fully true.

## 3.3 Support Vector Machine (SVM)

- Finds the hyperplane $w^\top x + b = 0$ that **maximizes the margin** between classes.
- **Support vectors** = points closest to hyperplane; only these determine it.
- Margin $=\frac{2}{\|w\|}$ → maximizing margin ⟺ minimizing $\|w\|^2$.

**Hard vs Soft Margin:**
| | Hard Margin | Soft Margin |
|---|---|---|
| Assumption | Perfectly separable | Some misclassification allowed (slack ξ) |
| Regularization param C | N/A | Large C = less tolerance (narrow margin, overfit risk); Small C = more tolerance (wide margin) |

**Cost (Hinge Loss):**
$$\min_{w,b}\frac12\|w\|^2 + C\sum\max(0, 1-y_i(w^\top x_i+b))$$

**Kernel Trick** (for non-linear data — compute dot products in high-dim space without explicit transform):
| Kernel | Formula | Use |
|---|---|---|
| Linear | $x_i^Tx_j$ | Linearly separable |
| Polynomial | $(x_i^Tx_j+c)^d$ | Curved boundaries |
| RBF (Gaussian) | $e^{-\gamma\|x_i-x_j\|^2}$ | Most common, non-linear |
| Sigmoid | $\tanh(\alpha x_i^Tx_j+c)$ | Neural-net-like |

`gamma` high → tighter fit (overfit risk). **SVR** fits within an ε-tube, only points outside the tube penalized/become support vectors. **Feature scaling is essential** for SVM (distance-based).

## 3.4 K-Nearest Neighbors (KNN)

- **Instance-based / lazy learner** — no training phase, stores data, computes distances at prediction time.
- **Classification:** majority vote of K nearest neighbors. **Regression:** mean of K neighbors.
- **Distance metrics:** Euclidean (default), Manhattan, Minkowski (general, p-parameter), Hamming (categorical), Cosine (text/sparse).

| K | Effect |
|---|---|
| Small K (e.g. 1) | Low bias, high variance → overfits, noise-sensitive |
| Large K | High bias, low variance → underfits, smoother boundary |

Use **odd K** for binary classification (avoid ties); choose via cross-validation (elbow in error-vs-K plot). **Weighted KNN:** weight = 1/distance.

**Feature scaling is mandatory** (distance-based). Suffers from **curse of dimensionality**.

**Speed-up structures:**
| | KD-Tree | Ball Tree |
|---|---|---|
| Partition | Axis-aligned boxes | Hyperspheres |
| Best for | Low-dim (<~20) | Medium–high-dim |
| Metrics | Mostly Euclidean | Many metrics |

---
---

# MODULE IV — Trees and Unsupervised Learning

## 4.1 Decision Trees

- Splits data into subsets by feature values → tree of **Root → Internal (decision) → Leaf (output)** nodes.
- White-box / interpretable, but **prone to overfitting**.

### Impurity Measures
$$Entropy(S) = -\sum p_i\log_2 p_i \qquad(\text{0 to 1, binary})$$
$$Gini(S) = 1-\sum p_i^2 \qquad(\text{0 to 0.5, binary})$$

$$\text{Information Gain}(S,A) = Entropy(S) - \sum_v \frac{|S_v|}{|S|}Entropy(S_v)$$

| | Entropy | Gini |
|---|---|---|
| Speed | Slower (log) | Faster |
| Used in | ID3, C4.5 | CART (sklearn default) |
| Sensitivity | Slightly more to imbalance | Less |

**Numerical feature splits:** sort values → try **midpoints** between consecutive values as thresholds → pick threshold with best impurity reduction (computationally expensive).

### Pruning (to reduce overfitting)
| Pre-Pruning | Post-Pruning |
|---|---|
| Stop early: `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_leaf_nodes` | Grow full tree, then trim via **Cost Complexity Pruning** (`ccp_alpha`) |
| Faster, risk underfitting | Better generalization, costlier |

### Regression Trees
Split to minimize **variance/MSE** instead of Gini/Entropy; leaf value = **mean of targets** in that region → step-function output.

```python
DecisionTreeClassifier(criterion='gini', max_depth=5)
DecisionTreeRegressor(max_depth=5)
```
No feature scaling needed. Sensitive to noisy data (**high variance model**).

## 4.2 Ensemble Learning: Random Forest & AdaBoost

### Bagging vs Boosting
| Aspect | Bagging | Boosting |
|---|---|---|
| Training | Parallel, independent | Sequential, each fixes previous errors |
| Sampling | Bootstrap (with replacement) | Weighted (misclassified ↑ weight) |
| Goal | Reduce variance | Reduce bias (& variance) |
| Combine | Majority vote / average | Weighted vote/sum |
| Overfitting risk | Lower | Higher |
| Example | **Random Forest** | **AdaBoost, Gradient Boosting, XGBoost** |

### Random Forest = Bagging + Feature Randomness
- Each tree: bootstrap sample of rows + random subset of features per split (`max_features`) → decorrelates trees.
- **OOB (Out-of-Bag)** samples give a free validation estimate.
- Classification → majority vote; Regression → average.
- **Feature Importance:** Mean Decrease in Impurity, or (more reliable) **Permutation Importance**.
- No scaling needed; robust to outliers & missing data.

| Hyperparameter | Effect |
|---|---|
| `n_estimators` | More trees = stable, diminishing returns |
| `max_depth` | Deeper = more variance |
| `max_features` | Fewer = more decorrelated, more bias |
| `min_samples_leaf` | Higher = smoother predictions |

### AdaBoost (Adaptive Boosting)
- Sequential ensemble of **decision stumps** (depth-1 trees).
$$F(x)=\sum_t \alpha_t h_t(x)$$
- **Amount of say:** $\alpha_t = \frac12\ln\left(\frac{1-\varepsilon_t}{\varepsilon_t}\right)$ — $\varepsilon_t\to0 \Rightarrow \alpha_t$ large; $\varepsilon_t=0.5\Rightarrow\alpha_t=0$.
- **Weight update:** misclassified points get weight × $e^{\alpha_t}$ (↑); correct get × $e^{-\alpha_t}$ (↓) → normalize → resample (weighted).
- Final prediction: $H(x)=\text{sign}\left(\sum\alpha_t h_t(x)\right)$ (classification) or weighted avg (regression).
- **Higher overfitting risk** than Random Forest (sensitive to noise/outliers).

| | AdaBoost | Random Forest |
|---|---|---|
| Type | Boosting | Bagging |
| Base learner | Stumps (depth 1) | Full-depth trees |
| Tree weight | Varies ($\alpha_t$) | Equal |

## 4.3 Unsupervised Learning — Overview

No labels; goal = find structure in raw data.

| Algorithm | Type | Use case |
|---|---|---|
| K-Means | Clustering (centroid-based) | Customer segmentation |
| Hierarchical | Clustering (tree-based) | Gene expression, nested groups |
| DBSCAN | Clustering (density-based) | Anomaly/outlier detection, arbitrary shapes |
| GMM | Clustering (probabilistic) | Soft/overlapping clusters |
| PCA | Dimensionality reduction | Visualization, compression |

## 4.4 K-Means Clustering

**Algorithm:**
1. Initialize K centroids
2. **Assign** each point to nearest centroid
3. **Update** centroid = mean of assigned points
4. Repeat 2–3 until convergence

**Distance metrics:** Euclidean (straight-line), Manhattan (grid/city-block).

**Choosing K — Elbow Method:**
$$WCSS = \sum(\text{distance to nearest centroid})^2$$
Plot WCSS vs K → pick the "elbow" (sharp flattening point).

**Random Initialization Trap:** bad random centroids → bad clustering. **Fix: K-Means++** — spreads out initial centroids smartly.

## 4.5 Hierarchical Clustering

- No centroids needed; builds a **tree (dendrogram)** of nested clusters.
- **Agglomerative** (bottom-up: merge closest points/clusters repeatedly) vs **Divisive** (top-down: split one big cluster).
- **Dendrogram:** x-axis = points, y-axis = merge distance.
- **Choosing K:** draw a horizontal threshold line; count vertical lines it crosses (longest vertical line with no horizontal crossing = natural cut point).

| | K-Means | Hierarchical |
|---|---|---|
| Need K upfront | Yes | No |
| Centroids | Yes | No |
| Speed (large data) | Faster | Slower (all-pairs) |

## 4.6 DBSCAN (Density-Based Clustering)

Groups **densely packed** points; marks sparse-region points as **noise/outliers**. Finds **arbitrary-shaped** (non-convex) clusters, unlike K-Means.

**Parameters:** ε (neighborhood radius), `minPts` (min points for density).

| Point type | Definition |
|---|---|
| **Core point** | ≥ minPts within ε radius |
| **Border point** | < minPts within ε, but within ε of a core point |
| **Noise/Outlier** | Neither core nor reachable from a core point |

**Pros:** no K needed, arbitrary shapes, handles outliers, no shape assumption.
**Cons:** struggles with varying densities, sensitive to ε/minPts, poor in high dimensions.

## 4.7 Gaussian Mixture Models (GMM)

> **Definition:** A **probabilistic, soft clustering** method that models the data as a mixture of K multivariate Gaussian (normal) distributions — each cluster is described by a mean **μ**, covariance **Σ**, and a mixing weight **π** (prior probability of that cluster).

$$p(x) = \sum_{k=1}^{K}\pi_k\,\mathcal N(x\mid\mu_k,\Sigma_k), \qquad \sum_k\pi_k=1$$

- Unlike K-Means (hard assignment, spherical clusters, equal-size assumption), GMM gives **soft assignments** — a probability that each point belongs to each cluster — and can model **elliptical clusters** of different sizes/orientations via the covariance matrix.
- **Trained via Expectation-Maximization (EM):**
  1. **E-step:** compute responsibility (posterior probability) of each cluster for each point, given current parameters.
  2. **M-step:** update $\mu_k, \Sigma_k, \pi_k$ to maximize expected log-likelihood given the responsibilities.
  3. Repeat until convergence (log-likelihood stops increasing).
- **Choosing K:** use **AIC/BIC** (Bayesian Information Criterion) instead of the elbow method.
- **K-Means is a special case of GMM** — where covariances are spherical & equal, and assignment is hard (arg-max instead of soft probability).

```python
from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=3, covariance_type='full')
gmm.fit(X)
labels = gmm.predict(X)              # hard labels
probs  = gmm.predict_proba(X)        # soft cluster probabilities
```

| | K-Means | GMM |
|---|---|---|
| Assignment | Hard | Soft (probabilistic) |
| Cluster shape | Spherical, equal size | Elliptical, varying size/orientation |
| Basis | Distance to centroid | Probability density |
| Algorithm | Iterative (Lloyd's) | Expectation-Maximization |

## 4.8 Clustering Evaluation — Silhouette Score

For point $i$ in cluster $C_I$:
$$a(i)=\text{avg. distance to other points in own cluster} \qquad b(i)=\min_{J\ne I}\ \text{avg. distance to points in nearest other cluster}$$
$$s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}} \in [-1,1]$$

| s(i) | Meaning |
|---|---|
| ≈ +1 | Well-clustered (far from other clusters) |
| ≈ 0 | On the boundary between two clusters |
| ≈ −1 | Likely misclassified (closer to another cluster) |

Average over all points = overall **Silhouette Score** of the clustering — higher is better. Works for K-Means, Hierarchical, DBSCAN, GMM.

---
---

# MODULE V — Dimensionality Reduction

## 5.1 Curse of Dimensionality

- As feature count ↑, feature-space volume grows exponentially but data stays sparse.
- **Effects:** distances become meaningless (all points look equidistant), need exponentially more data, higher overfitting risk, more compute/storage.
- **Fix:** reduce dimensions via **Feature Selection** (keep subset of original features) or **Feature Extraction** (create new combined features).

| | Feature Selection | Feature Extraction |
|---|---|---|
| Idea | Pick subset of existing features | Combine features into new ones |
| Interpretability | High | Lower |
| Examples | Forward/Backward selection, Chi-square, Correlation filter | **PCA, LDA**, t-SNE, Autoencoders |

## 5.2 Principal Component Analysis (PCA) — Unsupervised

> **Goal:** find new orthogonal axes (**Principal Components**) along which data variance is **maximized** — PC1 = max variance direction, PC2 = next-highest variance, ⊥ to PC1, etc. Project data onto top-k PCs → dimensionality reduced with minimal information loss.

**Steps:**
1. **Standardize** data: $z=\frac{x-\mu}{\sigma}$
2. Compute **covariance matrix** $\Sigma = \frac1n X^TX$
3. **Eigen-decompose:** $\Sigma v = \lambda v$ → eigenvector $v$ = PC direction, eigenvalue $\lambda$ = variance captured
4. Sort eigenvectors by eigenvalue (descending); pick top k
5. Project: $X_{new}=X\cdot W$ (W = top-k eigenvectors)

$$\text{Explained Variance Ratio} = \frac{\lambda_i}{\sum_j\lambda_j}$$

Choose k via **Scree plot** (cumulative explained variance vs #components) — pick where it crosses ~90–95%.

```python
from sklearn.decomposition import PCA
X_pca = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(X))
```

**PCA is unsupervised** — it doesn't use class labels; it only maximizes variance.

## 5.3 Linear Discriminant Analysis (LDA) — Supervised

> **Definition:** LDA is a **supervised** dimensionality-reduction (and classification) technique that finds the projection axes that **maximize the separation between classes** while **minimizing the spread (variance) within each class** — unlike PCA, which ignores labels and only maximizes overall variance.

**Objective — maximize the Fisher criterion:**
$$J(w) = \frac{w^\top S_B w}{w^\top S_W w}$$

where:
- $S_B$ = **Between-class scatter matrix** — how far apart class means are from the overall mean
- $S_W$ = **Within-class scatter matrix** — how spread out points are inside each class

$$S_B = \sum_{c} n_c(\mu_c-\mu)(\mu_c-\mu)^\top \qquad S_W = \sum_c\sum_{i\in c}(x_i-\mu_c)(x_i-\mu_c)^\top$$

- Solved as a **generalized eigenvalue problem**: $S_W^{-1}S_B\, w = \lambda w$. The eigenvectors (sorted by eigenvalue) give the **linear discriminants** (LD1, LD2, …).
- For a C-class problem, LDA can produce at most **C − 1** discriminant components (since $S_B$ has rank ≤ C−1).
- Because it uses class labels, LDA-reduced features are often more useful than PCA's for a downstream **classification** task.

### PCA vs LDA

| Aspect | PCA | LDA |
|---|---|---|
| Type | Unsupervised | Supervised (needs labels) |
| Maximizes | Total variance | Between-class / within-class variance ratio |
| Max components | min(n_features, n_samples) | C − 1 (C = #classes) |
| Goal | Best data representation | Best class separability |
| Used for | Compression, visualization, noise reduction | Classification pre-processing, visualization of class separation |

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=1)          # max = n_classes - 1
X_lda = lda.fit_transform(X, y)    # needs y! (supervised)
```

---
---

# Appendix A — Math Foundations

## Vectors & Distances (used across all algorithms)

$$\|\mathbf v\|_2=\sqrt{\sum v_i^2}\ (\text{Euclidean}) \qquad \|\mathbf v\|_1=\sum|v_i|\ (\text{Manhattan})$$
$$\text{cos\_sim}(a,b)=\frac{a\cdot b}{\|a\|\|b\|} \qquad \cos\theta = \frac{a\cdot b}{\|a\|\|b\|}$$

| Distance | Formula | Used in |
|---|---|---|
| Euclidean | $\sqrt{\sum(x_i-y_i)^2}$ | KNN, K-Means |
| Manhattan | $\sum\|x_i-y_i\|$ | Lasso, grid-based |
| Minkowski | $(\sum\|x_i-y_i\|^p)^{1/p}$ | generalizes above (p=1 Manhattan, p=2 Euclidean) |
| Mahalanobis | $\sqrt{(x-\mu)^\top\Sigma^{-1}(x-\mu)}$ | anomaly detection (accounts for correlation/scale) |
| Hamming | # differing positions | binary strings |
| Cosine | $1-\cos\text{sim}$ | text/NLP |

## Hyperplane (core of SVM/Logistic Regression)
$$w\cdot x + b = 0 \qquad d(\text{point to hyperplane}) = \frac{|w\cdot x_0+b|}{\|w\|}$$
- $w\cdot x+b>0$ → positive class; $<0$ → negative class.
- **SVM margin** $=\frac{2}{\|w\|}$.

## Calculus for ML

$$\text{Chain rule (backprop): } \frac{dz}{dx}=\frac{dz}{dy}\cdot\frac{dy}{dx} \qquad \nabla f = \left[\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\right]$$

| Activation | Derivative |
|---|---|
| Sigmoid $\sigma(x)$ | $\sigma(x)(1-\sigma(x))$ |
| Tanh | $1-\tanh^2(x)$ |
| ReLU | 1 if x>0 else 0 |

## Eigenvalues/Eigenvectors & SVD (basis of PCA)
$$Av=\lambda v \qquad A=U\Sigma V^\top$$
PCA uses eigenvectors of the **covariance matrix**; SVD generalizes this to non-square matrices.

---
---

# Appendix B — Probability & Statistics

## Descriptive Statistics

| Measure | Formula | Notes |
|---|---|---|
| Mean | $\bar x=\sum x_i/n$ | Sensitive to outliers |
| Median | middle value | Robust to outliers |
| Mode | most frequent value | Best for categorical |
| Variance (sample) | $s^2=\frac{\sum(x_i-\bar x)^2}{n-1}$ | **n−1: Bessel's correction** (unbiased estimator; corrects for using x̄ instead of true μ) |
| Std Dev | $s=\sqrt{s^2}$ | Same units as data |
| IQR | $Q_3-Q_1$ | Robust spread measure |
| Outlier fences | $Q_1-1.5\cdot IQR$, $Q_3+1.5\cdot IQR$ | |

**Empirical Rule (Normal dist.):** μ±1σ ≈ 68%, μ±2σ ≈ 95%, μ±3σ ≈ 99.7%

## Covariance & Correlation
$$Cov(X,Y)=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{n-1} \qquad r=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}\in[-1,1]$$
- **Spearman's rank correlation** — for monotonic (non-linear) or ordinal data, uses ranks not raw values.
- ⚠️ **Correlation ≠ Causation.**

## Probability Basics
$$P(A\cup B)=P(A)+P(B)-P(A\cap B) \qquad P(A\cap B)=P(A)P(B|A)$$
$$\text{Bayes: } P(A|B)=\frac{P(B|A)P(A)}{P(B)}$$

## Key Distributions
| Distribution | Type | Mean | Variance |
|---|---|---|---|
| Bernoulli | Discrete | p | p(1-p) |
| Binomial | Discrete | np | np(1-p) |
| Poisson | Discrete | λ | λ |
| Normal | Continuous | μ | σ² |
| Uniform | Continuous | (a+b)/2 | (b-a)²/12 |

**PMF vs PDF vs CDF:** PMF = exact P(X=x) (discrete); PDF = density, area under curve = probability (continuous, P(X=exact)=0); CDF = $P(X\le x)$ (both types, cumulative).

**Central Limit Theorem:** sample mean distribution → Normal as n→∞, regardless of population shape. $\bar X\sim N(\mu,\sigma^2/n)$, Standard Error $=\sigma/\sqrt n$.

## Inferential Statistics — Hypothesis Testing

**Process:** State H₀/H₁ → choose α (usually 0.05) → compute test statistic → find p-value → **p ≤ α → reject H₀**.

| Test | When to use |
|---|---|
| Z-test | σ known, n ≥ 30: $Z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}$ |
| t-test | σ unknown / n < 30: $t=\frac{\bar x-\mu_0}{s/\sqrt n}$, df = n−1 |
| Chi-Square | Categorical data: $\chi^2=\sum\frac{(O-E)^2}{E}$ |
| ANOVA | Compare 3+ group means: $F=MSB/MSW$ |

**Type I vs Type II Error:**
| | H₀ True | H₀ False |
|---|---|---|
| Reject H₀ | Type I Error (α) — false positive | Correct (Power) |
| Fail to Reject | Correct | Type II Error (β) — false negative |

**Confidence Interval:** $\bar x \pm z^*\cdot\frac{\sigma}{\sqrt n}$ (or t* if σ unknown). 95% CI → z*=1.96.

## EDA Workflow
```
Load → Check structure (df.info/describe) → Handle missing values →
Detect outliers (IQR/Z-score) → Visualize distributions → Analyze
relationships (correlation heatmap) → Feature insights
```
Univariate (1 var) → Bivariate (2 vars: scatter/boxplot) → Multivariate (heatmaps/pairplots).

---
---

# 📋 Final Exam Cheat Sheet

| Concept | Formula |
|---|---|
| Sigmoid | $\sigma(z)=\frac1{1+e^{-z}}$ |
| Log Loss | $-\frac1m\sum[y\log h+(1-y)\log(1-h)]$ |
| Gini | $1-\sum p_i^2$ |
| Entropy | $-\sum p_i\log_2p_i$ |
| Information Gain | $Entropy(S)-\sum\frac{|S_v|}{|S|}Entropy(S_v)$ |
| SVM margin | $2/\|w\|$ |
| Hinge Loss | $\max(0,1-y(w^Tx+b))$ |
| Bayes Theorem | $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$ |
| Ridge penalty | $+\lambda\sum\beta_j^2$ |
| Lasso penalty | $+\lambda\sum|\beta_j|$ |
| AdaBoost say | $\alpha_t=\frac12\ln\frac{1-\varepsilon_t}{\varepsilon_t}$ |
| WCSS (K-Means) | $\sum(\text{dist to centroid})^2$ |
| Silhouette | $\frac{b(i)-a(i)}{\max(a(i),b(i))}$ |
| PCA | $\Sigma v=\lambda v$, keep top-k eigenvectors |
| LDA | maximize $\frac{w^TS_Bw}{w^TS_Ww}$ |
| R² | $1-\frac{SS_{res}}{SS_{tot}}$ |
| Bias-Variance | $Error=Bias^2+Variance+\sigma^2$ |

### Algorithm → Category Quick Map
```
SUPERVISED
 ├─ Regression: Linear, Ridge/Lasso/ElasticNet, Polynomial, SVR, Regression Trees
 └─ Classification: Logistic Regression, Naive Bayes, KNN, SVM, Decision Trees,
                     Random Forest, AdaBoost

UNSUPERVISED
 ├─ Clustering: K-Means, Hierarchical, DBSCAN, GMM
 └─ Dim. Reduction: PCA (unsupervised), LDA (supervised)

EVALUATION
 ├─ Regression: MAE, MSE, RMSE, R², Adjusted R²
 ├─ Classification: Accuracy, Precision, Recall, F1, ROC-AUC
 └─ Clustering: WCSS (elbow), Silhouette Score, AIC/BIC (GMM)
```

### "Which model when scaling is/isn't needed"
- **Needs scaling:** Logistic Regression, SVM, KNN, K-Means, PCA, LDA, Ridge/Lasso, Gradient Descent–based models
- **No scaling needed:** Decision Trees, Random Forest, AdaBoost/Gradient Boosting (threshold/rank-based splits, not distance-based)

---
*Compiled revision notes — organized by Module I (Intro/Concept Learning), Module II (Regression), Module III (Classification: Bayesian/Instance-based), Module IV (Trees & Unsupervised), Module V (Dimensionality Reduction), plus Math/Stats appendices.*