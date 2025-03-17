# 12 ⚡ Errors and Debugging

Errors are inevitable in programming. Python provides exception handling and debugging tools to ensure programs fail gracefully and help identify issues efficiently. Exception handling improves code reliability, while debugging helps track and fix errors.

This chapter covers handling exceptions with `try-except-finally`, built-in exceptions, raising custom exceptions, logging errors, and debugging techniques.

---

## 12.1 ❌ Understanding Errors in Python  

Python has two main types of errors:  

### 🔹 Syntax Errors (Parsing Errors)

Occurs when Python encounters an incorrectly written statement.

```python
print("Hello"  # Missing closing parenthesis -> SyntaxError
```

✅ Fix: Ensure correct syntax.

---

### 🔹 Runtime Errors (Exceptions)

Occur during execution, such as dividing by zero or accessing an undefined variable.

```python
x = 5 / 0  # ZeroDivisionError
```

Python provides built-in exception types, such as:  

| Exception Type  | Description |
|----------------|----------------|
| `ZeroDivisionError` | Division by zero error |
| `TypeError` | Invalid operation on incompatible data types |
| `ValueError` | Function receives incorrect data type |
| `IndexError` | Accessing an invalid index in a list |
| `KeyError` | Accessing a missing key in a dictionary |
| `FileNotFoundError` | Attempting to open a non-existent file |

---

## 12.2 🛠️ Handling Exceptions with `try-except`  

The `try-except` block catches runtime errors and prevents program crashes.

### ✅ Basic Exception Handling

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

Output:  

```
Cannot divide by zero!
```

✅ Use Case: Handling invalid user inputs, avoiding crashes in AI applications.

---

## 12.3 🔄 Handling Multiple Exceptions  

Multiple exceptions can be handled in a single `try-except` block.

```python
try:
    num = int("Python")  # Causes ValueError
except (ValueError, TypeError):
    print("Invalid input!")
```

✅ Use Case: Handling diverse input errors in data processing pipelines.

---

## 12.4 📌 Using `finally` for Cleanup  

The `finally` block executes whether an exception occurs or not.

```python
try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing the file.")  # Always runs
```

✅ Use Case: Ensuring file/database connections are properly closed.

---

## 12.5 🚀 Raising Custom Exceptions (`raise`)  

Use `raise` to define custom exceptions for better debugging.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

print(check_age(15))  # Raises ValueError
```

✅ Use Case: Enforcing validation rules in APIs and ML models.

---

## 12.6 📝 Logging Errors (`logging` Module)

Instead of printing errors, use logging to track them efficiently.

```python
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)

try:
    result = 5 / 0
except ZeroDivisionError as e:
    logging.error(f"Error occurred: {e}")
```

✅ Use Case: Tracking issues in AI applications, logging errors in production.

---

## 12.7 🐛 Debugging Techniques  

Debugging helps find and fix issues before deployment.

### 🔹 Using `print()` for Debugging

```python
def add(a, b):
    print(f"Adding {a} and {b}")  # Debugging output
    return a + b

print(add(5, 3))
```

✅ Use Case: Checking function execution and variable values.

---

### 🔹 Using `assert` for Testing

`assert` helps validate assumptions in the code.

```python
def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

print(divide(10, 2))  # Runs fine
print(divide(10, 0))  # Raises AssertionError
```

✅ Use Case: Preventing invalid inputs in ML models.

---

### 🔹 Debugging with `pdb` (Python Debugger)

`pdb` allows step-by-step execution.

```python
import pdb

def multiply(x, y):
    pdb.set_trace()  # Debugging breakpoint
    return x * y

print(multiply(3, 4))
```

✅ Use Case: Investigating code behavior interactively.

---

## 12.8 🛠️ Best Practices for Exception Handling & Debugging

✅ DO:

- Use specific exceptions (`ZeroDivisionError`, `FileNotFoundError`)
- Use logging instead of `print()`
- Use `finally` for resource cleanup
- Use assertions for quick debugging

❌ AVOID:

- Using `except:` without specifying the exception
- Silencing exceptions (`pass` inside `except`)
- Overusing `try-except` in simple operations

---

## 🚀 Summary

| Concept | Description | Use Case |
|---------|-------------|----------|
| try-except | Catches runtime errors | Handling invalid inputs |
| Multiple Exceptions | Catches different errors | Complex workflows |
| finally | Executes cleanup code | Closing files/databases |
| raise | Throws custom exceptions | Enforcing validation |
| logging | Saves errors to a log file | Debugging production apps |
| assert | Ensures correct values | Quick testing |
| pdb | Interactive debugging | Step-by-step execution |

---

## 🔚 Final Thoughts

Mastering exception handling and debugging is essential for writing robust, error-free Python applications.

Would you like hands-on debugging exercises? 🚀
