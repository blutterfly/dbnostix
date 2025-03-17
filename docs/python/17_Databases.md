# 17 🏛️ Databases

Databases are essential for storing, managing, and retrieving structured data. Python provides built-in and third-party libraries for working with SQL and NoSQL databases.

This chapter covers SQLite, PostgreSQL, MySQL, and MongoDB, along with how to perform CRUD operations (Create, Read, Update, Delete).

---

## 17.1 🗂️ Types of Databases  

| Database Type | Example | Best For |
|------------------|------------|--------------|
| Relational (SQL) | SQLite, MySQL, PostgreSQL | Structured data with relationships |
| NoSQL (Document-based) | MongoDB, Firebase | Unstructured or semi-structured data |

---

## 17.2 🏗️ Working with SQLite (Lightweight SQL Database)  

SQLite is a lightweight, file-based SQL database that comes pre-installed with Python.

### ✅ Connecting to SQLite

```python
import sqlite3

conn = sqlite3.connect("database.db")  # Creates/opens a database file
cursor = conn.cursor()
```

### 🔹 Creating a Table

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()
```

### 🔹 Inserting Data

```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()
```

### 🔹 Reading Data

```python
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Output: [(1, 'Alice', 25)]
```

✅ Use Case: Small applications, local storage, prototyping.

---

## 17.3 🏦 Working with PostgreSQL & MySQL (SQL Databases for Large Applications)  

### ✅ Installing PostgreSQL/MySQL Connector

```bash
pip install psycopg2  # PostgreSQL
pip install mysql-connector-python  # MySQL
```

### 🔹 Connecting to PostgreSQL

```python
import psycopg2

conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="mypassword",
    host="localhost"
)
cursor = conn.cursor()
```

### 🔹 Querying a PostgreSQL Table

```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

✅ Use Case: Enterprise applications, web applications, analytics.

---

## 17.4 🍃 Working with MongoDB (NoSQL Database)  

MongoDB stores data in JSON-like documents.

### ✅ Installing MongoDB Driver

```bash
pip install pymongo
```

### 🔹 Connecting to MongoDB

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]
```

### 🔹 Inserting a Document

```python
user = {"name": "Alice", "age": 25}
collection.insert_one(user)
```

### 🔹 Retrieving Data

```python
for user in collection.find():
    print(user)
```

✅ Use Case: Big data, real-time analytics, IoT applications.

---

## 17.5 🔄 CRUD Operations in Databases  

| Operation | SQL Example | MongoDB Example |
|--------------|----------------|---------------------|
| Create | `INSERT INTO users VALUES (1, 'Alice', 25);` | `collection.insert_one({"name": "Alice", "age": 25})` |
| Read | `SELECT * FROM users;` | `collection.find({})` |
| Update | `UPDATE users SET age=30 WHERE name='Alice';` | `collection.update_one({"name": "Alice"}, {"$set": {"age": 30}})` |
| Delete | `DELETE FROM users WHERE name='Alice';` | `collection.delete_one({"name": "Alice"})` |

✅ Use Case: Building full-stack web applications, managing structured/unstructured data.

---

## 🚀 Summary

| Database | Best For |
|-------------|-------------|
| SQLite | Small applications, local storage |
| PostgreSQL/MySQL | Large-scale, structured data |
| MongoDB | Flexible, unstructured data |

---

## 🔚 Final Thoughts

Databases are essential for storing and managing data in Python applications.  
Would you like a real-world project on integrating databases with Python? 🚀
