Implementing a Database System
with DuckDB for Local Processing
and MotherDuck for Scalable Cloud
Storage
Jesus L. Monroy · Follow
Published in T3CH · 4 min read · 2 days ago
61
Photo by Growtika on Unsplash
Overview
This project explores how to leverage the strengths of DuckDB and
MotherDuck to build a robust data processing and storage solution. DuckDB
excels at fast in-memory analytics, while MotherDuck provides a scalable
and cost-effective cloud data warehouse. By combining these technologies,
you can achieve optimal performance for both local and cloud-based data
operations.
Environment settings
import polars as pl
import duckdb as db
import glob
Extraction from data sources
- csv files
csv_files = glob.glob('./datasets/*.csv')
list(enumerate(csv_files))
- json files
json_files = glob.glob('./datasets/*.json')
list(enumerate(json_files))
- database tables
db_files = glob.glob('datasets/*.db')
list(enumerate(db_files))
Data warehouse creation
conn = db.connect('my_database.db')
Data warehouse load
conn.sql(f"create or replace table water_collection as 
        select * from '{csv_files[0]}' ")
conn.sql(f"create or replace table contains_null as
        select * from '{csv_files[1]}' ")
conn.sql(f"create or replace table sales_info as
        select * from '{csv_files[2]}' ")
conn.sql(f"create or replace table cdmx_subway as
        select * from '{csv_files[3]}' ")
conn.sql(f"create or replace table airports as
        select * from '{csv_files[4]}' ")
conn.sql(f"create or replace table colors as
        select * from '{csv_files[5]}' ")
conn.sql(f"create or replace table sets as
        select * from '{csv_files[6]}' ")
conn.sql(f"create or replace table appl_stock as
        select * from '{csv_files[7]}' ")
conn.sql(f"create or replace table sales as
        select * from '{csv_files[8]}' ")
conn.sql(f"create or replace table prevalencia as
        select * from '{json_files[0]}' ")
conn.sql(f"create or replace table people as
        select * from '{json_files[1]}' ")
retail = db.connect('./datasets/retail_db.db')
retail.sql('show tables')
retail_sales_pl = retail.sql('select * from retail_sales').pl()
conn.execute("create or replace table retail_sales as from retail_sales_pl");
restaurants = db.connect('./datasets/restaurants.db')
restaurants.sql('show tables')
restaurants_pl = restaurants.sql('select * from restaurants').pl()
conn.execute("create or replace table restaurants as from restaurants_pl");
Data retrieval
conn.sql('show databases')
conn.sql('show tables')
conn.sql('select * from restaurants limit 5').pl()
Cloud Data Warehouse with MotherDuck
dw = db.connect('md')
dw.sql('select current_database()').show()
Convert queries from local database to polars
airports_pl = conn.sql('select * from airports').pl()
appl_stock_pl = conn.sql('select * from appl_stock').pl()
cdmx_subway_pl = conn.sql('select * from cdmx_subway').pl()
colors_pl = conn.sql('select * from colors').pl()
contains_null_pl = conn.sql('select * from contains_null').pl()
people_pl = conn.sql('select * from people').pl()
prevalencia_pl = conn.sql('select * from prevalencia').pl()
restaurants_pl = conn.sql('select * from restaurants').pl()
retail_sales_pl = conn.sql('select * from retail_sales').pl()
sales_pl = conn.sql('select * from sales').pl()
sales_info_pl = conn.sql('select * from sales_info').pl()
sets_pl = conn.sql('select * from sets').pl()
water_collection_pl = conn.sql('select * from water_collection').pl()
Upload dataframes to MotherDuck
dw.sql(f"create or replace table airports as select * from airports_pl");
dw.sql(f"create or replace table appl_stock as
      select * from appl_stock_pl");
dw.sql(f"create or replace table cdmx_subway as
      select * from cdmx_subway_pl");
dw.sql(f"create or replace table colors as select * from colors_pl");
dw.sql(f"create or replace table contains_null as
      select * from contains_null_pl");
dw.sql(f"create or replace table people as select * from people_pl");
dw.sql(f"create or replace table prevalencia as
      select * from prevalencia_pl");
dw.sql(f"create or replace table restaurants as
      select * from restaurants_pl");
dw.sql(f"create or replace table retail_sales as
      select * from retail_sales_pl");
dw.sql(f"create or replace table sales as
      select * from sales_pl");
dw.sql(f"create or replace table sales_info as
      select * from sales_info_pl");
dw.sql(f"create or replace table sets as
      select * from sets_pl");
dw.sql(f"create or replace table water_collection as
      select * from water_collection_pl");
Check uploaded tables
dw.sql('show tables')
Close all database connections
# close db connections
conn.close()
retail.close()
restaurants.close()
dw.close()
Conclusions
By combining DuckDB’s in-memory processing capabilities with MotherDuck’s
cloud-based data warehousing, you can create a powerful and flexible data
processing and storage solution. This approach allows you to efficiently
handle both local and cloud-based data operations, optimize performance,
and scale your data infrastructure as needed.
Open in app
Search Write
Contact
Portfolio | Linkedin | Twitter
Data Science Python Duckdb Motherduck Etl
Published in T3CH
Follow
605 Followers · Last published 22 hours ago
Snoop & Learn about Technology, AI, Hacking, Coding, Software, News, Tools,
Leaks, Bug Bounty, OSINT & Cybersecurity !¡! But, not limited 2, anything that is
Tech Linked…You’ll probably find here ! ;) — Stay ahead with Latest Tech News! ->
You write about? Just ping to join !
Written by Jesus L. Monroy
Follow
56 Followers · 23 Following
Economist & Data Scientist
No responses yet
What are your thoughts?
Respond
More from Jesus L. Monroy and T3CH
In T3CH by Jesus L. Monroy In T3CH by Khaleel Khan
Designing Elegant Tables with Unlock Hidden Secrets: How This
Great Tables and Python Tool Reveals Everything About An…
Great Tables Python is a powerful and Deep-HLR: An Essential Tool for Fraud
versatile library that simplifies the process o… Prevention and OSINT Investigations
Nov 1, 2024 216 Aug 23, 2024 453 14
In T3CH by TRedEye In T3CH by Jesus L. Monroy
Advent of Cyber 2024 {All Tasks Building ETL Pipelines in BigQuery
Update daily} — Tryhackme… with Python
Advent of Cyber 2024 BY ::-> TRedEye In the realm of data analytics, Extract,
Transform, Load (ETL) processes play a…
Dec 3, 2024 356 2 Oct 31, 2024 56
See all from Jesus L. Monroy See all from T3CH
Recommended from Medium
In Python in Plain English by Raphael Schols Tomer Gabay
How to Turn PDF Documents into How to Setup Your Macbook for
Data Tables with Python Data Science in 2025
Learn how to extract data from PDFs and Easy Steps to Get the Best Experience From
structure it into tables Your MacBook as a Data Scientist
Jan 13 180 2 Dec 28, 2024 174 1
Lists
Predictive Modeling w/ Coding & Development
Python
11 stories · 981 saves
20 stories · 1789 saves
Practical Guides to Machine ChatGPT prompts
Learning
51 stories · 2487 saves
10 stories · 2165 saves
Gen. David L. In Stackademic by Mayur Koshti
Python ETL Framework Bonobo: Native Support for Advanced Data
Efficiently Perform Data Extractio… Types in PostgreSQL
Doing ETL (Extract, Transform, Load)? Use Practical Examples of Using PostgreSQL’s
Python’s Bonobo library! It simplifies comple… Advanced Data Types
Dec 31, 2024 24 1 Jan 13 75 1
Hugo Lu Abhilasha Gulhane
™
What dbt  Labs’ acquisition of Data Engineer Topic: Shell
SDF Labs means for the data… Scripting
dbt Labs™’ acquisition of SDF Labs spells Here’s an overview of shell scripting,
trouble for other SQL-Development… important commands, examples, and sampl…
6d ago 97 4 Jan 11 18
See more recommendations