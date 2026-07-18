"""
Kernel da Lia - Central de controle da assistente
"""

from .assistente import Assistente


class Kernel:
    """
    Responsável por inicializar e coordenar toda a lógica da Lia.
    """

    def __init__(self):
        self.assistente = Assistente()
        self.iniciado = False

    def iniciar(self):
        """Inicializa o Kernel da Lia."""
        if self.iniciado:
            return

        self.iniciado = True
        print("🧠 Lia Kernel iniciado com sucesso!")

    def responder(self, mensagem: str) -> str:
        """
        Método principal que recebe a mensagem do usuário
        e retorna a resposta da Lia.
        """
        if not mensagem or not mensagem.strip():
            return "Pode falar algo para mim?"

        # Delega a resposta para o Assistente (que contém a lógica + pesquisa)
        return self.assistente.responder(mensagem)
