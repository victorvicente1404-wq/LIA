"""
ChatGPT Integration for Lia
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ChatGPT:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.url = "https://api.openai.com/v1/chat/completions"

    def perguntar(self, mensagem: str):
        if not self.api_key:
            return None  # Deixa o fallback funcionar

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "Você é a Lia, uma assistente amigável e útil. Responda em português."},
                    {"role": "user", "content": mensagem}
                ],
                "max_tokens": 300,
                "temperature": 0.7
            }

            response = requests.post(self.url, headers=headers, json=data, timeout=10)
            
            if response.status_code == 429:
                return "Estou com muitas solicitações agora. Tente novamente em alguns segundos."
            if response.status_code == 401:
                return "Chave OpenAI inválida."

            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()

        except Exception as e:
            print(f"[DEBUG] Erro ChatGPT: {e}")
            return None  # Deixa fallback
