from database import db

services_options = {

    "code": "AM_1",
    "service_name": "Atende+",
    "message": "Olá! O que você deseja fazer no Atende+ hoje?",
    "options": [

        {
            "text": "Criar uma conta",
            "next step": "AM_2"
        }, 

        {
            "text": "Obter ficha médica",
            "next step": ""
        }, 

        {
            "text": "Voltar para a tela inicial",
            "next step": "MENU"
        },

    ]

}