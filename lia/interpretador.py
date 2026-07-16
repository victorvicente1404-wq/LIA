class Interpretador:

    def normalizar(self, texto):

        texto = texto.lower()

        caracteres = {
            "á": "a",
            "à": "a",
            "ã": "a",
            "â": "a",
            "é": "e",
            "ê": "e",
            "í": "i",
            "ó": "o",
            "ô": "o",
            "õ": "o",
            "ú": "u",
            "ç": "c"
        }

        for antigo, novo in caracteres.items():
            texto = texto.replace(antigo, novo)

        return texto

    def interpretar(self, texto):

        texto = self.normalizar(texto)

        if "meu nome" in texto:
            return "PERGUNTAR_NOME"

        if "quem eu sou" in texto:
            return "PERGUNTAR_NOME"

        return "DESCONHECIDO"
