"""
Módulo de pesquisa da Lia.
"""

import requests


class Pesquisa:

    @staticmethod
    def pesquisar(pergunta):

        # 1° tenta DuckDuckGo
        resposta = Pesquisa.pesquisar_duckduckgo(pergunta)

        if resposta:
            return resposta

        # Futuramente:
        # resposta = Pesquisa.pesquisar_wikipedia(pergunta)
        # if resposta:
        #     return resposta

        # resposta = Pesquisa.pesquisar_ia(pergunta)
        # if resposta:
        #     return resposta

        return None

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

            relacionados = dados.get("RelatedTopics", [])

            for item in relacionados:

                if isinstance(item, dict):

                    texto = item.get("Text")

                    if texto:
                        return texto

            return None

        except Exception:

            return None

    @staticmethod
    def pesquisar_wikipedia(pergunta):

        # Vamos implementar na próxima etapa.

        return None

    @staticmethod
    def pesquisar_ia(pergunta):

        # Aqui futuramente ficará o Gemini,
        # ChatGPT ou outra IA.

        return None
