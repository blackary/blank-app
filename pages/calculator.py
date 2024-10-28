import streamlit as st

num1 = st.number_input("num1", value=4)

num2 = st.number_input("num2", value=5)

st.write("num1 + num2 =", num1+num2)