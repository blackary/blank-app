# import pyjokes
import streamlit as st
import requests

def get_pokemon(num):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}/")

    st.image(response.json()["sprites"]["other"]["showdown"]["front_default"], width=200)

number = st.slider("Pick a pokemon", 1, 122)

get_pokemon(number)


# st.write(pyjokes.get_joke())

