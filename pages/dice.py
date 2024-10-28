import streamlit as st

import random

sides = st.slider("Number of sides", value=6)

st.write(roll_dice(sides))