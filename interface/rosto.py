"""
Rosto da Lia.

Este widget desenha o rosto da assistente.
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush
)
from PySide6.QtCore import Qt

from .tema import Tema


class Rosto(QWidget):

    def __init__(self):

        super().__init__()

        self.estado = "normal"

        self.setMinimumSize(

            Tema.TAMANHO_ROSTO,

            Tema.TAMANHO_ROSTO

        )

    # ---------------------------------

    def definir_estado(self, estado):

        self.estado = estado

        self.update()

    # ---------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(

            QPainter.Antialiasing

        )

        painter.fillRect(

            self.rect(),

            QColor(Tema.FUNDO)

        )

        painter.setBrush(

            QBrush(

                QColor(Tema.ROSTO)

            )

        )

        painter.setPen(Qt.NoPen)

        # ------------------------------
        # OLHOS
        # ------------------------------

        if self.estado == "piscando":

            painter.setPen(

                QPen(

                    QColor(Tema.OLHOS),

                    4

                )

            )

            painter.drawLine(

                80,

                90,

                120,

                90

            )

            painter.drawLine(

                180,

                90,

                220,

                90

            )

        else:

            painter.setBrush(

                QColor(Tema.OLHOS)

            )

            painter.drawEllipse(

                80,

                70,

                40,

                40

            )

            painter.drawEllipse(

                180,

                70,

                40,

                40

            )

        # ------------------------------
        # BOCA
        # ------------------------------

        painter.setPen(

            QPen(

                QColor(Tema.BOCA),

                4

            )

        )

        if self.estado == "feliz":

            painter.drawArc(

                95,

                140,

                110,

                50,

                0,

                -180 * 16

            )

        elif self.estado == "triste":

            painter.drawArc(

                95,

                165,

                110,

                50,

                0,

                180 * 16

            )

        elif self.estado == "falando":

            painter.drawEllipse(

                135,

                145,

                30,

                40

            )

        elif self.estado == "pensando":

            painter.drawLine(

                120,

                160,

                180,

                160

            )

        else:

            painter.drawArc(

                95,

                150,

                110,

                30,

                0,

                -180 * 16

            )
