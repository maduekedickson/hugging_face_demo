import streamlit as st

from utils.image_generator import (
    generate_image
)

st.title("Image Generation")

prompt = st.text_input(
    "Describe Image"
)

if st.button("Create Image"):

    with st.spinner("Generating image (local CPU runs take a few minutes)..."):
        image = generate_image(prompt)

    st.image(
        image,
        use_container_width=True
    )