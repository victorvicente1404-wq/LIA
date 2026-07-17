"""
Sistema de eventos da Lia.

Um Evento representa qualquer resposta gerada pela
assistente. Além do texto, ele pode conter emoção,
ações e informações extras.
"""


class Evento:

    def __init__(

        self,

        texto="",

        emocao="normal",

        acao=None,

        dados=None

    ):

        self.texto = texto

        self.emocao = emocao

        self.acao = acao

        self.dados = dados or {}

    def para_dict(self):

        return {

            "texto": self.texto,

            "emocao": self.emocao,

            "acao": self.acao,

            "dados": self.dados

        }

    def __str__(self):

        return self.texto
