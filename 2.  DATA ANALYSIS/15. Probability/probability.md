# 📊 Probability & Distributions — Revision Notes

> **Coverage:** Introduction to Probability · Probability Distribution Functions · CLT · Estimates

---

## 🔷 PART 1 — Introduction to Probability

### Addition Rule

| Case | Formula |
|------|---------|
| Mutually Exclusive | `P(A ∪ B) = P(A) + P(B)` |
| Non-Mutually Exclusive | `P(A ∪ B) = P(A) + P(B) − P(A ∩ B)` |

### Multiplication Rule

| Case | Formula |
|------|---------|
| Independent Events | `P(A ∩ B) = P(A) × P(B)` |
| Dependent Events | `P(A ∩ B) = P(A) × P(B\|A)` |

```python
# Addition & Multiplication Rules
P_A, P_B = 0.4, 0.3
P_A_and_B = 0.1  # for non-mutually exclusive

# Addition
P_union_exclusive     = P_A + P_B
P_union_non_exclusive = P_A + P_B - P_A_and_B

# Multiplication (independent)
P_indep = P_A * P_B

# Multiplication (dependent) — P(B|A) given
P_B_given_A = 0.25
P_dep = P_A * P_B_given_A

print(f"P(A∪B) mutually exclusive     : {P_union_exclusive}")
print(f"P(A∪B) non-mutually exclusive : {P_union_non_exclusive}")
print(f"P(A∩B) independent            : {P_indep}")
print(f"P(A∩B) dependent              : {P_dep}")
```

---

## 🔷 PART 2 — Probability Distribution Functions

### PDF · PMF · CDF — Key Relationships

## 1. PMF — Probability Mass Function
 
**Type:** Discrete random variables only
 
**Definition:** Gives the exact probability that a discrete random variable equals a specific value.
 
$$P(X = x)$$
 
**Rules:**
- $P(X = x) \geq 0$ for all $x$
- $\sum_{\text{all } x} P(X = x) = 1$

**How it's calculated:**
Count favorable outcomes divided by total outcomes, or use a known formula (e.g., Binomial, Poisson).
 
Binomial example:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
 
**Why needed:**
To find the probability of a specific outcome in discrete settings — e.g., *"What's the probability of getting exactly 3 heads in 5 flips?"*
 
**Example:**
Rolling a fair die → $P(X = 4) = \frac{1}{6}$
 
---
 
## 2. PDF — Probability Density Function
 
**Type:** Continuous random variables only
 
**Definition:** A function $f(x)$ describing the *relative likelihood* of a continuous variable taking a value near $x$. NOT a direct probability — probabilities come from integrating it.
 
$$P(a \leq X \leq b) = \int_a^b f(x)\, dx$$
 
**Rules:**
- $f(x) \geq 0$ for all $x$
- $\int_{-\infty}^{\infty} f(x)\, dx = 1$
- $P(X = \text{exact value}) = 0$ always

**How it's calculated:**
Derived mathematically from the distribution (e.g., Normal, Exponential, Uniform). Area under curve = probability.
 
Normal distribution PDF:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
 
**Why needed:**
To find probabilities over *ranges* for continuous variables — e.g., *"What's the probability that a person's height is between 170–180 cm?"*
 
**Key distinction from PMF:**
$f(x)$ itself is not a probability. Only the *area* under $f(x)$ is.
 
---
 
## 3. CDF — Cumulative Distribution Function
 
**Type:** Both discrete and continuous
 
**Definition:** Gives the probability that a random variable $X$ is *less than or equal to* a value $x$.
 
$$F(x) = P(X \leq x)$$
 
**Rules:**
- $0 \leq F(x) \leq 1$
- Non-decreasing: if $a < b$, then $F(a) \leq F(b)$
- $F(-\infty) = 0$, $F(+\infty) = 1$

**How it's calculated:** 
For **discrete** variables — sum the PMF up to $x$:
$$F(x) = \sum_{t \leq x} P(X = t)$$
 
For **continuous** variables — integrate the PDF up to $x$:
$$F(x) = \int_{-\infty}^{x} f(t)\, dt$$
 
