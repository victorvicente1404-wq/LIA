"""
Animações e efeitos visuais da Lia.
"""

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QWidget


class Animacoes:
    """
    Classe auxiliar para gerenciar animações da interface.
    """

    @staticmethod
    def animar_entrada(widget: QWidget, duracao: int = 400):
        """Anima a entrada de um widget (fade + slide)."""
        # Animação de opacidade
        anim_opacidade = QPropertyAnimation(widget, b"windowOpacity")
        anim_opacidade.setDuration(duracao)
        anim_opacidade.setStartValue(0.0)
        anim_opacidade.setEndValue(1.0)
        anim_opacidade.setEasingCurve(QEasingCurve.InOutQuad)
        anim_opacidade.start()

    @staticmethod
    def piscar_rosto(rosto_widget, vezes: int = 1):
        """Faz o rosto piscar (efeito visual)."""
        def piscar():
            rosto_widget.definir_estado("piscando")
            QTimer.singleShot(150, lambda: rosto_widget.definir_estado("normal"))

        for i in range(vezes):
            QTimer.singleShot(i * 400, piscar)

    @staticmethod
    def falar(rosto_widget):
        """Anima o rosto enquanto a Lia 'fala'."""
        rosto_widget.definir_estado("falando")
        QTimer.singleShot(1200, lambda: rosto_widget.definir_estado("normal"))

    @staticmethod
    def feliz(rosto_widget):
        """Anima o rosto feliz."""
        rosto_widget.definir_estado("feliz")
        QTimer.singleShot(2000, lambda: rosto_widget.definir_estado("normal"))

    @staticmethod
    def pensando(rosto_widget):
        """Anima o rosto pensando."""
        rosto_widget.definir_estado("pensando")
