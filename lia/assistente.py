class Lia:

    def __init__(self):
        self.nome_usuario = ""

    def iniciar(self):

        print("Lia: Ola!")

        self.nome_usuario = input("Lia: Qual e o seu nome? ")

        print(f"Lia: Prazer em conhece-lo, {self.nome_usuario}!")

        pergunta = input("Voce: ")

        if pergunta.lower() == "qual e meu nome?":
            print(f"Lia: Seu nome e {self.nome_usuario}.")
        else:
            print("Lia: Ainda estou aprendendo.")
