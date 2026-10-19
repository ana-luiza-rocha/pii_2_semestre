from database import db

step = db["step"]

atende_mais_steps = [

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

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
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
                "next step": "" #OPCAO MENU
            }, 

            {
                "text": "Não",
                "next step": "AM_OFM_06"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            },

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            }

        ]

    },

    {

        "code": "AM_OFM_06",
        "service_name": "Atende+",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui! Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "" # AVALIACAO
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            },
        ]

    }
]

