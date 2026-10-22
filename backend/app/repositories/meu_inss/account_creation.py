from app.database.database import db
from app.repositories.collections import step

account_creation_steps = [

    {

        "code": "MI_CC_01",
        "service_name": "Meu INSS",
        "message": "Você tem o Meu INSS no celular?",
        "options": [

            {
                "text": "Sim, já tenho",
                "next step": "MI_CC_02"
            }, 

            {
                "text": "Não tenho",
                "next step": "MI_CC_09"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "MI_CC_02",
        "service_name": "Meu INSS",
        "message": "Você já entrou na sua conta Gov.br?",
        "options": [

            {
                "text": "Sim, já entrei",
                "next step": "MI_CC_03"
            }, 

            {
                "text": "Ainda não",
                "next step": "MI_CC_07"
            },

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "MI_CC_03",
        "service_name": "Meu INSS",
        "message": "Precisa de ajuda com algum serviço do Meu INSS?",
        "options": [

            {
                "text": "Sim, preciso de ajuda",
                "next step": "MI_CC_04"
            }, 

            {
                "text": "Não, obrigado",
                "next step": "MI_CC_05"
            },

            {
                "text": "Voltar à pergunta anterior",
            },



        ]

    },

    {

        "code": "MI_CC_04",
        "service_name": "Meu INSS",
        "message": "Com o que você precisa de ajuda no Meu INSS?",
        "options": [

            {
                "text": "Criar uma conta",
                "next step": "MI_CC_01"
            }, 

            {
                "text": "Consultar um benefício",
                "next step": "" #o fluxo de benefício não existe ainda!
            }, 


        ]

    },

    {

        "code": "MI_CC_05",
        "service_name": "Meu INSS",
        "message": "Precisa de ajuda com mais alguma coisa?",
        "options": [

            {
                "text": "Sim",
                "next step": "MI_CC_15"
            }, 

            {
                "text": "Não",
                "next step": "MI_CC_06"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            },


        ]

    },

    {

        "code": "MI_CC_06",
        "service_name": "Meu INSS",
        "message": "Espero ter ajudado! Se precisar novamente, estarei por aqui. Até a próxima!",
        "options": [

            {
                "text": "Avaliar tutorial",
                "next step": "MI_CC_12" 
            }, 

            {
                "text": "Voltar para a página inicial",
                "next step": "MENU"
            }, 


        ]

    },

    {

        "code": "MI_CC_07",
        "service_name": "Meu INSS",
        "message": "Você precisa de ajuda para fazer login na sua conta do Gov.br?",
        "options": [

            {
                "text": "Sim, preciso de ajuda",
                "next step": "MI_CC_08"
            }, 

            {
                "text": "Não, consigo entrar",
                "next step": "MI_CC_03"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "MI_CC_08",
        "service_name": "Meu INSS",
        "message": "Ótimo! No vídeo, você verá passo a passo como entrar na sua conta Gov.br pelo aplicativo.",
        "video_path": "videos/Criar_conta_gov.mp4",
        "next step": "MI_CC_03"

    },

    {

        "code": "MI_CC_09",
        "service_name": "Meu INSS",
        "message": "Sem problemas! Vamos te ajudar a baixar o Meu INSS. Qual celular você usa?",
        "options": [

            {
                "text": "Android",
                "next step": "MI_CC_10"
            }, 

            {
                "text": "Apple",
                "next step": "MI_CC_11"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "MI_CC_10",
        "service_name": "Meu INSS",
        "message": "Certo! Abaixo, você encontrará um vídeo com o passo a passo para baixar o aplicativo Meu INSS em dispositivos Android.",
        "video_path": "videos/Baixar_meu_inss_android.mp4",
        "options": [

            {
                "text": "Continuar",
                "next step": "MI_CC_07"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "MI_CC_11",
        "service_name": "Meu INSS",
        "message": "Certo! Abaixo, você encontrará um vídeo com o passo a passo para baixar o aplicativo Meu INSS em dispositivos Apple.",
        "next step": "MI_CC_07"

    },

    {

        "code": "MI_CC_12",
        "service_name": "Meu INSS",
        "message": "Qual nota você daria para este tutorial?",
        "options": [

            {
                "text": "Enviar",
                "next step": "MI_CC_13"
            }, 

            {
                "text": "Voltar à pergunta anterior",
            }, 


        ]

    },

    {

        "code": "MI_CC_13",
        "service_name": "Atende+",
        "message": "Avaliação enviada com sucesso!",
        "show_with_next": True,
        "next step": "MI_CC_14"

    },

    
    {

        "code": "MI_CC_14",
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

        "code": "MI_CC_15",
        "service_name": "Meu INSS",
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

for documento in account_creation_steps:
    step.replace_one(
        {"code": documento["code"]},
        documento,
        upsert=True,
    )
