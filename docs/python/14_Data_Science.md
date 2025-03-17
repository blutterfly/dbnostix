# 14 📊 Data Science

Data Science involves analyzing, processing, and visualizing data to derive insights. Python is widely used in Data Science due to its rich ecosystem of libraries. This chapter covers NumPy, Pandas, and Matplotlib, the three core libraries for data manipulation, analysis, and visualization.

---

## 14.1 🔢 NumPy – Numerical Computing  

NumPy (Numerical Python) provides fast, efficient array operations and is the foundation for scientific computing in Python.

### ✅ Installing NumPy

```bash
pip install numpy
```

### 🔹 Creating NumPy Arrays

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]
```

### 🔹 NumPy Array Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Output: [5 7 9]
print(a * b)  # Output: [4 10 18]
print(np.dot(a, b))  # Dot product: 1*4 + 2*5 + 3*6 = 32
```

### 🔹 Generating Random Data

```python
random_numbers = np.random.rand(5)  # 5 random numbers
print(random_numbers)
```

✅ Use Case: Data preprocessing, handling large numerical datasets efficiently.

---

## 14.2 🗃️ Pandas – Data Manipulation  

Pandas simplifies working with structured data (tables, CSVs, JSONs, databases).

### ✅ Installing Pandas

```bash
pip install pandas
```

### 🔹 Creating a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)
```

### 🔹 Reading Data from CSV

```python
df = pd.read_csv("data.csv")
print(df.head())  # Display first 5 rows
```

### 🔹 Filtering Data

```python
young_employees = df[df["Age"] < 30]
print(young_employees)
```

### 🔹 Adding a New Column

```python
df["Bonus"] = df["Salary"] * 0.10  # 10% bonus
print(df)
```

✅ Use Case: Handling datasets, cleaning and preparing data for ML models.

---

## 14.3 📊 Matplotlib – Data Visualization  

Matplotlib is the primary library for plotting graphs and visualizing data.

### ✅ Installing Matplotlib

```bash
pip install matplotlib
```

### 🔹 Plotting a Line Graph

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

plt.plot(x, y, marker="o", linestyle="-")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()
```

### 🔹 Creating a Bar Chart

```python
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(categories, values, color="blue")
plt.title("Bar Chart Example")
plt.show()
```

### 🔹 Creating a Histogram

```python
data = np.random.randn(1000)

plt.hist(data, bins=30, color="green")
plt.title("Histogram of Random Data")
plt.show()
```

✅ Use Case: Exploratory Data Analysis (EDA), understanding dataset distributions.

---

## 🚀 Summary

| Library | Purpose | Best For |
|---------|---------|----------|
| NumPy | Fast numerical computing | Arrays, linear algebra, statistics |
| Pandas | Data manipulation | CSVs, databases, data wrangling |
| Matplotlib | Data visualization | Graphs, charts, and plots |

---

## 🔚 Final Thoughts

Mastering NumPy, Pandas, and Matplotlib is essential for data science, machine learning, and AI applications.  
Would you like practical projects to apply these concepts? 🚀
