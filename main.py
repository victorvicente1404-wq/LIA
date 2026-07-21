"""
Ponto de entrada da Lia.
"""

import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication

from interface import Janela


def main():
    # Carrega o .env no início do programa
    try:
        from dotenv import load_dotenv
        env_path = Path(__file__).parent / ".env"
        load_dotenv(env_path)
        print("✅ .env carregado com sucesso!")
    except ImportError:
        print("⚠️ Pacote python-dotenv não encontrado. Instale com: pip install python-dotenv")
    except Exception as e:
        print(f"⚠️ Erro ao carregar .env: {e}")

    app = QApplication(sys.argv)

    janela = Janela()
    janela.show()

    print("🚀 Lia iniciada! Fale com ela na janela.")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
