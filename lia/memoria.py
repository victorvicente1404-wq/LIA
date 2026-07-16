import json


class Memoria:

    def __init__(self):

        self.arquivo = "data/memoria.json"

    def carregar(self):

        with open(self.arquivo, "r", encoding="utf-8") as arquivo:

            return json.load(arquivo)

    def salvar(self, dados):

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def guardar_nome(self, nome):

        dados = self.carregar()

        dados["usuario"]["nome"] = nome

        self.salvar(dados)

    def ler_nome(self):

        dados = self.carregar()

        return dados["usuario"]["nome"]

    def aprender(self, objeto, descricao):

        dados = self.carregar()

        dados["conhecimento"][objeto.lower()] = descricao

        self.salvar(dados)

    def consultar(self, objeto):

        dados = self.carregar()

        return dados["conhecimento"].get(objeto.lower())
        
    def adicionar_gosto(self, gosto):
        
        dados = self.carregar()

        if gosto not in dados["preferencias"]["gostos"]:

        dados["preferencias"]["gostos"].append(gosto)

        self.salvar(dados)
        
    def ler_gostos(self):
        
        dados = self.carregar()
        
        return dados["preferencias"]["gostos"]
