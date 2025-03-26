# Skimpy

Here’s what Skimpy offers:
Data Shape: Shows the number of rows and columns.
Column Data Types: Groups your columns by data type for clarity.
Summary Statistics: Includes mean, median, and other key stats.
Missing Values: Highlights missing data for each column.
Visual Insights: Offers distribution charts to spot patterns quickly.


## Implementation
Install
~~~bash
pip install polars==0.18.4 
pip install summarytools 
pip install skimpy
~~~

Example

~~~python
import polars as pl
import pandas as pd
import seaborn as sns
from summarytools import dfSummary
from skimpy import skim
df_pd = sns.load_dataset('iris')
df_pl = pl.from_pandas(df_pd)
skim(df_pd)

Openinapp
Open in app
skim(df_pl) # works with Polars DataFrame
Search Write
dfSummary(df_pd)
~~~

Illustration: 

~~~python
from skimpy import skim
import pandas as pd
# Create a sample DataFrame
data = {'Age': [25, 30, 35, 40, None], 
        'Salary': [50000, 60000, 70000, 80000, 90000], 
        'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']}
df = pd.DataFrame(data)

# Generate a summary
skim(df)
When you run this code in a Jupyter Notebook, Skimpy creates a beautiful,
structured report that’s way better than the plain output of df.describe().
Bonus: Skimpy also works with Polars, which is a fast and efficient
alternative to Pandas for large datasets.
Here’s a quick example of how to use Skimpy to summarize a dataset. We’ll
create a sample dataset and use Skimpy to generate a comprehensive
summary.
Step 1: Install Skimpy
First, ensure that you have the Skimpy library installed. You can install it
using pip:
pip install skimpy
Step 2: Import Libraries and Create a Sample Dataset
We’ll use Pandas to create a DataFrame, then summarize it with Skimpy.
from skimpy import skim
import pandas as pd
# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, None],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining Date': ['2020-01-15', '2019-06-20', '2021-03-10', '2018-12-25', '20
}
# Convert Joining Date to datetime
df = pd.DataFrame(data)
df['Joining Date'] = pd.to_datetime(df['Joining Date'])
Step 3: Generate the Summary
Using Skimpy is straightforward. Pass the DataFrame to the skim() function.
# Generate a summary of the dataset
skim(df)
~~~

What You’ll Get:
~~~plain
The output will include:
General Overview: Number of rows, columns, and missing values.
Data Types: Organized by type (e.g., numeric, categorical).
Statistics: Mean, median, min, max, and standard deviation for numeric
columns.
Unique Values: For categorical columns.
Distribution Insights: Charts for numeric columns (when supported in
the environment).
~~~

~~~python
import polars as pl
from skimpy import skim
# Create a Polars DataFrame
data = pl.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, None],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining Date': ['2020-01-15', '2019-06-20', '2021-03-10', '2018-12-25', '20
})
# Summarize the dataset
skim(data)
~~~



