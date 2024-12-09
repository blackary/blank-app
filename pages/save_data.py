import streamlit as st

from sqlitedict import SqliteDict

def save_data(name, data):
    with SqliteDict("example.sqlite", autocommit=True) as db:
        db[name] = data

def get_data(name):
    with SqliteDict("example.sqlite") as db:
        return db[name]


name = st.text_input("Data name")

numbers = st.data_editor([1, 2, 3, 4, 5], num_rows='dynamic')

if st.button("Save"):
    save_data(name, numbers)
    st.toast(f"Data saved to `{name}`")

if st.button("Load"):
    st.toast(f"Loading data `{name}`")
    st.write(get_data(name))