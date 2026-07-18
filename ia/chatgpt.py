"""
Integração com ChatGPT (OpenAI) para a Lia.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ChatGPT:
    """
    Classe para usar a API da OpenAI (ChatGPT) como fallback
    quando a pesquisa tradicional não for suficiente.
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.url = "https://api.openai.com/v1/chat/completions"
    
    def perguntar(self, mensagem: str, contexto: str = ""):
        """
        Envia uma pergunta para o ChatGPT e retorna a resposta.
        """
        if not self.api_key:
            return "⚠️ Chave da OpenAI não configurada. Adicione OPENAI_API_KEY no arquivo .env"

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system", 
                        "content": "Você é a Lia, uma assistente virtual amigável, útil e divertida."
                    },
                    {
                        "role": "user", 
                        "content": f"{contexto}\n\nPergunta: {mensagem}"
                    }
                ],
                "max_tokens": 400,
                "temperature": 0.7
            }
            
            response = requests.post(
                self.url, 
                headers=headers, 
                json=data, 
                timeout=15
            )
            
            response.raise_for_status()
            
            return response.json()["choices"][0]["message"]["content"].strip()
            
        except Exception as e:
            return f"⚠️ Erro ao consultar ChatGPT: {str(e)[:100]}"

    def esta_configurado(self):
        """Verifica se a API Key está configurada."""
        return bool(self.api_key)
