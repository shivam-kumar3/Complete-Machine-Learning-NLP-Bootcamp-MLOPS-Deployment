# Reading data from different sources

import pandas as pd 
from io import StringIO
data = '{"Employee_name" :"Shivam","email":"shivam@gmail.com","Job profile":[{"Title":"teamLead", "title2" : "Sr. Developer"}]}'

print(data)



# reading json file
df = pd.read_json(data)
print(df)

# reading html file

url = 'https://www.fdic.gov/bank-failures/failed-bank-list'

df = pd.read_html(url)

print(df)


# reading excel file 
df2 = pd.read_excel("NEW.xlsx")

print(df2)


# converting a pickle file
df2.to_pickle('df2')

pd.read_pickle('df2')