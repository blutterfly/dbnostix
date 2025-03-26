# NumPy

Explore pandas functions that can also use with numpy

+ Pandas for data manipulation and analysis or 
+ NumPy for numerical computing


## Compare Pandas and Numpy

### 1. Shift 

The pandas.Series.shift() function shifts the values of a particular position
in a Series up or down by a specified number of periods. 

Pandas: Shifts the values of a series by a certain number of periods.
NumPy Equivalent: You can use np.roll() to achieve a similar effect.

Example
~~~python
# Pandas
df['shifted'] = df['column'].shift(1)

#  NumPy
df['shifted'] = np.roll(df['column'].values, 1)
~~~

### 2. Diff 
pandas.Series.diff() is
used to calculate the difference between consecutive elements in a given
series.

Interestingly, you can achieve the same result with NumPy using np.diff().

Example
~~~python
# Pandas
df['difference'] = df['column'].diff()
# NumPy
df['difference'] = np.diff(df['column'], prepend=np.nan)
~~~

Output
~~~plaintext

output
   column  difference  difference_np
0      30         NaN             NaN
1      32         2.0             2.0
2      35         3.0             3.0
3      31        -4.0            -4.0
4      29        -2.0            -2.0
~~~

### 3. Apply

pandas.DataFrame.apply() you can add two rows and form a
new one as an answer.

Pandas: Apply a function to each row or column.
NumPy Equivalent: Use np.apply_along_axis() for similar functionality
on NumPy arrays.

Example

