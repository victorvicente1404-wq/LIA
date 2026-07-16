from .interpretador import Interpretador


class Lia:

    def __init__(self):

        self.nome_usuario = ""
        self.interpretador = Interpretador()

    def iniciar(self):

        print("Lia: Ola!")

        self.nome_usuario = input("Lia: Qual e o seu nome? ")

        print(f"Lia: Prazer em conhece-lo, {self.nome_usuario}!")

        pergunta = input("Voce: ")

        intencao = self.interpretador.interpretar(pergunta)

        if intencao == "PERGUNTAR_NOME":

            print(f"Lia: Seu nome e {self.nome_usuario}.")

        else:

            print("Lia: Ainda estou aprendendo.")
