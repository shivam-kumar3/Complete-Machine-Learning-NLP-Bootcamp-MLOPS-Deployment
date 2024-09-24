import streamlit as st
import pandas as pd
import numpy as np
# python -m streamlit run app.py

# Title of the application
st.title("Hello Streamlit")

# Display a simple text
st.write("This is a simple text")

# create a simple DF
df = pd.DataFrame({
    "Name" : "Shivam",
    "Age" : 28,
    "Designation" : "Data Scientist",
},index=[0])

# display the dataframe
st.write("Here is the short intro")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["A","B","C"]
)

st.line_chart(chart_data)