import httpx
from app.config import settings

class FireworksClient:

    def __init__(self):
        self.base_url = settings.FIREWORKS_BASE_URL.rstrip("/")
        self.api_key = settings.FIREWORKS_API_KEY

    def generate(self, model: str, prompt: str):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.4,
            "max_tokens": 300
        }

        response = httpx.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()