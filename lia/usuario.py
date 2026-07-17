"""
Gerenciamento do usuário.

Esta classe representa tudo o que a Lia sabe
sobre o usuário.
"""


class Usuario:

    def __init__(self, memoria):

        self.memoria = memoria

    # -------------------------
    # Nome
    # -------------------------

    def definir_nome(self, nome):

        nome = nome.strip()

        self.memoria.definir_usuario(
            "nome",
            nome
        )

    def obter_nome(self):

        return self.memoria.obter_usuario(
            "nome",
            ""
        )

    # -------------------------
    # Idade
    # -------------------------

    def definir_idade(self, idade):

        self.memoria.definir_usuario(
            "idade",
            idade
        )

    def obter_idade(self):

        return self.memoria.obter_usuario(
            "idade",
            None
        )

    # -------------------------
    # Cidade
    # -------------------------

    def definir_cidade(self, cidade):

        self.memoria.definir_usuario(
            "cidade",
            cidade
        )

    def obter_cidade(self):

        return self.memoria.obter_usuario(
            "cidade",
            ""
        )

    # -------------------------
    # Profissão
    # -------------------------

    def definir_profissao(self, profissao):

        self.memoria.definir_usuario(
            "profissao",
            profissao
        )

    def obter_profissao(self):

        return self.memoria.obter_usuario(
            "profissao",
            ""
        )

    # -------------------------
    # Gostos
    # -------------------------

    def adicionar_gosto(self, gosto):

        gostos = self.memoria.obter_usuario(
            "gostos",
            []
        )

        gosto = gosto.strip()

        if gosto not in gostos:

            gostos.append(gosto)

            self.memoria.definir_usuario(
                "gostos",
                gostos
            )

    def obter_gostos(self):

        return self.memoria.obter_usuario(
            "gostos",
            []
        )

    # -------------------------
    # Preferências
    # -------------------------

    def definir_preferencia(
        self,
        chave,
        valor
    ):

        self.memoria.definir_preferencia(
            chave,
            valor
        )

    def obter_preferencia(
        self,
        chave,
        padrao=None
    ):

        return self.memoria.obter_preferencia(
            chave,
            padrao
        )

    # -------------------------
    # Resumo
    # -------------------------

    def resumo(self):

        return {

            "nome": self.obter_nome(),

            "idade": self.obter_idade(),

            "cidade": self.obter_cidade(),

            "profissao": self.obter_profissao(),

            "gostos": self.obter_gostos()

        }
