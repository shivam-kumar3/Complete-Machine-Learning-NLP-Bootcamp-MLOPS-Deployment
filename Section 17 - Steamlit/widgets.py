import streamlit as st
# python -m streamlit run widgets.py
from PIL import Image


st.title("Streamlit text Input")

name = st.text_input("Enter Your name")
if name:
    st.write(f"Hello, {name}")
#slider
age = st.slider("Select your age", 0,100,18)
st.write("Your age is ", age)
# Dropbox
choice = st.selectbox('Choose your fav. Language',["Python", "C", "C++"])
st.write("You selected", choice)


# upload button
uploaded_file = st.file_uploader("Choose as JPG file", type = "jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded File")



