# DuckDb Intro

Here’s a summarized breakdown of the key takeaways from the article **“Introducing DuckDB and Python”** along with relevant code blocks:

---

## 🔑 Key Takeaways

### ✅ What is DuckDB?

* An **in-process analytical SQL database** optimized for OLAP.
* Requires **no server**, **no setup**, and **works inside Python scripts**.
* Excellent for large datasets (CSV, Parquet, JSON) and memory-efficient querying.

---

### ✅ Benefits Over pandas

* Handles **large files** without loading into memory.
* Enables **SQL queries** on local files and `pandas` DataFrames.
* Supports **efficient filtering**, **joins**, and **write operations** directly to disk.

---

### ✅ Installation

```bash
pip install duckdb
```

---

## 💡 Example Usage Patterns

### 📌 Query a CSV File Directly

```python
import duckdb

result = duckdb.query("SELECT * FROM 'users.csv' LIMIT 5").to_df()
print(result)
```

---

### 📌 Join Across Multiple Files

```python
query = """
SELECT u.id, u.name, o.total
FROM 'users.csv' u
JOIN 'orders.csv' o ON u.id = o.user_id
WHERE o.total > 100
"""
df = duckdb.query(query).to_df()
```

---

### 📌 Query a pandas DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
})

result = duckdb.query("SELECT name FROM df WHERE score > 80").to_df()
print(result)
```

---

### 📌 Query a Parquet File (with filter)

```python
df = duckdb.query("SELECT * FROM 'data/2023_logs.parquet' WHERE status = 'error'").to_df()
```

---

### 📌 Create a SQL View Over File Paths

```python
duckdb.query("CREATE VIEW logs AS SELECT * FROM 'data/*.parquet'")
```

---

### 📌 Write Query Results to Disk

```python
duckdb.query("""
COPY (SELECT * FROM 'users.csv' WHERE country = 'US')
TO 'us_users.csv'
""")
```

---

### 📌 SQL-Based Pipeline in Python

```python
duckdb.query("CREATE TEMP TABLE sales AS SELECT * FROM 'sales_2024.csv'")

duckdb.query("""
CREATE TEMP TABLE filtered AS
SELECT * FROM sales WHERE amount > 1000
""")

result = duckdb.query("SELECT region, COUNT(*) FROM filtered GROUP BY region").to_df()
```

---

### 📌 Parameterized Queries

```python
region = 'West'
result = duckdb.query("SELECT * FROM 'sales.csv' WHERE region = ?", [region]).to_df()
```

---

## 🚫 When *Not* to Use DuckDB

* For **transactional workloads**, **multi-user access**, or **relational constraints**.
* Stick with PostgreSQL or MySQL for persistent, transactional applications.

---

Would you like a comparison cheat sheet between DuckDB, pandas, and SQLite for specific tasks?
