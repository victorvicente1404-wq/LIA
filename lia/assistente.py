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

            pergunta_normal = self.interpretador.normalizar(pergunta)

            intencao = self.interpretador.interpretar(pergunta)

            if intencao == "NOME":

                nome = pergunta[12:].strip()

                self.memoria.guardar_nome(nome)

                print(f"Lia: Entendido. Seu nome e {nome}.")

            elif intencao == "GOSTO":

                gosto = pergunta[9:].strip()

                self.memoria.adicionar_gosto(gosto)

                print("Lia: Vou lembrar disso.")

            elif intencao == "APRENDER":

                partes = pergunta.split(" e ", 1)

                if len(partes) > 1:

                    objeto = partes[0].strip()

                    descricao = partes[1].strip()

                    self.memoria.aprender(objeto, descricao)

                    print("Lia: Aprendi isso.")

                else:

                    print("Lia: Nao consegui aprender. Tente novamente.")

            elif intencao == "PERGUNTAR":

                objeto = pergunta_normal

                objeto = objeto.replace("o que e ", "")
                objeto = objeto.replace("quem e ", "")
                objeto = objeto.replace("qual e ", "")

                objeto = objeto.strip()

                resposta = self.memoria.consultar(objeto)

                if resposta:

                    print(f"Lia: {objeto} e {resposta}")

                else:

                    print("Lia: Ainda nao sei isso. Pode me ensinar.")

            else:

                print("Lia: Ainda nao entendi.")
