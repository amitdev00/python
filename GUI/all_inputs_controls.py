import streamlit as st

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)


if st.checkbox("Show/Hide"):
    st.text("Showing the widget")

status = st.radio("select gender: ", ['Male', 'Female'])

if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobby = st.selectbox("Select a hobby: ", ['Sports', 'Reading', 'Writing', ])
st.write("Your hobby is:", hobby)

hobbies = st.multiselect("Select your hobbies: ", [
                         'Dancing', 'Reading', 'Writing', 'Sports'])
st.write("You selected", len(hobbies), "hobbies")

numbers_slider = st.slider(
    "Select required threshold value between 0 and 100", 0, 100, 10, 2)
st.write("You are on the numeber: ", numbers_slider)

st.image("black-mountain-peaks-minimal-background-m1w23hhf09ln2vor.jpg", caption="Scenery")
