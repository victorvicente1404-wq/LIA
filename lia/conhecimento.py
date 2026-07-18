"""
Gerencia os conhecimentos da Lia.
"""

import json
import os


class Conhecimento:

    def __init__(self, memoria=None):

        # Caminho corrigido para a pasta data
        self.arquivo = "data/conhecimento.json"

        self.conhecimentos = {}

        self.carregar()

    # -------------------------

    def carregar(self):

        if os.path.exists(self.arquivo):

            with open(
                self.arquivo,
                "r",
                encoding="utf-8"
            ) as arquivo:

                self.conhecimentos = json.load(arquivo)

        else:
            self.salvar()

    # -------------------------

    def salvar(self):

        # Garante que a pasta data existe
        os.makedirs("data", exist_ok=True)

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

    # -------------------------

    def aprender(self, objeto, descricao):

        objeto = objeto.lower().strip()
        self.conhecimentos[objeto] = descricao
        self.salvar()

    # -------------------------

    def consultar(self, objeto):

        objeto = objeto.lower().strip()
        return self.conhecimentos.get(objeto)
