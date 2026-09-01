# Hierarchical Clustering

## What is it?
**Hierarchical Clustering (HC)** groups data into clusters **without needing centroids** — it builds a tree of nested clusters instead of picking K upfront like K-Means.

---

## Two Types
1. **Agglomerative** — bottom-up: start with individual points, merge them into bigger clusters
2. **Divisive** — top-down: start with one big cluster, split it into smaller ones

---

## Agglomerative — How it Works (Steps)
1. Treat **each point** as its own **separate cluster**
2. Find the **nearest points/clusters** and **merge** them into a new cluster
3. **Repeat** the merging process until **all points** end up in a **single cluster**

> Distance between points/clusters is measured using **Euclidean Distance**

---

## Dendrogram
A **tree diagram** that visually records the merging order — shows *which* clusters merged and *at what distance*.

- **X-axis** → individual data points
- **Y-axis** → Euclidean Distance at which merges happened
- Lower merges = points that are very similar (merged early, at small distance)
- Higher merges = less similar clusters (merged later, at large distance)

---

## Choosing Number of Clusters (K) — Threshold Method
1. Set a **threshold** (a distance cutoff line) on the dendrogram
2. **Select the longest vertical line such that no horizontal line passes through it**
3. Count how many vertical lines the threshold line crosses → that's your **K**

> Example: a low threshold can give K=4, a higher threshold can give K=2 — fewer, bigger clusters.

---

## K-Means vs Hierarchical Clustering
| Aspect | K-Means | Hierarchical |
|---|---|---|
| Need K upfront? | Yes | No (decide later via dendrogram) |
| Uses centroids? | Yes | No |
| Output | Fixed K clusters | Tree of nested clusters (dendrogram) |
| Speed on large data | Faster | Slower (compares all pairs) |
| Flexibility | Fixed shape/size clusters | Can capture nested/hierarchical structure |

---

## Quick Recap
| Concept | One-liner |
|---|---|
| Agglomerative | Bottom-up merging of points into clusters |
| Divisive | Top-down splitting of one cluster into many |
| Dendrogram | Tree diagram showing merge order & distances |
| Threshold | Distance cutoff line used to decide final K |
