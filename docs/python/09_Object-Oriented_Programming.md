# 09 🏗️ Object-Oriented

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into reusable objects. It is widely used in data science, machine learning, and AI to manage models, datasets, and complex systems efficiently.

This chapter covers classes, objects, inheritance, polymorphism, encapsulation, and abstraction to help structure Python programs for scalability and maintainability.

---

## 09.1 🏗️ What is OOP?  

OOP is based on the concept of objects that contain data (attributes) and functions (methods). This approach makes programs modular, reusable, and easy to maintain.

### 🔹 Key OOP Concepts

| Concept | Description |
|---------|------------|
| Class | A blueprint for creating objects |
| Object | An instance of a class |
| Encapsulation | Hiding internal details of an object |
| Inheritance | A child class inherits attributes and methods from a parent class |
| Polymorphism | Different classes can have methods with the same name but different behaviors |
| Abstraction | Hiding unnecessary implementation details |

---

## 09.2 📦 Creating Classes and Objects  

A class is a blueprint for creating objects.

### ✅ Defining a Class and Creating an Object

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def display_info(self):  # Method
        return f"{self.brand} {self.model}"

# Creating an object
car1 = Car("Toyota", "Corolla")
print(car1.display_info())  # Output: Toyota Corolla
```

✅ Use Case: Creating machine learning models, database records, or simulation objects.

---

## 09.3 🔐 Encapsulation (Data Protection)

Encapsulation restricts direct access to object attributes, ensuring data integrity.

### ✅ Private Variables in a Class

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```

✅ Use Case: Protecting sensitive data like user credentials, financial data.

---

## 09.4 🔄 Inheritance (Code Reusability)

Inheritance allows a child class to use the properties and methods of a parent class, reducing redundant code.

### ✅ Single Inheritance

```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Usage
dog = Dog()
print(dog.make_sound())  # Output: Bark
```

✅ Use Case: Extending functionality of ML models, custom layers in deep learning.

### 🔹 Multiple Inheritance

```python
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):  # Inheriting from A and B
    pass

obj = C()
print(obj.method_a())  # Output: Method A
print(obj.method_b())  # Output: Method B
```

✅ Use Case: Combining functionalities from different modules (e.g., ML models + preprocessing steps).

---

## 09.5 🔄 Polymorphism (Multiple Forms)

Polymorphism allows different classes to use the same method name but behave differently.

### ✅ Method Overriding

```python
class Shape:
    def area(self):
        return "Area method not implemented"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius  2  # Overriding method

# Usage
circle = Circle(5)
print(circle.area())  # Output: 78.5
```

✅ Use Case: Implementing AI models with different training methods.

---

## 09.6 🎭 Abstraction (Hiding Implementation Details)

Abstraction hides complex logic and exposes only relevant details.

### ✅ Using the `ABC` Module for Abstraction

```python
from abc import ABC, abstractmethod

class Payment(ABC):  # Abstract Class
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

# Usage
payment = CreditCardPayment()
print(payment.process_payment(100))  # Output: Processing credit card payment of $100
```

✅ Use Case: Defining AI model architecture, creating frameworks for ML algorithms.

---

## 09.7 🛠️ OOP in Real-World AI and ML

### ✅ OOP for Machine Learning Models

```python
class MLModel:
    def train(self, data):
        return "Training the model on data"

class NeuralNetwork(MLModel):
    def train(self, data):
        return "Training deep learning model"

model1 = MLModel()
model2 = NeuralNetwork()

print(model1.train("Dataset"))  # Output: Training the model on data
print(model2.train("Dataset"))  # Output: Training deep learning model
```

✅ Use Case: Modularizing ML models and creating reusable AI components.

---

## 🚀 Summary

| OOP Concept | Description | Use Case |
|-------------|------------|----------|
| Class & Object | Blueprint and instance of an object | AI models, Data structures |
| Encapsulation | Restricting direct access to attributes | Secure financial transactions |
| Inheritance | Child class inherits from parent class | Model pipelines, feature engineering |
| Polymorphism | Same method, different behavior | Different AI models processing inputs |
| Abstraction | Hiding unnecessary details | AI frameworks, APIs |

---

# 🔚 Final Thoughts

Object-Oriented Programming enhances modularity and reusability, making it ideal for building scalable ML models, AI systems, and large applications.

Would you like real-world coding challenges for hands-on practice? 🚀
