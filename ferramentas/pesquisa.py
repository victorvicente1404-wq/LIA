import logging
from duckduckgo_search import DDGS

# Configuração do Logger para registrar o comportamento da busca
logger = logging.getLogger(__name__)

def pesquisar_web(termo: str, max_resultados: int = 3) -> list:
    """
    Realiza uma busca rápida na internet utilizando o motor do DuckDuckGo.
    
    Argumentos:
        termo (str): A frase ou palavra-chave que o usuário quer pesquisar.
        max_resultados (int): O limite de links que queremos retornar (padrão: 3).
        
    Retorna:
        list: Uma lista de dicionários contendo 'titulo', 'link' e 'resumo'.
    """
    try:
        logger.info(f"Iniciando pesquisa web para o termo: '{termo}'")
        
        # Instancia o buscador do DuckDuckGo
        with DDGS() as ddgs:
            resultados = list(ddgs.text(termo, max_results=max_resultados))
            
        if not resultados:
            logger.warning(f"Nenhum resultado foi encontrado para a busca: '{termo}'")
            return []
            
        # Formata e limpa a resposta para manter o sistema leve
        resultados_formatados = []
        for res in resultados:
            resultados_formatados.append({
                "titulo": res.get("title", "Sem título"),
                "link": res.get("href", ""),
                "resumo": res.get("body", "Sem descrição disponível.")
            })
            
        logger.info(f"Pesquisa concluída com sucesso. {len(resultados_formatados)} resultados obtidos.")
        return resultados_formatados

    except Exception as e:
        logger.error(f"Erro crítico ao executar a pesquisa na internet: {e}", exc_info=True)
        return []
