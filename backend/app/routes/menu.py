from fastapi import FastAPI

app = FastAPI()

# rota para retornar o nome dos serviços encontrados no site: Atende+ e meu INSS
@app.get("/services")
def services():
    return find_available_services()

# rota para retornar o nome usado no botão de suporte
@app.get("/support")
def support():
    return find_support_title()