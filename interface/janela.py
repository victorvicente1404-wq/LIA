from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QLabel
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

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignTop)

        self.rosto_label = QLabel()

        self.rosto_label.setAlignment(Qt.AlignCenter)

        self.rosto_label.setStyleSheet("""
            font-size:48px;
        """)

        self.rosto_label.setText(
            self.rosto.obter()
        )

        self.chat = QTextEdit()

        self.chat.setReadOnly(True)

        self.chat.append("<b>Lia:</b> Ola! Como posso ajudar?")

        self.entrada = QLineEdit()

        self.entrada.setPlaceholderText(
            "Digite uma mensagem..."
        )

        self.entrada.returnPressed.connect(
            self.enviar
        )

        layout.addWidget(self.rosto_label)

        layout.addWidget(self.chat)

        layout.addWidget(self.entrada)

        self.setLayout(layout)

    def enviar(self):

        mensagem = self.entrada.text().strip()

        if mensagem == "":
            return

        self.chat.append(
            f"<b>Voce:</b> {mensagem}"
        )

        resposta = self.lia.responder(
            mensagem
        )

        self.chat.append(
            f"<b>Lia:</b> {resposta}"
        )

        self.entrada.clear()

        self.chat.verticalScrollBar().setValue(
            self.chat.verticalScrollBar().maximum()
        )
