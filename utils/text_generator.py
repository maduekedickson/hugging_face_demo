from functools import lru_cache

from huggingface_hub import InferenceClient
from transformers import pipeline

from utils.config import HF_TOKEN, USE_API

LOCAL_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
API_MODEL = "Qwen/Qwen2.5-7B-Instruct"


@lru_cache(maxsize=1)
def _local_pipeline():
    return pipeline("text-generation", model=LOCAL_MODEL)


def generate_text(prompt):
    messages = [{"role": "user", "content": prompt}]

    if USE_API:
        client = InferenceClient(provider="auto", token=HF_TOKEN)
        response = client.chat_completion(
            messages=messages,
            model=API_MODEL,
            max_tokens=150,
            temperature=0.9,
        )
        return response.choices[0].message.content

    output = _local_pipeline()(
        messages,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.9,
    )
    return output[0]["generated_text"][-1]["content"]
