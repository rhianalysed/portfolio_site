import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque a leo ac tellus congue fringilla in sit 
amet eros. Integer at vulputate ante. Ut eget facilisis nibh, pharetra laoreet nibh. Integer sed convallis justo. 
Donec sed nisi id urna dignissim scelerisque at id risus. Integer rutrum vehicula urna laoreet congue. Quisque 
aliquet velit vitae orci auctor, ac tempor dui molestie. Mauris porta lectus quis diam egestas vulputate. Aliquam 
porttitor dapibus orci in posuere. """
st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("portfolio_website/data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('portfolio_website/images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('portfolio_website/images/' + row['image'])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('portfolio_website/images/' + row['image'])