"""
Interpretador da Lia.
Responsável por entender a intenção do usuário.
"""

import re


class Interpretador:

    def interpretar(self, frase):

        frase = frase.strip()

        frase_lower = frase.lower()

        # -------------------------
        # Cumprimento
        # -------------------------

        cumprimentos = [

            "oi",

            "olá",

            "ola",

            "e ai",

            "e aí",

            "bom dia",

            "boa tarde",

            "boa noite"

        ]

        if any(
            frase_lower.startswith(c)
            for c in cumprimentos
        ):

            return {

                "acao": "CUMPRIMENTO"

            }

        # -------------------------
        # Salvar Nome
        # -------------------------

        match = re.match(

            r"meu nome (é|e)\s+(.+)",

            frase_lower

        )

        if match:

            return {

                "acao": "SALVAR_NOME",

                "valor": match.group(2).strip().title()

            }

        # -------------------------
        # Perguntar Nome
        # -------------------------

        if any(

            texto in frase_lower

            for texto in [

                "qual meu nome",

                "qual é meu nome",

                "como eu me chamo"

            ]

        ):

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
        # Perguntas
        # -------------------------

        consultas = [

            "o que é ",

            "o que e ",

            "quem é ",

            "quem e ",

            "qual é ",

            "qual e ",

            "o que significa ",

            "me fale sobre ",

            "me diga o que é ",

            "explique ",

            "explique o que é "

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
        # Conversa Livre
        # -------------------------

        return {

            "acao": "CONVERSAR",

            "mensagem": frase

        }
