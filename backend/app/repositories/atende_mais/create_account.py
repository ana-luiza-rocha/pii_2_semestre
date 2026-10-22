from app.database.database import db
from app.repositories.collections import step

create_account_steps = [

    {

        "code": "AM_CC_01",
        "service_name": "Atende+",
        "message": "Você já está com a ficha médica?",
        "options": [

            {
                "text": "Sim, já tenho",
                "next step": "AM_CC_02"
            }, 

            {
                "text": "Não, ainda preciso",
                "next step": "AM_CC_05"
            }, 

            {
                "text": "Não sei",
                "next step": "AM_CC_06"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_CC_02",
        "service_name": "Atende+",
        "message": "Ótimo! Abaixo, você encontrará um vídeo com o passo a passo para criar sua conta no site do Atende+.",
        "video_path": "videos/Criar_conta_atende_mais.mp4",
        "next step": "AM_CC_03"

    },

    {

        "code": "AM_CC_03",
        "service_name": "Atende+",
        "message": "Precisa de ajuda com mais alguma coisa?",
        "options": [

            {
                "text": "Sim",
                "next step": "AM_CC_10"
            }, 

            {
                "text": "Não",
                "next step": "AM_CC_04"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_CC_04",
        "service_name": "Atende+",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui. Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "AM_CC_07"
            }, 

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            }, 


        ]

    },

    {

        "code": "AM_CC_05",
        "service_name": "Atende+",
        "message": "Quer ver como conseguir sua ficha médica?",
        "options": [

            {
                "text": "Sim, ver tutorial",
                "next step": "AM_OFM_01"
            }, 

            {
                "text": "Não, obrigado",
                "next step": "AM_CC_03"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_CC_06",
        "service_name": "Atende+",
        "message": "A Ficha de Avaliação Médica é um documento preenchido pelo médico com informações sobre sua condição de saúde e suas necessidades para usar o Atende+.",
        "next step": "AM_CC_05"

    },

    {

        "code": "AM_CC_07",
        "service_name": "Atende+",
        "message": "Qual nota você daria para este tutorial?",
        "options": [

            {
                "text": "Enviar",
                "next step": "AM_CC_08"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "AM_CC_08",
        "service_name": "Atende+",
        "message": "Avaliação enviada com sucesso!",
        "show_with_next": True,
        "next step": "AM_CC_09"

    },

    
    {

        "code": "AM_CC_09",
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

        "code": "AM_CC_10",
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

for documento in create_account_steps:
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
