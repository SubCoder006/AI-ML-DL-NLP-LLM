# DBSCAN Clustering

**DBSCAN** = Density-Based Spatial Clustering of Applications with Noise.
It groups points that are **densely packed together**, and marks points in low-density regions as **outliers/noise**. Unlike K-Means, it can find **non-linear (arbitrary shaped)** clusters.

## Core Idea

Two parameters control everything:

- **ε (epsilon)** — radius of the neighborhood around a point
- **minPts** — minimum number of points required inside that radius (including the point itself) for it to be considered "dense"

## Types of Points

**Core Point**
A point that has **≥ minPts** points (including itself) within its ε radius.
→ Lies inside a dense region.

**Border Point**
A point that has **fewer than minPts** points within its ε radius, but it lies **within the ε radius of a core point**.
→ On the edge of a cluster, reachable from a core point but not dense itself.

**Outlier / Noise Point**
A point that is **neither a core point nor reachable from any core point**.
→ Doesn't belong to any cluster.

## How Clusters Form

- Core points that are within each other's ε radius get connected → they form a single cluster (density-reachable chain).
- Border points get attached to the cluster of the nearest core point that "reaches" them.
- Everything else left over becomes noise.

## Non-Linear Clustering

Since DBSCAN grows clusters by chaining nearby dense points rather than measuring distance from a center (like K-Means), it can capture **curved, irregular, and non-convex shapes** — clusters that K-Means or GMM would fail to separate correctly.

## Pros

- No need to specify number of clusters beforehand
- Can find arbitrarily shaped clusters
- Naturally detects and handles outliers/noise
- Robust to clusters of different shapes (not just spherical)

## Cons

- Struggles when clusters have **varying densities** (one global ε/minPts doesn't fit all)
- Sensitive to the choice of ε and minPts — bad values can merge clusters or call everything noise
- Not great in high-dimensional data (distance becomes less meaningful — "curse of dimensionality")
- Doesn't work well when clusters are close together with little density gap between them
