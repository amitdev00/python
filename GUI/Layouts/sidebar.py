import streamlit as st

st.title("My Streamlit App")

with st.sidebar:
    st.header("Sidebar Controls")

    user_name = st.text_input("Enter your name: ")

    selected_option = st.selectbox(
        "Choose an option: ", 
        ("Option A", "Option B", "Option C")
    )

    show_details = st.checkbox("Show details")

if user_name:
    st.write(f"Hello! {user_name}")

st.write(f"You selected: {selected_option}")

if show_details:
    st.write("Here are some additional details about your selection")