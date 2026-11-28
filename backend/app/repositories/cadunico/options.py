from app.database.database import db
from app.repositories.collections import step

cadunico_options = {

    "code": "CU_01",
    "service_name": "CadÚnico",
    "message": "O que você necessita em relação ao CadÚnico?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": "CU_CC_01"
        },

        {
            "text": "Baixar aplicativo",
            "next step": "CU_BA_01"
        },

        {
            "text": "Voltar para a página inicial",
            "next step": "MENU"
        }

    ]

}

step.update_one(
    {"code": cadunico_options["code"]},
    {"$set": cadunico_options},
    upsert=True,
)
