from .interpretador import Interpretador
from .memoria import Memoria
from .usuario import Usuario
from .conhecimento import Conhecimento
from .respostas import Respostas


class Lia:

    def __init__(self):

        self.interpretador = Interpretador()

        self.memoria = Memoria()

        self.usuario = Usuario(self.memoria)

        self.conhecimento = Conhecimento(self.memoria)

    def responder(self, mensagem):

        resultado = self.interpretador.interpretar(
            mensagem
        )

        acao = resultado["acao"]

        # ==========================
        # NOME
        # ==========================

        if acao == "SALVAR_NOME":

            self.usuario.definir_nome(
                resultado["nome"]
            )

            return Respostas.APRENDIDO

        if acao == "RESPONDER_NOME":

            nome = self.usuario.obter_nome()

            if nome == "":

                return Respostas.NAO_SEI

            return Respostas.nome(nome)

        # ==========================
        # JOGO FAVORITO
        # ==========================

        if acao == "SALVAR_JOGO":

            self.usuario.definir_jogo_favorito(
                resultado["jogo"]
            )

            return Respostas.APRENDIDO

        if acao == "RESPONDER_JOGO":

            jogo = self.usuario.obter_jogo_favorito()

            if jogo == "":

                return Respostas.NAO_SEI

            return Respostas.jogo_favorito(
                jogo
            )

        # ==========================
        # GOSTOS
        # ==========================

        if acao == "SALVAR_GOSTO":

            self.usuario.adicionar_gosto(
                resultado["gosto"]
            )

            return Respostas.APRENDIDO

        # ==========================
        # APRENDER
        # ==========================

        if acao == "APRENDER":

            self.conhecimento.aprender(

                resultado["objeto"],

                resultado["descricao"]

            )

            return Respostas.aprendeu(

                resultado["objeto"]

            )

        # ==========================
        # CONSULTAR
        # ==========================

        if acao == "CONSULTAR":

            resposta = self.conhecimento.consultar(

                resultado["objeto"]

            )

            if resposta is None:

                return Respostas.desconhecido(

                    resultado["objeto"]

                )

            return Respostas.conhecimento(

                resultado["objeto"],

                resposta

            )

        # ==========================
        # DESCONHECIDO
        # ==========================

        return Respostas.NAO_ENTENDI
