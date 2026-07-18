"""
Integração com o Claude (Anthropic)
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Claude:
    """
    Classe para comunicação com o modelo Claude da Anthropic.
    """

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.url = "https://api.anthropic.com/v1/messages"

    def perguntar(self, mensagem: str, contexto: str = ""):
        """
        Envia uma pergunta para o Claude e retorna a resposta.
        """
        if not self.api_key:
            return "Chave da Anthropic (Claude) não configurada."

        try:
            headers = {
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json"
            }

            data = {
                "model": "claude-3-haiku-20240307",  # ou claude-3-sonnet-20240229
                "max_tokens": 500,
                "temperature": 0.7,
                "messages": [
                    {
                        "role": "user",
                        "content": f"{contexto}\n\nPergunta: {mensagem}"
                    }
                ]
            }

            response = requests.post(
                self.url,
                headers=headers,
                json=data,
                timeout=20
            )

            response.raise_for_status()
            resultado = response.json()

            return resultado["content"][0]["text"].strip()

        except Exception as e:
            return f"Erro ao consultar Claude: {str(e)[:100]}"
