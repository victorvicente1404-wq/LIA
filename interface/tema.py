"""
Tema visual da Lia.

Todas as cores, fontes e tamanhos da interface
devem ser definidos aqui.
"""


class Tema:

    # ==========================================
    # CORES
    # ==========================================

    FUNDO = "#1E1E1E"

    PAINEL = "#2A2A2A"

    DESTAQUE = "#FF69B4"

    TEXTO = "#FFFFFF"

    TEXTO_SECUNDARIO = "#CFCFCF"

    BORDA = "#444444"

    ENTRADA = "#303030"

    BOTAO = "#FF69B4"

    BOTAO_HOVER = "#FF85C2"

    BOTAO_TEXTO = "#FFFFFF"

    # ==========================================
    # ROSTO
    # ==========================================

    ROSTO = "#FFFFFF"

    OLHOS = "#FFFFFF"

    BOCA = "#FFFFFF"

    # ==========================================
    # FONTES
    # ==========================================

    FONTE = "Segoe UI"

    TAMANHO_TITULO = 18

    TAMANHO_NORMAL = 12

    TAMANHO_CHAT = 11

    # ==========================================
    # TAMANHOS
    # ==========================================

    LARGURA_JANELA = 500

    ALTURA_JANELA = 700

    TAMANHO_ROSTO = 250

    RAIO_BORDA = 12

    MARGEM = 12

    ESPACAMENTO = 10

    # ==========================================
    # ESTILO (QSS)
    # ==========================================

    @staticmethod
    def estilo():

        return f"""

        QWidget {{

            background-color: {Tema.FUNDO};

            color: {Tema.TEXTO};

            font-family: "{Tema.FONTE}";

            font-size: {Tema.TAMANHO_NORMAL}pt;

        }}

        QTextEdit {{

            background-color: {Tema.PAINEL};

            border: 1px solid {Tema.BORDA};

            border-radius: {Tema.RAIO_BORDA}px;

            padding: 8px;

        }}

        QLineEdit {{

            background-color: {Tema.ENTRADA};

            border: 1px solid {Tema.BORDA};

            border-radius: {Tema.RAIO_BORDA}px;

            padding: 8px;

        }}

        QPushButton {{

            background-color: {Tema.BOTAO};

            color: {Tema.BOTAO_TEXTO};

            border: none;

            border-radius: {Tema.RAIO_BORDA}px;

            padding: 8px;

        }}

        QPushButton:hover {{

            background-color: {Tema.BOTAO_HOVER};

        }}

        """