**Why needed:**
- Find probabilities over ranges: $P(a < X \leq b) = F(b) - F(a)$
- Find percentiles and quantiles (e.g., median = $x$ where $F(x) = 0.5$)
- Used directly in hypothesis testing, confidence intervals, p-values
- Converts PDF/PMF into usable probability statements
---
 
## Relationship Summary
 
```
PMF / PDF
    ↓  (sum / integrate)
   CDF
    ↓  (differentiate / difference)
PMF / PDF
```
 
| | PMF | PDF | CDF |
|---|---|---|---|
| Variable type | Discrete | Continuous | Both |
| Gives | Exact P(X = x) | Density at x | P(X ≤ x) |
| Direct probability? | Yes | No (area is) | Yes |
| Sum/Integral | Sums to 1 | Integrates to 1 | Reaches 1 |
| Use case | Exact outcomes | Ranges (continuous) | Cumulative / percentiles |
 
---
 
## Quick Intuition
 
- **PMF** → "Exactly how likely is *this* outcome?" (discrete)
- **PDF** → "How dense is probability *around* this point?" (continuous)
- **CDF** → "How likely is the outcome to be *at most* this value?" (both)



```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.linspace(-4, 4, 300)
pdf = stats.norm.pdf(x)
cdf = stats.norm.cdf(x)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1); plt.plot(x, pdf, 'b'); plt.title("PDF — Normal"); 
plt.fill_between(x, pdf, alpha=0.2)
plt.subplot(1, 2, 2); plt.plot(x, cdf, 'r'); plt.title("CDF — Normal")
plt.tight_layout(); plt.show()
```

---

### 1️⃣ Bernoulli Distribution
- Bernoulli distribution models a **random experiment** with two outcomes (**success/failure**)

