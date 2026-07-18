"""
Kernel da Lia - Central de controle
Roteador de ferramentas externas
"""

from .assistente import Assistente  # Note: pode precisar ajustar import


class Roteador:
    """
    Responsável por decidir se deve usar ferramentas externas
    antes de cair no assistente principal.
    """

    def __init__(self):
        self.assistente = Assistente()  # fallback

    def decidir(self, mensagem: str) -> str:
        """
        Analisa a mensagem e decide se deve usar alguma ferramenta especial.
        Retorna a resposta se encontrou, senão retorna None.
        """
        mensagem_lower = mensagem.lower().strip()

        # Exemplos de rotas futuras:
        # if "clima" in mensagem_lower or "tempo" in mensagem_lower:
        #     return self.ferramenta_tempo(mensagem)

        # if "calcular" in mensagem_lower or any(c.isdigit() for c in mensagem):
        #     from ferramentas.calculadora import Calculadora
        #     return Calculadora.calcular(mensagem)

        # Por enquanto, retorna None para usar o fluxo normal (pesquisa)
        return None

    # ------------------- Ferramentas futuras -------------------

    def ferramenta_tempo(self, mensagem):
        """Exemplo de integração futura."""
        return None

    def ferramenta_calculadora(self, mensagem):
        """Exemplo de integração futura."""
        return None
