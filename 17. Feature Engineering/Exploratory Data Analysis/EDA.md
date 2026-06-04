## Exploratory Data Analysis (EDA)

### 1. What is EDA?
EDA is the process of analyzing datasets to summarize main characteristics using statistics and visualization.

---

### 2. Objectives
- Understand data structure
- Detect missing values & outliers
- Identify patterns & relationships
- Check assumptions before modeling

---

### 3. Types of EDA

#### a) Univariate Analysis
- Single variable
- Numerical → mean, median, std
- Categorical → frequency count

#### b) Bivariate Analysis
- Relationship between 2 variables
- Examples:
  - Numerical vs Numerical → scatter plot, correlation
  - Categorical vs Numerical → boxplot
  - Categorical vs Categorical → contingency table

#### c) Multivariate Analysis
- More than 2 variables
- Heatmaps, pairplots

---

### 4. Key Steps

#### 1. Data Understanding
- Shape, columns, data types
- `df.info()`, `df.describe()`

#### 2. Missing Values
- Detect → `isnull()`
- Handle:
  - Drop
  - Fill (mean/median/mode)

#### 3. Outlier Detection
- Boxplot, IQR method
- Z-score

#### 4. Data Distribution
- Histogram
- KDE plot
- Skewness

#### 5. Correlation Analysis
- Correlation matrix
- Heatmap

---

### 5. Common Visualizations
- Histogram → distribution
- Boxplot → outliers
- Scatter plot → relationships
- Bar chart → categorical counts
- Heatmap → correlation

---

### 6. Important Concepts
- Skewness:
  - Positive → right tail
  - Negative → left tail
- Correlation:
  - +1 → strong positive
  - -1 → strong negative
- Multicollinearity → high correlation between features

---

### 7. Tools
- Python Libraries:
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn

---

### 8. Quick Workflow
1. Load data
2. Check structure
3. Handle missing values
4. Detect outliers
5. Visualize distributions
6. Analyze relationships
7. Feature insights

---

### 9. Why EDA Matters
- Improves model performance
- Prevents wrong assumptions
- Helps feature selection
