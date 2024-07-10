import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("RhiCoded")
    content = """Hi, welcome to RhiCoded!

I'm excited about my journey transitioning into programming and diving deeper into the tech world. 

Please feel free to have a look at some apps I have created using Python
    """
    st.write(content)

content2 = "Below find some apps I have coded in Python:"
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].itterows():
        st.header(row['title'])