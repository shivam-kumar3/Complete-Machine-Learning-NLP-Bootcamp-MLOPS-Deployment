'''
Data manipulation and analysis with pandas

data manipulation and analysis are key task in any data science or data analysis projects.
Pandas provides a wide range of functions for data manipulation and analysis, making it easier to clean transform and extract insights from data.
in this lesson, we will cover various data manipulation and analysis techniques using pandas
'''

import pandas as pd

df = pd.read_csv('data.csv', encoding='latin1')
print(df.head())

print(df.tail)

print(df.describe())

print(df.dtypes)

# handling missing values 
print(df.isnull().sum()/df.shape[0]*100)

print(df.shape)

# filling missing values with the mean of the column


# changing the data type to int from float
print(df.dtypes)
df = df.apply(lambda x: x.fillna(0).astype(int) if x.dtype == 'float' else x)

print(df.dtypes)

df['num_voted_users_filled'] = df['num_voted_users'].fillna(df["num_voted_users"].mean())

print(df)