import streamlit as st

st.title("🐚 Welcome to Zergei Junior High!")

"""
We are so excited to have you joining us this year! Before you can be officially enrolled, 
we need to collect some information from you:
* Your full name
* Your age
* Your date of birth
* A photo for your official ID
* Which sports you have played so far
* Your favorite color
* Have you been on your official school visit yet?
"""

# EXAMPLE INPUT
full_name = st.text_input("What is your full name?")


# EXAMPLE OUTPUT
st.subheader("Student info")
st.write("Full name:", full_name)
st.write("Age:", )

