'''
Pandas

pandas is a powerful data manipulation library in python, widely used for data analysis and data cleaning. it provies two primary dta structures. SERIES and DATAFRAME. 
a SERIES is a one dimentional array like objects, 
while DATAFRAME is two dimensional , size mutable, and potentially hoterogeneous tabular data structure with labeled axes ( rows and columns)
'''

import pandas as pd
# SERIES
data = [1,2,3,4,5]

series = pd.Series(data)

print(series)
print(type(series))

# series from dict
new = {"a":1,"b":2,"c":3} #keys will become the index
index = ['x','y','z']
new1 = pd.Series(new,index=index)

print(new1)

# dataframe from dict
data2 = {"Name":["shivam","shahi","mohan", "rohan"],
         "Age":[25,32,21,23],
         "Dept":["Data Science", "SDE", "Sales","Marketing"]
         }

print(data2)

pd_data = pd.DataFrame(data2)

print(pd_data)

import numpy as np

df = np.array(data2)
print(df)

print(pd_data.loc[1])
'''
Use .loc[] when you want to select data by label.
Use .iloc[] when you want to select data by position.
'''

print(pd_data.loc[0])
print(pd_data.loc[1])
print(pd_data.loc[2])

print(pd_data.iloc[0])
print(pd_data.iloc[1])
print(pd_data.iloc[2])

'''
loc[]:

- Used for label-based indexing.
- It allows you to select rows and columns by their 
- labels (row names or index labels).
- Example: pd_data.loc[0] will select the row with index label 0.


iloc[]:

- Used for integer-based indexing.
- It allows you to select rows and columns by their - - - integer positions (i.e., by their order).
- Example: pd_data.iloc[0] will select the first row (row at position 0).
'''

print(pd_data.at[0,'Name'])

# accessing a specified elemetns using iat

print(pd_data.iat[2,2])

# Data Manipulation with dataframe 

# adding a column
pd_data['Salary'] = [100000,50000,40000,80000]

print(pd_data)

# removing a column

pd_data.drop("Salary", axis = 1, inplace= True)

print(pd_data)

# add age to the column
pd_data['Age'] = pd_data['Age']+1

print(pd_data)

pd_data.drop(0)

