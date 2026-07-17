"""
Kernel da Lia.

Este módulo coordena toda a assistente.

Nenhum outro módulo deve controlar diretamente
a aplicação. Toda comunicação passa pelo Kernel.
"""

from .assistente import Assistente


class Kernel:

    def __init__(self):

        self.assistente = Assistente()

        self.iniciado = False

    def iniciar(self):

        if self.iniciado:

            return

        self.iniciado = True

    def responder(self, mensagem):

        return self.assistente.responder(
            mensagem
        )
