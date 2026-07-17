class Respostas:

    @staticmethod
    def criar(texto, emocao="normal"):

        return {
            "texto": texto,
            "emocao": emocao
        }

    @staticmethod
    def ola():

        return Respostas.criar(
            "Ola!",
            "feliz"
        )

    @staticmethod
    def aprendido():

        return Respostas.criar(
            "Entendido. Vou lembrar disso.",
            "feliz"
        )

    @staticmethod
    def nao_entendi():

        return Respostas.criar(
            "Nao entendi. Pode explicar melhor.",
            "confuso"
        )

    @staticmethod
    def nao_sei():

        return Respostas.criar(
            "Ainda nao sei isso.",
            "pensando"
        )

    @staticmethod
    def nome(nome):

        return Respostas.criar(
            f"Seu nome e {nome}.",
            "feliz"
        )

    @staticmethod
    def jogo(jogo):

        return Respostas.criar(
            f"Seu jogo favorito e {jogo}.",
            "feliz"
        )

    @staticmethod
    def conhecimento(objeto, descricao):

        return Respostas.criar(
            f"{objeto} e {descricao}.",
            "normal"
        )

    @staticmethod
    def desconhecido(objeto):

        return Respostas.criar(
            f"Ainda nao sei o que e {objeto}.",
            "pensando"
        )
