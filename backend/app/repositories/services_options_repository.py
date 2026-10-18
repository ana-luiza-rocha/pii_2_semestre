from database import db

services_options = [
    
{

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

},

{

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

},

{

    "code": "FB_01",
    "service_name": "Sugestões e reclamações",
    "message": "O que você gostaria de fazer?",
    "options": [

        {
            "text": "Enviar uma sugestão",
            "next step": ""
        }, 

        {
            "text": "Fazer uma reclamação",
            "next step": ""
        }, 

        {
            "text": "Enviar um elogio",
            "next step": ""
        }, 

        {
            "text": "Voltar para a tela inicial",
            "next step": "MENU"
        },

    ]

}

]