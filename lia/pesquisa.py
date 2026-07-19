"""
Módulo de pesquisa da Lia.

Este módulo centraliza todas as pesquisas da IA.
Toda nova fonte de conhecimento deve ser adicionada aqui.
"""

import requests


class Pesquisa:

    def __init__(self):

        self.fontes = [

            self.pesquisar_wikipedia,

            self.pesquisar_duckduckgo,

            self.pesquisar_gemini,

            self.pesquisar_chatgpt,

            self.pesquisar_deepseek

        ]

    # --------------------------------------------------

    @staticmethod
    def pesquisar(pergunta):

        pesquisa = Pesquisa()

        for fonte in pesquisa.fontes:

            try:

                resposta = fonte(pergunta)

                if resposta:

                    resposta = resposta.strip()

                    if len(resposta) > 20:

                        return resposta

            except Exception:

                continue

        return None

    # --------------------------------------------------

    @staticmethod
    def pesquisar_wikipedia(pergunta):

        try:

            titulo = pergunta.replace(" ", "_")

            url = (

                "https://pt.wikipedia.org/api/rest_v1/page/summary/"

                + titulo

            )

            resposta = requests.get(

                url,

                headers={

                    "User-Agent": "LIA/1.0"

                },

                timeout=10

            )

            if resposta.status_code != 200:

                return None

            dados = resposta.json()

            return dados.get("extract")

        except Exception:

            return None

    # --------------------------------------------------

    @staticmethod
    def pesquisar_duckduckgo(pergunta):

        try:

            resposta = requests.get(

                "https://api.duckduckgo.com/",

                params={

                    "q": pergunta,

                    "format": "json",

                    "no_redirect": 1,

                    "no_html": 1

                },

                timeout=10

            )

            dados = resposta.json()

            if dados.get("AbstractText"):

                return dados["AbstractText"]

            for item in dados.get("RelatedTopics", []):

                if isinstance(item, dict):

                    texto = item.get("Text")

                    if texto:

                        return texto

            return None

        except Exception:

            return None

    # --------------------------------------------------
    # IA - Gemini
    # --------------------------------------------------

    @staticmethod
    def pesquisar_gemini(pergunta):

        """
        Futuramente:
        Google Gemini API
        """

        return None

    # --------------------------------------------------
    # IA - ChatGPT
    # --------------------------------------------------

    @staticmethod
    def pesquisar_chatgpt(pergunta):

        """
        Futuramente:
        OpenAI API
        """

        return None

    # --------------------------------------------------
    # IA - DeepSeek
    # --------------------------------------------------

    @staticmethod
    def pesquisar_deepseek(pergunta):

        """
        Futuramente:
        DeepSeek API
        """

        return None
