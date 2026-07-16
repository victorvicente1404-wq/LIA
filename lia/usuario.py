class Usuario:

    def __init__(self, memoria):

        self.memoria = memoria

    # ==========================
    # NOME
    # ==========================

    def definir_nome(self, nome):

        nome = nome.strip()

        if not nome:
            return False

        self.memoria.guardar_nome(nome)

        return True

    def obter_nome(self):

        return self.memoria.ler_nome()

    def possui_nome(self):

        return self.obter_nome() != ""

    # ==========================
    # JOGO FAVORITO
    # ==========================

    def definir_jogo_favorito(self, jogo):

        jogo = jogo.strip()

        if not jogo:
            return False

        self.memoria.guardar_jogo_favorito(jogo)

        return True

    def obter_jogo_favorito(self):

        return self.memoria.ler_jogo_favorito()

    # ==========================
    # GOSTOS
    # ==========================

    def adicionar_gosto(self, gosto):

        gosto = gosto.strip()

        if not gosto:
            return False

        self.memoria.adicionar_gosto(gosto)

        return True

    def obter_gostos(self):

        return self.memoria.ler_gostos()

    def gosta_de(self, item):

        item = item.strip().lower()

        gostos = self.obter_gostos()

        return item in [g.lower() for g in gostos]
