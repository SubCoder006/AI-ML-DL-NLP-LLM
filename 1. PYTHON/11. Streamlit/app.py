import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## create a simple dataframe
df = pd.DataFrame({
    'arr1':[1,2,3,4],
    'arr2':[1,4,9,16],
})

## display the dataframe
st.write("Here is the dataframe")
st.write(df)


## create a line chart
chart=pd.DataFrame(
    np.random.randn(20,4),columns=['a','b','c','d']
)
st.bar_chart(chart)