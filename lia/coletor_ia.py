"""
Coletor de respostas das IAs.

Este módulo consulta todas as IAs configuradas
e devolve uma lista de respostas.
"""

from typing import List


class ColetorIA:

    def __init__(self):

        self.fontes = []

    # -------------------------------------------------

    def registrar(self, funcao):

        self.fontes.append(funcao)

    # -------------------------------------------------

    def coletar(self, pergunta: str) -> List[dict]:

        respostas = []

        for fonte in self.fontes:

            try:

                resultado = fonte(pergunta)

                if resultado:

                    respostas.append(resultado)

            except Exception:

                continue

        return respostas
