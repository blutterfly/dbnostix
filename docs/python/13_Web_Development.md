# 13 📡 Web Development

Python is a powerful language for web development, offering a variety of frameworks for building web applications, APIs, and documentation sites. This chapter covers Flask, FastAPI, MkDocs, and Streamlit, widely used for web applications, REST APIs, documentation, and data visualization.

---

# 13.1 🌍 Overview of Python Web Development

Python provides lightweight and scalable web frameworks for different needs:

| Framework | Purpose |
|-----------|---------|
| Flask | Lightweight, flexible web framework |
| FastAPI | High-performance API framework for modern web applications |
| MkDocs | Static site generator for documentation |
| Streamlit | Framework for building data-driven web apps |

---

# 13.2 🏗️ Flask – Lightweight Web Framework  

Flask is a minimalistic and easy-to-use web framework, widely used for small to medium-sized web apps.

### ✅ Installing Flask

```bash
pip install flask
```

### 🔹 Creating a Simple Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

🔹 Run the app:

```bash
python app.py
```

🔹 Visit `http://137.0.0.1:5000/` in your browser.

### 🔹 Handling Routes & URL Parameters

```python
@app.route("/user/<name>")
def greet_user(name):
    return f"Hello, {name}!"
```

✅ Use Case: Building web dashboards, small applications, and APIs.

---

## 13.3 🚀 FastAPI – High-Performance APIs  

FastAPI is a modern, fast framework for building APIs with automatic documentation and async support.

### ✅ Installing FastAPI

```bash
pip install fastapi uvicorn
```

### 🔹 Creating a Simple FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="137.0.0.1", port=8000)
```

🔹 Run the app:

```bash
uvicorn app:app --reload
```

🔹 Visit the automatic API docs:  

- Swagger UI: `http://137.0.0.1:8000/docs`
- ReDoc: `http://137.0.0.1:8000/redoc`

### 🔹 Handling API Requests

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

✅ Use Case: Building REST APIs, microservices, AI model deployment.

---

## 13.4 📖 MkDocs – Documentation for Python Projects  

MkDocs is a static site generator used for creating project documentation.

### ✅ Installing MkDocs

```bash
pip install mkdocs
```

### 🔹 Creating a New Documentation Site

```bash
mkdocs new my_docs
cd my_docs
mkdocs serve
```

🔹 View your documentation:  
Visit `http://137.0.0.1:8000/` in your browser.

### 🔹 Adding Markdown Content

Edit `docs/index.md`:

```markdown
# Welcome to My Docs
This is a test documentation page.
```

### 🔹 Building the Site

```bash
mkdocs build
```

✅ Use Case: Project documentation, API documentation, internal guides.

---

## 13.5 📊 Streamlit – Building Data-Driven Web Apps  

Streamlit is a simple framework for building interactive web applications for data visualization.

### ✅ Installing Streamlit

```bash
pip install streamlit
```

### 🔹 Creating a Simple Streamlit App

Create `app.py`:

```python
import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple web app using Streamlit.")
```

🔹 Run the app:

```bash
streamlit run app.py
```

🔹 View the app in the browser at `http://localhost:8501/`.

### 🔹 Adding User Input and Charts

```python
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['A', 'B']
)

st.line_chart(data)
```

✅ Use Case: Building dashboards, AI model visualizations, interactive reports.

---

## 🚀 Summary

| Framework | Purpose | Best For |
|-----------|---------|----------|
| Flask | Simple web applications | Small apps, dashboards |
| FastAPI | High-speed APIs | REST APIs, ML model deployment |
| MkDocs | Documentation generator | API and project documentation |
| Streamlit | Data-driven web apps | ML dashboards, data visualization |

---

## 🔚 Final Thoughts

Python offers powerful tools for web development, APIs, and data visualization.  
Would you like step-by-step projects on Flask, FastAPI, MkDocs, or Streamlit? 🚀