$$P(X = k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$$

| Stat | Value |
|------|-------|
| Mean | `p` |
| Variance | `p(1−p)` |

```python
from scipy.stats import bernoulli

p = 0.6
dist = bernoulli(p)

print(f"P(X=1) = {dist.pmf(1):.2f}")   # success
print(f"P(X=0) = {dist.pmf(0):.2f}")   # failure
print(f"Mean   = {dist.mean():.2f}")
print(f"Var    = {dist.var():.2f}")

samples = dist.rvs(size=1000)
print(f"Sample mean ≈ {samples.mean():.3f}")
```

---

### 2️⃣ Binomial Distribution

**Models:** Number of successes in `n` independent Bernoulli trials

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

| Stat | Value |
|------|-------|
| Mean | `np` |
| Variance | `np(1−p)` |

```python
from scipy.stats import binom

n, p = 10, 0.5
dist = binom(n, p)

k = np.arange(0, n+1)
plt.bar(k, dist.pmf(k), color='steelblue', edgecolor='white')
plt.title(f"Binomial(n={n}, p={p})"); plt.xlabel("k"); plt.ylabel("P(X=k)")
plt.show()

print(f"P(X=6)     = {dist.pmf(6):.4f}")
print(f"P(X<=6)    = {dist.cdf(6):.4f}")
print(f"Mean       = {dist.mean()}")
print(f"Variance   = {dist.var()}")
```

---

### 3️⃣ Poisson Distribution

**Models:** Number of events in a fixed interval (rate = λ)

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

| Stat | Value |
|------|-------|
| Mean | `λ` |
| Variance | `λ` |

```python
from scipy.stats import poisson

lam = 4   # average events per interval
dist = poisson(lam)

k = np.arange(0, 15)
plt.bar(k, dist.pmf(k), color='coral', edgecolor='white')
plt.title(f"Poisson(λ={lam})"); plt.xlabel("k"); plt.ylabel("P(X=k)")
plt.show()

print(f"P(X=3)  = {dist.pmf(3):.4f}")
print(f"P(X<=5) = {dist.cdf(5):.4f}")
print(f"Mean    = {dist.mean()}, Var = {dist.var()}")
```

---

### 4️⃣ Normal / Gaussian Distribution

**Models:** Continuous symmetric bell-curve data

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

| Stat | Value |
|------|-------|
| Mean | `μ` |
| Variance | `σ²` |

```python
from scipy.stats import norm

mu, sigma = 0, 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)

plt.plot(x, norm.pdf(x, mu, sigma), 'b', lw=2)
plt.fill_between(x, norm.pdf(x, mu, sigma), alpha=0.2)
plt.title(f"Normal(μ={mu}, σ={sigma})"); plt.show()

print(f"P(X < 1.96) = {norm.cdf(1.96):.4f}")   # ≈ 97.5%
print(f"68–95–99.7 rule:")
for z in [1, 2, 3]:
    print(f"  ±{z}σ covers {norm.cdf(z) - norm.cdf(-z):.4%}")
```

---

### 5️⃣ Standard Normal Distribution & Z-Score

$$Z = \frac{X - \mu}{\sigma}$$

```python
# Z-score standardisation
data  = np.array([55, 70, 80, 90, 65])
mu    = data.mean()
sigma = data.std()

z_scores = (data - mu) / sigma
print("Z-scores:", np.round(z_scores, 2))

# Probability from Z
z = 1.5
print(f"P(Z < {z})  = {norm.cdf(z):.4f}")
print(f"P(Z > {z})  = {1 - norm.cdf(z):.4f}")
print(f"P(-{z}<Z<{z}) = {norm.cdf(z) - norm.cdf(-z):.4f}")
```

---

### 6️⃣ Uniform Distribution

**Models:** Equal probability across `[a, b]`

$$f(x) = \frac{1}{b - a}, \quad x \in [a, b]$$

| Stat | Value |
|------|-------|
| Mean | `(a+b)/2` |
| Variance | `(b−a)²/12` |

```python
from scipy.stats import uniform

a, b = 2, 8
dist = uniform(loc=a, scale=b-a)

x = np.linspace(0, 10, 300)
plt.plot(x, dist.pdf(x), 'g', lw=2)
plt.title(f"Uniform({a}, {b})"); plt.ylim(0, 0.3); plt.show()

print(f"P(3 < X < 6) = {dist.cdf(6) - dist.cdf(3):.4f}")
print(f"Mean         = {dist.mean():.2f}")
print(f"Variance     = {dist.var():.4f}")
```

---

### 7️⃣ Log-Normal Distribution

**Models:** Variable whose **log** is normally distributed (e.g. stock prices, income)

$$\ln(X) \sim N(\mu, \sigma^2)$$

| Stat | Value |
|------|-------|
| Mean | `exp(μ + σ²/2)` |
| Variance | `(exp(σ²)−1)·exp(2μ+σ²)` |

```python
from scipy.stats import lognorm

mu, sigma = 0, 0.5
dist = lognorm(s=sigma, scale=np.exp(mu))

x = np.linspace(0.01, 6, 300)
plt.plot(x, dist.pdf(x), 'm', lw=2)
plt.title(f"Log-Normal(μ={mu}, σ={sigma})"); plt.show()

print(f"Mean     = {dist.mean():.4f}")
print(f"Variance = {dist.var():.4f}")
```

---

### 8️⃣ Power Law Distribution

**Models:** Heavy-tailed phenomena — wealth, city sizes, word frequency

$$P(X \geq x) \propto x^{-\alpha}$$

```python
# Simulate power-law using Pareto (special case)
from scipy.stats import pareto

alpha = 2.0          # shape / tail index
dist  = pareto(alpha)

x = np.linspace(1, 10, 300)
plt.loglog(x, dist.pdf(x), 'r', lw=2)
plt.title(f"Power Law / Pareto(α={alpha}) — log-log scale"); plt.show()

samples = dist.rvs(10000)
print(f"Sample mean ≈ {samples.mean():.2f}")
```

---

### 9️⃣ Pareto Distribution

**Models:** Pareto Principle ("80/20 rule"); special power-law with scale `x_m`

$$f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}, \quad x \geq x_m$$

| Stat | Value |
|------|-------|
| Mean | `α·xₘ / (α−1)` for α > 1 |
| Variance | `xₘ²·α / ((α−1)²(α−2))` for α > 2 |

