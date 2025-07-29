# import streamlit as st

# # Initialize session state
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# # Navigation function
# def go_to_page(page_name):
#     st.session_state.page = page_name

# # Home Page
# if st.session_state.page == "home":
#     st.title("Home Page")
#     st.write("Welcome to the Home Page!")

#     if st.button("Go to Page 2"):
#         go_to_page("page2")

# # Page 2
# elif st.session_state.page == "page2":
#     st.title("Page 2")
#     st.write("This is Page 2 content.")

#     if st.button("Back to Home"):
#         go_to_page("home")


import streamlit  as st

st.set_page_config(page_title= "My Streamlit Application", page_icon=":rocket")

st.title("Welcome to my streamlit app")
st.write("This is a simple streamlit application")

if st.button("Page 1"):
    st.switch_page("Pages/page1.py")
    
elif st.button("Page 2"):
    st.switch_page("Pages/page2.py")