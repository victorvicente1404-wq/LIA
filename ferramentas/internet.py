"""
Ferramenta de Internet da Lia.
"""

import requests


class Internet:
    """
    Classe para verificação de conexão e download de arquivos.
    """

    @staticmethod
    def verificar_conexao():
        """Verifica se há conexão com a internet."""
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except:
            return False

    @staticmethod
    def baixar_arquivo(url, caminho):
        """Baixa um arquivo da internet."""
        try:
            r = requests.get(url, stream=True, timeout=30)
            r.raise_for_status()
            
            with open(caminho, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except Exception as e:
            print(f"Erro ao baixar arquivo: {e}")
            return False

    @staticmethod
    def get(url, timeout=10):
        """Faz uma requisição GET simples."""
        try:
            headers = {"User-Agent": "Lia-Assistent/1.0"}
            r = requests.get(url, headers=headers, timeout=timeout)
            r.raise_for_status()
            return r
        except Exception as e:
            print(f"Erro na requisição: {e}")
            return None
