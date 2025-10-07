'''Task 2 – Column Data Types & Index
Question:
Create a DataFrame using the given data. Print:
Column data types (dtypes)
Row index (index)

Data:
{
    'Product': ['Laptop', 'Tablet', 'Mobile'],
    'Price': [60000, 30000, 15000],
    'InStock': [True, True, False]
}

Sample Output:

Data Types:
Product     object
Price        int64
InStock       bool
dtype: object

Index: RangeIndex(start=0, stop=3, step=1)'''

import pandas as pd
data={
    'Product': ['Laptop', 'Tablet', 'Mobile'],
    'Price': [60000, 30000, 15000],
    'InStock': [True, True, False]
}
df=pd.DataFrame(data)
print("Data Types:",df.dtypes)
print("Index:",df.index)