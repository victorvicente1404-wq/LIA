import json


class Memoria:

    def __init__(self):

        self.arquivo = "data/memoria.json"

    def carregar(self):

        with open(self.arquivo, "r", encoding="utf-8") as arquivo:

            return json.load(arquivo)

    def salvar(self, dados):

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            json.dump(dados, arquivo, indent=4)

    def guardar(self, chave, valor):

        dados = self.carregar()

        dados[chave] = valor

        self.salvar(dados)

    def ler(self, chave):

        dados = self.carregar()

        return dados.get(chave)
