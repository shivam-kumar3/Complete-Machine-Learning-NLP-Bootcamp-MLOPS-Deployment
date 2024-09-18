# Reading data from different sources

import pandas as pd 
from io import StringIO
data = '{"Employee_name" :"Shivam","email":"shivam@gmail.com","Job profile":[{"Title":"teamLead", "title2" : "Sr. Developer"}]}'

print(data)

df = pd.read_json(data)
print(df)