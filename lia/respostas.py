class Respostas:

    # ==========================
    # GERAIS
    # ==========================

    OLA = "Ola!"

    DESPEDIDA = "Ate logo!"

    NAO_ENTENDI = "Nao entendi. Pode explicar melhor?"

    NAO_SEI = "Ainda nao sei isso. Pode me ensinar?"

    APRENDIDO = "Entendido. Vou lembrar disso."

    # ==========================
    # USUARIO
    # ==========================

    @staticmethod
    def nome(nome):

        return f"Seu nome e {nome}."

    @staticmethod
    def jogo_favorito(jogo):

        return f"Seu jogo favorito e {jogo}."

    @staticmethod
    def gosto(gosto):

        return f"Entendi. Vou lembrar que voce gosta de {gosto}."

    # ==========================
    # CONHECIMENTO
    # ==========================

    @staticmethod
    def conhecimento(objeto, descricao):

        return f"{objeto} e {descricao}."

    @staticmethod
    def aprendeu(objeto):

        return f"Aprendi sobre {objeto}."

    # ==========================
    # ERROS
    # ==========================

    @staticmethod
    def desconhecido(objeto):

        return f"Ainda nao sei o que e {objeto}. Pode me ensinar?"
