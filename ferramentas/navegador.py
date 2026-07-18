"""
Ferramenta de Navegador da Lia.
Permite abrir sites e navegar na internet.
"""

import webbrowser
import os


class Navegador:

    @staticmethod
    def abrir_site(url: str):
        """Abre um site no navegador padrão."""
        try:
            if not url.startswith("http"):
                url = "https://" + url
            webbrowser.open(url)
            return f"Abrindo {url} no navegador..."
        except Exception as e:
            return f"Erro ao abrir o site: {str(e)}"

    @staticmethod
    def pesquisar_google(query: str):
        """Abre o Google com uma pesquisa."""
        try:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Pesquisando no Google: '{query}'"
        except Exception as e:
            return f"Erro ao pesquisar no Google: {str(e)}"

    @staticmethod
    def abrir_youtube(query: str = None):
        """Abre o YouTube (com ou sem pesquisa)."""
        try:
            if query:
                url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                return f"Abrindo YouTube com busca: '{query}'"
            else:
                url = "https://www.youtube.com"
                return "Abrindo YouTube..."
            
            webbrowser.open(url)
        except Exception as e:
            return f"Erro ao abrir o YouTube: {str(e)}"
