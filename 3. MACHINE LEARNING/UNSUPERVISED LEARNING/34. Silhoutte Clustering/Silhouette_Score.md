# Silhouette Score (Clustering Evaluation)

Silhouette score tells us **how well a data point fits into its own cluster** compared to other clusters. Used to judge the quality of a clustering model (works for K-Means, Hierarchical, DBSCAN, etc.)

## a(i) — Mean Intra-Cluster Distance

For a point $i$ belonging to cluster $C_I$:

$$a(i) = \frac{1}{|C_I| - 1} \sum_{j \in C_I,\, i \neq j} d(i,j)$$

- Average distance from point $i$ to **every other point in its own cluster**
- We divide by $|C_I| - 1$ (excludes distance to itself)
- **Smaller a(i) → point fits well in its cluster**

## b(i) — Mean Nearest-Cluster Distance

$$b(i) = \min_{J \neq I} \frac{1}{|C_J|} \sum_{j \in C_J} d(i,j)$$

- For every other cluster, compute the average distance of $i$ to all its points
- Take the **smallest** of those averages
- That closest cluster = the **"neighboring cluster"** of $i$ (next best fit if it weren't in its own cluster)

Ideally we want $a(i) \ll b(i)$ — much closer to own cluster than to the nearest other cluster.

## Silhouette Value s(i)

$$s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}, \quad \text{if } |C_I| > 1$$

$$s(i) = 0, \quad \text{if } |C_I| = 1$$

Equivalent piecewise form:

$$
s(i) =
\begin{cases}
1 - a(i)/b(i), & a(i) < b(i) \\
0, & a(i) = b(i) \\
b(i)/a(i) - 1, & a(i) > b(i)
\end{cases}
$$

## Range & Interpretation

$$-1 \le s(i) \le 1$$

- **Close to +1** → point is well matched to its own cluster, far from neighboring clusters (good clustering)
- **Close to 0** → point lies on/near the boundary between two clusters
- **Close to -1** → point is probably in the wrong cluster (closer to a neighboring cluster than its own)

Averaging $s(i)$ over all points gives the overall **silhouette score** of the clustering model — higher is better.
