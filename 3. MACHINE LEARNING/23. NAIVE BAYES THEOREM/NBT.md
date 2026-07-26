# Naive Bayes Theorem — Simplified Guide

## What is it?

Naive Bayes is a **classification algorithm** based on **Bayes' Theorem**.
It predicts which category (class) something belongs to, using probability.

> "Naive" = it assumes all features are independent of each other (which isn't always true in real life, but it still works surprisingly well).

---

## The Core Formula (Bayes' Theorem)

```
P(A|B) = ( P(B|A) * P(A) ) / P(B)
```

In plain words:

```
P(class | data) = ( P(data | class) * P(class) ) / P(data)
```

| Term | Meaning |
|------|---------|
| P(class \| data) | Probability of a class, given the data (what we want to find) |
| P(data \| class) | Probability of seeing this data if it belongs to that class |
| P(class) | How common that class is overall (prior) |
| P(data) | Probability of the data occurring (normalizing constant) |

---

## How It Works (Step-by-Step)

1. **Learn** from training data — calculate probabilities of each class and each feature within that class.
2. **Assume independence** — treat every feature as unrelated to the others.
3. **Calculate probability** for each possible class using the formula above.
4. **Pick the class** with the highest probability → that's the prediction.

**Example:** Classifying an email as *Spam* or *Not Spam* based on words like "free," "win," "meeting."
- It checks how often these words appear in spam vs. non-spam emails.
- Multiplies the probabilities together.
- Whichever class (spam/not spam) scores higher wins.

---

## Types of Naive Bayes

| Type | Used For | Data Type |
|------|----------|-----------|
| **Gaussian Naive Bayes** | Continuous numeric data (e.g., height, temperature) | Assumes normal (bell curve) distribution |
| **Multinomial Naive Bayes** | Text classification, word counts | Discrete counts (e.g., word frequency) |
| **Bernoulli Naive Bayes** | Binary features (yes/no, present/absent) | 0s and 1s |

---

## Where It's Used

- 📧 **Spam detection** (spam vs. not spam)
- 📰 **Text/News classification** (sports, politics, tech, etc.)
- 😊 **Sentiment analysis** (positive/negative reviews)
- 🩺 **Medical diagnosis** (disease prediction based on symptoms)
- 🎯 **Recommendation systems**

---

## Why It's Popular (Functionality Highlights)

- ✅ **Fast** — simple math, trains and predicts quickly
- ✅ **Works well with small datasets**
- ✅ **Handles high-dimensional data** (like thousands of words in text)
- ✅ **Simple to implement**
- ⚠️ **Limitation:** The "independence" assumption is rarely 100% true, so accuracy can drop when features are strongly related.

---

## One-Line Summary

**Naive Bayes calculates the probability of each class based on given features (assuming they're independent), and picks the class with the highest probability.**