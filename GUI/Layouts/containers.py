import streamlit as st

st.header("Container Example")

with st.container(border= True):
    st.write("This content is inside a container with border.")
    input = st.text_input("Enter text: ")
    st.write(input)
    

long_text = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..." * 50
with st.container(height=200):
    st.markdown(long_text)
