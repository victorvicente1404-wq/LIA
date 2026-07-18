import logging
from ferramentas.pesquisa import pesquisar_web

# Configuração do Logger
logger = logging.getLogger(__name__)

class SistemaPesquisa:
    def __init__(self):
        """
        Inicializa o gerenciador do sistema de pesquisas da LIA.
        """
        pass

    def pesquisar_e_sintetizar(self, pergunta: str) -> str:
        """
        Realiza a pesquisa baseada na dúvida do usuário e formata os dados
        em um bloco de texto legível para enriquecer o contexto da IA.
        
        Argumentos:
            pergunta (str): A dúvida ou comando enviado pelo usuário.
            
        Retorna:
            str: Bloco de texto com os dados da internet ou mensagem de erro.
        """
        logger.info(f"SistemaPesquisa acionado para a pergunta: '{pergunta}'")
        
        # Executa a busca web trazendo até 3 resultados
        resultados = pesquisar_web(pergunta, max_resultados=3)
        
        if not resultados:
            logger.warning("SistemaPesquisa não obteve resultados válidos da ferramenta web.")
            return "AVISO DO SISTEMA: Não foi possível obter informações recentes da internet para esta pergunta."
            
        # Constrói o cabeçalho do contexto que a IA vai ler
        contexto = (
            "=========================================================\n"
            "INFORMAÇÕES EM TEMPO REAL OBTIDAS DA INTERNET:\n"
            "Use os dados abaixo para responder ao usuário com precisão.\n"
            "=========================================================\n\n"
        )
        
        # Adiciona cada resultado formatado ao bloco de texto
        for i, res in enumerate(resultados, 1):
            contexto += f"Fonte [{i}]: {res['titulo']}\n"
            contexto += f"Link de Referência: {res['link']}\n"
            contexto += f"Conteúdo extraído: {res['resumo']}\n"
            contexto += "---------------------------------------------------------\n"
            
        contexto += "\nFIM DAS INFORMAÇÕES DA INTERNET. Prossiga com a resposta final utilizando os dados acima."
        
        logger.info("Contexto de pesquisa gerado e sintetizado com sucesso.")
        return contexto
