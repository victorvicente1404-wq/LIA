"""
Ferramenta de Pesquisa na Web
"""

import requests
from bs4 import BeautifulSoup

class Pesquisa:
    @staticmethod
    def buscar(query: str, max_resultados=3):
        try:
            url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
            headers = {"User-Agent": "LIA-Assistent/1.0"}
            
            r = requests.get(url, headers=headers, timeout=10)
            r.raise_for_status()
            
            soup = BeautifulSoup(r.text, 'html.parser')
            results = soup.find_all('div', class_='result__body')[:max_resultados]
            
            if not results:
                return "Não encontrei resultados para essa busca."
            
            resposta = f"🔍 Resultados para '{query}':\n\n"
            for i, result in enumerate(results):
                titulo = result.find('a', class_='result__a')
                snippet = result.find('a', class_='result__snippet')
                
                if titulo:
                    resposta += f"{i+1}. {titulo.get_text().strip()}\n"
                if snippet:
                    resposta += f"   {snippet.get_text().strip()[:180]}...\n\n"
            
            return resposta.strip()
            
        except Exception as e:
            return f"⚠️ Erro na pesquisa: {str(e)[:80]}"
