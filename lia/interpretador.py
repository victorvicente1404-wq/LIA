class Interpretador:

    def normalizar(self, texto):

        texto = texto.lower().strip()

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

        texto = texto.replace("?", "")

        # ---------- PERGUNTAS ----------

        if texto in [
            "qual meu nome",
            "qual e meu nome",
            "quem sou eu",
            "como eu me chamo"
        ]:

            return {
                "acao": "RESPONDER_NOME"
            }

        if texto.startswith("o que e "):

            return {
                "acao": "CONSULTAR",
                "objeto": texto[7:].strip()
            }

        if texto.startswith("quem e "):

            return {
                "acao": "CONSULTAR",
                "objeto": texto[7:].strip()
            }

        # ---------- APRENDER ----------

        if texto.startswith("meu nome e "):

            return {
                "acao": "SALVAR_NOME",
                "nome": texto[11:].strip()
            }

        if texto.startswith("gosto de "):

            return {
                "acao": "SALVAR_GOSTO",
                "gosto": texto[9:].strip()
            }

        if texto.startswith("meu jogo favorito e "):

            return {
                "acao": "SALVAR_JOGO",
                "jogo": texto[20:].strip()
            }

        if " e " in texto:

            partes = texto.split(" e ", 1)

            return {
                "acao": "APRENDER",
                "objeto": partes[0].strip(),
                "descricao": partes[1].strip()
            }

        return {
            "acao": "DESCONHECIDO"
        }
