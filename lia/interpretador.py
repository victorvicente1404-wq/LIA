class Interpretador:

    def normalizar(self, texto):

        texto = texto.lower()

        caracteres = {
            "á":"a","à":"a","ã":"a","â":"a",
            "é":"e","ê":"e",
            "í":"i",
            "ó":"o","ô":"o","õ":"o",
            "ú":"u",
            "ç":"c"
        }

        for antigo, novo in caracteres.items():
            texto = texto.replace(antigo, novo)

        return texto

    def interpretar(self, texto):

        texto = self.normalizar(texto)

        if texto.startswith("o que e "):
            return "PERGUNTAR"

        if texto.startswith("quem e "):
            return "PERGUNTAR"

        if texto.startswith("qual e "):
            return "PERGUNTAR"

        if texto.startswith("meu nome e "):
            return "NOME"

        if texto.startswith("gosto de "):
            return "GOSTO"

        if " e " in texto:
            return "APRENDER"

        return "DESCONHECIDO"
