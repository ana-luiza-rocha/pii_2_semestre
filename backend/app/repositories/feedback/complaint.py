from database import db
from collections import step

complaint_steps = [

    {

        "code": "FB_FR_01",
        "service_name": "Feedback",
        "message": "Conte para a gente o que aconteceu para que possamos melhorar",
        "options": [

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            },

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
        "next step": "FB_FR_03"

    },

    {
        "code": "FB_FR_03",
        "service_name": "Feedback",
        "message": "Obrigado por ajudar a melhorar o Guia Fácil.",
        "options": [

            {
                "text": "Voltar à pergunta anterior",
            },

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            }

        ]

    }

]