~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
df = pd.DataFrame(data)
# Using Pandas
df['result'] = df.apply(lambda row: row['a'] + row['b'], axis=1)
# Using NumPy
result = np.apply_along_axis(lambda row: row[0] + row[1], 1, df[['a', 'b']].valu
print(df)
print("NumPy Result:", result)
~~~

Output
~~~plain
   a  b  result
0  1  4       5
1  2  5       7
2  3  6       9
NumPy Result: [5 7 9]
~~~

### 4. Rank
pandas.Series.rank()

Pandas: Computes the rank of each element in a Series.
NumPy Equivalent: You can achieve similar functionality using
np.argsort().

Example:
~~~python

import pandas as pd
import numpy as np
# Sample DataFrame
data = {'column': [50, 20, 80, 60]}
df = pd.DataFrame(data)
# Using Pandas
df['rank'] = df['column'].rank()
# Using NumPy
ranks = np.argsort(np.argsort(df['column'].values))
df['numpy_rank'] = ranks + 1  # Adding 1 because ranks start from 1 in Pandas
print(df)
~~~

Output
~~~plain
   column  rank  numpy_rank
0      50   2.0           2
1      20   1.0           1
2      80   4.0           4
3      60   3.0           3
~~~

### 5. IsIn
pandas.Series.isin()
Pandas: Check if elements in a Series are in a given list or array.
NumPy Equivalent: Use np.in1d() to perform this task.

Example:
~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {
    'product': ['TV', 'Sofa', 'Laptop', 'Table', 'Shirt', 'Headphones', 'Shoes']
    'category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Clothi
}
df = pd.DataFrame(data)
# Categories to check
target_categories = ['Electronics', 'Furniture', 'Clothing']
# Using Pandas
df['is_in'] = df['category'].isin(target_categories)
# Using NumPy
df['is_in_np'] = np.in1d(df['category'], target_categories)
# Display the DataFrame
print(df)
~~~

Output:
~~~plain
      product    category  is_in  is_in_np
0          TV  Electronics   True      True
1        Sofa   Furniture    True      True
2      Laptop  Electronics   True      True
3       Table   Furniture    True      True
4       Shirt   Clothing     True      True
5  Headphones  Electronics   True      True
6       Shoes     Apparel   False     False
~~~

### 6. CumSum 

Pandas: Calculates the cumulative sum of the values in a series.
NumPy Equivalent: Use np.cumsum() for cumulative summation.

Example:

~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {'column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
# Using Pandas to calculate cumulative sum
df['cumsum_pandas'] = df['column'].cumsum()
# Using NumPy to calculate cumulative sum
df['cumsum_numpy'] = np.cumsum(df['column'].values)
print(df)
~~~

Output:
~~~
   column  cumsum_pandas  cumsum_numpy
0       1              1             1
1       2              3             3
2       3              6             6
3       4             10            10
4       5             15            15
~~~

### 7. Expanding 

Now, we can achieve this using the pandas.Series.expanding() function,
which expands a window over the data to compute cumulative statistics like
the running mean.

NumPy Equivalent: You can achieve this manually with np.cumsum() and
computing the desired statistic over expanding windows.

Example:
~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {'column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
# Using Pandas to calculate the expanding mean
df['expanding_mean'] = df['column'].expanding().mean()
# Using NumPy to calculate the manual expanding mean
expanding_mean = np.cumsum(df['column'].values) / np.arange(1, len(df) + 1)
# Adding the NumPy result to the DataFrame
df['expanding_mean_numpy'] = expanding_mean
# Display the DataFrame
print(df)
~~~

Output:
~~~plain
   column  expanding_mean  expanding_mean_numpy
0       1             1.0                  1.0
1       2             1.5                  1.5
2       3             2.0                  2.0
3       4             2.5                  2.5
4       5             3.0                  3.0
~~~

### 8. Pct_Change 

Pandas: Computes the percentage change between the current and prior
element.
NumPy Equivalent: Use a combination of NumPy array operations to
calculate the percentage change.

Example:
~~~python
import pandas as pd
import numpy as np
# Sample sales data
data = {'day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
        'sales': [100, 110, 150, 120, 130]}
# Create DataFrame
df = pd.DataFrame(data)
# Using Pandas to compute percentage change
df['pct_change_pandas'] = df['sales'].pct_change()
# Using NumPy to compute percentage change manually
pct_change_numpy = np.diff(df['sales'].values) / df['sales'].values[:-1]
pct_change_numpy = np.insert(pct_change_numpy, 0, np.nan)  # Insert NaN at the s
# Add the NumPy result to the DataFrame
df['pct_change_numpy'] = pct_change_numpy
# Display the DataFrame
print(df)
~~~

Output
~~~plain
     day  sales  pct_change_pandas  pct_change_numpy
0  Day 1    100                NaN               NaN
1  Day 2    110           0.100000          0.100000
2  Day 3    150           0.363636          0.363636
3  Day 4    120          -0.200000         -0.200000
4  Day 5    130           0.083333          0.083333
~~~

### 9. Fill NA 

Pandas: Fills NaN values with a specified value or method.
NumPy Equivalent: Use np.where() to replace NaN values in a NumPy
array.

Example:

~~~python
import pandas as pd
import numpy as np
# Sample data with NaN values
data = {'scores': [100, 200, np.nan, 300, np.nan]}
# Create DataFrame
df = pd.DataFrame(data)
# Using Pandas to fill NaN values
df['filled_pandas'] = df['scores'].fillna(0)
# Using NumPy to fill NaN values manually
df['filled_numpy'] = np.where(np.isnan(df['scores'].values), 0, df['scores'].val
# Display the DataFrame
print(df)


Output:
~~~plain
   scores  filled_pandas  filled_numpy
0   100.0          100.0         100.0
1   200.0          200.0         200.0
2     NaN            0.0           0.0
3   300.0          300.0         300.0
4     NaN            0.0           0.0
~~~

### 10. Drop NA 
The pandas.DataFrame.dropna() function removes rows (or columns) from a

Pandas: Drops rows or columns with NaN values.
NumPy Equivalent: Use ~np.isnan() to filter out rows containing NaN.

Example:

~~~python
import pandas as pd
import numpy as np
# Sample data with NaN values
data = {'scores': [100, 200, np.nan, 300, 150]}
# Create DataFrame
df = pd.DataFrame(data)
# Using Pandas to drop rows with NaN values
df_cleaned_pandas = df.dropna()
# Using NumPy to manually filter out rows with NaN values
df_cleaned_numpy = df[~np.isnan(df['scores'].values)]
# Display the results
print("Original DataFrame:\n", df)
print("\nPandas dropna():\n", df_cleaned_pandas)
print("\nNumPy equivalent:\n", df_cleaned_numpy)
~~~

Output
~~~plain

Original DataFrame:
    scores
0   100.0
1   200.0
2     NaN
3   300.0
4   150.0
Pandas dropna():
    scores
0   100.0
1   200.0
3   300.0
4   150.0
NumPy equivalent:
    scores
0   100.0
1   200.0
3   300.0
4   150.0
~~~

### 11. Value Counts 

Pandas: Counts the unique values in a series.
NumPy Equivalent: Use np.unique() with return_counts=True to get
unique values and their counts.
Example:
Responses: ['A', 'B', 'A', 'C', 'B', 'A', 'B']
~~~python
import pandas as pd
import numpy as np
# Sample data
data = {'responses': ['A', 'B', 'A', 'C', 'B', 'A', 'B']}
# Create DataFrame
df = pd.DataFrame(data)
# Using Pandas to count unique values
value_counts_pandas = df['responses'].value_counts()
# Using NumPy to count unique values manually
unique, counts = np.unique(df['responses'].values, return_counts=True)
value_counts_numpy = dict(zip(unique, counts))  # Combine unique values and coun
# Display the results
print("Pandas value_counts():\n", value_counts_pandas)
print("\nNumPy equivalent:\n", value_counts_numpy)
~~~

Output:
~~~plain
Pandas value_counts():
 A    3
 B    3
 C    1
Name: responses, dtype: int64
NumPy equivalent:
 {'A': 3, 'B': 3, 'C': 1}
~~~
