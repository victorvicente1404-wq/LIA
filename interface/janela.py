from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit
)

from PySide6.QtCore import Qt

from .rosto import Rosto

from lia.assistente import Lia


class Janela(QWidget):

    def __init__(self):

        super().__init__()

        self.lia = Lia()

        self.setWindowTitle("Lia")

        self.resize(500, 650)

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignTop)

        # -------------------------
        # Rosto
        # -------------------------

        self.rosto = Rosto()

        # -------------------------
        # Chat
        # -------------------------

        self.chat = QTextEdit()

        self.chat.setReadOnly(True)

        self.chat.append(
            "<b>Lia:</b> Ola! Como posso ajudar?"
        )

        # -------------------------
        # Entrada
        # -------------------------

        self.entrada = QLineEdit()

        self.entrada.setPlaceholderText(
            "Digite uma mensagem..."
        )

        self.entrada.returnPressed.connect(
            self.enviar
        )

        # -------------------------
        # Layout
        # -------------------------

        layout.addWidget(self.rosto)

        layout.addWidget(self.chat)

        layout.addWidget(self.entrada)

        self.setLayout(layout)

    def enviar(self):

        mensagem = self.entrada.text().strip()

        if not mensagem:

            return

        self.chat.append(
            f"<b>Voce:</b> {mensagem}"
        )

        self.rosto.definir_estado(
            "pensando"
        )

        resposta = self.lia.responder(
            mensagem
        )

        self.chat.append(
            f"<b>Lia:</b> {resposta}"
        )

        self.rosto.definir_estado(
            "normal"
        )

        self.entrada.clear()

        barra = self.chat.verticalScrollBar()

        barra.setValue(
            barra.maximum()
        )        self.chat.verticalScrollBar().setValue(
            self.chat.verticalScrollBar().maximum()
        )
