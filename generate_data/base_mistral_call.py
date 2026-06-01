import os
from mistralai.async_client import MistralAsyncClient
from mistralai.models.chat_completion import ChatMessage
from global_variables import MISTRAL_DEFAULT_MODEL
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

# Pobranie klucza
api_key = os.environ.get("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("Nie znaleziono MISTRAL_API_KEY. Upewnij się, że plik .env istnieje i zawiera ten klucz.")

# Inicjalizacja klienta
client = MistralAsyncClient(api_key=api_key)


class MistralRequest:
    def __init__(self, max_tokens=1000, temperature=1.0):
        self.model = MISTRAL_DEFAULT_MODEL
        self.max_tokens = max_tokens
        self.temperature = temperature

    async def request(self, messages) -> str:
        mistral_messages = [ChatMessage(role=m["role"], content=m["content"]) for m in messages]
        response = await client.chat(
            model=self.model,
            messages=mistral_messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response.choices[0].message.content