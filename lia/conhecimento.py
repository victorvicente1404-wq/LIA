class Conhecimento:

    def __init__(self, memoria):

        self.memoria = memoria

    def aprender(self, objeto, descricao):

        objeto = objeto.lower().strip()

        descricao = descricao.strip()

        self.memoria.aprender(objeto, descricao)

    def responder(self, objeto):

        objeto = objeto.lower().strip()

        resposta = self.memoria.consultar(objeto)

        if resposta:

            return f"{objeto} e {resposta}"

        return None
