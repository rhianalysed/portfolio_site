import streamlit as st
import pandas as pd

df = pd.read_csv("portfolio_website/topics.csv")

st.header("Contact Us")

with st.form(key="email_form"):
    st.text_input("Your Email")
    st.selectbox("Select Category", df['topic'].unique())
    st.text_area("Enter Message")
    button = st.form_submit_button()
    if button:
        st.info("Your Email has been sent")
