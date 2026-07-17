from PySide6.QtWidgets import QWidget

from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush
)

from PySide6.QtCore import Qt


class Rosto(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(250, 250)

        self.estado = "normal"

    def definir_estado(self, estado):

        self.estado = estado

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        painter.fillRect(
            self.rect(),
            QColor("#202225")
        )

        painter.setBrush(
            QBrush(
                QColor("white")
            )
        )

        painter.setPen(
            Qt.NoPen
        )

        # -------------------------
        # OLHOS
        # -------------------------

        if self.estado == "piscando":

            painter.setPen(
                QPen(
                    QColor("white"),
                    4
                )
            )

            painter.drawLine(
                70,
                90,
                110,
                90
            )

            painter.drawLine(
                140,
                90,
                180,
                90
            )

        else:

            painter.drawEllipse(
                70,
                70,
                40,
                40
            )

            painter.drawEllipse(
                140,
                70,
                40,
                40
            )

        # -------------------------
        # BOCA
        # -------------------------

        painter.setPen(
            QPen(
                QColor("white"),
                4
            )
        )

        if self.estado == "feliz":

            painter.drawArc(
                90,
                120,
                70,
                40,
                0,
                -180 * 16
            )

        elif self.estado == "triste":

            painter.drawArc(
                90,
                145,
                70,
                40,
                0,
                180 * 16
            )

        elif self.estado == "falando":

            painter.drawEllipse(
                115,
                135,
                20,
                30
            )

        else:

            painter.drawArc(
                90,
                130,
                70,
                25,
                0,
                -180 * 16
            )
