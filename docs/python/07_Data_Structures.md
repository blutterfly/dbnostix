# 07 🎒 Data Structures  

Data structures are essential for organizing, storing, and managing data efficiently in Python. Python provides built-in data structures such as Lists, Tuples, Dictionaries, and Sets, each suited for different tasks.  

This chapter covers their properties, operations, and use cases in Data Science, Machine Learning, and AI applications.

---

## 07.1 📋 Lists (Ordered, Mutable, Indexed)  

A list is an ordered, mutable (changeable) collection that allows duplicate values. Lists are widely used for storing and manipulating datasets.

### ✅ Creating a List

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [1, "Python", 3.14, True]
```

### 🔹 List Operations

```python
fruits.append("mango")  # Add element
fruits.remove("banana") # Remove element
fruits.insert(1, "grape")  # Insert at index
fruits.pop()  # Remove last item
print(fruits)
```

✅ Use Case: Managing data records, feature lists, training data batches in ML.

### 🔹 List Slicing

```python
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [2, 3, 4]
```

✅ Use Case: Extracting subsets of data in AI and ML models.

---

# 07.2 📌 Tuples (Ordered, Immutable, Indexed)  

A tuple is like a list but immutable (cannot be modified). Tuples are used where data should not change.

### ✅ Creating a Tuple

```python
coordinates = (10.5, 20.3)
colors = ("red", "green", "blue")
```

### 🔹 Tuple Operations

```python
print(coordinates[0])  # Access elements
print(len(colors))     # Tuple length
```

✅ Use Case: Storing constant data like color codes, geographic coordinates.

### 🔹 Tuple Packing & Unpacking

```python
point = (3, 4)
x, y = point  # Unpacking
print(x, y)   # Output: 3 4
```

✅ Use Case: Assigning multiple values in one step in AI and data transformations.

---

# 07.3 🗂️ Dictionaries (Key-Value Pairs, Unordered, Mutable)  

A dictionary (`dict`) stores data in key-value pairs, making it ideal for fast lookups.

### ✅ Creating a Dictionary

```python
student = {"name": "Alice", "age": 21, "grade": "A"}
```

### 🔹 Dictionary Operations

```python
print(student["name"])   # Access value
student["age"] = 22      # Modify value
student["city"] = "NY"   # Add new key-value pair
del student["grade"]     # Remove key-value pair
```

✅ Use Case: Storing JSON-like data, AI model parameters, ML hyperparameters.

### 🔹 Iterating Over a Dictionary

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

✅ Use Case: Extracting metadata from datasets, handling API responses.

---

# 07.4 🔥 Sets (Unordered, Unique Elements, Fast Lookups)  

A set is an unordered collection of unique elements, useful for removing duplicates and fast lookups.

### ✅ Creating a Set

```python
numbers = {1, 2, 3, 4, 4, 2}  # Duplicates removed automatically
```

### 🔹 Set Operations

```python
numbers.add(5)  # Add element
numbers.remove(3)  # Remove element
```

### 🔹 Set Operations for AI & ML

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))    # {1, 2, 3, 4, 5, 6}
print(A.intersection(B))  # {3, 4}
print(A.difference(B))    # {1, 2}
```

✅ Use Case: Removing duplicate values in datasets, comparing feature sets.

---

# 🚀 Summary

| Data Structure | Properties | Use Case |
|----------------|--------------|--------------|
| List  📋 | Ordered, Mutable | Storing datasets, feature lists |
| Tuple 📌 | Ordered, Immutable | Constants, fixed ML configurations |
| Dictionary 🗂️ | Key-Value Pairs, Mutable | Fast lookups, JSON data, ML parameters |
| Set 🔥 | Unordered, Unique Elements | Removing duplicates, comparing data |

---

# 🔚 Final Thoughts

Understanding Lists, Tuples, Dictionaries, and Sets is crucial for data processing, feature engineering, and AI applications.

Would you like real-world coding exercises on these topics? 🚀
