"""
Ferramenta de Calculadora da Lia.
Permite fazer cálculos matemáticos simples.
"""

import re
import math


class Calculadora:

    @staticmethod
    def calcular(expressao: str):
        """
        Avalia uma expressão matemática simples.
        Ex: "2 + 2", "5 * 3", "10 / 2", "2**3", "sqrt(16)"
        """
        try:
            # Remove espaços extras
            expr = expressao.strip().lower()

            # Suporte a funções matemáticas
            if "sqrt" in expr:
                numero = float(re.search(r"sqrt\((\d+)\)", expr).group(1))
                return math.sqrt(numero)

            if "pi" in expr:
                expr = expr.replace("pi", str(math.pi))

            # Avalia expressão segura (apenas operações básicas)
            # Usando eval com restrição de contexto
            resultado = eval(
                expr,
                {"__builtins__": {}},
                {
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "log": math.log,
                    "sqrt": math.sqrt,
                    "pi": math.pi,
                    "e": math.e
                }
            )

            # Formata o resultado
            if isinstance(resultado, float):
                if resultado.is_integer():
                    return int(resultado)
                return round(resultado, 6)
            
            return resultado

        except Exception:
            return "Não consegui calcular isso. Tente algo como: 2 + 2 ou 5 * 3"

    @staticmethod
    def eh_calculo(mensagem: str) -> bool:
        """Verifica se a mensagem parece ser um cálculo."""
        palavras_calculo = ["+", "-", "*", "/", "**", "sqrt", "calcule", "quanto é"]
        mensagem_lower = mensagem.lower()
        return any(palavra in mensagem_lower for palavra in palavras_calculo)
