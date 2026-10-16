from utils.text_generator import generate_text


def answer_question(context, question):
    prompt = (
        "Answer the question using only the context below. "
        "Reply with a short answer only.\n\n"
        f"Context: {context}\n\n"
        f"Question: {question}"
    )
    return generate_text(prompt).strip()
