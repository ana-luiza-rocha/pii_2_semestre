# ============================================== #
# ESTE CÓDIGO SERVE PARA CARREGAR E VALIDAR /
# A CONFIGURAÇÃO DO BANCO E SUAS CREDENCIAIS.
# ============================================== #

import os
from pathlib import Path
from urllib.parse import quote

# Precisa disto para pegar as credenciais do banco, as quais estão armazenadas no .env
from dotenv import load_dotenv

# Pega o caminho do arquivo atual, torna ele absoluto e vai até o root do projeto
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

MONGODB_DB = os.getenv("MONGODB_DB") or os.getenv("MONGO_DB")
MONGODB_URI = os.getenv("MONGODB_URI")

# Docker Compose provides the MONGO_* variables to the seed container.
# Build a container-to-container URI when a full URI was not provided.
if not MONGODB_URI:
    mongo_host = os.getenv("MONGO_HOST")
    mongo_port = os.getenv("MONGO_PORT", "27017")
    mongo_user = os.getenv("MONGO_ROOT_USER")
    mongo_password = os.getenv("MONGO_ROOT_PASSWORD")

    if mongo_host and mongo_user and mongo_password:
        encoded_user = quote(mongo_user, safe="")
        encoded_password = quote(mongo_password, safe="")
        MONGODB_URI = (
            f"mongodb://{encoded_user}:{encoded_password}@"
            f"{mongo_host}:{mongo_port}/?authSource=admin"
        )

# Para verificar se realmente existem o username e a password neste ambiente
if not MONGODB_URI:
    raise RuntimeError("Não foi possível gerar o URI do Banco.")

if not MONGODB_DB:
    raise RuntimeError("Nome da database está faltando neste environment.")

if __name__ == "__main__":
    print("Sucesso")
