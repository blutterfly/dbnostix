# Quick Examples
## Example Code
~~~python
import pandas as pd
import numpy as np

# 1. Load Data with read_csv
df = pd.read_csv('data.csv', usecols=['Column1', 'Column2'])

# 2. View the First Few Rows with head()
df.head()

# 3. Check missing values
df.isna().sum()

# 4. Remove duplicates
df.drop_duplicates(inplace=True)

# 5. Rename columns
df.rename(columns={'old_name':'new_name'}, inplace=True)

# 6. Convert Data Types with astype()
df['Column1'] = df['Column1'].astype(float)

# 7. Handle Missing Data with fillna()
df.fillna(method='ffill', inplace=True)

# 8. Set a Column as the Index
df.set_index('Column1', inplace=True)

# 9. Use groupby() for Aggregation
df.groupby('Category').agg({'Value': 'sum'})

# 10. Sort Values with sort_values()
df.sort_values(by='Column1', ascending=False)

# 11. Use apply() for Custom Functions
df['new_column'] = df['Column1'].apply(lambda x: x * 2)

# 12. Filter Rows Based on Conditions
df_filtered = df[df['Column1'] > 10]

# 13. Use query() for More Complex Filters
df.query('Column1 > 10 and Column2 == "Yes"')

# 14. Concatenate DataFrames with concat()
df_combined = pd.concat([df1, df2], axis=0)

# 15. Merge DataFrames with merge()
df_merged = pd.merge(df1, df2, on='ID')

# 16. Reset Index with reset_index()
df.reset_index(drop=True, inplace=True)

# 17. Export Data to Excel with to_excel()
df.to_excel('output.xlsx', index=False)

# 18. Save dataframe to CSV
df.to_csv('output.csv', index=False)

# 19. Quickly Get Descriptive Statistics with describe()
df.describe()

# 20. Lambda Functions on Columns
df['new_column'] = df.apply(lambda row: row['Column1'] + row['Column2'], axis=1)

# 21. Drop Unwanted Columns with drop()
df.drop(columns=['Column1', 'Column2'], inplace=True)

# 22. Random sampling — use sample()
df_sample = df.sample(n=5)

# 23. Extract Year, Month, or Day from DateTime Columns
df['year'] = df['DateColumn'].dt.year
df['month'] = df['DateColumn'].dt.month

# 24. Convert Column to Categorical Type
df['Category'] = df['Category'].astype('category')

# 25. Find Duplicates Across Specific Columns
df[df.duplicated(subset=['Column1', 'Column2'])]

# 26. Use shift() for Lagging Data
df['lagged_column'] = df['Value'].shift(1)

# 27. Pivot Data with pivot_table()
df_pivot = df.pivot_table(values='Value', index='Category', columns='Region', ag

# 28. Plot with Pandas’ Built-In Plotting
You can also plot quick plots with pandas integrated with Matplotlib.
df['Value'].plot(kind='line')

# 29. Working with Strings on the Columns
df['name'] = df['name'].str.lower()

# 30. Make a New Column Using a Condition
import numpy as np
df['NewColumn'] = np.where(df['Value'] > 10, 'High', 'Low')

# 31. Using nunique() for Unique Values Count
df['Category'].nunique()

# 32. Get Column Data Types with dtypes
df.dtypes

# 33. Find Correlations with corr()
df.corr()

# 34. Change Display Options
pd.set_option('display.max_rows', 100)

35. Efficient Row-wise Operations
for idx, row in df.iterrows():
    print(row['Column1'])
~~~
## Conclusion
