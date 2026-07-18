"""
Memória IA da Lia.
Responsável por gerenciar memória de conversas e contexto com IAs externas.
"""

import json
import os
from datetime import datetime


class MemoriaIA:

    def __init__(self):
        self.arquivo = "data/memoria_ia.json"
        self.historico = []
        self.carregar()

    def carregar(self):
        """Carrega a memória salva."""
        try:
            if os.path.exists(self.arquivo):
                with open(self.arquivo, "r", encoding="utf-8") as f:
                    self.historico = json.load(f)
            else:
                self.salvar()
        except Exception:
            self.historico = []

    def salvar(self):
        """Salva a memória em arquivo."""
        try:
            os.makedirs("data", exist_ok=True)
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(self.historico, f, indent=4, ensure_ascii=False)
        except Exception:
            pass

    def adicionar(self, mensagem_usuario: str, resposta_lia: str):
        """Adiciona uma interação ao histórico."""
        entrada = {
            "timestamp": datetime.now().isoformat(),
            "usuario": mensagem_usuario,
            "lia": resposta_lia
        }
        self.historico.append(entrada)
        
        # Mantém apenas as últimas 50 interações
        if len(self.historico) > 50:
            self.historico = self.historico[-50:]
        
        self.salvar()

    def obter_contexto(self, limite=10):
        """Retorna contexto recente para usar em prompts de IA."""
        if not self.historico:
            return ""
        
        contexto = "Histórico recente de conversa:\n"
        for item in self.historico[-limite:]:
            contexto += f"Usuário: {item['usuario']}\n"
            contexto += f"Lia: {item['lia']}\n\n"
        
        return contexto

    def limpar(self):
        """Limpa toda a memória."""
        self.historico = []
        self.salvar()
