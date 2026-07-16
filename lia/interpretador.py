class Interpretador:

    def normalizar(self, texto):

        texto = texto.lower().strip()

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

        texto = texto.replace("?", "")

        # ==========================
        # NOME
        # ==========================

        if texto.startswith("meu nome e "):

            return {
                "acao": "SALVAR_NOME",
                "nome": texto[11:].strip()
            }

        if texto in [
            "qual meu nome",
            "qual e meu nome",
            "quem sou eu",
            "como eu me chamo"
        ]:

            return {
                "acao": "RESPONDER_NOME"
            }

        # ==========================
        # JOGO FAVORITO
        # ==========================

        if texto.startswith("meu jogo favorito e "):

            return {
                "acao": "SALVAR_JOGO",
                "jogo": texto[20:].strip()
            }

        if texto in [
            "qual meu jogo favorito",
            "qual e meu jogo favorito"
        ]:

            return {
                "acao": "RESPONDER_JOGO"
            }

        # ==========================
        # GOSTOS
        # ==========================

        if texto.startswith("gosto de "):

            return {
                "acao": "SALVAR_GOSTO",
                "gosto": texto[9:].strip()
            }

        # ==========================
        # CONSULTAS
        # ==========================

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

        if texto.startswith("qual e "):

            return {
                "acao": "CONSULTAR",
                "objeto": texto[7:].strip()
            }

        # ==========================
        # APRENDER
        # ==========================

        if " e " in texto:

            partes = texto.split(" e ", 1)

            if len(partes) == 2:

                return {
                    "acao": "APRENDER",
                    "objeto": partes[0].strip(),
                    "descricao": partes[1].strip()
                }

        # ==========================
        # DESCONHECIDO
        # ==========================

        return {
            "acao": "DESCONHECIDO"
                }
