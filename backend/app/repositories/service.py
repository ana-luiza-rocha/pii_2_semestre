from app.database.database import db
from app.repositories.collections import service

atende_mais = {
    "code": "atende+",
    "name": "Atende+",
    "description": "Criar conta, obter ficha médica e marcar viagem",
    "initial_step": "AM_1"
}

meu_inss = {
    "code": "meu-inss",
    "name": "Meu INSS",
    "description": "Criar conta",
    "initial_step": "MI_01"
}

cadunico = {
    "code": "cadunico",
    "name": "CadÚnico",
    "description": "Criar conta e baixar aplicativo",
    "initial_step": "CU_01"
}

feedback = {
    "code": "feedback",
    "name": "Sugestões e reclamações",
    "initial_step": "FB_01"
}

for documento in [atende_mais, meu_inss, cadunico, feedback]:
    service.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )

def ordenar_servicos(itens):
    ordem = ["atende+", "meu-inss", "cadunico"]
    lista = []
    for code in ordem:
        for item in itens:
            if item["code"] == code:
                lista.append(item)
    return lista

def find_available_services():
    itens = list(db.service.find(
        {"code": {"$ne": "feedback"}},
        {"_id": 0, "code": 1, "name": 1}
    ))
    return ordenar_servicos(itens)


def find_support_title():
    return db.service.find({"code": "feedback"}, {"_id": 0, "name": 1})


def find_services_descriptions():
    itens = list(db.service.find(
        {"code": {"$ne": "feedback"}},
        {"_id": 0, "code": 1, "description": 1}
    ))
    return ordenar_servicos(itens)
