Open in app
Search Write
How to Map Column Values in a
Pandas DataFrame?
Gen. Devin DL. · Follow
3 min read · Dec 24, 2024
86
Mapping column values refers to replacing specific values in a column with
other values, commonly used in data cleaning and transformation.
There are many scenarios where mapping column values is useful. Here are
a few common use cases:
1. Mapping certain string values in a column to numbers. For example,
mapping “Male” and “Female” to 0 and 1, respectively, to facilitate
training and prediction in machine learning algorithms.
2. Replacing abbreviations with full names. For instance, replacing “USA”
and “UK” with “United States” and “United Kingdom” to make the data
more readable.
3. Correcting mis-spelled words by replacing them with the correct
spelling. For example, replacing “Cocacola” with “Coca-Cola” to avoid
errors in statistics and analysis.
In this post we will introduce several common mapping techniques.
Using the map function
The map function is one of the simplest and most direct methods. For
example, in the following case, mapping gender values to 0 and 1.
import pandas as pd
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "sex": ["female", "male", "male", "male", "female", "male"],
    "age": [23, 34, 29, 42, 25, 31],
})
df.sex = df.sex.map({
    "female": 0, 
    "male": 1,
})
print(df)
Before mapping:
After mapping:
Factorize Mapping
Using the map function to map column values is the most straightforward
method. However, when there are many distinct values in the column,
mapping them one by one can be cumbersome. For example, in the case of
the grade column in the following example, unlike the sex column which
only has two values, it contains more possible values.
In this case, we can use the factorize method to perform the mapping.
import pandas as pd
df = pd.DataFrame({
    "name": ["John", "Emily", "Michael", "Sarah", "James", "Olivia"],
    "sex": ["male", "female", "male", "female", "male", "female"],
    "grade": ["A", "B", "C", "A", "B", "C"],
})
df.sex = df.sex.factorize()[0]
df.grade = df.grade.factorize()[0]
print(df)
Before mapping:
After mapping:
The factorize function returns a tuple with two elements. The first element
is an array of numbers representing the mapped values, and the second
element is an index type, where the index values correspond to the unique
values in the column.
df.grade.factorize()
So the code uses factorize()[0].
If we want to binarize the values after mapping, for example, in the case of
the grade column, where there are four different values representing
different grade levels. If we only want two categories — fail (F) and pass
(non-F), then code will be：
df.grade = df.grade.factorize()[0]
df.grade = (df.grade == 2).astype("int")
print(df)
After mapping:
Here A and B are mapped to 0, and C is mapped to 1.
Thanks for your reading.
Pandas Dataframe Python Data Preprocessing Pandas
Written by Gen. Devin DL.
Follow
505 Followers · 4 Following
AI practitioner & python coder to record what I learned in AI & Data Science &
Python project development
No responses yet
What are your thoughts?
Respond
More from Gen. Devin DL.
Gen. Devin DL. Gen. Devin DL.
Four Ways to Package a Python Building Python ETL Data Pipelines
Project into an executable EXE… with Five Typical Cases
In Python, packaging a project into an Data pipelines are the backbone of data
executable EXE file is a common task,… processing. Simply put, it’s about moving da…
Sep 14, 2024 104 Jan 26 71
Gen. Devin DL. Gen. Devin DL.
ETL-PIPES: An Efficient Python ETL Comparison of Flask, Django, and
Data Processing Library FastAPI: Advantages,…
ETL-pipes is a powerful and flexible Python In Python web development, Flask, Django,
library specifically designed for ETL (Extract… and FastAPI are all popular frameworks. This…
Nov 30, 2024 117 6 Oct 17, 2023 92
See all from Gen. Devin DL.
Recommended from Medium
Sarowar Jahan Saurav Vijay Gadhave
Beyond the Basics: 11 Complex When to Use COUNT(*) vs
Statistical Algorithms to Elevate… COUNT(1) in SQL Queries
Data Science is more than just running Note: If you’re not a medium member, CLICK
standard algorithms or crafting elegant… HERE
Sep 13, 2024 107 Jan 14 399 25
Lists
Staff picks Stories to Help You Level-Up
at Work
817 stories · 1632 saves
19 stories · 943 saves
Self-Improvement 101 Productivity 101
20 stories · 3316 saves 20 stories · 2791 saves
In Stackademic by Khouloud Haddad Amamou Alice Yang
Data Analysis with Python Pandas How to Create, Update and Remove
and Matplotlib Tables in Excel with Python
1. Introduction Tables in Excel are a powerful tool that helps
us manage, organize, and analyze data…
Jan 30 150 8 Oct 10, 2024 11
In Artificial Intelligence in Plain En… by Ritesh Gu… Python Coding
Data Science All Algorithm 9 Confusing Python Concepts That
Cheatsheet 2025 Frustrate Most Developers
Stories, strategies, and secrets to choosing 1. The is vs == Confusion
the perfect algorithm.
Jan 5 1.3K 27 Oct 2, 2024 162 2
See more recommendations