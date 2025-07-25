import streamlit as st

st.header("Columns Example")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Content in column1")
    st.button("Button1")

with col2:
    st.write("Content in column2")
    st.checkbox("Checkbox2")

with col3:
    st.write("Content in column3")
    st.slider("Slider 3", 0, 10)