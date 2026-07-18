"""
Interpretador da Lia.
Responsável por entender os comandos do usuário.
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
            "oi", "olá", "ola", "e ai", "e aí", "bom dia",
            "boa tarde", "boa noite", "oi lia", "olá lia"
        ]:
            return {
                "acao": "CUMPRIMENTO"
            }

        # -------------------------
        # Salvar Nome
        # -------------------------

        if frase_lower.startswith("meu nome é "):
            return {
                "acao": "SALVAR_NOME",
                "valor": frase[11:].strip()
            }

        if frase_lower.startswith("meu nome e "):
            return {
                "acao": "SALVAR_NOME",
                "valor": frase[11:].strip()
            }

        # -------------------------
        # Perguntar Nome
        # -------------------------

        if frase_lower in [
            "qual meu nome", "como eu me chamo", "qual é meu nome"
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
        # Consultar (perguntas)
        # -------------------------

        consultas = [
            "o que é ", "o que e ", "quem é ", "quem e ",
            "qual é ", "qual e ", "o que significa ",
            "me fale sobre ", "me diga o que é "
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
        # Desconhecido
        # -------------------------

        return {
            "acao": "DESCONHECIDO"
        }
