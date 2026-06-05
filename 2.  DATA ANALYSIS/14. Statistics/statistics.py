# Statistics in Python — Simple Examples
# Dataset: Exam scores of 20 students

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

scores = np.array([45, 52, 61, 61, 63, 65, 67, 70, 72, 73,
                   74, 75, 78, 80, 82, 85, 88, 91, 94, 99])

study_hours = np.array([1, 2, 2, 3, 4, 4, 5, 5, 6, 6,
                        7, 7, 7, 8, 8, 9, 9, 10, 10, 11])

print("Dataset:", scores)

# ── Central Tendency ─────────────────────────────────────────
print("\n--- Central Tendency ---")
print("Mean   :", np.mean(scores))          # average
print("Median :", np.median(scores))        # middle value
print("Mode   :", stats.mode(scores).mode)  # most frequent value

# ── Dispersion ───────────────────────────────────────────────
print("\n--- Dispersion ---")
print("Range    :", scores.max() - scores.min())       # spread of data
print("Variance :", round(np.var(scores, ddof=1), 2))  # avg squared deviation (sample)
print("Std Dev  :", round(np.std(scores, ddof=1), 2))  # square root of variance

# ── Percentiles & Quartiles ──────────────────────────────────
print("\n--- Percentiles & Quartiles ---")
Q1  = np.percentile(scores, 25)   # 25% of data falls below this
Q2  = np.percentile(scores, 50)   # same as median
Q3  = np.percentile(scores, 75)   # 75% of data falls below this
IQR = Q3 - Q1                     # spread of middle 50%
print(f"Q1={Q1},  Q2={Q2},  Q3={Q3},  IQR={IQR}")
print("70th Percentile:", np.percentile(scores, 70))

# ── 5-Number Summary ─────────────────────────────────────────
print("\n--- 5-Number Summary ---")
print("Min    :", scores.min())
print("Q1     :", Q1)
print("Median :", Q2)
print("Q3     :", Q3)
print("Max    :", scores.max())

# ── Outlier Detection ────────────────────────────────────────
print("\n--- Outliers (IQR method) ---")
lower = Q1 - 1.5 * IQR   # anything below this is an outlier
upper = Q3 + 1.5 * IQR   # anything above this is an outlier
outliers = scores[(scores < lower) | (scores > upper)]
print(f"Fences: [{lower}, {upper}]")
print("Outliers:", outliers if len(outliers) > 0 else "None")

# ── Variance: Biased (÷n) vs Unbiased (÷n-1) ─────────────────
print("\n--- Bessel's Correction ---")
print("Pop Variance  (÷n)  :", round(np.var(scores),        2))  # biased
print("Samp Variance (÷n-1):", round(np.var(scores, ddof=1), 2)) # unbiased

# ── Empirical Rule (68-95-99.7) ──────────────────────────────
print("\n--- Empirical Rule ---")
mu, s = np.mean(scores), np.std(scores, ddof=1)
for k in [1, 2, 3]:
    lo, hi = mu - k*s, mu + k*s
    pct = np.sum((scores >= lo) & (scores <= hi)) / len(scores) * 100
    print(f"  μ ± {k}σ  [{lo:.1f}, {hi:.1f}]  →  {pct:.0f}% of data  (theory: {[68,95,99][k-1]}%)")

# ── Correlation & Covariance ─────────────────────────────────
print("\n--- Correlation & Covariance ---")
cov = np.cov(study_hours, scores)[0, 1]              # how X and Y move together
r, p = stats.pearsonr(study_hours, scores)           # standardized (-1 to +1)
print(f"Covariance  : {cov:.2f}   (hard to interpret, scale-dependent)")
print(f"Correlation : r = {r:.4f}  (scale-free, strong positive)")
print(f"P-value     : {p:.6f}  (statistically significant)")

# ── Confidence Interval ──────────────────────────────────────
print("\n--- 95% Confidence Interval for Mean ---")
ci = stats.t.interval(0.95, df=len(scores)-1,
                       loc=np.mean(scores), scale=stats.sem(scores))
print(f"({ci[0]:.2f}, {ci[1]:.2f})  → true mean likely falls in this range")

# ── Plots ─────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Statistics — Visual Summary", fontsize=14, fontweight="bold")

# Histogram
axes[0,0].hist(scores, bins=8, color="steelblue", edgecolor="white")
axes[0,0].axvline(mu, color="red", linestyle="--", label=f"Mean={mu:.1f}")
axes[0,0].axvline(np.median(scores), color="orange", linestyle="--", label=f"Median={np.median(scores):.1f}")
axes[0,0].set_title("Histogram"); axes[0,0].legend(fontsize=8)

# Box plot (shows 5-number summary visually)
axes[0,1].boxplot(scores, patch_artist=True,
                  boxprops=dict(facecolor="steelblue", alpha=0.5),
                  medianprops=dict(color="red", linewidth=2))
axes[0,1].set_title("Box Plot (5-Number Summary)")

# PMF — discrete random variable (coin toss)
x = np.arange(0, 4)
pmf = stats.binom.pmf(x, n=3, p=0.5)
axes[0,2].bar(x, pmf, color="mediumseagreen", edgecolor="white", width=0.5)
[axes[0,2].text(i, pmf[i]+0.005, f"{pmf[i]:.3f}", ha="center", fontsize=9) for i in x]
axes[0,2].set_title("PMF — Coin Toss (Discrete RV)")
axes[0,2].set_xlabel("Heads"); axes[0,2].set_ylabel("P(X=x)")

# PDF — continuous random variable (heights)
x_h = np.linspace(140, 200, 300)
axes[1,0].plot(x_h, stats.norm.pdf(x_h, 170, 10), color="darkorange", linewidth=2)
axes[1,0].fill_between(np.linspace(160,180,200),
                        stats.norm.pdf(np.linspace(160,180,200), 170, 10),
                        alpha=0.3, color="darkorange", label="P(160≤X≤180)")
axes[1,0].set_title("PDF — Heights (Continuous RV)"); axes[1,0].legend(fontsize=8)

# Empirical Rule
x_n = np.linspace(mu-4*s, mu+4*s, 400)
axes[1,1].plot(x_n, stats.norm.pdf(x_n, mu, s), color="navy", linewidth=2)
for k, color in zip([3,2,1], ["#d4e6f1","#a9cce3","#7fb3d3"]):
    x_s = np.linspace(mu-k*s, mu+k*s, 300)
    axes[1,1].fill_between(x_s, stats.norm.pdf(x_s, mu, s),
                            alpha=0.6, color=color, label=f"±{k}σ")
axes[1,1].set_title("Empirical Rule"); axes[1,1].legend(fontsize=7)

# Correlation scatter
m, b = np.polyfit(study_hours, scores, 1)
axes[1,2].scatter(study_hours, scores, color="steelblue", edgecolors="white", s=60)
axes[1,2].plot(np.linspace(1,11,100), m*np.linspace(1,11,100)+b, color="red", linewidth=2, label=f"r={r:.3f}")
axes[1,2].set_title("Correlation: Study Hours vs Score")
axes[1,2].set_xlabel("Study Hours"); axes[1,2].legend(fontsize=8)

plt.tight_layout()
plt.show()
plt.close()
