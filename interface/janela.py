"""
Janela principal da Lia.
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from lia import Kernel

from .tema import Tema
from .chat import Chat
from .rosto import Rosto
from .componentes import EntradaLia, BotaoLia


class Janela(QWidget):

    def __init__(self):

        super().__init__()

        self.kernel = Kernel()
        self.kernel.iniciar()

        self.setWindowTitle("Lia")

        self.resize(
            Tema.LARGURA_JANELA,
            Tema.ALTURA_JANELA
        )

        self.setStyleSheet(
            Tema.estilo()
        )

        self.criar_interface()

    # ---------------------------------

    def criar_interface(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(
            Tema.MARGEM,
            Tema.MARGEM,
            Tema.MARGEM,
            Tema.MARGEM
        )

        layout.setSpacing(
            Tema.ESPACAMENTO
        )

        # -------------------------
        # Rosto
        # -------------------------

        self.rosto = Rosto()

        layout.addWidget(
            self.rosto
        )

        # -------------------------
        # Chat
        # -------------------------

        self.chat = Chat()

        layout.addWidget(
            self.chat
        )

        # -------------------------
        # Entrada
        # -------------------------

        linha = QHBoxLayout()

        self.entrada = EntradaLia()

        self.entrada.returnPressed.connect(
            self.enviar
        )

        self.botao = BotaoLia("Enviar")

        self.botao.clicked.connect(
            self.enviar
        )

        linha.addWidget(
            self.entrada
        )

        linha.addWidget(
            self.botao
        )

        layout.addLayout(
            linha
        )

        self.setLayout(
            layout
        )

        self.chat.adicionar_lia(
            "Olá! Eu sou a Lia."
        )

    # ---------------------------------

    def enviar(self):

        mensagem = self.entrada.text().strip()

        if mensagem == "":
            return

        self.chat.adicionar_usuario(
            mensagem
        )

        self.rosto.definir_estado(
            "pensando"
        )

        resposta = self.kernel.responder(
            mensagem
        )

        self.chat.adicionar_lia(
            resposta
        )

        self.rosto.definir_estado(
            "normal"
        )

        self.entrada.clear()
