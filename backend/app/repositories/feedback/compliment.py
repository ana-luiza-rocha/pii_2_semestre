from app.database.database import db
from app.repositories.collections import step

compliment_steps = [

    {

        "code": "FB_EE_01",
        "service_name": "Feedback",
        "message": "Conte para a gente o que você gostou no Guia Fácil.",
        "options": [


            {
                "text": "Enviar",
                "next step": "FB_EE_02"
            }

        ]

    },

    {

        "code": "FB_EE_02",
        "service_name": "Feedback",
        "message": "Mensagem enviada com sucesso!",
        "show_with_next": True,
        "next step": "FB_EE_03"

    },

    {
        "code": "FB_EE_03",
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

for documento in compliment_steps:
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
