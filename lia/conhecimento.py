"""
Sistema de conhecimento da Lia.

Este módulo controla tudo o que a Lia aprende.
No futuro ele também será responsável por
pesquisar na internet, consultar outras IAs
e validar informações.
"""


class Conhecimento:

    def __init__(self, memoria):

        self.memoria = memoria

    # -------------------------
    # Aprender
    # -------------------------

    def aprender(

        self,

        objeto,

        descricao

    ):

        objeto = objeto.strip().lower()

        descricao = descricao.strip()

        self.memoria.aprender(

            objeto,

            descricao

        )

    # -------------------------
    # Consultar
    # -------------------------

    def consultar(

        self,

        objeto

    ):

        objeto = objeto.strip().lower()

        return self.memoria.consultar(

            objeto

        )

    # -------------------------
    # Verificar
    # -------------------------

    def existe(

        self,

        objeto

    ):

        return (

            self.consultar(objeto)

            is not None

        )

    # -------------------------
    # Atualizar
    # -------------------------

    def atualizar(

        self,

        objeto,

        descricao

    ):

        self.aprender(

            objeto,

            descricao

        )

    # -------------------------
    # Remover
    # -------------------------

    def remover(

        self,

        objeto

    ):

        objeto = objeto.strip().lower()

        conhecimento = self.memoria.dados.get(

            "conhecimento",

            {}

        )

        if objeto in conhecimento:

            del conhecimento[objeto]

            self.memoria.salvar()

            return True

        return False

    # -------------------------
    # Listar
    # -------------------------

    def listar(self):

        return self.memoria.dados.get(

            "conhecimento",

            {}

        )

    # -------------------------
    # Quantidade
    # -------------------------

    def quantidade(self):

        return len(

            self.listar()

        )
