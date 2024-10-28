# import pyjokes
import streamlit as st
import requests

number = st.slider("Pick a pokemon", 1, 122)
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}/")

st.image(response.json()["sprites"]["other"]["showdown"]["front_default"])

# st.write(pyjokes.get_joke())

