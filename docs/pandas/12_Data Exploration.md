Must-Know Python Pandas
Functions for Effortless Data
Exploration
Gen. David L. · Follow
5 min read · Nov 27, 2024
19
Open in app
Search Write
The key point of data analysis lies in uncovering the stories behind the data.
To achieve this, it’s essential to build a solid foundation by thoroughly
exploring and understanding the data. In this process, Python’s Pandas
library plays a crucial role. Pandas not only offers a powerful set of features
but also provides high flexibility, making data exploration both easy and
efficient.
In this post we will introduce several must-know Pandas methods for
effective data exploration.
Create a CSV sample dataset
To better illustrate and demonstrate how to use Pandas functions, let’s first
create a sample CSV dataset.
import random
import csv
from faker import Faker
# Initialize Faker
fake = Faker()
# List of products and their categories
products = [
    {"name": "Laptop", "category": "Electronics", "price": 899.99},
    {"name": "Smartphone", "category": "Electronics", "price": 699.99},
    {"name": "Headphones", "category": "Accessories", "price": 49.99},
    {"name": "Coffee Maker", "category": "Home Appliances", "price": 79.99},
    {"name": "Sneakers", "category": "Fashion", "price": 59.99},
    {"name": "Backpack", "category": "Fashion", "price": 39.99},
    {"name": "Blender", "category": "Home Appliances", "price": 99.99},
    {"name": "Desk Chair", "category": "Furniture", "price": 129.99},
    {"name": "Water Bottle", "category": "Accessories", "price": 19.99},
    {"name": "Notebook", "category": "Stationery", "price": 5.99},
]
# Define a function to generate order data
def generate_order_data(num_rows):
    data = []
    for _ in range(num_rows):
        product = random.choice(products)
        quantity = random.randint(1, 10)
        total = round(product["price"] * quantity, 2)
        order = {
            "Order ID": fake.uuid4(),
            "Customer Name": fake.name(),
            "Customer Email": fake.email(),
            "Product Name": product["name"],
            "Category": product["category"],
            "Quantity": quantity,
            "Price": product["price"],
            "Total": total,
            "Order Date": fake.date_this_year(),
            "Shipping Address": fake.address(),
        }
        data.append(order)
    return data
# Generate 1000 rows of data
num_rows = 1000
order_data = generate_order_data(num_rows)
# Save the data to a CSV file
output_file = "sample_orders.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=order_data[0].keys())
    writer.writeheader()
    writer.writerows(order_data)
print(f"Sample dataset with {num_rows} rows has been saved to '{output_file}'.")
This code ensures that the sample dataset is saved as a structured CSV file
(sample_orders.csv) for further data analysis by pandas functions.
Head function head()
head(): Used to preview the top rows of the sample dataset.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the first 10 rows of the dataset
print(df.head(10))
Tail function tail()
tail(): Used to preview the bottom rows of the sample dataset.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the last 10 rows of the dataset
print(df.tail(10))
Sample function sample()
sample(): This function is highly valuable when working with large datasets.
When we need to extract and analyze a smaller subset from a larger
DataFrame, `sample()` helps efficiently retrieve random samples, enabling
preliminary data exploration or performance evaluation.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Read and display the random 10 rows from the dataset
print(df.sample(10))
Information function info()
info(): This function provides a summary of the dataset, including the
number of entries, column names, data types, and memory usage.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display a summary of the dataset
print(df.info())
Describe function describe()
describe(): This function provides basic statistical information about the
dataset, such as mean, standard deviation, minimum and maximum values,
and quartiles.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the basic statistical information about the dataset
print(df.describe())
Value counts function value_counts()
value_counts(): This method returns the count of all unique values in a
column or a pandas Series.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the count of all unique values in a column,such as "Category"
print(df["Category"].value_counts())
Shape attribute
shape: This attribute returns the number of rows and columns in the dataset.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the number of rows and columns in the dataset
print(df.shape)
Dataframe dtypes attribute
df.dtypes: This attribute returns the data types of all columns.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the data types of all columns
print(df.dtypes)
Unique function unique()
unique(): This method returns all unique values in a column or a pandas
Series.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display all unique values in a column.
print(df["Category"].unique())
Nunique function nunique()
nunique(): This function returns the number of unique values in a
DataFrame.
import pandas as pd
# Read the sample_orders.csv file into a Pandas DataFrame
df = pd.read_csv("sample_orders.csv")
# Display the count of unique values in the dataset, sorted in descending order
df.nunique().sort_values(ascending=False)
In this post we provide a detailed introduction to essential core functions in
the Pandas library, which are crucial for data analysis. These functions make
data exploration more straightforward and efficient, helping analysts quickly
grasp the structure and characteristics of a dataset.
With these must-know functions, data analysts can gain deeper insights into
the data, uncover the stories behind it, and provide data-driven support for
decision-making. These Pandas functions are an indispensable part of the
data analysis workflow, enhancing both the efficiency and the depth of
analysis.
Thanks for your reading.
Python Pandas Pandas Tutorial Pandas Data Preprocessing
Python Pandas Dataframe
Written by Gen. David L.
Follow
453 Followers · 4 Following
AI practitioner & python coder to record what I learned in python project
development
No responses yet
What are your thoughts?
Respond
More from Gen. David L.
Gen. David L. Gen. David L.
Advanced Pandas Features: ETL-PIPES: An Efficient Python ETL
Enhance Your Data Processing… Data Processing Library
The essence of data analysis lies in ETL-pipes is a powerful and flexible Python
uncovering the stories behind the data. In thi… library specifically designed for ETL (Extract…
Dec 5, 2024 105 Nov 30, 2024 45 6
Gen. David L. Gen. David L.
How to Map Column Values in a Four Ways to Package a Python
Pandas DataFrame? Project into an executable EXE…
Mapping column values refers to replacing In Python, packaging a project into an
specific values in a column with other values,… executable EXE file is a common task,…
Dec 24, 2024 81 Sep 14, 2024 94
See all from Gen. David L.
Recommended from Medium
Anita Gupta Harold Finch
Statistics Handbook for Data Top 25 Python Scripts To Automate
Analysts Your Daily Tasks
Why This Handbook? Python is an excellent tool for automating
daily tasks, thanks to its simplicity and a wid…
Sep 14, 2024 422 11 Nov 19, 2024 337 5
Lists
Staff picks Stories to Help You Level-Up
at Work
798 stories · 1568 saves
19 stories · 917 saves
Self-Improvement 101 Productivity 101
20 stories · 3214 saves 20 stories · 2716 saves
In The Pythoneers by Kevin Meneses González In Python in Plain English by Satyam Sahu
5 Ways to Make Money with Python How I Automated Data Cleaning in
in 2025 Python Using Functions and…
The future belongs to those who believe in the Discover the key Python techniques that
beauty of their dreams.” — Eleanor Roosevelt transformed my data-cleaning workflow fro…
Dec 8, 2024 282 10 Nov 4, 2024 216 7
Gen. David L. Lorenzo Uriel
Starting a Python Project
How to Split Columns in a
This guide documents the steps I take to set
DataFrame Using Python Pandas up the foundation of any Python project, wit…
Splitting columns is a common data
manipulation operation in Pandas. It allows u… Nov 19, 2024 208 1
Dec 21, 2024 62
See more recommendations