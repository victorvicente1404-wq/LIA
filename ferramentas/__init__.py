"""
Pacote de ferramentas da Lia.
Aqui são importadas todas as ferramentas disponíveis.
"""

from .pesquisa import Pesquisa
from .internet import Internet
from .calculadora import Calculadora
from .sistema import Sistema
from .tempo import Tempo

__all__ = [
    "Pesquisa",
    "Internet",
    "Calculadora",
    "Sistema",
    "Tempo"
]
