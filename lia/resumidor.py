"""
Resumidor da Lia.

Recebe várias respostas de diferentes fontes
e cria uma única resposta para o usuário.
"""


class Resumidor:

    @staticmethod
    def resumir(respostas):

        if not respostas:
            return None

        textos = []

        fontes = []

        for resposta in respostas:

            texto = resposta.get("resposta", "").strip()

            fonte = resposta.get("fonte", "Desconhecida")

            if texto:

                textos.append(texto)

                fontes.append(fonte)

        if not textos:

            return None

        # Remove respostas repetidas

        textos_unicos = []

        for texto in textos:

            if texto not in textos_unicos:

                textos_unicos.append(texto)

        resposta_final = "\n\n".join(textos_unicos)

        return {

            "resposta": resposta_final,

            "fontes": fontes

        }
