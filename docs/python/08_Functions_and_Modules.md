# 08 🎭 Functions and Modules

Functions and modules are essential building blocks in Python, promoting code reuse, modularity, and maintainability. Understanding them is crucial for data science, machine learning, and AI, where reusable code improves efficiency and readability.  

This chapter covers defining functions, argument handling, lambda functions, recursion, and working with modules to write efficient, modular, and scalable Python code.

---

## 08.1 🎯 Functions: The Building Blocks of Python  

A function is a reusable block of code that performs a specific task.

### ✅ Defining a Function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

✅ Use Case: Encapsulating repetitive code, making programs more readable.

---

## 08.2 🎭 Function Arguments and Parameters  

Functions in Python support different types of arguments:

### 🔹 Positional Arguments

```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

### 🔹 Default Arguments

```python
def power(base, exponent=2):
    return base  exponent

print(power(3))     # Output: 9 (3²)
print(power(3, 3))  # Output: 27 (3³)
```

### 🔹 Keyword Arguments

```python
print(power(exponent=3, base=2))  # Output: 8
```

### 🔹 Variable-Length Arguments (\*args, \*\*kwargs)

```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # Output: 10

def display_info(info):
    print(info)

display_info(name="Alice", age=25)
```

✅ Use Case: Handling dynamic data inputs in ML models, APIs, and automation scripts.

---

## 08.3 ⚡ Lambda (Anonymous) Functions  

Lambda functions are short, one-line functions often used in data processing.

### ✅ Lambda Syntax

```python
square = lambda x: x  2
print(square(5))  # Output: 25
```

### 🔹 Lambda with map(), filter(), reduce()

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

✅ Use Case: Data transformations in pandas, NumPy, and machine learning preprocessing.

---

## 08.4 🔁 Recursion: Functions Calling Themselves  

Recursion is used when a problem can be broken down into smaller subproblems.

### ✅ Factorial Calculation

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

✅ Use Case: Tree-based algorithms, graph traversal (DFS), Fibonacci sequence.

---

## 08.5 📦 Python Modules (Importing and Organizing Code)

Modules allow code organization by grouping related functions and variables.

### ✅ Importing a Module

```python
import math
print(math.sqrt(25))  # Output: 5.0
```

### 🔹 Importing Specific Functions

```python
from math import sqrt
print(sqrt(16))  # Output: 4.0
```

### 🔹 Creating a Custom Module

📌 Create a file `mymodule.py`  

```python
def greet(name):
    return f"Hello, {name}!"
```

📌 Import and Use the Module

```python
import mymodule
print(mymodule.greet("Alice"))
```

✅ Use Case: Reusing functions in large AI projects, ML models, and APIs.

---

## 08.6 📂 Working with Built-in and Third-Party Modules  

### 🔹 Useful Built-in Modules

| Module | Purpose |
|--------|---------|
| `math` | Mathematical functions |
| `random` | Random number generation |
| `datetime` | Date and time operations |
| `os` | File and system operations |
| `sys` | System-related functions |
| `re` | Regular expressions |

### 🔹 Installing & Using Third-Party Modules

```bash
pip install numpy pandas
```

```python
import numpy as np
import pandas as pd
```

✅ Use Case: Data science, AI model training, automation.

