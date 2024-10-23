import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

with open("system_prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read().strip()