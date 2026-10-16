# ESTE CÓDIGO SERVE PARA CARREGAR E VALIDAR /
# A CONFIGURAÇÃO DO BANCO E SUAS CREDENCIAIS.

import os
from pathlib import Path

# Precisa disto para pegar as credenciais do banco, as quais estão armazenadas no .env
from dotenv import load_dotenv

# Pega o caminho do arquivo atual, torna ele absoluto e vai até o root do projeto
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_DB = os.getenv("MONGO_DB")

MONGO_ROOT_USER = os.getenv("MONGO_ROOT_USER")
MONGO_ROOT_PASSWORD = os.getenv("MONGO_ROOT_PASSWORD")

# Para verificar se realmente existem o username e a password neste ambiente
if not MONGO_ROOT_USER or not MONGO_ROOT_PASSWORD:
    raise RuntimeError("Credenciais do MongoDB estão faltando neste environment.")

if not MONGO_DB:
    raise RuntimeError("Nome da database está faltando neste environment.")

if __name__ == "__main__":
    print("Sucesso")