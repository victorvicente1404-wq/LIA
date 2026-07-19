"""
Sistema de aprendizado da Lia.
"""

from .conhecimento import Conhecimento


class Aprendizado:

    def __init__(self):

        self.conhecimento = Conhecimento()

    # ---------------------------------

    def aprender(self, assunto, resposta):

        assunto = assunto.lower().strip()

        if assunto == "":
            return False

        if resposta is None:
            return False

        resposta = resposta.strip()

        if resposta == "":
            return False

        # Evita salvar repetido
        existente = self.conhecimento.consultar(
            assunto
        )

        if existente:

            return False

        self.conhecimento.aprender(
            assunto,
            resposta
        )

        return True

    # ---------------------------------

    def consultar(self, assunto):

        return self.conhecimento.consultar(
            assunto
        )
