# 📊 Statistics — Complete Revision Notes

---

## Table of Contents

1. [What is Statistics?](#1-what-is-statistics)
2. [Types of Statistics](#2-types-of-statistics)
3. [Population vs Sample Data](#3-population-vs-sample-data)
4. [Variables](#4-variables)
5. [Random Variables](#5-random-variables)
6. [Measures of Central Tendency](#6-measures-of-central-tendency)
7. [Measures of Dispersion](#7-measures-of-dispersion)
8. [Standard Deviation](#8-standard-deviation)
9. [Why Sample Variance is Divided by n−1?](#9-why-sample-variance-is-divided-by-n1-bessels-correction)
10. [Histograms](#10-histograms)
11. [Percentiles and Quartiles](#11-percentiles-and-quartiles)
12. [5-Number Summary](#12-5-number-summary)
13. [Correlation and Covariance](#13-correlation-and-covariance)

---

## 1. What is Statistics?

**Statistics** is the science of **collecting, organizing, analyzing, interpreting, and presenting data** to make informed decisions under uncertainty.

### Applications
| Domain | Use Case |
|---|---|
| Business | Sales forecasting, market research |
| Medicine | Drug trials, disease analysis |
| Machine Learning | Model evaluation, feature selection |
| Finance | Risk analysis, stock prediction |
| Government | Census, economic planning |

---

## 2. Types of Statistics

### 2.1 Descriptive Statistics
Summarizes and describes the features of a dataset.
- Does **not** draw conclusions beyond the data.
- Tools: mean, median, mode, variance, charts, histograms.

> **Example:** "The average score of students in the class is 72."

### 2.2 Inferential Statistics
Uses a **sample** to make inferences (predictions/conclusions) about a **population**.
- Involves probability and hypothesis testing.
- Tools: t-tests, regression, confidence intervals.

> **Example:** "Based on a sample of 500 voters, candidate A is likely to win."

### Difference: Descriptive vs Inferential

| Feature | Descriptive | Inferential |
|---|---|---|
| Goal | Summarize data | Draw conclusions |
| Scope | Entire dataset | Sample → Population |
| Output | Charts, averages | Predictions, probabilities |
| Certainty | Definite | Probabilistic |

---

## 3. Population vs Sample Data

### Population
> The **entire group** of individuals or observations you want to study.

- Denoted by **N** (size)
- Parameters: μ (mean), σ (std dev)
- Rarely feasible to collect completely

### Sample
> A **subset** of the population selected for study.

- Denoted by **n** (size)
- Statistics: x̄ (mean), s (std dev)
- Must be **representative** and **random**

### Difference

| Feature | Population | Sample |
|---|---|---|
| Size | All data (N) | Subset (n) |
| Mean symbol | μ | x̄ |
| Std Dev symbol | σ | s |
| Cost | High | Low |
| Feasibility | Often impossible | Practical |

---

## 4. Variables

A **variable** is any characteristic or quantity that can take different values.

### 4.1 Qualitative (Categorical) Variables
Values are **categories or labels**, not numbers.

- **Nominal:** No natural order → *e.g., Color, Gender, City*
- **Ordinal:** Natural order exists → *e.g., Rating (Good/Better/Best), Education level*

### 4.2 Quantitative (Numerical) Variables
Values are **numbers** that can be measured.

- **Discrete:** Countable, finite values → *e.g., Number of students, Goals scored*
- **Continuous:** Any value in a range → *e.g., Height, Temperature, Weight*

### Summary Table

| Type | Subtype | Example | Math Operations |
|---|---|---|---|
| Qualitative | Nominal | Eye color | Count only |
| Qualitative | Ordinal | Satisfaction rating | Count, rank |
| Quantitative | Discrete | No. of cars | Count, add |
| Quantitative | Continuous | Body temperature | All operations |

---

## 5. Random Variables

A **random variable** is a variable whose value is determined by the **outcome of a random experiment**.

> It maps outcomes of a random process to numerical values.

### 5.1 Discrete Random Variable
Takes **countable** values.

> **Example:** X = number of heads in 3 coin tosses → X ∈ {0, 1, 2, 3}

**Probability Mass Function (PMF):**

```
P(X = x) = probability of each specific value
Sum of all P(X = x) = 1
```

### 5.2 Continuous Random Variable
Takes **any value** in an interval.

> **Example:** X = exact height of a person → X ∈ [0, ∞)

**Probability Density Function (PDF):**

```
P(a ≤ X ≤ b) = area under the curve between a and b
P(X = exact value) = 0
```

### Difference: Discrete vs Continuous Random Variables

| Feature | Discrete | Continuous |
|---|---|---|
| Values | Countable | Uncountable / interval |
| Probability | P(X = x) > 0 | P(X = x) = 0 |
| Tool | PMF | PDF |
| Example | Dice roll | Weight, Time |

---

## 6. Measures of Central Tendency

These describe the **center** or **typical value** of a dataset.

---

### 6.1 Mean (Arithmetic Average)

**Population Mean:**

$$\mu = \frac{\sum_{i=1}^{N} x_i}{N}$$

**Sample Mean:**

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

- Most commonly used.
- Sensitive to **outliers**.

> **Example:** Data = {2, 4, 6, 8, 10} → Mean = 30/5 = **6**

---

### 6.2 Median

The **middle value** when data is sorted in ascending order.

- If n is **odd:** Median = middle value
- If n is **even:** Median = average of two middle values

$$\text{Position} = \frac{n+1}{2}$$

- **Not affected by outliers.**

> **Example:** {1, 3, 5, 7, 9} → Median = **5**
> **Example:** {1, 3, 5, 7} → Median = (3+5)/2 = **4**

---

### 6.3 Mode

The value that **appears most frequently** in the dataset.

- A dataset can have **no mode**, **one mode (unimodal)**, or **multiple modes (bimodal/multimodal)**.
- Best for **categorical data**.

> **Example:** {1, 2, 2, 3, 4} → Mode = **2**

---

### When to Use Which?

| Situation | Best Measure |
|---|---|
| Symmetric distribution, no outliers | Mean |
| Skewed distribution or outliers present | Median |
| Categorical data | Mode |
| Income, house prices | Median |

---

## 7. Measures of Dispersion

These describe the **spread** or **variability** of a dataset around the center.

---

### 7.1 Range

$$\text{Range} = \text{Maximum} - \text{Minimum}$$

- Simple but **highly sensitive to outliers**.

---

### 7.2 Variance

The **average of squared deviations** from the mean.

**Population Variance:**

$$\sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}$$

**Sample Variance:**

$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}$$

- Units are **squared** (e.g., cm²), which can be hard to interpret.

---

### 7.3 Standard Deviation

Square root of variance — in the **same units** as the data.

**Population Std Dev:**

$$\sigma = \sqrt{\frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}}$$

**Sample Std Dev:**

$$s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$$

---

### 7.4 Interquartile Range (IQR)

$$\text{IQR} = Q_3 - Q_1$$

- Measures spread of the **middle 50%** of data.
- **Robust to outliers.**

---

### Difference: Variance vs Standard Deviation

| Feature | Variance | Standard Deviation |
|---|---|---|
| Formula | Avg of squared deviations | √Variance |
| Units | Squared units (cm²) | Original units (cm) |
| Interpretability | Harder | Easier |
| Sensitivity | High | High |

---

## 8. Standard Deviation

**Standard Deviation (SD)** measures how much data values **deviate on average** from the mean.

### Interpretation Using Empirical Rule (Normal Distribution)

```
    |----- 68% -----|
    |------- 95% -------|
    |--------- 99.7% ----------|
    
    μ-3σ  μ-2σ  μ-σ   μ   μ+σ  μ+2σ  μ+3σ
```

| Range | % of Data |
|---|---|
| μ ± 1σ | ~68% |
| μ ± 2σ | ~95% |
| μ ± 3σ | ~99.7% |

### Low vs High Standard Deviation

| Low SD | High SD |
|---|---|
| Data points are close to the mean | Data points are spread far from mean |
| Consistent/uniform data | Variable/spread-out data |
| e.g., Factory parts with precise dimensions | e.g., Student scores in a difficult exam |

---

## 9. Why Sample Variance is Divided by n−1? (Bessel's Correction)

### The Problem
When using a **sample** to estimate the **population variance**, dividing by **n** gives a **biased (underestimated)** result.

> This is because the sample mean x̄ is calculated *from the same data*, so the deviations from x̄ are **smaller** than actual deviations from the true population mean μ.

### The Fix — Bessel's Correction
Dividing by **(n − 1)** instead of **n** compensates for this bias and gives an **unbiased estimator** of population variance.

```
Biased (Population formula applied to sample):
  s² = Σ(xᵢ - x̄)² / n        ← underestimates σ²

Unbiased (Correct sample formula):
  s² = Σ(xᵢ - x̄)² / (n−1)   ← unbiased estimate of σ²
```

### Degrees of Freedom
- With n data points and 1 constraint (x̄ is fixed), only **n − 1** values are **free to vary**.
- Dividing by n−1 reflects the **true degrees of freedom** in the sample.

> **Intuition:** If you know n−1 values and the mean, the last value is determined. You lose 1 degree of freedom when you estimate the mean from data.

---

## 10. Histograms

A **histogram** is a bar chart that shows the **frequency distribution** of continuous data grouped into **bins (class intervals)**.

### Key Components
- **X-axis:** Value ranges (bins/intervals)
- **Y-axis:** Frequency (count) or relative frequency (%)
- **Bars touch each other** (unlike bar charts)

### Shapes of Histograms

| Shape | Description | Implication |
|---|---|---|
| Symmetric (Bell) | Mirror image on both sides | Mean ≈ Median ≈ Mode |
| Right-skewed | Long tail to the right | Mean > Median |
| Left-skewed | Long tail to the left | Mean < Median |
| Bimodal | Two peaks | Two groups in data |
| Uniform | All bars same height | All values equally likely |

### Histogram vs Bar Chart

| Feature | Histogram | Bar Chart |
|---|---|---|
| Data type | Continuous | Categorical |
| Bars | Touch each other | Have gaps |
| X-axis | Numeric ranges | Categories |

---

## 11. Percentiles and Quartiles

### Percentile
The **pecentile** is given by :
$$\text{Percentile} = \frac{\text{Number of samples below x}}{n} \times (100)$$
where **x** is the given number whose *percentile* is to be found.

The **p-th percentile** is the value below which **p%** of the data falls.

$$\text{Percentile Position} = \frac{p}{100} \times (n + 1)$$

> **Example:** 70th percentile means 70% of values are below this point.

---

### Quartiles
Special percentiles that divide data into **4 equal parts**.

| Quartile | Percentile | Meaning |
|---|---|---|
| Q1 (First Quartile) | 25th | 25% of data falls below |
| Q2 (Second Quartile) | 50th | Median — 50% falls below |
| Q3 (Third Quartile) | 75th | 75% of data falls below |

```
|---25%---|---25%---|---25%---|---25%---|
Min      Q1        Q2        Q3       Max
```

**IQR = Q3 − Q1** → Spread of middle 50% of data

### Outlier Detection Using IQR

```
Lower Fence = Q1 − 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR

Any value outside these fences is an outlier.
```

---

## 12. 5-Number Summary

A compact summary of a dataset using **5 key values**:

| # | Value | Description |
|---|---|---|
| 1 | **Minimum** | Smallest value |
| 2 | **Q1** | 25th percentile |
| 3 | **Median (Q2)** | 50th percentile (middle) |
| 4 | **Q3** | 75th percentile |
| 5 | **Maximum** | Largest value |

### Visual: Box Plot (Box-and-Whisker)

```
    |-----|======|==========|======|-----|
   Min   Q1    Median      Q3    Max

   |_____|                        |_____|
   Whisker     Box (IQR)         Whisker
```

- **Box** spans from Q1 to Q3 (IQR)
- **Line inside box** = Median
- **Whiskers** extend to Min and Max (or to fences, with outliers plotted separately)

### Uses of 5-Number Summary
- Quick visual summary of spread and center
- Identifying skewness
- Comparing multiple datasets
- Detecting outliers

---

## 13. Correlation and Covariance

### 13.1 Covariance

**Covariance** measures how two variables **change together**.

- If both **increase/decrease** together → covariance is **positive**.
- If one **increases** while the other **decreases** → covariance is **negative**.

**Population Covariance:**

$$\text{Cov}(X, Y) = \frac{\sum_{i=1}^{N}(x_i - \mu_X)(y_i - \mu_Y)}{N}$$

**Sample Covariance:**

$$\text{Cov}(X, Y) = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{n - 1}$$

### Interpreting Covariance

| Value | Meaning |
|---|---|
| Cov > 0 | X and Y increase together (positive relationship) |
| Cov < 0 | One increases while other decreases (negative relationship) |
| Cov = 0 | No linear relationship |

> ⚠️ **Limitation:** Covariance values depend on the **scale/units** of the variables, making comparison across datasets difficult.

---

## 13.2 Correlation (Pearson's r)

Measures **both direction and strength** of the linear relationship, on a **standardized scale**.

### Formula

$$
r = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}
$$

Or equivalently:

$$
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \cdot \sum(y_i - \bar{y})^2}}
$$

---

### Interpreting Pearson's r

| Value of r | Interpretation |
|---|---|
| +1.0 | Perfect positive linear relationship |
| +0.7 to +0.9 | Strong positive relationship |
| +0.4 to +0.6 | Moderate positive relationship |
| 0 to +0.3 | Weak positive relationship |
| 0 | No linear relationship |
| −0.3 to 0 | Weak negative relationship |
| −0.7 to −0.4 | Moderate negative relationship |
| −1.0 | Perfect negative linear relationship |

---

## 13.3 Spearman’s Rank Correlation (rₛ)

Measures **direction and strength of a monotonic relationship** using **ranks instead of actual values**.

### Formula (No tied ranks)

$$
r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
$$

Or equivalently:

$$
r_s = \frac{\text{Cov}(R(x_i), R(y_i))}{\sigma_{R(x_i)} \cdot \sigma_{R(y_i)}}
$$

- **d<sub>i</sub>** = **R(x<sub>i</sub>)** - **R(y<sub>i</sub>)** : Difference between ranks  
- **R(x<sub>i</sub>)** : Rank of X  
- **R(y<sub>i</sub>)** : Rank of Y  
- **n** : Number of observations    
---

### Definition (Easy)

- Checks how well the **ranking/order** of two variables matches  
- Works even when the relationship is **not linear**

---

### When to Use

- Data is **not normally distributed**  
- Relationship is **non-linear but monotonic**  
- Data is **ordinal (ranked)**  

---

### Mini Real-Life Examples

- Exam rank vs study hours rank  
- Instagram followers rank vs engagement rank  
- Customer ratings (1–5 stars) vs repeat purchases  

---

## Difference: Covariance vs Correlation

| Feature | Covariance | Correlation |
|---|---|---|
| Range | (−∞, +∞) | [−1, +1] |
| Units | Units of X × Y | Dimensionless |
| Scale sensitivity | Yes | No |
| Interpretation | Direction only | Direction + Strength |
| Easier to compare | ❌ | ✅ |

---

## Difference: Pearson vs Spearman

| Feature | Pearson (r) | Spearman (rₛ) |
|---|---|---|
| Relationship type | Linear | Monotonic |
| Data used | Actual values | Ranks |
| Sensitive to outliers | Yes | Less |
| Assumption | Normal distribution preferred | No strict assumption |
| Best for | Precise numeric data | Ranked / skewed data |

---

## Key Caution

> **Correlation ≠ Causation**

Two variables being correlated does **not** mean one causes the other.

**Example:**  
Ice cream sales and drowning rates increase together → due to **summer (hidden variable)**, not causation.

---

## Quick Intuition

- **Covariance** → Direction only  
- **Pearson** → Direction + Strength (linear)  
- **Spearman** → Direction + Strength (ranking-based)
---

## 🔑 Quick Formula Reference

| Concept | Formula |
|---|---|
| Population Mean | μ = Σxᵢ / N |
| Sample Mean | x̄ = Σxᵢ / n |
| Population Variance | σ² = Σ(xᵢ − μ)² / N |
| Sample Variance | s² = Σ(xᵢ − x̄)² / (n−1) |
| Population Std Dev | σ = √[Σ(xᵢ − μ)² / N] |
| Sample Std Dev | s = √[Σ(xᵢ − x̄)² / (n−1)] |
| IQR | Q3 − Q1 |
| Lower Outlier Fence | Q1 − 1.5 × IQR |
| Upper Outlier Fence | Q3 + 1.5 × IQR |
| Pearson Correlation | r = Cov(X,Y) / (σX × σY) |
| Spearman Correlation | rₛ = 1 − (6 Σdᵢ²) / (n(n²−1)) |
| Sample Covariance | Cov = Σ(xᵢ−x̄)(yᵢ−ȳ) / (n−1) |

---

*End of Statistics Revision Notes*