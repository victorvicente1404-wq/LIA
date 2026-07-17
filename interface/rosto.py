class Rosto:

    def __init__(self):

        self.olho_esquerdo = "◕"
        self.olho_direito = "◕"
        self.boca = "◡"

    def normal(self):

        self.olho_esquerdo = "◕"
        self.olho_direito = "◕"
        self.boca = "◡"

    def feliz(self):

        self.olho_esquerdo = "^"
        self.olho_direito = "^"
        self.boca = "◡"

    def pensando(self):

        self.olho_esquerdo = "•"
        self.olho_direito = "•"
        self.boca = "-"

    def surpresa(self):

        self.olho_esquerdo = "○"
        self.olho_direito = "○"
        self.boca = "O"

    def triste(self):

        self.olho_esquerdo = "◕"
        self.olho_direito = "◕"
        self.boca = "︵"

    def piscar(self):

        self.olho_esquerdo = "^"
        self.olho_direito = "◕"
        self.boca = "◡"

    def falar(self):

        self.olho_esquerdo = "◕"
        self.olho_direito = "◕"
        self.boca = "○"

    def obter(self):

        return (
            f"({self.olho_esquerdo} "
            f"{self.boca} "
            f"{self.olho_direito})"
        )
