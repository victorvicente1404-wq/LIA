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

        if " o que e " in f" {texto} ":
            return "PERGUNTAR"

        if " e " in texto:
            return "APRENDER"

        return "DESCONHECIDO"
