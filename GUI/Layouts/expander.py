import streamlit as st

st.header("Expander")

with st.expander("click to reveal more information"):
    st.write("The content is hidden until expander is clicked.")
    st.image("building.jpg", caption = "Building")