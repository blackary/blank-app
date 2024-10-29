# import pyjokes
import streamlit as st
import requests

def get_pokemon(num):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}/")
    data = response.json()
    st.title(data["name"])

    st.image(data["sprites"]["other"]["showdown"]["front_shiny"], width=200)
    st.image(data["sprites"]["other"]["showdown"]["back_shiny"], width=200)

number = st.slider("Pick a pokemon", 1, 122)

get_pokemon(number)


# st.write(pyjokes.get_joke())

