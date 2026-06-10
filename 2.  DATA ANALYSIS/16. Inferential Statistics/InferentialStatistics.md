# 📊 Inferential Statistics — Complete Notes

---

## Table of Contents

1. [Hypothesis Testing and Mechanism](#1-hypothesis-testing-and-mechanism)
2. [What is P-value?](#2-what-is-p-value)
3. [Z-Test – Hypothesis Testing](#3-z-test--hypothesis-testing)
4. [Student's t Distribution](#4-students-t-distribution)
5. [T-Statistics with t-Test Hypothesis Testing](#5-t-statistics-with-t-test-hypothesis-testing)
6. [Z-test vs T-test](#6-z-test-vs-t-test)
7. [Type I and Type II Errors](#7-type-i-and-type-ii-errors)
8. [Bayes Theorem](#8-bayes-theorem)
9. [Confidence Interval and Margin of Error](#9-confidence-interval-and-margin-of-error)
10. [What is Chi-Square Test?](#10-what-is-chi-square-test)
11. [Chi-Square Goodness of Fit](#11-chi-square-goodness-of-fit)
12. [ANOVA Test](#12-anova-test)
13. [Assumptions of ANOVA](#13-assumptions-of-anova)
14. [Types of ANOVA](#14-types-of-anova)
15. [Partitioning of Variance in ANOVA](#15-partitioning-of-variance-in-anova)

---

# 1. Hypothesis Testing and Mechanism

## What is it?

A structured method to make decisions about a population using sample data. It answers: *"Is this result real, or just random luck?"*

---

## Intuition

You can never test everyone — so you test a sample and use logic + math to decide whether your result is too extreme to be a coincidence. Hypothesis testing gives you a framework to challenge assumptions and separate signal from noise.

---

## Analogy: The Court Trial

| Court | Hypothesis Testing |
|---|---|
| Accused is innocent (default) | Null Hypothesis H₀ |
| Accused is guilty (claim) | Alternative Hypothesis H₁ |
| Evidence presented | Sample Data |
| Verdict | Reject / Fail to Reject H₀ |
| Beyond reasonable doubt | Significance level α |

> You assume innocence **until proven guilty beyond reasonable doubt** — same in statistics.

---

## Step-by-Step Mechanism

**Step 1 — State hypotheses:**
- **H₀ (Null):** Default assumption. "Nothing is happening."
- **H₁ (Alternative):** What you're trying to prove.

> Example: A pill claims to reduce blood pressure.
> H₀: Pill has NO effect. H₁: Pill DOES reduce blood pressure.

**Step 2 — Choose significance level α** (usually 0.05)
This means: "I accept a 5% chance of being wrong."

**Step 3 — Collect data, compute test statistic**
A single number summarising how far your sample is from what H₀ predicts.

**Step 4 — Find the p-value**
Probability of seeing data this extreme if H₀ were true.

**Step 5 — Decide**
- p ≤ α → Reject H₀
- p > α → Fail to reject H₀

> ⚠️ "Fail to reject H₀" ≠ "H₀ is true." It just means not enough evidence against it.

---

## Formula (General)

```
Test Statistic = (Observed value − Expected value under H₀) / Standard Error
```

---

## Types of Tests at a Glance

| Test | When to Use |
|---|---|
| Z-test | Large sample, known population σ |
| t-test | Small sample, unknown σ |
| Chi-square | Categorical data |
| ANOVA | Comparing 3+ group means |

---

# 2. What is P-value?

## What is it?

The probability of getting results **as extreme as (or more extreme than)** your observation — **assuming H₀ is true**.

Plain English: *How likely is it that random chance alone produced your result?*

---

## Intuition

You flip a coin 10 times and get 9 heads. Is the coin biased?

If the coin were fair, what's the chance of getting 9 or 10 heads purely by luck? That probability = your **p-value**.

- Small p-value → result would be rare if H₀ were true → strong evidence against H₀
- Large p-value → result is common under H₀ → no strong evidence

---

## Analogy: The Rainstorm Test

A weather app claims it rains only 20% of days in January. You observe 22 rainy days out of 30. The p-value answers: *"If 20% were really true, how often would I see 22+ rainy days just by luck?"* If that probability is tiny, the app's model is wrong.

---

## Formula

```
p-value = P(Z ≥ z_observed)           [right-tailed]
p-value = P(Z ≤ z_observed)           [left-tailed]
p-value = 2 × P(Z ≥ |z_observed|)     [two-tailed]
```

---

## Decision Rule

- p ≤ 0.05 → Statistically significant → Reject H₀
- p > 0.05 → Not significant → Fail to reject H₀

---

## Common Misconceptions

| Wrong | Correct |
|---|---|
| p = 0.03 means H₀ is 3% likely to be true | It means data this extreme occurs 3% of the time IF H₀ is true |
| p > 0.05 proves H₀ is true | It just means insufficient evidence to reject it |
| Small p = large practical effect | Small p only means statistical significance |

---

# 3. Z-Test – Hypothesis Testing

## What is it?

Tests whether a sample mean is significantly different from a known population mean — when the **population standard deviation σ is known** (or n is large).

---

## Intuition

You manage a biscuit factory. Each packet should weigh 200g (σ = 5g known from years of data). You sample 50 packets: average = 197g. Is the machine miscalibrated, or is this normal variation?

The Z-statistic converts your result into "how many standard errors away from the target" — a universal scale you can look up.

---

## When to Use

- Sample size n ≥ 30
- Population standard deviation σ is known

---

## Formula

```
       x̄ − μ₀
Z = ───────────
       σ / √n

x̄  = sample mean
μ₀ = hypothesized population mean
σ  = population standard deviation (known)
n  = sample size
```

---

## Critical Values

| α | One-tailed | Two-tailed |
|---|---|---|
| 0.10 | 1.28 | 1.645 |
| 0.05 | 1.645 | 1.96 |
| 0.01 | 2.33 | 2.576 |

**Decision:** |Z_calculated| > Z_critical → Reject H₀ or **p-value < α**

---

## Worked Example

> Average height of Indian men = 165 cm (σ = 6 cm). Sample: n = 36, x̄ = 167 cm. Test at α = 0.05 (two-tailed).

```
H₀: μ = 165    H₁: μ ≠ 165
Z_critical = ±1.96

Z = (167 − 165) / (6 / √36) = 2 / 1 = 2.0

|Z| = 2.0 > 1.96 → Reject H₀

Conclusion: Average height is significantly different from 165 cm.
```

---

# 4. Student's t Distribution

## What is it?

A bell-shaped distribution used **instead of the normal distribution** when sample size is small and σ is unknown. It has **heavier tails** than the normal, reflecting extra uncertainty.

---

## Intuition & Origin

William Gosset worked at Guinness Brewery in 1908. He needed to test beer quality with tiny sample sizes. He discovered that using the normal distribution on small samples gave overconfident results — the uncertainty from estimating σ itself makes the distribution wider.

He published under the pseudonym **"Student"** — hence Student's t-distribution.

*The smaller your sample, the less certain you are, so the distribution should have wider tails.*

---

## Analogy

You want to know the average software engineer salary in Bengaluru.

- Ask 3000 people → estimate is reliable → use normal distribution
- Ask only 5 friends → estimate could be way off → use t-distribution (accounts for extra uncertainty)

---

## Key Property: Degrees of Freedom

**df = n − 1**

- As df increases → t-distribution approaches the normal distribution
- With df < 30 → noticeably wider tails than normal
- At df → ∞ → t = Z (identical)

---

## Formula

```
       x̄ − μ₀
t = ───────────       df = n − 1
       s / √n

s = sample standard deviation (estimated, not known)
```

**Note:** s uses (n−1) in the denominator — this is **Bessel's correction**, which corrects for the bias in estimating population variance from a small sample.

---

## t Critical Values Table

| df | α = 0.05 (two-tailed) | α = 0.01 |
|---|---|---|
| 5 | 2.571 | 4.032 |
| 10 | 2.228 | 3.169 |
| 20 | 2.086 | 2.845 |
| 30 | 2.042 | 2.750 |
| ∞ | 1.960 | 2.576 |

> As df increases, t critical values converge to Z critical values.

---

# 5. T-Statistics with t-Test Hypothesis Testing

## What is it?

A hypothesis test using the t-distribution to determine if means are significantly different — when σ is unknown and/or sample is small.

---

## Three Types of t-Tests

### One-Sample t-Test
Compare a sample mean against a known/hypothesized value.

> Is the average weight of students in this class = 60 kg?

```
       x̄ − μ₀
t = ───────────    df = n − 1
       s / √n
```

---

### Independent Two-Sample t-Test
Compare means of two **separate, independent groups**.

> Do Group A (new teaching) and Group B (old teaching) score differently?

```
         x̄₁ − x̄₂
t = ─────────────────────────    df = n₁ + n₂ − 2
     sp × √(1/n₁ + 1/n₂)

sp = √[(n₁−1)s₁² + (n₂−1)s₂²) / (n₁+n₂−2)]   (pooled std dev)
```

---

### Paired t-Test
Same subjects measured **before and after**. Compare the differences.

> Did a diet program reduce weight in the same group of people?

```
        d̄
t = ────────      df = n − 1
     sd / √n

d̄  = mean of (after − before) differences
sd = standard deviation of differences
```

---

## Worked Example: One-Sample t-Test

> Claim: Average exam score = 70. Sample: n = 10, x̄ = 75, s = 8. Test at α = 0.05 (two-tailed).

```
H₀: μ = 70    H₁: μ ≠ 70
df = 9 → t_critical = ±2.262

t = (75 − 70) / (8 / √10) = 5 / 2.53 = 1.976

|t| = 1.976 < 2.262 → Fail to reject H₀

Conclusion: Not enough evidence that the mean differs from 70.
```

---

# 6. Z-test vs T-test

## Core Difference

| Feature | Z-Test | t-Test |
|---|---|---|
| Population σ | Known | Unknown (use sample s) |
| Sample size | n ≥ 30 | n < 30 (safe for any n) |
| Distribution | Standard Normal | t-distribution |
| Degrees of freedom | Not applicable | df = n − 1 |
| As n → ∞ | — | Converges to Z-test |

---

## Decision Rule

- σ known AND n ≥ 30 → Z-test
- σ unknown OR n < 30 → t-test
- **When in doubt → use t-test** (for large n, results are virtually identical)

---

## Analogy

- **Z-test:** A doctor with 40 years of records knows the exact disease statistics → confident, uses Z.
- **t-test:** A new doctor estimating from 10 patient records → appropriately uncertain, uses t.

---

# 7. Type I and Type II Errors

## What are they?

- **Type I Error (α):** Rejecting H₀ when it's actually TRUE → False Positive
- **Type II Error (β):** Failing to reject H₀ when it's actually FALSE → False Negative

---

## The 4 Possible Outcomes

| | H₀ is TRUE | H₀ is FALSE |
|---|---|---|
| **Reject H₀** | ❌ Type I Error (α) | ✅ Correct (Power = 1−β) |
| **Fail to Reject H₀** | ✅ Correct | ❌ Type II Error (β) |

---

## Analogy: Medical Cancer Test

> H₀: Patient does NOT have cancer.

- **Type I Error:** Healthy patient tests positive → unnecessary treatment.
- **Type II Error:** Cancer patient tests negative → sent home untreated (potentially fatal).

Both errors are costly — just in different ways.

---

## Key Relationships

```
α = P(Reject H₀ | H₀ is true)
β = P(Fail to reject H₀ | H₀ is false)
Power = 1 − β
```

**α and β trade-off** (fixed sample size):
- Decrease α (stricter test) → β increases (easier to miss real effects)
- Increase α (looser test) → β decreases (but more false alarms)

**Solution:** Increase sample size n → reduces both α and β simultaneously.

---

## Real-World Examples

| Field | Type I Error | Type II Error |
|---|---|---|
| Medicine | Treating a healthy patient | Missing a real disease |
| Law | Convicting innocent person | Freeing guilty person |
| Spam filter | Blocking real email | Letting spam through |
| ML model | False positive prediction | Missed true positive |

---

# 8. Bayes Theorem

## What is it?

A formula that updates the probability of a hypothesis **after receiving new evidence**. It answers: *"Given new data, how should I update my belief?"*

---

## Intuition

Traditional (Frequentist) stats asks: *"If H₀ is true, how likely is this data?"*

Bayes asks: *"Given this data, how likely is H₀?"* — which is actually what we want to know.

Bayes Theorem is the mathematical rule for updating beliefs correctly based on evidence.

---

## Components

| Symbol | Meaning |
|---|---|
| P(A) | **Prior** — belief BEFORE seeing evidence |
| P(B\|A) | **Likelihood** — probability of evidence given A is true |
| P(B) | **Marginal** — total probability of the evidence |
| P(A\|B) | **Posterior** — updated belief AFTER seeing evidence |

---

## Formula

```
         P(B|A) × P(A)
P(A|B) = ──────────────
               P(B)

Expanding P(B):
P(B) = P(B|A)·P(A) + P(B|Ā)·P(Ā)
```

---

## Worked Example: Medical Diagnosis

- Disease affects 1% of population: P(Disease) = 0.01
- Test is 95% accurate: P(Positive | Disease) = 0.95
- False positive rate: P(Positive | No Disease) = 0.05

> You test positive. How likely are you to actually have the disease?

```
P(B) = 0.95×0.01 + 0.05×0.99
     = 0.0095 + 0.0495 = 0.059

P(Disease | Positive) = 0.0095 / 0.059 ≈ 16.1%
```

**Most people guess 95%. The true answer is only ~16%.**

Why? The disease is rare. Most positives in a healthy population are false alarms.

---

## Where Bayes is Used

- Spam filters: P(spam | these words)
- Medical diagnosis
- Naive Bayes Classifier in ML
- Fraud detection
- Bayesian A/B testing

---

# 9. Confidence Interval and Margin of Error

## What is it?

A **confidence interval (CI)** is a range of values likely to contain the true population parameter. The **margin of error (MoE)** is the ± half-width of that range.

---

## Intuition

A point estimate (sample mean) is like throwing one dart — you could easily miss. A confidence interval is like casting a net — you're much more likely to capture the true value.

> "I am 95% confident the true mean lies between X and Y."

The 95% means: if you repeated this study 100 times, about 95 of the resulting intervals would contain the true mean.

---

## Analogy: Election Poll

> "Candidate A leads with 52% — margin of error ±3%."

True support is somewhere between **49% and 55%** with 95% confidence. That ±3% = **margin of error**. The interval [49%, 55%] = **confidence interval**.

---

## Formula

**Large sample (Z-based):**
```
CI = x̄ ± Z* × (σ/√n)
MoE = Z* × (σ/√n)
```

**Small sample (t-based):**
```
CI = x̄ ± t* × (s/√n)
```

**Critical values:**

| Confidence Level | Z* |
|---|---|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

---

## Worked Example

> n = 100, x̄ = 68 kg, σ = 10 kg. Build a 95% CI.

```
MoE = 1.96 × (10/√100) = 1.96 × 1 = 1.96

CI = (68 − 1.96, 68 + 1.96) = (66.04 kg, 69.96 kg)

Interpretation: 95% confident the true average weight 
is between 66.04 and 69.96 kg.
```

---

## What Affects CI Width?

| Makes CI Wider | Makes CI Narrower |
|---|---|
| Higher confidence (99%) | Lower confidence (90%) |
| Smaller sample size | Larger sample size |
| Higher variability (large σ) | Lower variability |

---

# 10. What is Chi-Square Test?

## What is it?

A test for **categorical data** that checks whether observed frequencies differ significantly from expected frequencies, or whether two categorical variables are independent.

---

## Intuition

Most tests deal with means and continuous data. But what about:
- *Are men and women equally likely to prefer tea vs coffee?*
- *Is this die fair?*
- *Do students from different cities prefer different careers?*

These involve **counts and categories**, not averages. The Chi-Square test is built exactly for this — it measures the gap between what you observed and what you expected.

---

## Types of Chi-Square Tests

| Test | Purpose |
|---|---|
| Goodness of Fit | Does sample distribution match expected distribution? |
| Test of Independence | Are two categorical variables related? |
| Test of Homogeneity | Are proportions equal across populations? |

---

## Formula

```
         (O − E)²
χ² = Σ  ──────────
             E

O = Observed frequency
E = Expected frequency

df = (categories − 1)            [Goodness of Fit]
df = (rows − 1)(columns − 1)     [Independence Test]
```

**Logic:**
- O = E everywhere → χ² = 0 (perfect fit)
- Large gaps between O and E → large χ² → small p-value → reject H₀

---

## Assumptions

1. Data is categorical.
2. Observations are independent.
3. Each expected frequency ≥ 5.
4. Reasonably large sample size.

---

# 11. Chi-Square Goodness of Fit

## What is it?

Tests whether an **observed frequency distribution** matches a **hypothesized expected distribution**.

---

## Intuition

You have a theory about how data should be distributed. You collect real data. Goodness of Fit asks: *Does my observed data fit the expected distribution?*

---

## Worked Example: Netflix Genre Preferences

Netflix expects: Action 40%, Comedy 35%, Drama 25%.
Survey of 200 subscribers shows:

| Genre | Observed (O) | Expected (E) | (O−E)²/E |
|---|---|---|---|
| Action | 70 | 80 | 1.25 |
| Comedy | 80 | 70 | 1.43 |
| Drama | 50 | 50 | 0.00 |
| **Total** | **200** | **200** | **χ² = 2.68** |

```
H₀: Observed = Expected distribution
df = 3 − 1 = 2
χ²_critical (α=0.05, df=2) = 5.991

χ² = 2.68 < 5.991 → Fail to Reject H₀

Conclusion: No significant difference from expected preferences.
```

---

# 12. ANOVA Test

## What is it?

**Analysis of Variance (ANOVA)** compares the means of **three or more groups simultaneously** to determine if at least one group mean is significantly different.

---

## Why Not Just Run Multiple t-Tests?

If you run 3 t-tests (A vs B, B vs C, A vs C), each has 5% error chance.

Combined error rate ≈ 1 − (0.95)³ ≈ **14.3%** — that's **alpha inflation**.

ANOVA tests all groups at once, keeping error at exactly α = 0.05.

---

## Core Idea

Compare **variation between groups** to **variation within groups**.

- If between-group variation >> within-group variation → at least one group mean differs.
- If they're similar → differences are just noise.

---

## Hypotheses

- H₀: μ₁ = μ₂ = μ₃ = ... = μₖ (all group means equal)
- H₁: At least one group mean is different

---

## Formula

```
       MSB     SSB/(k−1)
F =  ───── = ───────────
       MSW     SSW/(N−k)

SSB = Σ nⱼ(x̄ⱼ − x̄)²    [Between-group sum of squares]
SSW = ΣΣ(xᵢⱼ − x̄ⱼ)²   [Within-group sum of squares]

k = number of groups
N = total observations
df₁ = k−1,  df₂ = N−k
```

---

## ANOVA Table

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between Groups | SSB | k−1 | MSB = SSB/(k−1) | F = MSB/MSW |
| Within Groups | SSW | N−k | MSW = SSW/(N−k) | |
| Total | SST | N−1 | | |

---

## Interpreting F

- F ≈ 1 → No meaningful group difference → Fail to reject H₀
- F >> 1 → Groups genuinely differ → Reject H₀

---

## Important Limitation

ANOVA only tells you **that** a difference exists — not **which** groups differ. Use post-hoc tests (Tukey's HSD, Bonferroni) to find out which pairs differ.

---

# 13. Assumptions of ANOVA

## The 4 Assumptions

### 1. Independence of Observations
Each observation must be independent. Random sampling ensures this.

### 2. Normality
Data within each group should be approximately normally distributed.

How to check: Shapiro-Wilk test, Q-Q plot, histogram.

ANOVA is robust to mild violations when n is large (Central Limit Theorem). For small n + severe non-normality → use **Kruskal-Wallis test** (non-parametric alternative).

### 3. Homogeneity of Variances (Homoscedasticity)
Variance within each group should be approximately equal: σ₁² ≈ σ₂² ≈ ... ≈ σₖ²

How to check: Levene's Test, Bartlett's Test.

If severely violated → use **Welch's ANOVA** instead.

### 4. Interval or Ratio Scale
The dependent variable must be continuous numeric data, not categorical.

---

## Quick Reference

| Assumption | How to Check | If Violated |
|---|---|---|
| Independence | Study design | Redesign; use mixed-effects model |
| Normality | Shapiro-Wilk, Q-Q plot | Kruskal-Wallis test |
| Equal variances | Levene's test | Welch's ANOVA |
| Continuous DV | Know your data | Use Chi-square for categorical |

---

# 14. Types of ANOVA

## One-Way ANOVA

**One independent variable, 3+ groups.**

> Test scores across three teaching methods: Lecture, Online, Project-based.

Tests: Is μ_A = μ_B = μ_C?

---

## Two-Way ANOVA

**Two independent variables simultaneously.**

> Test scores by Teaching Method AND by Gender.

Detects three things:
- **Main effect of Factor 1** — does teaching method affect scores?
- **Main effect of Factor 2** — does gender affect scores?
- **Interaction effect** — does the effect of teaching method differ by gender?

The interaction is the most powerful insight — it reveals effects that one-way ANOVA would miss entirely.

---

## Repeated Measures ANOVA

**Same subjects measured multiple times** (across time or conditions).

> Blood pressure of same patients: before treatment, after 1 month, after 3 months.

Like a paired t-test but for 3+ time points.

---

## Summary Table

| Type | Factors | Subjects | Use Case |
|---|---|---|---|
| One-Way | 1 | Independent | 3+ independent groups |
| Two-Way | 2 | Independent | 2 factors + possible interaction |
| Repeated Measures | 1+ | Same subjects | Multiple measurements per subject |

---

# 15. Partitioning of Variance in ANOVA

## What is it?

ANOVA works by **splitting total variation** in your data into:
1. Variation **due to group differences** (SSB)
2. Variation **due to random noise** within groups (SSW)

---

## Intuition

You measure 30 students' test scores. Scores vary. Why?

1. Different students had different teachers (group effect)
2. Even within the same class, individual students differ (random noise)

ANOVA separates these two sources to decide: *Is the group-level difference real, or just noise?*

---

## The Core Equation

```
SST = SSB + SSW

SST = Σ(xᵢ − x̄)²              Total variation (all obs vs grand mean)
SSB = Σ nⱼ(x̄ⱼ − x̄)²           Between-group variation (group means vs grand mean)
SSW = ΣΣ(xᵢⱼ − x̄ⱼ)²          Within-group variation (obs vs their group mean)
```

### Total Sum of Squares (SST)

$$
SS_T = \sum x_{ij}^{2} - \frac{T^2}{N}
$$

### Between-Groups Sum of Squares (SSB)

$$
SS_B = \sum_{i=1}^{k}\frac{T_i^2}{n_j} - \frac{T^2}{N}
$$

### For equal-sized groups \(n_j = n\):

$$
SS_B = \frac{\sum T_i^2}{n} - \frac{T^2}{N}
$$

### Within-Groups Sum of Squares (SSW)

$$
SS_W = \sum x_{ij}^{2} - \sum_{i=1}^{k}\frac{T_i^2}{n_j}
$$

---

## How One Score Decomposes

> Student score = 75, Grand mean = 65, Their class mean = 70

```
Total deviation    = 75 − 65 = 10
Between (class)    = 70 − 65 = 5   (class is above average)
Within (personal)  = 75 − 70 = 5   (student is above class average)

5 + 5 = 10 ✓
```

Every single observation's deviation can be split this way — that's the beauty of the partition.

---

## Effect Size: η² (Eta-Squared)

F tells you *if* a difference exists. η² tells you *how big* it is.

```
       SSB
η² = ─────       Range: 0 to 1
       SST

η² = 0.01 → Small effect
η² = 0.06 → Medium effect
η² = 0.14 → Large effect
```

> A result can be statistically significant but practically tiny, especially with large n. Always report η².

---

## Two-Way ANOVA: Extended Partitioning

```
SST = SSA + SSB + SS(A×B) + SSW

SSA      = Main effect of Factor A
SSB      = Main effect of Factor B
SS(A×B)  = Interaction effect (A and B together)
SSW      = Error (within-group noise)
```

Each component has its own F-statistic and p-value.

---

# 📋 Formula Quick Reference

```
Z-Test:               Z = (x̄ − μ₀) / (σ/√n)

One-sample t-Test:    t = (x̄ − μ₀) / (s/√n),    df = n−1

Two-sample t-Test:    t = (x̄₁ − x̄₂) / [sp√(1/n₁ + 1/n₂)]

Paired t-Test:        t = d̄ / (sd/√n),            df = n−1

Confidence Interval:  x̄ ± Z*(σ/√n)   or   x̄ ± t*(s/√n)

Bayes Theorem:        P(A|B) = P(B|A)·P(A) / P(B)

Chi-Square:           χ² = Σ[(O−E)²/E]

ANOVA F-statistic:    F = MSB/MSW = [SSB/(k−1)] / [SSW/(N−k)]

Eta-Squared:          η² = SSB/SST
```

---

# 🧠 Memory Aids

| Concept | Remember it as |
|---|---|
| Type I Error | **False Alarm** — you cried wolf |
| Type II Error | **Missed it** — the wolf got through |
| p-value | Probability of your result if H₀ were true |
| t vs Z | **t = tiny sample, tricky** |
| ANOVA | Compares variance **between** groups to variance **within** |
| Chi-square | For **Counts and Categories** only |
| Bayes | Prior belief + Evidence = Updated belief |
| Confidence Interval | A net, not a single hook |

---

*"Without data, you're just another person with an opinion." — W. Edwards Deming*