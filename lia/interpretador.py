"""
Interpretador da Lia - Versão ultra sensível
"""

import re


class Interpretador:

    def interpretar(self, frase):

        frase = frase.strip()
        frase_lower = frase.lower()

        # Cumprimento
        if any(g in frase_lower for g in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
            return {"acao": "CUMPRIMENTO"}

        # Nome
        if frase_lower.startswith(("meu nome é ", "meu nome e ")):
            return {
                "acao": "SALVAR_NOME",
                "valor": frase[11:].strip()
            }

        if any(x in frase_lower for x in ["qual meu nome", "como eu me chamo"]):
            return {"acao": "PERGUNTAR_NOME"}

        # Aprender
        if frase_lower.startswith("aprenda que "):
            texto = frase[12:]
            partes = re.split(r"\s+é\s+|\s+e\s+", texto, maxsplit=1, flags=re.IGNORECASE)
            if len(partes) == 2:
                return {
                    "acao": "APRENDER",
                    "objeto": partes[0].strip().lower(),
                    "descricao": partes[1].strip()
                }

        # CONSULTAR - Ultra sensível
        if any(p in frase_lower for p in [
            "o que é", "oque é", "oq é", "quem é", "o que são", "oque são",
            "qual é", "o que significa", "me fale sobre", "me diga o que", 
            "o que é um", "o que é uma", "o que foi", "quem foi"
        ]):
            # Remove o início da pergunta
            objeto = frase_lower
            for prefix in ["o que é ", "oque é ", "oq é ", "quem é ", "o que são ", "oque são ", "qual é ", "o que significa ", "me fale sobre ", "me diga o que é ", "o que é um ", "o que é uma "]:
                if objeto.startswith(prefix):
                    objeto = objeto[len(prefix):]
                    break
            objeto = objeto.replace("?", "").strip()
            return {"acao": "CONSULTAR", "objeto": objeto}

        # Força consulta em qualquer frase com "?" ou palavras chave
