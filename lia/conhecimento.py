"""
Gerencia os conhecimentos da Lia.
"""

import json
import os
from datetime import datetime


class Conhecimento:

    def __init__(self, memoria=None):

        self.arquivo = "data/conhecimento.json"

        self.conhecimentos = {}

        self.carregar()

    # --------------------------------------------------

    def carregar(self):

        os.makedirs("data", exist_ok=True)

        if os.path.exists(self.arquivo):

            try:

                with open(

                    self.arquivo,

                    "r",

                    encoding="utf-8"

                ) as arquivo:

                    self.conhecimentos = json.load(
                        arquivo
                    )

            except Exception:

                self.conhecimentos = {}

        else:

            self.salvar()

    # --------------------------------------------------

    def salvar(self):

        with open(

            self.arquivo,

            "w",

            encoding="utf-8"

        ) as arquivo:

            json.dump(

                self.conhecimentos,

                arquivo,

                indent=4,

                ensure_ascii=False

            )

    # --------------------------------------------------

    def aprender(

        self,

        objeto,

        descricao,

        fonte="Memória"

    ):

        objeto = objeto.lower().strip()

        if objeto == "" or descricao is None:

            return

        descricao = descricao.strip()

        self.conhecimentos[objeto] = {

            "descricao": descricao,

            "fonte": fonte,

            "data": datetime.now().strftime(

                "%d/%m/%Y %H:%M"

            ),

            "acessos": 0

        }

        self.salvar()

    # --------------------------------------------------

    def consultar(

        self,

        objeto

    ):

        objeto = objeto.lower().strip()

        conhecimento = self.conhecimentos.get(

            objeto

        )

        if conhecimento is None:

            return None

        conhecimento["acessos"] += 1

        self.salvar()

        return conhecimento["descricao"]

    # --------------------------------------------------

    def existe(

        self,

        objeto

    ):

        objeto = objeto.lower().strip()

        return objeto in self.conhecimentos

    # --------------------------------------------------

    def remover(

        self,

        objeto

    ):

        objeto = objeto.lower().strip()

        if objeto in self.conhecimentos:

            del self.conhecimentos[objeto]

            self.salvar()

    # --------------------------------------------------

    def listar(self):

        return list(

            self.conhecimentos.keys()

        )
