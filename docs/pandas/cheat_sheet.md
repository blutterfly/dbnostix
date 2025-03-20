# Cheatsheet

# Selecting and Filtering Data

Selecting and filtering data are fundamental operations when working with Pandas DataFrames. Pandas provides multiple methods for selecting specific rows and columns based on labels, positions, and conditions.

---

## 1. Selecting Data

### 1.1 Selecting Columns

- Using column names:

```python
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
})

# Select a single column
print(df["Name"])

# Select multiple columns
print(df[["Name", "City"]])
```

### 1.2 Selecting Rows

- Using `.loc[]` (label-based indexing):

```python
# Select a row by index label
print(df.loc[0])  # First row
```

- Using `.iloc[]` (position-based indexing):

```python
# Select a row by position
print(df.iloc[2])  # Third row
```

- Selecting multiple rows:

```python
print(df.loc[0:2])  # Select rows 0 to 2
print(df.iloc[0:2])  # Select first two rows
```

---

## 2. Filtering Data

Filtering is used to extract subsets of a DataFrame that meet specific conditions.

### 2.1 Filtering Rows Based on Condition

```python
# Select rows where Age > 30
print(df[df["Age"] > 30])
```

### 2.2 Filtering with Multiple Conditions

Using `&` (AND condition):

```python
# Select rows where Age > 30 and City is "Chicago"
print(df[(df["Age"] > 30) & (df["City"] == "Chicago")])
```

Using `|` (OR condition):

```python
# Select rows where Age < 30 or City is "Houston"
print(df[(df["Age"] < 30) | (df["City"] == "Houston")])
```

Using `.isin()` for filtering specific values:

```python
# Select rows where City is in ["New York", "Houston"]
print(df[df["City"].isin(["New York", "Houston"])])
```

Using `.between()` for range-based filtering:

```python
# Select rows where Age is between 25 and 35
print(df[df["Age"].between(25, 35)])
```

Using `.query()` for SQL-like filtering:

```python
print(df.query("Age > 30 and City == 'Chicago'"))
```

---

## 3. Selecting Specific Rows and Columns

```python
# Select specific rows and columns
print(df.loc[df["Age"] > 30, ["Name", "City"]])
```

```python
# Select first two rows and first two columns
print(df.iloc[0:2, 0:2])
```

---

## Mini Tutorial: Filtering a Real Dataset

Let's assume we have a dataset `data.csv` with employee information:

### Step 1: Load the Dataset

```python
df = pd.read_csv("data.csv")
```

### Step 2: Explore the Data

```python
print(df.head())  # View the first few rows
print(df.info())  # Get summary information
```

### Step 3: Apply Filtering

```python
# Employees older than 40
older_employees = df[df["Age"] > 40]

# Employees in the IT department
it_employees = df[df["Department"] == "IT"]

# Employees with salary between 50K and 100K
mid_salary_employees = df[df["Salary"].between(50000, 100000)]

# IT employees in New York
ny_it_employees = df[(df["Department"] == "IT") & (df["City"] == "New York")]
```

### Step 4: Save the Filtered Data

```python
ny_it_employees.to_csv("filtered_data.csv", index=False)
```

---

## Conclusion

- Use `.loc[]` and `.iloc[]` for row and column selection.
- Use conditional filtering with boolean operators (`&`, `|`).
- Use `.query()` for SQL-like filtering.
- Use `.isin()` and `.between()` for specialized filtering.

Would you like an example using PandasGUI for interactive filtering? 🚀
