from app.database.database import db
from app.repositories.collections import step

feedback_options = {

    "code": "FB_01",
    "service_name": "Sugestões e reclamações",
    "message": "O que você gostaria de fazer?",
    "options": [

        {
            "text": "Enviar uma sugestão",
            "next step": "FB_ES_01"
        }, 

        {
            "text": "Fazer uma reclamação",
            "next step": "FB_FR_01"
        }, 

        {
            "text": "Enviar um elogio",
            "next step": "FB_EE_01"
        }, 

        {
            "text": "Voltar para a tela inicial",
            "next step": "MENU"
        },

    ]

}

insert_feedback_options = step.insert_one(feedback_options)
