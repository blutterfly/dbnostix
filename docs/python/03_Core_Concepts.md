# 03 ⚙️ Core Concepts

## Basic  

### 1. Variables & Data Types  

Python supports multiple data types:

```python
x = 10         # Integer
y = 3.14       # Float
z = "Python"   # String
a = True       # Boolean
b = [1, 2, 3]  # List
c = (4, 5, 6)  # Tuple
d = {"key": "value"}  # Dictionary
```

### 2. Conditional Statements  

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

### 3. Loops (For & While)  

```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### 4. Functions  

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Ted"))  # Output: Hello, Ted!
```

### 5. Object-Oriented Programming (OOP)  

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Car: {self.brand} {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.display())  # Output: Car: Toyota Corolla
```

### 6. Exception Handling  

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")
```

### 7. File Handling  

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### 8. Modules & Libraries  

```python
import math
print(math.factorial(5))  # Output: 120
```

---


Mastering these core Python concepts enables Data Scientists, Machine Learning Engineers, and AI developers to build efficient, scalable, and high-performance solutions. 🚀

Later,  code challenges or exercises to reinforce these topics will be covered. 🤔
