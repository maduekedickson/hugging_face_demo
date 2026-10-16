import streamlit as st

from utils.text_generator import generate_text

st.title("Text Generation")

prompt = st.text_area(
    "Enter Prompt"
)

if st.button("Generate"):

    response = generate_text(prompt)

    st.subheader("Result")

    st.write(response)