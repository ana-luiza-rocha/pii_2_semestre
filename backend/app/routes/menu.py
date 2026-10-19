from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.repositories.service import find_available_services, find_support_title, find_services_descriptions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# rota para retornar o nome dos serviços encontrados no site: Atende+ e meu INSS
@app.get("/services")
def services():
    result = find_available_services()
    return [service["name"] for service in result]

# rota para retornar o nome usado no botão de suporte
@app.get("/support")
def support():
    result = find_support_title()
    return [service["name"] for service in result]


@app.get("/services/descriptions")
def services_descriptions():
    result = find_services_descriptions()
    return [service["description"] for service in result]
