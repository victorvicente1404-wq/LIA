"""
Interpretador da Lia.

Converte frases do usuário em comandos internos.

No futuro este módulo poderá utilizar modelos
de IA, mantendo a mesma interface para o resto
do sistema.
"""

import re


class Interpretador:

    def __init__(self):

        self.cumprimentos = [

            "oi",
            "ola",
            "olá",
            "bom dia",
            "boa tarde",
            "boa noite"

        ]

    # ---------------------------------

    def normalizar(self, texto):

        texto = texto.lower()

        texto = texto.strip()

        return texto

    # ---------------------------------

    def interpretar(self, texto):

        original = texto

        texto = self.normalizar(texto)

        # ------------------------------
        # Cumprimentos
        # ------------------------------

        if texto in self.cumprimentos:

            return {

                "acao": "CUMPRIMENTO"

            }

        # ------------------------------
        # Nome
        # ------------------------------

        padroes_nome = [

            r"meu nome e (.+)",

            r"meu nome é (.+)",

            r"eu me chamo (.+)",

            r"pode me chamar de (.+)"

        ]

        for padrao in padroes_nome:

            resultado = re.match(

                padrao,

                texto

            )

            if resultado:

                return {

                    "acao": "SALVAR_NOME",

                    "valor": resultado.group(1).strip()

                }

        # ------------------------------
        # Perguntar nome
        # ------------------------------

        perguntas_nome = [

            "qual e meu nome",

            "qual é meu nome",

            "quem sou eu",

            "quem eu sou"

        ]

        if texto in perguntas_nome:

            return {

                "acao": "PERGUNTAR_NOME"

            }

        # ------------------------------
        # Aprender
        # ------------------------------

        if " e " in texto:

            partes = texto.split(

                " e ",

                1

            )

            objeto = partes[0].strip()

            descricao = partes[1].strip()

            if objeto != "" and descricao != "":

                return {

                    "acao": "APRENDER",

                    "objeto": objeto,

                    "descricao": descricao

                }

        # ------------------------------
        # Consultar
        # ------------------------------

        perguntas = [

            "o que e ",

            "o que é ",

            "quem e ",

            "quem é ",

            "qual e ",

            "qual é "

        ]

        for pergunta in perguntas:

            if texto.startswith(pergunta):

                objeto = texto.replace(

                    pergunta,

                    ""

                ).strip()

                return {

                    "acao": "CONSULTAR",

                    "objeto": objeto

                }

        # ------------------------------

        return {

            "acao": "DESCONHECIDO",

            "texto": original

        }
