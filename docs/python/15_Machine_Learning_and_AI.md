# 15 🧠 Machine Learning and AI   

Machine Learning (ML) and Artificial Intelligence (AI) enable computers to learn from data and make predictions. Python is the leading language for ML & AI due to its rich ecosystem of libraries.  

This chapter covers scikit-learn, TensorFlow, and PyTorch, which are widely used for data preprocessing, building ML models, and deep learning applications.

---

## 15.1 🔍 What is Machine Learning?  

Machine Learning is a subset of AI that focuses on teaching computers to learn from data. It is classified into:  

| Type | Description | Example |
|----------|---------------|-------------|
| Supervised Learning | Uses labeled data | Spam detection, house price prediction |
| Unsupervised Learning | Finds hidden patterns | Clustering customers, anomaly detection |
| Reinforcement Learning | Learns by trial and error | Game AI, robotics |

---

## 15.2 🛠️ Scikit-Learn – Machine Learning for Beginners  

Scikit-learn is a simple and powerful ML library for classification, regression, clustering, and preprocessing.

### ✅ Installing Scikit-Learn

```bash
pip install scikit-learn
```

### 🔹 Loading a Dataset

```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head())
```

✅ Use Case: Loading datasets for training ML models.

### 🔹 Training a Simple Classifier

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

✅ Use Case: Building predictive models for classification problems.

---

## 15.3 🤖 TensorFlow – Deep Learning Framework  

TensorFlow is a powerful framework for building deep learning models.

### ✅ Installing TensorFlow

```bash
pip install tensorflow
```

### 🔹 Creating a Simple Neural Network

```python
import tensorflow as tf
from tensorflow import keras

# Define a simple model
model = keras.Sequential([
    keras.layers.Dense(16, activation='relu', input_shape=(4,)),
    keras.layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=8)
```

✅ Use Case: Training neural networks for AI applications.

---

## 15.4 🔥 PyTorch – Deep Learning for Research & AI  

PyTorch is widely used in AI research and deep learning experiments.

### ✅ Installing PyTorch

```bash
pip install torch torchvision
```

### 🔹 Creating a Simple Neural Network

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define the model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.softmax(self.fc2(x), dim=1)

model = SimpleNN()
```

✅ Use Case: Developing custom AI models for image recognition, NLP, and robotics.

---

## 15.5 📊 Model Evaluation and Metrics  

Measuring model performance is critical in ML & AI.

| Metric | Use Case |
|------------|-------------|
| Accuracy | Classification problems |
| Precision & Recall | Imbalanced datasets (e.g., fraud detection) |
| Mean Squared Error (MSE) | Regression models |
| ROC Curve | Evaluating classification models |

### 🔹 Evaluating a Model

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

✅ Use Case: Assessing model performance before deployment.

---

## 🚀 Summary

| Library | Purpose | Best For |
|------------|------------|-------------|
| Scikit-learn | Traditional ML models | Classification, regression, clustering |
| TensorFlow | Deep learning | Neural networks, AI applications |
| PyTorch | AI research | Custom AI models, NLP, computer vision |

---

## 🔚 Final Thoughts  

Machine Learning and AI enable automation, predictions, and decision-making in various industries.  

Would you like hands-on projects on ML & AI? 🚀
