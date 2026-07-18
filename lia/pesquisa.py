"""
Módulo de pesquisa da Lia - Integração principal para responder dúvidas do usuário
"""

import requests


class Pesquisa:
    """
    Classe responsável por buscar informações na internet
    quando a Lia não sabe a resposta.
    """

    @staticmethod
    def pesquisar(pergunta: str):
        """Método principal de pesquisa. Tenta várias fontes."""

        # 1. Tenta Wikipédia primeiro (melhor para definições e fatos)
        resposta = Pesquisa.pesquisar_wikipedia(pergunta)
        if resposta and len(resposta.strip()) > 30:
            return resposta.strip()

        # 2. Tenta DuckDuckGo como fallback
        resposta = Pesquisa.pesquisar_duckduckgo(pergunta)
        if resposta and len(resposta.strip()) > 30:
            return resposta.strip()

        return None

    @staticmethod
    def pesquisar_wikipedia(pergunta: str):
        """Busca na Wikipédia em português."""
        try:
            # Formata o título para URL
            titulo = pergunta.replace(" ", "_")
            url = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{titulo}"

            resposta = requests.get(
                url,
                headers={"User-Agent": "Lia-Assistent/1.0"},
                timeout=10
            )

            if resposta.status_code != 200:
                return None

            dados = resposta.json()
            texto = dados.get("extract")

            return texto if texto else None

        except Exception:
            return None

    @staticmethod
    def pesquisar_duckduckgo(pergunta: str):
        """Busca via API do DuckDuckGo."""
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

            # Resumo principal
            if dados.get("AbstractText"):
                return dados["AbstractText"]

            # Tópicos relacionados
            for item in dados.get("RelatedTopics", []):
                if isinstance(item, dict) and item.get("Text"):
                    return item["Text"]

            return None

        except Exception:
            return None
