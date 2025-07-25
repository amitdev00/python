import streamlit as st
name = st.text_input("Enter your name: ")

if (st.button("Submit")):
    result = name.title()
    st.success(f"Your name is {result}")
