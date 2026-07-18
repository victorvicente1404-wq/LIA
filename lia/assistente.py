"""
Assistente principal da Lia.
"""

from .interpretador import Interpretador
from .memoria import Memoria
from .usuario import Usuario
from .conhecimento import Conhecimento
from .respostas import Respostas
from .pesquisa import Pesquisa


class Assistente:

    def __init__(self):

        self.memoria = Memoria()
        self.usuario = Usuario(self.memoria)
        self.conhecimento = Conhecimento(self.memoria)
        self.interpretador = Interpretador()

    def responder(self, mensagem):

        mensagem = mensagem.strip()

        if mensagem == "":
            return Respostas.vazia()

        comando = self.interpretador.interpretar(mensagem)
        acao = comando["acao"]

        # ----------------------------
        # Cumprimento
        # ----------------------------

        if acao == "CUMPRIMENTO":
            return Respostas.ola()

        # ----------------------------
        # Nome
        # ----------------------------

        if acao == "SALVAR_NOME":

            self.usuario.definir_nome(
                comando["valor"]
            )

            return Respostas.aprendido()

        if acao == "PERGUNTAR_NOME":

            nome = self.usuario.obter_nome()

            if nome == "":
                return Respostas.nao_sei()

            return Respostas.nome(nome)

        # ----------------------------
        # Aprender
        # ----------------------------

        if acao == "APRENDER":

            self.conhecimento.aprender(
                comando["objeto"],
                comando["descricao"]
            )

            return Respostas.aprendido()

       # ----------------------------
       # Consultar
       # ----------------------------

       if acao == "CONSULTAR":

            objeto = comando["objeto"]

            # Procura na memória
            resposta = self.conhecimento.consultar(
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

            # Não encontrou -> pesquisar
            resposta = Pesquisa.pesquisar(
                objeto
            )

            if resposta:

                # Aprende automaticamente
                self.conhecimento.aprender(
                    objeto,
                    resposta
                )

                return Respostas.conhecimento(
                    resposta
                )

            return Respostas.desconhecido()

        # ----------------------------
        # Desconhecido
        # ----------------------------

        return Respostas.nao_entendi()
