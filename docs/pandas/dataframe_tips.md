# Dataframe Tips

Pandas is one of the most popular Python libraries for data manipulation
and analysis. Use these tips for efficiency

## 1. Use .at and .iat

Accessing or modifying individual values in a DataFrame is something you’ll
do often. While **.loc** and **.iloc** are the most common methods, they aren’t
always the fastest. 

For single-value access, .at (label-based) and .iat
(integer position-based) are optimized for speed. This can make a big
difference in large datasets.

~~~python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Accessing a value
value = df.at[0, 'A']  # Faster than df.loc[0, 'A']

# Modifying a value
df.iat[1, 1] = 10      # Faster than df.iloc[1, 1] = 10
~~~

In simple terms: Use .at when you know the column and row labels, and
.iat when you’re working with index positions.

## 2. Use .query

Filtering rows with conditions is a daily task. While traditional boolean
indexing works, it can get messy, especially with multiple conditions. Enter
the query method, which lets you filter rows using SQL-like syntax for
readability.

~~~python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Instead of this
filtered = df[(df['A'] > 1) & (df['B'] < 6)]

# Use query for cleaner code
filtered = df.query('A > 1 & B < 6')
~~~

When your filtering logic gets more complex, query makes your code much
easier to read and maintain.

## 3. Use vectorized operations

Loops feel natural to use, but they’re inefficient when working with Pandas.
The library is built for vectorized operations, which are faster because
they’re executed in C under the hood. If you’re using for loops or apply for
simple column-wise calculations, you’re doing it the hard way.

~~~python
# Slow loop
df['C'] = [a + b for a, b in zip(df['A'], df['B'])]

# Fast vectorized operation
df['C'] = df['A'] + df['B']
~~~
Not only is the vectorized approach faster, but it’s also more readable. Think
of your DataFrame as a single entity rather than individual rows and
columns.

## 4. Use .assign to chain operations

Data cleaning often involves multiple transformations. Instead of
performing one operation, assigning it back to the DataFrame, and
repeating, you can use .assign to chain them together. This makes your
code more elegant and less error-prone.

~~~python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Add or modify columns in one step
df = df.assign(
    D=df['A'] * 2,
    E=lambda x: x['B'] + 3
)
~~~

Now you can add or modify multiple columns without interrupting the
workflow. This is especially useful when chaining multiple operations
together.

## 5. Use .map and .applymap

If you’re transforming a single column, use .map instead of apply. It’s faster
and more concise. For element-wise transformations across an entire
DataFrame, use .applymap. Reserve apply for row-wise or column-wise
operations.

~~~python
# Use map for single columns
df['A'] = df['A'].map(lambda x: x * 2)
# Use applymap for element-wise operations across the DataFrame
df = df.applymap(lambda x: x * 2)
~~~

This keeps your code focused and avoids unnecessary complexity.

## 6. Use .to_dict 

When working with APIs or exporting data, you’ll often need to convert a
DataFrame to a dictionary. Instead of writing custom code, use Pandas’ built-
in to_dict method. Choosing the correct orient argument can save you a lot
of headaches.

~~~python
# Convert rows to a list of dictionaries
data_dict = df.to_dict(orient='records')
~~~

This method is perfect for JSON-style outputs, where each dictionary
represents a row. It’s a lifesaver when integrating with external systems.

## 7. Use .groupby 

The .groupby function is a powerhouse for summarizing data, but did you
know you can combine it with .agg to perform multiple custom
aggregations at once? This makes it easy to produce complex summaries in
just a few lines.

~~~python
df = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': [1, 2, 3], 'C': [4, 5, 6]})
# Group by column 'A' and compute custom aggregations
result = df.groupby('A').agg(
    sum_B=('B', 'sum'),    # Sum of column B
    mean_C=('C', 'mean')   # Mean of column C
)
~~~

Instead of chaining multiple .groupby and aggregation calls, this allows you
