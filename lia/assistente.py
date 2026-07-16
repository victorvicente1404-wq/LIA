from .interpretador import Interpretador
from .memoria import Memoria


class Lia:

    def __init__(self):

        self.interpretador = Interpretador()
        self.memoria = Memoria()

    def iniciar(self):

        print("Lia: Ola!")

        nome = self.memoria.ler("nome")

        if not nome:

            nome = input("Lia: Qual e o seu nome? ")

            self.memoria.guardar("nome", nome)

        print(f"Lia: Prazer em conhece-lo, {nome}!")

        pergunta = input("Voce: ")

        intencao = self.interpretador.interpretar(pergunta)

        if intencao == "PERGUNTAR_NOME":

            print(f"Lia: Seu nome e {self.memoria.ler('nome')}.")

        else:

            print("Lia: Ainda estou aprendendo.")
