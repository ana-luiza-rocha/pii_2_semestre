# ============================================== #
# ESTE CÓDIGO SERVE PARA FAZER DE FATO A CONEXÃO /
# COM O BANCO. A VARIAVEL 'db' AQUI DECLARADA /
# REPRESENTA O BANCO A SER USADO
# ============================================== #

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
    MONGODB_DB,
    MONGODB_URI
)

client = MongoClient(MONGODB_URI, timeoutMS=5000)

db = client[MONGODB_DB]

# a função abaixo serve para verificar se
# o MongoDB está responsivo e "alcançável"
def check_connection():
    try:
        client.admin.command("ping")
        return True

    except PyMongoError as e:
        print(f"\033[91m{type(e)}\033[00m")
        print(f"\033[38;2;255;165;0m{e}\033[0m")
        return False

# praticidade.
def close_connection():
    client.close()

if __name__ == "__main__":
    TESTING = True

    if TESTING == True:
        print("== TESTANDO ==")

        print(f"Conexão responsiva: {check_connection()} (True)")
        print("Fechando conexão...")
        close_connection()
        print(f"Conexão responsiva: {check_connection()} (False)")

        print("== FIM DO TESTE ==")

    # ÚLTIMO TESTE FOI BEM SUCEDIDO (17out2026-16h22min)
