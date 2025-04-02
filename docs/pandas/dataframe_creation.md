

## Code Examples

~~~python
# A simple dataframe  with Name, Age, and City columns.
import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30],
    "City": ["New York", "Los Angeles"]
})
print(df)

# List of dictionaries
data = [
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    {"Name": "David", "Age": 40, "City": "Miami"}
]
df = pd.DataFrame(data)
print(df)

# Converts a list of dictionaries to a DataFrame.
df = pd.DataFrame({
    "Name": ["Eve", "Frank"],
    "Age": [28, 34],
    "City": ["Boston", "Seattle"]
}, index=["Row1", "Row2"])
print(df)

# Uses custom labels for rows instead of default numeric index.
Creating DataFrames
df_list = pd.DataFrame([
    ["Grace", 29],
    ["Henry", 32]
], columns=["Name", "Age"])
print(df_list)

# Uses separate lists for each row and specifies column labels.
data_dict = {"Name": ["Ivy", "Jack"], "Age": [24, 36]}
df_dict = pd.DataFrame(data_dict)
print(df_dict)
~~~

## Importing data from CSV files
the transition from file-based storage to in-memory data manipulation
efficiently. This method is straightforward and essential for handling large
datasets typically stored in CSV format.
~~~python
df_csv = pd.read_csv("data.csv")
print(df_csv)
~~~

## Search
~~~python
import pandas as pd Open in app
# Create a DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})
# Use .loc to select by label
first_row = df.loc[0]  # Select the first row
specific_cell = df.loc[1, 'Age']  # Access a specific cell
print("First Row:\n", first_row)
print("Specific Cell (Row 1, Age):", specific_cell)
# Use .iloc to select by position
first_column = df.iloc[:, 0]  # Select the first column
specific_rows = df.iloc[0:2]  # Retrieve the first two rows
print("First Column:\n", first_column)
print("Specific Rows:\n", specific_rows)
# Apply boolean indexing to filter data
adults = df[df['Age'] > 25]  # Filter rows where age is greater than 25
los_angeles_residents = df[df['City'] == "Los Angeles"]
print("Adults:\n", adults)
print("Los Angeles Residents:\n", los_angeles_residents)
~~~


## Modifying DataFrames

~~~python
# Add a new column 'Height' to the DataFrame
df['Height'] = [165, 180, 175]  # Heights corresponding to each person
print("DataFrame with Height:\n", df)
# Remove the 'City' column from the DataFrame
df = df.drop('City', axis=1)
print("DataFrame without City:\n", df)
# Updating specific cell values in the DataFrame
df.loc[0, 'Age'] = 26
df.iloc[2, 1] = 36  # Update Charlie's age using integer position
print("Updated DataFrame:\n", df)
~~~

## Data Cleaning

Example 1: Filling NaN with Mean

~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, np.nan, 30]}
df = pd.DataFrame(data)
# Fill NaN values in 'Age' with the mean of the column
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
~~~

Example 2: Removing Rows with NaN

~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, np.nan, 30],
        'City': [np.nan, 'New York', 'Los Angeles']}
df = pd.DataFrame(data)
# Drop rows where any element is NaN
df_clean = df.dropna()
print(df_clean)
~~~

Example 3: Filling NaN with Forward Fill Method

~~~python
import pandas as pd
import numpy as np
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, np.nan, np.nan],
        'City': ['New York', np.nan, 'Los Angeles']}
df = pd.DataFrame(data)
# Forward fill NaN values in the DataFrame
df.ffill(inplace=True)
print(df)
~~~

Example 4: Converting String to Integer
~~~
import pandas as pd
# Sample DataFrame
data = {'ID': ['101', '102', '103'],
        'Amount': ['1000', '1500', '1200']}
df = pd.DataFrame(data)
# Convert 'Amount' from string to integer
df['Amount'] = df['Amount'].astype(int)
print(df.dtypes)
~~~

Example 5: Converting Integer to Float
~~~python
import pandas as pd
# Sample DataFrame
data = {'Product': ['A', 'B', 'C'],
        'Price': [200, 150, 300]}
df = pd.DataFrame(data)
# Convert 'Price' from int to float
df['Price'] = df['Price'].astype(float)
print(df.dtypes)
~~~

Example 6: Handling Conversion Errors

~~~python
import pandas as pd
# Sample DataFrame
data = {'Year': ['2020', 'NaN', '2021'],
        'Value': ['100', '200.5', '300']}
df = pd.DataFrame(data)
try:
    # Attempt to convert 'Year' to int
    df['Year'] = df['Year'].astype(int)
except ValueError:
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
print(df)
~~~

