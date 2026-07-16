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

        intencao = self.interpretador.interpretar(pergunta)

        if intencao == "APRENDER":

            partes = pergunta.split(" e ", 1)

            if len(partes) == 2:

                objeto = partes[0].strip()

                descricao = partes[1].strip()

                self.memoria.aprender(objeto, descricao)

                print("Lia: Entendido. Vou lembrar disso.")

        elif intencao == "PERGUNTAR":

            objeto = pergunta.lower()

            objeto = objeto.replace("o que e", "")

            objeto = objeto.strip()

            resposta = self.memoria.consultar(objeto)

            if resposta:

                print(f"Lia: {objeto} e {resposta}")

            else:

                print("Lia: Ainda nao sei. Pode me ensinar.")

        else:

            print("Lia: Ainda estou aprendendo.")
