# 📐 Mathematics for Machine Learning

> *Every formula you need — from vectors to hyperplanes — in clean sequence.*

---

## 🗂️ Table of Contents

1. [Basic Algebra & Notation](#1-basic-algebra--notation)
2. [Vectors](#2-vectors)
3. [Matrices](#3-matrices)
4. [2D Geometry](#4-2d-geometry)
5. [3D Geometry](#5-3d-geometry)
6. [Planes & Hyperplanes](#6-planes--hyperplanes)
7. [Distance Formulas](#7-distance-formulas)
8. [Probability & Statistics](#8-probability--statistics)
9. [Calculus for ML](#9-calculus-for-ml)
10. [Information Theory](#10-information-theory)
11. [Linear Algebra Deep Dive](#11-linear-algebra-deep-dive)

---

## 1. Basic Algebra & Notation

### Summation & Product

$$\sum_{i=1}^{n} x_i \;=\; x_1 + x_2 + \cdots + x_n$$

$$\prod_{i=1}^{n} x_i \;=\; x_1 \times x_2 \times \cdots \times x_n$$

---

### Exponents & Logarithms

$$a^m \cdot a^n = a^{m+n} \qquad (a^m)^n = a^{mn}$$

$$\log_a(xy) = \log_a x + \log_a y \qquad \log_a\!\left(\frac{x}{y}\right) = \log_a x - \log_a y$$

$$\log_a(x^n) = n\cdot\log_a x \qquad \log_a x = \frac{\ln x}{\ln a}$$

---

### Natural Exponential

$$e \approx 2.71828$$

$$e^x \cdot e^y = e^{x+y} \qquad \ln(e^x) = x \qquad \frac{d}{dx}\,e^x = e^x \quad \leftarrow \textit{very important in ML}$$

---

## 2. Vectors

### 📌 Definition

A vector is an ordered list of numbers representing **magnitude + direction**.

$$\text{2D:}\;\mathbf{v} = [v_1,\, v_2] \qquad \text{3D:}\;\mathbf{v} = [v_1,\, v_2,\, v_3] \qquad n\text{D:}\;\mathbf{v} = [v_1,\, v_2,\, \ldots,\, v_n]$$

---

### ➕ Vector Addition & Subtraction

$$\mathbf{a} + \mathbf{b} = [a_1+b_1,\; a_2+b_2,\; a_3+b_3]$$

$$\mathbf{a} - \mathbf{b} = [a_1-b_1,\; a_2-b_2,\; a_3-b_3]$$

---

### ✖️ Scalar Multiplication

$$\lambda \cdot \mathbf{v} = [\lambda v_1,\; \lambda v_2,\; \lambda v_3]$$

---

### 📏 Vector Magnitude (Norm)

**L1 Norm — Manhattan:**

$$\|\mathbf{v}\|_1 = |v_1| + |v_2| + \cdots + |v_n|$$

**L2 Norm — Euclidean (most common):**

$$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

**Lp Norm — General:**

$$\|\mathbf{v}\|_p = \left(|v_1|^p + |v_2|^p + \cdots + |v_n|^p\right)^{\!{1}/{p}}$$

**L∞ Norm — Chebyshev:**

$$\|\mathbf{v}\|_\infty = \max\!\left(|v_1|,\, |v_2|,\, \ldots,\, |v_n|\right)$$

---

### 🎯 Unit Vector (Normalization)

$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$$

Unit vector has magnitude $= 1$. Direction is preserved; only magnitude changes.

---

### 🔵 Dot Product (Inner Product)

**Formula:**

$$\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n = \|\mathbf{a}\|\,\|\mathbf{b}\|\cos\theta$$

**Properties:**

$$\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a} \qquad\textit{(commutative)}$$

$$\mathbf{a}\cdot(\mathbf{b}+\mathbf{c}) = \mathbf{a}\cdot\mathbf{b} + \mathbf{a}\cdot\mathbf{c} \qquad\textit{(distributive)}$$

$$\mathbf{a} \cdot \mathbf{a} = \|\mathbf{a}\|^2 \qquad\textit{(self dot product)}$$

**Geometric meaning:**

| Angle | Dot Product | Interpretation |
|:---:|:---:|:---|
| $\theta = 0°$ | $\mathbf{a}\cdot\mathbf{b} = \|\mathbf{a}\|\|\mathbf{b}\|$ | Parallel, same direction |
| $\theta = 90°$ | $\mathbf{a}\cdot\mathbf{b} = 0$ | **Perpendicular / orthogonal** ← key in ML |
| $\theta = 180°$ | $\mathbf{a}\cdot\mathbf{b} = -\|\mathbf{a}\|\|\mathbf{b}\|$ | Parallel, opposite direction |

**Angle between vectors:**

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|} \qquad \theta = \arccos\!\left(\frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}\right)$$

---

### ❌ Cross Product (3D only)

$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = \begin{bmatrix} a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3 \\ a_1 b_2 - a_2 b_1 \end{bmatrix}$$

$$\|\mathbf{a} \times \mathbf{b}\| = \|\mathbf{a}\|\,\|\mathbf{b}\|\sin\theta$$

Result: a vector **perpendicular** to both $\mathbf{a}$ and $\mathbf{b}$.

---

### 📐 Vector Projection

**Projection of $\mathbf{a}$ onto $\mathbf{b}$:**

$$\operatorname{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|^2}\,\mathbf{b}$$

**Scalar projection:**

$$\operatorname{comp}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|}$$

---

### 🌡️ Cosine Similarity (used heavily in NLP/Embeddings)

$$\text{cos\_sim}(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$$

| Value | Meaning |
|:---:|:---|
| $+1$ | Identical direction (very similar) |
| $\phantom{+}0$ | Orthogonal (unrelated) |
| $-1$ | Opposite direction (very different) |

---

## 3. Matrices

### 📌 Definition

A matrix is a 2D array of numbers: $A \in \mathbb{R}^{m \times n}$ ($m$ rows, $n$ columns).

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$

---

### Matrix Operations

**Addition (same shape only):**

$$(A + B)_{ij} = A_{ij} + B_{ij}$$

**Scalar multiplication:**

$$(\lambda A)_{ij} = \lambda \cdot A_{ij}$$

**Matrix Multiplication** — $A \in \mathbb{R}^{m \times n},\; B \in \mathbb{R}^{n \times p} \;\Rightarrow\; C = AB \in \mathbb{R}^{m \times p}$:

$$C_{ij} = \sum_{k} A_{ik} \cdot B_{kj} \qquad \textit{Note: } AB \neq BA \textit{ in general}$$

---

### Transpose

$$(A^\top)_{ij} = A_{ji} \qquad (AB)^\top = B^\top A^\top \qquad (A+B)^\top = A^\top + B^\top$$

---

### Identity Matrix

$$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \qquad AI = IA = A$$

---

### Inverse Matrix

$$AA^{-1} = A^{-1}A = I \qquad (AB)^{-1} = B^{-1}A^{-1} \qquad (A^\top)^{-1} = (A^{-1})^\top$$

Exists only when $\det(A) \neq 0$.

---

### Determinant

**2×2:**

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

**3×3 (cofactor expansion):**

$$\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)$$

---

### Trace

$$\operatorname{tr}(A) = \sum_i A_{ii} = a_{11} + a_{22} + \cdots + a_{nn}$$

$$\operatorname{tr}(AB) = \operatorname{tr}(BA) \qquad \operatorname{tr}(A^\top) = \operatorname{tr}(A)$$

---

### Eigenvalues & Eigenvectors

$$A\mathbf{v} = \lambda\mathbf{v}$$

| Symbol | Meaning |
|:---:|:---|
| $A$ | Matrix |
| $\mathbf{v}$ | Eigenvector — direction unchanged by $A$ |
| $\lambda$ | Eigenvalue — how much $\mathbf{v}$ is scaled |

**To find eigenvalues:** $\det(A - \lambda I) = 0$

**To find eigenvectors:** $(A - \lambda I)\mathbf{v} = \mathbf{0}$

> **In ML:** PCA uses eigenvectors of the covariance matrix!

---

### Frobenius Norm of a Matrix

$$\|A\|_F = \sqrt{\sum_i \sum_j A_{ij}^2}$$

Like the L2 norm, but for matrices.

---

## 4. 2D Geometry

### 📍 Distance Between Two Points

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

---

### 📍 Midpoint

$$M = \left(\frac{x_1 + x_2}{2},\;\frac{y_1 + y_2}{2}\right)$$

---

### 📏 Equation of a Line

**Slope-Intercept form:**

$$y = mx + c \qquad m = \frac{y_2 - y_1}{x_2 - x_1}$$

**General form:**

$$ax + by + c = 0$$

**Point-slope form:**

$$y - y_1 = m(x - x_1)$$

**Two-point form:**

$$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$$

---

### 📐 Angle of a Line with the X-axis

$$\tan\theta = m \qquad \theta = \arctan(m)$$

---

### 📐 Angle Between Two Lines

$$\tan\theta = \frac{|m_1 - m_2|}{|1 + m_1 m_2|}$$

$$\text{Parallel: } m_1 = m_2 \quad(\theta = 0°) \qquad \text{Perpendicular: } m_1 \cdot m_2 = -1 \quad(\theta = 90°)$$

---

### 📏 Distance from a Point to a Line (2D)

$$d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$$

where the line is $ax + by + c = 0$ and the point is $P = (x_0, y_0)$.

> 🔑 **This is the foundation of SVM margin calculation!**

---

### 🔵 Circle

$$\text{Center }(h, k),\;\text{radius }r: \qquad (x - h)^2 + (y - k)^2 = r^2$$

---

### 🏠 Area of Triangle (3 points)

$$\text{Area} = \frac{1}{2}\,\bigl|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)\bigr|$$

---

## 5. 3D Geometry

### 📍 Distance Between Two Points in 3D

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

---

### 📍 Midpoint in 3D

$$M = \left(\frac{x_1+x_2}{2},\;\frac{y_1+y_2}{2},\;\frac{z_1+z_2}{2}\right)$$

---

### 📐 Direction Cosines of a Vector

For $\mathbf{v} = [a, b, c]$ with magnitude $r = \sqrt{a^2+b^2+c^2}$:

$$\cos\alpha = \frac{a}{r}, \qquad \cos\beta = \frac{b}{r}, \qquad \cos\gamma = \frac{c}{r}$$

$$\cos^2\!\alpha + \cos^2\!\beta + \cos^2\!\gamma = 1 \quad \leftarrow \textit{always true!}$$

---

### 📐 Direction Ratios

Any scalar multiples of $[a, b, c]$ are direction ratios.
Direction ratios of the line through $P_1(x_1,y_1,z_1)$ and $P_2(x_2,y_2,z_2)$:

$$[x_2 - x_1,\; y_2 - y_1,\; z_2 - z_1]$$

---

### ✏️ Equation of a Line in 3D

**Vector form:**

$$\mathbf{r} = \mathbf{a} + \lambda\mathbf{b}$$

where $\mathbf{a}$ is a point on the line, $\mathbf{b}$ is the direction vector, and $\lambda$ is a scalar parameter.

**Cartesian / Symmetric form:**

$$\frac{x - x_1}{l} = \frac{y - y_1}{m} = \frac{z - z_1}{n}$$

where $(x_1, y_1, z_1)$ is a point on the line and $[l, m, n]$ are direction ratios.

---

### 📐 Angle Between Two Lines in 3D

$$\cos\theta = \frac{|\mathbf{b}_1 \cdot \mathbf{b}_2|}{\|\mathbf{b}_1\|\,\|\mathbf{b}_2\|}$$

$$\text{Parallel: } \mathbf{b}_1 \times \mathbf{b}_2 = \mathbf{0} \qquad \text{Perpendicular: } \mathbf{b}_1 \cdot \mathbf{b}_2 = 0$$

---

### 📏 Distance Between Two Skew Lines

For lines $\mathbf{r} = \mathbf{a}_1 + \lambda\mathbf{b}_1$ and $\mathbf{r} = \mathbf{a}_2 + \mu\mathbf{b}_2$:

$$d = \frac{\bigl|(\mathbf{a}_2 - \mathbf{a}_1)\cdot(\mathbf{b}_1 \times \mathbf{b}_2)\bigr|}{\|\mathbf{b}_1 \times \mathbf{b}_2\|}$$

---

### 📏 Distance from a Point to a Line (3D)

For a line through $A$ with direction $\mathbf{b}$ and a point $P$:

$$d = \frac{\|(\mathbf{P} - \mathbf{A}) \times \mathbf{b}\|}{\|\mathbf{b}\|}$$

---

### 🌐 Sphere

$$\text{Center }(a,b,c),\;\text{radius }r: \qquad (x-a)^2 + (y-b)^2 + (z-c)^2 = r^2$$

---

## 6. Planes & Hyperplanes

### 📌 What is a Plane?

A plane in 3D is a flat 2D surface extending infinitely.
It is fully defined by a **point + normal vector** $\mathbf{n} = [A, B, C]$ perpendicular to the plane.

---

### ✏️ Equation of a Plane (3D)

**General form:**

$$Ax + By + Cz + D = 0 \qquad \text{where } [A, B, C] \text{ is the normal vector}$$

**Point-Normal form:**

$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$$

**Intercept form:**

$$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1 \qquad \text{where } a, b, c \text{ are the axis intercepts}$$

**Three-point form** — given $P_1, P_2, P_3$:

$$\mathbf{v}_1 = P_2 - P_1, \quad \mathbf{v}_2 = P_3 - P_1, \quad \mathbf{n} = \mathbf{v}_1 \times \mathbf{v}_2, \quad \mathbf{n} \cdot (\mathbf{r} - P_1) = 0$$

---

### 📐 Angle Between Two Planes

$$\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\|\,\|\mathbf{n}_2\|}$$

$$\text{Parallel: } \mathbf{n}_1 \times \mathbf{n}_2 = \mathbf{0} \qquad \text{Perpendicular: } \mathbf{n}_1 \cdot \mathbf{n}_2 = 0$$

---

### 📏 Distance Between Parallel Planes

$$\text{Plane 1: }Ax + By + Cz + D_1 = 0 \qquad \text{Plane 2: }Ax + By + Cz + D_2 = 0$$

$$d = \frac{|D_1 - D_2|}{\sqrt{A^2 + B^2 + C^2}}$$

---

### 🔑 Hyperplane (nD) — The Core of ML

A **hyperplane** is the generalization of a plane to $n$ dimensions:

$$\text{In 2D} \to \text{a line} \qquad \text{In 3D} \to \text{a plane} \qquad \text{In }n\text{D} \to \text{a hyperplane}$$

$$\mathbf{w} \cdot \mathbf{x} + b = 0 \qquad \Longleftrightarrow \qquad w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b = 0$$

| Symbol | Meaning |
|:---:|:---|
| $\mathbf{w}$ | Weight vector — normal to hyperplane, $\mathbf{w} \in \mathbb{R}^n$ |
| $\mathbf{x}$ | Input point, $\mathbf{x} \in \mathbb{R}^n$ |
| $b$ | Bias — scalar offset |

**Signed distance from origin to hyperplane:**

$$d = \frac{-b}{\|\mathbf{w}\|}$$

**Which side of the hyperplane is a point on?**

$$\mathbf{w} \cdot \mathbf{x} + b > 0 \;\Rightarrow\; \text{positive side (class +1 in SVM)}$$
$$\mathbf{w} \cdot \mathbf{x} + b < 0 \;\Rightarrow\; \text{negative side (class −1 in SVM)}$$
$$\mathbf{w} \cdot \mathbf{x} + b = 0 \;\Rightarrow\; \text{on the plane (decision boundary)}$$

---

## 7. Distance Formulas

### 📏 7.1 Distance from a Point to a Plane (3D)

For plane $Ax + By + Cz + D = 0$ and point $P = (x_0, y_0, z_0)$:

$$d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}} = \frac{|\mathbf{n} \cdot P + D|}{\|\mathbf{n}\|}$$

> ⭐ This formula is used in **SVM** to compute the margin between classes!

---

### 📏 7.2 Distance from a Point to a Hyperplane (nD)

For hyperplane $\mathbf{w} \cdot \mathbf{x} + b = 0$ and point $\mathbf{x}_0 \in \mathbb{R}^n$:

$$d = \frac{|\mathbf{w} \cdot \mathbf{x}_0 + b|}{\|\mathbf{w}\|} = \frac{|w_1 x_{01} + w_2 x_{02} + \cdots + w_n x_{0n} + b|}{\sqrt{w_1^2 + w_2^2 + \cdots + w_n^2}}$$

**In SVM:**

$$\text{Margin} = \frac{2}{\|\mathbf{w}\|} \qquad \text{Maximizing margin} \;\longleftrightarrow\; \text{Minimizing } \|\mathbf{w}\|^2$$

---

### 📏 7.3 Euclidean Distance (Most Common in ML)

$$d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_2 = \sqrt{\sum_i (x_i - y_i)^2}$$

*Used in: KNN, K-Means, t-SNE*

---

### 📏 7.4 Manhattan Distance (L1)

$$d(\mathbf{x}, \mathbf{y}) = \sum_i |x_i - y_i|$$

*Used in: LASSO regularization, robust metrics*

---

### 📏 7.5 Minkowski Distance (General)

$$d(\mathbf{x}, \mathbf{y}) = \left(\sum_i |x_i - y_i|^p\right)^{\!{1}/{p}}$$

| $p$ | Distance |
|:---:|:---|
| $p = 1$ | Manhattan distance |
| $p = 2$ | Euclidean distance |
| $p \to \infty$ | Chebyshev distance — max of differences |

---

### 📏 7.6 Mahalanobis Distance

$$d(\mathbf{x}, \boldsymbol{\mu}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu})}$$

where $\Sigma$ is the covariance matrix and $\boldsymbol{\mu}$ is the mean vector.
Accounts for correlation and scale — used in anomaly detection.

---

### 📏 7.7 Hamming Distance

Number of positions where two binary strings differ:

$$d(\texttt{"1011"},\, \texttt{"1001"}) = 1 \qquad \text{(only one bit differs)}$$

*Used in: hashing, binary classifiers*

---

### 📏 7.8 Cosine Distance

$$d(\mathbf{a}, \mathbf{b}) = 1 - \text{cos\_sim}(\mathbf{a},\mathbf{b}) = 1 - \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$$

Range: $[0,\, 2]$ — used in text similarity, recommendation systems.

---

## 8. Probability & Statistics

### 📊 Basic Probability

$$0 \le P(A) \le 1$$

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) \qquad P(A^c) = 1 - P(A)$$

