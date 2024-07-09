import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("RhiCoded")
    content = """Hi, welcome to RhiCoded!

I'm excited about my journey transitioning into programming and diving deeper into the tech world. 
Check out my GitHub to see the cool stuff I've been working on, from Excel dashboards to PowerBI visualizations, and Python projects.
I'm all about exploring data and creating solutions with SQL and Python.
    """
    st.write(content)