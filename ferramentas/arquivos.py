"""
Ferramentas para manipulação de arquivos da Lia.
"""

import os
import json
from pathlib import Path


class Arquivos:

    @staticmethod
    def criar_pasta(caminho):
        """Cria uma pasta se ela não existir."""
        try:
            os.makedirs(caminho, exist_ok=True)
            return True
        except Exception:
            return False

    @staticmethod
    def listar_arquivos(diretorio="."):
        """Lista arquivos em um diretório."""
        try:
            return [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
        except Exception:
            return []

    @staticmethod
    def ler_arquivo(caminho):
        """Lê o conteúdo de um arquivo de texto."""
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Erro ao ler arquivo: {str(e)}"

    @staticmethod
    def escrever_arquivo(caminho, conteudo):
        """Escreve conteúdo em um arquivo."""
        try:
            # Garante que a pasta existe
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            return True
        except Exception:
            return False

    @staticmethod
    def ler_json(caminho):
        """Lê um arquivo JSON."""
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None

    @staticmethod
    def salvar_json(caminho, dados):
        """Salva dados em um arquivo JSON."""
        try:
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False

    @staticmethod
    def existe(caminho):
        """Verifica se um arquivo ou pasta existe."""
        return os.path.exists(caminho)
