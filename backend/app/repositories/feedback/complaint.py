from app.database.database import db
from app.repositories.collections import step

complaint_steps = [

    {

        "code": "FB_FR_01",
        "service_name": "Feedback",
        "message": "Conte para a gente o que aconteceu para que possamos melhorar",
        "options": [


            {
                "text": "Enviar",
                "next step": "FB_FR_02"
            }

        ]

    },

    {

        "code": "FB_FR_02",
        "service_name": "Feedback",
        "message": "Mensagem enviada com sucesso!",
        "show_with_next": True,
        "next step": "FB_FR_03"

    },

    {
        "code": "FB_FR_03",
        "service_name": "Feedback",
        "message": "Obrigado por ajudar a melhorar o Guia Fácil.",
        "options": [

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            },


        ]

    }

]

for documento in complaint_steps:
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
