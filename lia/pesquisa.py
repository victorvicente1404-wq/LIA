import requests


class Pesquisa:

    URL = "https://api.duckduckgo.com/"

    @staticmethod
    def pesquisar(pergunta):

        try:

            resposta = requests.get(

                Pesquisa.URL,

                params={

                    "q": pergunta,

                    "format": "json",

                    "no_redirect": 1,

                    "no_html": 1

                },

                timeout=10

            )

            dados = resposta.json()

            texto = dados.get("AbstractText", "")

            if texto:

                return texto

            relacionados = dados.get("RelatedTopics", [])

            for item in relacionados:

                if isinstance(item, dict):

                    texto = item.get("Text", "")

                    if texto:

                        return texto

            return None

        except Exception:

            return None
