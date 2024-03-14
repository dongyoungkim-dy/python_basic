# in the terminal, you will need to install streamlit using pip (already done)
import streamlit as st
import pandas as pd
import time


df = pd.read_csv("dy_lesson_12/titanic_data/train.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Hello world")

with col2:
    name = st.text_input("What is your name?")

with col3:
    st.write(f"Hello {name}")
    st.dataframe(df)



with st.spinner("Loading"):

    time.sleep(5)

    big_number = 99999999
    st.write(f"This is a big number {big_number}")
# You can use ctrl + z to stop it from running