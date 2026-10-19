from database import db

services_options = {

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

