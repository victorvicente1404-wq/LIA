"""
Configurações da Lia.
Carrega variáveis do arquivo .env.
"""

import os

from dotenv import load_dotenv

# Carrega o arquivo .env
load_dotenv()

# -----------------------------
# APIs
# -----------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# -----------------------------
# Modelo padrão
# -----------------------------

OPENAI_MODEL = "gpt-5"

GEMINI_MODEL = "gemini-2.5-pro"

DEEPSEEK_MODEL = "deepseek-chat"

# -----------------------------
# Configurações da Lia
# -----------------------------

LIA_NOME = "Lia"

VERSAO = "0.2.0"
