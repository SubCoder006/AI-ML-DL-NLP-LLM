# K-Means Clustering

## What is it?
**K-Means** is an **unsupervised ML algorithm** that groups unlabeled data into **K clusters**, where each point belongs to the cluster with the **nearest centroid** (center point).

---

## How it Works (Algorithm)
1. **Initialize** — pick some `K` points as **centroids**
2. **Assign** — group each point to its **nearest centroid**
3. **Update** — move each centroid to the **average (mean)** position of its group
4. **Repeat** steps 2–3 until centroids stop moving (converge)

---

## Distance Metrics
Used to measure "nearest" point to a centroid.

**Euclidean Distance** (straight-line distance):
$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$
> Use case: air traffic, physical straight-path distance (e.g. Iron Man flying point-to-point)

**Manhattan Distance** (grid-like distance):
$$d = |x_2-x_1| + |y_2-y_1|$$
> Use case: city block movement — like a taxi driving along street blocks (can't cut diagonally)

---

## How to Choose K? (Elbow Method)
- **WCSS** = **Within Cluster Sum of Squares** — sum of squared distances between each point and its nearest centroid
$$WCSS = \sum_{i=1}^{n} (\text{distance from point to nearest centroid})^2$$
- Run K-Means for `K = 1 to 20`, plot **WCSS vs K**
- WCSS **decreases** as K increases (more clusters = tighter groups)
- The **"elbow" point** — where the drop sharply flattens — is the best K

---

## Random Initialization Trap
- If starting centroids are picked **randomly**, K-Means can converge to a **bad/wrong clustering**
- Poor initial centroid placement → clusters don't match the actual data groups

### Fix: K-Means++
A smarter initialization technique:
- Spreads out initial centroids instead of placing them randomly close together
- Leads to **better, more consistent** final clusters

---

## Quick Recap
| Concept | One-liner |
|---|---|
| K-Means | Groups data into K clusters by nearest centroid |
| Centroid | Mean position of points in a cluster |
| WCSS | Measures cluster tightness; used to pick best K |
| Elbow Method | Plot WCSS vs K, pick the bend point |
| K-Means++ | Smart centroid init to avoid bad clustering |