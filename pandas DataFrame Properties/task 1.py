'''Task 1 – Shape, Size & Dimensions
Question:
Create a DataFrame using the given data. 
Print:
Shape of the DataFrame
Total number of elements (size)
Number of dimensions (ndim)

Data:
{
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Dept': ['HR', 'IT', 'Finance']
}

Sample Output:
Shape: (3, 3)
Size: 9
Dimensions: 2'''

import pandas as pd
data={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Dept': ['HR', 'IT', 'Finance']
}
df=pd.DataFrame(data)
print("Shape:",df.shape)
print("Size:",df.size)
print("Dimensions:",df.ndim)