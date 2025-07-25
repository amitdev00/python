import streamlit as st

st.header("Image in Containers")


with st.container(border= True):
    st.write("Image 1")
    st.image("goats.jpg")
    
with st.container(border=True):
    st.write("Image 2")
    st.image("issomething.jpg")