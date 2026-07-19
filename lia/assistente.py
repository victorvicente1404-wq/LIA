"""
Assistente principal da Lia.
"""

from .interpretador import Interpretador
from .memoria import Memoria
from .usuario import Usuario
from .conhecimento import Conhecimento
from .pesquisa import Pesquisa
from .respostas import Respostas


class Assistente:

    def __init__(self):

        self.memoria = Memoria()

        self.usuario = Usuario(
            self.memoria
        )

        self.conhecimento = Conhecimento(
            self.memoria
        )

        self.interpretador = Interpretador()

    # ----------------------------------

    def responder(self, mensagem):

        mensagem = mensagem.strip()

        if not mensagem:

            return Respostas.vazia()

        comando = self.interpretador.interpretar(
            mensagem
        )

        acao = comando.get("acao")

        # ----------------------------------
        # Cumprimento
        # ----------------------------------

        if acao == "CUMPRIMENTO":

            return Respostas.ola()

        # ----------------------------------
        # Nome
        # ----------------------------------

        if acao == "SALVAR_NOME":

            self.usuario.definir_nome(
                comando["valor"]
            )

            return Respostas.aprendido()

        if acao == "PERGUNTAR_NOME":

            nome = self.usuario.obter_nome()

            if nome:

                return Respostas.nome(nome)

            return Respostas.nao_sei()

        # ----------------------------------
        # Aprender
        # ----------------------------------

        if acao == "APRENDER":

            self.conhecimento.aprender(

                comando["objeto"],

                comando["descricao"]

            )

            return Respostas.aprendido()

        # ----------------------------------
        # Consultar
        # ----------------------------------

        if acao == "CONSULTAR":

            objeto = comando["objeto"]

            # Procura no conhecimento

            resposta = self.conhecimento.consultar(
                objeto
            )

            if resposta:

                return Respostas.conhecimento(
                    resposta
                )

            # Pesquisa

            resposta = Pesquisa.pesquisar(
                objeto
            )

            if resposta:

                self.conhecimento.aprender(

                    objeto,

                    resposta

                )

                return Respostas.conhecimento(
                    resposta
                )

            return Respostas.desconhecido()

        # ----------------------------------

        return Respostas.nao_entendi()
