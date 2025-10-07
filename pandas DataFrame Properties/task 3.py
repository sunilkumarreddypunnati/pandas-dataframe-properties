'''Task 3 – Column Labels & Axes

Question:
Create a DataFrame using the given data. Print:
Column labels (columns)
Row & column labels (axes)
Data:
{
    'Country': ['India', 'USA', 'UK'],
    'Capital': ['Delhi', 'Washington', 'London'],
    'Population': [1390000000, 331000000, 68000000]
}
Sample Output:
Columns: Index(['Country', 'Capital',
 'Population'], dtype='object')
Axes: [RangeIndex(start=0, 
stop=4, step=1),
        Index(['Country', 
        'Capital', 'Population'], dtype='object')]'''
import pandas as pd
data={
    'Country': ['India', 'USA'
                , 'UK', 'Germany'],
    'Capital': ['Delhi', 'Washington'
                , 'London', 'Berlin'],
    'Population': [1390000000, 331000000,
                    68000000, 83000000]
}
df=pd.DataFrame(data)
print("Columns:",df.columns)
print("Axes:",'\n',df.axes)