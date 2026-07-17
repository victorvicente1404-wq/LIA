import sys

from PySide6.QtWidgets import QApplication

from interface.janela import Janela


app = QApplication(sys.argv)

janela = Janela()

janela.show()

app.exec()
