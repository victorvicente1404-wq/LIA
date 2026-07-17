"""
Componente de chat da Lia.
"""

from PySide6.QtWidgets import QTextEdit


class Chat(QTextEdit):

    def __init__(self):

        super().__init__()

        self.setReadOnly(True)

        self.setAcceptRichText(True)

        self.setPlaceholderText(
            "A conversa aparecerá aqui..."
        )

    # ---------------------------------

    def adicionar_usuario(self, texto):

        self.append(

            f"<b>Você:</b> {texto}"

        )

        self.rolar_final()

    # ---------------------------------

    def adicionar_lia(self, texto):

        self.append(

            f"<b>Lia:</b> {texto}"

        )

        self.rolar_final()

    # ---------------------------------

    def adicionar_sistema(self, texto):

        self.append(

            f"<i>{texto}</i>"

        )

        self.rolar_final()

    # ---------------------------------

    def limpar(self):

        self.clear()

    # ---------------------------------

    def rolar_final(self):

        barra = self.verticalScrollBar()

        barra.setValue(

            barra.maximum()

        )
