# LIA-main/ferramentas/internet.py
import requests

class Internet:
    @staticmethod
    def verificar_conexao():
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except:
            return False

    @staticmethod
    def baixar_arquivo(url, caminho):
        try:
            r = requests.get(url, stream=True)
            with open(caminho, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except:
            return False
