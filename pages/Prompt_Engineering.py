import streamlit as st

from utils.text_generator import generate_text

st.title("Prompt Engineering")

examples = {
    "Simple":
        "Explain gravity",

    "Role Prompt":
        "You are a physics teacher. Explain gravity.",

    "Kid Friendly":
        "Explain gravity to a 10 year old.",

    "Football Example":
        """
        You are a science teacher.

        Explain gravity using football examples.
        """
}

choice = st.selectbox(
    "Select Prompt Style",
    examples.keys()
)

if st.button("Run Prompt"):

    result = generate_text(
        examples[choice]
    )

    st.write(result)