$$P(A \cap B) = P(A)\cdot P(B \mid A)$$

**Independence:**

$$P(A \cap B) = P(A)\cdot P(B) \qquad \text{iff } A \text{ and } B \text{ are independent}$$

---

### 📊 Bayes' Theorem

$$P(A \mid B) = \frac{P(B \mid A)\cdot P(A)}{P(B)}$$

$$\underbrace{P(\text{class} \mid \text{data})}_{\text{Posterior}} = \frac{\overbrace{P(\text{data} \mid \text{class})}^{\text{Likelihood}}\cdot\overbrace{P(\text{class})}^{\text{Prior}}}{\underbrace{P(\text{data})}_{\text{Evidence}}}$$

---

### 📊 Expectation & Variance

**Mean (Expectation):**

$$\mu = \mathbb{E}[X] = \sum_i x_i \cdot P(x_i) \quad \text{(discrete)} \qquad = \int x\cdot f(x)\,dx \quad \text{(continuous)}$$

**Variance:**

$$\sigma^2 = \operatorname{Var}(X) = \mathbb{E}\!\left[(X - \mu)^2\right] = \mathbb{E}[X^2] - \left(\mathbb{E}[X]\right)^2$$

**Standard Deviation:**

$$\sigma = \sqrt{\operatorname{Var}(X)}$$

