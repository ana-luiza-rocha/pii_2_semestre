from database import db

services_options = {

    "code": "MI_01",
    "service_name": "Meu INSS",
    "message": "Olá! O que você deseja fazer no Meu INSS hoje?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": ""
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