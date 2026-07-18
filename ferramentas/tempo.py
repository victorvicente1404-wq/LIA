"""
Ferramenta de Tempo da Lia.
Responsável por pegar data, hora e informações relacionadas ao tempo.
"""

from datetime import datetime
import locale


class Tempo:

    @staticmethod
    def obter_hora():
        """Retorna a hora atual formatada."""
        agora = datetime.now()
        return agora.strftime("%H:%M")

    @staticmethod
    def obter_data():
        """Retorna a data atual formatada."""
        agora = datetime.now()
        return agora.strftime("%d de %B de %Y")

    @staticmethod
    def obter_dia_semana():
        """Retorna o dia da semana atual."""
        try:
            locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        except:
            pass  # se não conseguir, usa o padrão
        agora = datetime.now()
        return agora.strftime("%A")

    @staticmethod
    def saudacao():
        """Retorna saudação de acordo com o horário."""
        hora = datetime.now().hour

        if 5 <= hora < 12:
            return "Bom dia"
        elif 12 <= hora < 18:
            return "Boa tarde"
        else:
            return "Boa noite"

    @staticmethod
    def informacoes_completas():
        """Retorna todas as informações de tempo juntas."""
        return {
            "saudacao": Tempo.saudacao(),
            "hora": Tempo.obter_hora(),
            "data": Tempo.obter_data(),
            "dia": Tempo.obter_dia_semana()
        }