**Covariance:**

$$\operatorname{Cov}(X, Y) = \mathbb{E}\!\left[(X - \mu_X)(Y - \mu_Y)\right] = \mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y]$$

**Correlation:**

$$\rho(X, Y) = \frac{\operatorname{Cov}(X,Y)}{\sigma_X \cdot \sigma_Y} \qquad \rho \in [-1,\, 1]$$

---

### 📊 Key Distributions

**Gaussian (Normal):**

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \qquad \mathcal{N}(\mu,\, \sigma^2)$$

68-95-99.7 rule: $1\sigma,\, 2\sigma,\, 3\sigma$ from the mean.

**Bernoulli:**

$$P(X=1) = p, \qquad P(X=0) = 1-p, \qquad \mathbb{E}[X] = p, \qquad \operatorname{Var}[X] = p(1-p)$$

**Binomial:**

$$P(X=k) = \binom{n}{k}\,p^k\,(1-p)^{n-k} \qquad \mathbb{E}[X] = np, \qquad \operatorname{Var}[X] = np(1-p)$$

**Softmax** (probability output in neural nets):

$$\operatorname{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\displaystyle\sum_j e^{z_j}}$$

Converts raw scores to probabilities; all outputs sum to $1$.

---

### 📊 Sample Statistics (from data)

