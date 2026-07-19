"""
Sistema de aprendizado da Lia.
"""

from .conhecimento import Conhecimento


class Aprendizado:

    def __init__(self):

        self.conhecimento = Conhecimento()


    # ---------------------------------

    def aprender(self, assunto, informacao):

        if not assunto:

            return False


        if not informacao:

            return False


        assunto = assunto.lower().strip()


        self.conhecimento.aprender(

            assunto,

            informacao

        )


        return True


    # ---------------------------------

    def ja_sabe(self, assunto):

        resposta = self.conhecimento.consultar(

            assunto

        )


        if resposta:

            return True


        return False


    # ---------------------------------

    def obter_aprendizado(self, assunto):

        return self.conhecimento.consultar(

            assunto

        )
