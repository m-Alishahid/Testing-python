import streamlit as st

# Title of the app
st.title("🚀 Welcome to My First Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Button to display greeting
if st.button("Greet Me!"):
    st.write(f"Hello, {name}! 🎉")

# Number input and calculation
num = st.number_input("Enter a number:", min_value=1, step=1)
st.write(f"Square of {num} is {num**2}")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv"])
if uploaded_file:
    st.write("Uploaded File Name:", uploaded_file.name)