$$\bar{x} = \frac{1}{n}\sum_i x_i \qquad s^2 = \frac{1}{n-1}\sum_i (x_i - \bar{x})^2 \qquad s = \sqrt{s^2}$$

---

## 9. Calculus for ML

### 📉 Derivatives

**Basic rules:**

$$\frac{d}{dx}(c) = 0 \qquad \frac{d}{dx}(x^n) = nx^{n-1} \qquad \frac{d}{dx}(e^x) = e^x \qquad \frac{d}{dx}\ln x = \frac{1}{x}$$

**Chain Rule — the backbone of backpropagation:**

$$\frac{d}{dx}\,f(g(x)) = f'(g(x))\cdot g'(x) \qquad \Longleftrightarrow \qquad \frac{dz}{dx} = \frac{dz}{dy}\cdot\frac{dy}{dx}$$

**Product Rule:**

$$\frac{d}{dx}\bigl[f(x)\,g(x)\bigr] = f'(x)\,g(x) + f(x)\,g'(x)$$

**Quotient Rule:**

$$\frac{d}{dx}\!\left[\frac{f}{g}\right] = \frac{f'g - fg'}{g^2}$$

---

### 📉 Partial Derivatives

For $f(x_1, x_2, \ldots, x_n)$:

$$\frac{\partial f}{\partial x_1} = \text{derivative w.r.t. } x_1\text{, treating others as constants}$$

