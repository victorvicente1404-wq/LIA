class Lia:

    def __init__(self):
        self.nome_usuario = ""

    def normalizar(self, texto):

        texto = texto.lower()

        texto = texto.replace("é", "e")
        texto = texto.replace("ê", "e")
        texto = texto.replace("á", "a")
        texto = texto.replace("à", "a")
        texto = texto.replace("ã", "a")
        texto = texto.replace("â", "a")
        texto = texto.replace("í", "i")
        texto = texto.replace("ó", "o")
        texto = texto.replace("ô", "o")
        texto = texto.replace("õ", "o")
        texto = texto.replace("ú", "u")
        texto = texto.replace("ç", "c")

        return texto

    def iniciar(self):

        print("Lia: Ola!")

        self.nome_usuario = input("Lia: Qual e o seu nome? ")

        print(f"Lia: Prazer em conhece-lo, {self.nome_usuario}!")

        pergunta = input("Voce: ")

        pergunta = self.normalizar(pergunta)

        if (
            "meu nome" in pergunta
            or "quem eu sou" in pergunta
        ):

            print(f"Lia: Seu nome e {self.nome_usuario}.")

        else:

            print("Lia: Ainda estou aprendendo.")
