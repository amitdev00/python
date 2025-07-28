import streamlit as st



st.set_page_config(page_title="My Multi-Page App", page_icon="💡")
st.title("Welcome to Streamlit Application")
st.write("Navigate using the sidebar")

if st.button("Page 1"):
    st.switch_page("Python/GUI/Application/Pages1/page1.py")
elif st.button("Page 2"):
    st.switch_page("Pages1/page2.py")