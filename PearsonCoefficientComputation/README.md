# 📊 Manual Pearson Correlation Calculator

This repository contains a Python script to compute **Karl Pearson’s coefficient of correlation** between two sets of student test scores: Physics and History.

The implementation is **fully manual**, relying only on basic Python structures and the standard `math` module — **no external libraries** like `pandas`, `numpy`, or `scipy` were used.  
This approach was chosen to demonstrate how the formula can be constructed and computed step-by-step.

---

## 🧩 Problem Statement

Given the test scores of 10 students in Physics and History, compute **Karl Pearson’s coefficient of correlation** between these scores.

### 🎯 Inputs

Two lists of integers, representing test scores:

```
Physics Scores:  15  12  8   8   7   7   7   6   5   3  
History Scores:  10  25  17  11  13  17  20  13  9   15
```

---

## 📤 Output Format

Print a single floating-point number rounded to **three decimal places**, e.g.:

```
0.145
```

Do **not** include leading or trailing spaces.

---

## 📐 Pearson's Correlation Coefficient

Karl Pearson's correlation coefficient is calculated using the following formula:\
$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$


Where:

- \( r \): Pearson's correlation coefficient  
- \( $x_i$, $y_i$ \): individual values from the datasets  
- \( $\bar{x}$, $\bar{y}$ \): means of the x and y datasets  
- \( n \): number of data points

---

## 💻 Manual Implementation

The script [`ManualPearson.py`](ManualPearson.py):

- Computes sample means manually
- Computes numerator and denominator step-by-step
- Uses only `math.sqrt` for square root calculations

📌 This implementation avoids the use of libraries such as `pandas` or `numpy`, to emphasize manual construction of the correlation logic.

---

## ✅ Result

The correct Pearson correlation coefficient for the given input data is:

```
0.145
```

Rounded to three decimal places, as expected by platforms like HackerRank.

---

## 📂 File Structure

```
├── ManualPearson.py    # Manual calculation script (only uses math)
└── README.md           # Problem description and explanation
```

---

## 🧠 Notes

- This project is ideal for students and beginners seeking to **understand the derivation and calculation of correlation** without relying on high-level libraries.

---
