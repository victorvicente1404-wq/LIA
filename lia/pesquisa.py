"""
Módulo de pesquisa da Lia.
"""

import requests


class Pesquisa:

    @staticmethod
    def pesquisar(pergunta):

        # 1° Wikipédia
        resposta = Pesquisa.pesquisar_wikipedia(pergunta)

        if resposta:
            return resposta

        # 2° DuckDuckGo
        resposta = Pesquisa.pesquisar_duckduckgo(pergunta)

        if resposta:
            return resposta

        # Futuramente:
        # resposta = Pesquisa.pesquisar_ia(pergunta)

        return None

    # -----------------------------------------

    @staticmethod
    def pesquisar_wikipedia(pergunta):

        try:

            url = (
                "https://pt.wikipedia.org/api/rest_v1/page/summary/"
                + pergunta.replace(" ", "_")
            )

            resposta = requests.get(

                url,

                headers={

                    "User-Agent": "Lia/0.1"

                },

                timeout=10

            )

            if resposta.status_code != 200:

                return None

            dados = resposta.json()

            texto = dados.get("extract")

            if texto:

                return texto

            return None

        except Exception:

            return None

    # -----------------------------------------

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

            texto = dados.get("AbstractText")

            if texto:

                return texto

            relacionados = dados.get("RelatedTopics", [])

            for item in relacionados:

                if isinstance(item, dict):

                    texto = item.get("Text")

                    if texto:

                        return texto

            return None

        except Exception:

            return None

    # -----------------------------------------

    @staticmethod

    def pesquisar_ia(pergunta):

        """
        Futuramente:
        Gemini
        ChatGPT
        DeepSeek
        """

        return None
