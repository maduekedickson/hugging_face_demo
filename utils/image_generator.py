from functools import lru_cache

import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import InferenceClient

from utils.config import HF_TOKEN, USE_API

LOCAL_MODEL = "segmind/tiny-sd"
API_MODEL = "stabilityai/stable-diffusion-3-medium-diffusers"


@lru_cache(maxsize=1)
def _local_pipeline():
    return StableDiffusionPipeline.from_pretrained(
        LOCAL_MODEL, dtype=torch.float32
    ).to("cpu")


def generate_image(prompt):
    if USE_API:
        client = InferenceClient(provider="hf-inference", token=HF_TOKEN)
        return client.text_to_image(prompt, model=API_MODEL)

    return _local_pipeline()(
        prompt,
        num_inference_steps=15,
        guidance_scale=7.0,
    ).images[0]