**Example:**

$$f(x, y) = x^2 y + 3xy^2 \qquad \Rightarrow \qquad \frac{\partial f}{\partial x} = 2xy + 3y^2, \quad \frac{\partial f}{\partial y} = x^2 + 6xy$$

---

### 📉 Gradient

$$\nabla f(\mathbf{x}) = \left[\frac{\partial f}{\partial x_1},\;\frac{\partial f}{\partial x_2},\;\ldots,\;\frac{\partial f}{\partial x_n}\right]$$

Points in the direction of **steepest ascent**; $-\nabla f$ points toward steepest descent ← used in training!

---

### 📉 Gradient Descent

$$\mathbf{x}_\text{new} = \mathbf{x}_\text{old} - \alpha\,\nabla f(\mathbf{x}_\text{old})$$

where $\alpha$ is the learning rate. Converges to a minimum when $f$ is convex.

| Variant | Samples per step | Characteristic |
|:---|:---:|:---|
| Batch GD | All $N$ | Stable, slow |
| Stochastic | $1$ | Fast, noisy |
| Mini-batch | $k$ | Best of both ← standard in DL |

---

### 📉 Common Activation Derivatives

**Sigmoid:**

$$\sigma(x) = \frac{1}{1+e^{-x}} \qquad \sigma'(x) = \sigma(x)\bigl(1 - \sigma(x)\bigr)$$

