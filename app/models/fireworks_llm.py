import requests

from app.config import (
    FIREWORKS_API_KEY,
    FIREWORKS_BASE_URL,
    DEFAULT_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
)


class FireworksLLM:

    def improve_caption(
        self,
        caption: str,
        transcript: str
    ) -> str:

        headers = {
            "Authorization": f"Bearer {FIREWORKS_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": DEFAULT_MODEL,
            "max_tokens": MAX_TOKENS,
            "temperature": TEMPERATURE,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Improve the video caption using the transcript."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Caption: {caption}\n"
                        f"Transcript: {transcript}"
                    ),
                },
            ],
        }

        response = requests.post(
            f"{FIREWORKS_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]


fireworks_llm = FireworksLLM()