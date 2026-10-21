from app.database.database import db
from app.repositories.collections import step

atende_mais_options = {

    "code": "AM_1",
    "service_name": "Atende+",
    "message": "O que você deseja fazer no Atende+ hoje?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": "AM_CC_01"
        }, 

        {
            "text": "Obter ficha médica",
            "next step": "AM_OFM_01"
        }, 

        {
            "text": "Voltar para a página inicial",
            "next step": "MENU"
        }  

    ]

}

step.update_one(
    {"code": atende_mais_options["code"]},
    {"$set": atende_mais_options},
    upsert=True,
)
