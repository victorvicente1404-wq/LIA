"""
Assistente principal da Lia - Forçando pesquisa
"""

from .interpretador import Interpretador
from .memoria import Memoria
from .usuario import Usuario
from .conhecimento import Conhecimento
from .respostas import Respostas
from .pesquisa import Pesquisa

try:
    from ia.roteador import Roteador
except ImportError:
    Roteador = None


class Assistente:

    def __init__(self):
        self.memoria = Memoria()
        self.usuario = Usuario(self.memoria)
        self.conhecimento = Conhecimento(self.memoria)
        self.interpretador = Interpretador()
        self.roteador = Roteador() if Roteador else None

    def responder(self, mensagem: str):

        mensagem = mensagem.strip()
        if not mensagem:
            return Respostas.vazia()

        # 1. IA
        if self.roteador:
            try:
                resp = self.roteador.decidir(mensagem)
                if resp:
                    return resp
            except:
                pass

        # 2. Força consulta para qualquer frase longa
        objeto = mensagem.replace("?", "").replace("oque ", "o que ").strip()

        # Memória
        resposta = self.conhecimento.consultar(objeto)
        if resposta:
            return Respostas.conhecimento(resposta)

        # Pesquisa na web
        resposta = Pesquisa.pesquisar(objeto)
        if resposta:
            self.conhecimento.aprender(objeto, resposta)
            return Respostas.conhecimento(resposta)

        return Respostas.nao_entendi()
