from app.database.database import db
from app.repositories.collections import step

atende_mais_options = {

    "code": "AM_1",
    "service_name": "Atende+",
    "message": "O que você necessita em relação ao Atende+?",
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
            "text": "Marcar viagem",
            "next step": "AM_MV_01"
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
