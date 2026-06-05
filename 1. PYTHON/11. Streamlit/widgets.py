import streamlit as st
import pandas as pd

st.title("Streamlit text input")
name = st.text_input("Enter your name :")
if name :
    st.write(f"Hello, {name}")

age = st.slider("Select your age :",0,100,20)

options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favorite language:",options)
st.write(f"You selected {choice}.") 

data = {
    "Name": ["John","Jane","Jake","Jill","Thomas"],
    "Age" : [20,22,25,23,24],
    "City":["New York","Los Angeles","Chicago","New York","Los Angeles"]
}

df = pd.DataFrame(data)
st.write(df)
uploaded_file = st.file_uploader("Choose a CSV file.",type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
