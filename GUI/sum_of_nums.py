import streamlit as st

st.title("Add Two Numbers", )

num1 = st.number_input("Enter first number: ", value = 0.0, step = 1.0)

num2 = st.number_input("Enter second number: ", value = 0.0, step = 1.0)



if st.button("Add"):
    result = num1 + num2
    st.success(f"The sum of {num1} and {num2} is {result}")
elif st.button("Subtract"):
    result = num1 - num2
    st.success(f"The subtraction of {num1} and {num2} is {result}")
elif st.button("Multiply"):
    result = num1 * num2
    st.success(f"The multiplication of {num1} and {num2} is {result}")
elif st.button("Division"):
    result = num1 / num2
    st.success(f"The division of {num1} and {num2} is {result}")
else:
    st.warning("Please enter both numbers")