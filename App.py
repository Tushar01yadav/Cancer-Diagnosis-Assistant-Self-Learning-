import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Add a subtitle
st.subheader("This is a basic example")

# Text input
name = st.text_input("Enter your name")

# Number input
number = st.number_input("Enter a number", min_value=0)

# Button
if st.button("Submit"):
    st.success(f"Hello {name}! You entered the number {number}.")
    st.info(f"Double of your number is: {number * 2}")