**Tanh:**

$$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} \qquad \tanh'(x) = 1 - \tanh^2(x)$$

**ReLU:**

$$\operatorname{ReLU}(x) = \max(0,\, x) \qquad \operatorname{ReLU}'(x) = \begin{cases} 1 & x > 0 \\ 0 & x < 0 \end{cases}$$

---

### 📉 Jacobian Matrix

For vector-valued function $f: \mathbb{R}^n \to \mathbb{R}^m$:

$$J(f) = \begin{bmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\[10pt] \vdots & \ddots & \vdots \\[4pt] \dfrac{\partial f_m}{\partial x_1} & \cdots & \dfrac{\partial f_m}{\partial x_n} \end{bmatrix} \in \mathbb{R}^{m \times n}$$

---

### 📉 Hessian Matrix

Second-order partial derivatives — describes curvature:

$$H(f) = \begin{bmatrix} \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} \\[10pt] \dfrac{\partial^2 f}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} \end{bmatrix} \in \mathbb{R}^{n \times n}$$

$$H \text{ positive definite} \;\Rightarrow\; \text{local minimum} \qquad H \text{ negative definite} \;\Rightarrow\; \text{local maximum}$$

---

## 10. Information Theory

### 🔵 Entropy (Uncertainty in data)

$$H(X) = -\sum_x P(x)\,\log_2 P(x)$$

| Entropy | Meaning |
|:---|:---|
| High $H(X)$ | More uncertainty / randomness |
| Low $H(X)$ | More predictable |

*Used in: Decision Trees (splitting criterion)*

---

### 🔵 Cross-Entropy Loss (Classification)

**Binary:**

$$\mathcal{L} = -\bigl[y\log(p) + (1-y)\log(1-p)\bigr]$$

**Multi-class:**

$$\mathcal{L} = -\sum_i y_i\,\log(p_i)$$

where $y$ is the true label and $p$ is the predicted probability.

---

### 🔵 KL Divergence (Distance between distributions)

