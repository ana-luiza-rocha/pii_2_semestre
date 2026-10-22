from app.database.database import db
from app.repositories.collections import step

get_medical_forms_steps = [

    {

        "code": "AM_OFM_01",
        "service_name": "Atende+",
        "message": "Abaixo, você encontrará um vídeo com o passo a passo para obter a sua ficha médica no site do Atende+.",
        "video_path": "videos/Obter_ficha_medica_atende_mais.mp4",
        "next step": "AM_OFM_02"

    },

    {

        "code": "AM_OFM_02",
        "service_name": "Atende+",
        "message": "Precisa de ajuda com mais alguma coisa?",
        "options": [

            {
                "text": "Sim",
                "next step": "AM_OFM_7"
            }, 

            {
                "text": "Não",
                "next step": "AM_OFM_03"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_OFM_03",
        "service_name": "Atende+",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui! Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "AM_OFM_04" 
            }, 

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            }, 


        ]

    },

    {

        "code": "AM_OFM_04",
        "service_name": "Atende+",
        "message": "Qual nota você daria para este tutorial?",
        "options": [

            {
                "text": "Enviar",
                "next step": "AM_OFM_05"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "AM_OFM_05",
        "service_name": "Atende+",
        "message": "Avaliação enviada com sucesso!",
        "show_with_next": True,
        "next step": "AM_OFM_06"

    },

    
    {

        "code": "AM_OFM_06",
        "service_name": "Atende+",
        "message": "Obrigado por ajudar a melhorar o Guia Fácil",
        "options": [

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            }, 


        ]

    },

    {

        "code": "AM_OFM_7",
        "service_name": "Atende+",
        "message": "Com qual serviço você gostaria de ajuda?",
        "options": [

            {
                "text": "Atende+",
                "next step": "AM_1"
            }, 

            {
                "text": "Meu INSS",
                "next step": "MI_01"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    }

]

for documento in get_medical_forms_steps:
    step.replace_one(
        {"code": documento["code"]},
        documento,
        upsert=True,
    )

current_step_codes = [documento["code"] for documento in get_medical_forms_steps]
step.delete_many({
    "code": {"$regex": "^AM_OFM_", "$nin": current_step_codes}
})
