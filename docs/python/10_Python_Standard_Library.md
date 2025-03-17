# 10 🧰 Python Standard Library  

The Python Standard Library is a collection of built-in modules and functions that provide powerful functionality without needing external dependencies. It includes modules for mathematical operations, file handling, date/time manipulation, data structures, web services, OS interaction, and more.

This chapter explores some of the most useful standard library modules, their features, and how they can simplify Python development.

---

## 10.1 🔢 `math` – Mathematical Operations  

The `math` module provides mathematical functions such as trigonometry, logarithms, and factorials.

### ✅ Common Functions in `math`

```python
import math

print(math.sqrt(25))    # Output: 5.0
print(math.factorial(5))  # Output: 120
print(math.log(100, 10))  # Output: 2.0
print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045
```

✅ Use Case: Calculations in machine learning, data science, and AI models.

---

## 10.2 🎲 `random` – Generating Random Numbers  

The `random` module helps in random sampling, shuffling, and generating random numbers.

### ✅ Generating Random Numbers

```python
import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Random choice
print(random.sample(range(100), 5))  # 5 random numbers from 0-99
```

✅ Use Case: Random sampling, AI model parameter initialization, data augmentation.

---

## 10.3 📆 `datetime` – Working with Dates and Time  

The `datetime` module provides tools for date and time manipulation.

### ✅ Getting Current Date and Time

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2025-03-06 14:30:15
```

### 🔹 Calculating Time Differences

```python
from datetime import timedelta

future_date = now + timedelta(days=7)
print(future_date.strftime("%Y-%m-%d"))  # Output: (7 days ahead)
```

✅ Use Case: Timestamps in logs, scheduling tasks, time-series analysis.

---

## 10.4 📂 `os` – Interacting with the Operating System  

The `os` module helps manage files, directories, and system operations.

### ✅ Common OS Operations

```python
import os

print(os.getcwd())  # Get current working directory
os.mkdir("new_folder")  # Create a new folder
os.rename("old_file.txt", "new_file.txt")  # Rename a file
os.remove("new_file.txt")  # Delete a file
```

✅ Use Case: File automation, script execution, managing system resources.

---

## 10.5 📜 `sys` – System-Specific Functions  

The `sys` module provides functions related to the Python interpreter and command-line arguments.

### ✅ Getting Command-Line Arguments

```python
import sys
print(sys.argv)  # List of command-line arguments
```

### 🔹 Exiting the Program

```python
sys.exit("Terminating program")
```

✅ Use Case: Handling script execution arguments, system interaction.

---

## 10.6 🔍 `re` – Regular Expressions (Pattern Matching)  

The `re` module provides powerful text searching and pattern matching.

### ✅ Searching for Patterns

```python
import re

text = "My email is example@gmail.com"
match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print(match.group())  # Output: example@gmail.com
```

✅ Use Case: Data cleaning, log processing, text extraction in NLP.

---

## 10.7 📡 `urllib` – Fetching Web Data  

The `urllib` module allows sending HTTP requests and fetching web content.

### ✅ Downloading a Webpage

```python
import urllib.request

response = urllib.request.urlopen("https://www.python.org")
html = response.read().decode("utf-8")
print(html[:200])  # Prints first 200 characters of HTML
```

✅ Use Case: Web scraping, downloading datasets, API calls.

---

## 10.8 🗃️ `json` – Handling JSON Data  

The `json` module allows converting Python objects to JSON format and vice versa.

### ✅ Converting Python Dictionary to JSON

```python
import json

data = {"name": "Alice", "age": 25, "city": "New York"}
json_data = json.dumps(data)
print(json_data)  # Output: JSON formatted string
```

### 🔹 Parsing JSON Data

```python
parsed_data = json.loads(json_data)
print(parsed_data["name"])  # Output: Alice
```

✅ Use Case: Handling API responses, saving structured data.

---

## 10.9 🔄 `csv` – Reading and Writing CSV Files  

The `csv` module allows handling comma-separated values (CSV) files, commonly used in data science.

### ✅ Reading a CSV File

```python
import csv

with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

✅ Use Case: Reading structured datasets for ML training.

---

## 10.10 🗂️ `collections` – Advanced Data Structures  

The `collections` module provides specialized data structures like deque, Counter, defaultdict.

### ✅ Counting Elements with Counter

```python
from collections import Counter

data = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(data)
print(counter)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
```

✅ Use Case: Counting words in NLP, tracking data occurrences.

---

## 🚀 Summary of Useful Python Standard Library Modules

| Module | Purpose |
|--------|---------|
| math | Mathematical operations (sqrt, factorial, log, pi) |
| random | Random number generation, shuffling |
| datetime | Date and time handling |
| os | OS file management (create, rename, delete) |
| sys | System operations, command-line arguments |
| re | Regular expressions for pattern matching |
| urllib | Web requests and data fetching |
| json | JSON data encoding/decoding |
| csv | Reading and writing CSV files |
| collections | Advanced data structures (Counter, deque) |

---

## 🔚 Final Thoughts

The Python Standard Library provides powerful tools for data processing, automation, system operations, and web interactions. Mastering these modules helps in building efficient Python programs.

Would you like hands-on exercises on these modules? 🚀
