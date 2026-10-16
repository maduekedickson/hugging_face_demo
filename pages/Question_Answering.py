import streamlit as st

from utils.qa_engine import (
    answer_question
)

st.title("Question Answering")

context = st.text_area(
    "Knowledge Base"
)

question = st.text_input(
    "Question"
)

if st.button("Ask"):

    answer = answer_question(
        context,
        question
    )

    st.success(answer)