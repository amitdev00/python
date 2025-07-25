import streamlit as st

st.header("Putting images in columns")

col1, col2, col3 = st.columns([2, 2, 2])
st.set_page_config(layout = "wide")

with col1:
    with st.container(height = 700):
        st.write("Image 1")
        st.image("building.jpg")

with col2:
    with st.container(height = 700):
        st.write("Image 2")
        st.image("goats.jpg")

with col3:
    with st.container(height = 700):
        st.write("Image 3")
        st.image("issomething.jpg")