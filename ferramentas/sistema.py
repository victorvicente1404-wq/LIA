"""
Ferramentas de Sistema da Lia.
Permite interagir com o sistema operacional.
"""

import os
import platform
import psutil
from datetime import datetime


class Sistema:

    @staticmethod
    def informacoes_sistema():
        """Retorna informações básicas do sistema."""
        try:
            info = {
                "sistema": platform.system(),
                "versao": platform.version(),
                "arquitetura": platform.machine(),
                "processador": platform.processor(),
                "ram_total": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
                "ram_usada": f"{psutil.virtual_memory().used / (1024**3):.2f} GB",
                "hora_atual": datetime.now().strftime("%H:%M:%S"),
                "data_atual": datetime.now().strftime("%d/%m/%Y")
            }
            return info
        except:
            return {"erro": "Não foi possível obter informações do sistema."}

    @staticmethod
    def listar_arquivos(diretorio="."):
        """Lista arquivos em um diretório."""
        try:
            arquivos = os.listdir(diretorio)
            return arquivos
        except Exception as e:
            return f"Erro ao listar arquivos: {str(e)}"

    @staticmethod
    def abrir_programa(nome_programa):
        """Tenta abrir um programa (funciona melhor no Windows)."""
        try:
            if platform.system() == "Windows":
                os.startfile(nome_programa)
                return f"Programa {nome_programa} aberto com sucesso!"
            else:
                return "Abertura automática de programas disponível apenas no Windows por enquanto."
        except Exception as e:
            return f"Não foi possível abrir {nome_programa}: {str(e)}"

    @staticmethod
    def status_bateria():
        """Retorna status da bateria (se disponível)."""
        try:
            bateria = psutil.sensors_battery()
            if bateria:
                return {
                    "percentual": bateria.percent,
                    "carregando": bateria.power_plugged
                }
            return "Bateria não detectada."
        except:
            return "Não foi possível verificar a bateria."
