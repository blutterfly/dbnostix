# SummaryTools


SummaryTools is another library that provides a detailed overview of your
dataset. It’s similar to Skimpy but adds a few extra features, like:
Collapsible Summaries: Perfect for when you have large datasets and
want a clean overview.
Tabbed Summaries: Makes it easy to switch between different views of
your data.


## Implamentation
Here’s how to use SummaryTools:

~~~python
from summarytools import dfSummary
import pandas as pd
# Create a sample DataFrame
data = {'Age': [25, 30, 35, 40, None], 
        'Salary': [50000, 60000, 70000, 80000, 90000], 
        'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']}
df = pd.DataFrame(data)
# Generate a collapsible summary
summary = dfSummary(df)
summary.to_notebook()  # Use this to display the report in Jupyter Notebook
~~~


~~~python
from summarytools import dfSummary
import pandas as pd
# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, None],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining Date': ['2020-01-15', '2019-06-20', '2021-03-10', '2018-12-25', '20
}
df = pd.DataFrame(data)
df['Joining Date'] = pd.to_datetime(df['Joining Date'])  # Convert Joining Date 

# Step 3: Generate a Summary with SummaryTools
Use the dfSummary function to create a summary and display it in a Jupyter
Notebook.
# Generate a summary of the dataset
summary = dfSummary(df) 
# Display the summary in a Jupyter Notebook
summary.to_notebook()
~~~

~~~plain
What the Summary Includes
Overview: Number of rows, columns, and missing values.
Column-Level Insights:
Data type.
Mean, median, and standard deviation for numeric columns.
Unique values for categorical columns.
Distribution charts (where applicable).
Interactive Features:
Collapsible sections for large datasets.
Tabbed views for switching between summaries.
~~~

Example

~~~plain
Example Output
General Overview:
Rows: 5
Columns: 5
Missing Values: Age (1 missing)
Column Details:
Advanced Features
Save the Summary to HTML
You can save the summary report as an HTML file for sharing:
summary.to_html('dataset_summary.html')
Export as JSON or CSV
You can export the data insights for programmatic use:
summary.to_json('dataset_summary.json') 
summary.to_csv('dataset_summary.csv')
~~~