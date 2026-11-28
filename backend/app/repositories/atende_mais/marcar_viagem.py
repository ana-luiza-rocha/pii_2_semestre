from app.database.database import db
from app.repositories.collections import step

marcar_viagem_steps = [

    {

        "code": "AM_MV_01",
        "service_name": "Atende+",
        "message": "Você já tem cadastro no Atende+?",
        "options": [

            {
                "text": "Sim, já tenho",
                "next step": "AM_MV_02"
            },

            {
                "text": "Não tenho",
                "next step": "AM_MV_03"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_MV_02",
        "service_name": "Atende+",
        "message": "Ótimo! Abaixo, você encontrará um vídeo com o passo a passo para marcar sua viagem no site do Atende+.",
        "video_path": "videos/Marcar_viagem_atende_mais.mp4",
        "next step": "AM_CC_07"

    },

    {

        "code": "AM_MV_03",
        "service_name": "Atende+",
        "message": "Quer ver como fazer seu cadastro no Atende+?",
        "options": [

            {
                "text": "Sim, ver tutorial",
                "next step": "AM_CC_01"
            },

            {
                "text": "Não, obrigado",
                "next step": "AM_CC_04"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

]

for documento in marcar_viagem_steps:
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
