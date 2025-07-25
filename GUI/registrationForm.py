import streamlit as st
import datetime as dt

st.title("Student Registration Form")

fname = st.text_input("First Name")

lname = st.text_input("Last Name")

dob = st.date_input("Date of Birth")

address1 = st.text_area("Address 1")

address2 = st.text_area("Address 2")

city = st.text_input("City")

phone_number = st.number_input("Phone Number")

email = st.text_input("Email")

father_name = st.text_input("Father's Name")

mother_name = st.text_input("Mother's Name")



