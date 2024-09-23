import streamlit as st

def what_type_is_it(thing):
    st.write(f"value = `{thing}`")
    st.write(f"data type = `{type(thing).__name__}`")
    st.divider()

x = st.button("Press me")

what_type_is_it(x)

y = st.checkbox("Check me")

what_type_is_it(y)

z = st.number_input("Enter something")

what_type_is_it(z)

a = st.number_input("Enter something", value=3)

what_type_is_it(a)

b = st.text_input("Enter something", value="Hi")

what_type_is_it(b)

c = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

what_type_is_it(c)

st.write("""
Your assignment:
         
Go to https://docs.streamlit.io/develop/api-reference/widgets
         
Pick two more input widgets and add them to this page, and see what 
types of variable comes out of each one.
         
Hint: use `what_type_is_it()`
""")