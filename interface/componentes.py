"""
Componentes reutilizáveis da interface da Lia.
"""

from PySide6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from .tema import Tema


class BotaoLia(QPushButton):

    def __init__(self, texto=""):

        super().__init__(texto)

        self.setMinimumHeight(42)

        self.setCursor(Qt.PointingHandCursor)


class EntradaLia(QLineEdit):

    def __init__(self):

        super().__init__()

        self.setMinimumHeight(42)

        self.setPlaceholderText(
            "Digite uma mensagem..."
        )


class TituloLia(QLabel):

    def __init__(self, texto):

        super().__init__(texto)

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(

            f"""

            font-size: {Tema.TAMANHO_TITULO}pt;

            font-weight: bold;

            color: {Tema.TEXTO};

            """

        )


class Painel(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet(

            f"""

            QFrame {{

                background-color: {Tema.PAINEL};

                border-radius: {Tema.RAIO_BORDA}px;

            }}

            """

        )