```python
from scipy.stats import pareto

alpha, x_m = 3, 1   # shape, scale
dist = pareto(b=alpha, scale=x_m)

x = np.linspace(x_m, 5, 300)
plt.plot(x, dist.pdf(x), 'darkorange', lw=2)
plt.title(f"Pareto(α={alpha}, xₘ={x_m})"); plt.show()

print(f"Mean     = {dist.mean():.4f}")
print(f"Variance = {dist.var():.4f}")
print(f"P(X > 2) = {1 - dist.cdf(2):.4f}")
```

---

## 🔷 PART 3 — Central Limit Theorem (CLT)

**Statement:** The sampling distribution of the sample mean approaches **Normal** as `n → ∞`, regardless of the population distribution.

$$\bar{X} \sim N\!\left(\mu,\ \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty$$

**Standard Error:** $SE = \dfrac{\sigma}{\sqrt{n}}$

```python
import numpy as np
import matplotlib.pyplot as plt

population = np.random.exponential(scale=2, size=100_000)  # skewed population

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, n in enumerate([1, 5, 30, 100]):
    means = [np.random.choice(population, n).mean() for _ in range(3000)]
    axes[i].hist(means, bins=40, color='steelblue', edgecolor='white', density=True)
    axes[i].set_title(f"n = {n}")
    axes[i].set_xlabel("Sample Mean")

plt.suptitle("Central Limit Theorem — Sample Mean Distributions", fontsize=13)
plt.tight_layout(); plt.show()

mu    = population.mean()
sigma = population.std()
print(f"Population: μ={mu:.2f}, σ={sigma:.2f}")
print(f"SE (n=30): σ/√n = {sigma/np.sqrt(30):.4f}")
```

---

## 🔷 PART 4 — Estimates

### Point Estimates

| Estimator | Formula |
|-----------|---------|
| Sample Mean | `x̄ = Σxᵢ / n` |
| Sample Variance | `s² = Σ(xᵢ − x̄)² / (n−1)` (Bessel's correction) |
| Sample Std Dev | `s = √s²` |

### Confidence Interval

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

```python
import numpy as np
from scipy import stats

data = np.random.normal(loc=50, scale=10, size=40)

# Point estimates
x_bar = data.mean()
s     = data.std(ddof=1)   # ddof=1 → Bessel's correction
SE    = s / np.sqrt(len(data))

# 95% Confidence Interval
ci = stats.t.interval(0.95, df=len(data)-1, loc=x_bar, scale=SE)

print(f"Sample Mean      : {x_bar:.4f}")
print(f"Sample Std Dev   : {s:.4f}")
print(f"Standard Error   : {SE:.4f}")
print(f"95% CI           : ({ci[0]:.4f}, {ci[1]:.4f})")
```

### MLE — Maximum Likelihood Estimation (Normal)

```python
from scipy.stats import norm

data = np.random.normal(60, 15, 200)

# MLE for Normal: μ_hat = mean, σ_hat = std (ddof=0)
mu_hat, sigma_hat = norm.fit(data)
print(f"MLE μ̂ = {mu_hat:.4f},  σ̂ = {sigma_hat:.4f}")
```

---

## 📦 Quick Reference — All Distributions

| Distribution | Type | Key Params | Mean | Variance |
|---|---|---|---|---|
| Bernoulli | Discrete | p | p | p(1−p) |
| Binomial | Discrete | n, p | np | np(1−p) |
| Poisson | Discrete | λ | λ | λ |
| Normal | Continuous | μ, σ | μ | σ² |
| Uniform | Continuous | a, b | (a+b)/2 | (b−a)²/12 |
| Log-Normal | Continuous | μ, σ | e^(μ+σ²/2) | (e^σ²−1)·e^(2μ+σ²) |
| Pareto | Continuous | α, xₘ | αxₘ/(α−1) | — |

---

## 🛠️ Imports Cheat Sheet

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import (
    bernoulli, binom, poisson,
    norm, uniform, lognorm, pareto
)
```

---

*Happy Revising! 🚀*