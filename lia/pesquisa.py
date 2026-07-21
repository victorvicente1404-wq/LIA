"""
Módulo de pesquisa da Lia.
"""

import requests


class Pesquisa:

    @staticmethod
    def pesquisar(pergunta):

        # 1. Wikipédia
        resposta = Pesquisa.pesquisar_wikipedia(pergunta)
        if resposta and len(resposta) > 30:
            return resposta

        # 2. DuckDuckGo
        resposta = Pesquisa.pesquisar_duckduckgo(pergunta)
        if resposta and len(resposta) > 30:
            return resposta

        return None

    @staticmethod
    def pesquisar_wikipedia(pergunta):
        try:
            url = "https://pt.wikipedia.org/api/rest_v1/page/summary/" + requests.utils.quote(pergunta.replace(" ", "_"))
            r = requests.get(url, headers={"User-Agent": "LIA/1.0"}, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return data.get("extract")
            return None
        except:
            return None

    @staticmethod
    def pesquisar_duckduckgo(pergunta):
        try:
            r = requests.get(
                "https://api.duckduckgo.com/",
                params={"q": pergunta, "format": "json", "no_redirect": 1, "no_html": 1},
                timeout=10
            )
            data = r.json()
            if data.get("AbstractText"):
                return data["AbstractText"]
            for item in data.get("RelatedTopics", []):
                if isinstance(item, dict) and item.get("Text"):
                    return item["Text"]
            return None
        except:
            return None
