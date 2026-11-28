from app.database.database import db
from app.repositories.collections import step

baixar_aplicativo_steps = [

    {

        "code": "CU_BA_01",
        "service_name": "CadÚnico",
        "message": "Vamos te ajudar a baixar o aplicativo do CadÚnico. Qual celular você usa?",
        "options": [

            {
                "text": "Motorola",
                "next step": "CU_BA_02"
            },

            {
                "text": "Samsung",
                "next step": "CU_BA_03"
            },

            {
                "text": "iPhone",
                "next step": "CU_BA_04"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "CU_BA_02",
        "service_name": "CadÚnico",
        "message": "Certo! Abaixo, você encontrará um vídeo com o passo a passo para baixar o aplicativo CadÚnico no Motorola.",
        "video_path": "videos/Baixar_cadunico_android.mp4",
        "next step": "CU_BA_05"

    },

    {

        "code": "CU_BA_03",
        "service_name": "CadÚnico",
        "message": "Certo! Abaixo, você encontrará um vídeo com o passo a passo para baixar o aplicativo CadÚnico no Samsung.",
        "video_path": "videos/Baixar_cadunico_android.mp4",
        "next step": "CU_BA_05"

    },

    {

        "code": "CU_BA_04",
        "service_name": "CadÚnico",
        "message": "Certo! Abaixo, você encontrará um vídeo com o passo a passo para baixar o aplicativo CadÚnico no iPhone.",
        "video_path": "videos/Baixar_cadunico_apple.mp4",
        "next step": "CU_BA_05"

    },

    {

        "code": "CU_BA_05",
        "service_name": "CadÚnico",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui. Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "CU_BA_06"
            },

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            },


        ]

    },

    {

        "code": "CU_BA_06",
        "service_name": "CadÚnico",
        "message": "Qual nota você daria para este tutorial?",
        "options": [

            {
                "text": "Enviar",
                "next step": "CU_BA_07"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "CU_BA_07",
        "service_name": "CadÚnico",
        "message": "Avaliação enviada com sucesso!",
        "show_with_next": True,
        "next step": "CU_BA_08"

    },

    {

        "code": "CU_BA_08",
        "service_name": "CadÚnico",
        "message": "Obrigado por ajudar a melhorar o Guia Fácil",
        "options": [

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            },


        ]

    },

]

for documento in baixar_aplicativo_steps:
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
