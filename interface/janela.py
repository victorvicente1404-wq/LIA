from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit
)

from PySide6.QtCore import Qt

from .rosto import Rosto


class Janela(QWidget):

    def __init__(self):

        super().__init__()

        self.rosto = Rosto()

        self.setWindowTitle("Lia")

        self.setFixedSize(450, 600)

        self.layout = QVBoxLayout()

        self.layout.setAlignment(Qt.AlignCenter)

        self.rosto_label = QLabel()

        self.rosto_label.setAlignment(Qt.AlignCenter)

        self.rosto_label.setStyleSheet("""
            font-size: 42px;
        """)

        self.rosto_label.setText(
            self.rosto.obter()
        )

        self.texto = QLabel()

        self.texto.setAlignment(Qt.AlignCenter)

        self.texto.setWordWrap(True)

        self.texto.setText(
            "Olá! Como posso ajudar?"
        )

        self.entrada = QLineEdit()

        self.entrada.setPlaceholderText(
            "Digite aqui..."
        )

        self.layout.addWidget(
            self.rosto_label
        )

        self.layout.addWidget(
            self.texto
        )

        self.layout.addWidget(
            self.entrada
        )

        self.setLayout(
            self.layout
        )

    def atualizar_rosto(self):

        self.rosto_label.setText(
            self.rosto.obter()
        )
