import streamlit as st

def concatenate_name(first_name, last_name):
    return f"{first_name} {last_name}"

st.title("Name concatenator")

first_name = st.text_input("First name: ")
last_name = st.text_input("Last name: ")

if st.button("Concatenate"):
    if first_name and last_name:
        full_name =  concatenate_name(first_name, last_name)
        st.success(f"Full Name: {full_name}")
    else:
        st.error("Please enter both first name and last name.")

