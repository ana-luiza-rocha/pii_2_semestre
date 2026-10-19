from app.database.database import db
from app.repositories.collections import service

atende_mais = {
    "code": "atende+",
    "name": "Atende+",
    "description": "Agendamentos e serviços",
    "initial_step": "AM_1"
}

meu_inss = {
    "code": "meu-inss",
    "name": "Meu INSS",
    "description": "Consultas e solicitações",
    "initial_step": "MI_01"
}

feedback = {
    "code": "feedback",
    "name": "Sugestões e reclamações",
    "initial_step": "FB_01"
}

for documento in [atende_mais, meu_inss, feedback]:
    service.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )

def find_available_services():
    return db.service.find({"code": { "$ne": "feedback"}},{"_id": 0,"name": 1}).sort("code", 1)


def find_support_title():
    return db.service.find({"code": "feedback"}, {"_id": 0, "name": 1})


def find_services_descriptions():
    return db.service.find({"code": {"$ne": "feedback"}}, {"_id": 0, "description": 1}).sort("code", 1)
