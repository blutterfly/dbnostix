# Advanced Techniques

Advanced Pandas Techniques for Data Processing and Performance

### 1. Data chunking
There are often scenarios we encounter where the size of the data is more
than the available memory (RAM) we have. In such cases, it’s a good idea to
read data in chunks from the file so that the system doesn’t run out of
memory.

~~~python
1 # Initialize an empty list to store the chunks
2 private_rooms = []
3
4 # Read the CSV file in chunks
5 for chunk in pd.read_csv('data/listings.csv', chunksize=1000):
6     # Process each chunk (for example, filter listings where room_type is "Private room")
7     processed_chunk = chunk[chunk["room_type"] == "Private room"]
8     
9     # Append the processed chunk to the list
10     private_rooms.append(processed_chunk)
11
12 # Combine all processed chunks into a dataframe
13 private_rooms = pd.concat(private_rooms)
~~~

### 2. Progress bar
Pandas’ apply() functions, which are commonly used to perform element-
wise operations on DataFrame columns or rows.

~~~python
1 import time
2 from datetime import datetime
3
4 from tqdm import tqdm
5 tqdm.pandas()  # add this to integrate progress bar functionality to pandas
6
7
8 def convert_to_datetime(date):
9     # return date if type of date is not string
10     if type(date) != str:
11         return date
12     
13     # time.sleep() added to demonstrate the progress bar more effectively 
14     time.sleep(0.1)
15
16     # returns a datetime object
17     return datetime.strptime(date, "%Y-%m-%d")
18
19 private_rooms["last_review"] = private_rooms["last_review"].progress_apply(convert_to_datetime)
~~~

### 3. Populate Multiple Columns

Solution: apply() with result_type="expand"

~~~python
1 def get_date_and_month_name(last_review_date):
2     # returns the day and month
3     return last_review_date.day_name(), last_review_date.month_name()
4
5
6 private_rooms[["Day", "Month"]] = private_rooms.apply(
7     lambda x : get_date_and_month_name(x["last_review"]),
8     axis=1,
9     result_type="expand"
10 )
~~~



### 4. Parallel Processing

Use multiprocessing module.  (using np.array_split()) into multiple chunks (depending on the number of
cores available in your system)
Once the chunks are processed and the desired output for each chunk is
obtained, it can be concatenated back to a single DataFrame.


~~~python
1 import time
2 import random
3 from multiprocessing import Pool
4
5 import numpy as np
6 import pandas as pd
7 from tqdm import tqdm
8
9 tqdm.pandas()
10
11
12 def predict_sentiment(review):
13     time.sleep(0.1)  # simulating time taken by prediction model
14     return "Positive" if random.randint(1,10) > 5 else "Negative"
15
16
17 def batch_predict_sentiment(review_df):
18     review_df["sentiment"] = review_df["comments"].progress_apply(predict_sentiment)
19     return review_df
20
21
22 def fetch_sentiment_for_review():
23     n_cores = 64
24     reviews = pd.read_csv("data/reviews.csv")
25     review_batches = np.array_split(reviews, n_cores)  # split into same number of batches as n_c
26     
27     # Processing Parallely
28     with Pool(n_cores) as pool:
29         sentiment_prediction_batches = pool.map(batch_predict_sentiment, review_batches)
30
31     # Once all the batches are processed, concatenate list of DataFrames into a single DataFrame
32     sentiment_prediction = pd.concat(sentiment_prediction_batches)
33     return sentiment_prediction
34
35
36 reviews_with_sentiment = fetch_sentiment_for_review()
~~~

From more than 13 hours to less than 13 minutes!
Each batch consists of 7521 reviews and there are a total of 64 batches. In
this scenario

Tip: set n_cores more than the actual number of cores my system has. 
This is because during the execution of time.sleep(0.1) the
CPU remains idle and each process interleaves for other process to execute.
If your process is CPU intensive, it is recommended to keep n_cores less
than the actual number of cores your system has.

### 5. Complex Merging

Merging is quite a common operation performed by individuals who deal
with data. However, sometimes it can get quite complicated to understand if
any particular data points were lost during the merging process. It might be
due to a plethora of reasons — the worst one being, malformed or faulty
data.

The indicator=True.  When enabled it creates a new column named _merge which can
denote three different scenarios based on the type of merge operation
performed.

+ left_only — indicates that the row’s key only exists in the left DataFrame
and it couldn’t find a match in the right DataFrame
+ right_only — indicates that the row’s key only exists in the right
+ both — indicates that the row’s key exists in both the DataFrames and data

~~~python
merged_df = listings.merge(
    reviews,
    left_on="id",
    right_on="listing_id",
    how="outer",
    indicator=True
)
merged_df.shape
~~~

## 6. Data Segmentation
pd.cut() is a powerful function that can be used when you need to segment
data into multiple bins. It can also act as a way to convert continuous values
into categorical values.
One such scenario is demonstrated in the example below. We will be
Segmenting the price of each listing into multiple price brackets (bins).
We can set a predetermined number of price brackets — “$0 — $100”, “$101 —
$250”, “$251 — $500”, “$500 — $1000”, and “$1000+”.

Create bins and label for each bin
~~~python
bins = [0, 100, 250, 500, 1000, float('inf')]
labels = ["$0 - $100", "$101 - $250", "$251 - $500", "$500 - $1000", "$1000+"]
listings["price_bucket"] = pd.cut(listings["price"], bins=bins, labels=labels)
~~~

Please note here that the number of labels (5) is less than number of bins (6)
by one. This is because the initial two values in the bin belong to the first
label.


## 7. Cross-Tabulation Analysis
Using the above data, we can go one step further and perform a cross-
tabulation between the price brackets and room types available for those
price brackets.
Here’s where pd.crosstab() comes into play. It can be used to perform a
simple cross-tabulation between price_bucket and room_type.

~~~python
room_type_breakup = pd.crosstab(
    listings["price_bucket"],
    listings["room_type"],
    margins=True  # This will add the row and column totals
)
~~~
