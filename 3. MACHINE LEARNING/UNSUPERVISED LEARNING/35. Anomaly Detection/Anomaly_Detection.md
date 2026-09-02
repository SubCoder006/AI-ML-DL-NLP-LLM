# Anomaly Detection — Isolation Forest & Local Outlier Factor

## What is Anomaly Detection?
**Goal:** Detect **outliers** — data points that deviate significantly from the rest of the data.
Outliers play an important role in many real-world problems (fraud detection, sports stats, sensor faults, etc.)

**Example:** In an IPL dataset of runs scored, most values are small (10–15), but one value like `100` stands out as an outlier.

---

## 1. Isolation Forest

### Core Idea
Anomalies are **few and different**, so they are **easier to isolate** than normal points.

- Uses **many decision trees** → called an **Isolation Forest**
- Each tree randomly splits the data (random feature + random split value)
- **Outliers** get isolated **quickly** (fewer splits, closer to root, shallow depth)
- **Normal points** need **more splits** to isolate (deeper in the tree)

### Key Terms
| Term | Meaning |
|---|---|
| Isolated Tree | A tree where a point becomes a leaf node quickly |
| Isolated Node | A point separated by very few splits — likely an outlier |
| Path Length `h(x)` | Number of splits needed to isolate point `x` |

### Anomaly Score Formula

$$
S(x, m) = 2^{-\frac{E(h(x))}{c(m)}}
$$

**Where:**
- `x` = data point  
- `m` = number of data points  
- `E(h(x))` = average path length (search depth) of `x` across all isolation trees  
- `c(m)` = average path length of unsuccessful search in a Binary Search Tree (normalization factor)

### Interpretation

| Condition | Result | Meaning |
|---|---|---|
| `E(h(x)) << c(m)` | `S(x,m) ≈ 1` | **Anomaly / Outlier** (isolated quickly) |
| `E(h(x)) >> c(m)` | `S(x,m) ≈ 0` | **Normal data point** (needs many splits) |

**Threshold:** Score `> 0.5` → considered an **outlier**

---

## 2. Local Outlier Factor (LOF)

### Core Idea
LOF detects outliers based on **local density** — comparing a point's density to the density of its **neighbors**, rather than the whole dataset.

### Two Types of Outliers
1. **Local Outlier** — a point that has low density *relative to its nearby neighbors*, even if it lies close to some cluster
2. **Global Outlier** — a point that is far from all clusters entirely (obvious outlier)

> LOF is especially useful for catching **local outliers**, which simple distance-based methods (like a single global threshold) can miss — a point can look "normal" globally but still be a local outlier compared to its neighborhood.

### How It Works
1. Compute **K-Nearest Neighbours (KNN)** for each point (`k` is a hyperparameter, e.g. `k = 5`)
2. Estimate **local density** of each point based on distance to its k neighbors
3. Compare a point's local density to the **local density of its neighbors**
4. This ratio gives the **LOF Score**

### LOF Score Interpretation
| LOF Score | Meaning |
|---|---|
| ≈ 1 | Similar density to neighbors → **normal point** |
| >> 1 | Much lower density than neighbors → **outlier** |

### Key Flow
```
K-Nearest Neighbour → Local Density → Compare with Neighbors' Density → LOF Score
```

---

## Quick Comparison

| Aspect | Isolation Forest | Local Outlier Factor |
|---|---|---|
| Basis | Isolation via random splits (tree-based) | Density comparison with neighbors |
| Detects | Global outliers (isolates points fast) | Local + global outliers |
| Key metric | Path length → Anomaly Score `S(x,m)` | Density ratio → LOF Score |
| Sensitive to | Number of trees, subsample size | Choice of `k` (neighbors) |
