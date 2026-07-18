"""
Integração com DeepSeek - IA alternativa para respostas mais avançadas.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DeepSeek:
    """
    Classe para comunicação com a API da DeepSeek.
    """

    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.url = "https://api.deepseek.com/v1/chat/completions"

    def perguntar(self, mensagem: str, contexto: str = ""):
        """
        Envia uma pergunta para a DeepSeek e retorna a resposta.
        """
        if not self.api_key:
            return "Chave da API DeepSeek não configurada. Use a pesquisa local por enquanto."

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "Você é a Lia, uma assistente amigável, útil e inteligente."
                    },
                    {
                        "role": "user",
                        "content": mensagem
                    }
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }

            response = requests.post(
                self.url,
                headers=headers,
                json=data,
                timeout=20
            )

            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()

        except Exception as e:
            return f"Erro ao consultar DeepSeek: {str(e)[:100]}"
