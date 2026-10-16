import os

from dotenv import load_dotenv

load_dotenv()

USE_API = os.getenv("USE_API", "false").lower() == "true"
HF_TOKEN = os.getenv("HF_TOKEN")
