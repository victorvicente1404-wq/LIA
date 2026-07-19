"""
Ponto de entrada da Lia.
"""

import sys

from PySide6.QtWidgets import QApplication

from interface import Janela


def main():
    """
    Inicializa a aplicação da Lia.
    """

    app = QApplication(sys.argv)

    # Impede que o programa feche se todas as janelas forem ocultadas.
    app.setQuitOnLastWindowClosed(True)

    janela = Janela()
    janela.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
