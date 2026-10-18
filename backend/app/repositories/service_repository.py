from database import db

service = db["service"]

atende_mais = {
    "code": "atende+",
    "name": "Atende+",
    "description": "Agendamentos e serviços",
    "initial_step": "Olá! O que você deseja fazer no Atende+ hoje?"
}

meu_inss = {
    "code": "meu-inss",
    "name": "Meu INSS",
    "description": "Consultas e solicitações",
    "initial_step": "Olá! O que você deseja fazer no Meu INSS hoje?"
}

feedback = {
    "code": "feedback",
    "name": "Sugestões e reclamações",
    "initial_step": "O que você gostaria de fazer?"
}

inserir = service.insert_many(atende_mais, meu_inss, feedback)