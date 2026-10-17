# ============================================== #
# ESTE CÓDIGO SERVE PARA FAZER DE FATO A CONEXÃO /
# COM O BANCO. A VARIAVEL 'db' AQUI DECLARADA /
# REPRESENTA O BANCO A SER USADO
# ============================================== #

# biblioteca para URL
from urllib.parse import quote_plus

# === PYMONGO ===#
from pymongo import MongoClient

# isto serve para usar o try-except na hora de verificar se há conexão
from pymongo.errors import PyMongoError
#================#

# == CONSIDERAÇÃO == #
# caso for rodar apenas este arquivo, deixe apenas 'from db_config import...',
# mas caso for rodar da main, coloque todo o caminho do diretorio da main até
# este arquivo no import de db_config

# para usar este arquivo, importe o seguinte: db, check_connection, close_connection
#====================#

from db_config import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_DB,
    MONGO_ROOT_USER,
    MONGO_ROOT_PASSWORD,
)

# formata para url
username = quote_plus(MONGO_ROOT_USER)
password = quote_plus(MONGO_ROOT_PASSWORD)

URI = (
    f"mongodb://{username}:{password}"
    f"@{MONGO_HOST}:{MONGO_PORT}/"
    "?authSource=admin"
)

client = MongoClient(URI)

db = client[MONGO_DB]

# a função abaixo serve para verificar se
# o MongoDB está responsivo e "alcançável"
def check_connection():
    try:
        client.admin.command("ping")
        return True

    except PyMongoError:
        return False

# praticidade.
def close_connection():
    client.close()

if __name__ == "__main__":
    TESTING = False

    if TESTING == True:
        print("== TESTANDO ==")

        print(f"Conexão responsiva: {check_connection()} (True)")
        print("Fechando conexão...")
        close_connection()
        print(f"Conexão responsiva: {check_connection()} (False)")

        print("== FIM DO TESTE ==")

    # ÚLTIMO TESTE FOI BEM SUCEDIDO (17out2026-16h22min)
