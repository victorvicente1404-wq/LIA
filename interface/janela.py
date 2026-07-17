from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit
)

from PySide6.QtCore import Qt

from .rosto import Rosto

from lia.assistente import Lia


class Janela(QWidget):

    def __init__(self):

        super().__init__()

        self.lia = Lia()

        self.rosto = Rosto()

        self.setWindowTitle("Lia")

        self.resize(500, 650)

        self.layout = QVBoxLayout()

        self.layout.setAlignment(Qt.AlignCenter)

        self.rosto_label = QLabel()

        self.rosto_label.setAlignment(Qt.AlignCenter)

        self.rosto_label.setStyleSheet(
            "font-size:48px;"
        )

        self.texto = QLabel()

        self.texto.setAlignment(Qt.AlignCenter)

        self.texto.setWordWrap(True)

        self.texto.setStyleSheet(
            "font-size:16px;"
        )

        self.texto.setText("Olá!")

        self.entrada = QLineEdit()

        self.entrada.setPlaceholderText(
            "Digite uma mensagem..."
        )

        self.entrada.returnPressed.connect(
            self.enviar
        )

        self.layout.addWidget(self.rosto_label)

        self.layout.addWidget(self.texto)

        self.layout.addWidget(self.entrada)

        self.setLayout(self.layout)

        self.atualizar_rosto()

    def atualizar_rosto(self):

        self.rosto_label.setText(
            self.rosto.obter()
        )

    def enviar(self):

        mensagem = self.entrada.text()

        if mensagem == "":
            return

        resposta = self.lia.responder(mensagem)

        self.texto.setText(resposta)

        self.entrada.clear()
