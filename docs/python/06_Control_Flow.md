# 06 🔄 Control Flow

Control flow determines the execution order of statements in a Python program. It includes conditional statements, loops, and exception handling, allowing programs to make decisions and repeat actions efficiently.

---

## 🔹 4.1 Conditional Statements (if, elif, else)  

Conditional statements allow Python to execute different blocks of code based on conditions.

### ✅ Basic if-else Statement

```python
x = 10

if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
```

Output: `Positive number`

### 🔹 Nested if Statements

```python
age = 20

if age > 18:
    if age >= 21:
        print("Eligible for full privileges")
    else:
        print("Limited privileges")
else:
    print("Not eligible")
```

✅ Use Case: Decision trees in ML models, data validation, user authentication.

---

## 🔹 4.2 Looping in Python  

Loops allow repeating actions based on conditions.

### 🔹 for Loop (Iterating over Sequences)

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

Output:

```
1
2
3
4
5
```

✅ Use Case: Iterating over lists, tuples, dictionaries, and strings in data processing, ML datasets.

### 🔹 for Loop with range()

```python
for i in range(1, 6):
    print(i)
```

Output:  

```
1
2
3
4
5
```

✅ Use Case: Creating training epochs in machine learning models.

---

### 🔹 while Loop (Repeat Until Condition Fails)

```python
count = 0

while count < 5:
    print("Count:", count)
    count += 1
```

Output:  

```
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
```

✅ Use Case: Keeping a server running, waiting for a user input, or training an ML model until convergence.

---

## 🔹 4.3 Loop Control Statements

Python provides ways to modify loop behavior using `break`, `continue`, and `pass`.

### 🔹 break (Exit Loop Early)

```python
for num in range(10):
    if num == 5:
        break  # Stops at 5
    print(num)
```

Output:  

```
0
1
2
3
4
```

✅ Use Case: Stopping an AI model early if a condition is met.

---

### 🔹 continue (Skip Iteration)

```python
for num in range(5):
    if num == 2:
        continue  # Skips 2
    print(num)
```

Output:  

```
0
1
3
4
```

✅ Use Case: Skipping invalid data points in datasets.

---

### 🔹 pass (Do Nothing)

```python
for i in range(5):
    if i == 3:
        pass  # Placeholder
    print(i)
```

✅ Use Case: Placeholder for functions, classes, loops.

---

## 🔹 4.4 List Comprehensions for Loops

Python supports one-liner loops with list comprehensions, improving efficiency.

```python
numbers = [x * 2 for x in range(5)]
print(numbers)
```

Output: `[0, 2, 4, 6, 8]`

✅ Use Case: Feature engineering, transforming datasets, list filtering.

---

## 🔹 4.5 Exception Handling (try-except-finally)

Handling exceptions prevents crashes in programs.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete.")
```

Output:  

```
Cannot divide by zero!
Execution complete.
```

✅ Use Case: Preventing failures in data pipelines, ML model training.

---

# 🚀 Summary

| Concept | Key Takeaway |
|---------|-------------|
| if-elif-else | Executes different blocks based on conditions |
| for loop | Iterates over sequences (lists, tuples, etc.) |
| while loop | Runs while condition is `True` |
| break | Exits loop early |
| continue | Skips current iteration |
| pass | Placeholder statement |
| List Comprehensions | Shorter syntax for loops |
| Exception Handling | Prevents program crashes |

---

# 🔚 Final Thoughts

Control flow is crucial for decision-making and iteration in Python. Mastering it allows writing efficient, error-free code.

Would you like exercises or real-world examples to reinforce these topics? 🚀
