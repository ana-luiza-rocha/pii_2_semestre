from app.database.database import db
from app.repositories.collections import step

get_medical_forms_steps = [

    {

        "code": "AM_OFM_01",
        "service_name": "Atende+",
        "message": "Você pode pegar sua ficha médica em um Posto de Atendimento da SPTrans",
        "next step": "AM_OFM_02"

    },

    {

        "code": "AM_OFM_02",
        "service_name": "Atende+",
        "message": "Quer encontrar um posto perto de você?",
        "options": [

            {
                "text": "Sim, por favor",
                "next step": "AM_OFM_03" 
            }, 

            {
                "text": "Não, obrigado",
                "next step": "AM_OFM_05"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_OFM_03",
        "service_name": "Atende+",
        "message": "A SPTrans tem um site onde você pode ver os endereços dos postos de atendimento disponíveis. Toque no botão abaixo para consultar.",
        "next step": "AM_OFM_04"

    },

    {

        "code": "AM_OFM_04",
        "service_name": "Atende+",
        "message": "Lembre-se de levar a ficha ao seu médico para preencher.",
        "next step": "AM_OFM_05"

    },

    {

        "code": "AM_OFM_05",
        "service_name": "Atende+",
        "message": "Precisa de ajuda com mais alguma coisa?",
        "options": [

            {
                "text": "Sim",
                "next step": "AM_OFM_10"
            }, 

            {
                "text": "Não",
                "next step": "AM_OFM_06"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "AM_OFM_06",
        "service_name": "Atende+",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui! Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "AM_OFM_07" 
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "AM_OFM_07",
        "service_name": "Atende+",
        "message": "Qual nota você daria para este tutorial?",
        "options": [

            {
                "text": "Enviar",
                "next step": "AM_OFM_08"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "AM_OFM_08",
        "service_name": "Atende+",
        "message": "Avaliação enviada com sucesso!",
        "next step": "AM_OFM_09"

    },

    
    {

        "code": "AM_OFM_09",
        "service_name": "Atende+",
        "message": "Obrigado por ajudar a melhorar o Guia Fácil",
        "options": [

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "AM_OFM_10",
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
    step.update_one(
        {"code": documento["code"]},
        {"$set": documento},
        upsert=True,
    )
