'''Task 4 – Values & Transpose
Question:
Create a DataFrame using the given data. Print:
Values as NumPy array (values)
Transpose of DataFrame (T)

Data:
{
    'Student': ['Ravi', 'Maya', 'Tanu'],
    'Math': [85, 90, 78],
    'Science': [88, 92, 80]
}

Sample Output:
Values:
[['Ravi' 85 88]
 ['Maya' 90 92]
 ['Tanu' 78 80]]
Transpose:
          0     1     2
Student  Ravi  Maya  Tanu
Math       85    90    78
Science    88    92    80'''

import pandas as pd
data={
    'Student': ['Ravi', 'Maya', 'Tanu'],
    'Math': [85, 90, 78],
    'Science': [88, 92, 80]
}
df=pd.DataFrame(data)
print("Values:\n",df.values,'\n')
print("Transpose:\n",df.T)