$$KL(P \| Q) = \sum_x P(x)\,\log\frac{P(x)}{Q(x)}$$

$$KL \ge 0 \text{ always} \qquad KL = 0 \text{ iff } P = Q \qquad KL(P\|Q) \neq KL(Q\|P) \text{ (not symmetric)}$$

---

### 🔵 Mutual Information

$$I(X;\,Y) = H(X) - H(X \mid Y) = \sum_x \sum_y P(x,y)\,\log\frac{P(x,y)}{P(x)\,P(y)}$$

Measures how much knowing $Y$ reduces uncertainty about $X$.

---

## 11. Linear Algebra Deep Dive

### 🔑 Singular Value Decomposition (SVD)

$$A = U\,\Sigma\,V^\top$$

| Factor | Dimensions | Description |
|:---:|:---:|:---|
| $A$ | $\mathbb{R}^{m \times n}$ | Original matrix |
| $U$ | $\mathbb{R}^{m \times m}$ | Left singular vectors (orthogonal) |
| $\Sigma$ | $\mathbb{R}^{m \times n}$ | Diagonal — singular values $\sigma_1 \ge \sigma_2 \ge \cdots \ge 0$ |
| $V$ | $\mathbb{R}^{n \times n}$ | Right singular vectors (orthogonal) |

*Used in: PCA, recommender systems, image compression*

---

### 🔑 PCA (Principal Component Analysis)

$$\tilde{X} = X - \overline{X} \qquad C = \frac{1}{n}\tilde{X}^\top\tilde{X} \qquad C = Q\Lambda Q^\top \qquad Z = \tilde{X}\,Q_k$$

Variance explained by the $k$-th component:

$$\frac{\lambda_k}{\displaystyle\sum_i \lambda_i}$$

---

### 🔑 Matrix Rank

$$\operatorname{rank}(A) = \text{number of linearly independent rows (or columns)}$$

$$\operatorname{rank}(A) = \operatorname{rank}(A^\top) \qquad \operatorname{rank}(AB) \le \min\!\bigl(\operatorname{rank}(A),\,\operatorname{rank}(B)\bigr)$$

Full rank: $\operatorname{rank}(A) = \min(m,n)$ → inverse exists (if square).

---

### 🔑 Quadratic Form

$$f(\mathbf{x}) = \mathbf{x}^\top A\mathbf{x} = \sum_i \sum_j A_{ij}\,x_i x_j$$

$$\text{Positive definite: } \mathbf{x}^\top A\mathbf{x} > 0\;\forall\,\mathbf{x} \ne \mathbf{0} \;\Longleftrightarrow\; \text{all eigenvalues} > 0$$

*Used in: Mahalanobis distance, optimization*

---

### 🔑 Normal Equation (Closed-form Linear Regression)

$$\mathbf{y} = X\mathbf{w} + \varepsilon$$

**Optimal weights:**

$$\mathbf{w}^* = \left(X^\top X\right)^{-1} X^\top \mathbf{y}$$

Works when $X^\top X$ is invertible. For large datasets: use gradient descent instead.

---

## 📌 Quick Reference Summary

| Formula | Use in ML |
|:---|:---|
| $\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\|\,\|\mathbf{b}\|\cos\theta$ | Attention, cosine similarity |
| $d = \dfrac{\|\mathbf{w} \cdot \mathbf{x} + b\|}{\|\mathbf{w}\|}$ | SVM margin |
| $\nabla\mathcal{L}$ | Gradient descent |
| $\dfrac{d\mathcal{L}}{dx} = \dfrac{d\mathcal{L}}{dy}\cdot\dfrac{dy}{dx}$ | Backpropagation (chain rule) |
| $H(X) = -\sum P\log P$ | Decision tree splitting |
| $\mathcal{L} = -\sum y\log(p)$ | Cross-entropy classification loss |
| $A = U\Sigma V^\top$ | PCA, matrix factorization |
| $P(A\mid B) = \dfrac{P(B\mid A)\,P(A)}{P(B)}$ | Naive Bayes |
| $\|\mathbf{x} - \mathbf{y}\|_2$ | KNN, K-Means |
| $A\mathbf{v} = \lambda\mathbf{v}$ | PCA eigenvectors |

---

> 📖 **Learning tip:** Don't memorize — **understand the geometry** behind each formula.
> Every formula here has a picture in your mind waiting to be drawn.

---

*Built for ML learners who want to understand the math.*