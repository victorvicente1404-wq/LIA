class Conhecimento:

    def __init__(self, memoria):

        self.memoria = memoria

    def aprender(self, objeto, descricao):

        objeto = objeto.strip().lower()
        descricao = descricao.strip()

        if objeto == "" or descricao == "":
            return False

        self.memoria.aprender(objeto, descricao)

        return True

    def consultar(self, objeto):

        objeto = objeto.strip().lower()

        if objeto == "":
            return None

        return self.memoria.consultar(objeto)

    def sabe(self, objeto):

        return self.consultar(objeto) is not None
