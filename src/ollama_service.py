import requests
from config import OLLAMA_API_URL, OLLAMA_MODEL, SYSTEM_PROMPT


def chat_with_ollama(user_message):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": OLLAMA_MODEL,
                "messages": messages,
                "stream": False,
                "temperature": 0.8,
                "num_ctx": 8192,
                # "mirostat": 1,
                "num_predict": -2,
            },
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except requests.RequestException as e:
        print(f"Error calling OLLAMA API: {e}")
        return "An error occurred while processing your request."
