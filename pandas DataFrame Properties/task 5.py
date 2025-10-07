'''Task 5 – Check Empty & Info
Question:
Create a DataFrame using the given data. Print:
Whether the DataFrame is empty (empty)
Summary information (info())
Data:
{
    'Employee': ['John', 'Sara', 'Mike', 'Anna'],
    'Salary': [55000, 60000, 65000, 62000],
    'Bonus': [5000, 6000, 7000, 6200]
}
'''

import pandas as pd 
data={
    'Employee': ['John', 'Sara', 'Mike', 'Anna'],
    'Salary': [55000, 60000, 65000, 62000],
    'Bonus': [5000, 6000, 7000, 6200]
}
df=pd.DataFrame(data)
print("Is Empty?:",df.empty)
print("Info:\n",df.info())