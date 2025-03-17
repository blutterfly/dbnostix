# 05 📝 Syntax and Variables

Python's simple and readable syntax makes it a favorite among beginners and experts alike. Understanding its basic syntax and variable handling is essential for writing clean and efficient code.

---

## 🔹 3.1 Python Syntax Basics

Python follows an indentation-based syntax rather than using `{}` like C or Java. This makes the code cleaner and more readable.

### ✅ Example: Python Syntax

```python
# Correct indentation
if True:
    print("Hello, Python!")  # Indented block
```

```python
# ❌ Incorrect indentation (will raise an error)
if True:
print("Hello, Python!")  # IndentationError
```

### 🛠 Key Features of Python Syntax

- No curly braces `{}` for blocks—indentation matters!
- No need for semicolons `;` at the end of statements.
- Uses `#` for single-line comments and `""" """` for multi-line comments.

---

## 🔹 3.2 Variables in Python

Variables in Python store data and do not require explicit type declaration. Python is dynamically typed, meaning the data type is determined at runtime.

### ✅ Declaring Variables

```python
name = "Alice"       # String
age = 25            # Integer
height = 5.9        # Float
is_student = True   # Boolean
```

### 🔹 Rules for Variable Naming

✅ Allowed:

- Can start with a letter or underscore `_`
- Can contain letters, numbers, and underscores
- Case-sensitive (`Age` and `age` are different)

❌ Not Allowed:

- Cannot start with a number (`2name ❌`)
- Cannot use special characters (`@name ❌`)

### 🔹 Multiple Variable Assignment

```python
a, b, c = 1, 2, "Python"
print(a, b, c)  # Output: 1 2 Python
```

✅ Use Case: Quick assignment of multiple values.

---

## 🔹 3.3 Data Types in Python

Python provides built-in data types for handling different kinds of values.

| Type   | Example  | Description  |
|-----------|-------------|-----------------|
| `int`     | `x = 10`     | Whole numbers |
| `float`   | `y = 3.14`   | Decimal numbers |
| `str`     | `s = "Python"` | Text/String |
| `bool`    | `b = True`  | Boolean (True/False) |
| `list`    | `l = [1,2,3]` | Ordered, mutable collection |
| `tuple`   | `t = (1,2,3)` | Ordered, immutable collection |
| `dict`    | `d = {"key": "value"}` | Key-value pairs |
| `set`     | `s = {1,2,3}` | Unordered unique elements |

✅ Use Case: Storing structured data, lists, and key-value mappings.

---

## 🔹 3.4 Type Conversion

Python allows explicit type conversion (casting) when needed.

```python
x = 5          # Integer
y = str(x)     # Convert to string
z = float(x)   # Convert to float
print(y, z)    # Output: '5' 5.0
```

✅ Use Case: Ensuring correct data formats in ML/DL models and databases.

---

## 🔹 3.5 String Manipulation

Python strings (`str`) support multiple operations.

```python
name = "Python"
print(name.upper())   # PYTHON
print(name.lower())   # python
print(name[0:3])      # Pyt (Slicing)
```

✅ Use Case: Data cleaning in text processing and NLP.

---

## 🔹 3.6 User Input

Python allows reading user input using `input()`.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

✅ Use Case: Interactive Python applications and CLI tools.

---

## 🔹 3.7 Constants in Python

Python doesn’t have built-in constants, but by convention, uppercase names are used.

```python
PI = 3.1416  # Treated as a constant
```

✅ Use Case: Defining scientific constants.

---

## 🔹 3.8 f-Strings for String Formatting

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

✅ Use Case: Readable string interpolation.

---

## 🚀 Summary

| Concept | Key Takeaway |
|---------|-------------|
| Python Syntax | Uses indentation instead of `{}` |
| Variables | Dynamically typed, no explicit declaration needed |
| Data Types | Includes `int`, `float`, `str`, `bool`, `list`, `dict`, etc. |
| Type Conversion | Use `str()`, `int()`, `float()` for casting |
| String Manipulation | Supports `.upper()`, `.lower()`, slicing, and f-strings |
| User Input | `input()` for user interaction |
| Constants | Uppercase variable names conventionally used |

---

# 🔚 Final Thoughts

Understanding basic syntax and variables is the foundation for mastering Python. Once comfortable with these, you can move on to data structures, control flow, and advanced programming concepts.

Would you like exercises or quizzes to reinforce learning? 🚀
