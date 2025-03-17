# 11 🌐 File Handling

File handling is an essential part of programming, allowing reading, writing, and manipulating files. In data science, machine learning, and AI, working with text files, CSV files, and logs is common for storing and processing large datasets.  

This chapter covers file handling operations, including reading, writing, appending, working with different file formats, and error handling.

---

## 11.1 📂 Working with Files in Python  

Python provides built-in functions for opening, reading, writing, and closing files.

### ✅ Opening a File

```python
file = open("example.txt", "r")  # Open a file in read mode
print(file.read())  # Read the entire file content
file.close()  # Always close the file after use
```

✅ Use Case: Reading log files, dataset files, configuration files.

---

## 11.2 📝 Writing to a File  

To write to a file, use write ('w') mode. If the file doesn’t exist, Python creates a new file.

### ✅ Writing Data

```python
file = open("example.txt", "w")  # Open in write mode
file.write("Hello, Python!\nWelcome to File Handling.")
file.close()
```

🔹 Note: `'w'` mode overwrites existing content. To append, use `'a'`.

### ✅ Appending Data to an Existing File

```python
file = open("example.txt", "a")
file.write("\nThis is an additional line.")
file.close()
```

✅ Use Case: Logging data, saving AI/ML model outputs.

---

## 11.3 📖 Reading Files Efficiently  

Python provides different ways to read files efficiently.

### ✅ Reading a File Line by Line

```python
file = open("example.txt", "r")

for line in file:
    print(line.strip())  # Removing extra newlines
file.close()
```

✅ Use Case: Processing large datasets without memory overflow.

### 🔹 Using `readlines()` to Read All Lines as a List

```python
file = open("example.txt", "r")
lines = file.readlines()
print(lines)  # Output: List of lines in the file
file.close()
```

✅ Use Case: Reading structured text data (e.g., logs, reports).

---

## 11.4 🚀 Using `with` Statement for File Handling  

Using `with open()` ensures that the file automatically closes after execution.

### ✅ Safe File Handling with `with`

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

✅ Use Case: Better memory management, avoiding file lock issues.

---

## 11.5 📊 Handling Different File Formats

### 🔹 Working with CSV Files (`csv` Module)

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Output: List of values in each row
```

✅ Use Case: Reading structured datasets in ML models.

### 🔹 Writing to a CSV File

```python
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
```

✅ Use Case: Saving processed data from AI pipelines.

---

### 🔹 Working with JSON Files (`json` Module)

```python
import json

data = {"name": "Alice", "age": 25, "city": "New York"}

# Writing JSON data
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON data
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

✅ Use Case: Handling API responses, configuration files, AI model metadata.

---

## 11.6 🛠️ Error Handling in File Operations

It’s important to handle file-related errors to prevent crashes.

### ✅ Handling File Not Found Error

```python
try:
    with open("non_existent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
```

✅ Use Case: Ensuring robust scripts in production AI pipelines.

---

## 11.7 📂 Working with Directories (`os` Module)

The `os` module allows working with directories and file management.

### ✅ Listing Files in a Directory

```python
import os

print(os.listdir("."))  # Lists all files in the current directory
```

### 🔹 Creating and Deleting Folders

```python
os.mkdir("new_folder")  # Create a folder
os.rmdir("new_folder")  # Remove a folder
```

✅ Use Case: Managing dataset directories in ML projects.

---

## Summary

| Concept | Description | Use Case |
|---------|-------------|----------|
| Reading Files | `open("file.txt", "r")` | Loading datasets, logs |
| Writing Files | `open("file.txt", "w")` | Saving AI model results |
| Appending to Files | `open("file.txt", "a")` | Logging incremental data |
| Using `with` Statement | Ensures safe file handling | Avoids resource leaks |
| CSV Handling | `csv.reader()`, `csv.writer()` | Working with structured data |
| JSON Handling | `json.load()`, `json.dump()` | API responses, metadata storage |
| Error Handling | `try-except` for missing files | Prevents crashes in AI pipelines |
| Directory Management | `os.listdir()`, `os.mkdir()` | Managing datasets and logs |

---

##  Final Thoughts

Mastering file handling and I/O is essential for data processing, logging, and storage in AI, ML, and automation projects.

Would you like real-world coding exercises for practice? 🚀
