Member-only story
7 Pandas DataFrame Tricks I Wish I
Knew in My Last Job
Brent Fischer · Follow
Published in Python in Plain English · 4 min read · Jan 2, 2025
5
Open in app
Search Write
Pandas for Experts
Pandas is one of the most popular Python libraries for data manipulation
and analysis, but it can be overwhelming when you’re starting out or under
time pressure at work. Learning these tricks would have saved me a lot of
frustration and time in my last job, and I’m here to share them with you so
you can work smarter, not harder.
1. Use   and   for Faster Access to Single Values
.at .iat
Accessing or modifying individual values in a DataFrame is something you’ll
do often. While .loc and .iloc are the most common methods, they aren’t
always the fastest. For single-value access, .at (label-based) and .iat
(integer position-based) are optimized for speed. This can make a big
difference in large datasets.
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Accessing a value
value = df.at[0, 'A']  # Faster than df.loc[0, 'A']
# Modifying a value
df.iat[1, 1] = 10      # Faster than df.iloc[1, 1] = 10
In simple terms: Use .at when you know the column and row labels, and
.iat when you’re working with index positions.
2. Use   for Cleaner Filtering
query
Filtering rows with conditions is a daily task. While traditional boolean
indexing works, it can get messy, especially with multiple conditions. Enter
the query method, which lets you filter rows using SQL-like syntax for
readability.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Instead of this
filtered = df[(df['A'] > 1) & (df['B'] < 6)]
# Use query for cleaner code
filtered = df.query('A > 1 & B < 6')
When your filtering logic gets more complex, query makes your code much
easier to read and maintain.
3. Vectorized Operations Instead of Loops
Loops feel natural to use, but they’re inefficient when working with Pandas.
The library is built for vectorized operations, which are faster because
they’re executed in C under the hood. If you’re using for loops or apply for
simple column-wise calculations, you’re doing it the hard way.
# Slow loop
df['C'] = [a + b for a, b in zip(df['A'], df['B'])]
# Fast vectorized operation
df['C'] = df['A'] + df['B']
Not only is the vectorized approach faster, but it’s also more readable. Think
of your DataFrame as a single entity rather than individual rows and
columns.
4. Use   to Chain Transformations
.assign
Data cleaning often involves multiple transformations. Instead of
performing one operation, assigning it back to the DataFrame, and
repeating, you can use .assign to chain them together. This makes your
code more elegant and less error-prone.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Add or modify columns in one step
df = df.assign(
    D=df['A'] * 2,
    E=lambda x: x['B'] + 3
)
Now you can add or modify multiple columns without interrupting the
workflow. This is especially useful when chaining multiple operations
together.
5. Replace   with   or   for Simpler Tasks
apply .map .applymap
If you’re transforming a single column, use .map instead of apply. It’s faster
and more concise. For element-wise transformations across an entire
DataFrame, use .applymap. Reserve apply for row-wise or column-wise
operations.
# Use map for single columns
df['A'] = df['A'].map(lambda x: x * 2)
# Use applymap for element-wise operations across the DataFrame
df = df.applymap(lambda x: x * 2)
This keeps your code focused and avoids unnecessary complexity.
6. Convert DataFrames to Dictionaries Efficiently
When working with APIs or exporting data, you’ll often need to convert a
DataFrame to a dictionary. Instead of writing custom code, use Pandas’ built-
in to_dict method. Choosing the correct orient argument can save you a lot
of headaches.
# Convert rows to a list of dictionaries
data_dict = df.to_dict(orient='records')
This method is perfect for JSON-style outputs, where each dictionary
represents a row. It’s a lifesaver when integrating with external systems.
7. Use   with Custom Aggregations
.groupby
The .groupby function is a powerhouse for summarizing data, but did you
know you can combine it with .agg to perform multiple custom
aggregations at once? This makes it easy to produce complex summaries in
just a few lines.
df = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': [1, 2, 3], 'C': [4, 5, 6]})
# Group by column 'A' and compute custom aggregations
result = df.groupby('A').agg(
    sum_B=('B', 'sum'),    # Sum of column B
    mean_C=('C', 'mean')   # Mean of column C
)
Instead of chaining multiple .groupby and aggregation calls, this allows you
to calculate everything at once, making your code concise and efficient.
Thank you for being a part of the community
Before you go:
👏
Be sure to clap and follow the writer  
Follow us: X | LinkedIn | YouTube | Newsletter | Podcast
Check out CoFeed, the smart way to stay up-to-date with the latest in
🧪
tech 
🚀
Start your own free AI-powered blog on Differ 
 💻
Join our content creators community on Discord   
For more content, visit plainenglish.io + stackademic.com
Pandas Python Dataframes Tricks
Published in Python in Plain English
Follow
36K Followers · Last published 13 hours ago
New Python content every day. Follow to join our 3.5M+ monthly readers.
Written by Brent Fischer
Follow
24 Followers · 12 Following
Python Developer, Python Trainer, Geek, RPGs, Pizza, Traveller. Loves Rust, C,
Linux. Drop by at friendlybytes.net
No responses yet
What are your thoughts?
Respond
More from Brent Fischer and Python in Plain English
In Level Up Coding by Brent Fischer In Python in Plain English by Kiran Maan
Linux for Pythonistas: Advanced Can Mojo Really Replace Python?
File Monitoring and Automation… Let’s Test It
In Linux, inotify (inotify stands for "inode A few days ago, I got to know about Mojo on
notify") is a powerful kernel subsystem that… Medium. I just made a pause and read: “Mojo…
Dec 12, 2024 95 Dec 19, 2024 697 14
In Python in Plain English by Afsalkh In Python in Plain English by Brent Fischer
Why Does round(6.5) Return 6 Python Advanced: The Beginner’s
While round(7.5) Returns 8 in… Guide to Ruff
Pythonistas, Can You Explain This Rounding As Python projects grow in size and
Oddity? complexity, maintaining clean and consisten…
Dec 3, 2024 697 13 Dec 9, 2024 20
See all from Brent Fischer See all from Python in Plain English
Recommended from Medium
In Dev Genius by Aleksei Aleinikov De Os
10 Ways to Work with Large Files in Pandas Read Excel 18 Times Faster
Python: Effortlessly Handle…
Yesterday, I had to process around 750 Excel
Handling large text files in Python can feel files with approximately 165,000 rows each.…
overwhelming. When files grow into…
Dec 1, 2024 304 3 Jul 11, 2024 164 1
Lists
Coding & Development Predictive Modeling w/
Python
11 stories · 964 saves
20 stories · 1765 saves
Practical Guides to Machine ChatGPT
Learning
21 stories · 938 saves
10 stories · 2138 saves
Varun Singh Lorenzo Uriel
Python 3.14 Released — Top 5 Starting a Python Project
Features You Must Know
This guide documents the steps I take to set
Faster Annotations & Mind-Blowing Updates up the foundation of any Python project, wit…
You NEED to Know!
Dec 31, 2024 62 Nov 19, 2024 200 1
In Towards Data Engineering by Sandun Lakshan In Towards Data Science by Vladimir Zhyvov
10 Best Python Text User Interface From Default Python Line Chart to
(TUI) Libraries for 2025 Journal-Quality Infographics
Text-based user interfaces (TUIs) are a simple Transform boring default Matplotlib line
way to create interactive applications that ru… charts into stunning, customized…
Dec 10, 2024 36 1 Dec 30, 2024 1.1K 18
See more recommendations