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

                nome = self.memoria.ler_nome()

                if nome:
                    print(f"Lia: Seu nome e {nome}.")
                else:
                    print("Lia: Ainda nao sei seu nome.")

            elif acao == "SALVAR_GOSTO":

                self.memoria.adicionar_gosto(resultado["gosto"])

                print("Lia: Entendido. Vou lembrar disso.")

            elif acao == "SALVAR_JOGO":

                self.memoria.guardar_jogo_favorito(resultado["jogo"])

                print(f"Lia: Legal! Vou lembrar que seu jogo favorito e {resultado['jogo']}.")

            elif acao == "RESPONDER_JOGO":

                jogo = self.memoria.ler_jogo_favorito()

                if jogo:
                    print(f"Lia: Seu jogo favorito e {jogo}.")
                else:
                    print("Lia: Voce ainda nao me contou seu jogo favorito.")

            elif acao == "APRENDER":

                self.memoria.aprender(
                    resultado["objeto"],
                    resultado["descricao"]
                )

                print(f"Lia: Aprendi o que e {resultado['objeto']}.")

            elif acao == "CONSULTAR":

                resposta = self.memoria.consultar(
                    resultado["objeto"]
                )

                if resposta:

                    print(f"Lia: {resultado['objeto']} e {resposta}")

                else:

                    print("Lia: Ainda nao sei isso. Pode me ensinar.")

            else:

                print("Lia: Ainda nao entendi.")
