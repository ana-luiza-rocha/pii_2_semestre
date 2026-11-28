from app.database.database import db
from app.repositories.collections import step

criar_conta_steps = [

    {

        "code": "CU_CC_01",
        "service_name": "CadÚnico",
        "message": "Já separou os documentos necessários?",
        "options": [

            {
                "text": "Sim, já separei",
                "next step": "CU_CC_05"
            },

            {
                "text": "Não, ainda não",
                "next step": "CU_CC_02"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "CU_CC_02",
        "service_name": "CadÚnico",
        "message": "Você gostaria de saber quais são os documentos necessários?",
        "options": [

            {
                "text": "Sim, quero saber",
                "next step": "CU_CC_03"
            },

            {
                "text": "Não, obrigado",
                "next step": "CU_CC_05"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "CU_CC_03",
        "service_name": "CadÚnico",
        "message": "Separe RG, CPF e Certidão de nascimento ou casamento de todos os membros familiares, e um comprovante ou declaração de residência.",
        "next step": "CU_CC_05"

    },

    {

        "code": "CU_CC_05",
        "service_name": "CadÚnico",
        "message": "Quer ver o vídeo de como criar a sua conta?",
        "options": [

            {
                "text": "Sim, ver o vídeo",
                "next step": "CU_CC_04"
            },

            {
                "text": "Não, obrigado",
                "next step": "CU_CC_06"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "CU_CC_04",
        "service_name": "CadÚnico",
        "message": "Ótimo! Abaixo, você encontrará um vídeo com o passo a passo para criar sua conta no CadÚnico.",
        "video_path": "videos/Criar_conta_cadunico.mp4",
        "next step": "CU_CC_07"

    },

    {

        "code": "CU_CC_07",
        "service_name": "CadÚnico",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui. Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "CU_CC_08"
            },

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            },


        ]

    },

    {

        "code": "CU_CC_08",
        "service_name": "CadÚnico",
        "message": "Qual nota você daria para este tutorial?",
        "options": [

            {
                "text": "Enviar",
                "next step": "CU_CC_09"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "CU_CC_09",
        "service_name": "CadÚnico",
        "message": "Avaliação enviada com sucesso!",
        "show_with_next": True,
        "next step": "CU_CC_10"

    },

    {

        "code": "CU_CC_10",
        "service_name": "CadÚnico",
        "message": "Obrigado por ajudar a melhorar o Guia Fácil",
        "options": [

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            },


        ]

    },

    {

        "code": "CU_CC_06",
        "service_name": "CadÚnico",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui. Até a próxima!",
        "options": [

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            },


        ]

    },

]

for documento in criar_conta_steps:
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
