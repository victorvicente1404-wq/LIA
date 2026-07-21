"""
Roteador da Lia - Gerencia IAs com fallback
"""

from ia.chatgpt import ChatGPT
from ia.gemini import Gemini

class Roteador:
    def __init__(self):
        self.chatgpt = ChatGPT()
        self.gemini = Gemini()

    def decidir(self, mensagem: str):
        """Tenta ChatGPT → Gemini → retorna None (para pesquisa)"""

        # Tenta ChatGPT primeiro
        if self.chatgpt:
            try:
                resposta = self.chatgpt.perguntar(mensagem)
                if resposta:
                    return resposta
            except:
                pass

        # Fallback para Gemini
        if self.gemini:
            try:
                resposta = self.gemini.perguntar(mensagem)
                if resposta:
                    return resposta
            except:
                pass

        # Se nenhuma IA responder, retorna None para o assistente usar pesquisa
        return None
