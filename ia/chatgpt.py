# LIA-main/ia/chatgpt.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ChatGPT:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.url = "https://api.openai.com/v1/chat/completions"
    
    def perguntar(self, mensagem: str, contexto=""):
        if not self.api_key:
            return "Chave da OpenAI não configurada."
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "Você é a Lia, uma assistente amigável e útil."},
                    {"role": "user", "content": mensagem}
                ],
                "max_tokens": 300,
                "temperature": 0.7
            }
            
            response = requests.post(self.url, headers=headers, json=data, timeout=15)
            response.raise_for_status()
            
            return response.json()["choices"][0]["message"]["content"].strip()
            
        except Exception as e:
            return f"Erro ao consultar ChatGPT: {str(e)}"
