from database import db

step = db["step"]

compliment_steps = [

    {

        "code": "FB_EE_01",
        "service_name": "Feedback",
        "message": "Conte para a gente o que você gostou no Guia Fácil.",
        "options": [

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            },

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
        "next step": "FB_EE_03"

    },

    {
        "code": "FB_EE_03",
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

