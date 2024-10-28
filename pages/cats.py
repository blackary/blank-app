# import pyjokes
import streamlit as st
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/1/")

st.image(response.json()["sprites"]["other"]["showdown"]["front_default"])

# st.write(pyjokes.get_joke())

