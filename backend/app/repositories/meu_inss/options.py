from app.database.database import db
from app.repositories.collections import step

meu_inss_options = {

    "code": "MI_01",
    "service_name": "Meu INSS",
    "message": "Olá! O que você deseja fazer no Meu INSS hoje?",
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
            "text": "Voltar para a tela inicial",
            "next step": "MENU"
        },

    ]

}

insert_meu_inss_options = step.insert_one(meu_inss_options)
