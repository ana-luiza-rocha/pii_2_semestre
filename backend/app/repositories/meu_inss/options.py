from database import db

meu_inss_options = {

    "code": "MI_01",
    "service_name": "Meu INSS",
    "message": "Olá! O que você deseja fazer no Meu INSS hoje?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": "MI_CC_01"
        }, 

        {
            "text": "Consultar um benefício",
            "next step": ""
        }, 

        {
            "text": "Voltar para a tela inicial",
            "next step": "MENU"
        },

    ]

}