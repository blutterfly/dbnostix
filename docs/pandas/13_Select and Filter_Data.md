Member-only story
Python Pandas: loc and iloc
How to Select and Filter Data in Python
Python Fundamentals · Following
Published in Towards Dev · 5 min read · Mar 16, 2024
27
Python pandas library provides several methods for selecting and filtering
data, such as loc, iloc, [ ] bracket operator, query, isin, between.
Open in app
Search Write
Image from pexels.com
This article will guide you through the essential techniques and functions for
data selection and filtering using pandas. Whether you need to extract
specific rows or columns or apply conditional filtering, pandas has got you
covered. Let’s dive in!
Table of Contents
1. Selecting Columns : [ ] operator, loc, iloc
2. Filtering Rows : [ ] operator, loc, iloc, isin, query, between, string methods
3. Updating Values : loc, iloc, replace
1. Selecting Columns
loc[ ] : This accessor selects rows and columns by labels.
Example: df.loc[row_label, column_label]
*** You can also use loc for slicing operations:
df.loc['row1_label':'row2_label' , 'column1_label':'column2_label']
# Using loc for label-based selection
df.loc[:, 'Customer Country':'Customer State']
all the rows & columns from Customer Country to Customer State
# Using loc for label-based selection
df.loc[[0,1,2], 'Customer Country':'Customer State']
rows 0,1,2 & columns from Customer Country to Customer State
iloc[ ] : This accessor selects rows and columns by integer location.
Example: df.iloc[row_position, column_position]
*** You can also use iloc for slicing operations:
df.iloc['row1_position':'row2_position','col1_position':'col2_position']
# Using iloc for index-based selection
df.iloc[[0,1,2,3] , [3,4,5,6,7,8]]
# or
df.iloc[[0,1,2,3] , 3:9]
rows 0,1,2,3 & columns 3 to 8
# Using iloc for index-based selection
df.iloc[:, 3:8]
all the rows & columns from 3 to 8
[ ] Bracket operator : It allows to select one or multiple columns.
Example: df[['column_label']] or df[['column1', 'column2']]
# Selecting a single column
df[['Customer Country']]
a single column
# Selecting multiple columns
df[['Customer Country', 'Customer State']]
multiple columns
2. Filtering Rows
loc[ ] : It filters rows by labels.
Example: df.loc[condition]
# Using loc for filtering rows
condition = df['Order Quantity'] > 3
df.loc[condition]
# or
df.loc[df['Order Quantity'] > 3]
dataframe with the Order Quantity > 3
# Using loc for filtering rows
df.loc[df['Customer Country'] == 'United States']
dataframe with the Customer Country = United States
iloc() : It filters rows by integer positions.
# Using iloc for filtering rows
df.iloc[[0, 2, 4]]
rows with integer index 0, 2 and 4
# Using iloc for filtering rows
df.iloc[:3, :2]
[ ] Bracket operator : It allows filtering rows based on a condition.
Example: df[condition]
# Using [] bracket operator for filtering rows# Using [] bracket operator for fi
condition = df['Order Quantity'] > 3
df[condition]
# or
df[df['Order Quantity'] > 3]
dataframe with the order quantity > 3
isin([ ]) : It is used to filter data based on a list.
Example: df[df['column_name'].isin(['value1', 'value2'])]
# Using isin for filtering rows
df[df['Customer Country'].isin(['United States', 'Puerto Rico'])]
rows where column ‘Customer Country’ is ‘United States’ or ‘Puerto Rico’
# Filter rows based on values in a list and select spesific columns
df[["Customer Id", "Order Region"]][df['Order Region'].isin(['Central America', 
it selected Customer Id and Order Region columns, where Order Region is Central America or Caribbean
# Using NOT isin for filtering rows
df[~df['Customer Country'].isin(['United States'])]
rows where column ‘Customer Country’ is NOT ‘United States’
query() : This method is used to select data based on a SQL-like
expression.
Example: df.query('condition')
In case your column names contain spaces or special characters, first you
should use the rename() function to rename them.
# Rename the columns before performing the query
df.rename(columns={'Order Quantity' : 'Order_Quantity', "Customer Fname" : "Cust
# Using query for filtering rows with a single condition
df.query('Order_Quantity > 3')
dataframe with the order quantity > 3
# Using query for filtering rows with multiple conditions
df.query('Order_Quantity > 3 and Customer_Fname == "Mary"')
dataframe with the order quantity > 3 and Customer Fname = Mary
between() : Filters rows based on values that fall within a specified range.
Example: df[df['column_name'].between(start, end)]
# Filter rows based on values within a range
df[df['Order Quantity'].between(3, 5)]
dataframe with the order quantity between 3 and 5
String methods : Filters rows based on string matching conditions.
Example: str.startswith(), str.endswith(), str.contains()
# Using str.startswith() for filtering rows
df[df['Category Name'].str.startswith('Cardio')]
# Using str.contains() for filtering rows
df[df['Customer Segment'].str.contains('Office')]
3. Updating Values
loc[ ] : This accessor selects specific rows and columns in the DataFrame
and assigns new values.
# Update values in a column based on a condition
df.loc[df['Customer Country'] == 'United States', 'Customer Country'] = 'USA'
It changed the United Stated to USA, in Customer Country column
iloc[ ] : This accessor selects specific rows and columns in the DataFrame
and assigns new values.
# Update values in a column based on a condition
df.iloc[df['Order Quantity'] > 3, 15] = 'greater than 3'
# or
condition = df['Order Quantity'] > 3
df.iloc[condition, 15] = 'greater than 3'
It changed the values greater than 3 in Order Quantity column to “greater than 3” text
replace() : It replaces specific values in a DataFrame with new values.
Ex: df.['column_name'].replace(old_value, new_value, inplace=True)
# Replace specific values in a column
df['Order Quantity'].replace(5, 'equals 5', inplace=True)
It changed the “5” to “equals 5” in Order Quantity column
Conclusion
Python pandas provides several functions and techniques for selecting and
filtering data within a DataFrame.
By mastering these techniques, you’ll be well-equipped to explore and
analyze your data effectively.
Remember, practice makes perfect.
Thank you for reading!
Python Fundamentals
🚀
Thank you for your time and interest! 
💫
You can find even more content at Python Fundamentals 
Python Data Science Data Analysis Data Analytics Data Scientist
Published in Towards Dev
Follow
6.3K Followers · Last published 17 hours ago
A publication for sharing projects, ideas, codes, and new theories.
Written by Python Fundamentals
Following
2.5K Followers · 1.1K Following
Learn Python with new contents every day
No responses yet
What are your thoughts?
Respond
More from Python Fundamentals and Towards Dev
In Python in Plain English by Python Fundamentals In Towards Dev by AshokReddy
Selecting and Filtering Data in Swagger UI is Gone in .NET 9:
Python Pandas: loc and iloc Here’s What You Need to Do Next
Python pandas library provides several Introduction:
methods for selecting and filtering data, suc…
Jan 27 12 Jan 27 66 2
In Towards Dev by Bill WANG Python Fundamentals
Running DeepSeek R1 Locally on 10 Useful Python Pandas Functions
Mac in Two Simple Commands for Data Exploration
Follow up on my DeepSeek blogs about Data exploration and data understanding are
crucial steps to take before diving into data…
Jan 26 79 4 May 4, 2024 20
See all from Python Fundamentals See all from Towards Dev
Recommended from Medium
J. Aashish Kumar
Building a Data Pipeline with 25 Amazing Python Tricks That
Python: A Step-by-Step Guide to… Will Instantly Improve Your Code
Photo by Tudor Baciu on Unsplash
Nov 4, 2024 21 Feb 17 1
Lists
Predictive Modeling w/ Coding & Development
Python
11 stories · 1016 saves
20 stories · 1838 saves
Practical Guides to Machine ChatGPT prompts
Learning
51 stories · 2599 saves
10 stories · 2214 saves
PURRFECT SOFTWARE LIMITED In Stackademic by Khouloud Haddad Amamou
10 Python Libraries for Web Data Analysis with Python Pandas
Scraping That Changed the Game… and Matplotlib
Join Me as I Share the Essential Python 1. Introduction
Libraries That Made Web Scraping a Breeze
Feb 16 10 Jan 30 150 8
In Python in Plain English by Kiran Maan Ime Eti-mfon
Don’t Use This Way to Copy the Data Wrangling with Python
Objects in Python
Merging, Joining, and Concatenating Data
You won’t regret learning this!!!
Feb 17 187 Nov 7, 2024 10 1
See more recommendations