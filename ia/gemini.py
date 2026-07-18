"""
Integração com o Gemini (Google AI)
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Gemini:
    """
    Classe para comunicação com o modelo Gemini do Google.
    """

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"

    def perguntar(self, mensagem: str, contexto: str = ""):
        """
        Envia uma pergunta para o Gemini e retorna a resposta.
        """
        if not self.api_key:
            return "Chave da API do Gemini não configurada."

        try:
            headers = {
                "Content-Type": "application/json"
            }

            # Prompt mais natural
            prompt = f"{contexto}\n\nUsuário: {mensagem}\nLia:"

            data = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 400,
                }
            }

            response = requests.post(self.url, headers=headers, json=data, timeout=15)
            
            if response.status_code != 200:
                return f"Erro na API Gemini: {response.status_code}"

            resultado = response.json()
            
            try:
                texto = resultado["candidates"][0]["content"]["parts"][0]["text"]
                return texto.strip()
            except (KeyError, IndexError):
                return "Não consegui gerar uma resposta do Gemini."

        except Exception as e:
            return f"Erro ao consultar Gemini: {str(e)[:100]}"
