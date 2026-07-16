from .interpretador import Interpretador
from .memoria import Memoria


class Lia:

    def __init__(self):

        self.interpretador = Interpretador()
        self.memoria = Memoria()

    def iniciar(self):

        print("Lia: Ola!")

        nome = self.memoria.ler_nome()

        if nome == "":
            nome = input("Lia: Qual e o seu nome? ")
            self.memoria.guardar_nome(nome)

        print(f"Lia: Prazer em conhece-lo, {nome}!")

        while True:

            pergunta = input("Voce: ")

            if pergunta.lower() in ["sair", "exit", "tchau"]:
                print("Lia: Ate logo!")
                break

            resultado = self.interpretador.interpretar(pergunta)

            acao = resultado["acao"]

            if acao == "SALVAR_NOME":

                self.memoria.guardar_nome(resultado["nome"])

                print(f"Lia: Entendido. Vou lembrar que seu nome e {resultado['nome']}.")

            elif acao == "RESPONDER_NOME":

                nome = self.memoria.l
