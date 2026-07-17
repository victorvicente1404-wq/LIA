"""
Kernel da Lia - Central de controle
"""

from .assistente import Assistente
from ia.roteador import Roteador

class Kernel:
    def __init__(self):
        self.assistente = Assistente()
        self.roteador = Roteador()
        self.iniciado = False

    def iniciar(self):
        if self.iniciado:
            return
        self.iniciado = True
        print("🧠 Lia Kernel iniciado com sucesso!")

    def responder(self, mensagem: str) -> str:
        if not mensagem.strip():
            return "Pode falar algo para mim?"

        # Tenta ferramentas externas primeiro
        resposta_externa = self.roteador.decidir(mensagem)
        if resposta_externa:
            return resposta_externa

        # Usa o assistente local
        return self.assistente.responder(mensagem)
