from app.database.database import db
from app.repositories.collections import service

atende_mais = {
    "code": "atende+",
    "name": "Atende+",
    "description": "Agendamentos e serviços",
    "initial_step": "AM_01"
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

insert_services = service.insert_many([atende_mais, meu_inss, feedback])
