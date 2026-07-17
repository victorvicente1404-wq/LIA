"""
Sistema de respostas da Lia.
"""


class Respostas:

    @staticmethod
    def ola():

        return "Ola! Como posso ajudar?"

    @staticmethod
    def vazia():

        return "Pode escrever alguma coisa."

    @staticmethod
    def aprendido():

        return "Entendido. Vou lembrar disso."

    @staticmethod
    def nao_entendi():

        return (
            "Ainda nao consegui entender isso."
        )

    @staticmethod
    def nao_sei():

        return (
            "Ainda nao sei responder isso."
        )

    @staticmethod
    def desconhecido():

        return (
            "Nao encontrei nenhuma informacao."
        )

    @staticmethod
    def nome(nome):

        return f"Seu nome e {nome}."

    @staticmethod
    def conhecimento(descricao):

        return descricao

    @staticmethod
    def erro():

        return (
            "Ocorreu um erro interno."
        )
