"""
Memória permanente da Lia.

Responsável por salvar e carregar informações
do usuário e do conhecimento da assistente.
"""

import json
from pathlib import Path


class Memoria:

    def __init__(self):

        self.arquivo = (
            Path(__file__).parent.parent
            / "data"
            / "memoria.json"
        )

        self.dados = {}

        self.carregar()

    # -------------------------
    # Arquivo
    # -------------------------

    def carregar(self):

        if not self.arquivo.exists():

            self.dados = {

                "usuario": {},

                "conhecimento": {},

                "preferencias": {},

                "historico": []

            }

            self.salvar()

            return

        with open(

            self.arquivo,

            "r",

            encoding="utf-8"

        ) as arquivo:

            self.dados = json.load(

                arquivo

            )

    def salvar(self):

        with open(

            self.arquivo,

            "w",

            encoding="utf-8"

        ) as arquivo:

            json.dump(

                self.dados,

                arquivo,

                indent=4,

                ensure_ascii=False

            )

    # -------------------------
    # Usuário
    # -------------------------

    def definir_usuario(

        self,

        chave,

        valor

    ):

        self.dados["usuario"][

            chave

        ] = valor

        self.salvar()

    def obter_usuario(

        self,

        chave,

        padrao=None

    ):

        return self.dados["usuario"].get(

            chave,

            padrao

        )

    # -------------------------
    # Conhecimento
    # -------------------------

    def aprender(

        self,

        objeto,

        descricao

    ):

        self.dados["conhecimento"][

            objeto.lower()

        ] = descricao

        self.salvar()

    def consultar(

        self,

        objeto

    ):

        return self.dados["conhecimento"].get(

            objeto.lower()

        )

    # -------------------------
    # Preferências
    # -------------------------

    def definir_preferencia(

        self,

        chave,

        valor

    ):

        self.dados["preferencias"][

            chave

        ] = valor

        self.salvar()

    def obter_preferencia(

        self,

        chave,

        padrao=None

    ):

        return self.dados["preferencias"].get(

            chave,

            padrao

        )

    # -------------------------
    # Histórico
    # -------------------------

    def adicionar_historico(

        self,

        autor,

        mensagem

    ):

        self.dados["historico"].append(

            {

                "autor": autor,

                "mensagem": mensagem

            }

        )

        self.salvar()

    def obter_historico(self):

        return self.dados["historico"]
