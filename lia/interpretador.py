"""
Interpretador da Lia.
"""

import re


class Interpretador:

    def interpretar(self, frase):

        frase = frase.strip()

        frase_lower = frase.lower()

        # -------------------------
        # Cumprimento
        # -------------------------

        if frase_lower in [

            "oi",

            "olá",

            "ola",

            "e ai",

            "e aí",

            "bom dia",

            "boa tarde",

            "boa noite"

        ]:

            return {

                "acao": "CUMPRIMENTO"

            }

        # -------------------------
        # Meu nome é...
        # -------------------------

        if frase_lower.startswith("meu nome é "):

            return {

                "acao": "SALVAR_NOME",

                "valor": frase[11:].strip()

            }

        # -------------------------

        if frase_lower.startswith("meu nome e "):

            return {

                "acao": "SALVAR_NOME",

                "valor": frase[11:].strip()

            }

        # -------------------------

        if frase_lower in [

            "qual meu nome",

            "como eu me chamo"

        ]:

            return {

                "acao": "PERGUNTAR_NOME"

            }

        # -------------------------
        # Aprender
        # -------------------------

        if frase_lower.startswith("aprenda que "):

            texto = frase[12:]

            partes = re.split(

                r"\s+é\s+|\s+e\s+",

                texto,

                maxsplit=1,

                flags=re.IGNORECASE

            )

            if len(partes) == 2:

                return {

                    "acao": "APRENDER",

                    "objeto": partes[0].strip().lower(),

                    "descricao": partes[1].strip()

                }

        # -------------------------
        # Consultar
        # -------------------------

        consultas = [

            "o que é ",

            "o que e ",

            "quem é ",

            "quem e ",

            "qual é ",

            "qual e "

        ]

        for inicio in consultas:

            if frase_lower.startswith(inicio):

                objeto = frase_lower[len(inicio):]

                objeto = objeto.replace("?", "").strip()

                return {

                    "acao": "CONSULTAR",

                    "objeto": objeto

                }

        # -------------------------

        return {

            "acao": "DESCONHECIDO"

        }
