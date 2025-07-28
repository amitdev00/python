import streamlit as st

# Create the tabs and assign them to variables
tab1 , tab2, tab3 = st.tabs(["Tab A", "Tab B", "Tab C"])

# Populate the content of each tab using 'with' statement
with tab1:
    st.header("Content for Tab A")
    st.write("This is some text in Tab A")
    st.button("Click me in Tab A")

with tab2:
    st.header("Content for Tab B")
    st.metric(label= "Temprature", value="25°C", delta="2°C")

with tab3:
    st.header("Content for Tab C")
    st.image("building.jpg")
    
