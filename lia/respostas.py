import random


class Respostas:

    def ola(self):

        return random.choice([
            "Ola!",
            "Oi!",
            "Como posso ajudar?"
        ])

    def despedida(self):

        return random.choice([
            "Ate logo!",
            "Foi um prazer conversar com voce.",
            "Ate mais!"
        ])

    def aprendeu(self):

        return random.choice([
            "Entendido. Vou lembrar disso.",
            "Aprendi isso.",
            "Ok, vou guardar essa informacao."
        ])

    def nao_entendi(self):

        return random.choice([
            "Nao entendi.",
            "Pode explicar de outra forma?",
            "Ainda estou aprendendo."
        ])

    def nao_sei(self):

        return random.choice([
            "Ainda nao sei isso.",
            "Nao conheco essa informacao.",
            "Pode me ensinar?"
        ])

    def responder_nome(self, nome):

        return f"Seu nome e {nome}."

    def responder_jogo(self, jogo):

        return f"Seu jogo favorito e {jogo}."

    def responder_conhecimento(self, objeto, descricao):

        return f"{objeto} e {descricao}."
