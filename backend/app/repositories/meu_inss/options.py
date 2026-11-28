from app.database.database import db
from app.repositories.collections import step

meu_inss_options = {

    "code": "MI_01",
    "service_name": "Meu INSS",
    "message": "O que você necessita em relação a plataforma “Meu INSS”?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": "MI_CC_01"
        }, 

        {
            "text": "Consultar um benefício",
            "next step": "" #o fluxo de benefício não existe ainda!
        },

        {
            "text": "Voltar para a página inicial",
            "next step": "MENU"
        }  

    ]

}

step.update_one(
    {"code": meu_inss_options["code"]},
    {"$set": meu_inss_options},
    upsert=True,
)
