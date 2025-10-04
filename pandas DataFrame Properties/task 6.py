'''Task 6 – Combined Properties

Question:
Create a DataFrame using the given data. Print:

Shape
Columns
Values
Data types

Data:

{
    'City': ['Mumbai', 'Chennai', 'Kolkata'],
    'State': ['Maharashtra', 'Tamil Nadu', 'West Bengal'],
    'Population_million': [20, 10, 14]
}
'''

import pandas as pd
data={
    'City': ['Mumbai', 'Chennai', 'Kolkata'],
    'State': ['Maharashtra', 'Tamil Nadu', 'West Bengal'],
    'Population_million': [20, 10, 14]
}
df=pd.DataFrame(data)
print("Shape:",df.shape,'\n')
print("Columns:",df.columns,'\n')
print("Values:\n",df.values,'\n')
print("DataTypes:\n",df.dtypes,'\n')