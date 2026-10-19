from database import db

step = db["step"]

atende_mais_steps = [

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
                "next step": "MENU"
            },

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            },

        ]

    },

    {

        "code": "AM_CC_02",
        "service_name": "Atende+",
        "message": "Ótimo! Ao iniciar o vídeo, o site do Atende+ será aberto para você acompanhar o passo a passo. O vídeo continuará aparecendo em um tamanho menor enquanto você utiliza o site.",
        "next step": "AM_CC_03"

    },

    {

        "code": "AM_CC_03",
        "service_name": "Atende+",
        "message": "Precisa de ajuda com mais alguma coisa?",
        "options": [

            {
                "text": "Sim",
                "next step": "" #OPCAO MENU
            }, 

            {
                "text": "Não",
                "next step": "AM_CC_04"
            },

            {
                "text": "Voltar à pergunta anterior",
                "next step": "AM_CC_01"
            },

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
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
                "next step": "" # AVALIACAO
            }, 

            {
                "text": "Voltar à pergunta anterior",
                "next step": "AM_CC_03"
            }, 

            {
                "text": "Voltar para a tela inicial",
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
                "next step": "AM_CC_02"
            }, 

            {
                "text": "Não, obrigado",
                "next step": "AM_CC_03"
            }, 

            {
                "text": "Voltar à pergunta anterior",
                "next step": "AM_CC_01"
            },

            {
                "text": "Voltar para a tela inicial",
                "next step": "MENU"
            }

        ]

    },

    {

        "code": "AM_CC_06",
        "service_name": "Atende+",
        "message": "A Ficha de Avaliação Médica é um documento preenchido pelo médico com informações sobre sua condição de saúde e suas necessidades para usar o Atende+.",
        "next step": "AM_CC_05"

    }
]

