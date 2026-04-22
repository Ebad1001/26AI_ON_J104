# !python -m streamlit run file.py

import streamlit as st

def incr():
    global temp_counter
    temp_counter += 1
    st.session_state.perm_counter += 1

st.button("Increment", on_click=incr)

temp_counter = 0
st.write(f"TEMP = {temp_counter}")

if "perm_counter" not in st.session_state:
    st.session_state.perm_counter = 0
st.write(f"PERM = {st.session_state.perm_counter}")