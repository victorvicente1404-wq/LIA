import logging
from lia.pesquisa import SistemaPesquisa

# Configuração do Logger
logger = logging.getLogger(__name__)

class InterpretadorLIA:
    def __init__(self):
        """
        Inicializa o interpretador de comandos e mensagens da LIA.
        """
        self.sistema_pesquisa = SistemaPesquisa()
        
        # Lista de gatilhos comuns que indicam a necessidade de buscar dados em tempo real
        self.gatilhos_pesquisa = [
            "pesquise sobre", "pesquisa", "busque no google", "procure por",
            "quem é", "quem foi", "o que é", "o que significa",
            "notícias sobre", "últimas de", "tempo hoje", "como está o"
        ]

    def interpretar(self, texto_usuario: str) -> dict:
        """
        Analisa o texto enviado pelo usuário para identificar a intenção, 
        realizar pesquisas se necessário e estruturar a carga de dados para a IA.
        
        Argumentos:
            texto_usuario (str): A mensagem bruta digitada ou dita pelo usuário.
            
        Retorna:
            dict: Um dicionário contendo o texto final processado e metadados da intenção.
        """
        if not texto_usuario:
            return {"intencao": "vazia", "texto_processado": "", "contexto_pesquisa": ""}

        texto_minusc = texto_usuario.lower().strip()
        logger.info(f"Interpretando entrada do usuário: '{texto_usuario}'")

        # Verifica se a mensagem exige uma pesquisa externa
        precisa_pesquisa = any(gatilho in texto_minusc for gatilho in self.gatilhos_pesquisa)
        
        contexto_pesquisa = ""
        intencao = "conversa_geral"

        if precisa_pesquisa:
            logger.info("Gatilho de pesquisa detectado. Iniciando busca externa...")
            intencao = "pesquisa_web"
            
            # Limpa os prefixos de comando comuns para refinar a busca no DuckDuckGo
            termo_busca = texto_usuario
            for gatilho in self.gatilhos_pesquisa:
                if texto_minusc.startswith(gatilho):
                    termo_busca = texto_usuario[len(gatilho):].strip(" ?,.")
                    break
            
            # Executa a pesquisa e pega o bloco de texto formatado com as fontes
            contexto_pesquisa = self.sistema_pesquisa.pesquisar_e_sintetizar(termo_busca)

        # Monta o prompt final enriquecido que será enviado para a IA
        if contexto_pesquisa:
            texto_processado = f"{contexto_pesquisa}\n\nCom base nas informações acima, responda ao usuário de forma natural:\n{texto_usuario}"
        else:
            texto_processado = texto_usuario

        resultado = {
            "intencao": intencao,
            "texto_processado": texto_processado,
            "contexto_pesquisa": contexto_pesquisa
        }

        logger.info(f"Interpretação concluída. Intenção identificada: {intencao}")
        return resultado
